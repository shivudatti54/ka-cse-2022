#!/usr/bin/env python3
"""
VTU Content Validator & Fixer
Validates SVG/JSON files and fixes broken ones using NVIDIA API (FREE)
"""

import os
import sys
import json
import re
import xml.etree.ElementTree as ET
import urllib.request
import urllib.error
import time
from pathlib import Path
from datetime import datetime

# Unbuffered output
sys.stdout = sys.stderr = open(sys.stdout.fileno(), mode='w', buffering=1)

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)

# ============== CONFIG ==============
NVIDIA_API_KEY_FILE = "/Users/ggoudar/Documents/GitHub/smalltools/vtu_engg_model_answers/vtu_syllabus/2022_Scheme/api_key.txt"
with open(NVIDIA_API_KEY_FILE, 'r') as f:
    NVIDIA_API_KEY = f.read().strip()

NVIDIA_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

# Best free models for structured output
MODELS = [
    "deepseek-ai/deepseek-v3.2",
    "meta/llama-3.3-70b-instruct",
    "google/gemma-3-27b-it"
]

CSE_DIR = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse"
REPORT_FILE = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/validation_report.json"

# ============== STATS ==============
stats = {
    "svg_valid": 0,
    "svg_invalid": 0,
    "svg_fixed": 0,
    "json_valid": 0,
    "json_invalid": 0,
    "json_fixed": 0,
    "errors": []
}

# ============== NVIDIA API ==============
def call_nvidia_api(prompt, max_retries=3):
    """Call NVIDIA API with fallback models"""
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }

    for attempt in range(max_retries * len(MODELS)):
        model = MODELS[attempt % len(MODELS)]
        try:
            data = json.dumps({
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3,
                "max_tokens": 8000
            }).encode('utf-8')

            req = urllib.request.Request(NVIDIA_API_URL, data=data, headers=headers)
            with urllib.request.urlopen(req, timeout=120) as response:
                result = json.loads(response.read().decode('utf-8'))
                return result['choices'][0]['message']['content']
        except urllib.error.HTTPError as e:
            if e.code == 429:
                log(f"  Rate limited, waiting 10s...")
                time.sleep(10)
            else:
                time.sleep(2)
        except Exception as e:
            time.sleep(2)
    return None

# ============== SVG VALIDATION ==============
def validate_svg(filepath):
    """Validate SVG file - returns (is_valid, error_message)"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if it starts with <svg
        if not content.strip().startswith('<svg'):
            return False, "Does not start with <svg>"

        # Check for matching </svg>
        if '</svg>' not in content:
            return False, "Missing closing </svg> tag"

        # Try XML parsing
        try:
            ET.fromstring(content)
        except ET.ParseError as e:
            return False, f"XML parse error: {str(e)[:100]}"

        # Check for required attributes
        if 'width=' not in content or 'height=' not in content:
            return False, "Missing width/height attributes"

        # Check for invalid HTML elements in SVG
        invalid_elements = ['<ul>', '<li>', '<div>', '<span>', '<p>', '<footer>', '<section>']
        for elem in invalid_elements:
            if elem in content.lower():
                return False, f"Contains invalid HTML element: {elem}"

        # Check for broken/truncated content
        if len(content) < 200:
            return False, "SVG too short (likely truncated)"

        return True, None

    except Exception as e:
        return False, f"Read error: {str(e)}"

def fix_svg(filepath, error_msg):
    """Fix broken SVG using NVIDIA API"""
    try:
        # Read the topic's read.md for context
        topic_dir = os.path.dirname(os.path.dirname(filepath))
        read_md_path = os.path.join(topic_dir, "read.md")

        context = ""
        if os.path.exists(read_md_path):
            with open(read_md_path, 'r') as f:
                context = f.read()[:2000]

        topic_id = os.path.basename(topic_dir)
        topic_title = topic_id.replace('-', ' ').title()

        prompt = f"""Fix this broken SVG for the topic: "{topic_title}"

Error: {error_msg}

Context from study material:
{context[:1500]}

Requirements:
1. SVG dimensions: width="420" height="400"
2. Include data-topic-id="{topic_id}" attribute
3. Use gradient background with pastel colors
4. Include 4-6 sections with data-narration attributes
5. Add smooth animations using <animate> elements
6. Use professional colors (indigo, teal, orange)
7. Include clear labels
8. NO HTML elements (no ul, li, div, span, p, footer, section)
9. Must be valid XML
10. Include title at top

Return ONLY the complete SVG code starting with <svg and ending with </svg>. No explanations."""

        response = call_nvidia_api(prompt)

        if response:
            # Extract SVG from response
            match = re.search(r'<svg[^>]*>[\s\S]*?</svg>', response, re.IGNORECASE)
            if match:
                new_svg = match.group()
                # Validate the new SVG
                try:
                    ET.fromstring(new_svg)
                    with open(filepath, 'w') as f:
                        f.write(new_svg)
                    return True
                except:
                    return False
        return False
    except Exception as e:
        log(f"  Fix error: {e}")
        return False

# ============== JSON VALIDATION ==============
def validate_json(filepath):
    """Validate JSON file - returns (is_valid, error_message)"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if not content.strip():
            return False, "Empty file"

        data = json.loads(content)

        # Type-specific validation
        filename = os.path.basename(filepath)

        if filename == "mcqs.json":
            if not isinstance(data, dict) or "mcqs" not in data:
                return False, "Missing 'mcqs' key"
            if len(data.get("mcqs", [])) < 3:
                return False, f"Only {len(data.get('mcqs', []))} MCQs (need 3+)"

        elif filename == "flashcards.json":
            if not isinstance(data, dict) or "flashcards" not in data:
                return False, "Missing 'flashcards' key"
            if len(data.get("flashcards", [])) < 3:
                return False, f"Only {len(data.get('flashcards', []))} flashcards (need 3+)"

        elif filename == "questions.json":
            if not isinstance(data, dict) or "questions" not in data:
                return False, "Missing 'questions' key"

        elif filename == "visual.json":
            if not isinstance(data, dict) or "visuals" not in data:
                return False, "Missing 'visuals' key"

        elif filename == "memory.json":
            if not isinstance(data, dict):
                return False, "Not a valid object"

        return True, None

    except json.JSONDecodeError as e:
        return False, f"JSON parse error: {str(e)[:100]}"
    except Exception as e:
        return False, f"Read error: {str(e)}"

def fix_json(filepath, error_msg):
    """Fix broken JSON using NVIDIA API"""
    try:
        topic_dir = os.path.dirname(filepath)
        read_md_path = os.path.join(topic_dir, "read.md")
        filename = os.path.basename(filepath)

        context = ""
        if os.path.exists(read_md_path):
            with open(read_md_path, 'r') as f:
                context = f.read()[:2000]

        topic_id = os.path.basename(topic_dir)
        topic_title = topic_id.replace('-', ' ').title()

        # Read existing broken content
        existing = ""
        try:
            with open(filepath, 'r') as f:
                existing = f.read()[:500]
        except:
            pass

        if filename == "mcqs.json":
            prompt = f"""Generate valid MCQs JSON for topic: "{topic_title}"

Context:
{context[:1500]}

Error in existing file: {error_msg}

Generate exactly this JSON structure:
{{
  "topicId": "{topic_id}",
  "mcqs": [
    {{
      "id": "mcq-1",
      "question": "Question text here?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correctAnswer": 0,
      "explanation": "Explanation why this is correct"
    }}
  ]
}}

Generate 5 MCQs. Return ONLY valid JSON, no explanations."""

        elif filename == "flashcards.json":
            prompt = f"""Generate valid flashcards JSON for topic: "{topic_title}"

Context:
{context[:1500]}

Generate exactly this JSON structure:
{{
  "topicId": "{topic_id}",
  "flashcards": [
    {{
      "id": "card-1",
      "front": "Question or term",
      "back": "Answer or definition"
    }}
  ]
}}

Generate 5 flashcards. Return ONLY valid JSON, no explanations."""

        elif filename == "questions.json":
            prompt = f"""Generate valid questions JSON for topic: "{topic_title}"

Context:
{context[:1500]}

Generate exactly this JSON structure:
{{
  "topicId": "{topic_id}",
  "questions": [
    {{
      "id": "q-1",
      "question": "Question text?",
      "answer": "Detailed answer",
      "difficulty": "medium"
    }}
  ]
}}

Generate 5 questions. Return ONLY valid JSON, no explanations."""

        elif filename == "visual.json":
            prompt = f"""Generate valid visual.json for topic: "{topic_id}"

Generate exactly this JSON:
{{
  "topicId": "{topic_id}",
  "visuals": [
    {{
      "id": "{topic_id}-svg",
      "title": "{topic_title}",
      "description": "Animated diagram for {topic_title}",
      "type": "animated-svg",
      "file": "assets/{topic_id}.svg",
      "animated": true
    }}
  ]
}}

Return ONLY valid JSON, no explanations."""

        else:
            return False

        response = call_nvidia_api(prompt)

        if response:
            # Extract JSON from response
            try:
                # Try to find JSON in response
                json_match = re.search(r'\{[\s\S]*\}', response)
                if json_match:
                    new_json = json_match.group()
                    # Validate
                    parsed = json.loads(new_json)
                    with open(filepath, 'w') as f:
                        json.dump(parsed, f, indent=2)
                    return True
            except:
                pass
        return False
    except Exception as e:
        log(f"  Fix error: {e}")
        return False

# ============== MAIN ==============
def find_all_files(directory, pattern):
    """Find all files matching pattern"""
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(pattern) or filename == pattern:
                files.append(os.path.join(root, filename))
    return files

def main():
    log("=" * 70)
    log("VTU CONTENT VALIDATOR & FIXER")
    log("=" * 70)
    log(f"Directory: {CSE_DIR}")
    log(f"Using models: {MODELS[0]} (primary)")
    log("")

    # Phase 1: Find all files
    log("Phase 1: Finding files...")
    svg_files = find_all_files(CSE_DIR, ".svg")
    mcq_files = find_all_files(CSE_DIR, "mcqs.json")
    flashcard_files = find_all_files(CSE_DIR, "flashcards.json")
    question_files = find_all_files(CSE_DIR, "questions.json")
    visual_files = find_all_files(CSE_DIR, "visual.json")

    log(f"  SVGs: {len(svg_files)}")
    log(f"  MCQs: {len(mcq_files)}")
    log(f"  Flashcards: {len(flashcard_files)}")
    log(f"  Questions: {len(question_files)}")
    log(f"  Visuals: {len(visual_files)}")
    log("")

    # Phase 2: Validate SVGs
    log("Phase 2: Validating SVGs...")
    invalid_svgs = []
    for i, filepath in enumerate(svg_files):
        if i % 100 == 0:
            log(f"  Progress: {i}/{len(svg_files)}")

        is_valid, error = validate_svg(filepath)
        if is_valid:
            stats["svg_valid"] += 1
        else:
            stats["svg_invalid"] += 1
            invalid_svgs.append({"path": filepath, "error": error})

    log(f"  Valid: {stats['svg_valid']}, Invalid: {stats['svg_invalid']}")
    log("")

    # Phase 3: Validate JSONs
    log("Phase 3: Validating JSONs...")
    invalid_jsons = []
    all_json_files = mcq_files + flashcard_files + question_files + visual_files

    for i, filepath in enumerate(all_json_files):
        if i % 200 == 0:
            log(f"  Progress: {i}/{len(all_json_files)}")

        is_valid, error = validate_json(filepath)
        if is_valid:
            stats["json_valid"] += 1
        else:
            stats["json_invalid"] += 1
            invalid_jsons.append({"path": filepath, "error": error})

    log(f"  Valid: {stats['json_valid']}, Invalid: {stats['json_invalid']}")
    log("")

    # Phase 4: Fix invalid files
    log("Phase 4: Fixing invalid files...")
    log(f"  SVGs to fix: {len(invalid_svgs)}")
    log(f"  JSONs to fix: {len(invalid_jsons)}")
    log("")

    # Fix SVGs
    if invalid_svgs:
        log("Fixing SVGs...")
        for i, item in enumerate(invalid_svgs):
            log(f"  [{i+1}/{len(invalid_svgs)}] {os.path.basename(item['path'])} - {item['error'][:50]}")
            if fix_svg(item["path"], item["error"]):
                stats["svg_fixed"] += 1
                log(f"    ✓ Fixed")
            else:
                stats["errors"].append({"type": "svg", "path": item["path"], "error": item["error"]})
                log(f"    ✗ Failed")

            # Rate limiting
            if i % 10 == 9:
                time.sleep(2)

    # Fix JSONs
    if invalid_jsons:
        log("Fixing JSONs...")
        for i, item in enumerate(invalid_jsons):
            log(f"  [{i+1}/{len(invalid_jsons)}] {os.path.basename(item['path'])} - {item['error'][:50]}")
            if fix_json(item["path"], item["error"]):
                stats["json_fixed"] += 1
                log(f"    ✓ Fixed")
            else:
                stats["errors"].append({"type": "json", "path": item["path"], "error": item["error"]})
                log(f"    ✗ Failed")

            # Rate limiting
            if i % 10 == 9:
                time.sleep(2)

    # Save report
    log("")
    log("Saving report...")
    report = {
        "timestamp": datetime.now().isoformat(),
        "stats": stats,
        "invalid_svgs": invalid_svgs[:50],  # First 50 for review
        "invalid_jsons": invalid_jsons[:50]
    }
    with open(REPORT_FILE, 'w') as f:
        json.dump(report, f, indent=2)

    log("")
    log("=" * 70)
    log("COMPLETE")
    log("=" * 70)
    log(f"SVG:  {stats['svg_valid']} valid, {stats['svg_invalid']} invalid, {stats['svg_fixed']} fixed")
    log(f"JSON: {stats['json_valid']} valid, {stats['json_invalid']} invalid, {stats['json_fixed']} fixed")
    log(f"Report: {REPORT_FILE}")

if __name__ == "__main__":
    main()
