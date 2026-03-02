#!/usr/bin/env python3
"""
SVG Generator with TTS Narration for VTU Sem 5 CSE

Generates educational SVG diagrams with TTS-ready narration sections.
Processes all topics across all subjects in parallel.

Usage:
    python3 generate_tts_svgs.py [--workers 4] [--subject bcs501]
"""

import urllib.request
import urllib.error
import json
import os
import time
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import re

# ============== CONFIGURATION ==============
API_KEY = os.environ.get("NVIDIA_API_KEY", "")
API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODEL = "deepseek-ai/deepseek-v3.1"
FALLBACK_MODEL = "meta/llama-3.3-70b-instruct"

MAX_WORKERS = 4
BASE_PATH = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse/sem-5"
SKIP_EXISTING = False  # Set to False to regenerate all
# ============================================

print_lock = Lock()

def log(msg):
    with print_lock:
        print(msg, flush=True)


def call_api(prompt, max_tokens=6000, model=None, retries=3, backoff=2):
    """Call NVIDIA NIM API with retry logic"""
    if model is None:
        model = MODEL

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.3,
        "stream": False
    }

    last_error = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(API_URL, data=json.dumps(data).encode(), headers=headers, method='POST')
            with urllib.request.urlopen(req, timeout=180) as response:
                result = json.loads(response.read().decode())
                return result.get("choices", [{}])[0].get("message", {}).get("content", "")
        except urllib.error.HTTPError as e:
            last_error = e
            if e.code in [500, 502, 503, 504, 429]:
                wait_time = backoff ** attempt
                log(f"    API error {e.code}, retry {attempt+1}/{retries} in {wait_time}s...")
                time.sleep(wait_time)
                continue
            else:
                break
        except Exception as e:
            last_error = e
            wait_time = backoff ** attempt
            log(f"    Error: {str(e)[:50]}, retry {attempt+1}/{retries}")
            time.sleep(wait_time)
            continue

    # Try fallback model
    if model == MODEL and FALLBACK_MODEL:
        log(f"    Primary failed, trying fallback...")
        return call_api(prompt, max_tokens, FALLBACK_MODEL, retries=2)

    return None


def discover_topics(subject_filter=None):
    """Discover all topics from all subjects"""
    topics = []

    # Get all subject directories
    subjects = [d for d in os.listdir(BASE_PATH)
                if os.path.isdir(os.path.join(BASE_PATH, d)) and d.startswith('bcs')]

    if subject_filter:
        subjects = [s for s in subjects if s == subject_filter]

    for subject_id in sorted(subjects):
        subject_path = os.path.join(BASE_PATH, subject_id)
        chapters_path = os.path.join(subject_path, "chapters")

        if not os.path.exists(chapters_path):
            continue

        # Get all modules
        modules = [d for d in os.listdir(chapters_path)
                   if os.path.isdir(os.path.join(chapters_path, d)) and d.startswith('module-')]

        for module_id in sorted(modules):
            topics_path = os.path.join(chapters_path, module_id, "topics")

            if not os.path.exists(topics_path):
                continue

            # Get all topics
            topic_dirs = [d for d in os.listdir(topics_path)
                         if os.path.isdir(os.path.join(topics_path, d))]

            for topic_id in topic_dirs:
                topic_path = os.path.join(topics_path, topic_id)
                read_md = os.path.join(topic_path, "read.md")

                if os.path.exists(read_md):
                    topics.append({
                        "subject_id": subject_id,
                        "module_id": module_id,
                        "topic_id": topic_id,
                        "topic_path": topic_path,
                        "read_md": read_md
                    })

    return topics


def read_topic_content(read_md_path):
    """Read and extract key content from read.md"""
    try:
        with open(read_md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract title (first # heading)
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Topic"

        # Get first 2000 chars for context
        summary = content[:2000]

        return title, summary
    except Exception as e:
        log(f"Error reading {read_md_path}: {e}")
        return "Topic", ""


def generate_svg(topic, content_summary):
    """Generate educational SVG with TTS narration structure"""

    prompt = f"""You are creating an educational SVG diagram for a VTU CSE student.

TOPIC: {topic['topic_id'].replace('-', ' ').title()}
CONTENT PREVIEW:
{content_summary[:1500]}

REQUIREMENTS:

1. SVG STRUCTURE (MANDATORY):
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 400" width="420" height="400" data-topic-id="{topic['topic_id']}">
  <defs>
    <!-- Gradients MUST come first -->
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#E3F2FD"/>
      <stop offset="100%" style="stop-color:#BBDEFB"/>
    </linearGradient>
  </defs>

  <rect width="420" height="400" fill="url(#bg)"/>

  <g data-narration="Introduction sentence explaining the main concept.">
    <!-- Visual elements for concept 1 -->
  </g>

  <g data-narration="Second key point or component explained clearly.">
    <!-- Visual elements for concept 2 -->
  </g>

  <g data-narration="Third important aspect of the topic.">
    <!-- Visual elements for concept 3 -->
  </g>

  <g data-narration="Fourth element showing relationships or process.">
    <!-- Visual elements for concept 4 -->
  </g>

  <g data-narration="Conclusion tying everything together.">
    <!-- Visual elements for concept 5 -->
  </g>
</svg>
```

2. NARRATION GUIDELINES:
- Write 4-5 clear, educational sentences
- Each sentence explains what's being shown visually
- Use simple, TTS-friendly language (avoid symbols, abbreviations)
- Example: "The system consists of three main components: client, server, and database."
- NOT: "System has 3 parts (C/S/DB) -> connected"

3. VISUAL GUIDELINES:
- Use colors: #1565C0 (dark blue), #2196F3 (blue), #64B5F6 (light blue), #4CAF50 (green)
- Create boxes, arrows, labels to illustrate concepts
- Keep it simple and clear
- Use text labels with font-size="12" or "14"

4. MANDATORY ATTRIBUTES:
- xmlns="http://www.w3.org/2000/svg"
- viewBox="0 0 420 400"
- data-topic-id="{topic['topic_id']}"
- Every <g> MUST have data-narration attribute

5. NO HTML ELEMENTS:
- Use only SVG elements (rect, circle, path, text, line, polygon)
- NO <div>, <span>, <p>, <br>, etc.

Generate the complete SVG now. Output ONLY the SVG code, starting with <svg and ending with </svg>."""

    return call_api(prompt, max_tokens=6000)


def extract_svg(content):
    """Extract SVG from API response"""
    if not content:
        return None

    # Remove markdown code blocks
    content = re.sub(r'```xml\s*', '', content)
    content = re.sub(r'```svg\s*', '', content)
    content = re.sub(r'```\s*', '', content)

    start = content.find('<svg')
    end = content.rfind('</svg>') + 6

    if start >= 0 and end > start:
        return content[start:end]
    return None


def validate_svg(svg):
    """Validate SVG structure and TTS requirements"""
    issues = []

    if not svg:
        return False, ["Empty SVG"], False

    # Check basic structure
    if not svg.strip().startswith('<svg'):
        issues.append("Missing <svg> start tag")
    if not svg.strip().endswith('</svg>'):
        issues.append("Missing </svg> end tag")

    # Check required attributes
    if 'xmlns=' not in svg:
        issues.append("Missing xmlns attribute")
    if 'data-topic-id=' not in svg:
        issues.append("Missing data-topic-id attribute")

    # Check for <defs> section
    if '<defs>' not in svg:
        issues.append("Missing <defs> section")

    # Check for data-narration attributes
    narration_count = svg.count('data-narration=')
    if narration_count < 4:
        issues.append(f"Too few narration sections ({narration_count}, need 4-5)")
    elif narration_count > 6:
        issues.append(f"Too many narration sections ({narration_count}, need 4-5)")

    # Check for HTML elements (not allowed)
    html_elements = ['<div', '<span', '<p>', '<br', '<button', '<input']
    for elem in html_elements:
        if elem in svg.lower():
            issues.append(f"Contains HTML element: {elem}")

    # Check size
    size = len(svg.encode('utf-8'))
    if size < 800:
        issues.append(f"Too small ({size} bytes, likely incomplete)")

    # Try XML parse
    try:
        import xml.etree.ElementTree as ET
        ET.fromstring(svg)
    except Exception as e:
        issues.append(f"Invalid XML: {str(e)[:80]}")

    is_valid = len(issues) == 0
    can_fix = any('Missing' in i or 'Too few' in i for i in issues)

    return is_valid, issues, can_fix


def process_topic(topic, num, total, max_retries=2):
    """Process single topic with validation and retry"""

    # Read topic content
    title, content_summary = read_topic_content(topic['read_md'])
    topic['title'] = title

    # Determine output path
    assets_path = os.path.join(topic['topic_path'], 'assets')
    os.makedirs(assets_path, exist_ok=True)

    svg_filename = f"{topic['topic_id']}.svg"
    svg_filepath = os.path.join(assets_path, svg_filename)

    # Check if should skip
    if SKIP_EXISTING and os.path.exists(svg_filepath):
        with open(svg_filepath, 'r', encoding='utf-8') as f:
            existing_svg = f.read()
        is_valid, issues, _ = validate_svg(existing_svg)
        if is_valid:
            return {"topic": topic['topic_id'], "status": "skipped", "path": svg_filepath}
        else:
            log(f"[{num}/{total}] {topic['title'][:40]} - existing invalid, regenerating...")

    # Try generating
    for attempt in range(max_retries + 1):
        if attempt > 0:
            log(f"[{num}/{total}] {topic['title'][:40]} - retry {attempt}/{max_retries}")

        content = generate_svg(topic, content_summary)
        svg = extract_svg(content)

        if not svg:
            log(f"[{num}/{total}] {topic['title'][:40]} - no SVG extracted")
            continue

        # Validate
        is_valid, issues, can_fix = validate_svg(svg)

        if is_valid:
            with open(svg_filepath, 'w', encoding='utf-8') as f:
                f.write(svg)
            log(f"[{num}/{total}] ✓ {topic['title'][:50]}")
            return {"topic": topic['topic_id'], "status": "success", "path": svg_filepath}
        else:
            log(f"[{num}/{total}] {topic['title'][:40]} - invalid: {issues[0]}")

    # Save with warning
    if svg:
        with open(svg_filepath, 'w', encoding='utf-8') as f:
            f.write(svg)
        log(f"[{num}/{total}] ⚠ {topic['title'][:50]} (needs review)")
        return {"topic": topic['topic_id'], "status": "warning", "issues": issues, "path": svg_filepath}

    log(f"[{num}/{total}] ✗ {topic['title'][:50]} FAILED")
    return {"topic": topic['topic_id'], "status": "failed"}


def main():
    parser = argparse.ArgumentParser(description='Generate TTS-ready SVG assets for VTU Sem 5 CSE')
    parser.add_argument('--workers', type=int, default=MAX_WORKERS, help='Parallel workers')
    parser.add_argument('--subject', type=str, help='Process only this subject (e.g., bcs501)')
    parser.add_argument('--skip-existing', action='store_true', help='Skip topics with valid existing SVGs')
    args = parser.parse_args()

    global SKIP_EXISTING
    if args.skip_existing:
        SKIP_EXISTING = True

    log("=" * 80)
    log(f"VTU Sem 5 CSE - SVG Generator with TTS Narration")
    log(f"Model: {MODEL}")
    log(f"Workers: {args.workers}")
    log(f"Skip existing: {SKIP_EXISTING}")
    if args.subject:
        log(f"Subject filter: {args.subject}")
    log("=" * 80)

    if not API_KEY:
        log("\nERROR: Set NVIDIA_API_KEY environment variable")
        log("Get your key from: https://build.nvidia.com/")
        sys.exit(1)

    # Discover topics
    log("\nDiscovering topics...")
    topics = discover_topics(args.subject)
    log(f"Found {len(topics)} topics across all subjects\n")

    if not topics:
        log("No topics found!")
        sys.exit(1)

    # Process in parallel
    results = []
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {}
        for i, topic in enumerate(topics, 1):
            future = executor.submit(process_topic, topic, i, len(topics))
            futures[future] = topic['topic_id']

        for future in as_completed(futures):
            results.append(future.result())

    # Summary
    elapsed = time.time() - start_time
    success = sum(1 for r in results if r["status"] == "success")
    skipped = sum(1 for r in results if r["status"] == "skipped")
    warning = sum(1 for r in results if r["status"] == "warning")
    failed = sum(1 for r in results if r["status"] == "failed")

    log(f"\n{'=' * 80}")
    log(f"COMPLETE - {elapsed:.1f}s")
    log(f"  ✓ Success:  {success}")
    log(f"  → Skipped:  {skipped}")
    log(f"  ⚠ Warning:  {warning}")
    log(f"  ✗ Failed:   {failed}")
    log(f"  TOTAL:      {len(results)}")

    if warning > 0:
        log(f"\nTopics with warnings (review manually):")
        for r in results:
            if r["status"] == "warning":
                log(f"  - {r['topic']}")

    if failed > 0:
        log(f"\nFailed topics:")
        for r in results:
            if r["status"] == "failed":
                log(f"  - {r['topic']}")

    log("=" * 80)

    # Return exit code
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
