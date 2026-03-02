#!/usr/bin/env python3
"""
CSE Content Validator & Fixer - Parallel 100B+ Models
Uses NVIDIA API with 7 large models in parallel, subject by subject
"""

import os
import sys
import json
import re
import xml.etree.ElementTree as ET
import urllib.request
import urllib.error
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

# Unbuffered output
sys.stdout = sys.stderr = open(sys.stdout.fileno(), mode='w', buffering=1)

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)

# ============== CONFIG ==============
NVIDIA_API_KEY = "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"
NVIDIA_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

# 100B+ models only - no fallback to smaller models
MODELS_100B = [
    "mistralai/mistral-large-3-675b-instruct-2512",  # 675B
    "deepseek-ai/deepseek-v3.2",                      # ~670B MoE
    "deepseek-ai/deepseek-v3.1",                      # ~670B MoE
    "meta/llama-3.1-405b-instruct",                   # 405B
    "igenius/colosseum_355b_instruct_16k",            # 355B
    "nvidia/llama-3.1-nemotron-ultra-253b-v1",        # 253B
    "mistralai/devstral-2-123b-instruct-2512",        # 123B
]

CSE_DIR = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse"
REPORT_DIR = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/reports"

# Thread-safe stats
stats_lock = threading.Lock()
stats = {
    "subjects_processed": 0,
    "topics_total": 0,
    "topics_valid": 0,
    "topics_fixed": 0,
    "topics_failed": 0,
    "files_fixed": 0,
    "api_calls": 0,
    "errors": []
}

# ============== API CALL ==============
def call_nvidia_api(prompt, model_index=0, max_retries=3):
    """Call NVIDIA API with 100B+ model fallback"""
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }

    for attempt in range(max_retries):
        # Rotate through 100B+ models
        model = MODELS_100B[(model_index + attempt) % len(MODELS_100B)]
        try:
            data = json.dumps({
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.2,
                "max_tokens": 16000
            }).encode('utf-8')

            req = urllib.request.Request(NVIDIA_API_URL, data=data, headers=headers)
            with urllib.request.urlopen(req, timeout=180) as response:
                result = json.loads(response.read().decode('utf-8'))
                with stats_lock:
                    stats["api_calls"] += 1
                return result['choices'][0]['message']['content'], model

        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(5)
            else:
                time.sleep(2)
        except Exception as e:
            time.sleep(2)

    return None, None

# ============== VALIDATION ==============
def validate_svg(content):
    """Validate SVG content"""
    errors = []
    if not content:
        return ["Empty SVG"]

    if not content.strip().startswith('<svg'):
        errors.append("Missing <svg> tag")
    if '</svg>' not in content:
        errors.append("Missing </svg>")

    try:
        ET.fromstring(content)
    except ET.ParseError as e:
        errors.append(f"XML error: {str(e)[:50]}")

    invalid_html = ['<ul>', '<li>', '<div>', '<footer>', '<section>', '<span>']
    for elem in invalid_html:
        if elem in content.lower():
            errors.append(f"Invalid HTML: {elem}")
            break

    if 'data-narration' not in content:
        errors.append("Missing data-narration")

    return errors

def validate_json_file(content, file_type):
    """Validate JSON content"""
    errors = []
    if not content:
        return ["Empty file"]

    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        return [f"JSON error: {str(e)[:50]}"]

    if file_type == "mcqs.json":
        if "mcqs" not in data:
            errors.append("Missing 'mcqs' key")
        elif len(data.get("mcqs", [])) < 3:
            errors.append(f"Only {len(data.get('mcqs', []))} MCQs")

    elif file_type == "flashcards.json":
        if "flashcards" not in data:
            errors.append("Missing 'flashcards' key")
        elif len(data.get("flashcards", [])) < 3:
            errors.append(f"Only {len(data.get('flashcards', []))} cards")

    elif file_type == "questions.json":
        if "questions" not in data:
            errors.append("Missing 'questions' key")

    elif file_type == "visual.json":
        if "visuals" not in data:
            errors.append("Missing 'visuals' key")

    return errors

# ============== TOPIC PROCESSING ==============
def read_topic_files(topic_path):
    """Read all files from a topic directory"""
    files = {}
    topic_id = os.path.basename(topic_path)

    # Read markdown files
    for md_file in ["read.md", "purpose.md"]:
        path = os.path.join(topic_path, md_file)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                files[md_file] = f.read()

    # Read JSON files
    for json_file in ["mcqs.json", "flashcards.json", "questions.json", "visual.json", "memory.json"]:
        path = os.path.join(topic_path, json_file)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                files[json_file] = f.read()

    # Read SVG
    svg_path = os.path.join(topic_path, "assets", f"{topic_id}.svg")
    if os.path.exists(svg_path):
        with open(svg_path, 'r', encoding='utf-8') as f:
            files["svg"] = f.read()
        files["svg_path"] = svg_path

    return files

def validate_topic(files):
    """Validate all files in a topic"""
    issues = {}

    # Validate SVG
    if "svg" in files:
        svg_errors = validate_svg(files["svg"])
        if svg_errors:
            issues["svg"] = svg_errors

    # Validate JSONs
    for json_file in ["mcqs.json", "flashcards.json", "questions.json", "visual.json"]:
        if json_file in files:
            json_errors = validate_json_file(files[json_file], json_file)
            if json_errors:
                issues[json_file] = json_errors

    return issues

def build_fix_prompt(topic_path, files, issues):
    """Build prompt to fix topic issues"""
    topic_id = os.path.basename(topic_path)
    topic_title = topic_id.replace('-', ' ').title()

    prompt = f"""You are fixing content for an educational topic: "{topic_title}"

=== CURRENT FILES ===

"""

    # Add read.md for context
    if "read.md" in files:
        prompt += f"=== read.md (context) ===\n{files['read.md'][:3000]}\n\n"

    # Add files with issues
    for file_name, file_issues in issues.items():
        if file_name in files:
            prompt += f"=== {file_name} (ISSUES: {', '.join(file_issues)}) ===\n{files[file_name][:2000]}\n\n"
        elif file_name == "svg" and "svg" in files:
            prompt += f"=== SVG (ISSUES: {', '.join(file_issues)}) ===\n{files['svg'][:2000]}\n\n"

    prompt += f"""
=== TASK ===
Fix the files with issues listed above. Return ONLY a valid JSON response:

{{
  "fixed_files": {{
"""

    # Add expected fixes
    fix_templates = []
    for file_name in issues.keys():
        if file_name == "svg":
            fix_templates.append(f'    "svg": "<svg width=\\"420\\" height=\\"400\\" ...complete valid SVG...</svg>"')
        elif file_name == "mcqs.json":
            fix_templates.append(f'    "mcqs.json": {{"topicId": "{topic_id}", "mcqs": [...]}}')
        elif file_name == "flashcards.json":
            fix_templates.append(f'    "flashcards.json": {{"topicId": "{topic_id}", "flashcards": [...]}}')
        elif file_name == "questions.json":
            fix_templates.append(f'    "questions.json": {{"topicId": "{topic_id}", "questions": [...]}}')
        elif file_name == "visual.json":
            fix_templates.append(f'    "visual.json": {{"topicId": "{topic_id}", "visuals": [...]}}')

    prompt += ",\n".join(fix_templates)
    prompt += """
  }
}

REQUIREMENTS:
- SVG: valid XML, width="420" height="400", include data-narration attributes, NO HTML elements (ul, li, div, footer, section)
- MCQs: minimum 5 MCQs with question, options (4), correctAnswer (0-3), explanation
- Flashcards: minimum 5 cards with front and back
- Questions: minimum 3 questions with question, answer, difficulty
- visual.json: reference the SVG file correctly

Return ONLY the JSON, no explanations."""

    return prompt

def apply_fixes(topic_path, fixes, files):
    """Apply fixes to topic files"""
    fixed_count = 0
    topic_id = os.path.basename(topic_path)

    for file_name, content in fixes.items():
        try:
            if file_name == "svg":
                # Extract SVG content
                if isinstance(content, str):
                    svg_match = re.search(r'<svg[^>]*>[\s\S]*?</svg>', content, re.IGNORECASE)
                    if svg_match:
                        svg_content = svg_match.group()
                        # Validate before saving
                        try:
                            ET.fromstring(svg_content)
                            svg_path = os.path.join(topic_path, "assets", f"{topic_id}.svg")
                            os.makedirs(os.path.dirname(svg_path), exist_ok=True)
                            with open(svg_path, 'w') as f:
                                f.write(svg_content)
                            fixed_count += 1
                        except:
                            pass

            elif file_name.endswith('.json'):
                # Parse and validate JSON
                if isinstance(content, str):
                    try:
                        data = json.loads(content)
                    except:
                        continue
                else:
                    data = content

                json_path = os.path.join(topic_path, file_name)
                with open(json_path, 'w') as f:
                    json.dump(data, f, indent=2)
                fixed_count += 1

        except Exception as e:
            pass

    return fixed_count

def process_topic(topic_path, model_index):
    """Process a single topic - validate and fix if needed"""
    topic_id = os.path.basename(topic_path)

    # Read all files
    files = read_topic_files(topic_path)
    if not files:
        return {"status": "skipped", "reason": "no files"}

    # Validate
    issues = validate_topic(files)

    if not issues:
        return {"status": "valid"}

    # Build prompt and call API
    prompt = build_fix_prompt(topic_path, files, issues)
    response, model_used = call_nvidia_api(prompt, model_index)

    if not response:
        return {"status": "failed", "reason": "API error", "issues": issues}

    # Parse response and apply fixes
    try:
        # Extract JSON from response
        json_match = re.search(r'\{[\s\S]*"fixed_files"[\s\S]*\}', response)
        if json_match:
            result = json.loads(json_match.group())
            fixes = result.get("fixed_files", {})
            fixed_count = apply_fixes(topic_path, fixes, files)

            if fixed_count > 0:
                return {"status": "fixed", "files_fixed": fixed_count, "model": model_used}
    except Exception as e:
        pass

    return {"status": "failed", "reason": "parse error", "issues": issues}

# ============== SUBJECT PROCESSING ==============
def find_subjects():
    """Find all subjects in CSE directory"""
    subjects = []
    for sem_dir in sorted(os.listdir(CSE_DIR)):
        sem_path = os.path.join(CSE_DIR, sem_dir)
        if os.path.isdir(sem_path) and sem_dir.startswith("sem-"):
            for subject_dir in sorted(os.listdir(sem_path)):
                subject_path = os.path.join(sem_path, subject_dir)
                if os.path.isdir(subject_path):
                    subjects.append({
                        "semester": sem_dir,
                        "name": subject_dir,
                        "path": subject_path
                    })
    return subjects

def find_topics(subject_path):
    """Find all topics in a subject"""
    topics = []
    chapters_path = os.path.join(subject_path, "chapters")

    if not os.path.exists(chapters_path):
        return topics

    for root, dirs, files in os.walk(chapters_path):
        if "topics" in root and "read.md" in files:
            topics.append(root)

    return topics

def process_subject(subject, subject_index, total_subjects):
    """Process all topics in a subject using parallel models"""
    global stats

    subject_name = subject["name"]
    subject_path = subject["path"]
    semester = subject["semester"]

    log(f"\n{'='*60}")
    log(f"[{subject_index+1}/{total_subjects}] {semester}/{subject_name}")
    log(f"{'='*60}")

    # Find all topics
    topics = find_topics(subject_path)
    if not topics:
        log(f"  No topics found, skipping...")
        return

    log(f"  Found {len(topics)} topics")

    with stats_lock:
        stats["topics_total"] += len(topics)

    # Process topics in parallel (7 models)
    results = {"valid": 0, "fixed": 0, "failed": 0, "files_fixed": 0}

    with ThreadPoolExecutor(max_workers=7) as executor:
        futures = {}
        for i, topic_path in enumerate(topics):
            model_index = i % len(MODELS_100B)
            future = executor.submit(process_topic, topic_path, model_index)
            futures[future] = topic_path

        for future in as_completed(futures):
            topic_path = futures[future]
            topic_id = os.path.basename(topic_path)

            try:
                result = future.result()
                status = result.get("status", "failed")

                if status == "valid":
                    results["valid"] += 1
                elif status == "fixed":
                    results["fixed"] += 1
                    results["files_fixed"] += result.get("files_fixed", 0)
                    log(f"  ✓ Fixed: {topic_id[:40]} ({result.get('model', '')[:20]})")
                else:
                    results["failed"] += 1

            except Exception as e:
                results["failed"] += 1

    # Update global stats
    with stats_lock:
        stats["subjects_processed"] += 1
        stats["topics_valid"] += results["valid"]
        stats["topics_fixed"] += results["fixed"]
        stats["topics_failed"] += results["failed"]
        stats["files_fixed"] += results["files_fixed"]

    log(f"  Summary: {results['valid']} valid, {results['fixed']} fixed, {results['failed']} failed")

# ============== MAIN ==============
def main():
    log("="*70)
    log("CSE PARALLEL FIX - 100B+ MODELS ONLY")
    log("="*70)
    log(f"Directory: {CSE_DIR}")
    log(f"Models: {len(MODELS_100B)} (100B+ only)")
    log(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log("")

    # Create report directory
    os.makedirs(REPORT_DIR, exist_ok=True)

    # Find all subjects
    subjects = find_subjects()
    log(f"Found {len(subjects)} subjects in CSE\n")

    start_time = time.time()

    # Process each subject
    for i, subject in enumerate(subjects):
        process_subject(subject, i, len(subjects))

        # Save intermediate report every 5 subjects
        if (i + 1) % 5 == 0:
            save_report(start_time)

    # Final report
    save_report(start_time, final=True)

    elapsed = time.time() - start_time
    log("")
    log("="*70)
    log("COMPLETE")
    log("="*70)
    log(f"Time: {elapsed/60:.1f} minutes")
    log(f"Subjects: {stats['subjects_processed']}")
    log(f"Topics: {stats['topics_total']}")
    log(f"  Valid: {stats['topics_valid']}")
    log(f"  Fixed: {stats['topics_fixed']}")
    log(f"  Failed: {stats['topics_failed']}")
    log(f"Files fixed: {stats['files_fixed']}")
    log(f"API calls: {stats['api_calls']}")

def save_report(start_time, final=False):
    """Save progress report"""
    elapsed = time.time() - start_time
    report = {
        "timestamp": datetime.now().isoformat(),
        "elapsed_minutes": round(elapsed / 60, 1),
        "stats": dict(stats),
        "models_used": MODELS_100B
    }

    filename = "final_report.json" if final else "progress_report.json"
    report_path = os.path.join(REPORT_DIR, filename)

    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)

if __name__ == "__main__":
    main()
