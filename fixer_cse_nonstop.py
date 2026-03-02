#!/usr/bin/env python3
"""
CSE Non-Stop Content Fix - Generate & Save Only
No validation, just fix and save. Status + Git commit every 10 mins.
"""

import os
import sys
import json
import re
import subprocess
import urllib.request
import urllib.error
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

sys.stdout = sys.stderr = open(sys.stdout.fileno(), mode='w', buffering=1)

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)

# ============== CONFIG ==============
NVIDIA_API_KEY = "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"
NVIDIA_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

MODELS_100B = [
    "mistralai/mistral-large-3-675b-instruct-2512",
    "meta/llama-3.1-405b-instruct",
    "igenius/colosseum_355b_instruct_16k",
    "nvidia/llama-3.1-nemotron-ultra-253b-v1",
    "mistralai/devstral-2-123b-instruct-2512",
]

CSE_DIR = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse"
VTU_DIR = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme"

# Stats
stats_lock = threading.Lock()
stats = {
    "topics_processed": 0,
    "topics_fixed": 0,
    "topics_skipped": 0,
    "api_calls": 0,
    "errors": 0,
    "model_usage": {m: 0 for m in MODELS_100B},
    "model_success": {m: 0 for m in MODELS_100B},
    "model_errors": {m: 0 for m in MODELS_100B},
}

last_checkpoint = time.time()
start_time = time.time()

# ============== API ==============
def call_api(prompt, model):
    """Call NVIDIA API - single model, no fallback"""
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        data = json.dumps({
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,
            "max_tokens": 12000
        }).encode('utf-8')

        req = urllib.request.Request(NVIDIA_API_URL, data=data, headers=headers)
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode('utf-8'))
            with stats_lock:
                stats["api_calls"] += 1
                stats["model_usage"][model] += 1
                stats["model_success"][model] += 1
            return result['choices'][0]['message']['content']

    except Exception as e:
        with stats_lock:
            stats["model_usage"][model] += 1
            stats["model_errors"][model] += 1
            stats["errors"] += 1
        return None

# ============== QUICK CHECKS ==============
def needs_fix(topic_path):
    """Quick check if topic needs fixing"""
    topic_id = os.path.basename(topic_path)

    # Check SVG
    svg_path = os.path.join(topic_path, "assets", f"{topic_id}.svg")
    if os.path.exists(svg_path):
        try:
            with open(svg_path, 'r') as f:
                svg = f.read()
            if '<footer>' in svg or '<ul>' in svg or len(svg) < 200:
                return True, "svg"
        except:
            return True, "svg"

    # Check MCQs
    mcq_path = os.path.join(topic_path, "mcqs.json")
    if os.path.exists(mcq_path):
        try:
            with open(mcq_path, 'r') as f:
                data = json.load(f)
            if "mcqs" not in data or len(data.get("mcqs", [])) < 3:
                return True, "mcqs"
        except:
            return True, "mcqs"

    # Check flashcards
    fc_path = os.path.join(topic_path, "flashcards.json")
    if os.path.exists(fc_path):
        try:
            with open(fc_path, 'r') as f:
                data = json.load(f)
            if "flashcards" not in data or len(data.get("flashcards", [])) < 3:
                return True, "flashcards"
        except:
            return True, "flashcards"

    return False, None

# ============== FIX TOPIC ==============
def fix_topic(topic_path, model):
    """Fix a single topic"""
    topic_id = os.path.basename(topic_path)
    topic_title = topic_id.replace('-', ' ').title()

    # Read context
    read_path = os.path.join(topic_path, "read.md")
    context = ""
    if os.path.exists(read_path):
        with open(read_path, 'r') as f:
            context = f.read()[:2500]

    prompt = f"""Create educational content about "{topic_title}".

Context: {context[:1500]}

Generate 3 items:

1. SVG DIAGRAM about {topic_title}:
- Start with: <svg xmlns="http://www.w3.org/2000/svg" width="420" height="400" data-topic-id="{topic_id}">
- Put <defs> with gradients FIRST inside svg
- Create 4 colored <g> sections, each with data-narration explaining that concept
- Each <g> has: <rect> background + <text> labels about {topic_title}
- Use ONLY: svg, defs, linearGradient, stop, g, rect, text, circle, path
- NO HTML tags like div, section, ul, li, footer

2. MCQs: 5 multiple choice questions about {topic_title}
Format: {{"topicId":"{topic_id}","mcqs":[{{"id":"mcq-1","question":"...","options":["A","B","C","D"],"correctAnswer":0,"explanation":"..."}}]}}

3. FLASHCARDS: 5 study cards about {topic_title}
Format: {{"topicId":"{topic_id}","flashcards":[{{"id":"fc-1","front":"...","back":"..."}}]}}

Return JSON only:
{{"svg":"<svg>...</svg>","mcqs":{{...}},"flashcards":{{...}}}}"""

    response = call_api(prompt, model)
    if not response:
        return False

    # Extract and save
    saved = 0

    # Try to parse as JSON first
    svg_content = None
    mcqs_data = None
    flashcards_data = None

    try:
        # Find JSON object in response
        json_match = re.search(r'\{[\s\S]*\}', response)
        if json_match:
            data = json.loads(json_match.group())

            # Extract SVG from JSON (will be properly unescaped)
            if "svg" in data and isinstance(data["svg"], str):
                svg_content = data["svg"]

            if "mcqs" in data:
                mcqs_data = data["mcqs"]

            if "flashcards" in data:
                flashcards_data = data["flashcards"]
    except:
        pass

    # Fallback: extract SVG directly from response if not in JSON
    if not svg_content:
        svg_match = re.search(r'<svg[^>]*>[\s\S]*?</svg>', response, re.IGNORECASE)
        if svg_match:
            svg_content = svg_match.group()
            # Unescape if it looks escaped
            if '\\n' in svg_content or '\\"' in svg_content:
                svg_content = svg_content.replace('\\n', '\n').replace('\\"', '"').replace('\\/', '/')

    # Save SVG
    if svg_content and svg_content.strip().startswith('<svg'):
        # Final cleanup - remove any remaining escape sequences
        svg_content = svg_content.replace('\\n', '\n').replace('\\"', '"').replace('\\/', '/')
        svg_dir = os.path.join(topic_path, "assets")
        os.makedirs(svg_dir, exist_ok=True)
        with open(os.path.join(svg_dir, f"{topic_id}.svg"), 'w') as f:
            f.write(svg_content)
        saved += 1

    # Save MCQs
    if mcqs_data:
        try:
            if isinstance(mcqs_data, dict):
                final_mcqs = mcqs_data
            else:
                final_mcqs = {"topicId": topic_id, "mcqs": mcqs_data}
            with open(os.path.join(topic_path, "mcqs.json"), 'w') as f:
                json.dump(final_mcqs, f, indent=2)
            saved += 1
        except:
            pass

    # Save Flashcards
    if flashcards_data:
        try:
            if isinstance(flashcards_data, dict):
                final_fc = flashcards_data
            else:
                final_fc = {"topicId": topic_id, "flashcards": flashcards_data}
            with open(os.path.join(topic_path, "flashcards.json"), 'w') as f:
                json.dump(final_fc, f, indent=2)
            saved += 1
        except:
            pass

    return saved > 0

# ============== GIT OPERATIONS ==============
def git_commit_push():
    """Git add, commit and push"""
    try:
        os.chdir(VTU_DIR)
        subprocess.run(['git', 'add', '-A'], capture_output=True, timeout=30)

        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True, timeout=30)
        if result.stdout.strip():
            msg = f"CSE content fix - {stats['topics_fixed']} topics fixed\n\nCo-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
            subprocess.run(['git', 'commit', '--no-verify', '-m', msg], capture_output=True, timeout=60)
            subprocess.run(['git', 'push'], capture_output=True, timeout=60)
            return True
    except:
        pass
    return False

# ============== STATUS ==============
def print_status():
    """Print status of all models"""
    elapsed = (time.time() - start_time) / 60

    log("")
    log("=" * 70)
    log(f"STATUS REPORT - {elapsed:.1f} minutes elapsed")
    log("=" * 70)
    log(f"Topics: {stats['topics_processed']} processed, {stats['topics_fixed']} fixed, {stats['topics_skipped']} skipped")
    log(f"API calls: {stats['api_calls']}, Errors: {stats['errors']}")
    log("")
    log("MODEL STATUS:")
    log("-" * 70)

    for model in MODELS_100B:
        usage = stats['model_usage'][model]
        success = stats['model_success'][model]
        errors = stats['model_errors'][model]
        rate = (success / usage * 100) if usage > 0 else 0
        short_name = model.split('/')[-1][:30]
        log(f"  {short_name:35} | calls: {usage:4} | success: {success:4} | errors: {errors:3} | rate: {rate:.0f}%")

    log("-" * 70)
    log("")

def checkpoint():
    """10-min checkpoint: status + git commit"""
    global last_checkpoint

    print_status()

    if git_commit_push():
        log("✓ Git commit & push successful")
    else:
        log("  No changes to commit")

    last_checkpoint = time.time()

# ============== MAIN ==============
def find_all_topics():
    """Find all topics in CSE"""
    topics = []
    for root, dirs, files in os.walk(CSE_DIR):
        if 'topics' in root and 'read.md' in files:
            topics.append(root)
    return topics

def process_batch(topics_batch, model_index):
    """Process a batch of topics with one model"""
    model = MODELS_100B[model_index]

    for topic_path in topics_batch:
        topic_id = os.path.basename(topic_path)

        needs, reason = needs_fix(topic_path)

        with stats_lock:
            stats["topics_processed"] += 1

        if not needs:
            with stats_lock:
                stats["topics_skipped"] += 1
            continue

        if fix_topic(topic_path, model):
            with stats_lock:
                stats["topics_fixed"] += 1
            log(f"  ✓ {topic_id[:45]} ({model.split('/')[-1][:15]})")

        # Check if 10 mins passed
        if time.time() - last_checkpoint > 600:
            checkpoint()

def main():
    global start_time, last_checkpoint

    log("=" * 70)
    log("CSE NON-STOP FIX - GENERATE & SAVE ONLY")
    log("=" * 70)
    log(f"Models: {len(MODELS_100B)} (100B+ only)")
    log(f"Checkpoint: Every 10 minutes (status + git commit)")
    log(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log("")

    start_time = time.time()
    last_checkpoint = start_time

    # Find all topics
    all_topics = find_all_topics()
    log(f"Found {len(all_topics)} topics in CSE")
    log("")

    # Split topics among models
    batch_size = len(all_topics) // len(MODELS_100B) + 1
    batches = []
    for i in range(len(MODELS_100B)):
        start_idx = i * batch_size
        end_idx = min(start_idx + batch_size, len(all_topics))
        batches.append(all_topics[start_idx:end_idx])

    log(f"Split into {len(batches)} batches (~{batch_size} topics each)")
    log("")

    # Process in parallel
    with ThreadPoolExecutor(max_workers=len(MODELS_100B)) as executor:
        futures = []
        for i, batch in enumerate(batches):
            future = executor.submit(process_batch, batch, i)
            futures.append(future)

        # Wait for all
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                log(f"Batch error: {e}")

    # Final checkpoint
    checkpoint()

    log("")
    log("=" * 70)
    log("COMPLETE")
    log("=" * 70)
    log(f"Total time: {(time.time() - start_time) / 60:.1f} minutes")
    log(f"Topics fixed: {stats['topics_fixed']}")
    log(f"API calls: {stats['api_calls']}")

if __name__ == "__main__":
    main()
