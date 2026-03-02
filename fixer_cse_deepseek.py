#!/usr/bin/env python3
"""
CSE DeepSeek Content Fix - Slower but working
Uses only DeepSeek models with longer timeout (300s)
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

DEEPSEEK_MODELS = [
    "deepseek-ai/deepseek-v3.2",
    "deepseek-ai/deepseek-v3.1",
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
    "model_usage": {m: 0 for m in DEEPSEEK_MODELS},
    "model_success": {m: 0 for m in DEEPSEEK_MODELS},
    "model_errors": {m: 0 for m in DEEPSEEK_MODELS},
}

last_checkpoint = time.time()
start_time = time.time()

# ============== API ==============
def call_api(prompt, model):
    """Call NVIDIA API with longer timeout for DeepSeek"""
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
        with urllib.request.urlopen(req, timeout=300) as response:  # 5 min timeout
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
        log(f"    Error: {str(e)[:50]}")
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
            if '<footer>' in svg or '<ul>' in svg or '<section' in svg or len(svg) < 200:
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
            context = f.read()[:1500]

    prompt = f"""Create educational content about "{topic_title}".

Context: {context[:1000]}

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
    svg_content = None
    mcqs_data = None
    flashcards_data = None

    try:
        json_match = re.search(r'\{[\s\S]*\}', response)
        if json_match:
            data = json.loads(json_match.group())
            if "svg" in data and isinstance(data["svg"], str):
                svg_content = data["svg"]
            if "mcqs" in data:
                mcqs_data = data["mcqs"]
            if "flashcards" in data:
                flashcards_data = data["flashcards"]
    except:
        pass

    if not svg_content:
        svg_match = re.search(r'<svg[^>]*>[\s\S]*?</svg>', response, re.IGNORECASE)
        if svg_match:
            svg_content = svg_match.group()
            if '\\n' in svg_content or '\\"' in svg_content:
                svg_content = svg_content.replace('\\n', '\n').replace('\\"', '"').replace('\\/', '/')

    # Save SVG
    if svg_content and svg_content.strip().startswith('<svg'):
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

# ============== STATUS ==============
def print_status():
    """Print status of DeepSeek models"""
    elapsed = (time.time() - start_time) / 60

    log("")
    log("=" * 60)
    log(f"DEEPSEEK STATUS - {elapsed:.1f} minutes elapsed")
    log("=" * 60)
    log(f"Topics: {stats['topics_processed']} processed, {stats['topics_fixed']} fixed")
    log(f"API calls: {stats['api_calls']}, Errors: {stats['errors']}")
    log("")

    for model in DEEPSEEK_MODELS:
        usage = stats['model_usage'][model]
        success = stats['model_success'][model]
        errors = stats['model_errors'][model]
        rate = (success / usage * 100) if usage > 0 else 0
        short_name = model.split('/')[-1]
        log(f"  {short_name:20} | calls: {usage:4} | success: {success:4} | errors: {errors:3} | rate: {rate:.0f}%")

    log("")

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
    model = DEEPSEEK_MODELS[model_index]

    for topic_path in topics_batch:
        topic_id = os.path.basename(topic_path)

        needs, reason = needs_fix(topic_path)

        with stats_lock:
            stats["topics_processed"] += 1

        if not needs:
            with stats_lock:
                stats["topics_skipped"] += 1
            continue

        log(f"  → {topic_id[:40]} ({model.split('/')[-1][:12]})")

        if fix_topic(topic_path, model):
            with stats_lock:
                stats["topics_fixed"] += 1
            log(f"  ✓ {topic_id[:40]} DONE")

        # Status every 5 mins
        if time.time() - last_checkpoint > 300:
            print_status()

def main():
    global start_time, last_checkpoint

    log("=" * 60)
    log("DEEPSEEK SLOW FIX - 300s timeout")
    log("=" * 60)
    log(f"Models: {len(DEEPSEEK_MODELS)} (DeepSeek only)")
    log(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log("")

    start_time = time.time()
    last_checkpoint = start_time

    all_topics = find_all_topics()
    log(f"Found {len(all_topics)} topics in CSE")

    # Split topics between 2 models
    mid = len(all_topics) // 2
    batches = [all_topics[:mid], all_topics[mid:]]

    log(f"Split into 2 batches (~{mid} topics each)")
    log("")

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = []
        for i, batch in enumerate(batches):
            future = executor.submit(process_batch, batch, i)
            futures.append(future)

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                log(f"Batch error: {e}")

    print_status()
    log("DEEPSEEK COMPLETE")

if __name__ == "__main__":
    main()
