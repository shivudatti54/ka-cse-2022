#!/usr/bin/env python3
"""
Benchmark Chutes LLM models on problematic quality-gate topics.

Tests 5 candidate models on 10 representative issue topics to find the best
rater for the quality gate pipeline.

Usage:
  python3 scripts/benchmark_models.py
"""

import json
import ssl
import time
import urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# ── Models to benchmark ──────────────────────────────────────────────────
CHUTES_API_KEY = "cpk_a744b82c5b9c4e8b9c7c8e1442e8d160.c3a84cdb26e850c9b8f358af872bca49.ymNhlwAf2nbhnTZJE620p8sv1aTgEGwx"
MINIMAX_API_KEY = "sk-cp-r--6hiKCzLgU9QbQREFxR4v336s2kP0vDCeb3x7-iNJxAAdDwQeXhInB8zgfwcduBNoBtQBSj33uci2eCKcCu7q4VjmMGWDhKYHXu_lpv1fmWctproM4cAg"

MODELS = {
    "minimax-m2.5": {
        "base_url": "https://api.minimax.io/v1/chat/completions",
        "api_key": MINIMAX_API_KEY,
        "model": "MiniMax-M2.5",
        "timeout": 120,
        "cost_per_mtok": {"in": 0.30, "out": 1.10},
    },
    "deepseek-r1": {
        "base_url": "https://llm.chutes.ai/v1/chat/completions",
        "api_key": CHUTES_API_KEY,
        "model": "deepseek-ai/DeepSeek-R1-TEE",
        "timeout": 240,
        "cost_per_mtok": {"in": 0.30, "out": 1.20},
    },
    "qwen3-235b-thinking": {
        "base_url": "https://llm.chutes.ai/v1/chat/completions",
        "api_key": CHUTES_API_KEY,
        "model": "Qwen/Qwen3-235B-A22B-Thinking-2507",
        "timeout": 240,
        "cost_per_mtok": {"in": 0.11, "out": 0.60},
    },
    "gpt-oss-120b": {
        "base_url": "https://llm.chutes.ai/v1/chat/completions",
        "api_key": CHUTES_API_KEY,
        "model": "openai/gpt-oss-120b-TEE",
        "timeout": 240,
        "cost_per_mtok": {"in": 0.04, "out": 0.18},
    },
    "deepseek-v3.2": {
        "base_url": "https://llm.chutes.ai/v1/chat/completions",
        "api_key": CHUTES_API_KEY,
        "model": "deepseek-ai/DeepSeek-V3.2-TEE",
        "timeout": 240,
        "cost_per_mtok": {"in": 0.28, "out": 0.42},
    },
}

# ── Sample topics — 10 across all 4 issue categories ─────────────────────
SAMPLE_TOPICS = [
    # WRONG_SUBJECT (3): Content doesn't match subject
    {
        "path": "cse/sem-5/bcs502-computer-networks/module-4/topics/features",
        "issue": "WRONG_SUBJECT",
        "prev_scores": {"minimax": "R=1 C=1 Q=5 T=1", "chutes": "R=1 C=1 Q=3 T=2"},
    },
    {
        "path": "cse/sem-3/bcs304-data-structures-and-applications/module-5/topics/leftist-trees",
        "issue": "WRONG_SUBJECT",
        "prev_scores": {"minimax": "R=1 C=5 Q=8 T=7", "chutes": "R=2 C=8 Q=9 T=7"},
    },
    {
        "path": "cse/sem-4/bcs405d-linear-algebra/module-1/topics/8-hours-teaching-learning-chalk-and-talk-method-po",
        "issue": "WRONG_SUBJECT",
        "prev_scores": {"minimax": "R=1 C=1 Q=2 T=1", "chutes": "R=2 C=1 Q=3 T=2"},
    },
    # WRONG_TIER (3): Depth doesn't match B.Tech level
    {
        "path": "cse/sem-6/bcs613d-advanced-java/module-1/topics/working-with-maps",
        "issue": "WRONG_TIER",
        "prev_scores": {"minimax": "R=9 C=2 Q=3 T=2", "chutes": "R=8 C=4 Q=6 T=4"},
    },
    {
        "path": "cse/sem-7/bcs702-parallel-computing/module-4/topics/producers-and-consumers",
        "issue": "WRONG_TIER",
        "prev_scores": {"minimax": "R=7 C=1 Q=1 T=1", "chutes": "R=9 C=5 Q=4 T=4"},
    },
    {
        "path": "cse/sem-6/bcs654a-introduction-to-data-structures/module-1/topics/declaring-structures",
        "issue": "WRONG_TIER",
        "prev_scores": {"minimax": "R=8 C=2 Q=3 T=2", "chutes": "R=10 C=6 Q=7 T=5"},
    },
    # LOW_QUALITY (2): Poor coverage/quality
    {
        "path": "cse/sem-3/bcs303-operating-systems/module-4/topics/segmentation",
        "issue": "LOW_QUALITY",
        "prev_scores": {"minimax": "R=3 C=4 Q=2 T=5", "chutes": "R=6 C=8 Q=4 T=5"},
    },
    {
        "path": "cse/sem-7/bcs702-parallel-computing/module-4/topics/cache-coherence-and-false-sharing-in-openmp",
        "issue": "LOW_QUALITY",
        "prev_scores": {"minimax": "R=5 C=2 Q=3 T=3", "chutes": "R=9 C=6 Q=7 T=6"},
    },
    # FIX_FILES (2): High-rated topics with JSON issues
    {
        "path": "cse/sem-3/bcs301-mathematics-for-computer-science/module-1/topics/exponential-distribution",
        "issue": "FIX_FILES",
        "prev_scores": {"minimax": "R=9 C=7 Q=7 T=6", "chutes": "R=10 C=9 Q=8 T=7"},
    },
    {
        "path": "cse/sem-3/bcs301-mathematics-for-computer-science/module-2/topics/markov-chains",
        "issue": "FIX_FILES",
        "prev_scores": {"minimax": "R=9 C=6 Q=7 T=8", "chutes": "R=10 C=6 Q=7 T=6"},
    },
]

# ── Rating prompt (copied from quality_gate.py) ─────────────────────────
RATING_PROMPT = """\
You are an expert educational content reviewer.

Rate this topic on FOUR dimensions:

1. **Subject Relevance** (1-10) — Does content match the stated subject and topic?
   - Use sibling topics for disambiguation.
   - Score 1-3 if content is about a COMPLETELY DIFFERENT subject/domain.
   - Score 4-6 if partially relevant with significant off-topic sections.
   - Score 7-10 if properly aligned.

2. **Coverage** (1-10) — Are key concepts covered with appropriate depth?

3. **Content Quality** (1-10) — Accuracy, clarity, well-crafted MCQs?

4. **Tier Appropriateness** (1-10) — Is the depth right for Standard (B.Tech, MSc, MCA)?
   Expected depth: Thorough theory with proofs where needed.
   Expected language: Formal academic. Technical vocabulary expected.
   Expected MCQ style: Hard — application, analysis, numerical problems
   Expected read.md length: 200-250 lines

Respond ONLY with valid JSON (no markdown fences, no extra text):
{
  "relevance": <1-10>,
  "relevance_remarks": "<brief>",
  "coverage": <1-10>,
  "coverage_remarks": "<brief>",
  "quality": <1-10>,
  "quality_remarks": "<brief>",
  "tier": <1-10>,
  "tier_remarks": "<brief>",
  "suggestions": ["<suggestion 1>", "<suggestion 2>"]
}"""

import re


def _slug_to_title(slug):
    cleaned = re.sub(r'^[a-z]{2,5}\d{3}[a-z]?-', '', slug)
    return cleaned.replace('-', ' ').title()


def load_topic_content(topic_path):
    """Load topic content for rating (matches quality_gate.py format)."""
    topic_dir = Path(topic_path)
    topic_slug = topic_dir.name
    parts_list = topic_dir.parts

    # Extract context
    topics_idx = None
    for i, part in enumerate(parts_list):
        if part == "topics":
            topics_idx = i
            break

    subject_slug = parts_list[topics_idx - 2] if topics_idx and topics_idx >= 2 else ""
    module_slug = parts_list[topics_idx - 1] if topics_idx else ""

    # Read module _index.json
    module_dir = topic_dir.parent.parent
    module_index = module_dir / '_index.json'
    module_name = _slug_to_title(module_slug)
    topic_name = topic_slug.replace('-', ' ').title()
    siblings = []

    if module_index.exists():
        try:
            mdata = json.loads(module_index.read_text())
            module_name = mdata.get('chapterTitle', mdata.get('title', module_name))
            for t in mdata.get('topics', []):
                if t.get('id') == topic_slug:
                    topic_name = t.get('title', topic_name)
                else:
                    siblings.append(t.get('title', t.get('id', '')))
        except Exception:
            pass

    # Read subject _index.json
    subject_dir = module_dir.parent
    subject_index = subject_dir / '_index.json'
    subject_name = _slug_to_title(subject_slug)

    if subject_index.exists():
        try:
            sdata = json.loads(subject_index.read_text())
            subject_name = sdata.get('subjectName', sdata.get('title', subject_name))
        except Exception:
            pass

    sem_dir = subject_dir.parent
    semester = sem_dir.name.replace('-', ' ').title() if 'sem' in sem_dir.name else ''

    siblings_str = ", ".join(siblings) or "(none)"
    content_parts = [
        f"SUBJECT: {subject_name}",
        f"MODULE: {module_name}",
        f"TOPIC: {topic_name}",
        f"SEMESTER: {semester}",
        f"SIBLING TOPICS: {siblings_str}",
        "",
    ]

    # read.md (first 3000 chars)
    read_path = topic_dir / "read.md"
    if read_path.exists():
        content = read_path.read_text(encoding="utf-8", errors="replace")
        content_parts.append("--- read.md (first 3000 chars) ---")
        content_parts.append(content[:3000])
    else:
        content_parts.append("--- read.md --- [MISSING]")

    # First MCQ
    mcqs_path = topic_dir / "mcqs.json"
    if mcqs_path.exists():
        try:
            mcqs = json.loads(mcqs_path.read_text(encoding="utf-8", errors="replace"))
            mcq_list = mcqs.get("mcqs", []) if isinstance(mcqs, dict) else mcqs if isinstance(mcqs, list) else []
            if mcq_list:
                content_parts.append("\n--- First MCQ ---")
                content_parts.append(json.dumps(mcq_list[0], indent=2)[:500])
        except Exception:
            pass

    return "\n".join(content_parts)


def call_model(model_name, messages, timeout=120):
    """Call a model API and return (parsed_json, elapsed_seconds, error)."""
    cfg = MODELS[model_name]
    payload = json.dumps({
        "model": cfg["model"],
        "max_tokens": 800,
        "temperature": 0.3,
        "messages": messages,
    }).encode()

    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        cfg["base_url"], data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {cfg['api_key']}",
        },
        method="POST",
    )

    try:
        start = time.time()
        resp = urllib.request.urlopen(req, timeout=cfg["timeout"], context=ctx)
        result = json.loads(resp.read().decode())
        elapsed = time.time() - start

        message = result.get("choices", [{}])[0].get("message", {})
        text = message.get("content", "") or message.get("reasoning_content", "")

        # Strip <think> tags
        if '<think>' in text and '</think>' in text:
            end = text.find('</think>')
            if end != -1:
                text = text[end + 8:]

        text = text.strip()

        # Parse JSON
        cleaned = text
        if cleaned.startswith("```"):
            nl = cleaned.find("\n")
            if nl != -1:
                cleaned = cleaned[nl + 1:]
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]
            cleaned = cleaned.strip()
        first = cleaned.find("{")
        last = cleaned.rfind("}")
        if first != -1 and last != -1 and first < last:
            cleaned = cleaned[first:last + 1]

        parsed = json.loads(cleaned)
        return parsed, elapsed, None

    except json.JSONDecodeError as e:
        return None, time.time() - start, f"JSON parse error: {e}"
    except Exception as e:
        return None, 0, str(e)


def benchmark_topic(topic_info, model_name):
    """Rate one topic with one model. Returns (model, topic_path, result)."""
    content = load_topic_content(topic_info["path"])
    messages = [
        {"role": "system", "content": RATING_PROMPT},
        {"role": "user", "content": content},
    ]

    parsed, elapsed, error = call_model(model_name, messages)

    if error:
        return model_name, topic_info["path"], {
            "error": error,
            "elapsed": elapsed,
            "scores": None,
        }

    return model_name, topic_info["path"], {
        "error": None,
        "elapsed": round(elapsed, 1),
        "scores": {
            "R": parsed.get("relevance"),
            "C": parsed.get("coverage"),
            "Q": parsed.get("quality"),
            "T": parsed.get("tier"),
        },
        "remarks": {
            "relevance": parsed.get("relevance_remarks", ""),
            "coverage": parsed.get("coverage_remarks", ""),
            "quality": parsed.get("quality_remarks", ""),
            "tier": parsed.get("tier_remarks", ""),
        },
    }


def main():
    print(f"{'='*100}")
    print(f"  MODEL BENCHMARK — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Testing {len(MODELS)} models on {len(SAMPLE_TOPICS)} problematic topics")
    print(f"{'='*100}\n")

    results = {}  # {topic_path: {model_name: result}}

    # Rate all topics × all models in parallel (one model at a time to avoid rate limits)
    for model_name in MODELS:
        print(f"\n--- Testing: {model_name} ({MODELS[model_name]['model']}) ---")
        model_results = {}

        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = {}
            for topic in SAMPLE_TOPICS:
                f = executor.submit(benchmark_topic, topic, model_name)
                futures[f] = topic["path"]

            for f in as_completed(futures):
                mname, tpath, res = f.result()
                model_results[tpath] = res
                tslug = Path(tpath).name
                if res["error"]:
                    print(f"  [{tslug:40s}] ERROR: {res['error'][:60]}")
                else:
                    s = res["scores"]
                    print(f"  [{tslug:40s}] R={s['R']:>2} C={s['C']:>2} Q={s['Q']:>2} T={s['T']:>2}  ({res['elapsed']}s)")

        for tpath, res in model_results.items():
            results.setdefault(tpath, {})[model_name] = res

    # ── Summary Table ────────────────────────────────────────────────────
    print(f"\n\n{'='*140}")
    print("COMPARISON TABLE")
    print(f"{'='*140}")

    model_names = list(MODELS.keys())

    # Header
    header = f"{'Topic':50s} {'Issue':15s}"
    for m in model_names:
        header += f" | {m:>20s}"
    print(header)
    print("-" * 140)

    # Per-topic rows
    model_totals = {m: {"R": [], "C": [], "Q": [], "T": [], "time": [], "errors": 0} for m in model_names}

    for topic in SAMPLE_TOPICS:
        tpath = topic["path"]
        tslug = Path(tpath).name[:48]
        row = f"{tslug:50s} {topic['issue']:15s}"
        for m in model_names:
            res = results.get(tpath, {}).get(m)
            if not res or res["error"]:
                row += f" | {'ERROR':>20s}"
                model_totals[m]["errors"] += 1
            else:
                s = res["scores"]
                row += f" | R={s['R']:>1} C={s['C']:>1} Q={s['Q']:>1} T={s['T']:>1} {res['elapsed']:>5.1f}s"
                for k in ["R", "C", "Q", "T"]:
                    if s[k] is not None:
                        model_totals[m][k].append(s[k])
                model_totals[m]["time"].append(res["elapsed"])
        print(row)

    # Averages
    print("-" * 140)
    avg_row = f"{'AVERAGE':50s} {'':15s}"
    for m in model_names:
        mt = model_totals[m]
        if mt["R"]:
            avg_r = sum(mt["R"]) / len(mt["R"])
            avg_c = sum(mt["C"]) / len(mt["C"])
            avg_q = sum(mt["Q"]) / len(mt["Q"])
            avg_t = sum(mt["T"]) / len(mt["T"])
            avg_time = sum(mt["time"]) / len(mt["time"])
            avg_row += f" | R={avg_r:.1f} C={avg_c:.1f} Q={avg_q:.1f} T={avg_t:.1f} {avg_time:>4.1f}s"
        else:
            avg_row += f" | {'ALL ERRORS':>20s}"
    print(avg_row)

    # Cost estimate
    print(f"\n{'='*80}")
    print("COST ESTIMATE (per 1700 topics, ~4K tokens/topic input, ~400 tokens output)")
    print(f"{'='*80}")
    for m in model_names:
        cfg = MODELS[m]
        cost_in = 1700 * 4000 / 1_000_000 * cfg["cost_per_mtok"]["in"]
        cost_out = 1700 * 400 / 1_000_000 * cfg["cost_per_mtok"]["out"]
        total = cost_in + cost_out
        errors = model_totals[m]["errors"]
        avg_t = (sum(model_totals[m]["time"]) / len(model_totals[m]["time"])) if model_totals[m]["time"] else 0
        print(f"  {m:25s}: ${total:.2f} per full run, avg {avg_t:.1f}s/topic, {errors} errors")

    # Agreement analysis
    print(f"\n{'='*80}")
    print("AGREEMENT ANALYSIS (how often models agree on issue classification)")
    print(f"{'='*80}")
    for topic in SAMPLE_TOPICS:
        tpath = topic["path"]
        tslug = Path(tpath).name[:40]
        verdicts = {}
        for m in model_names:
            res = results.get(tpath, {}).get(m)
            if not res or res["error"]:
                verdicts[m] = "ERR"
                continue
            s = res["scores"]
            avg_rcqt = (s["R"] + s["C"] + s["Q"] + s["T"]) / 4
            if s["R"] <= 4:
                verdicts[m] = "WRONG_SUBJ"
            elif s["T"] <= 4:
                verdicts[m] = "WRONG_TIER"
            elif s["Q"] <= 4 or s["C"] <= 4:
                verdicts[m] = "LOW_QUAL"
            else:
                verdicts[m] = "PASS"
        verdict_strs = [f"{m[:8]}={verdicts[m]}" for m in model_names]
        actual = topic["issue"]
        print(f"  {tslug:42s} [{actual:15s}] → {', '.join(verdict_strs)}")

    # Save raw results
    out_path = "cse/reports/benchmark_models_results.json"
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "models": {m: MODELS[m]["model"] for m in model_names},
            "topics": [{
                "path": t["path"],
                "issue": t["issue"],
                "prev_scores": t["prev_scores"],
                "results": {m: results.get(t["path"], {}).get(m) for m in model_names},
            } for t in SAMPLE_TOPICS],
        }, f, indent=2, default=str)
    print(f"\nRaw results saved to: {out_path}")


if __name__ == "__main__":
    main()
