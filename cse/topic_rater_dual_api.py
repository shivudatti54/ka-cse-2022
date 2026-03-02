#!/usr/bin/env python3
"""
VTU Content Pack Topic Rater

Modes:
  python rate_topics.py <topic-paths-file>          # Rate topics via APIs + generate reports
  python rate_topics.py --report-only <json-file>   # Generate HTML from existing JSON (no API calls)

APIs: Chutes (DeepSeek-R1, 671B) + MiniMax (M2.5, 456B)
"""

import asyncio
import argparse
import html as html_mod
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import aiohttp

# ── API Configuration ──────────────────────────────────────────────────────────
APIS = {
    "chutes": {
        "base_url": "https://llm.chutes.ai/v1/chat/completions",
        "api_key": "cpk_a744b82c5b9c4e8b9c7c8e1442e8d160.c3a84cdb26e850c9b8f358af872bca49.ymNhlwAf2nbhnTZJE620p8sv1aTgEGwx",
        "model": "deepseek-ai/DeepSeek-R1-TEE",
    },
    "minimax": {
        "base_url": "https://api.minimax.io/v1/chat/completions",
        "api_key": os.environ.get(
            "MINIMAX_API_KEY",
            "sk-cp-r--6hiKCzLgU9QbQREFxR4v336s2kP0vDCeb3x7-iNJxAAdDwQeXhInB8zgfwcduBNoBtQBSj33uci2eCKcCu7q4VjmMGWDhKYHXu_lpv1fmWctproM4cAg"
        ),
        "model": "MiniMax-M2.5",
    },
}

MAX_WORKERS = 25
TOPIC_FILES = ["read.md", "purpose.md", "mcqs.json", "flashcards.json",
               "questions.json", "memory.json", "visual.json"]

RATING_PROMPT = """\
You are an expert educational content reviewer for a VTU (Visvesvaraya Technological University) engineering study app.

You will be given all files from a single topic directory. Rate the topic on two dimensions:

1. **Coverage Rating** (1-10): How well does the content cover the topic?
   - Are all key concepts explained?
   - Is the depth appropriate for university-level study?
   - Are there enough MCQs, flashcards, and questions?
   - Are mnemonics and key points helpful?

2. **Content Quality Rating** (1-10): How good is the content itself?
   - Is the information accurate?
   - Is the writing clear and well-structured?
   - Are MCQ options well-crafted (no obvious answers, good distractors)?
   - Are flashcards effective for memorization?
   - Are explanations detailed enough?

Respond ONLY with valid JSON in this exact format (no markdown, no extra text):
{
  "coverage_rating": <1-10>,
  "coverage_remarks": "<brief explanation>",
  "content_quality_rating": <1-10>,
  "content_quality_remarks": "<brief explanation>",
  "file_ratings": {
    "read.md": {"rating": <1-10>, "remarks": "<brief>"},
    "purpose.md": {"rating": <1-10>, "remarks": "<brief>"},
    "mcqs.json": {"rating": <1-10>, "remarks": "<brief>"},
    "flashcards.json": {"rating": <1-10>, "remarks": "<brief>"},
    "questions.json": {"rating": <1-10>, "remarks": "<brief>"},
    "memory.json": {"rating": <1-10>, "remarks": "<brief>"},
    "visual.json": {"rating": <1-10>, "remarks": "<brief>"}
  },
  "suggestions": ["<improvement suggestion 1>", "<improvement suggestion 2>"]
}
"""


# ── Console Status ─────────────────────────────────────────────────────────────
class StatusTracker:
    def __init__(self, total: int, api_count: int):
        self.total = total
        self.api_count = api_count
        self.completed = 0
        self.failed = 0
        self.in_progress = 0
        self.lock = asyncio.Lock()
        self.start_time = time.time()

    async def start_topic(self, idx: int, name: str, api: str):
        async with self.lock:
            self.in_progress += 1
            elapsed = time.time() - self.start_time
            print(f"  [{self._progress()}] START  #{idx} | {api:7s} | {name} ({elapsed:.0f}s)")

    async def finish_topic(self, idx: int, name: str, api: str, success: bool):
        async with self.lock:
            self.in_progress -= 1
            if success:
                self.completed += 1
                tag = "DONE "
            else:
                self.failed += 1
                tag = "FAIL "
            elapsed = time.time() - self.start_time
            print(f"  [{self._progress()}] {tag}  #{idx} | {api:7s} | {name} ({elapsed:.0f}s)")

    def _progress(self):
        done = self.completed + self.failed
        return f"{done}/{self.total * self.api_count} done, {self.in_progress} active, {self.failed} failed"


# ── File Reading ───────────────────────────────────────────────────────────────
def read_topic_paths(filepath: str) -> list[tuple[int, str]]:
    """Parse topic paths file. Format: number→/path/to/topic"""
    topics = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "→" in line:
                parts = line.split("→", 1)
                idx = int(parts[0].strip())
                path = parts[1].strip()
            else:
                idx = len(topics) + 1
                path = line
            topics.append((idx, path))
    return topics


def load_topic_content(topic_path: str) -> str:
    """Load all files from a topic directory into a single string for the prompt."""
    parts = []
    topic_dir = Path(topic_path)
    topic_name = topic_dir.name

    parts.append(f"=== TOPIC: {topic_name} ===")
    parts.append(f"Path: {topic_path}\n")

    for fname in TOPIC_FILES:
        fpath = topic_dir / fname
        if fpath.exists():
            content = fpath.read_text(encoding="utf-8", errors="replace")
            if len(content) > 15000:
                content = content[:15000] + "\n... [TRUNCATED] ..."
            parts.append(f"--- FILE: {fname} ---")
            parts.append(content)
            parts.append("")
        else:
            parts.append(f"--- FILE: {fname} --- [MISSING]")
            parts.append("")

    return "\n".join(parts)


# ── API Call ───────────────────────────────────────────────────────────────────
async def call_api(session: aiohttp.ClientSession, api_name: str,
                   topic_content: str, retries: int = 2) -> dict | None:
    """Send topic content to an API and get the rating back."""
    api = APIS[api_name]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api['api_key']}",
    }

    payload = {
        "model": api["model"],
        "messages": [
            {"role": "system", "content": RATING_PROMPT},
            {"role": "user", "content": topic_content},
        ],
        "temperature": 0.1,
        "max_tokens": 2048,
    }

    for attempt in range(retries + 1):
        try:
            async with session.post(
                api["base_url"], headers=headers, json=payload, timeout=aiohttp.ClientTimeout(total=120)
            ) as resp:
                if resp.status != 200:
                    body = await resp.text()
                    if attempt < retries:
                        await asyncio.sleep(2 ** attempt)
                        continue
                    return {"error": f"HTTP {resp.status}: {body[:300]}"}

                data = await resp.json()
                content = data["choices"][0]["message"]["content"]

                # Strip DeepSeek-R1 <think>...</think> reasoning block
                content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL)

                # Strip markdown fences if present
                content = content.strip()
                if content.startswith("```"):
                    content = content.split("\n", 1)[1] if "\n" in content else content[3:]
                if content.endswith("```"):
                    content = content[:-3]
                content = content.strip()
                if content.startswith("json"):
                    content = content[4:].strip()

                rating = json.loads(content)
                rating["_model"] = api["model"]
                rating["_api"] = api_name
                return rating

        except json.JSONDecodeError as e:
            if attempt < retries:
                await asyncio.sleep(2 ** attempt)
                continue
            return {"error": f"JSON parse error: {e}", "raw_response": content[:500]}
        except asyncio.TimeoutError:
            if attempt < retries:
                await asyncio.sleep(2 ** attempt)
                continue
            return {"error": "Timeout after 120s"}
        except Exception as e:
            if attempt < retries:
                await asyncio.sleep(2 ** attempt)
                continue
            return {"error": str(e)}

    return {"error": "All retries exhausted"}


# ── Worker ─────────────────────────────────────────────────────────────────────
async def rate_topic(semaphore: asyncio.Semaphore, session: aiohttp.ClientSession,
                     idx: int, topic_path: str, api_name: str,
                     tracker: StatusTracker) -> dict:
    """Rate a single topic with a single API."""
    topic_name = Path(topic_path).name

    async with semaphore:
        await tracker.start_topic(idx, topic_name, api_name)

        try:
            topic_content = load_topic_content(topic_path)
            result = await call_api(session, api_name, topic_content)
            success = result is not None and "error" not in result
        except Exception as e:
            result = {"error": str(e)}
            success = False

        await tracker.finish_topic(idx, topic_name, api_name, success)

        return {
            "index": idx,
            "topic_path": topic_path,
            "topic_name": topic_name,
            "api": api_name,
            "model": APIS[api_name]["model"],
            "rating": result,
        }


# ── HTML Report Generator ─────────────────────────────────────────────────────
def _esc(text: str) -> str:
    """HTML-escape a string."""
    return html_mod.escape(str(text)) if text else ""


def _rating_cls(n) -> str:
    if n is None or not isinstance(n, (int, float)):
        return ""
    if n >= 8:
        return "high"
    if n >= 6:
        return "mid"
    return "low"


def _parse_path(path: str) -> tuple[str, str]:
    """Extract subject and module from a topic path."""
    m = re.search(r"/(sem-\d+)/([^/]+)/chapters/([^/]+)/", path)
    if m:
        return m.group(2), m.group(3)
    return "", ""


def generate_html_report(report: dict, html_path: Path):
    """Generate a fully standalone HTML report from the JSON data."""

    topics = report.get("topics", {})
    apis_info = report.get("apis", {})
    api_names = sorted(apis_info.keys())

    # ── Compute stats ──────────────────────────────────────────────────────
    by_subject: dict[str, dict] = {}
    totals: dict[str, dict] = {a: {"cov": [], "qual": []} for a in api_names}
    error_count = 0
    total_rated = 0

    for key in sorted(topics.keys(), key=lambda x: int(x)):
        t = topics[key]
        subject, module = _parse_path(t.get("topic_path", ""))
        if subject and subject not in by_subject:
            by_subject[subject] = {a: {"cov": [], "qual": []} for a in api_names}

        for api in api_names:
            r = (t.get("ratings", {}).get(api, {}) or {}).get("rating", {})
            if not r or "error" in r:
                error_count += 1
                continue
            total_rated += 1
            cov = r.get("coverage_rating")
            qual = r.get("content_quality_rating")
            if isinstance(cov, (int, float)):
                totals[api]["cov"].append(cov)
                if subject:
                    by_subject[subject][api]["cov"].append(cov)
            if isinstance(qual, (int, float)):
                totals[api]["qual"].append(qual)
                if subject:
                    by_subject[subject][api]["qual"].append(qual)

    def _avg(lst):
        return round(sum(lst) / len(lst), 1) if lst else 0

    # ── Build HTML ─────────────────────────────────────────────────────────
    lines = []
    w = lines.append

    w("<!DOCTYPE html>")
    w('<html lang="en">')
    w("<head>")
    w('  <meta charset="UTF-8">')
    w('  <meta name="viewport" content="width=device-width, initial-scale=1">')
    w(f"  <title>Topic Ratings Report</title>")
    w("  <style>")
    w("""    :root {
      --bg: #0f1419; --surface: #1a2332; --surface2: #243044;
      --text: #e6edf3; --text-muted: #8b949e; --accent: #58a6ff;
      --accent-dim: #388bfd66; --green: #3fb950; --amber: #d29922;
      --red: #f85149; --radius: 8px;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; background: var(--bg); color: var(--text); padding: 24px; line-height: 1.5; }
    .container { max-width: 1500px; margin: 0 auto; }
    h1 { font-size: 1.5rem; font-weight: 600; margin-bottom: 4px; }
    h2 { font-size: 1.15rem; font-weight: 600; margin: 24px 0 12px; color: var(--accent); }
    .subtitle { color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px; }

    /* Summary cards */
    .summary-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 24px; }
    .card { background: var(--surface); border-radius: var(--radius); padding: 16px; border: 1px solid var(--surface2); }
    .card .label { color: var(--text-muted); font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px; }
    .card .value { font-size: 1.25rem; font-weight: 600; }
    .card .value.rating { color: var(--accent); }
    .card .model-tag { font-size: 0.75rem; color: var(--text-muted); margin-top: 4px; padding: 3px 8px; background: var(--surface2); border-radius: 4px; display: inline-block; }

    /* Subject stats */
    .subject-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 12px; margin-bottom: 24px; }
    .subj-card { background: var(--surface); padding: 14px; border-radius: var(--radius); border: 1px solid var(--surface2); }
    .subj-card .name { font-size: 0.85rem; font-weight: 600; margin-bottom: 6px; word-break: break-word; }
    .subj-card .stats { font-size: 0.8rem; color: var(--text-muted); line-height: 1.7; }
    .subj-card .bar-wrap { height: 6px; background: var(--surface2); border-radius: 3px; margin-top: 6px; overflow: hidden; }
    .subj-card .bar-fill { height: 100%; border-radius: 3px; }

    /* Main table */
    table { width: 100%; border-collapse: collapse; background: var(--surface); border-radius: var(--radius); overflow: hidden; border: 1px solid var(--surface2); font-size: 0.88rem; }
    th, td { padding: 10px 14px; text-align: left; border-bottom: 1px solid var(--surface2); }
    th { background: var(--surface2); color: var(--text-muted); font-size: 0.78rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em; position: sticky; top: 0; z-index: 1; }
    tr:hover > td { background: rgba(56,139,253,0.06); }
    .topic-name { font-weight: 500; }
    .topic-path { font-size: 0.75rem; color: var(--text-muted); max-width: 300px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .r { font-weight: 600; display: inline-block; min-width: 1.4em; text-align: center; }
    .r.high { color: var(--green); }
    .r.mid { color: var(--amber); }
    .r.low { color: var(--red); }
    .r.err { color: var(--red); font-weight: 400; font-size: 0.8rem; }
    td.api-label { font-size: 0.75rem; color: var(--text-muted); }

    /* Expandable details */
    details { margin: 0; }
    details summary { cursor: pointer; color: var(--accent); font-size: 0.82rem; padding: 2px 0; list-style: none; }
    details summary::-webkit-details-marker { display: none; }
    details summary::before { content: '▸ '; }
    details[open] summary::before { content: '▾ '; }
    .detail-box { background: var(--bg); border-radius: var(--radius); padding: 14px; margin-top: 8px; }
    .detail-box .api-section { margin-bottom: 16px; }
    .detail-box .api-section:last-child { margin-bottom: 0; }
    .detail-box h4 { font-size: 0.85rem; color: var(--accent); margin-bottom: 8px; font-weight: 600; }
    .detail-box .remark { font-size: 0.82rem; color: var(--text-muted); margin-bottom: 6px; }
    .detail-box .remark strong { color: var(--text); font-weight: 500; }
    .file-tbl { width: 100%; font-size: 0.82rem; background: transparent; border: none; margin: 8px 0; }
    .file-tbl td, .file-tbl th { padding: 4px 10px; border-bottom: 1px solid var(--surface2); }
    .file-tbl th { background: transparent; text-transform: none; font-size: 0.78rem; }
    .file-tbl td:first-child { font-family: ui-monospace, monospace; font-size: 0.8rem; }
    .suggestions { margin-top: 8px; }
    .suggestions li { font-size: 0.82rem; color: var(--text-muted); margin-bottom: 3px; margin-left: 16px; }
    .error-text { color: var(--red); font-size: 0.82rem; }

    @media (max-width: 900px) { body { padding: 12px; } th, td { padding: 8px; } }""")
    w("  </style>")
    w("</head>")
    w("<body>")
    w('<div class="container">')

    # ── Header ─────────────────────────────────────────────────────────────
    source = Path(report.get("source_file", "")).stem
    w(f"<h1>Topic Ratings Report</h1>")
    api_labels = []
    for a in api_names:
        model = apis_info.get(a, {}).get("model", a)
        api_labels.append(f"{a} ({model})")
    w(f'<p class="subtitle">{_esc(source)} &mdash; {" &bull; ".join(api_labels)}</p>')

    # ── Summary cards ──────────────────────────────────────────────────────
    w('<div class="summary-grid">')
    w(f'<div class="card"><div class="label">Total topics</div><div class="value">{report.get("total_topics", len(topics))}</div></div>')
    t_sec = report.get("total_time_seconds")
    w(f'<div class="card"><div class="label">Time</div><div class="value">{t_sec:.1f}s</div></div>' if t_sec else "")
    w(f'<div class="card"><div class="label">Generated</div><div class="value" style="font-size:0.9rem">{_esc(report.get("generated_at", ""))}</div></div>')
    w(f'<div class="card"><div class="label">Errors</div><div class="value" style="color:{"var(--red)" if error_count else "var(--green)"}">{error_count}</div></div>')

    for api in api_names:
        model = apis_info.get(api, {}).get("model", api)
        ca = _avg(totals[api]["cov"])
        qa = _avg(totals[api]["qual"])
        w(f'<div class="card"><div class="label">{_esc(api)} avg (Cov / Qual)</div>')
        w(f'  <div class="value rating">{ca} / {qa}</div>')
        w(f'  <div class="model-tag">{_esc(model)}</div>')
        w("</div>")
    w("</div>")

    # ── Subject breakdown ──────────────────────────────────────────────────
    if by_subject:
        w("<h2>Subject Averages</h2>")
        w('<div class="subject-grid">')
        for subj in sorted(by_subject.keys()):
            sd = by_subject[subj]
            # count topics in this subject
            topic_count = max(len(sd[api_names[0]]["cov"]) if api_names else 0, 1)
            stat_parts = []
            overall_avg = 0
            n_avgs = 0
            for api in api_names:
                ca = _avg(sd[api]["cov"])
                qa = _avg(sd[api]["qual"])
                stat_parts.append(f"{api}: Cov {ca} / Qual {qa}")
                if sd[api]["cov"]:
                    overall_avg += ca
                    n_avgs += 1
                if sd[api]["qual"]:
                    overall_avg += qa
                    n_avgs += 1
            bar_pct = (overall_avg / n_avgs * 10) if n_avgs else 0
            bar_color = "var(--green)" if bar_pct >= 80 else ("var(--amber)" if bar_pct >= 60 else "var(--red)")

            w('<div class="subj-card">')
            w(f'  <div class="name">{_esc(subj)}</div>')
            w(f'  <div class="stats">{topic_count} topics<br>{"<br>".join(stat_parts)}</div>')
            w(f'  <div class="bar-wrap"><div class="bar-fill" style="width:{bar_pct:.0f}%;background:{bar_color}"></div></div>')
            w("</div>")
        w("</div>")

    # ── Main table ─────────────────────────────────────────────────────────
    w("<h2>All Topics</h2>")
    w("<table>")
    w("<thead><tr>")
    w("  <th>#</th><th>Topic</th><th>Subject / Module</th>")
    for api in api_names:
        model = apis_info.get(api, {}).get("model", "")
        short_model = model.split("/")[-1] if "/" in model else model
        w(f'  <th>{_esc(api)}<br><span style="font-weight:400;text-transform:none;font-size:0.7rem">{_esc(short_model)}</span><br>Cov / Qual</th>')
    w("  <th>Details</th>")
    w("</tr></thead>")
    w("<tbody>")

    for key in sorted(topics.keys(), key=lambda x: int(x)):
        t = topics[key]
        name = t.get("topic_name", "")
        path = t.get("topic_path", "")
        subject, module = _parse_path(path)
        short_path = re.sub(r"^.*/sem-\d+/", "", path)

        w("<tr>")
        w(f"  <td>{key}</td>")
        w(f'  <td><div class="topic-name">{_esc(name)}</div><div class="topic-path" title="{_esc(path)}">{_esc(short_path)}</div></td>')
        w(f'  <td><div>{_esc(subject)}</div><div class="topic-path">{_esc(module)}</div></td>')

        for api in api_names:
            rating_data = (t.get("ratings", {}).get(api, {}) or {})
            r = rating_data.get("rating", {})
            if not r or "error" in r:
                err_msg = r.get("error", "No data") if r else "No data"
                w(f'  <td><span class="r err" title="{_esc(err_msg)}">ERR</span></td>')
            else:
                cov = r.get("coverage_rating")
                qual = r.get("content_quality_rating")
                w(f'  <td><span class="r {_rating_cls(cov)}">{cov if cov is not None else "?"}</span>'
                  f' / <span class="r {_rating_cls(qual)}">{qual if qual is not None else "?"}</span></td>')

        # Details column
        w("  <td>")
        w("    <details><summary>View</summary>")
        w('    <div class="detail-box">')

        for api in api_names:
            rating_data = (t.get("ratings", {}).get(api, {}) or {})
            r = rating_data.get("rating", {})
            model = rating_data.get("model", apis_info.get(api, {}).get("model", api))

            w(f'    <div class="api-section">')
            w(f'      <h4>{_esc(api)} &mdash; {_esc(model)}</h4>')

            if not r or "error" in r:
                err_msg = r.get("error", "No data") if r else "No data"
                w(f'      <p class="error-text">{_esc(err_msg)}</p>')
                w("    </div>")
                continue

            cov_rem = r.get("coverage_remarks", "")
            qual_rem = r.get("content_quality_remarks", "")
            w(f'      <p class="remark"><strong>Coverage ({r.get("coverage_rating", "?")}/10):</strong> {_esc(cov_rem)}</p>')
            w(f'      <p class="remark"><strong>Quality ({r.get("content_quality_rating", "?")}/10):</strong> {_esc(qual_rem)}</p>')

            file_ratings = r.get("file_ratings", {})
            if file_ratings:
                w('      <table class="file-tbl"><thead><tr><th>File</th><th>Rating</th><th>Remarks</th></tr></thead><tbody>')
                for fname, fr in file_ratings.items():
                    fr_rating = fr.get("rating") if isinstance(fr, dict) else None
                    fr_remarks = fr.get("remarks", "") if isinstance(fr, dict) else ""
                    w(f'      <tr><td>{_esc(fname)}</td>'
                      f'<td><span class="r {_rating_cls(fr_rating)}">{fr_rating if fr_rating is not None else "?"}</span></td>'
                      f'<td>{_esc(fr_remarks)}</td></tr>')
                w("      </tbody></table>")

            suggestions = r.get("suggestions", [])
            if suggestions:
                w('      <div class="suggestions"><strong style="font-size:0.82rem">Suggestions:</strong><ul>')
                for s in suggestions:
                    w(f"        <li>{_esc(s)}</li>")
                w("      </ul></div>")

            w("    </div>")

        w("    </div>")
        w("    </details>")
        w("  </td>")
        w("</tr>")

    w("</tbody>")
    w("</table>")

    w("</div>")  # container
    w("</body>")
    w("</html>")

    html_path.write_text("\n".join(lines), encoding="utf-8")
    return html_path


# ── Main ───────────────────────────────────────────────────────────────────────
async def main():
    parser = argparse.ArgumentParser(description="VTU Content Pack Topic Rater")
    parser.add_argument("paths_file", nargs="?", help="Topic paths file")
    parser.add_argument("--report-only", dest="report_only", help="Generate HTML from an existing JSON report")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--minimax-only", action="store_true", help="Rate topics using only MiniMax")
    group.add_argument("--chutes-only", action="store_true", help="Rate topics using only Chutes")
    args = parser.parse_args()

    # ── Report-only mode ───────────────────────────────────────────────────
    if args.report_only:
        json_file = args.report_only
        if not os.path.exists(json_file):
            print(f"Error: File not found: {json_file}")
            sys.exit(1)
        with open(json_file) as f:
            report = json.load(f)
        html_path = Path(json_file).with_suffix(".html")
        generate_html_report(report, html_path)
        print(f"  HTML report generated: {html_path}")
        return

    # ── Normal mode ────────────────────────────────────────────────────────
    if not args.paths_file:
        parser.print_help()
        sys.exit(1)

    paths_file = args.paths_file
    if not os.path.exists(paths_file):
        print(f"Error: File not found: {paths_file}")
        sys.exit(1)

    if args.minimax_only:
        selected_apis = ["minimax"]
    elif args.chutes_only:
        selected_apis = ["chutes"]
    else:
        selected_apis = list(APIS.keys())

    topics = read_topic_paths(paths_file)
    print(f"\n{'='*70}")
    print(f"  VTU Content Rater")
    print(f"  Topics: {len(topics)}")
    print(f"  APIs: {', '.join(f'{k} ({APIS[k]['model']})' for k in selected_apis)}")
    print(f"  Workers: {MAX_WORKERS}")
    print(f"  Total jobs: {len(topics) * len(selected_apis)}")
    print(f"{'='*70}\n")

    tracker = StatusTracker(len(topics), len(selected_apis))
    semaphore = asyncio.Semaphore(MAX_WORKERS)

    connector = aiohttp.TCPConnector(limit=MAX_WORKERS + 5)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for idx, topic_path in topics:
            for api_name in selected_apis:
                tasks.append(rate_topic(semaphore, session, idx, topic_path, api_name, tracker))

        results = await asyncio.gather(*tasks)

    # ── Build report ───────────────────────────────────────────────────────
    elapsed = time.time() - tracker.start_time

    # Group results by topic
    by_topic: dict[int, dict] = {}
    for r in results:
        idx = r["index"]
        if idx not in by_topic:
            by_topic[idx] = {"topic_name": r["topic_name"], "topic_path": r["topic_path"], "ratings": {}}
        by_topic[idx]["ratings"][r["api"]] = {
            "model": r["model"],
            "rating": r["rating"],
        }

    # Save raw JSON report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = Path(paths_file).stem
    report_dir = Path(paths_file).parent / "reports"
    report_dir.mkdir(exist_ok=True)

    json_path = report_dir / f"{base_name}_ratings_{timestamp}.json"
    report = {
        "generated_at": datetime.now().isoformat(),
        "source_file": paths_file,
        "apis": {k: {"model": APIS[k]["model"], "base_url": APIS[k]["base_url"]} for k in selected_apis},
        "total_topics": len(topics),
        "total_time_seconds": round(elapsed, 1),
        "topics": dict(sorted(by_topic.items())),
    }
    with open(json_path, "w") as f:
        json.dump(report, f, indent=2)

    # Generate HTML report
    html_path = json_path.with_suffix(".html")
    generate_html_report(report, html_path)

    # Print summary table
    print(f"\n{'='*70}")
    print(f"  RATING SUMMARY")
    print(f"  Time: {elapsed:.0f}s | Topics: {len(topics)} | Failed: {tracker.failed}")
    print(f"{'='*70}")
    print(f"  {'#':>3}  {'Topic':<40} {'API':>7} {'Model':<25} {'Cov':>4} {'Qual':>4}")
    print(f"  {'-'*3}  {'-'*40} {'-'*7} {'-'*25} {'-'*4} {'-'*4}")

    cov_totals = {api: [] for api in selected_apis}
    qual_totals = {api: [] for api in selected_apis}

    for idx in sorted(by_topic.keys()):
        entry = by_topic[idx]
        name = entry["topic_name"][:40]
        for api_name, data in entry["ratings"].items():
            rating = data["rating"]
            model = data["model"]
            if "error" in rating:
                print(f"  {idx:>3}  {name:<40} {api_name:>7} {model:<25} {'ERR':>4} {'ERR':>4}")
            else:
                cov = rating.get("coverage_rating", "?")
                qual = rating.get("content_quality_rating", "?")
                print(f"  {idx:>3}  {name:<40} {api_name:>7} {model:<25} {cov:>4} {qual:>4}")
                if isinstance(cov, (int, float)):
                    cov_totals[api_name].append(cov)
                if isinstance(qual, (int, float)):
                    qual_totals[api_name].append(qual)

    print(f"\n  {'AVERAGES':>3}  {'':40}", end="")
    for api_name in selected_apis:
        cov_avg = sum(cov_totals[api_name]) / len(cov_totals[api_name]) if cov_totals[api_name] else 0
        qual_avg = sum(qual_totals[api_name]) / len(qual_totals[api_name]) if qual_totals[api_name] else 0
        print(f"\n       {'':40} {api_name:>7} {'avg':<25} {cov_avg:>4.1f} {qual_avg:>4.1f}", end="")

    print(f"\n\n  JSON report: {json_path}")
    print(f"  HTML report: {html_path}")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    asyncio.run(main())
