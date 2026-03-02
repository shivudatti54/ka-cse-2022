#!/usr/bin/env python3
"""MiniMax Tool - SVG fixer and content enhancer for studyApp topics.

Usage:
    python minimax.py fix-svg <topic-dir> [svg-filename]
    python minimax.py enhance <topic-dir> <file-type>
    python minimax.py batch-fix <subject-dir>
    python minimax.py batch-enhance <subject-dir> <file-type>
    python minimax.py fix-all <topic-dir>

File types: read, summary, purpose, mcqs, flashcards, memory, questions, visual, svg

Requires: MINIMAX_API_KEY environment variable (or uses default)
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
import glob

# --- Configuration ---
API_URL = "https://api.minimax.io/anthropic/v1/messages"
MODEL = "MiniMax-M2.5"
MAX_TOKENS = 8192
TIMEOUT = 300

DEFAULT_MINIMAX_KEY = "sk-cp-vFEAcD2-Sk2yAyIixvwMkub4FwE-q_-74bJ_4BwB6Vb8EbXuMVotaRmOvwedIY8v_FUuDd02m_q_4562dfj1Wm-9kigtgKGuRYefVCSFFkR2-S_8VlF6hQ4"


def _slug_to_title(slug: str) -> str:
    """Convert a directory slug to a human-readable title."""
    cleaned = re.sub(r'^[a-z]{2,5}\d{3}[a-z]?-', '', slug)
    return cleaned.replace('-', ' ').title()


def get_topic_context(topic_dir: str) -> dict:
    """Extract subject, module, and topic info from a topic directory path."""
    from pathlib import Path
    topic_path = Path(topic_dir)
    topic_slug = topic_path.name
    context = {
        'topic': topic_slug.replace('-', ' ').title(),
        'topic_slug': topic_slug,
        'module': '',
        'subject': '',
        'sibling_topics': [],
    }
    try:
        import json as _json
        module_dir = topic_path.parent.parent
        module_index = module_dir / '_index.json'
        if module_index.exists():
            with open(module_index) as f:
                mod_data = _json.load(f)
            context['module'] = mod_data.get('title', module_dir.name.replace('-', ' ').title())
            for t in mod_data.get('topics', []):
                t_title = t.get('title', t.get('id', ''))
                if t.get('id') == topic_slug:
                    context['topic'] = t_title or context['topic']
                else:
                    context['sibling_topics'].append(t_title)

        subject_dir = module_dir.parent.parent
        subject_index = subject_dir / '_index.json'
        if subject_index.exists():
            with open(subject_index) as f:
                subj_data = _json.load(f)
            context['subject'] = subj_data.get('title', _slug_to_title(subject_dir.name))
        else:
            context['subject'] = _slug_to_title(subject_dir.name)
    except Exception:
        for part in topic_path.parts:
            if re.match(r'^[a-z]{2,5}\d{3}', part):
                context['subject'] = _slug_to_title(part)
                break
    return context


def get_api_key():
    key = os.environ.get("MINIMAX_API_KEY", DEFAULT_MINIMAX_KEY)
    if not key:
        print("ERROR: Set MINIMAX_API_KEY environment variable")
        sys.exit(1)
    return key


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "(File not found)"


def call_api(system_prompt, user_message):
    """Call MiniMax API and return parsed response."""
    api_key = get_api_key()
    payload = {
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "system": system_prompt,
        "messages": [{"role": "user", "content": user_message}],
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )

    sys_tokens = len(system_prompt) // 4
    user_tokens = len(user_message) // 4
    print(f"Payload: ~{sys_tokens + user_tokens} tokens (system ~{sys_tokens}, user ~{user_tokens})")
    print()
    print(f"Sending to MiniMax {MODEL}...")

    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            response = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8") if e.fp else ""
        print(f"ERROR: HTTP {e.code}")
        print(body)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR: {e.reason}")
        sys.exit(1)
    elapsed = int(time.time() - start)

    if "error" in response:
        print(f"ERROR: {response['error']}")
        sys.exit(1)

    # Extract text
    text = ""
    for block in response.get("content", []):
        if block.get("type") == "text":
            text = block["text"]
            break

    content = text.strip()
    # Remove markdown fences
    if content.startswith("```"):
        content = re.sub(r"^```\w*\n?", "", content)
        content = re.sub(r"\n?```$", "", content)
        content = content.strip()

    usage = response.get("usage", {})
    return content, usage, elapsed


def print_token_usage(usage, elapsed):
    inp = usage.get("input_tokens", 0)
    out = usage.get("output_tokens", 0)
    total = inp + out
    print()
    print("=" * 50)
    print("  TOKEN CONSUMPTION")
    print("=" * 50)
    print(f"  Input tokens:  {inp:>8,}")
    print(f"  Output tokens: {out:>8,}")
    print(f"  Total tokens:  {total:>8,}")
    print(f"  API time:      {elapsed:>7}s")
    print("=" * 50)


# ============================================================
#  FIX-SVG
# ============================================================

SVG_SYSTEM_PROMPT = """You are an expert SVG diagram creator for educational content. You fix and polish SVG diagrams used in a university study app (VTU 2022 Scheme, CSE branch).

SVG SPEC REQUIREMENTS:
- viewBox="0 0 800 600", xmlns="http://www.w3.org/2000/svg"
- Background: <rect width="800" height="600" fill="#f8f9fa"/>
- 5-8 steps as <g class="step" id="stepN" data-narration="...">
- data-narration: 20-40 words, no jargon, conversational TTS-friendly
- Color palette: Blue #e3f2fd/#1976d2, Green #e8f5e9/#388e3c, Orange #fff3e0/#ff9800, Red #ffebee/#f44336, Purple #f3e5f5/#9c27b0
- Arrow markers in <defs>
- No fixed width/height attributes on root <svg> (only viewBox)

LAYOUT RULES:
- CRITICAL: Steps are CUMULATIVE, not slides. Each step ADDS to the diagram — all previous steps remain visible. This means NO step can reuse Y-coordinates already used by earlier steps. Each step must occupy its own unique vertical region.
- Plan your layout: divide the 600px height among all steps. With 5 steps, each gets ~100px. With 8 steps, each gets ~65px. Leave 40px for the title at top.
- Use diverse layouts WITHIN each step's region: hub-spoke, pipeline, comparison boxes, grid, etc.
- NO stacked rectangles (lazy vertical list of identical boxes)
- NO text-only steps with no visual elements
- NO overlapping text/elements between steps
- Each step should have meaningful visual progression building on previous steps
- Ensure adequate spacing between steps (minimum 15px gap)

NARRATION RULES:
- Each data-narration must be 20-40 words
- Conversational tone suitable for text-to-speech
- No technical jargon without explanation
- Should explain what the step shows

OUTPUT: Return ONLY the fixed SVG code. No explanation, no markdown, no code fences. Just the raw SVG starting with <svg and ending with </svg>."""


def fix_svg(topic_dir, svg_name=None):
    if not os.path.isdir(topic_dir):
        print(f"ERROR: Topic directory not found: {topic_dir}")
        sys.exit(1)

    topic_name = os.path.basename(topic_dir)
    ctx = get_topic_context(topic_dir)
    assets_dir = os.path.join(topic_dir, "assets")

    if svg_name is None:
        svgs = glob.glob(os.path.join(assets_dir, "*.svg"))
        if not svgs:
            print(f"ERROR: No SVG found in {assets_dir}")
            sys.exit(1)
        svg_path = svgs[0]
        svg_name = os.path.basename(svg_path)
    else:
        svg_path = os.path.join(assets_dir, svg_name)

    if not os.path.isfile(svg_path):
        print(f"ERROR: SVG not found at {svg_path}")
        sys.exit(1)

    print(f"=== MiniMax SVG Fixer ===")
    print(f"Subject: {ctx['subject']}")
    print(f"Topic:   {ctx['topic']}")
    print(f"SVG:     {svg_path}")
    print()

    read_md = read_file(os.path.join(topic_dir, "read.md"))
    purpose_md = read_file(os.path.join(topic_dir, "purpose.md"))
    summary_md = read_file(os.path.join(topic_dir, "summary.md"))
    svg_content = read_file(svg_path)

    siblings = ctx.get('sibling_topics', [])
    siblings_line = f"\nOther topics in this module: {', '.join(siblings)}" if siblings else ""

    user_message = f"""Fix this SVG diagram for the topic: "{ctx['topic']}"
Subject: {ctx['subject']}
Module: {ctx['module']}{siblings_line}

IMPORTANT: This diagram must be specifically about "{ctx['topic']}" in the context of "{ctx['subject']}".

== FULL TOPIC CONTENT (read.md) ==
{read_md}

== LEARNING OBJECTIVE (purpose.md) ==
{purpose_md}

== KEY POINTS (summary.md) ==
{summary_md}

== CURRENT SVG TO FIX ==
{svg_content}

Fix all issues: layout overlaps, narration length (must be 20-40 words each), anti-patterns, and ensure the diagram accurately teaches this topic based on the content above. Output ONLY the fixed SVG."""

    svg, usage, elapsed = call_api(SVG_SYSTEM_PROMPT, user_message)

    if not svg.startswith("<svg"):
        print(f"ERROR: Response doesn't start with <svg>")
        print(f"First 300 chars: {svg[:300]}")
        sys.exit(1)

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"Fixed SVG written to: {svg_path}")
    print_token_usage(usage, elapsed)

    # Validation
    has_viewbox = 'viewBox="0 0 800 600"' in svg
    has_bg = 'fill="#f8f9fa"' in svg
    step_count = len(re.findall(r'class="step"', svg))
    narrations = re.findall(r'data-narration="([^"]*)"', svg)
    word_counts = [len(n.split()) for n in narrations]

    print()
    print("=" * 50)
    print("  SVG VALIDATION")
    print("=" * 50)
    print(f"  viewBox 800x600:  {'PASS' if has_viewbox else 'FAIL'}")
    print(f"  Background rect:  {'PASS' if has_bg else 'FAIL'}")
    print(f"  Steps count:      {step_count} {'PASS' if 5 <= step_count <= 8 else 'WARN (expected 5-8)'}")
    print()
    for i, (n, wc) in enumerate(zip(narrations, word_counts)):
        status = "PASS" if 20 <= wc <= 40 else "FAIL"
        print(f"  step{i} narration: {wc:>2} words [{status}]")
    print("=" * 50)
    print()
    print("Done!")


# ============================================================
#  ENHANCE
# ============================================================

ENHANCE_SYSTEM_PROMPTS = {
    "read": """You are an expert educational content writer for a university study app (VTU 2022 Scheme, CSE branch).

TASK: Enhance the read.md file for this topic. This is the main study material students read.

FORMAT REQUIREMENTS:
- H1 header with topic title
- H2 sections for main concepts
- H3 subsections for detailed breakdowns
- Code blocks with language tags where applicable
- Tables for comparisons
- Numbered and bulleted lists
- 150-400 lines total

CONTENT REQUIREMENTS:
- Start with clear introduction explaining what and why
- Progress from basic to complex concepts
- Include real-world examples and applications
- Add code examples where the topic involves programming
- Include comparison tables between related concepts
- End with exam tips and key takeaways
- Use VTU exam-relevant terminology
- Explain all technical terms when first introduced

QUALITY RULES:
- Every concept must have at least one example
- No vague statements — be specific and concrete
- Align with the learning objectives in purpose.md
- Cover all points mentioned in summary.md
- Ensure factual accuracy for the subject domain

OUTPUT: Return ONLY the enhanced markdown. No explanation, no code fences wrapping the entire output.""",

    "summary": """You are an expert educational content writer for a university study app (VTU 2022 Scheme, CSE branch).

TASK: Enhance the summary.md file. This is a quick-reference card students use for revision.

FORMAT:
```
Topic Name
=====================================

## Overview
[2-3 sentence paragraph summarizing the topic]

## Key Points
- [Concise bullet point]
- [Concept: Brief explanation]

## Important Concepts
- [Term 1]: [1-line definition]
- [Term 2]: [1-line definition]

## Notes
- [Exam tip or study advice]
```

RULES:
- Keep it 20-35 lines total — scannable, not verbose
- Every bullet should be self-contained and memorizable
- Cover the most important concepts from read.md
- Include exam-relevant formulas or definitions
- Notes section should have practical exam tips
- Use colons to separate terms from definitions

OUTPUT: Return ONLY the enhanced markdown. No wrapping.""",

    "purpose": """You are an expert educational content writer for a university study app (VTU 2022 Scheme, CSE branch).

TASK: Enhance the purpose.md file. These are learning objectives using Bloom's taxonomy.

FORMAT:
```markdown
# Learning Objectives

After studying this topic, you should be able to:

1. [Action verb] [specific concept] [measurable outcome]
2. [Action verb] [specific concept] [measurable outcome]
...
```

RULES:
- 5-8 learning objectives
- Each starts with an action verb from Bloom's taxonomy:
  Remember: Define, List, Identify, Recall
  Understand: Explain, Describe, Summarize, Classify
  Apply: Implement, Calculate, Demonstrate, Use
  Analyze: Compare, Differentiate, Distinguish, Examine
  Evaluate: Justify, Assess, Critique, Judge
  Create: Design, Construct, Develop, Formulate
- Progress from lower to higher Bloom's levels
- Each objective must be specific and measurable
- Align with what read.md actually teaches
- Cover breadth of the topic

OUTPUT: Return ONLY the enhanced markdown. No wrapping.""",

    "mcqs": """You are an expert educational assessment designer for a university study app (VTU 2022 Scheme, CSE branch).

TASK: Enhance the mcqs.json file. These are multiple choice questions for self-assessment.

JSON SCHEMA:
{
  "topicId": "topic-slug",
  "mcqs": [
    {
      "id": "mcq1",
      "question": "Clear, specific question text",
      "options": [
        {"key": "A", "text": "Option text"},
        {"key": "B", "text": "Option text"},
        {"key": "C", "text": "Option text"},
        {"key": "D", "text": "Option text"}
      ],
      "correctAnswer": "A",
      "explanation": "Why the correct answer is right and others are wrong"
    }
  ]
}

RULES:
- 6-8 MCQs per topic
- Always exactly 4 options (A, B, C, D)
- Distractors must be plausible but clearly wrong
- Questions should cover: conceptual (2-3), application (2-3), analysis (1-2)
- Explanations must teach — explain WHY, not just restate the answer
- Questions must align with read.md content
- No trick questions or ambiguous wording
- Vary difficulty: 2 easy, 3-4 medium, 1-2 hard
- Keep the existing topicId

OUTPUT: Return ONLY valid JSON. No explanation, no markdown fences.""",

    "flashcards": """You are an expert educational content designer for a university study app (VTU 2022 Scheme, CSE branch).

TASK: Enhance the flashcards.json file. These are quick recall cards for spaced repetition.

JSON SCHEMA:
{
  "topicId": "topic-slug",
  "flashcards": [
    {
      "id": "fc1",
      "front": "Short question or prompt (5-15 words)",
      "back": "Concise answer (1-2 sentences, 15-60 words)"
    }
  ]
}

RULES:
- 6-8 flashcards per topic
- Front: Clear, specific question (not vague like "What about X?")
- Back: Complete but concise answer — one concept per card
- Card types to include:
  - Definitions (2-3): "What is [term]?"
  - Comparisons (1-2): "How does X differ from Y?"
  - Key facts (2-3): "What are the main types of...?"
- Must cover the most important concepts from read.md
- Keep the existing topicId

OUTPUT: Return ONLY valid JSON. No explanation, no markdown fences.""",

    "memory": """You are an expert educational content designer for a university study app (VTU 2022 Scheme, CSE branch).

TASK: Enhance the memory.json file. These are mnemonics and memory aids for exam prep.

JSON SCHEMA:
{
  "topicId": "topic-slug",
  "mnemonics": [
    {
      "id": "m1",
      "title": "Short title (2-5 words)",
      "content": "The mnemonic phrase, acronym, or memory aid"
    }
  ]
}

RULES:
- 2-3 mnemonics per topic
- Types to use:
  - Acronyms: First letters spell a word
  - Sentence mnemonics: First letters of words form the list to remember
  - Rhyming/rhythm aids: Catchy phrases that stick
- Must be genuinely memorable — not forced
- Must cover key lists, sequences, or classifications from the topic
- Keep the existing topicId

OUTPUT: Return ONLY valid JSON. No explanation, no markdown fences.""",

    "questions": """You are an expert educational assessment designer for a university study app (VTU 2022 Scheme, CSE branch).

TASK: Enhance the questions.json file. These are short and long answer questions for exam practice.

JSON SCHEMA:
{
  "topicId": "topic-slug",
  "questions": [
    {
      "id": "q1",
      "question": "Question text (exam-style wording)",
      "type": "short|long",
      "expectedPoints": [
        "Key point 1 that should be in the answer",
        "Key point 2"
      ]
    }
  ]
}

RULES:
- 3-5 questions per topic
- Mix of types: 1-2 short (2-3 expected points), 2-3 long (3-5 expected points)
- Short: "Define...", "List...", "Explain briefly..."
- Long: "Compare and contrast...", "Explain with example...", "Discuss the advantages..."
- Expected points should be specific and gradeable
- Questions should align with VTU exam patterns
- Keep the existing topicId

OUTPUT: Return ONLY valid JSON. No explanation, no markdown fences.""",

    "visual": """You are an expert educational content designer for a university study app (VTU 2022 Scheme, CSE branch).

TASK: Enhance the visual.json file. This defines diagram structures for the topic.

JSON SCHEMA:
{
  "topicId": "topic-slug",
  "visuals": [
    {
      "id": "v1",
      "title": "Visual title",
      "description": "What this visual shows",
      "type": "animated-svg",
      "file": "assets/filename.svg"
    }
  ],
  "diagrams": [
    {
      "id": "d1",
      "title": "Diagram title",
      "type": "flow|hierarchy|matrix|comparison|timeline",
      "content": {
        "nodes": [{"id": "n1", "label": "Node label"}],
        "edges": [{"from": "n1", "to": "n2"}]
      }
    }
  ]
}

RULES:
- 1-2 visuals referencing SVG files in assets/
- 1-2 diagrams with clear node/edge structures
- Diagram types: flow (processes), hierarchy (relationships), matrix (comparisons), timeline (sequences)
- Node labels: 2-5 words each
- Must represent key concepts from read.md
- Keep the existing topicId and any existing file references

OUTPUT: Return ONLY valid JSON. No explanation, no markdown fences.""",
}

FILE_TYPE_MAP = {
    "read": "read.md",
    "summary": "summary.md",
    "purpose": "purpose.md",
    "mcqs": "mcqs.json",
    "flashcards": "flashcards.json",
    "memory": "memory.json",
    "questions": "questions.json",
    "visual": "visual.json",
}


def enhance(topic_dir, file_type):
    if file_type == "svg":
        fix_svg(topic_dir)
        return

    if file_type not in ENHANCE_SYSTEM_PROMPTS:
        print(f"ERROR: Unknown file type '{file_type}'")
        print(f"Valid types: {', '.join(list(FILE_TYPE_MAP.keys()) + ['svg'])}")
        sys.exit(1)

    if not os.path.isdir(topic_dir):
        print(f"ERROR: Topic directory not found: {topic_dir}")
        sys.exit(1)

    topic_name = os.path.basename(topic_dir)
    ctx = get_topic_context(topic_dir)
    target_file = os.path.join(topic_dir, FILE_TYPE_MAP[file_type])

    if not os.path.isfile(target_file):
        print(f"ERROR: File not found: {target_file}")
        sys.exit(1)

    print(f"=== MiniMax Content Enhancer ===")
    print(f"Subject: {ctx['subject']}")
    print(f"Topic:   {ctx['topic']}")
    print(f"File:    {file_type} -> {target_file}")
    print()

    read_md = read_file(os.path.join(topic_dir, "read.md"))
    purpose_md = read_file(os.path.join(topic_dir, "purpose.md"))
    summary_md = read_file(os.path.join(topic_dir, "summary.md"))
    current_content = read_file(target_file)

    siblings = ctx.get('sibling_topics', [])
    siblings_line = f"\nOther topics in this module: {', '.join(siblings)}" if siblings else ""

    user_message = f"""Enhance the {file_type} file for topic: "{ctx['topic']}"
Subject: {ctx['subject']}
Module: {ctx['module']}{siblings_line}

IMPORTANT: All content must be specifically about "{ctx['topic']}" in the context of "{ctx['subject']}". Do not confuse with similarly named topics from other subjects.

== FULL TOPIC CONTENT (read.md) ==
{read_md}

== LEARNING OBJECTIVES (purpose.md) ==
{purpose_md}

== SUMMARY (summary.md) ==
{summary_md}

== CURRENT {file_type.upper()} CONTENT TO ENHANCE ==
{current_content}

Enhance this content based on the topic material above. Ensure accuracy, completeness, and alignment with the read.md content. Output ONLY the enhanced content."""

    content, usage, elapsed = call_api(ENHANCE_SYSTEM_PROMPTS[file_type], user_message)

    # Validate JSON types
    is_json = file_type in ("mcqs", "flashcards", "memory", "questions", "visual")
    if is_json:
        try:
            parsed = json.loads(content)
            content = json.dumps(parsed, indent=2, ensure_ascii=False)
            print("JSON validation: PASS")
        except json.JSONDecodeError as e:
            print(f"JSON validation: FAIL - {e}")
            json_match = re.search(r"\{[\s\S]*\}", content)
            if json_match:
                try:
                    parsed = json.loads(json_match.group())
                    content = json.dumps(parsed, indent=2, ensure_ascii=False)
                    print("JSON extraction: PASS (recovered)")
                except Exception:
                    print(f"JSON extraction: FAIL")
                    print(f"First 500 chars: {content[:500]}")
                    sys.exit(1)
            else:
                print(f"First 500 chars: {content[:500]}")
                sys.exit(1)

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)
        if not is_json and not content.endswith("\n"):
            f.write("\n")

    print(f"Enhanced content written to: {target_file}")
    print_token_usage(usage, elapsed)
    print_content_stats(content, file_type)
    print()
    print("Done!")


def print_content_stats(content, file_type):
    print()
    print("=" * 50)
    print("  CONTENT STATS")
    print("=" * 50)

    if file_type in ("read", "summary", "purpose"):
        lines = content.split("\n")
        print(f"  Lines:    {len(lines)}")
        print(f"  H1:       {sum(1 for l in lines if l.startswith('# '))}")
        print(f"  H2:       {sum(1 for l in lines if l.startswith('## '))}")
        print(f"  H3:       {sum(1 for l in lines if l.startswith('### '))}")
        print(f"  Words:    {len(content.split())}")
    elif file_type == "mcqs":
        parsed = json.loads(content)
        mcqs = parsed.get("mcqs", [])
        print(f"  MCQs:     {len(mcqs)}")
        for m in mcqs:
            opts = len(m.get("options", []))
            has_exp = bool(m.get("explanation"))
            status = "PASS" if opts == 4 and has_exp else "WARN"
            print(f"    {m['id']}: {opts} options, explanation={'yes' if has_exp else 'NO'} [{status}]")
    elif file_type == "flashcards":
        parsed = json.loads(content)
        cards = parsed.get("flashcards", [])
        print(f"  Cards:    {len(cards)}")
        for c in cards:
            print(f"    {c['id']}: front={len(c.get('front','').split())}w, back={len(c.get('back','').split())}w")
    elif file_type == "memory":
        parsed = json.loads(content)
        for m in parsed.get("mnemonics", []):
            print(f"    {m['id']}: {m.get('title', 'untitled')}")
    elif file_type == "questions":
        parsed = json.loads(content)
        for q in parsed.get("questions", []):
            pts = len(q.get("expectedPoints", []))
            print(f"    {q['id']}: {q.get('type','?')} ({pts} points)")
    elif file_type == "visual":
        parsed = json.loads(content)
        print(f"  Visuals:  {len(parsed.get('visuals', []))}")
        print(f"  Diagrams: {len(parsed.get('diagrams', []))}")

    print("=" * 50)


# ============================================================
#  BATCH OPERATIONS
# ============================================================

def find_topics(subject_dir):
    """Find all topic directories under a subject."""
    topics = []
    for root, dirs, files in os.walk(subject_dir):
        if "assets" in dirs and os.path.basename(os.path.dirname(root)) == "topics":
            topics.append(root)
        elif os.path.basename(os.path.dirname(root)) == "topics" and any(
            f.endswith(".md") or f.endswith(".json") for f in files
        ):
            topics.append(root)
    return sorted(topics)


def batch_fix(subject_dir):
    """Fix all SVGs in a subject directory."""
    topics = find_topics(subject_dir)
    if not topics:
        print(f"ERROR: No topics found under {subject_dir}")
        sys.exit(1)

    print(f"=== Batch SVG Fix: {os.path.basename(subject_dir)} ===")
    print(f"Found {len(topics)} topics")
    print()

    for i, topic in enumerate(topics, 1):
        name = os.path.basename(topic)
        svgs = glob.glob(os.path.join(topic, "assets", "*.svg"))
        if not svgs:
            print(f"[{i}/{len(topics)}] {name} — no SVG, skipping")
            continue
        print(f"\n[{i}/{len(topics)}] {name}")
        try:
            fix_svg(topic)
        except SystemExit:
            print(f"  FAILED — continuing...")
        time.sleep(2)

    print("\n=== Batch fix complete! ===")


def batch_enhance(subject_dir, file_type):
    """Enhance a file type across all topics in a subject."""
    topics = find_topics(subject_dir)
    if not topics:
        print(f"ERROR: No topics found under {subject_dir}")
        sys.exit(1)

    print(f"=== Batch Enhance ({file_type}): {os.path.basename(subject_dir)} ===")
    print(f"Found {len(topics)} topics")
    print()

    for i, topic in enumerate(topics, 1):
        name = os.path.basename(topic)
        print(f"\n[{i}/{len(topics)}] {name}")
        try:
            enhance(topic, file_type)
        except SystemExit:
            print(f"  FAILED — continuing...")
        time.sleep(2)

    print("\n=== Batch enhance complete! ===")


def fix_all(topic_dir):
    """Fix ALL files in a topic."""
    name = os.path.basename(topic_dir)
    print(f"=== Fixing all files in: {name} ===")

    for ftype in ["svg", "read", "summary", "purpose", "mcqs", "flashcards", "memory", "questions", "visual"]:
        print(f"\n--- {ftype} ---")
        try:
            enhance(topic_dir, ftype)
        except SystemExit:
            print(f"  SKIPPED ({ftype})")
        time.sleep(2)

    print("\n=== All done! ===")


# ============================================================
#  RESOLVE SVG PATH — handle topic dir, SVG path, or assets dir
# ============================================================

def resolve_svg_input(input_path):
    """Given a path (topic dir, SVG file, or assets dir), return (topic_dir, svg_name)."""
    if input_path.endswith(".svg"):
        svg_name = os.path.basename(input_path)
        topic_dir = os.path.dirname(os.path.dirname(input_path))
        return topic_dir, svg_name
    elif os.path.isdir(os.path.join(input_path, "assets")):
        return input_path, None
    elif os.path.isdir(input_path) and os.path.basename(input_path) == "assets":
        return os.path.dirname(input_path), None
    else:
        return input_path, None


# ============================================================
#  MAIN
# ============================================================

def usage():
    print(__doc__)
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        usage()

    cmd = sys.argv[1]

    if cmd == "fix-svg":
        if len(sys.argv) < 3:
            print("Usage: python minimax.py fix-svg <topic-dir-or-svg-path> [svg-filename]")
            sys.exit(1)
        topic_dir, svg_name = resolve_svg_input(sys.argv[2])
        if len(sys.argv) >= 4:
            svg_name = sys.argv[3]
        fix_svg(topic_dir, svg_name)

    elif cmd == "enhance":
        if len(sys.argv) < 4:
            print("Usage: python minimax.py enhance <topic-dir> <file-type>")
            print(f"Types: {', '.join(list(FILE_TYPE_MAP.keys()) + ['svg'])}")
            sys.exit(1)
        enhance(sys.argv[2], sys.argv[3])

    elif cmd == "batch-fix":
        if len(sys.argv) < 3:
            print("Usage: python minimax.py batch-fix <subject-dir>")
            sys.exit(1)
        batch_fix(sys.argv[2])

    elif cmd == "batch-enhance":
        if len(sys.argv) < 4:
            print("Usage: python minimax.py batch-enhance <subject-dir> <file-type>")
            sys.exit(1)
        batch_enhance(sys.argv[2], sys.argv[3])

    elif cmd == "fix-all":
        if len(sys.argv) < 3:
            print("Usage: python minimax.py fix-all <topic-dir>")
            sys.exit(1)
        fix_all(sys.argv[2])

    else:
        print(f"Unknown command: {cmd}")
        usage()


if __name__ == "__main__":
    main()
