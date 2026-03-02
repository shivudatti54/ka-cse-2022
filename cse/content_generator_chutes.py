#!/usr/bin/env python3
"""
VTU Content Generator - Chutes API (DeepSeek-R1)

Generates high-quality educational content for VTU topics using Chutes (DeepSeek-R1-TEE).
- 2 API calls per topic (smart batching)
- Sequential processing (one topic at a time)
- Simple blocking I/O with 300s timeout
- Progress tracking and resume support

Usage:
  python3 content_generator_chutes.py topic-paths.txt --start-from 101
  python3 content_generator_chutes.py topic-paths.txt --resume
"""

import argparse
import json
import re
import ssl
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────────────────
API_CONFIG = {
    "base_url": "https://llm.chutes.ai/v1/chat/completions",
    "api_key": "cpk_a744b82c5b9c4e8b9c7c8e1442e8d160.c3a84cdb26e850c9b8f358af872bca49.ymNhlwAf2nbhnTZJE620p8sv1aTgEGwx",
    "model": "deepseek-ai/DeepSeek-R1-TEE",
}

TIMEOUT = 300  # 5 minutes
MAX_TOKENS = 8192
TEMPERATURE = 0.3
PROGRESS_FILE = "chutes_progress.json"

# ── Prompts ────────────────────────────────────────────────────────────────
MARKDOWN_SYSTEM = """You are an expert university lecturer creating study material for VTU (Visvesvaraya Technological University) 2022 Scheme, Computer Science & Engineering branch.

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
[5-7 exam-relevant points for VTU exams]

Length: 1500-3000 words, B.E./B.Tech level
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

IMPORTANT: Return ONLY the delimited content. No JSON wrapping."""

ASSESSMENT_SYSTEM = """You are an expert exam paper setter for VTU 2022 Scheme, CSE branch.

Your task: Generate assessment materials as a SINGLE JSON object.

Return ONLY valid JSON (no markdown fences, no explanation):

{
  "flashcards": [
    {"id": "fc-1", "front": "Question", "back": "Answer (1-3 sentences)"}
  ],
  "mcqs": [
    {
      "id": "mcq-1",
      "question": "Question text",
      "options": ["A", "B", "C", "D"],
      "correctAnswer": "A",
      "explanation": "Why A is correct",
      "difficulty": "easy"
    }
  ],
  "memory": {
    "topicId": "TOPIC_ID",
    "mnemonics": [{"id": "m-1", "title": "Title", "content": "Mnemonic"}],
    "acronyms": [{"term": "TERM", "expansion": "Full form", "usage": "Usage"}],
    "visualTips": [{"concept": "Concept", "visualization": "How to visualize"}],
    "analogies": [{"concept": "Concept", "analogy": "Real-world analogy"}]
  },
  "questions": [
    {
      "id": "q-1",
      "type": "short",
      "question": "Question",
      "expectedPoints": ["Point 1", "Point 2"],
      "marks": 5,
      "difficulty": "medium"
    }
  ],
  "visual": {
    "topicId": "TOPIC_ID",
    "diagrams": [{"id": "d-1", "title": "Title", "description": "What it shows", "elements": ["E1"], "purpose": "Learning"}]
  },
  "code": [
    {
      "id": "code-1",
      "language": "pseudocode",
      "title": "Algorithm",
      "description": "What this demonstrates",
      "code": "ALGORITHM\\nBEGIN\\nEND",
      "explanation": "Explanation",
      "complexity": {"time": "O(n)", "space": "O(1)"}
    }
  ]
}

Requirements:
- 12-15 flashcards
- 15-20 MCQs (balanced difficulty)
- 5-7 short questions (5 marks)
- 3-4 long questions (10 marks)
- Rich memory aids

IMPORTANT: Return ONLY valid JSON."""

# ── API Functions ──────────────────────────────────────────────────────────
def call_api(messages: list) -> dict:
    """Call Chutes API with timeout."""
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

    start = time.time()
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)
        result = json.loads(resp.read().decode())
        elapsed = time.time() - start
        print(f"  API call completed in {elapsed:.1f}s")
        return result
    except Exception as e:
        elapsed = time.time() - start
        print(f"  ❌ API call failed after {elapsed:.1f}s: {str(e)[:100]}")
        raise

def extract_text(response: dict) -> str:
    """Extract text from Chutes API response (handles reasoning_content field)."""
    message = response.get("choices", [{}])[0].get("message", {})

    # Chutes (DeepSeek-R1) returns content in reasoning_content field
    content = message.get("reasoning_content", "")
    if not content:
        content = message.get("content", "")

    return content.strip()

# ── Content Generation ─────────────────────────────────────────────────────
def generate_markdown_batch(topic_context: dict) -> dict:
    """Call 1: Generate read.md + purpose.md + summary.md in ONE call."""
    print(f"\n  📝 Generating markdown files...")

    user_prompt = f"""Generate content for this VTU CSE topic:

Subject: {topic_context['subject']}
Module: {topic_context['module']}
Topic: {topic_context['topic']}

Follow the exact format specified in the system message."""

    messages = [
        {"role": "system", "content": MARKDOWN_SYSTEM},
        {"role": "user", "content": user_prompt}
    ]

    response = call_api(messages)
    content = extract_text(response)

    # Parse delimited format
    files = {}

    # Extract read.md
    read_match = re.search(r'===READ_MD===\s*(.+?)\s*===PURPOSE_MD===', content, re.DOTALL)
    if read_match:
        files['read.md'] = read_match.group(1).strip()

    # Extract purpose.md
    purpose_match = re.search(r'===PURPOSE_MD===\s*(.+?)\s*===SUMMARY_MD===', content, re.DOTALL)
    if purpose_match:
        files['purpose.md'] = purpose_match.group(1).strip()

    # Extract summary.md
    summary_match = re.search(r'===SUMMARY_MD===\s*(.+?)\s*===END===', content, re.DOTALL)
    if summary_match:
        files['summary.md'] = summary_match.group(1).strip()

    return files

def generate_assessment_batch(topic_context: dict, read_content: str) -> dict:
    """Call 2: Generate all JSON files in ONE call."""
    print(f"\n  📊 Generating assessment files...")

    user_prompt = f"""Generate assessment materials for this VTU CSE topic:

Subject: {topic_context['subject']}
Module: {topic_context['module']}
Topic: {topic_context['topic']}

Topic content summary:
{read_content[:500]}...

Return ONLY valid JSON as specified."""

    messages = [
        {"role": "system", "content": ASSESSMENT_SYSTEM},
        {"role": "user", "content": user_prompt}
    ]

    response = call_api(messages)
    content = extract_text(response)

    # Extract JSON from response
    content = content.strip()
    if content.startswith("```"):
        content = content[content.index("\n")+1:]
        if content.endswith("```"):
            content = content[:-3]
        content = content.strip()

    try:
        data = json.loads(content)

        # Create individual files
        files = {}
        files['flashcards.json'] = json.dumps(data.get('flashcards', []), indent=2)
        files['mcqs.json'] = json.dumps(data.get('mcqs', []), indent=2)
        files['memory.json'] = json.dumps(data.get('memory', {}), indent=2)
        files['questions.json'] = json.dumps(data.get('questions', []), indent=2)
        files['visual.json'] = json.dumps(data.get('visual', {}), indent=2)
        files['code.json'] = json.dumps(data.get('code', []), indent=2)

        return files
    except json.JSONDecodeError as e:
        print(f"  ❌ JSON parse error: {e}")
        print(f"  Response preview: {content[:200]}")
        return {}

# ── Topic Processing ───────────────────────────────────────────────────────
def get_topic_context(topic_path: str) -> dict:
    """Extract metadata from topic directory path."""
    parts = Path(topic_path).parts

    # Find indices
    topics_idx = None
    for i, part in enumerate(parts):
        if part == "topics":
            topics_idx = i
            break

    if topics_idx and topics_idx >= 2:
        return {
            "subject": parts[topics_idx - 2],
            "subject_dir": parts[topics_idx - 2],
            "module": parts[topics_idx - 1],
            "topic": parts[-1],
            "topic_dir": topic_path,
        }

    return {
        "subject": "Unknown",
        "subject_dir": "",
        "module": "Unknown",
        "topic": parts[-1] if parts else "Unknown",
        "topic_dir": topic_path,
    }

def process_topic(topic_path: str, topic_num: int, total: int) -> bool:
    """Process one topic: generate all content files."""
    ctx = get_topic_context(topic_path)
    topic_dir = Path(topic_path)

    print(f"\n{'='*80}")
    print(f"[{topic_num}/{total}] {ctx['subject']} > {ctx['module']} > {ctx['topic']}")
    print(f"{'='*80}")

    files_written = 0

    try:
        # Call 1: Markdown files
        markdown_files = generate_markdown_batch(ctx)
        for filename, content in markdown_files.items():
            file_path = topic_dir / filename
            file_path.write_text(content, encoding='utf-8')
            files_written += 1
            print(f"  ✅ {filename}")

        # Call 2: Assessment files (use read.md content)
        read_content = markdown_files.get('read.md', '')
        if read_content:
            assessment_files = generate_assessment_batch(ctx, read_content)
            for filename, content in assessment_files.items():
                file_path = topic_dir / filename
                file_path.write_text(content, encoding='utf-8')
                files_written += 1
                print(f"  ✅ {filename}")

        print(f"\n  ✅ Topic completed: {files_written}/9 files")
        return files_written >= 7  # Success if at least 7/9 files

    except Exception as e:
        print(f"\n  ❌ Topic failed: {str(e)[:100]}")
        return False

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
    Path(PROGRESS_FILE).write_text(json.dumps({
        "completed": list(completed),
        "last_updated": datetime.now().isoformat()
    }, indent=2))

# ── Main ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="VTU Content Generator - Chutes (DeepSeek-R1)")
    parser.add_argument("paths_file", help="Text file with topic paths (one per line)")
    parser.add_argument("--start-from", type=int, default=1, dest="start_from", help="Start from topic N (1-based)")
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

    # Print header
    print(f"\n{'='*80}")
    print("VTU CONTENT GENERATOR - CHUTES (DeepSeek-R1)")
    print(f"{'='*80}")
    print(f"Source file  : {paths_file.name}")
    print(f"Total topics : {len(all_topics)}")
    print(f"Processing   : {len(topics)} topics")
    print(f"API          : Chutes - {API_CONFIG['model']}")
    print(f"Mode         : {'DRY RUN' if args.dry_run else 'LIVE'}")
    if args.resume:
        print(f"Resume       : {len(completed)} completed")
    if args.start_from > 1:
        print(f"Start from   : Topic #{args.start_from}")
    print(f"{'='*80}\n")

    # Process topics
    stats = {"processed": 0, "success": 0, "failed": 0}

    for i, topic_path in enumerate(topics, 1):
        stats["processed"] += 1

        if args.dry_run:
            print(f"[{i}/{len(topics)}] SKIP (dry-run): {topic_path}")
            continue

        success = process_topic(topic_path, i, len(topics))

        if success:
            stats["success"] += 1
            completed.add(topic_path)
            save_progress(completed)
        else:
            stats["failed"] += 1

    # Print summary
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print(f"Processed: {stats['processed']}")
    print(f"Success  : {stats['success']}")
    print(f"Failed   : {stats['failed']}")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    main()
