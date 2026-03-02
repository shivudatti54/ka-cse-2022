#!/usr/bin/env python3
"""
Automated Content Quality Pipeline

Stages:
  1. SCAN     — File completeness (9 files exist, non-empty, valid JSON)
  2. RATE     — LLM-rate each topic (relevance, coverage, quality, tier match)
  3. REPORT   — JSON + HTML report (pre-fix)
  4. CLASSIFY — PASS / FIX_FILES / WRONG_SUBJECT / WRONG_TIER / LOW_QUALITY
  5. FIX      — Regenerate/adapt broken topics via MiniMax API (--fix only)
  6. REPORT   — Updated JSON + HTML report (post-fix)

Usage:
  python3 quality_gate.py <pack> --scan-only
  python3 quality_gate.py <pack> --level standard
  python3 quality_gate.py <pack> --level standard --resume
  python3 quality_gate.py <pack> --level standard --fix
  python3 quality_gate.py <pack> --report-only ratings.json
"""

import argparse
import asyncio
import html as html_mod
import json
import os
import re
import ssl
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path
from threading import Lock

try:
    import aiohttp
    HAS_AIOHTTP = True
except ImportError:
    HAS_AIOHTTP = False

# ── Configuration ─────────────────────────────────────────────────────────
APIS = {
    "minimax": {
        "base_url": "https://api.minimax.io/v1/chat/completions",
        "api_key": os.environ.get(
            "MINIMAX_API_KEY",
            "sk-cp-r--6hiKCzLgU9QbQREFxR4v336s2kP0vDCeb3x7-iNJxAAdDwQeXhInB8zgfwcduBNoBtQBSj33uci2eCKcCu7q4VjmMGWDhKYHXu_lpv1fmWctproM4cAg",
        ),
        "model": "MiniMax-M2.5",
    },
    "gpt-oss": {
        "base_url": "https://llm.chutes.ai/v1/chat/completions",
        "api_key": "cpk_a744b82c5b9c4e8b9c7c8e1442e8d160.c3a84cdb26e850c9b8f358af872bca49.ymNhlwAf2nbhnTZJE620p8sv1aTgEGwx",
        "model": "openai/gpt-oss-120b-TEE",
    },
    "deepseek-v3": {
        "base_url": "https://llm.chutes.ai/v1/chat/completions",
        "api_key": "cpk_a744b82c5b9c4e8b9c7c8e1442e8d160.c3a84cdb26e850c9b8f358af872bca49.ymNhlwAf2nbhnTZJE620p8sv1aTgEGwx",
        "model": "deepseek-ai/DeepSeek-V3.2-TEE",
    },
}
FIX_API = "minimax"  # Fix stage always uses MiniMax (better for generation)

TIMEOUT = 180
MAX_TOKENS_RATE = 2048
MAX_TOKENS_GEN = 8192
TEMPERATURE_RATE = 0.1
TEMPERATURE_GEN = 0.3
DEFAULT_WORKERS = 25
RETRIES = 2

EXPECTED_FILES = [
    "read.md", "purpose.md", "summary.md",
    "code.json", "flashcards.json", "mcqs.json",
    "memory.json", "questions.json", "visual.json",
]
MD_FILES = {"read.md", "purpose.md", "summary.md"}
JSON_FILES = {"code.json", "flashcards.json", "mcqs.json", "memory.json", "questions.json", "visual.json"}
MD_MIN_BYTES = 50
JSON_MIN_BYTES = 20

progress_lock = Lock()

# ── Tier Templates ────────────────────────────────────────────────────────
TIER_TEMPLATES = {
    "foundation": {
        "name": "Foundation", "programs": "Diploma",
        "language": "Simple, clear language. Everyday analogies. No jargon.",
        "depth": "Basics only. Practical how-to focus. No proofs.",
        "mcq_style": "Easy — direct recall, single-concept",
        "read_length": "100-150 lines",
    },
    "foundation_plus": {
        "name": "Foundation+", "programs": "BSc, BCA",
        "language": "Accessible academic. Technical terms explained.",
        "depth": "Conceptual + moderate theory. Some formal notation.",
        "mcq_style": "Medium — understanding and application",
        "read_length": "150-200 lines",
    },
    "standard": {
        "name": "Standard", "programs": "B.Tech, MSc, MCA",
        "language": "Formal academic. Technical vocabulary expected.",
        "depth": "Thorough theory with proofs where needed.",
        "mcq_style": "Hard — application, analysis, numerical problems",
        "read_length": "200-250 lines",
    },
    "advanced": {
        "name": "Advanced", "programs": "M.Tech",
        "language": "Formal, research-oriented. Dense academic.",
        "depth": "Deep theory, formal proofs, complexity analysis, research refs.",
        "mcq_style": "Hardest — evaluation, synthesis, edge cases",
        "read_length": "250+ lines",
    },
}

# ── Subject Categories ────────────────────────────────────────────────────
def get_subject_category(subject_slug: str) -> str:
    slug = subject_slug.lower()
    math_kw = ["math", "calculus", "algebra", "probability", "statistics", "numerical", "discrete"]
    if any(k in slug for k in math_kw):
        return "math_heavy"
    theory_kw = ["theory-of-computation", "automata", "compiler", "formal-language"]
    if any(k in slug for k in theory_kw):
        return "cs_theory"
    domain_kw = ["management", "economics", "professional-ethics", "constitution"]
    if any(k in slug for k in domain_kw):
        return "domain_specific"
    return "cs_core"


# ── Context Extraction (reused from topic_rater / content_generator) ──────
def _slug_to_title(slug: str) -> str:
    cleaned = re.sub(r'^[a-z]{2,5}\d{3}[a-z]?-', '', slug)
    return cleaned.replace('-', ' ').title()


def get_topic_context(topic_path: str) -> dict:
    topic_dir = Path(topic_path)
    topic_slug = topic_dir.name
    parts = topic_dir.parts

    ctx = {
        'topic': topic_slug.replace('-', ' ').title(),
        'topic_slug': topic_slug,
        'module': '', 'subject': '', 'semester': '',
        'subject_slug': '', 'sibling_topics': [],
    }

    topics_idx = None
    for i, part in enumerate(parts):
        if part == "topics":
            topics_idx = i
            break

    if not topics_idx or topics_idx < 2:
        return ctx

    module_slug = parts[topics_idx - 1]
    subject_slug = parts[topics_idx - 2] if topics_idx >= 2 else ""
    ctx['subject_slug'] = subject_slug

    # Module _index.json
    module_dir = topic_dir.parent.parent
    module_index = module_dir / '_index.json'
    if module_index.exists():
        try:
            mdata = json.loads(module_index.read_text())
            ctx['module'] = mdata.get('chapterTitle', mdata.get('title', _slug_to_title(module_slug)))
            for t in mdata.get('topics', []):
                if t.get('id') == topic_slug:
                    ctx['topic'] = t.get('title', ctx['topic'])
                else:
                    ctx['sibling_topics'].append(t.get('title', t.get('id', '')))
        except (json.JSONDecodeError, IOError):
            ctx['module'] = _slug_to_title(module_slug)
    else:
        ctx['module'] = _slug_to_title(module_slug)

    # Subject _index.json
    subject_dir = module_dir.parent
    subject_index = subject_dir / '_index.json'
    if subject_index.exists():
        try:
            sdata = json.loads(subject_index.read_text())
            ctx['subject'] = sdata.get('subjectName', sdata.get('title', _slug_to_title(subject_slug)))
            for ch in sdata.get('chapters', []):
                if ch.get('id') == module_slug:
                    ctx['module'] = ch.get('title', ctx['module'])
                    break
        except (json.JSONDecodeError, IOError):
            ctx['subject'] = _slug_to_title(subject_slug)
    else:
        ctx['subject'] = _slug_to_title(subject_slug)

    # Semester from path
    sem_dir = subject_dir.parent
    ctx['semester'] = sem_dir.name.replace('-', ' ').title() if 'sem' in sem_dir.name else ''

    return ctx


# ── API Call (sync urllib, retries, <think> strip) ────────────────────────
def call_api(messages: list, label: str, max_tokens: int = MAX_TOKENS_RATE,
             temperature: float = TEMPERATURE_RATE, api_name: str = "minimax") -> str:
    api = APIS[api_name]
    timeout = 240 if api_name in ("gpt-oss", "deepseek-v3") else TIMEOUT

    payload = json.dumps({
        "model": api["model"],
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": messages,
    }).encode()

    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        api["base_url"], data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api['api_key']}",
        },
        method="POST",
    )

    for attempt in range(RETRIES + 1):
        try:
            start = time.time()
            resp = urllib.request.urlopen(req, timeout=timeout, context=ctx)
            result = json.loads(resp.read().decode())
            elapsed = time.time() - start
            print(f"  [{label}] API responded in {elapsed:.1f}s")

            message = result.get("choices", [{}])[0].get("message", {})
            text = message.get("content", "") or message.get("reasoning_content", "")

            # Strip <think> tags
            if '<think>' in text and '</think>' in text:
                end = text.find('</think>')
                if end != -1:
                    text = text[end + 8:]

            return text.strip()
        except Exception as e:
            if attempt < RETRIES:
                time.sleep(2 ** attempt)
                continue
            print(f"  [{label}] FAILED after {RETRIES + 1} attempts: {e}")
            raise


async def call_api_async(session: 'aiohttp.ClientSession', messages: list, label: str,
                         max_tokens: int = MAX_TOKENS_RATE, temperature: float = TEMPERATURE_RATE,
                         api_name: str = "minimax") -> str:
    """Async version of call_api using aiohttp for the RATE stage."""
    api = APIS[api_name]
    timeout_s = 240 if api_name in ("gpt-oss", "deepseek-v3") else TIMEOUT

    payload = {
        "model": api["model"],
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": messages,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api['api_key']}",
    }

    for attempt in range(RETRIES + 1):
        try:
            start = time.time()
            async with session.post(
                api["base_url"], json=payload, headers=headers,
                timeout=aiohttp.ClientTimeout(total=timeout_s),
                ssl=ssl.create_default_context(),
            ) as resp:
                result = await resp.json()
            elapsed = time.time() - start
            print(f"  [{label}] API responded in {elapsed:.1f}s")

            message = result.get("choices", [{}])[0].get("message", {})
            text = message.get("content", "") or message.get("reasoning_content", "")

            # Strip <think> tags
            if '<think>' in text and '</think>' in text:
                end = text.find('</think>')
                if end != -1:
                    text = text[end + 8:]

            return text.strip()
        except Exception as e:
            if attempt < RETRIES:
                await asyncio.sleep(2 ** attempt)
                continue
            print(f"  [{label}] FAILED after {RETRIES + 1} attempts: {e}")
            raise


def parse_json_response(text: str) -> dict:
    cleaned = text.strip()
    # Strip markdown fences
    if cleaned.startswith("```"):
        nl = cleaned.find("\n")
        if nl != -1:
            cleaned = cleaned[nl + 1:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        cleaned = cleaned.strip()
    # Extract outermost JSON object
    first = cleaned.find("{")
    last = cleaned.rfind("}")
    if first != -1 and last != -1 and first < last:
        cleaned = cleaned[first:last + 1]
    return json.loads(cleaned)


# ── Stage 1: SCAN ────────────────────────────────────────────────────────
def discover_topics(pack_path: Path) -> list[str]:
    topics = []
    for root, dirs, files in os.walk(pack_path):
        if Path(root).parent.name == "topics":
            topics.append(root)
    topics.sort()
    return topics


CJK_RE = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]')
LLM_PREAMBLE_RE = re.compile(r'^(Of course|Sure|Certainly)[.\s!]', re.IGNORECASE)
AUDIENCE_RE = re.compile(r'B\.?Tech|MSc/MCA|for B\.Tech', re.IGNORECASE)


def scan_topic(topic_path: str) -> dict:
    topic_dir = Path(topic_path)
    result = {"missing": [], "empty": [], "invalid_json": [], "content_issues": [], "ok": True}

    for fname in EXPECTED_FILES:
        fpath = topic_dir / fname
        if not fpath.exists():
            result["missing"].append(fname)
            continue

        size = fpath.stat().st_size
        min_bytes = MD_MIN_BYTES if fname in MD_FILES else JSON_MIN_BYTES
        if size < min_bytes:
            result["empty"].append(fname)
            continue

        # Content quality checks on text files
        if fname in MD_FILES:
            text = fpath.read_text(encoding="utf-8", errors="replace")
            if CJK_RE.search(text):
                result["content_issues"].append(f"{fname}: contains Chinese/CJK characters")
            if LLM_PREAMBLE_RE.match(text.strip()):
                result["content_issues"].append(f"{fname}: starts with LLM preamble")
            if fname == "purpose.md" and AUDIENCE_RE.search(text):
                result["content_issues"].append(f"{fname}: contains audience mentions (B.Tech/MSc/MCA)")

        if fname in JSON_FILES:
            try:
                raw = fpath.read_text(encoding="utf-8", errors="replace")
                data = json.loads(raw)
                # Check topicId matches directory slug (only for dict-shaped files)
                if isinstance(data, dict):
                    topic_id = data.get("topicId")
                    if topic_id and topic_id != topic_dir.name:
                        result["invalid_json"].append(f"{fname}: topicId mismatch ({topic_id} != {topic_dir.name})")
                # Check for Chinese characters in JSON content
                if CJK_RE.search(raw):
                    result["content_issues"].append(f"{fname}: contains Chinese/CJK characters")
            except json.JSONDecodeError as e:
                result["invalid_json"].append(f"{fname}: {e}")

    result["ok"] = not (result["missing"] or result["empty"] or result["invalid_json"])
    return result


# ── Stage 2: RATE ─────────────────────────────────────────────────────────
RATING_PROMPT_TEMPLATE = """\
You are an expert educational content reviewer for a university study app.

CONTEXT: This content is for {tier_name} level students ({programs}).
These students need {tier_depth}
The language style should be: {tier_language}

Rate this topic on FOUR dimensions. For EACH dimension, provide a DETAILED remark
(2-3 sentences) explaining your score — what is good, what is wrong, and what specifically
needs to change. Vague remarks like "good" or "needs improvement" are NOT acceptable.

1. **Subject Relevance** (1-10) — Does content match the stated subject and topic?
   - Use sibling topics for disambiguation.
   - Score 1-3 if content is about a COMPLETELY DIFFERENT subject/domain.
   - Score 4-6 if partially relevant with significant off-topic sections.
   - Score 7-10 if properly aligned.

2. **Coverage** (1-10) — Are key concepts covered with appropriate depth for {programs} students?
   - Does it cover what a {tier_name}-level exam would expect?
   - Are there missing subtopics, definitions, or examples?

3. **Content Quality** (1-10) — Accuracy, clarity, well-crafted MCQs?
   - Are MCQs at {tier_mcq_style} level?
   - Are explanations clear and error-free?

4. **Tier Appropriateness** (1-10) — Is the depth right for {tier_name} ({programs})?
   Expected depth: {tier_depth}
   Expected language: {tier_language}
   Expected MCQ style: {tier_mcq_style}
   Expected read.md length: {tier_read_length}

Respond ONLY with valid JSON (no markdown fences, no extra text):
{{
  "relevance": <1-10>,
  "relevance_remarks": "<2-3 sentence detailed explanation>",
  "coverage": <1-10>,
  "coverage_remarks": "<2-3 sentence detailed explanation>",
  "quality": <1-10>,
  "quality_remarks": "<2-3 sentence detailed explanation>",
  "tier": <1-10>,
  "tier_remarks": "<2-3 sentence detailed explanation>",
  "suggestions": ["<specific actionable suggestion 1>", "<specific actionable suggestion 2>"]
}}"""


def build_rating_prompt(level: str) -> str:
    t = TIER_TEMPLATES[level]
    return RATING_PROMPT_TEMPLATE.format(
        tier_name=t["name"], programs=t["programs"],
        tier_depth=t["depth"], tier_language=t["language"],
        tier_mcq_style=t["mcq_style"], tier_read_length=t["read_length"],
    )


def load_topic_content_for_rating(topic_path: str) -> str:
    topic_dir = Path(topic_path)
    ctx = get_topic_context(topic_path)
    siblings = ", ".join(ctx.get('sibling_topics', [])) or "(none)"

    parts = [
        f"SUBJECT: {ctx['subject']}",
        f"MODULE: {ctx['module']}",
        f"TOPIC: {ctx['topic']}",
        f"SEMESTER: {ctx['semester']}",
        f"SIBLING TOPICS: {siblings}",
        "",
    ]

    # read.md (first 3000 chars)
    read_path = topic_dir / "read.md"
    if read_path.exists():
        content = read_path.read_text(encoding="utf-8", errors="replace")
        parts.append(f"--- read.md (first 3000 chars) ---")
        parts.append(content[:3000])
    else:
        parts.append("--- read.md --- [MISSING]")

    # First MCQ
    mcqs_path = topic_dir / "mcqs.json"
    if mcqs_path.exists():
        try:
            mcqs = json.loads(mcqs_path.read_text(encoding="utf-8", errors="replace"))
            mcq_list = mcqs.get("mcqs", []) if isinstance(mcqs, dict) else mcqs if isinstance(mcqs, list) else []
            first_mcq = mcq_list[0] if mcq_list else None
            if first_mcq:
                parts.append(f"\n--- First MCQ ---")
                parts.append(json.dumps(first_mcq, indent=2)[:500])
        except (json.JSONDecodeError, KeyError, IndexError):
            pass

    # First flashcard
    fc_path = topic_dir / "flashcards.json"
    if fc_path.exists():
        try:
            fcs = json.loads(fc_path.read_text(encoding="utf-8", errors="replace"))
            fc_list = fcs.get("flashcards", []) if isinstance(fcs, dict) else fcs if isinstance(fcs, list) else []
            first_fc = fc_list[0] if fc_list else None
            if first_fc:
                parts.append(f"\n--- First Flashcard ---")
                parts.append(json.dumps(first_fc, indent=2)[:300])
        except (json.JSONDecodeError, KeyError, IndexError):
            pass

    return "\n".join(parts)


async def rate_single_api(semaphore: asyncio.Semaphore, session: 'aiohttp.ClientSession',
                          topic_path: str, api_name: str, idx: int, total: int,
                          system_prompt: str) -> tuple:
    """Rate one topic with one API. Returns (topic_path, api_name, result_dict)."""
    async with semaphore:
        ctx = get_topic_context(topic_path)
        label = f"{idx}/{total} {ctx['topic'][:35]} [{api_name}]"
        print(f"  [{label}] Rating...")
        user_content = load_topic_content_for_rating(topic_path)
        messages = [{"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content}]
        try:
            text = await call_api_async(session, messages, label, api_name=api_name)
            rating = parse_json_response(text)
            rating["_model"] = APIS[api_name]["model"]
            return (topic_path, api_name, {"rating": rating, "error": None})
        except json.JSONDecodeError as e:
            return (topic_path, api_name, {"rating": None, "error": f"JSON parse: {e}"})
        except Exception as e:
            return (topic_path, api_name, {"rating": None, "error": str(e)[:200]})


async def rate_all_topics(to_rate: list, selected_apis: list, system_prompt: str,
                          workers: int, progress: dict, progress_path: Path,
                          topics_data: dict) -> tuple:
    """Rate all topics × all APIs concurrently using aiohttp. Returns (rated_count, failed_count)."""
    semaphore = asyncio.Semaphore(workers)
    connector = aiohttp.TCPConnector(limit=workers + 5)

    # For topics with partial ratings, only request missing APIs
    def _apis_needed(tp):
        cached = progress.get("rated", {}).get(tp, {})
        return [api for api in selected_apis if api not in cached]

    rated_count = 0
    failed_count = 0

    async with aiohttp.ClientSession(connector=connector) as session:
        # Build all tasks: one per (topic, api) pair
        tasks = []
        for i, tp in enumerate(to_rate):
            needed = _apis_needed(tp)
            for api_name in needed:
                tasks.append(rate_single_api(
                    semaphore, session, tp, api_name, i + 1, len(to_rate), system_prompt
                ))

        print(f"  Launching {len(tasks)} async rating tasks ({workers} concurrent)...")

        # Gather all results
        results = await asyncio.gather(*tasks, return_exceptions=True)

    # Process results grouped by topic
    topic_results = {}
    for r in results:
        if isinstance(r, Exception):
            print(f"    Unexpected error: {r}")
            continue
        tp, api_name, api_result = r
        if tp not in topic_results:
            topic_results[tp] = {}
        topic_results[tp][api_name] = api_result

    # Merge into progress and topics_data
    for tp, api_ratings in topic_results.items():
        all_failed = True
        for api_name, api_result in api_ratings.items():
            if api_result.get("error"):
                print(f"    FAIL: {Path(tp).name} [{api_name}] — {api_result['error'][:80]}")
            else:
                all_failed = False
        if all_failed:
            failed_count += 1
        else:
            rated_count += 1

        if tp not in progress["rated"]:
            progress["rated"][tp] = {}
        progress["rated"][tp].update(api_ratings)
        topics_data[tp]["ratings"] = progress["rated"][tp]

    save_progress(progress_path, progress)
    return rated_count, failed_count


def rate_topic_sync(topic_path: str, idx: int, total: int, system_prompt: str,
                    selected_apis: list[str] = None) -> dict:
    """Sync fallback for rating (used when aiohttp is not installed)."""
    if selected_apis is None:
        selected_apis = list(APIS.keys())
    ctx = get_topic_context(topic_path)
    base_label = f"{idx}/{total} {ctx['topic'][:35]}"
    user_content = load_topic_content_for_rating(topic_path)
    messages = [{"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}]

    ratings = {}
    for api_name in selected_apis:
        label = f"{base_label} [{api_name}]"
        print(f"  [{label}] Rating...")
        try:
            text = call_api(messages, label, api_name=api_name)
            rating = parse_json_response(text)
            rating["_model"] = APIS[api_name]["model"]
            ratings[api_name] = {"rating": rating, "error": None}
        except json.JSONDecodeError as e:
            ratings[api_name] = {"rating": None, "error": f"JSON parse: {e}"}
        except Exception as e:
            ratings[api_name] = {"rating": None, "error": str(e)[:200]}

    return {"ratings": ratings}


# ── Stage 4: CLASSIFY ─────────────────────────────────────────────────────
def classify_topic(scan: dict, ratings_dict: dict) -> tuple:
    """Classify topic — any single API scoring ≤5 on any dimension triggers a flag."""
    if scan.get("missing") or scan.get("empty"):
        return "FIX_FILES", "missing/empty files"
    if scan.get("content_issues"):
        return "FIX_FILES", "content issues: " + "; ".join(scan["content_issues"])
    all_ratings = [r["rating"] for r in ratings_dict.values() if r and r.get("rating")]
    if not all_ratings:
        return "FIX_FILES", "no ratings available"

    # Check each API individually — any dissent triggers flag (threshold: ≤5)
    for api_name, r_data in ratings_dict.items():
        if not r_data or not r_data.get("rating"):
            continue
        rating = r_data["rating"]
        rel = rating.get("relevance", 10)
        if isinstance(rel, (int, float)) and rel <= 5:
            remark = rating.get("relevance_remarks", "")
            return "WRONG_SUBJECT", f"{api_name} flagged relevance={rel}: {remark}"

    for api_name, r_data in ratings_dict.items():
        if not r_data or not r_data.get("rating"):
            continue
        rating = r_data["rating"]
        tier_score = rating.get("tier", 10)
        if isinstance(tier_score, (int, float)) and tier_score <= 5:
            remark = rating.get("tier_remarks", "")
            return "WRONG_TIER", f"{api_name} flagged tier={tier_score}: {remark}"

    for api_name, r_data in ratings_dict.items():
        if not r_data or not r_data.get("rating"):
            continue
        rating = r_data["rating"]
        cov = rating.get("coverage", 10)
        qual = rating.get("quality", 10)
        cov_ok = not isinstance(cov, (int, float)) or cov > 5
        qual_ok = not isinstance(qual, (int, float)) or qual > 5
        if not cov_ok or not qual_ok:
            cov_remark = rating.get("coverage_remarks", "")
            qual_remark = rating.get("quality_remarks", "")
            return "LOW_QUALITY", f"{api_name} flagged cov={cov}/qual={qual}: {cov_remark}; {qual_remark}"

    return "PASS", ""


# ── Stage 5: FIX ──────────────────────────────────────────────────────────
MARKDOWN_SYSTEM_TEMPLATE = """\
You are an expert university lecturer creating study material.

TARGET AUDIENCE: {tier_name} level ({programs})
LANGUAGE STYLE: {tier_language}
DEPTH: {tier_depth}
READ.MD LENGTH: {tier_read_length}

Generate THREE markdown files for this topic.
Return EXACTLY this delimited format (no extra text before/after):

===READ_MD===
# <Topic Title>

## Introduction
[2-3 paragraphs]

## Key Concepts
[Detailed explanations]

## Examples
[2-3 worked examples]

## Exam Tips
[5-7 points]

===PURPOSE_MD===
# Learning Objectives

After studying this topic, you should be able to:
1. [Outcome]
...
6-8 outcomes
===SUMMARY_MD===
# <Topic Title> - Summary

## Key Definitions
- [Definitions]

## Important Formulas
- [Formulas]

## Key Points
- [7-10 points]

## Common Mistakes
- [3-4 points]
===END===

IMPORTANT: Return ONLY the delimited content. No JSON wrapping."""

ASSESSMENT_SYSTEM_TEMPLATE = """\
You are an expert exam paper setter.

TARGET AUDIENCE: {tier_name} level ({programs})
MCQ STYLE: {tier_mcq_style}
DEPTH: {tier_depth}

Generate assessment materials as a SINGLE JSON object. Return ONLY valid JSON:

{{
  "flashcards": [{{"id": "fc-1", "front": "Q?", "back": "Answer."}}],
  "mcqs": [{{
    "id": "mcq-1", "question": "Q",
    "options": [{{"key": "A", "text": "Opt1"}}, {{"key": "B", "text": "Opt2"}},
                {{"key": "C", "text": "Opt3"}}, {{"key": "D", "text": "Opt4"}}],
    "correctAnswer": "A", "explanation": "Why", "difficulty": "easy"
  }}],
  "memory": {{
    "mnemonics": [{{"id": "m-1", "title": "T", "content": "M"}}],
    "acronyms": [{{"term": "T", "expansion": "E", "usage": "U"}}],
    "visualTips": [{{"concept": "C", "visualization": "V"}}],
    "analogies": [{{"concept": "C", "analogy": "A"}}]
  }},
  "questions": [{{
    "id": "q-1", "type": "short", "question": "Q",
    "keyPoints": ["P1", "P2"], "marks": 5
  }}],
  "visual": {{
    "diagrams": [{{"id": "d-1", "title": "T", "description": "D",
                   "elements": ["E1"], "purpose": "P"}}]
  }},
  "code": [{{
    "id": "code-1", "language": "pseudocode", "title": "T",
    "description": "D", "code": "BEGIN\\n  step\\nEND",
    "explanation": "E", "timeComplexity": "O(n)", "spaceComplexity": "O(1)"
  }}]
}}

Requirements:
- 10-12 flashcards, 12-15 MCQs (balanced difficulty)
- 5-7 short (5 marks) + 2-3 long (10 marks) questions
- 2-3 code examples, rich memory aids
- MCQ options MUST be objects with "key" and "text"
- questions use "keyPoints" (NOT "expectedPoints")
- code uses "timeComplexity"/"spaceComplexity" (NOT nested object)

IMPORTANT: Return ONLY valid JSON."""

TIER_ADAPT_SYSTEM = """\
You are an expert content adapter. Rewrite the given study material to match this tier:

TARGET: {tier_name} level ({programs})
LANGUAGE: {tier_language}
DEPTH: {tier_depth}
READ.MD LENGTH: {tier_read_length}

If the content is too advanced, simplify. If too simple, deepen.
Return the same delimited format as input:

===READ_MD===
[adapted content]
===PURPOSE_MD===
[adapted content]
===SUMMARY_MD===
[adapted content]
===END==="""


def _build_user_prompt(ctx: dict) -> str:
    siblings = ", ".join(ctx.get('sibling_topics', [])) or "(none)"
    return (
        f"Subject: {ctx['subject']}\nModule: {ctx['module']}\nTopic: {ctx['topic']}\n"
        f"Sibling topics: {siblings}\n\n"
        f"IMPORTANT: Generate content ONLY about \"{ctx['topic']}\" "
        f"as it relates to \"{ctx['subject']}\"."
    )


def _build_reviewer_feedback(ratings_dict: dict, classification: str, reason: str,
                             level: str = "") -> str:
    """Build reviewer feedback blocks so the fix generator knows exactly what to fix."""
    tier_ctx = ""
    if level and level in TIER_TEMPLATES:
        t = TIER_TEMPLATES[level]
        tier_ctx = (f"\nTarget Audience: {t['name']} level ({t['programs']})\n"
                    f"Expected Depth: {t['depth']}\n"
                    f"Expected Language: {t['language']}\n")

    lines = [
        f"\n\n{'='*60}",
        f"⚠ IMPORTANT: THIS IS A RE-GENERATION ATTEMPT.",
        f"The content you previously generated was reviewed by 3 independent",
        f"AI reviewers and FAILED quality checks. You MUST carefully read",
        f"ALL reviewer feedback below and address EVERY concern.",
        f"Do NOT repeat the same mistakes.",
        f"{'='*60}",
        f"Overall Verdict: {classification}",
        f"Trigger: {reason}",
        tier_ctx,
    ]
    for i, (api_name, r_data) in enumerate(ratings_dict.items(), 1):
        if not r_data or not r_data.get("rating"):
            continue
        r = r_data["rating"]
        model = r.get("_model", api_name)
        lines.append(f"--- REVIEWER {i}: {model} ---")
        lines.append(f"Scores: Relevance={r.get('relevance','?')}/10, "
                     f"Coverage={r.get('coverage','?')}/10, "
                     f"Quality={r.get('quality','?')}/10, "
                     f"Tier={r.get('tier','?')}/10")
        for dim in ["relevance", "coverage", "quality", "tier"]:
            remark = r.get(f"{dim}_remarks", "")
            if remark:
                lines.append(f"  → {dim.title()}: {remark}")
        suggestions = r.get("suggestions", [])
        if suggestions:
            for s in suggestions:
                lines.append(f"  → Suggestion: {s}")
        lines.append("")
    lines.append(f"{'='*60}")
    lines.append("ADDRESS ALL REVIEWER CONCERNS ABOVE. Do NOT generate generic")
    lines.append("content — tailor it precisely to the topic, subject, and tier.")
    lines.append(f"{'='*60}")
    return "\n".join(lines)


def _parse_md_delimited(text: str) -> dict:
    files = {}
    m = re.search(r'===READ_MD===\s*(.+?)\s*===PURPOSE_MD===', text, re.DOTALL)
    if m:
        files['read.md'] = m.group(1).strip()
    m = re.search(r'===PURPOSE_MD===\s*(.+?)\s*===SUMMARY_MD===', text, re.DOTALL)
    if m:
        files['purpose.md'] = m.group(1).strip()
    m = re.search(r'===SUMMARY_MD===\s*(.+?)\s*===END===', text, re.DOTALL)
    if m:
        files['summary.md'] = m.group(1).strip()
    return files


def _normalize_assessment(data: dict, topic_id: str) -> dict:
    files = {}

    flashcards = data.get('flashcards', [])
    for i, fc in enumerate(flashcards):
        fc.setdefault('id', f'fc-{i+1}')
    files['flashcards.json'] = json.dumps({"topicId": topic_id, "flashcards": flashcards}, indent=2)

    mcqs = data.get('mcqs', [])
    for i, m in enumerate(mcqs):
        m.setdefault('id', f'mcq-{i+1}')
        if m.get('options') and isinstance(m['options'][0], str):
            keys = ["A", "B", "C", "D"]
            m['options'] = [{"key": keys[j], "text": t} for j, t in enumerate(m['options'])]
        m.setdefault('difficulty', 'medium')
    files['mcqs.json'] = json.dumps({"topicId": topic_id, "mcqs": mcqs}, indent=2)

    memory = data.get('memory', {})
    memory.setdefault('topicId', topic_id)
    files['memory.json'] = json.dumps(memory, indent=2)

    questions = data.get('questions', [])
    for i, q in enumerate(questions):
        q.setdefault('id', f'q-{i+1}')
        q.setdefault('type', 'long' if q.get('marks', 0) >= 10 else 'short')
        if 'expectedPoints' in q and 'keyPoints' not in q:
            q['keyPoints'] = q.pop('expectedPoints')
    files['questions.json'] = json.dumps({"topicId": topic_id, "questions": questions}, indent=2)

    visual = data.get('visual', {})
    visual.setdefault('topicId', topic_id)
    files['visual.json'] = json.dumps(visual, indent=2)

    code_examples = data.get('code', [])
    for i, ex in enumerate(code_examples):
        ex.setdefault('id', f'code-{i+1}')
        ex.setdefault('language', 'pseudocode')
        if 'code' not in ex:
            ex['code'] = ex.get('pseudocode', '// No code')
        if 'complexity' in ex and isinstance(ex['complexity'], dict):
            ex.setdefault('timeComplexity', ex['complexity'].get('time', ''))
            ex.setdefault('spaceComplexity', ex['complexity'].get('space', ''))
            del ex['complexity']
    files['code.json'] = json.dumps({"topicId": topic_id, "examples": code_examples}, indent=2)

    return files


def fix_topic(topic_path: str, classification: str, scan: dict,
              level: str, idx: int, total: int,
              ratings_dict: dict = None, reason: str = "") -> dict:
    ctx = get_topic_context(topic_path)
    topic_dir = Path(topic_path)
    topic_id = ctx['topic_slug']
    tier = TIER_TEMPLATES[level]
    label = f"FIX {idx}/{total} {ctx['topic'][:30]}"
    result = {"fixed_files": [], "error": None}

    fmt = dict(tier_name=tier["name"], programs=tier["programs"],
               tier_language=tier["language"], tier_depth=tier["depth"],
               tier_mcq_style=tier["mcq_style"], tier_read_length=tier["read_length"])

    # Build reviewer feedback to inject into fix prompts
    feedback = _build_reviewer_feedback(ratings_dict, classification, reason, level) if ratings_dict else ""

    try:
        if classification == "FIX_FILES":
            missing_md = [f for f in (scan.get("missing", []) + scan.get("empty", [])) if f in MD_FILES]
            missing_json = [f for f in (scan.get("missing", []) + scan.get("empty", [])) if f in JSON_FILES]

            if missing_md:
                print(f"  [{label}] Regenerating markdown files...")
                sys_prompt = MARKDOWN_SYSTEM_TEMPLATE.format(**fmt)
                text = call_api(
                    [{"role": "system", "content": sys_prompt},
                     {"role": "user", "content": _build_user_prompt(ctx) + feedback}],
                    label, MAX_TOKENS_GEN, TEMPERATURE_GEN,
                )
                md_files = _parse_md_delimited(text)
                for fname, content in md_files.items():
                    if fname in missing_md or not (topic_dir / fname).exists():
                        (topic_dir / fname).write_text(content, encoding='utf-8')
                        result["fixed_files"].append(fname)

            if missing_json:
                read_content = (topic_dir / "read.md").read_text(encoding='utf-8', errors='replace')[:500] if (topic_dir / "read.md").exists() else ""
                print(f"  [{label}] Regenerating JSON files...")
                sys_prompt = ASSESSMENT_SYSTEM_TEMPLATE.format(**fmt)
                user = _build_user_prompt(ctx) + f"\n\nTopic summary:\n{read_content}" + feedback
                text = call_api(
                    [{"role": "system", "content": sys_prompt},
                     {"role": "user", "content": user}],
                    label, MAX_TOKENS_GEN, TEMPERATURE_GEN,
                )
                data = parse_json_response(text)
                json_files = _normalize_assessment(data, topic_id)
                for fname, content in json_files.items():
                    if fname in missing_json or not (topic_dir / fname).exists():
                        (topic_dir / fname).write_text(content, encoding='utf-8')
                        result["fixed_files"].append(fname)

        elif classification == "WRONG_SUBJECT":
            # Regenerate ALL files
            print(f"  [{label}] Full regeneration (wrong subject)...")
            sys_prompt = MARKDOWN_SYSTEM_TEMPLATE.format(**fmt)
            text = call_api(
                [{"role": "system", "content": sys_prompt},
                 {"role": "user", "content": _build_user_prompt(ctx) + feedback}],
                label, MAX_TOKENS_GEN, TEMPERATURE_GEN,
            )
            md_files = _parse_md_delimited(text)
            for fname, content in md_files.items():
                (topic_dir / fname).write_text(content, encoding='utf-8')
                result["fixed_files"].append(fname)

            read_content = md_files.get('read.md', '')[:500]
            sys_prompt = ASSESSMENT_SYSTEM_TEMPLATE.format(**fmt)
            user = _build_user_prompt(ctx) + f"\n\nTopic summary:\n{read_content}" + feedback
            text = call_api(
                [{"role": "system", "content": sys_prompt},
                 {"role": "user", "content": user}],
                label, MAX_TOKENS_GEN, TEMPERATURE_GEN,
            )
            data = parse_json_response(text)
            json_files = _normalize_assessment(data, topic_id)
            for fname, content in json_files.items():
                (topic_dir / fname).write_text(content, encoding='utf-8')
                result["fixed_files"].append(fname)

        elif classification == "WRONG_TIER":
            # Adapt existing markdown + regenerate MCQs/flashcards
            print(f"  [{label}] Adapting to {tier['name']} tier...")
            existing_md = ""
            for fname in ["read.md", "purpose.md", "summary.md"]:
                fpath = topic_dir / fname
                if fpath.exists():
                    existing_md += f"==={fname.upper().replace('.', '_')}===\n"
                    existing_md += fpath.read_text(encoding='utf-8', errors='replace')
                    existing_md += "\n"
            existing_md += "===END==="

            sys_prompt = TIER_ADAPT_SYSTEM.format(**fmt)
            text = call_api(
                [{"role": "system", "content": sys_prompt},
                 {"role": "user", "content": f"Adapt this content:\n\n{existing_md[:6000]}" + feedback}],
                label, MAX_TOKENS_GEN, TEMPERATURE_GEN,
            )
            md_files = _parse_md_delimited(text)
            for fname, content in md_files.items():
                (topic_dir / fname).write_text(content, encoding='utf-8')
                result["fixed_files"].append(fname)

            # Regenerate MCQs and flashcards at correct tier
            read_content = md_files.get('read.md', '')[:500]
            sys_prompt = ASSESSMENT_SYSTEM_TEMPLATE.format(**fmt)
            user = _build_user_prompt(ctx) + f"\n\nTopic summary:\n{read_content}" + feedback
            text = call_api(
                [{"role": "system", "content": sys_prompt},
                 {"role": "user", "content": user}],
                label, MAX_TOKENS_GEN, TEMPERATURE_GEN,
            )
            data = parse_json_response(text)
            json_files = _normalize_assessment(data, topic_id)
            for fname, content in json_files.items():
                (topic_dir / fname).write_text(content, encoding='utf-8')
                result["fixed_files"].append(fname)

        elif classification == "LOW_QUALITY":
            # Regenerate all (simpler than cherry-picking individual weak files)
            print(f"  [{label}] Upgrading low-quality content...")
            sys_prompt = MARKDOWN_SYSTEM_TEMPLATE.format(**fmt)
            text = call_api(
                [{"role": "system", "content": sys_prompt},
                 {"role": "user", "content": _build_user_prompt(ctx) + feedback}],
                label, MAX_TOKENS_GEN, TEMPERATURE_GEN,
            )
            md_files = _parse_md_delimited(text)
            for fname, content in md_files.items():
                (topic_dir / fname).write_text(content, encoding='utf-8')
                result["fixed_files"].append(fname)

            read_content = md_files.get('read.md', '')[:500]
            sys_prompt = ASSESSMENT_SYSTEM_TEMPLATE.format(**fmt)
            user = _build_user_prompt(ctx) + f"\n\nTopic summary:\n{read_content}" + feedback
            text = call_api(
                [{"role": "system", "content": sys_prompt},
                 {"role": "user", "content": user}],
                label, MAX_TOKENS_GEN, TEMPERATURE_GEN,
            )
            data = parse_json_response(text)
            json_files = _normalize_assessment(data, topic_id)
            for fname, content in json_files.items():
                (topic_dir / fname).write_text(content, encoding='utf-8')
                result["fixed_files"].append(fname)

    except Exception as e:
        result["error"] = str(e)[:200]
        print(f"  [{label}] FIX FAILED: {result['error']}")

    return result


# ── Stage 3/6: REPORT ─────────────────────────────────────────────────────
def _esc(text) -> str:
    return html_mod.escape(str(text)) if text else ""


def _rating_cls(n) -> str:
    if n is None or not isinstance(n, (int, float)):
        return ""
    return "high" if n >= 8 else ("mid" if n >= 6 else "low")


def _avg_ratings(ratings_dict: dict) -> dict:
    """Compute averaged ratings across APIs for display."""
    all_ratings = [r["rating"] for r in ratings_dict.values() if r and r.get("rating")]
    if not all_ratings:
        return {}
    avg = {}
    for key in ["relevance", "coverage", "quality", "tier"]:
        vals = [r.get(key) for r in all_ratings if isinstance(r.get(key), (int, float))]
        if vals:
            avg[key] = round(sum(vals) / len(vals), 1)
    return avg


def generate_report(topics_data: dict, output_dir: Path, tag: str = "") -> tuple[Path, Path]:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    suffix = f"_{tag}" if tag else ""
    json_path = output_dir / f"quality_gate{suffix}_{timestamp}.json"
    html_path = json_path.with_suffix(".html")

    # Compute stats
    counts = {"PASS": 0, "FIX_FILES": 0, "WRONG_SUBJECT": 0, "WRONG_TIER": 0, "LOW_QUALITY": 0, "UNRATED": 0}
    for t in topics_data.values():
        cls = t.get("classification", "UNRATED")
        counts[cls] = counts.get(cls, 0) + 1

    report = {
        "generated_at": datetime.now().isoformat(),
        "total_topics": len(topics_data),
        "counts": counts,
        "topics": topics_data,
    }

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    # Build HTML
    lines = []
    w = lines.append
    w("<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'>")
    w("<meta name='viewport' content='width=device-width,initial-scale=1'>")
    w("<title>Quality Gate Report</title>")
    w("<style>")
    w(""":root{--bg:#0f1419;--surface:#1a2332;--surface2:#243044;--text:#e6edf3;--muted:#8b949e;
--accent:#58a6ff;--green:#3fb950;--amber:#d29922;--red:#f85149;--radius:8px}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--text);padding:24px;line-height:1.5}
.container{max-width:1400px;margin:0 auto}
h1{font-size:1.5rem;font-weight:600;margin-bottom:4px}
h2{font-size:1.15rem;font-weight:600;margin:24px 0 12px;color:var(--accent)}
.subtitle{color:var(--muted);font-size:.9rem;margin-bottom:20px}
.summary-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:14px;margin-bottom:24px}
.card{background:var(--surface);border-radius:var(--radius);padding:16px;border:1px solid var(--surface2)}
.card .label{color:var(--muted);font-size:.78rem;text-transform:uppercase;letter-spacing:.05em;margin-bottom:4px}
.card .value{font-size:1.25rem;font-weight:600}
.filter-bar{margin-bottom:16px;display:flex;gap:8px;flex-wrap:wrap}
.filter-btn{padding:6px 14px;border-radius:4px;border:1px solid var(--surface2);background:var(--surface);
color:var(--text);cursor:pointer;font-size:.82rem}
.filter-btn.active{background:var(--accent);color:#000;border-color:var(--accent)}
table{width:100%;border-collapse:collapse;background:var(--surface);border-radius:var(--radius);
overflow:hidden;border:1px solid var(--surface2);font-size:.88rem}
th,td{padding:10px 14px;text-align:left;border-bottom:1px solid var(--surface2)}
th{background:var(--surface2);color:var(--muted);font-size:.78rem;font-weight:600;text-transform:uppercase;
letter-spacing:.04em;position:sticky;top:0;z-index:1}
tr:hover>td{background:rgba(56,139,253,.06)}
.r{font-weight:600;display:inline-block;min-width:1.4em;text-align:center}
.r.high{color:var(--green)}.r.mid{color:var(--amber)}.r.low{color:var(--red)}
.badge{padding:3px 8px;border-radius:4px;font-size:.75rem;font-weight:600;display:inline-block}
.badge.PASS{background:#3fb95022;color:var(--green)}
.badge.FIX_FILES{background:#d2992222;color:var(--amber)}
.badge.WRONG_SUBJECT{background:#f8514922;color:var(--red)}
.badge.WRONG_TIER{background:#f8514922;color:#ff7b72}
.badge.LOW_QUALITY{background:#d2992222;color:var(--amber)}
.badge.UNRATED{background:var(--surface2);color:var(--muted)}
details{margin:0}details summary{cursor:pointer;color:var(--accent);font-size:.82rem;list-style:none}
details summary::-webkit-details-marker{display:none}
details summary::before{content:'+ '}details[open] summary::before{content:'- '}
.detail-box{background:var(--bg);border-radius:var(--radius);padding:14px;margin-top:8px;font-size:.82rem}
.detail-box p{margin-bottom:4px;color:var(--muted)}
.detail-box strong{color:var(--text);font-weight:500}
.topic-path{font-size:.75rem;color:var(--muted);max-width:350px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.reason-cell{font-size:.78rem;color:var(--muted);max-width:280px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.reviewer-panel{background:var(--surface2);border-radius:6px;padding:10px 12px;margin:6px 0;border-left:3px solid var(--accent)}
.reviewer-panel h4{color:var(--accent);font-size:.82rem;margin-bottom:4px}
.reviewer-panel .scores{font-size:.78rem;color:var(--text);margin-bottom:4px}
.reviewer-panel .remark{font-size:.78rem;color:var(--muted);margin:2px 0}
@media(max-width:900px){body{padding:12px}th,td{padding:8px}}""")
    w("</style></head><body><div class='container'>")

    w(f"<h1>Quality Gate Report</h1>")
    w(f"<p class='subtitle'>{_esc(report['generated_at'])} &mdash; {len(topics_data)} topics</p>")

    # Detect which APIs were used
    apis_used = set()
    for t in topics_data.values():
        for api_name in t.get("ratings", {}):
            apis_used.add(api_name)
    apis_used = sorted(apis_used)

    # Summary cards
    w("<div class='summary-grid'>")
    w(f"<div class='card'><div class='label'>Total</div><div class='value'>{len(topics_data)}</div></div>")
    for cls, color in [("PASS", "var(--green)"), ("FIX_FILES", "var(--amber)"),
                       ("WRONG_SUBJECT", "var(--red)"), ("WRONG_TIER", "#ff7b72"),
                       ("LOW_QUALITY", "var(--amber)"), ("UNRATED", "var(--muted)")]:
        if counts.get(cls, 0) > 0:
            w(f"<div class='card'><div class='label'>{cls}</div>"
              f"<div class='value' style='color:{color}'>{counts[cls]}</div></div>")
    # Per-API average + pass rate cards
    for api_name in apis_used:
        api_scores = []
        api_pass = 0
        api_total = 0
        for t in topics_data.values():
            r = t.get("ratings", {}).get(api_name, {})
            if r and r.get("rating"):
                rt = r["rating"]
                vals = [rt.get(k) for k in ["relevance", "coverage", "quality", "tier"]
                        if isinstance(rt.get(k), (int, float))]
                if vals:
                    api_scores.append(sum(vals) / len(vals))
                    api_total += 1
                    # Pass if all dimensions > 5 (matches classify threshold)
                    if all(isinstance(rt.get(k), (int, float)) and rt.get(k) > 5
                           for k in ["relevance", "coverage", "quality", "tier"]):
                        api_pass += 1
        if api_scores:
            avg_score = sum(api_scores) / len(api_scores)
            pass_pct = (api_pass / api_total * 100) if api_total else 0
            pct_color = "var(--green)" if pass_pct >= 90 else ("var(--amber)" if pass_pct >= 70 else "var(--red)")
            w(f"<div class='card'><div class='label'>{_esc(api_name)} avg</div>"
              f"<div class='value' style='color:var(--accent)'>{avg_score:.1f}</div></div>")
            w(f"<div class='card'><div class='label'>{_esc(api_name)} pass</div>"
              f"<div class='value' style='color:{pct_color}'>{pass_pct:.0f}%</div></div>")
    w("</div>")

    # Filter bar
    w("<div class='filter-bar'>")
    w("<button class='filter-btn active' onclick='filterRows(\"all\")'>All</button>")
    for cls in ["PASS", "FIX_FILES", "WRONG_SUBJECT", "WRONG_TIER", "LOW_QUALITY"]:
        if counts.get(cls, 0) > 0:
            w(f"<button class='filter-btn' onclick='filterRows(\"{cls}\")'>{cls} ({counts[cls]})</button>")
    w("</div>")

    # Table
    w("<table id='main-table'><thead><tr>")
    w("<th>#</th><th>Topic</th><th>Subject</th><th>Rel</th><th>Cov</th><th>Qual</th><th>Tier</th><th>Status</th><th>Reason</th><th>Details</th>")
    w("</tr></thead><tbody>")

    for i, (key, t) in enumerate(sorted(topics_data.items(), key=lambda x: x[0]), 1):
        cls = t.get("classification", "UNRATED")
        ctx = t.get("context", {})
        ratings_dict = t.get("ratings", {})
        avg = _avg_ratings(ratings_dict)
        scan = t.get("scan", {})
        fix = t.get("fix", {})

        rel = avg.get("relevance")
        cov = avg.get("coverage")
        qual = avg.get("quality")
        tier_r = avg.get("tier")

        short_path = re.sub(r'^.*/(?:cse|ise|du_\w+)/', '', t.get("path", ""))

        w(f"<tr data-cls='{cls}'>")
        w(f"<td>{i}</td>")
        w(f"<td><div style='font-weight:500'>{_esc(ctx.get('topic', key))}</div>"
          f"<div class='topic-path' title='{_esc(t.get('path',''))}'>{_esc(short_path)}</div></td>")
        w(f"<td>{_esc(ctx.get('subject', ''))}</td>")
        for val, dim_key in [(rel, "relevance"), (cov, "coverage"), (qual, "quality"), (tier_r, "tier")]:
            if val is not None:
                # Build compact per-API breakdown for tooltip
                parts = []
                for api_name in apis_used:
                    ar = ratings_dict.get(api_name, {})
                    if ar and ar.get("rating"):
                        v = ar["rating"].get(dim_key)
                        if v is not None:
                            parts.append(f"{api_name[0].upper()}:{v}")
                tooltip = " ".join(parts) if len(parts) > 1 else ""
                cell_extra = ""
                if len(parts) > 1:
                    cell_extra = f"<br><span style='font-size:.7rem;color:var(--muted)'>{' '.join(parts)}</span>"
                w(f"<td title='{_esc(tooltip)}'><span class='r {_rating_cls(val)}'>{val}</span>{cell_extra}</td>")
            else:
                w("<td><span class='r' style='color:var(--muted)'>-</span></td>")
        w(f"<td><span class='badge {cls}'>{cls}</span></td>")
        reason_text = t.get("reason", "")
        w(f"<td class='reason-cell' title='{_esc(reason_text)}'>{_esc(reason_text[:80])}</td>")

        # Details column — per-API reviewer panels
        w("<td><details><summary>View</summary><div class='detail-box'>")
        for ri, api_name in enumerate(apis_used, 1):
            ar = ratings_dict.get(api_name, {})
            rating = ar.get("rating") if ar else None
            if rating:
                model = rating.get("_model", APIS.get(api_name, {}).get("model", api_name))
                w(f"<div class='reviewer-panel'>")
                w(f"<h4>Reviewer {ri}: {_esc(model)}</h4>")
                scores = []
                for k, label in [("relevance", "R"), ("coverage", "C"), ("quality", "Q"), ("tier", "T")]:
                    v = rating.get(k, "?")
                    color = "var(--green)" if isinstance(v, (int, float)) and v >= 8 else (
                        "var(--amber)" if isinstance(v, (int, float)) and v >= 5 else "var(--red)")
                    scores.append(f"<span style='color:{color}'>{label}={v}</span>")
                w(f"<p class='scores'>{', '.join(scores)}</p>")
                for dim, rk in [("Relevance", "relevance"), ("Coverage", "coverage"),
                                ("Quality", "quality"), ("Tier", "tier")]:
                    remark = rating.get(f"{rk}_remarks", "")
                    if remark:
                        w(f"<p class='remark'><strong>{dim}:</strong> {_esc(remark)}</p>")
                suggestions = rating.get("suggestions", [])
                if suggestions:
                    w("<p class='remark'><strong>Suggestions:</strong></p><ul>")
                    for s in suggestions:
                        w(f"<li style='font-size:.78rem;color:var(--muted)'>{_esc(s)}</li>")
                    w("</ul>")
                w("</div>")
            elif ar and ar.get("error"):
                w(f"<p style='color:var(--red)'><strong>{_esc(api_name)} error:</strong> {_esc(ar['error'])}</p>")
        if scan.get("missing"):
            w(f"<p><strong>Missing files:</strong> {_esc(', '.join(scan['missing']))}</p>")
        if scan.get("empty"):
            w(f"<p><strong>Empty files:</strong> {_esc(', '.join(scan['empty']))}</p>")
        if scan.get("invalid_json"):
            w(f"<p><strong>Invalid JSON:</strong> {_esc(', '.join(scan['invalid_json']))}</p>")
        if fix.get("fixed_files"):
            w(f"<p style='color:var(--green)'><strong>Fixed:</strong> {_esc(', '.join(fix['fixed_files']))}</p>")
        if fix.get("error"):
            w(f"<p style='color:var(--red)'><strong>Fix error:</strong> {_esc(fix['error'])}</p>")
        w("</div></details></td>")
        w("</tr>")

    w("</tbody></table>")

    # Filter JS
    w("""<script>
function filterRows(cls) {
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
  document.querySelectorAll('#main-table tbody tr').forEach(r => {
    r.style.display = (cls === 'all' || r.dataset.cls === cls) ? '' : 'none';
  });
}
</script>""")

    w("</div></body></html>")

    html_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, html_path


# ── Progress Tracking ─────────────────────────────────────────────────────
def load_progress(progress_path: Path) -> dict:
    if progress_path.exists():
        try:
            return json.loads(progress_path.read_text())
        except (json.JSONDecodeError, IOError):
            pass
    return {"rated": {}}


def save_progress(progress_path: Path, progress: dict):
    with progress_lock:
        progress["last_updated"] = datetime.now().isoformat()
        progress_path.write_text(json.dumps(progress, indent=2))


# ── Main ──────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Automated Content Quality Pipeline")
    parser.add_argument("pack_path", help="Path to content pack (e.g., cse/, du_mca/)")
    parser.add_argument("--level", choices=list(TIER_TEMPLATES.keys()), help="Tier level for rating")
    parser.add_argument("--scan-only", action="store_true", dest="scan_only", help="Filesystem check only")
    parser.add_argument("--fix", action="store_true", help="Fix classified issues (run after reviewing report)")
    parser.add_argument("--resume", action="store_true", help="Resume interrupted rating run")
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS, help=f"Parallel workers (default {DEFAULT_WORKERS})")
    parser.add_argument("--report-only", dest="report_only", help="Regenerate HTML from saved JSON")
    parser.add_argument("--apis", default=",".join(APIS.keys()),
                        help=f"Comma-separated API names to use (default: {','.join(APIS.keys())})")
    args = parser.parse_args()

    # Determine selected APIs
    selected_apis = [a.strip() for a in args.apis.split(",") if a.strip() in APIS]
    if not selected_apis:
        print(f"Error: No valid APIs in --apis={args.apis}. Available: {', '.join(APIS.keys())}")
        sys.exit(1)

    # ── Report-only mode ──────────────────────────────────────────────────
    if args.report_only:
        json_file = Path(args.report_only)
        if not json_file.exists():
            print(f"Error: File not found: {json_file}")
            sys.exit(1)
        report = json.loads(json_file.read_text())
        _, html_path = generate_report(report["topics"], json_file.parent, "regen")
        print(f"HTML report generated: {html_path}")
        return

    pack_path = Path(args.pack_path)
    if not pack_path.exists():
        print(f"Error: Pack path not found: {pack_path}")
        sys.exit(1)

    # ── Stage 1: SCAN ────────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print("QUALITY GATE — Stage 1: SCAN")
    print(f"{'='*70}")

    topic_paths = discover_topics(pack_path)
    print(f"Found {len(topic_paths)} topic directories")

    topics_data = {}
    scan_issues = 0
    for tp in topic_paths:
        scan = scan_topic(tp)
        ctx = get_topic_context(tp)
        topics_data[tp] = {
            "path": tp,
            "context": ctx,
            "scan": scan,
            "ratings": {},
            "classification": "UNRATED",
            "fix": {},
        }
        if not scan["ok"]:
            scan_issues += 1
            issues = scan["missing"] + scan["empty"] + scan["invalid_json"]
            print(f"  ISSUE: {ctx['topic'][:40]} — {', '.join(issues)}")

    print(f"\nScan complete: {len(topic_paths)} topics, {scan_issues} with issues")

    if args.scan_only:
        output_dir = pack_path / "reports"
        output_dir.mkdir(exist_ok=True)
        for tp, t in topics_data.items():
            t["classification"] = "FIX_FILES" if not t["scan"]["ok"] else "PASS"
        json_path, html_path = generate_report(topics_data, output_dir, "scan")
        print(f"\nJSON: {json_path}")
        print(f"HTML: {html_path}")
        return

    # ── Stage 2: RATE ────────────────────────────────────────────────────
    if not args.level:
        print("Error: --level required for rating (use --scan-only for filesystem check)")
        sys.exit(1)

    progress_path = pack_path / "reports" / "quality_gate_progress.json"
    (pack_path / "reports").mkdir(exist_ok=True)
    progress = load_progress(progress_path) if args.resume else {"rated": {}}

    # Migrate old progress formats:
    # 1. Single-API format (bare rating dict) → wrap in minimax key
    # 2. Old "chutes" key (DeepSeek-R1) → drop it (re-rate with new APIs)
    for tp, cached in list(progress.get("rated", {}).items()):
        if isinstance(cached, dict) and "relevance" in cached:
            progress["rated"][tp] = {"minimax": {"rating": cached, "error": None}}
        elif isinstance(cached, dict) and "chutes" in cached:
            del cached["chutes"]

    # Skip topics where ALL selected APIs already have ratings
    def _needs_rating(tp):
        cached = progress.get("rated", {}).get(tp, {})
        return not all(api in cached for api in selected_apis)

    to_rate = [tp for tp in topic_paths if _needs_rating(tp)]
    if args.resume and len(to_rate) < len(topic_paths):
        print(f"\nResuming: {len(topic_paths) - len(to_rate)} fully rated, {len(to_rate)} remaining")
        # Restore previous ratings
        for tp, cached in progress["rated"].items():
            if tp in topics_data:
                topics_data[tp]["ratings"] = cached

    api_names = ", ".join(selected_apis)
    print(f"\n{'='*70}")
    print(f"QUALITY GATE — Stage 2: RATE ({len(to_rate)} topics, level={args.level}, apis={api_names})")
    print(f"{'='*70}")

    system_prompt = build_rating_prompt(args.level)
    rated_count = 0
    failed_count = 0
    start_time = time.time()

    if to_rate:
        if HAS_AIOHTTP:
            # Async rating with aiohttp (fast — 25 concurrent workers)
            rated_count, failed_count = asyncio.run(
                rate_all_topics(to_rate, selected_apis, system_prompt,
                                args.workers, progress, progress_path, topics_data)
            )
        else:
            # Sync fallback (slow — sequential per topic)
            print("  WARNING: aiohttp not installed, falling back to sync rating (pip install aiohttp)")
            for i, tp in enumerate(to_rate):
                cached = progress.get("rated", {}).get(tp, {})
                needed = [api for api in selected_apis if api not in cached]
                result = rate_topic_sync(tp, i + 1, len(to_rate), system_prompt, needed)
                all_failed = all(r.get("error") for r in result["ratings"].values())
                if all_failed:
                    failed_count += 1
                else:
                    rated_count += 1
                if tp not in progress["rated"]:
                    progress["rated"][tp] = {}
                progress["rated"][tp].update(result["ratings"])
                topics_data[tp]["ratings"] = progress["rated"][tp]
                save_progress(progress_path, progress)

    elapsed = time.time() - start_time
    print(f"\nRating complete: {rated_count} rated, {failed_count} failed in {elapsed:.0f}s")

    # ── Stage 4: CLASSIFY ────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print("QUALITY GATE — Stage 4: CLASSIFY")
    print(f"{'='*70}")

    counts = {"PASS": 0, "FIX_FILES": 0, "WRONG_SUBJECT": 0, "WRONG_TIER": 0, "LOW_QUALITY": 0}
    for tp, t in topics_data.items():
        cls, reason = classify_topic(t["scan"], t.get("ratings", {}))
        t["classification"] = cls
        t["reason"] = reason
        counts[cls] += 1

    for cls, count in counts.items():
        if count > 0:
            print(f"  {cls:20s}: {count}")
    print(f"  {'TOTAL':20s}: {len(topics_data)}")

    # ── Stage 3: REPORT (pre-fix) ────────────────────────────────────────
    print(f"\n{'='*70}")
    print("QUALITY GATE — Stage 3: REPORT (pre-fix)")
    print(f"{'='*70}")

    output_dir = pack_path / "reports"
    output_dir.mkdir(exist_ok=True)
    json_path, html_path = generate_report(topics_data, output_dir, "pre-fix")
    print(f"JSON: {json_path}")
    print(f"HTML: {html_path}")

    if not args.fix:
        print(f"\nDone. Review report then re-run with --fix to apply fixes.")
        return

    # ── Stage 5: FIX ─────────────────────────────────────────────────────
    to_fix = [(tp, t) for tp, t in topics_data.items() if t["classification"] != "PASS"]
    if not to_fix:
        print("\nAll topics PASS — nothing to fix.")
        return

    print(f"\n{'='*70}")
    print(f"QUALITY GATE — Stage 5: FIX ({len(to_fix)} topics)")
    print(f"{'='*70}")

    fix_start = time.time()
    fixed_count = 0

    # Fix sequentially to avoid API rate limits during generation
    for i, (tp, t) in enumerate(to_fix, 1):
        result = fix_topic(tp, t["classification"], t["scan"], args.level, i, len(to_fix),
                           ratings_dict=t.get("ratings"), reason=t.get("reason", ""))
        t["fix"] = result
        if result["fixed_files"]:
            fixed_count += 1
            print(f"  Fixed {len(result['fixed_files'])} files for {t['context']['topic'][:40]}")

    fix_elapsed = time.time() - fix_start
    print(f"\nFix complete: {fixed_count}/{len(to_fix)} topics fixed in {fix_elapsed:.0f}s")

    # ── Stage 6: REPORT (post-fix) ───────────────────────────────────────
    print(f"\n{'='*70}")
    print("QUALITY GATE — Stage 6: REPORT (post-fix)")
    print(f"{'='*70}")

    json_path, html_path = generate_report(topics_data, output_dir, "post-fix")
    print(f"JSON: {json_path}")
    print(f"HTML: {html_path}")
    print(f"\n{'='*70}")
    print("QUALITY GATE COMPLETE")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    main()
