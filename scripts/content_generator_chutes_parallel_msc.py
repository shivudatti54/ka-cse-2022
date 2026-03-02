#!/usr/bin/env python3
"""
VTU Content Generator - Chutes Parallel

Generates content for VTU topics using DeepSeek-R1 with parallel processing.
- 25 concurrent workers
- 6-minute timeout with 15-second monitoring
- Smart batching (2 API calls per topic)
- Progress tracking and resume support

Usage:
  python3 content_generator_minimax_parallel.py topic-paths.txt --start-from 301
  python3 content_generator_minimax_parallel.py topic-paths.txt --resume --workers 25
"""

import argparse
import json
import re
import ssl
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from threading import Lock, Event, Thread

# ── Configuration ──────────────────────────────────────────────────────────
API_CONFIG = {
    "base_url": "https://llm.chutes.ai/v1/chat/completions",
    "api_key": "cpk_a744b82c5b9c4e8b9c7c8e1442e8d160.c3a84cdb26e850c9b8f358af872bca49.ymNhlwAf2nbhnTZJE620p8sv1aTgEGwx",
    "model": "deepseek-ai/DeepSeek-R1-TEE",
}

TIMEOUT = 360  # 6 minutes
HEARTBEAT_INTERVAL = 30  # Monitor every 30 seconds
MAX_TOKENS = 8192
TEMPERATURE = 0.3
DEFAULT_WORKERS = 25
PROGRESS_FILE = "chutes_msc_progress.json"

progress_lock = Lock()

# ── Prompts ────────────────────────────────────────────────────────────────
MARKDOWN_SYSTEM = """You are an expert university lecturer creating study material for University of Delhi (DU) NEP 2024, Computer Science program.

STUDENT PROFILE:
- University: University of Delhi (DU), Delhi, India — India's top central university
- Students: Postgraduate researchers and advanced CS students in MSc Computer Science program
- Exam pattern: Internal Assessment (25%) + End Semester Exam (75%)
- Content should be rigorous, conceptually deep, with real-world examples
- MSc CS is research-oriented — content must include current research context, theoretical depth, and advanced applications

Your task: Generate THREE markdown files for upgrading topic quality to 8+.

Return EXACTLY this delimited format (no extra text before/after):

===READ_MD===
# <Topic Title>

## Introduction
[2-3 paragraphs explaining the topic and its importance]

## Key Concepts
[Detailed explanations of all major concepts]

## Examples
[2-3 worked examples with step-by-step solutions]

## Exam Tips
[5-7 exam-relevant points for DU semester exams]

Length: 1500-3000 words, MSc CS (research-oriented) postgraduate level
===PURPOSE_MD===
# Learning Objectives

After studying this topic, you should be able to:

1. [Specific learning outcome]
2. [Specific learning outcome]
...
6-8 outcomes total
===SUMMARY_MD===
# <Topic Title> - Summary

## Key Definitions and Concepts
- [Concise definitions]

## Important Formulas and Theorems
- [All formulas with brief descriptions]

## Key Points
- [7-10 bullet points]

## Common Mistakes to Avoid
- [3-4 points]

## Revision Tips
- [3-4 practical tips]

Length: 400-800 words
===END===

IMPORTANT: Return ONLY the delimited content. No JSON wrapping.

CRITICAL OUTPUT RULES (MUST follow):
- Output ONLY in English. Never use Chinese, Japanese, Korean, or any non-Latin characters.
- Do NOT start with conversational preambles like "Of course", "Sure", "Certainly", "Here is a comprehensive", etc. Start directly with the content.
- Do NOT include metadata headers like "Subject:", "Module:", "Topic:" in the content body.
- Do NOT mention the target audience scope (no "B.Tech", "MSc", "MCA", "engineering students", "undergraduate students"). Write as if the reader is simply a student studying this topic.
- For memory aids/mnemonics: Do NOT use markdown bold (**text**). Use UPPERCASE for emphasis instead.
"""

ASSESSMENT_SYSTEM = """You are an expert exam paper setter for University of Delhi (DU) NEP 2024, Computer Science program.

Your task: Generate assessment materials as a SINGLE JSON object.

Return ONLY valid JSON (no markdown fences, no explanation):

{
  "flashcards": [
    {"id": "fc-1", "front": "Question text here?", "back": "Answer in 1-3 sentences."}
  ],
  "mcqs": [
    {
      "id": "mcq-1",
      "question": "Question text",
      "options": [
        {"key": "A", "text": "First option"},
        {"key": "B", "text": "Second option"},
        {"key": "C", "text": "Third option"},
        {"key": "D", "text": "Fourth option"}
      ],
      "correctAnswer": "A",
      "explanation": "Why A is correct",
      "difficulty": "easy"
    }
  ],
  "memory": {
    "mnemonics": [{"id": "m-1", "title": "Title", "content": "Mnemonic"}],
    "acronyms": [{"term": "TERM", "expansion": "Full form", "usage": "Usage"}],
    "visualTips": [{"concept": "Concept", "visualization": "How to visualize"}],
    "analogies": [{"concept": "Concept", "analogy": "Real-world analogy"}]
  },
  "questions": [
    {
      "id": "q-1",
      "type": "short",
      "question": "Question text",
      "keyPoints": ["Key point 1", "Key point 2"],
      "marks": 5
    }
  ],
  "visual": {
    "diagrams": [{"id": "d-1", "title": "Title", "description": "What it shows", "elements": ["E1"], "purpose": "Learning"}]
  },
  "code": [
    {
      "id": "code-1",
      "language": "pseudocode",
      "title": "Algorithm Title",
      "description": "What this demonstrates",
      "code": "ALGORITHM Name\\nBEGIN\\n  step1\\nEND",
      "explanation": "Explanation of the algorithm",
      "timeComplexity": "O(n)",
      "spaceComplexity": "O(1)"
    }
  ]
}

CRITICAL FORMAT RULES:
- MCQ options MUST be objects: [{"key": "A", "text": "..."}, ...] NOT plain strings
- questions use "keyPoints" (NOT "expectedPoints")
- code uses "timeComplexity"/"spaceComplexity" (NOT nested "complexity" object)
- All arrays need items with "id" fields

Requirements:
- 12-15 flashcards (id: fc-1, fc-2, ...)
- 15-20 MCQs (balanced easy/medium/hard, id: mcq-1, mcq-2, ...)
- 5-7 short questions (5 marks) + 3-4 long questions (10 marks), id: q-1, q-2, ...
- 2-4 code examples (pseudocode + C/Python/Java), id: code-1, code-2, ...
- Rich memory aids

IMPORTANT: Return ONLY valid JSON.

CRITICAL OUTPUT RULES (MUST follow):
- Output ONLY in English. Never use Chinese, Japanese, Korean, or any non-Latin characters.
- Do NOT start with conversational preambles like "Of course", "Sure", "Certainly", "Here is a comprehensive", etc. Start directly with the content.
- Do NOT include metadata headers like "Subject:", "Module:", "Topic:" in the content body.
- Do NOT mention the target audience scope (no "B.Tech", "MSc", "MCA", "engineering students", "undergraduate students"). Write as if the reader is simply a student studying this topic.
- For memory aids/mnemonics: Do NOT use markdown bold (**text**). Use UPPERCASE for emphasis instead.
"""

# ── API Functions with Heartbeat ───────────────────────────────────────────
def call_api_with_heartbeat(messages: list, topic_desc: str) -> dict:
    """Call Chutes API with timeout and heartbeat monitoring."""
    payload = json.dumps({
        "model": API_CONFIG["model"],
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
        "messages": messages,
    }).encode()

    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        API_CONFIG["base_url"],
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_CONFIG['api_key']}",
        },
        method="POST"
    )

    start_time = time.time()
    heartbeat_event = Event()

    def heartbeat():
        """Monitor API call progress."""
        while not heartbeat_event.is_set():
            if heartbeat_event.wait(HEARTBEAT_INTERVAL):
                break
            elapsed = time.time() - start_time
            print(f"  [{topic_desc}] Still waiting... {elapsed:.0f}s elapsed")

    heartbeat_thread = Thread(target=heartbeat, daemon=True)
    heartbeat_thread.start()

    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)
        result = json.loads(resp.read().decode())
        elapsed = time.time() - start_time
        print(f"  [{topic_desc}] ✓ API call completed in {elapsed:.1f}s")
        return result
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"  [{topic_desc}] ✗ API call failed after {elapsed:.1f}s: {str(e)[:100]}")
        raise
    finally:
        heartbeat_event.set()
        heartbeat_thread.join(timeout=1)

def extract_text(response: dict) -> str:
    """Extract text from Chutes API response."""
    try:
        message = response.get("choices", [{}])[0].get("message", {})

        # DeepSeek-R1 structure:
        # - 'content' = actual formatted output (what we want!)
        # - 'reasoning_content' = internal thinking process (not what we want)
        content = message.get("content", "")
        reasoning_content = message.get("reasoning_content", "")

        # Debug: print what we got
        if content:
            text = content
            field = "content"
        elif reasoning_content:
            text = reasoning_content
            field = "reasoning_content"
        else:
            # Try to find any text field
            print(f"    DEBUG: No content found. Message keys: {list(message.keys())}")
            print(f"    DEBUG: Full message: {str(message)[:500]}")
            return ""

        # Print first 200 chars to verify format
        preview = text[:200].replace('\n', ' ')
        print(f"    DEBUG: Got {len(text)} chars from '{field}': {preview}...")

        return text.strip()
    except Exception as e:
        print(f"    ERROR in extract_text: {e}")
        return ""

# ── Content Generation ─────────────────────────────────────────────────────
def generate_markdown_batch(topic_context: dict, topic_num: int) -> dict:
    """Call 1: Generate read.md + purpose.md + summary.md in ONE call."""
    topic_desc = f"{topic_num}:MD {topic_context['topic']}"

    siblings = topic_context.get('sibling_topics', [])
    siblings_str = "\nOther topics in this module: " + ", ".join(siblings) if siblings else ""

    user_prompt = f"""Generate content for this DU Computer Science topic:

Subject: {topic_context['subject']}
Module: {topic_context['module']}
Topic: {topic_context['topic']}{siblings_str}

IMPORTANT: Generate content ONLY about "{topic_context['topic']}" as it relates to "{topic_context['subject']}".
Do not confuse with similarly named topics from other subjects.

Follow the exact format specified in the system message."""

    messages = [
        {"role": "system", "content": MARKDOWN_SYSTEM},
        {"role": "user", "content": user_prompt}
    ]

    response = call_api_with_heartbeat(messages, topic_desc)
    content = extract_text(response)

    # Parse delimited format
    files = {}

    # Check if delimiters exist
    has_read = '===READ_MD===' in content
    has_purpose = '===PURPOSE_MD===' in content
    has_summary = '===SUMMARY_MD===' in content
    has_end = '===END===' in content
    print(f"    DEBUG: Delimiters found - READ:{has_read} PURPOSE:{has_purpose} SUMMARY:{has_summary} END:{has_end}")

    read_match = re.search(r'===READ_MD===\s*(.+?)\s*===PURPOSE_MD===', content, re.DOTALL)
    if read_match:
        files['read.md'] = read_match.group(1).strip()
        print(f"    DEBUG: Extracted read.md ({len(files['read.md'])} chars)")

    purpose_match = re.search(r'===PURPOSE_MD===\s*(.+?)\s*===SUMMARY_MD===', content, re.DOTALL)
    if purpose_match:
        files['purpose.md'] = purpose_match.group(1).strip()
        print(f"    DEBUG: Extracted purpose.md ({len(files['purpose.md'])} chars)")

    summary_match = re.search(r'===SUMMARY_MD===\s*(.+?)\s*===END===', content, re.DOTALL)
    if summary_match:
        files['summary.md'] = summary_match.group(1).strip()
        print(f"    DEBUG: Extracted summary.md ({len(files['summary.md'])} chars)")

    return files

def generate_assessment_batch(topic_context: dict, read_content: str, topic_num: int) -> dict:
    """Call 2: Generate all JSON files in ONE call."""
    topic_desc = f"{topic_num}:JSON {topic_context['topic']}"

    siblings = topic_context.get('sibling_topics', [])
    siblings_str = "\nOther topics in this module: " + ", ".join(siblings) if siblings else ""

    user_prompt = f"""Generate assessment materials for this DU Computer Science topic:

Subject: {topic_context['subject']}
Module: {topic_context['module']}
Topic: {topic_context['topic']}{siblings_str}

IMPORTANT: All questions, flashcards, and examples must be specifically about "{topic_context['topic']}" in the context of "{topic_context['subject']}".

Topic content summary:
{read_content[:500]}...

Return ONLY valid JSON as specified."""

    messages = [
        {"role": "system", "content": ASSESSMENT_SYSTEM},
        {"role": "user", "content": user_prompt}
    ]

    response = call_api_with_heartbeat(messages, topic_desc)
    content = extract_text(response)

    # Extract JSON
    original_len = len(content)
    content = content.strip()
    if content.startswith("```"):
        print(f"    DEBUG: Removing markdown fences")
        content = content[content.index("\n")+1:]
        if content.endswith("```"):
            content = content[:-3]
        content = content.strip()

    print(f"    DEBUG: JSON content length: {original_len} -> {len(content)} chars")
    print(f"    DEBUG: JSON preview: {content[:200]}...")

    try:
        data = json.loads(content)
        print(f"    DEBUG: JSON parsed successfully, keys: {list(data.keys())}")
        topic_id = topic_context.get('topic_slug', topic_context['topic'])
        files = {}

        # Wrap each content type with topicId for app compatibility
        flashcards = data.get('flashcards', [])
        for i, fc in enumerate(flashcards):
            if 'id' not in fc:
                fc['id'] = f'fc-{i+1}'
        files['flashcards.json'] = json.dumps({"topicId": topic_id, "flashcards": flashcards}, indent=2)

        mcqs = data.get('mcqs', [])
        for i, m in enumerate(mcqs):
            if 'id' not in m:
                m['id'] = f'mcq-{i+1}'
            # Fix string options -> object options
            if m.get('options') and isinstance(m['options'][0], str):
                keys = ["A", "B", "C", "D", "E", "F"]
                m['options'] = [{"key": keys[j], "text": t} for j, t in enumerate(m['options'])]
            if 'difficulty' not in m:
                m['difficulty'] = 'medium'
        files['mcqs.json'] = json.dumps({"topicId": topic_id, "mcqs": mcqs}, indent=2)

        memory = data.get('memory', {})
        if 'topicId' not in memory:
            memory['topicId'] = topic_id
        files['memory.json'] = json.dumps(memory, indent=2)

        questions = data.get('questions', [])
        for i, q in enumerate(questions):
            if 'id' not in q:
                q['id'] = f'q-{i+1}'
            if 'type' not in q:
                q['type'] = 'long' if q.get('marks', 0) >= 10 else 'short'
            # Normalize expectedPoints -> keyPoints
            if 'expectedPoints' in q and 'keyPoints' not in q:
                q['keyPoints'] = q.pop('expectedPoints')
        files['questions.json'] = json.dumps({"topicId": topic_id, "questions": questions}, indent=2)

        visual = data.get('visual', {})
        if 'topicId' not in visual:
            visual['topicId'] = topic_id
        files['visual.json'] = json.dumps(visual, indent=2)

        code_examples = data.get('code', [])
        for i, ex in enumerate(code_examples):
            if 'id' not in ex:
                ex['id'] = f'code-{i+1}'
            if 'language' not in ex:
                ex['language'] = 'pseudocode'
            if 'code' not in ex:
                ex['code'] = ex.get('pseudocode', ex.get('algorithm', '// No code'))
            # Normalize complexity object -> flat fields
            if 'complexity' in ex and isinstance(ex['complexity'], dict):
                if 'timeComplexity' not in ex and 'time' in ex['complexity']:
                    ex['timeComplexity'] = ex['complexity']['time']
                if 'spaceComplexity' not in ex and 'space' in ex['complexity']:
                    ex['spaceComplexity'] = ex['complexity']['space']
                del ex['complexity']
        files['code.json'] = json.dumps({"topicId": topic_id, "examples": code_examples}, indent=2)

        print(f"    DEBUG: Created {len(files)} JSON files (all wrapped with topicId)")
        return files
    except json.JSONDecodeError as e:
        print(f"    DEBUG: JSON parse error: {e}")
        print(f"    DEBUG: Failed content (first 500 chars): {content[:500]}")
        return {}

# ── Topic Processing ───────────────────────────────────────────────────────
def _slug_to_title(slug: str) -> str:
    """Convert directory slug to human-readable title.
    'bcs502-computer-networks' -> 'Computer Networks'
    'module-2' -> 'Module 2'
    'random-access' -> 'Random Access'
    """
    # Remove course code prefix (e.g., bcs502-, bcs306b-)
    cleaned = re.sub(r'^[a-z]{2,5}\d{3}[a-z]?-', '', slug)
    return cleaned.replace('-', ' ').title()


def get_topic_context(topic_path: str) -> dict:
    """Extract rich metadata from topic path and _index.json files."""
    topic_dir = Path(topic_path)
    parts = topic_dir.parts

    topics_idx = None
    for i, part in enumerate(parts):
        if part == "topics":
            topics_idx = i
            break

    if not topics_idx or topics_idx < 2:
        return {
            "subject": "Unknown",
            "module": "Unknown",
            "topic": parts[-1] if parts else "Unknown",
            "topic_slug": parts[-1] if parts else "unknown",
            "topic_dir": topic_path,
        }

    topic_slug = parts[-1]
    module_slug = parts[topics_idx - 1]
    subject_slug = parts[topics_idx - 2]

    # Defaults from slugs (fallback if _index.json not found)
    subject_name = _slug_to_title(subject_slug)
    module_name = _slug_to_title(module_slug)
    topic_name = _slug_to_title(topic_slug)

    # Read module _index.json for topic title and module title
    sibling_topics = []
    module_dir = topic_dir.parent.parent  # .../topics/<slug> -> .../module-N
    module_index = module_dir / '_index.json'
    if module_index.exists():
        try:
            with open(module_index) as f:
                mdata = json.load(f)
            module_name = mdata.get('chapterTitle', module_name)
            for t in mdata.get('topics', []):
                t_title = t.get('title', t.get('id', ''))
                if t.get('id') == topic_slug:
                    topic_name = t_title or topic_name
                else:
                    sibling_topics.append(t_title)
        except (json.JSONDecodeError, IOError):
            pass

    # Read subject _index.json for better module title
    subject_dir = module_dir.parent
    subject_index = subject_dir / '_index.json'
    if subject_index.exists():
        try:
            with open(subject_index) as f:
                sdata = json.load(f)
            if 'subjectName' in sdata:
                subject_name = sdata['subjectName']
            for ch in sdata.get('chapters', []):
                if ch.get('id') == module_slug:
                    module_name = ch.get('title', module_name)
                    break
        except (json.JSONDecodeError, IOError):
            pass

    return {
        "subject": subject_name,
        "module": module_name,
        "topic": topic_name,
        "topic_slug": topic_slug,
        "topic_dir": topic_path,
    }

def process_topic(topic_path: str, topic_num: int, total: int) -> dict:
    """Process one topic: generate all content files."""
    ctx = get_topic_context(topic_path)
    topic_dir = Path(topic_path)

    result = {
        "topic_path": topic_path,
        "topic_num": topic_num,
        "success": False,
        "files_written": 0,
        "error": None
    }

    print(f"\n[{topic_num}/{total}] START: {ctx['subject']} > {ctx['module']} > {ctx['topic']}")

    try:
        # Call 1: Markdown files
        markdown_files = generate_markdown_batch(ctx, topic_num)
        for filename, content in markdown_files.items():
            file_path = topic_dir / filename
            file_path.write_text(content, encoding='utf-8')
            result["files_written"] += 1

        # Call 2: Assessment files
        read_content = markdown_files.get('read.md', '')
        if read_content:
            assessment_files = generate_assessment_batch(ctx, read_content, topic_num)
            for filename, content in assessment_files.items():
                file_path = topic_dir / filename
                file_path.write_text(content, encoding='utf-8')
                result["files_written"] += 1

        result["success"] = result["files_written"] >= 7
        print(f"[{topic_num}/{total}] {'✅ DONE' if result['success'] else '⚠️ PARTIAL'}: {result['files_written']}/9 files")

    except Exception as e:
        result["error"] = str(e)[:200]
        print(f"[{topic_num}/{total}] ❌ FAILED: {result['error']}")

    return result

# ── Progress Tracking ──────────────────────────────────────────────────────
def load_progress() -> set:
    """Load completed topics from progress file."""
    if not Path(PROGRESS_FILE).exists():
        return set()
    try:
        data = json.loads(Path(PROGRESS_FILE).read_text())
        return set(data.get("completed", []))
    except:
        return set()

def save_progress(completed: set):
    """Save completed topics to progress file."""
    with progress_lock:
        Path(PROGRESS_FILE).write_text(json.dumps({
            "completed": list(completed),
            "last_updated": datetime.now().isoformat()
        }, indent=2))

# ── Main ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="VTU Content Generator - Chutes Parallel")
    parser.add_argument("paths_file", help="Text file with topic paths")
    parser.add_argument("--start-from", type=int, default=1, dest="start_from", help="Start from topic N")
    parser.add_argument("--end-at", type=int, default=0, dest="end_at", help="End at topic N (inclusive)")
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS, help=f"Number of workers (default {DEFAULT_WORKERS})")
    parser.add_argument("--resume", action="store_true", help="Skip completed topics")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    args = parser.parse_args()

    # Load topics
    paths_file = Path(args.paths_file)
    if not paths_file.exists():
        print(f"Error: File not found: {paths_file}")
        sys.exit(1)

    all_topics = [line.strip() for line in paths_file.read_text().splitlines() if line.strip()]

    # Apply filters
    completed = load_progress() if args.resume else set()
    topics = [t for t in all_topics if t not in completed] if args.resume else all_topics

    if args.start_from > 1:
        skip = args.start_from - 1
        if skip < len(topics):
            topics = topics[skip:]
            print(f"\n⏭️  Skipping first {skip} topics, starting from #{args.start_from}\n")

    if args.end_at > 0:
        if args.end_at < args.start_from:
            print(f"Error: --end-at ({args.end_at}) must be >= --start-from ({args.start_from})")
            sys.exit(1)
        keep_count = args.end_at - args.start_from + 1
        if keep_count <= 0:
            topics = []
        elif keep_count < len(topics):
            topics = topics[:keep_count]
            print(f"\n⏹️  Ending at topic #{args.end_at} (processing {keep_count} topics in selected range)\n")

    # Print header
    print(f"\n{'='*80}")
    print("VTU CONTENT GENERATOR - CHUTES PARALLEL")
    print(f"{'='*80}")
    print(f"Source file  : {paths_file.name}")
    print(f"Total topics : {len(all_topics)}")
    print(f"Processing   : {len(topics)} topics")
    print(f"Workers      : {args.workers}")
    print(f"API          : Chutes - {API_CONFIG['model']}")
    print(f"Timeout      : {TIMEOUT}s (monitoring every {HEARTBEAT_INTERVAL}s)")
    print(f"Mode         : {'DRY RUN' if args.dry_run else 'LIVE'}")
    if args.resume:
        print(f"Resume       : {len(completed)} completed")
    if args.start_from > 1:
        print(f"Start from   : Topic #{args.start_from}")
    if args.end_at > 0:
        print(f"End at       : Topic #{args.end_at}")
    print(f"{'='*80}\n")

    if args.dry_run:
        print("DRY RUN - No files will be written")
        return

    # Process topics in parallel
    stats = {"processed": 0, "success": 0, "partial": 0, "failed": 0}

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(process_topic, topic, i+1, len(topics)): topic
            for i, topic in enumerate(topics)
        }

        for future in as_completed(futures):
            result = future.result()
            stats["processed"] += 1

            if result["success"]:
                stats["success"] += 1
                completed.add(result["topic_path"])
                save_progress(completed)
            elif result["files_written"] >= 3:
                stats["partial"] += 1
            else:
                stats["failed"] += 1

    # Print summary
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print(f"Processed: {stats['processed']}")
    print(f"Success  : {stats['success']} (7-9 files)")
    print(f"Partial  : {stats['partial']} (3-6 files)")
    print(f"Failed   : {stats['failed']} (<3 files)")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    main()
