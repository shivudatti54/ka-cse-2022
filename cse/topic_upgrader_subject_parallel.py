#!/usr/bin/env python3
"""
VTU Topic Upgrader - Subject-Parallel with Smart Batching

KEY FEATURES:
- One thread per subject (parallel subjects, sequential topics within each)
- Smart batching: 2 API calls per topic (like nvidia_content_generator.py)
  * Call 1: read.md + purpose.md + summary.md (batched)
  * Call 2: flashcards.json + mcqs.json + memory.json + questions.json + visual.json + code.json (batched)
- Simple 300s timeout with 30s heartbeat monitoring
- Blocking I/O (urllib) - simpler, more predictable
- 8 API support: NVIDIA + Cerebras + Groq + SambaNova + Fireworks + OpenRouter + Chutes + MiniMax

Usage:
  # Default: All 8 APIs with round-robin distribution
  python3 topic_upgrader_subject_parallel.py sem4-topic-paths.txt --log

  # Use specific API only
  python3 topic_upgrader_subject_parallel.py sem4-topic-paths.txt --cerebras-only  # FASTEST
  python3 topic_upgrader_subject_parallel.py sem4-topic-paths.txt --groq-only

  # Start from specific topic
  python3 topic_upgrader_subject_parallel.py sem4-topic-paths.txt --start-from-topic 101 --log

  # Resume from last run
  python3 topic_upgrader_subject_parallel.py sem4-topic-paths.txt --resume --log
"""

import argparse
import json
import logging
import os
import random
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from threading import Thread, Lock, Event, Semaphore
from queue import Queue

# ── Logging ────────────────────────────────────────────────────────────────
logger = logging.getLogger("vtu_upgrader")
log_handler = logging.StreamHandler()
log_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
log_handler.setFormatter(log_formatter)
logger.addHandler(log_handler)
logger.setLevel(logging.WARNING)

# ── Configuration ──────────────────────────────────────────────────────────
APIS = {
    "nvidia": {
        "base_url": "https://integrate.api.nvidia.com/v1/chat/completions",
        "api_key": "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",
        "model": "meta/llama-3.3-70b-instruct",  # 70B - fast, high quality
        "sequential_only": True,  # NVIDIA doesn't support parallel calls
    },
    "cerebras": {
        "base_url": "https://api.cerebras.ai/v1/chat/completions",
        "api_key": "csk-2j8ex22cy2f9yw6k4v422eyyemjhwntrenemedw4jyf5hcy9",
        "model": "llama-3.3-70b",  # 70B - EXTREMELY FAST (0.5s response, 1M tokens/day)
        "sequential_only": False,  # Can handle parallel (64K tokens/min, 30 req/min)
        "needs_user_agent": True,  # Cloudflare protection
    },
    "groq": {
        "base_url": "https://api.groq.com/openai/v1/chat/completions",
        "api_key": "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",
        "model": "llama-3.3-70b-versatile",  # 70B - very fast (Groq has hardware acceleration)
        "sequential_only": True,  # 12K tokens/min limit - treat like NVIDIA
        "needs_user_agent": True,  # Groq requires User-Agent header
    },
    "sambanova": {
        "base_url": "https://api.sambanova.ai/v1/chat/completions",
        "api_key": "971fb779-d029-4f56-a848-1fa3b10b14bc",
        "model": "Meta-Llama-3.3-70B-Instruct",  # 70B - reliable (free tier)
        "sequential_only": True,  # 20 requests/day limit - sequential only
    },
    "fireworks": {
        "base_url": "https://api.fireworks.ai/inference/v1/chat/completions",
        "api_key": "fw_4bf7CVfr7PkNS9frh2AzmQ",
        "model": "accounts/fireworks/models/llama-v3p3-70b-instruct",  # 70B - fast
        "sequential_only": True,  # 60 requests limit - sequential only
        "needs_user_agent": True,  # Cloudflare protection
    },
    "openrouter": {
        "base_url": "https://openrouter.ai/api/v1/chat/completions",
        "api_key": "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",
        "model": "meta-llama/llama-3.3-70b-instruct:free",  # 70B - FREE tier
        "sequential_only": True,  # 50 calls/day limit - sequential only
    },
    "chutes": {
        "base_url": "https://llm.chutes.ai/v1/chat/completions",
        "api_key": "cpk_a744b82c5b9c4e8b9c7c8e1442e8d160.c3a84cdb26e850c9b8f358af872bca49.ymNhlwAf2nbhnTZJE620p8sv1aTgEGwx",
        "model": "deepseek-ai/DeepSeek-R1-TEE",  # 671B (uses reasoning_content field)
        "sequential_only": False,
        "uses_reasoning": True,  # DeepSeek R1 returns content in reasoning_content field
    },
    "minimax": {
        "base_url": "https://api.minimax.io/v1/chat/completions",
        "api_key": "sk-cp-r--6hiKCzLgU9QbQREFxR4v336s2kP0vDCeb3x7-iNJxAAdDwQeXhInB8zgfwcduBNoBtQBSj33uci2eCKcCu7q4VjmMGWDhKYHXu_lpv1fmWctproM4cAg",
        "model": "MiniMax-M2.5",  # 456B model (working with new API key)
        "sequential_only": False,
        "uses_reasoning": True,  # MiniMax also uses <think> tags
    },
}

REQUEST_TIMEOUT = 300  # 5 minutes total (like NVIDIA)
HEARTBEAT_INTERVAL = 30  # Log progress every 30 seconds
MAX_TOKENS = 8192
TEMPERATURE = 0.3
MAX_RETRIES = 2
RETRY_DELAY = 3
PROGRESS_FILE = "upgrade_progress.json"
DEFAULT_THREADS = 5  # 5 subjects in parallel (Chutes/MiniMax can handle more)
MAX_CONCURRENT_API_CALLS = 15  # Max 15 API calls for Chutes/MiniMax (they can handle parallel load)
API_CALL_DELAY = 0.5  # 0.5 second delay (reduced from 1s - Chutes/MiniMax are fast)

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
    "diagrams": [
      {
        "id": "diagram-1",
        "title": "Title",
        "description": "What it shows",
        "elements": ["Element 1", "Element 2"],
        "purpose": "Learning purpose"
      }
    ],
    "charts": [{"type": "flowchart", "title": "Title", "content": "What it illustrates"}],
    "mindMaps": [{"centralConcept": "Main", "branches": ["Branch 1"], "purpose": "Overview"}]
  },
  "code": [
    {
      "id": "code-1",
      "language": "pseudocode",
      "title": "Algorithm Title",
      "description": "What this demonstrates",
      "code": "ALGORITHM\\nBEGIN\\n...\\nEND",
      "explanation": "Line-by-line explanation",
      "complexity": {"time": "O(n)", "space": "O(1)"}
    }
  ]
}

GENERATION RULES:
- flashcards: 20-25 cards
- mcqs: 15-20 questions (4-5 easy, 8-10 medium, 3-5 hard)
- memory: 4-6 mnemonics, 3-5 acronyms, 4-6 visual tips, 3-5 analogies
- questions: 12-15 VTU-style questions (mix short/long/numerical)
- visual: 3-5 diagrams, 2-4 charts, 1-2 mind maps
- code: 3-5 examples IF applicable (return [] if purely conceptual)
"""

# ── Progress Tracking & Rate Limiting ─────────────────────────────────────
progress_lock = Lock()
stats_lock = Lock()
api_semaphore = None  # Global semaphore for API rate limiting (initialized in main)
nvidia_semaphore = None  # Dedicated semaphore for NVIDIA (max 1 concurrent call)
last_api_call_time = 0
api_call_lock = Lock()
shutdown_event = Event()

global_stats = {
    "topics_processed": 0,
    "topics_success": 0,
    "topics_partial": 0,
    "topics_failed": 0,
    "api_calls_success": 0,
    "api_calls_failed": 0,
    "api_calls_nvidia": 0,
    "api_calls_chutes": 0,
    "api_calls_minimax": 0,
}

def load_progress():
    """Load completed topics from progress file."""
    if not Path(PROGRESS_FILE).exists():
        return set()
    try:
        data = json.loads(Path(PROGRESS_FILE).read_text())
        return set(data.get("completed", []))
    except Exception:
        return set()

def save_progress(completed: set):
    """Save completed topics to progress file."""
    with progress_lock:
        try:
            Path(PROGRESS_FILE).write_text(json.dumps({
                "completed": list(completed),
                "last_updated": datetime.now().isoformat()
            }, indent=2))
        except Exception as e:
            logger.error(f"Could not save progress: {e}")

# ── Topic Context ──────────────────────────────────────────────────────────
def get_topic_context(topic_path: str) -> dict:
    """Extract subject/module/topic metadata from directory path."""
    topic_dir = Path(topic_path)
    parts = topic_dir.parts

    try:
        ti = len(parts) - 1
        module_i = ti - 2
        subject_i = module_i - 2
        sem_i = subject_i - 1
    except Exception:
        return None

    topic_id = parts[ti]
    module_id = parts[module_i]
    subject_dir = parts[subject_i]

    m = re.match(r"(bcsl?\d+[a-d]?)-(.+)", subject_dir)
    if m:
        subject_code = m.group(1).upper()
        subject_name = m.group(2).replace("-", " ").title()
    else:
        subject_code = subject_dir.upper()
        subject_name = subject_dir.replace("-", " ").title()

    module_num = module_id.split("-")[-1]
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
        "topic_id": topic_id,
        "topic_title": topic_title,
        "module_num": module_num,
        "module_id": module_id,
        "subject_code": subject_code,
        "subject_name": subject_name,
        "subject_dir": subject_dir,
        "siblings": sibling_topics,
    }

# ── API Calling (Blocking with Heartbeat) ──────────────────────────────────
def call_api_with_heartbeat(api_name: str, messages: list, topic_idx: int, file_desc: str) -> dict:
    """Call API with timeout, heartbeat logging, and rate limiting."""
    global last_api_call_time
    if shutdown_event.is_set():
        raise RuntimeError("Shutdown requested")

    # Rate limiting: ensure minimum delay between API calls
    with api_call_lock:
        now = time.time()
        time_since_last = now - last_api_call_time
        if time_since_last < API_CALL_DELAY:
            sleep_time = API_CALL_DELAY - time_since_last
            time.sleep(sleep_time)
        last_api_call_time = time.time()

    # For sequential-only APIs (NVIDIA, Groq, OpenRouter), use dedicated semaphore (max 1 concurrent call)
    # For others (Chutes, MiniMax), use general semaphore (max 15 concurrent)
    if APIS[api_name].get("sequential_only", False):
        nvidia_semaphore.acquire()
        semaphore_to_release = nvidia_semaphore
    else:
        api_semaphore.acquire()
        semaphore_to_release = api_semaphore

    try:
        api = APIS[api_name]
        payload = json.dumps({
            "model": api["model"],
            "max_tokens": MAX_TOKENS,
            "temperature": TEMPERATURE,
            "messages": messages,
        }).encode()

        ctx = ssl.create_default_context()
        req = urllib.request.Request(
            api["base_url"],
            data=payload,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api['api_key']}",
            },
            method="POST"
        )

        # Add User-Agent for Groq (Cloudflare requirement)
        if api.get("needs_user_agent", False):
            req.add_header('User-Agent', 'Mozilla/5.0')

        start_time = time.time()
        model_name = api["model"]
        logger.info(f"Topic #{topic_idx} | {file_desc} | Starting API call via {api_name.upper()} ({model_name})")

        # Heartbeat monitoring (log every 30s while waiting)
        heartbeat_event = Event()
        def heartbeat():
            while not heartbeat_event.is_set():
                if heartbeat_event.wait(HEARTBEAT_INTERVAL):
                    break
                elapsed = time.time() - start_time
                logger.debug(f"Topic #{topic_idx} | {file_desc} | Still waiting... {elapsed:.0f}s elapsed")

        heartbeat_thread = Thread(target=heartbeat, daemon=True)
        heartbeat_thread.start()

        try:
            resp = urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT, context=ctx)
            result = json.loads(resp.read().decode())
            elapsed = time.time() - start_time
            model_name = api["model"]
            logger.info(f"Topic #{topic_idx} | {file_desc} | ✓ Success in {elapsed:.1f}s via {api_name.upper()} ({model_name})")
            return result
        except urllib.error.HTTPError as e:
            elapsed = time.time() - start_time
            logger.error(f"Topic #{topic_idx} | {file_desc} | HTTP {e.code} after {elapsed:.1f}s")
            raise
        except Exception as e:
            elapsed = time.time() - start_time
            logger.error(f"Topic #{topic_idx} | {file_desc} | Error after {elapsed:.1f}s: {str(e)[:100]}")
            raise
        finally:
            heartbeat_event.set()
            heartbeat_thread.join(timeout=1)
    finally:
        # Always release the correct semaphore
        semaphore_to_release.release()

def extract_text(response: dict, api_name: str = None) -> str:
    """Extract text content from API response."""
    message = response.get("choices", [{}])[0].get("message", {})
    content = message.get("content", "")

    # Handle DeepSeek R1 format (Chutes) - reasoning in separate field
    if not content and api_name == "chutes":
        content = message.get("reasoning_content", "")

    return content.strip()

def extract_json_from_text(text: str) -> dict:
    """Extract JSON from response, handling markdown fences."""
    # Remove markdown fences
    if text.startswith("```"):
        text = text[text.index("\n")+1:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

    # Find JSON object
    start = text.find("{")
    if start == -1:
        raise ValueError("No JSON object found")

    # Use JSON decoder directly so braces inside strings don't break parsing.
    decoder = json.JSONDecoder()
    payload = text[start:]
    try:
        obj, _ = decoder.raw_decode(payload)
        return obj
    except json.JSONDecodeError:
        # If extra non-JSON text is appended, trim to last brace and retry.
        last_brace = payload.rfind("}")
        if last_brace != -1:
            trimmed = payload[:last_brace + 1]
            obj, _ = decoder.raw_decode(trimmed)
            return obj
        raise ValueError("Unclosed JSON object")

def _retry_sleep_seconds(exc: Exception, attempt: int) -> float:
    """Backoff policy with 429-aware delay and jitter."""
    if isinstance(exc, urllib.error.HTTPError) and exc.code == 429:
        retry_after = exc.headers.get("Retry-After")
        if retry_after and retry_after.isdigit():
            base = float(retry_after)
        else:
            base = RETRY_DELAY * (2 ** attempt)
    else:
        base = RETRY_DELAY * (1.5 ** attempt)
    return min(60.0, base + random.uniform(0.2, 1.0))

# ── Content Generation (Smart Batching) ───────────────────────────────────
def generate_markdown_batch(api_name: str, topic_idx: int, ctx: dict) -> dict:
    """Call 1: Generate read.md + purpose.md + summary.md in ONE call."""
    siblings_str = ", ".join(ctx["siblings"][:15]) if ctx["siblings"] else "(no sibling info)"
    user_msg = (
        f'Subject: {ctx["subject_code"]} — {ctx["subject_name"]} (VTU 2022 Scheme)\n'
        f'Module {ctx["module_num"]} topics: {siblings_str}\n\n'
        f'Generate 8+ quality content for: "{ctx["topic_title"]}"\n'
        f'Topic ID: {ctx["topic_id"]}'
    )

    messages = [
        {"role": "system", "content": MARKDOWN_SYSTEM},
        {"role": "user", "content": user_msg},
    ]

    for attempt in range(MAX_RETRIES + 1):
        try:
            resp = call_api_with_heartbeat(api_name, messages, topic_idx, "Markdown batch")
            text = extract_text(resp, api_name)

            # Parse delimited response
            result = {}
            for key, start_tag, end_tag in [
                ("read.md", "===READ_MD===", "===PURPOSE_MD==="),
                ("purpose.md", "===PURPOSE_MD===", "===SUMMARY_MD==="),
                ("summary.md", "===SUMMARY_MD===", "===END==="),
            ]:
                s = text.find(start_tag)
                e = text.find(end_tag) if end_tag != "===END===" else text.find("===END===")
                if e == -1 and end_tag == "===END===":
                    e = len(text)

                if s != -1 and e > s:
                    chunk = text[s + len(start_tag):e].strip()
                    result[key] = chunk
                else:
                    result[key] = None

            # Validate
            if result.get("read.md") and result.get("purpose.md"):
                return result
            else:
                logger.warning(f"Topic #{topic_idx} | Markdown batch incomplete (attempt {attempt+1})")
                if attempt < MAX_RETRIES:
                    time.sleep(_retry_sleep_seconds(ValueError("incomplete markdown"), attempt))
                    continue
                return result

        except Exception as e:
            logger.warning(f"Topic #{topic_idx} | Markdown batch error: {str(e)[:100]} (attempt {attempt+1})")
            if attempt < MAX_RETRIES:
                time.sleep(_retry_sleep_seconds(e, attempt))
                continue
            return {}

    return {}

def generate_assessment_batch(api_name: str, topic_idx: int, ctx: dict, read_content: str) -> dict:
    """Call 2: Generate all JSON assessment files in ONE call."""
    rc = read_content[:6000] if len(read_content) > 6000 else read_content
    prompt = ASSESSMENT_SYSTEM.replace("TOPIC_ID", ctx["topic_id"])
    user_msg = (
        f'Subject: {ctx["subject_code"]} — {ctx["subject_name"]}\n'
        f'Topic: "{ctx["topic_title"]}" (id: {ctx["topic_id"]})\n\n'
        f'== TOPIC CONTENT ==\n{rc}\n\n'
        f'Generate 8+ quality assessment materials.\n'
        f'topicId must be exactly "{ctx["topic_id"]}".'
    )

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_msg},
    ]

    for attempt in range(MAX_RETRIES + 1):
        try:
            resp = call_api_with_heartbeat(api_name, messages, topic_idx, "Assessment batch")
            text = extract_text(resp, api_name)
            data = extract_json_from_text(text)

            # Fix topicId
            if "memory" in data and isinstance(data["memory"], dict):
                data["memory"]["topicId"] = ctx["topic_id"]
            if "visual" in data and isinstance(data["visual"], dict):
                data["visual"]["topicId"] = ctx["topic_id"]

            # Validate
            required_keys = ["flashcards", "mcqs", "questions"]
            if all(k in data for k in required_keys):
                return data
            else:
                logger.warning(f"Topic #{topic_idx} | Assessment batch incomplete (attempt {attempt+1})")
                if attempt < MAX_RETRIES:
                    time.sleep(_retry_sleep_seconds(ValueError("incomplete assessment"), attempt))
                    continue
                return data

        except Exception as e:
            logger.warning(f"Topic #{topic_idx} | Assessment batch error: {str(e)[:100]} (attempt {attempt+1})")
            if attempt < MAX_RETRIES:
                time.sleep(_retry_sleep_seconds(e, attempt))
                continue
            return {}

    return {}

# ── Topic Processing ───────────────────────────────────────────────────────
def process_topic(topic_idx: int, topic_path: str, api_name: str, dry_run: bool) -> dict:
    """Process one topic with smart batching (2 API calls)."""
    topic_dir = Path(topic_path)
    start_time = time.time()

    ctx = get_topic_context(topic_path)
    if not ctx:
        logger.error(f"Topic #{topic_idx} | Could not parse topic path: {topic_path}")
        return {"success": False, "files_written": 0}

    display_label = f"{ctx['subject_code']} M{ctx['module_num']}: {ctx['topic_title']}"
    timestamp = datetime.now().strftime("%H:%M:%S")
    api_model = APIS[api_name]["model"].split("/")[-1] if "/" in APIS[api_name]["model"] else APIS[api_name]["model"]
    print(f"  [{timestamp}] 🚀 START  #{topic_idx:<4} {display_label:<50} ({api_name.upper()}: {api_model})")

    result = {"success": False, "files_written": 0, "errors": []}

    # Call 1: Markdown files
    markdown_data = generate_markdown_batch(api_name, topic_idx, ctx)

    # Call 2: Assessment files (use read.md if available)
    read_content = markdown_data.get("read.md", "")
    if not read_content:
        # Fallback: read existing read.md
        read_file = topic_dir / "read.md"
        if read_file.exists():
            read_content = read_file.read_text(encoding="utf-8", errors="replace")[:6000]

    assessment_data = generate_assessment_batch(api_name, topic_idx, ctx, read_content)

    # Write files
    files_written = 0
    if not dry_run:
        topic_dir.mkdir(parents=True, exist_ok=True)

        # Write markdown files
        for filename, content in markdown_data.items():
            if content:
                try:
                    (topic_dir / filename).write_text(content, encoding="utf-8")
                    files_written += 1
                    logger.debug(f"Topic #{topic_idx} | Wrote {filename}")
                except Exception as e:
                    result["errors"].append(f"{filename}: {str(e)[:50]}")

        # Write JSON files
        json_files = {
            "flashcards.json": assessment_data.get("flashcards", []),
            "mcqs.json": assessment_data.get("mcqs", []),
            "memory.json": assessment_data.get("memory", {}),
            "questions.json": assessment_data.get("questions", []),
            "visual.json": assessment_data.get("visual", {}),
            "code.json": assessment_data.get("code", []),
        }

        for filename, content in json_files.items():
            # Write empty arrays/objects too; [] and {} are valid outputs.
            if content is not None:
                try:
                    (topic_dir / filename).write_text(
                        json.dumps(content, indent=2, ensure_ascii=False),
                        encoding="utf-8"
                    )
                    files_written += 1
                    logger.debug(f"Topic #{topic_idx} | Wrote {filename}")
                except Exception as e:
                    result["errors"].append(f"{filename}: {str(e)[:50]}")

    elapsed = time.time() - start_time
    timestamp = datetime.now().strftime("%H:%M:%S")

    # Determine success
    if files_written >= 7:  # At least 7/9 files
        status = "✅"
        result["success"] = True
    elif files_written >= 3:
        status = "⚠️"
    else:
        status = "❌"

    result["files_written"] = files_written

    print(f"  [{timestamp}] {status} DONE   #{topic_idx:<4} {display_label:<50} ({elapsed:>5.1f}s) {files_written}/9 files ({api_name.upper()})")

    if result["errors"] and len(result["errors"]) <= 3:
        for err in result["errors"]:
            print(f"            ↳ {err}")

    return result

# ── Global API Round-Robin ────────────────────────────────────────────────
global_api_counter = 0
global_api_counter_lock = Lock()

def get_next_api(available_apis: list) -> str:
    """Get next API using global round-robin (thread-safe)."""
    global global_api_counter

    with global_api_counter_lock:
        # Simple round-robin: distribute evenly across all available APIs
        # With 5 APIs: nvidia, groq, openrouter, chutes, minimax
        # Each gets 20% of calls
        api_name = available_apis[global_api_counter % len(available_apis)]
        global_api_counter += 1
        return api_name

# ── Subject Worker Thread ──────────────────────────────────────────────────
def subject_worker(subject_name: str, topic_queue: Queue, completed: set, available_apis: list, dry_run: bool):
    """Process all topics for one subject sequentially."""
    worker_id = f"[{subject_name}]"
    logger.info(f"{worker_id} Worker started")

    topic_idx = 0
    subject_stats = {"processed": 0, "success": 0, "partial": 0, "failed": 0}

    while not shutdown_event.is_set():
        try:
            topic_path = topic_queue.get(timeout=1)
            if topic_path is None:  # Poison pill
                topic_queue.task_done()
                break

            topic_idx += 1

            # Get API using global round-robin (distributes evenly across threads)
            api_name = get_next_api(available_apis)

            # Process topic
            result = process_topic(topic_idx, topic_path, api_name, dry_run)

            # Update stats
            subject_stats["processed"] += 1
            if result["success"]:
                subject_stats["success"] += 1
                if not dry_run:
                    with progress_lock:
                        completed.add(topic_path)
                        save_progress(completed)
            elif result["files_written"] >= 3:
                subject_stats["partial"] += 1
            else:
                subject_stats["failed"] += 1

            # Update global stats
            with stats_lock:
                global_stats["topics_processed"] += 1
                if result["success"]:
                    global_stats["topics_success"] += 1
                    global_stats["api_calls_success"] += 2
                elif result["files_written"] >= 3:
                    global_stats["topics_partial"] += 1
                    global_stats["api_calls_success"] += 1
                    global_stats["api_calls_failed"] += 1
                else:
                    global_stats["topics_failed"] += 1
                    global_stats["api_calls_failed"] += 2

                # Track API usage
                if api_name == "nvidia":
                    global_stats["api_calls_nvidia"] += 2
                elif api_name == "chutes":
                    global_stats["api_calls_chutes"] += 2
                elif api_name == "minimax":
                    global_stats["api_calls_minimax"] += 2

            topic_queue.task_done()

        except Exception as e:
            logger.error(f"{worker_id} Worker error: {e}")
            break

    logger.info(f"{worker_id} Worker finished: {subject_stats['processed']} topics, {subject_stats['success']} success")

# ── Main ───────────────────────────────────────────────────────────────────
def main():
    global api_semaphore, nvidia_semaphore

    parser = argparse.ArgumentParser(description="VTU Topic Upgrader - Subject-Parallel with Smart Batching")
    parser.add_argument("paths_file", help="Text file with topic paths")
    parser.add_argument("--threads", type=int, default=DEFAULT_THREADS, help=f"Number of subject threads (default {DEFAULT_THREADS})")
    parser.add_argument("--max-api-calls", type=int, default=MAX_CONCURRENT_API_CALLS, help=f"Max concurrent API calls (default {MAX_CONCURRENT_API_CALLS})")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    parser.add_argument("--nvidia-only", action="store_true", help="Use only NVIDIA API")
    parser.add_argument("--cerebras-only", action="store_true", help="Use only Cerebras API (FASTEST - 0.5s)")
    parser.add_argument("--groq-only", action="store_true", help="Use only Groq API (extremely fast)")
    parser.add_argument("--sambanova-only", action="store_true", help="Use only SambaNova API (20 req/day)")
    parser.add_argument("--fireworks-only", action="store_true", help="Use only Fireworks AI (60 req limit)")
    parser.add_argument("--openrouter-only", action="store_true", help="Use only OpenRouter API (free tier)")
    parser.add_argument("--chutes-only", action="store_true", help="Use only Chutes API")
    parser.add_argument("--minimax-only", action="store_true", help="Use only MiniMax API")
    parser.add_argument("--resume", action="store_true", help="Skip completed topics")
    parser.add_argument("--start-from-topic", type=int, default=1, dest="start_from_topic", help="Start from topic number N (1-based index)")
    parser.add_argument("--log", action="store_true", help="Enable INFO logging")
    parser.add_argument("--debug", action="store_true", help="Enable DEBUG logging")
    args = parser.parse_args()

    # Initialize global API semaphores
    api_semaphore = Semaphore(args.max_api_calls)  # Parallel APIs (Chutes, MiniMax): max 15 concurrent
    nvidia_semaphore = Semaphore(1)  # Sequential APIs (NVIDIA, Groq, OpenRouter): max 1 concurrent

    # Configure logging
    if args.debug:
        logger.setLevel(logging.DEBUG)
    elif args.log:
        logger.setLevel(logging.INFO)

    # Read topic paths
    paths_file = Path(args.paths_file)
    if not paths_file.exists():
        print(f"Error: File not found: {paths_file}")
        sys.exit(1)

    all_topics = []
    with paths_file.open("r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                all_topics.append(line)

    if not all_topics:
        print("Error: No topics found")
        sys.exit(1)

    # Load progress
    completed = load_progress() if args.resume else set()

    # Apply filters: resume + start_from_topic
    topics = all_topics

    # Debug: print start_from_topic value
    start_idx = getattr(args, 'start_from_topic', 1)
    if start_idx != 1:
        print(f"\n[DEBUG] start_from_topic argument = {start_idx}")

    # Filter 1: Resume (skip completed)
    if args.resume:
        topics = [t for t in topics if t not in completed]

    # Filter 2: Start from topic N (1-based index)
    if start_idx > 1:
        skip_count = start_idx - 1
        if skip_count < len(topics):
            topics = topics[skip_count:]
            print(f"\n⏭️  Skipping first {skip_count} topics, starting from topic #{start_idx}\n")
        else:
            print(f"\n⚠️  Warning: --start-from-topic {start_idx} is beyond total topics ({len(topics)})\n")
            topics = []

    if args.resume and completed:
        print(f"\n📁 Resume mode: {len(completed)} completed, {len(topics)} remaining\n")

    # Group topics by subject
    subject_topics = defaultdict(list)
    for topic_path in topics:
        ctx = get_topic_context(topic_path)
        if ctx:
            subject_topics[ctx["subject_dir"]].append(topic_path)

    # Determine APIs
    available_apis = []

    if args.nvidia_only:
        available_apis = ["nvidia"]
    elif getattr(args, 'cerebras_only', False):
        available_apis = ["cerebras"]
    elif getattr(args, 'groq_only', False):
        available_apis = ["groq"]
    elif getattr(args, 'sambanova_only', False):
        available_apis = ["sambanova"]
    elif getattr(args, 'fireworks_only', False):
        available_apis = ["fireworks"]
    elif getattr(args, 'openrouter_only', False):
        available_apis = ["openrouter"]
    elif args.chutes_only:
        available_apis = ["chutes"]
    elif args.minimax_only:
        available_apis = ["minimax"]
    else:
        # Default: Use all 8 APIs (round-robin distribution)
        # Sequential APIs: nvidia, groq, sambanova, fireworks, openrouter (max 1 concurrent each)
        # Parallel APIs: cerebras, chutes, minimax (max 15 concurrent total)
        available_apis = ["nvidia", "cerebras", "groq", "sambanova", "fireworks", "openrouter", "chutes", "minimax"]

    if not available_apis:
        print("Error: No APIs selected")
        sys.exit(1)

    # NVIDIA API key is now hardcoded, no need to validate

    num_subjects = len(subject_topics)
    num_threads = min(args.threads, num_subjects)

    # Print header
    print(f"\n{'='*100}")
    print("  VTU TOPIC UPGRADER - SUBJECT-PARALLEL WITH SMART BATCHING")
    print(f"{'='*100}")
    print(f"  Source file        : {paths_file.name}")

    # Show topic count info
    start_idx = getattr(args, 'start_from_topic', 1)
    if args.resume and completed:
        total_str = f"{len(all_topics)} total ({len(completed)} completed, {len(topics)} remaining)"
    elif start_idx > 1:
        skipped = start_idx - 1
        total_str = f"{len(all_topics)} total (skipped {skipped}, processing {len(topics)})"
    else:
        total_str = str(len(topics))

    print(f"  Total topics       : {total_str}")
    print(f"  Subjects           : {num_subjects}")
    print(f"  Worker threads     : {num_threads}")
    print(f"  Max concurrent APIs: {args.max_api_calls}")
    print(f"  API call delay     : {API_CALL_DELAY}s between calls")
    print(f"  APIs               : {', '.join(api.upper() for api in available_apis)}")
    print(f"  API calls/topic    : 2 (batched: markdown + assessment)")
    print(f"  Timeout            : {REQUEST_TIMEOUT}s with {HEARTBEAT_INTERVAL}s heartbeat")

    # Mode string
    mode_parts = []
    start_idx = getattr(args, 'start_from_topic', 1)
    if args.dry_run:
        mode_parts.append('DRY RUN')
    else:
        mode_parts.append('LIVE')
    if args.resume:
        mode_parts.append('RESUME')
    if start_idx > 1:
        mode_parts.append(f'START FROM #{start_idx}')

    print(f"  Mode               : {' + '.join(mode_parts)}")
    print(f"{'='*100}\n")

    # Create queues for each subject
    subject_queues = {}
    for subject_name, topic_list in subject_topics.items():
        q = Queue()
        for topic_path in topic_list:
            q.put(topic_path)
        q.put(None)  # Poison pill
        subject_queues[subject_name] = q
        print(f"  📚 {subject_name}: {len(topic_list)} topics")

    print(f"\n{'─'*100}")
    print("  STARTING WORKERS...")
    print(f"{'─'*100}\n")

    start_time = time.time()

    # Start worker threads
    workers = []
    for subject_name, queue in subject_queues.items():
        worker = Thread(
            target=subject_worker,
            args=(subject_name, queue, completed, available_apis, args.dry_run),
            daemon=True
        )
        worker.start()
        workers.append(worker)

    # Wait for all workers
    try:
        for worker in workers:
            worker.join()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupt received. Stopping workers...")
        shutdown_event.set()
        for q in subject_queues.values():
            try:
                q.put_nowait(None)
            except Exception:
                pass
        for worker in workers:
            worker.join(timeout=2)
        print("⚠️  Exiting early due to user interrupt.")
        return

    total_elapsed = time.time() - start_time

    # Final summary
    print(f"\n{'='*100}")
    print(f"  COMPLETED IN {total_elapsed/60:.1f} MINUTES")
    print(f"{'='*100}")
    print(f"  Topics processed : {global_stats['topics_processed']}")
    print(f"  Success          : {global_stats['topics_success']} ({global_stats['topics_success']*100//max(1,global_stats['topics_processed'])}%)")
    print(f"  Partial success  : {global_stats['topics_partial']}")
    print(f"  Failed           : {global_stats['topics_failed']}")
    print(f"  API calls        : {global_stats['api_calls_success']} success, {global_stats['api_calls_failed']} failed")
    print(f"  API distribution : NVIDIA={global_stats['api_calls_nvidia']}, Chutes={global_stats['api_calls_chutes']}, MiniMax={global_stats['api_calls_minimax']}")
    print(f"  Speed            : {global_stats['topics_processed']/max(1,total_elapsed):.2f} topics/sec")
    print(f"{'='*100}\n")

    if not args.dry_run and completed:
        print(f"📁 Progress saved to {PROGRESS_FILE}")
        print(f"   To resume: python3 {sys.argv[0]} {args.paths_file} --resume\n")

if __name__ == "__main__":
    main()
