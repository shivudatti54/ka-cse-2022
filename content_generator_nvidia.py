#!/usr/bin/env python3
"""
NVIDIA Content Generator — fills ALL placeholder content for VTU study-app topics.

Reads placeholder topic lists for sem-5, sem-6, sem-7.  For each topic it calls
NVIDIA NIM API (Llama-3.1-405B) to generate:
  read.md, purpose.md, summary.md, flashcards.json, mcqs.json,
  memory.json, questions.json, visual.json, code.json

Usage:
    export NVIDIA_API_KEY="nvapi-..."
    python3 nvidia_content_generator.py                 # all semesters
    python3 nvidia_content_generator.py --sem 5         # only sem-5
    python3 nvidia_content_generator.py --topic dvr     # single topic (partial match)
    python3 nvidia_content_generator.py --dry-run       # preview, no API calls
    python3 nvidia_content_generator.py --resume        # skip topics already filled
"""

import json
import os
import ssl
import sys
import time
import re
import argparse
from pathlib import Path

# ─── Configuration ──────────────────────────────────────────────────────────
API_URL  = "https://integrate.api.nvidia.com/v1/chat/completions"
MODEL    = "meta/llama-3.1-405b-instruct"
MAX_TOKENS   = 12000
TEMPERATURE  = 0.3
TIMEOUT      = 300       # seconds per API call
DELAY        = 2         # seconds between API calls

SCRIPT_DIR = Path(__file__).resolve().parent          # .../vtu-2022-scheme/
REPO_ROOT  = SCRIPT_DIR.parent.parent                 # .../study-app-template/

PLACEHOLDER_FILES = [
    SCRIPT_DIR / "cse/sem-5/sem5-new-placeholder-files.txt",
    SCRIPT_DIR / "cse/sem-6/sem6-new-placeholder-files.txt",
    SCRIPT_DIR / "cse/sem-7/bcs703-new-placeholder-files.txt",
]

# Files we generate (in order)
CONTENT_FILES = [
    "read.md", "purpose.md", "summary.md",
    "flashcards.json", "mcqs.json", "memory.json",
    "questions.json", "visual.json", "code.json",
]

# ─── Prompts ────────────────────────────────────────────────────────────────

MARKDOWN_SYSTEM = r"""You are an expert university lecturer creating study material for VTU (Visvesvaraya Technological University) 2022 Scheme, Computer Science & Engineering branch.

Given a subject, module number, and topic — generate three pieces of content.
Return your response in EXACTLY this delimited format (no extra text before/after):

===READ_MD===
<comprehensive study material in markdown, 1500-3000 words>
===PURPOSE_MD===
<learning objectives in markdown>
===SUMMARY_MD===
<concise revision notes in markdown, 400-800 words>
===END===

FORMAT RULES for read.md:
- Start with: # <Topic Title>
- Use ## for major sections, ### for sub-sections
- Include an Introduction section
- Cover all key concepts, definitions, formulas, diagrams (described in text)
- Include relevant examples
- End with ## Exam Tips section listing 4-6 exam-relevant points
- Write at B.E./B.Tech level — accurate, detailed, exam-focused

FORMAT RULES for purpose.md:
- Start with: # Learning Objectives
- Then: "After studying this topic, you should be able to:"
- Numbered list of 5-7 specific, measurable learning outcomes

FORMAT RULES for summary.md:
- Start with: # <Topic Title> - Summary
- Bullet points covering all key definitions and concepts
- Section: ### Important Formulas, Definitions, and Theorems
- Section: ### Key Points (5-8 bullet points)
- End with: ### Revision Tips (3-4 practical tips)

IMPORTANT: Return ONLY the delimited content. No JSON wrapping. No markdown fences around the whole response."""

ASSESSMENT_SYSTEM = r"""You are an expert exam paper setter for VTU 2022 Scheme, CSE branch.

Given topic content, generate assessment materials as a single JSON object.
Return ONLY valid JSON — no markdown fences, no explanation outside the JSON.

{
  "flashcards": {
    "topicId": "TOPIC_ID",
    "flashcards": [
      {"id": "fc1", "front": "question text", "back": "detailed answer (1-3 sentences)"}
    ]
  },
  "mcqs": {
    "topicId": "TOPIC_ID",
    "mcqs": [
      {
        "id": "mcq-1",
        "question": "question text",
        "options": ["option A text", "option B text", "option C text", "option D text"],
        "correctAnswer": "A",
        "explanation": "why A is correct",
        "difficulty": "easy"
      }
    ]
  },
  "memory": {
    "topicId": "TOPIC_ID",
    "mnemonics": [
      {"id": "m1", "title": "Mnemonic title", "content": "Mnemonic content — acronym or memory aid"}
    ]
  },
  "questions": {
    "topicId": "TOPIC_ID",
    "questions": [
      {
        "id": "q1",
        "type": "short",
        "question": "question text",
        "expectedPoints": ["point 1", "point 2"],
        "marks": 5
      }
    ]
  },
  "code": {
    "topicId": "TOPIC_ID",
    "examples": [
      {
        "id": "pseudocode-name",
        "title": "Algorithm: Title",
        "description": "what this demonstrates",
        "language": "pseudocode",
        "code": "ALGORITHM Name\nBEGIN\n  step\nEND",
        "explanation": "explanation"
      }
    ]
  }
}

GENERATION RULES:
- flashcards: Generate 8-10 cards covering key concepts. Front = concise question, Back = detailed answer.
- mcqs: Generate 6-8 questions. Mix difficulties: 2 easy, 3-4 medium, 1-2 hard. correctAnswer is A/B/C/D letter.
- memory: Generate 4-5 mnemonics — acronyms, rhymes, or associations to remember key lists/concepts.
- questions: Generate 5-7 — mix of "short" (5 marks, 3-5 expected points) and "long" (10 marks, 5-7 points).
- code: Generate 2-3 examples IF the topic is code-applicable (algorithms, protocols, data structures, computations). Use languages: pseudocode (mandatory if applicable), python, c, or java. If topic is purely conceptual (history, definitions-only), set "examples": [].

IMPORTANT:
- "language" for code must be one of: pseudocode, python, c, java
- topicId must exactly match "TOPIC_ID" everywhere
- Return ONLY the JSON object"""


# ─── Helpers ────────────────────────────────────────────────────────────────

def call_api(api_key, messages):
    """Call NVIDIA NIM API. Returns parsed JSON response."""
    import urllib.request, urllib.error
    payload = json.dumps({
        "model": MODEL, "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE, "messages": messages,
    }).encode()
    ctx = ssl.create_default_context()
    req = urllib.request.Request(API_URL, data=payload, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }, method="POST")
    resp = urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)
    return json.loads(resp.read().decode())


def extract_text(response):
    """Extract text content from API response."""
    return response.get("choices", [{}])[0].get("message", {}).get("content", "").strip()


def extract_json(response):
    """Extract and parse JSON from API response, stripping fences."""
    text = extract_text(response)
    # Strip markdown fences
    if text.startswith("```"):
        text = text[text.index("\n")+1:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()
    # Find JSON object
    start = text.find("{")
    if start == -1:
        raise ValueError("No JSON object found")
    depth, end = 0, -1
    for i in range(start, len(text)):
        if text[i] == "{": depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0: end = i; break
    if end == -1:
        raise ValueError("Unclosed JSON object")
    return json.loads(text[start:end+1])


def is_placeholder(filepath):
    """True if the file is a placeholder (empty JSON or bare markdown header)."""
    try:
        content = filepath.read_text(encoding="utf-8").strip()
        if content in ("", "[]"):
            return True
        if content.startswith("#") and content.count("\n") <= 1 and len(content) < 200:
            return True
        return False
    except Exception:
        return True


def get_topic_context(topic_dir):
    """Extract subject/module/topic metadata from the directory path."""
    parts = topic_dir.parts
    # Walk up: topics/<id> -> module-N -> chapters -> <subject> -> sem-N
    try:
        ti = len(parts) - 1                      # topic_id
        topics_i = ti - 1                         # "topics"
        module_i = topics_i - 1                   # "module-N"
        chapters_i = module_i - 1                 # "chapters"
        subject_i = chapters_i - 1                # subject dir name
        sem_i = subject_i - 1                     # sem-N
    except Exception:
        return None

    topic_id    = parts[ti]
    module_id   = parts[module_i]
    subject_dir = parts[subject_i]
    sem_dir     = parts[sem_i]

    # Parse subject code + name
    m = re.match(r"(bcsl?\d+[a-d]?)-(.+)", subject_dir)
    if m:
        subject_code = m.group(1).upper()
        subject_name = m.group(2).replace("-", " ").title()
    else:
        subject_code = subject_dir.upper()
        subject_name = subject_dir.replace("-", " ").title()

    module_num = module_id.split("-")[-1]

    # Get proper title and sibling topics from _index.json
    topic_title = topic_id.replace("-", " ").title()
    sibling_topics = []
    index_path = topic_dir.parent.parent / "_index.json"
    if index_path.is_file():
        try:
            idx = json.loads(index_path.read_text(encoding="utf-8"))
            for t in idx.get("topics", []):
                sibling_topics.append(t.get("title", t.get("id", "")))
                if t.get("id") == topic_id:
                    topic_title = t.get("title", topic_title)
        except Exception:
            pass

    return {
        "topic_id":    topic_id,
        "topic_title": topic_title,
        "module_num":  module_num,
        "module_id":   module_id,
        "subject_code": subject_code,
        "subject_name": subject_name,
        "sem":         sem_dir.replace("sem-", ""),
        "siblings":    sibling_topics,
    }


# ─── Discovery ──────────────────────────────────────────────────────────────

def discover_topics(placeholder_files, sem_filter=None, topic_filter=None):
    """Parse placeholder file lists and return unique topic directory Paths."""
    seen = set()
    topic_dirs = []
    for pf in placeholder_files:
        if not pf.is_file():
            print(f"  WARN: {pf.name} not found, skipping")
            continue
        if sem_filter:
            if f"sem-{sem_filter}" not in str(pf) and f"sem{sem_filter}" not in str(pf):
                continue
        for raw_line in pf.read_text().splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            # Resolve path: try absolute, then relative to REPO_ROOT, then SCRIPT_DIR
            p = Path(line)
            if not p.is_absolute():
                # sem-6/7 files use paths like "content-packs/vtu-2022-scheme/cse/..."
                candidate = REPO_ROOT / line
                if candidate.exists() or "content-packs" in line:
                    p = candidate
                else:
                    p = SCRIPT_DIR / line
            # Derive topic dir from "topics/<topic-id>/..."
            if "topics" not in p.parts:
                continue
            ti = p.parts.index("topics")
            if ti + 1 >= len(p.parts):
                continue
            topic_dir = Path(*p.parts[:ti+2])
            key = str(topic_dir)
            if key not in seen and topic_dir.is_dir():
                if topic_filter and topic_filter not in topic_dir.name:
                    continue
                seen.add(key)
                topic_dirs.append(topic_dir)
    return topic_dirs


# ─── Generation ─────────────────────────────────────────────────────────────

def generate_markdown(api_key, ctx):
    """Call 1: Generate read.md + purpose.md + summary.md. Returns dict or None."""
    siblings_str = ", ".join(ctx["siblings"][:15]) if ctx["siblings"] else "(no sibling info)"
    user_msg = (
        f'Subject: {ctx["subject_code"]} — {ctx["subject_name"]} (VTU 2022, Sem {ctx["sem"]})\n'
        f'Module {ctx["module_num"]} topics: {siblings_str}\n\n'
        f'Generate content for the topic: "{ctx["topic_title"]}"\n'
        f'Topic ID: {ctx["topic_id"]}'
    )
    messages = [
        {"role": "system", "content": MARKDOWN_SYSTEM},
        {"role": "user",   "content": user_msg},
    ]
    resp = call_api(api_key, messages)
    text = extract_text(resp)

    result = {}
    for key, start_tag, end_tag in [
        ("read_md",    "===READ_MD===",    "===PURPOSE_MD==="),
        ("purpose_md", "===PURPOSE_MD===", "===SUMMARY_MD==="),
        ("summary_md", "===SUMMARY_MD===", "===END==="),
    ]:
        s = text.find(start_tag)
        e = text.find(end_tag) if end_tag != "===END===" else text.find("===END===")
        if end_tag == "===END===" and e == -1:
            e = len(text)
        if s == -1:
            result[key] = ""
        else:
            chunk = text[s + len(start_tag):e].strip() if e > s else text[s + len(start_tag):].strip()
            result[key] = chunk

    # Fallback: if delimiters missing, try to split by headers
    if not result.get("read_md"):
        # Take the whole text as read_md
        result["read_md"] = text
    if not result.get("purpose_md"):
        result["purpose_md"] = (
            f"# Learning Objectives\n\n"
            f"After studying this topic, you should be able to:\n\n"
            f"1. Understand the fundamentals of {ctx['topic_title']}.\n"
            f"2. Explain key concepts related to {ctx['topic_title']}.\n"
            f"3. Apply the principles of {ctx['topic_title']} in problem solving.\n"
        )
    if not result.get("summary_md"):
        result["summary_md"] = f"# {ctx['topic_title']} - Summary\n\n(Summary to be added.)"

    return result


def generate_assessment(api_key, ctx, read_content):
    """Call 2: Generate all JSON assessment files. Returns parsed dict or None."""
    # Truncate read content if very long
    rc = read_content[:6000] if len(read_content) > 6000 else read_content
    prompt = ASSESSMENT_SYSTEM.replace("TOPIC_ID", ctx["topic_id"])
    user_msg = (
        f'Subject: {ctx["subject_code"]} — {ctx["subject_name"]} (Sem {ctx["sem"]})\n'
        f'Topic: "{ctx["topic_title"]}" (id: {ctx["topic_id"]})\n\n'
        f'== TOPIC CONTENT ==\n{rc}\n\n'
        f'Generate assessment materials. topicId must be exactly "{ctx["topic_id"]}".\n'
        f'Return ONLY the JSON object.'
    )
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user",   "content": user_msg},
    ]
    resp = call_api(api_key, messages)
    data = extract_json(resp)

    # Fix topicId everywhere
    for key in ("flashcards", "mcqs", "memory", "questions", "code"):
        if key in data and isinstance(data[key], dict):
            data[key]["topicId"] = ctx["topic_id"]

    return data


def write_visual_json(topic_dir, ctx):
    """Write visual.json without API call — just metadata pointing to the SVG."""
    vj = {
        "topicId": ctx["topic_id"],
        "visuals": [{
            "id": f"{ctx['topic_id']}-svg",
            "title": ctx["topic_title"],
            "description": f"Diagram for {ctx['topic_title']}",
            "type": "svg",
            "file": f"assets/{ctx['topic_id']}.svg",
            "animated": False,
        }]
    }
    (topic_dir / "visual.json").write_text(
        json.dumps(vj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def update_index_flags(topic_dir, ctx):
    """Set hasVisual and hasQuestions to true in the module's _index.json."""
    index_path = topic_dir.parent.parent / "_index.json"
    if not index_path.is_file():
        return
    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
        changed = False
        for t in data.get("topics", []):
            if t.get("id") == ctx["topic_id"]:
                if not t.get("hasQuestions"):
                    t["hasQuestions"] = True
                    changed = True
                break
        if changed:
            index_path.write_text(
                json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
    except Exception:
        pass


# ─── Processing ─────────────────────────────────────────────────────────────

def process_topic(api_key, topic_dir, ctx, resume=False):
    """Generate all content for one topic. Returns status string."""
    tid = ctx["topic_id"]

    # Check if already filled (resume mode)
    if resume:
        read_path = topic_dir / "read.md"
        mcqs_path = topic_dir / "mcqs.json"
        if read_path.is_file() and not is_placeholder(read_path) \
           and mcqs_path.is_file() and not is_placeholder(mcqs_path):
            return "skip-filled"

    # ── Call 1: Markdown content ──
    print(f"    [1/2] Generating markdown content...")
    t0 = time.time()
    md = generate_markdown(api_key, ctx)
    print(f"          Done in {time.time()-t0:.1f}s")

    # Write markdown files
    (topic_dir / "read.md").write_text(md["read_md"], encoding="utf-8")
    (topic_dir / "purpose.md").write_text(md["purpose_md"], encoding="utf-8")
    (topic_dir / "summary.md").write_text(md["summary_md"], encoding="utf-8")

    time.sleep(DELAY)

    # ── Call 2: Assessment JSON ──
    print(f"    [2/2] Generating assessment content...")
    t0 = time.time()
    assess = generate_assessment(api_key, ctx, md["read_md"])
    print(f"          Done in {time.time()-t0:.1f}s")

    # Write JSON files
    file_map = {
        "flashcards.json": assess.get("flashcards", {"topicId": tid, "flashcards": []}),
        "mcqs.json":       assess.get("mcqs",       {"topicId": tid, "mcqs": []}),
        "memory.json":     assess.get("memory",     {"topicId": tid, "mnemonics": []}),
        "questions.json":  assess.get("questions",   {"topicId": tid, "questions": []}),
        "code.json":       assess.get("code",        {"topicId": tid, "examples": []}),
    }
    for fname, data in file_map.items():
        (topic_dir / fname).write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    # Write visual.json (no API call)
    write_visual_json(topic_dir, ctx)

    # Update _index.json flags
    update_index_flags(topic_dir, ctx)

    return "generated"


# ─── Main ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="NVIDIA Content Generator for VTU placeholder topics")
    parser.add_argument("--sem", type=int, choices=[5, 6, 7], help="Process only this semester")
    parser.add_argument("--topic", type=str, help="Process only topics matching this substring")
    parser.add_argument("--dry-run", action="store_true", help="List topics without making API calls")
    parser.add_argument("--resume", action="store_true", help="Skip topics that already have content")
    args = parser.parse_args()

    api_key = os.environ.get("NVIDIA_API_KEY", "")
    if not api_key and not args.dry_run:
        print("ERROR: Set NVIDIA_API_KEY environment variable")
        print("  export NVIDIA_API_KEY='nvapi-...'")
        sys.exit(1)

    # Discover topics
    print("Discovering placeholder topics...")
    topic_dirs = discover_topics(
        PLACEHOLDER_FILES,
        sem_filter=str(args.sem) if args.sem else None,
        topic_filter=args.topic,
    )
    print(f"Found {len(topic_dirs)} topics to process\n")

    if not topic_dirs:
        print("No topics found. Check placeholder files exist.")
        sys.exit(0)

    # Dry run
    if args.dry_run:
        for i, td in enumerate(topic_dirs, 1):
            ctx = get_topic_context(td)
            if ctx:
                print(f"  {i:3d}. [{ctx['subject_code']} M{ctx['module_num']}] {ctx['topic_title']}")
            else:
                print(f"  {i:3d}. {td}")
        print(f"\nTotal: {len(topic_dirs)} topics × 2 API calls = {len(topic_dirs)*2} calls")
        return

    # Process
    print(f"NVIDIA Content Generator")
    print(f"Model: {MODEL}")
    print(f"Topics: {len(topic_dirs)} | API calls: ~{len(topic_dirs)*2}")
    print(f"{'='*70}\n")

    stats = {"generated": 0, "skipped": 0, "failed": 0}

    for i, td in enumerate(topic_dirs, 1):
        ctx = get_topic_context(td)
        if not ctx:
            print(f"[{i}/{len(topic_dirs)}] SKIP (cannot parse context): {td}")
            stats["skipped"] += 1
            continue

        label = f"[{i}/{len(topic_dirs)}] {ctx['subject_code']} M{ctx['module_num']}: {ctx['topic_title']}"
        print(label)

        try:
            status = process_topic(api_key, td, ctx, resume=args.resume)
            if status == "skip-filled":
                print(f"    SKIP (already has content)")
                stats["skipped"] += 1
            else:
                stats["generated"] += 1
                print(f"    OK — all 9 files written")
        except KeyboardInterrupt:
            print("\n\nInterrupted by user.")
            break
        except Exception as e:
            print(f"    FAILED: {e}")
            stats["failed"] += 1

        # Delay between topics
        if i < len(topic_dirs):
            time.sleep(DELAY)

    # Summary
    print(f"\n{'='*70}")
    print(f"  SUMMARY")
    print(f"{'='*70}")
    print(f"  Total topics:  {len(topic_dirs)}")
    print(f"  Generated:     {stats['generated']}")
    print(f"  Skipped:       {stats['skipped']}")
    print(f"  Failed:        {stats['failed']}")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
