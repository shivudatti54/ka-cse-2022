#!/usr/bin/env python3
"""
Fix specific topics that have wrong content by regenerating via MiniMax API.

These topics were generated with content from the wrong subject:
- introduction (module-2): Has Data Structures → Should be Data Link Layer intro
- random-access (module-2): Has File Organization → Should be MAC Random Access (ALOHA, CSMA)
- pvr (module-3): Has Page Replacement → Should be Path Vector Routing

Usage:
  python3 fix_wrong_topics.py
  python3 fix_wrong_topics.py --dry-run
"""

import json
import re
import ssl
import sys
import time
import urllib.request
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────────────────
API_CONFIG = {
    "base_url": "https://api.minimax.io/v1/chat/completions",
    "api_key": "sk-cp-r--6hiKCzLgU9QbQREFxR4v336s2kP0vDCeb3x7-iNJxAAdDwQeXhInB8zgfwcduBNoBtQBSj33uci2eCKcCu7q4VjmMGWDhKYHXu_lpv1fmWctproM4cAg",
    "model": "MiniMax-M2.5",
}

CONTENT_ROOT = Path(__file__).resolve().parent.parent
TIMEOUT = 360
MAX_TOKENS = 16384
TEMPERATURE = 0.3

# ── Topics to fix ─────────────────────────────────────────────────────────
TOPICS_TO_FIX = [
    {
        "path": "cse/sem-5/bcs502-computer-networks/module-2/topics/introduction",
        "subject": "Computer Networks (BCS502)",
        "module": "Module 2: Data Link Layer",
        "topic": "Introduction to Data Link Layer: Error Detection and Correction",
        "description": """This topic covers the introduction to the Data Link Layer in the OSI model.
Key areas to cover:
- What is the Data Link Layer? Its position in the OSI/TCP-IP model
- Services provided by DLL: framing, error control, flow control, access control
- Types of errors: single-bit errors, burst errors
- Error detection methods overview (parity check, CRC, checksum)
- Error correction overview (Hamming code, forward error correction)
- Difference between error detection and error correction
- DLL design issues and sub-layers (LLC and MAC)
Do NOT confuse with Data Structures. This is purely about computer networking.""",
    },
    {
        "path": "cse/sem-5/bcs502-computer-networks/module-2/topics/random-access",
        "subject": "Computer Networks (BCS502)",
        "module": "Module 2: Data Link Layer - Multiple Access Protocols",
        "topic": "Random Access Protocols (Multiple Access)",
        "description": """This topic covers Random Access (contention-based) MAC protocols in computer networks.
Key areas to cover:
- What are Multiple Access Protocols? Why are they needed?
- ALOHA: Pure ALOHA and Slotted ALOHA, throughput analysis, vulnerable time
- CSMA (Carrier Sense Multiple Access): 1-persistent, non-persistent, p-persistent
- CSMA/CD (Collision Detection): used in Ethernet, minimum frame size, jam signal
- CSMA/CA (Collision Avoidance): used in WiFi/802.11, RTS/CTS, NAV, IFS
- Throughput comparison of different random access protocols
- Real-world applications: Ethernet (802.3), WiFi (802.11)
Do NOT confuse with random access file organization or memory access. This is about how multiple devices share a network medium.""",
    },
    {
        "path": "cse/sem-5/bcs502-computer-networks/module-3/topics/pvr",
        "subject": "Computer Networks (BCS502)",
        "module": "Module 3: Network Layer - Routing",
        "topic": "Path Vector Routing (PVR)",
        "description": """This topic covers Path Vector Routing protocol used in inter-domain routing.
Key areas to cover:
- What is Path Vector Routing? How it differs from Distance Vector and Link State
- BGP (Border Gateway Protocol) as the primary path vector protocol
- Path attributes: AS-PATH, NEXT-HOP, LOCAL-PREF, MED
- Loop prevention using AS-PATH (detecting own AS in path)
- Policy-based routing decisions in BGP
- eBGP vs iBGP
- BGP message types: OPEN, UPDATE, KEEPALIVE, NOTIFICATION
- Route selection process in BGP
- Autonomous Systems (AS) and inter-domain routing
- Advantages and limitations of path vector routing
Do NOT confuse with page replacement algorithms (PVR is not Page Virtual Replacement). This is about network routing.""",
    },
]

# ── Prompts ────────────────────────────────────────────────────────────────
MARKDOWN_SYSTEM = """You are an expert university lecturer creating study material for VTU (Visvesvaraya Technological University) 2022 scheme, Computer Science and Engineering program.

STUDENT PROFILE:
- University: VTU, Karnataka, India
- Program: B.E. in Computer Science and Engineering
- Exam pattern: CIE (50%) + SEE (50%), each module typically carries 20 marks
- Content should be thorough, exam-oriented, with practical examples

Your task: Generate THREE markdown files for this specific topic.

CRITICAL: Pay close attention to the topic description. Generate content ONLY about the specified networking topic. Do NOT generate content about data structures, file systems, operating systems, or any other unrelated subject.

Return EXACTLY this delimited format (no extra text before/after):

===READ_MD===
# <Topic Title>

## Introduction
[2-3 paragraphs explaining the topic and its importance in computer networking]

## Key Concepts
[Detailed explanations of all major concepts with diagrams described in text]

## How It Works
[Step-by-step explanation of the protocol/mechanism]

## Examples
[2-3 worked examples with step-by-step solutions]

## Real-World Applications
[Practical applications and where this is used]

## Exam Tips
[5-7 exam-relevant points for VTU semester exams]

Length: 1500-3000 words, B.E. level
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

ASSESSMENT_SYSTEM_PART1 = """You are an expert exam paper setter for VTU 2022 scheme, Computer Science and Engineering.

CRITICAL: Generate content ONLY about the specified networking topic.

Generate flashcards and MCQs as a JSON object. Return ONLY valid JSON:

{
  "flashcards": [
    {"id": "fc-1", "front": "Question?", "back": "Answer in 1-3 sentences."}
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
  ]
}

Requirements:
- 10-12 flashcards
- 12-15 MCQs (balanced easy/medium/hard)
- MCQ options MUST be objects with "key" and "text"
- Keep explanations concise (1-2 sentences)

IMPORTANT: Return ONLY valid JSON. No markdown fences.

CRITICAL OUTPUT RULES (MUST follow):
- Output ONLY in English. Never use Chinese, Japanese, Korean, or any non-Latin characters.
- Do NOT start with conversational preambles like "Of course", "Sure", "Certainly", "Here is a comprehensive", etc. Start directly with the content.
- Do NOT include metadata headers like "Subject:", "Module:", "Topic:" in the content body.
- Do NOT mention the target audience scope (no "B.Tech", "MSc", "MCA", "engineering students", "undergraduate students"). Write as if the reader is simply a student studying this topic.
- For memory aids/mnemonics: Do NOT use markdown bold (**text**). Use UPPERCASE for emphasis instead.
"""

ASSESSMENT_SYSTEM_PART2 = """You are an expert exam paper setter for VTU 2022 scheme, Computer Science and Engineering.

CRITICAL: Generate content ONLY about the specified networking topic.

Generate memory aids, exam questions, visual descriptions, and code examples as a JSON object. Return ONLY valid JSON:

{
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
      "explanation": "Explanation",
      "timeComplexity": "O(n)",
      "spaceComplexity": "O(1)"
    }
  ]
}

Requirements:
- 4-6 short questions (5 marks) + 2-3 long questions (10 marks)
- 2-3 code examples
- Rich memory aids (2-3 of each type)
- 2-3 visual diagram descriptions
- questions use "keyPoints" (NOT "expectedPoints")
- code uses "timeComplexity"/"spaceComplexity" (NOT nested object)

IMPORTANT: Return ONLY valid JSON. No markdown fences.

CRITICAL OUTPUT RULES (MUST follow):
- Output ONLY in English. Never use Chinese, Japanese, Korean, or any non-Latin characters.
- Do NOT start with conversational preambles like "Of course", "Sure", "Certainly", "Here is a comprehensive", etc. Start directly with the content.
- Do NOT include metadata headers like "Subject:", "Module:", "Topic:" in the content body.
- Do NOT mention the target audience scope (no "B.Tech", "MSc", "MCA", "engineering students", "undergraduate students"). Write as if the reader is simply a student studying this topic.
- For memory aids/mnemonics: Do NOT use markdown bold (**text**). Use UPPERCASE for emphasis instead.
"""


# ── API Call ───────────────────────────────────────────────────────────────
def call_api(messages: list, label: str) -> str:
    """Call MiniMax API and return extracted text."""
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
    print(f"  [{label}] Calling MiniMax API...")

    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)
        result = json.loads(resp.read().decode())
        elapsed = time.time() - start
        print(f"  [{label}] API responded in {elapsed:.1f}s")

        # Extract text
        message = result.get("choices", [{}])[0].get("message", {})
        text = message.get("content", "") or message.get("reasoning_content", "")

        # Strip <think> tags
        if '<think>' in text and '</think>' in text:
            think_end = text.find('</think>')
            if think_end != -1:
                text = text[think_end + 8:].strip()

        return text.strip()
    except Exception as e:
        elapsed = time.time() - start
        print(f"  [{label}] FAILED after {elapsed:.1f}s: {e}")
        raise


def clean_json(content: str) -> str:
    """Clean JSON response from API."""
    cleaned = content.strip()
    if cleaned.startswith("```"):
        first_nl = cleaned.find("\n")
        if first_nl != -1:
            cleaned = cleaned[first_nl + 1:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        cleaned = cleaned.strip()
    first = cleaned.find("{")
    last = cleaned.rfind("}")
    if first != -1 and last != -1 and first < last:
        cleaned = cleaned[first:last + 1]
    return cleaned


# ── Content Generation ─────────────────────────────────────────────────────
def generate_markdown(topic_info: dict) -> dict:
    """Generate read.md, purpose.md, summary.md."""
    user_prompt = f"""Generate content for this VTU Computer Networks topic:

Subject: {topic_info['subject']}
Module: {topic_info['module']}
Topic: {topic_info['topic']}

IMPORTANT CONTEXT - Read carefully:
{topic_info['description']}

Follow the exact format specified in the system message."""

    text = call_api([
        {"role": "system", "content": MARKDOWN_SYSTEM},
        {"role": "user", "content": user_prompt}
    ], f"MD:{topic_info['topic'][:30]}")

    files = {}
    read_match = re.search(r'===READ_MD===\s*(.+?)\s*===PURPOSE_MD===', text, re.DOTALL)
    if read_match:
        files['read.md'] = read_match.group(1).strip()
        print(f"    read.md: {len(files['read.md'])} chars")

    purpose_match = re.search(r'===PURPOSE_MD===\s*(.+?)\s*===SUMMARY_MD===', text, re.DOTALL)
    if purpose_match:
        files['purpose.md'] = purpose_match.group(1).strip()
        print(f"    purpose.md: {len(files['purpose.md'])} chars")

    summary_match = re.search(r'===SUMMARY_MD===\s*(.+?)\s*===END===', text, re.DOTALL)
    if summary_match:
        files['summary.md'] = summary_match.group(1).strip()
        print(f"    summary.md: {len(files['summary.md'])} chars")

    return files


def generate_assessment(topic_info: dict, read_content: str) -> dict:
    """Generate all JSON assessment files using 2 split API calls."""
    topic_id = Path(topic_info['path']).name
    files = {}

    user_base = f"""Subject: {topic_info['subject']}
Module: {topic_info['module']}
Topic: {topic_info['topic']}

IMPORTANT CONTEXT:
{topic_info['description']}

Topic content summary:
{read_content[:500]}...

Return ONLY valid JSON as specified."""

    # --- Call 1: Flashcards + MCQs ---
    for attempt in range(3):
        try:
            text1 = call_api([
                {"role": "system", "content": ASSESSMENT_SYSTEM_PART1},
                {"role": "user", "content": f"Generate flashcards and MCQs for:\n\n{user_base}"}
            ], f"FC+MCQ:{topic_info['topic'][:25]}")
            text1 = clean_json(text1)
            data1 = json.loads(text1)

            flashcards = data1.get('flashcards', [])
            for i, fc in enumerate(flashcards):
                if 'id' not in fc:
                    fc['id'] = f'fc-{i+1}'
            files['flashcards.json'] = json.dumps({"topicId": topic_id, "flashcards": flashcards}, indent=2)

            mcqs = data1.get('mcqs', [])
            for i, m in enumerate(mcqs):
                if 'id' not in m:
                    m['id'] = f'mcq-{i+1}'
                if m.get('options') and isinstance(m['options'][0], str):
                    keys = ["A", "B", "C", "D"]
                    m['options'] = [{"key": keys[j], "text": t} for j, t in enumerate(m['options'])]
                if 'difficulty' not in m:
                    m['difficulty'] = 'medium'
            files['mcqs.json'] = json.dumps({"topicId": topic_id, "mcqs": mcqs}, indent=2)
            print(f"    Part1: {len(flashcards)} flashcards, {len(mcqs)} MCQs")
            break
        except (json.JSONDecodeError, Exception) as e:
            print(f"    Part1 attempt {attempt+1} failed: {e}")
            if attempt < 2:
                time.sleep(3)

    # --- Call 2: Memory + Questions + Visual + Code ---
    for attempt in range(3):
        try:
            text2 = call_api([
                {"role": "system", "content": ASSESSMENT_SYSTEM_PART2},
                {"role": "user", "content": f"Generate memory aids, questions, visuals, code for:\n\n{user_base}"}
            ], f"MEM+Q:{topic_info['topic'][:25]}")
            text2 = clean_json(text2)
            data2 = json.loads(text2)

            memory = data2.get('memory', {})
            if 'topicId' not in memory:
                memory['topicId'] = topic_id
            files['memory.json'] = json.dumps(memory, indent=2)

            questions = data2.get('questions', [])
            for i, q in enumerate(questions):
                if 'id' not in q:
                    q['id'] = f'q-{i+1}'
                if 'type' not in q:
                    q['type'] = 'long' if q.get('marks', 0) >= 10 else 'short'
                if 'expectedPoints' in q and 'keyPoints' not in q:
                    q['keyPoints'] = q.pop('expectedPoints')
            files['questions.json'] = json.dumps({"topicId": topic_id, "questions": questions}, indent=2)

            visual = data2.get('visual', {})
            if 'topicId' not in visual:
                visual['topicId'] = topic_id
            files['visual.json'] = json.dumps(visual, indent=2)

            code_examples = data2.get('code', [])
            for i, ex in enumerate(code_examples):
                if 'id' not in ex:
                    ex['id'] = f'code-{i+1}'
                if 'language' not in ex:
                    ex['language'] = 'pseudocode'
                if 'code' not in ex:
                    ex['code'] = ex.get('pseudocode', '// No code')
                if 'complexity' in ex and isinstance(ex['complexity'], dict):
                    if 'timeComplexity' not in ex and 'time' in ex['complexity']:
                        ex['timeComplexity'] = ex['complexity']['time']
                    if 'spaceComplexity' not in ex and 'space' in ex['complexity']:
                        ex['spaceComplexity'] = ex['complexity']['space']
                    del ex['complexity']
            files['code.json'] = json.dumps({"topicId": topic_id, "examples": code_examples}, indent=2)
            print(f"    Part2: {len(questions)} questions, {len(code_examples)} code, memory+visual OK")
            break
        except (json.JSONDecodeError, Exception) as e:
            print(f"    Part2 attempt {attempt+1} failed: {e}")
            if attempt < 2:
                time.sleep(3)

    print(f"    Generated {len(files)} JSON files total")
    return files


# ── Main ───────────────────────────────────────────────────────────────────
def main():
    dry_run = "--dry-run" in sys.argv
    json_only = "--json-only" in sys.argv

    print(f"\n{'='*70}")
    print("FIX WRONG TOPICS - MiniMax Content Regeneration")
    print(f"{'='*70}")
    print(f"Topics to fix: {len(TOPICS_TO_FIX)}")
    print(f"Mode: {'DRY RUN' if dry_run else 'JSON ONLY' if json_only else 'FULL'}")
    print(f"{'='*70}\n")

    for i, topic_info in enumerate(TOPICS_TO_FIX, 1):
        topic_dir = CONTENT_ROOT / topic_info['path']
        print(f"\n[{i}/{len(TOPICS_TO_FIX)}] {topic_info['topic']}")
        print(f"  Path: {topic_dir}")

        if not topic_dir.exists():
            print(f"  ERROR: Directory not found!")
            continue

        md_files = {}

        if not json_only:
            # Step 1: Generate markdown files
            md_files = generate_markdown(topic_info)
            if len(md_files) < 3:
                print(f"  WARNING: Only got {len(md_files)}/3 markdown files, retrying...")
                time.sleep(2)
                md_files = generate_markdown(topic_info)

            if not dry_run:
                for fname, content in md_files.items():
                    fpath = topic_dir / fname
                    fpath.write_text(content, encoding='utf-8')
                    print(f"  Wrote {fname}")
        else:
            print(f"  Skipping markdown (--json-only)")

        # Step 2: Generate assessment files
        # Use existing read.md if we didn't regenerate it
        read_content = md_files.get('read.md', '')
        if not read_content:
            read_path = topic_dir / 'read.md'
            if read_path.exists():
                read_content = read_path.read_text(encoding='utf-8')

        if read_content:
            json_files = generate_assessment(topic_info, read_content)

            if not dry_run:
                for fname, content in json_files.items():
                    fpath = topic_dir / fname
                    fpath.write_text(content, encoding='utf-8')
                    print(f"  Wrote {fname}")

            total = len(md_files) + len(json_files)
            print(f"  {'DONE' if total >= 7 or (json_only and len(json_files) >= 6) else 'PARTIAL'}: {len(json_files)}/6 JSON files")
        else:
            print(f"  ERROR: No read.md content available, skipping assessment")

    print(f"\n{'='*70}")
    print("COMPLETE")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    main()
