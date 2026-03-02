#!/usr/bin/env python3
"""
VTU 2022 Scheme Hybrid Content Generator

Features:
- Local LM Studio for text content (read.md, full.md, summary.md, purpose.md)
- NVIDIA API for structured content (mcqs, flashcards, visual, questions, memory)
- Parallel execution with proper synchronization
- Auto-commit after every topic
- Backfill summary.md during NVIDIA rate limit waits
- Resource-efficient (8GB RAM limit for local model)

Usage:
    python3 generate_hybrid.py
"""

import os
import sys
import json
import re
import subprocess
import shutil
import urllib.request
import urllib.error
import time
import threading
from pathlib import Path
from difflib import SequenceMatcher
from concurrent.futures import ThreadPoolExecutor, as_completed, wait
from queue import Queue
import argparse

# Unbuffered output
sys.stdout = sys.stderr = open(sys.stdout.fileno(), mode='w', buffering=1)

def log(msg):
    """Print with flush for real-time logging"""
    print(msg, flush=True)

# ============== CONFIGURATION ==============
# NVIDIA API
NVIDIA_API_KEY_FILE = "/Users/ggoudar/Documents/GitHub/smalltools/vtu_engg_model_answers/vtu_syllabus/2022_Scheme/api_key.txt"
with open(NVIDIA_API_KEY_FILE, 'r') as f:
    NVIDIA_API_KEY = f.read().strip()

NVIDIA_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
# Smaller models first (better rate limits), then larger fallbacks
NVIDIA_MODEL = "meta/llama-3.2-3b-instruct"  # 3B - best rate limits
NVIDIA_FALLBACK_MODELS = [
    "google/gemma-2-9b-it",                   # 9B - good rate limits
    "microsoft/phi-3-mini-4k-instruct",       # Small - good rate limits
    "meta/llama-3.1-8b-instruct",             # 8B - decent rate limits
    "google/gemma-2-27b-it",                  # 27B - fallback
    "meta/llama-3.3-70b-instruct",            # 70B - last resort
]

# Local LM Studio API
LOCAL_API_URL = "http://localhost:1234/v1/chat/completions"
LOCAL_MODEL = "qwen2.5-3b-instruct"  # Best for educational prose content

# Paths
VTU_SYLLABUS_DIR = "/Users/ggoudar/Documents/GitHub/smalltools/vtu_engg_model_answers/vtu_syllabus/2022_Scheme"
GENERIC_CONTENT_DIR = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/cs_generic_content"
VTU_OUTPUT_DIR = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme"

FUZZY_MATCH_THRESHOLD = 0.65

# Branch mappings
BRANCH_FOLDERS = {
    "Computer_Science_Engineering": "cse",
    "Information_Science_Engineering": "ise",
    "AI_Machine_Learning": "ai-ml",
    "Artificial_Intelligence_Data_Science": "aids",
}

# Statistics
stats = {
    "subjects_processed": 0,
    "topics_copied": 0,
    "topics_generated": 0,
    "topics_failed": 0,
    "local_calls": 0,
    "nvidia_calls": 0,
    "model_usage": {},  # Track which models are used
}
stats_lock = threading.Lock()

# Queue for backfill tasks (summary.md for existing topics)
backfill_queue = Queue()

# ============== API FUNCTIONS ==============
def get_local_model():
    """Auto-detect loaded model in LM Studio"""
    try:
        req = urllib.request.Request(
            "http://localhost:1234/v1/models",
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            models = data.get('data', [])
            if models:
                # Return first available model
                return models[0]['id']
    except:
        pass
    return LOCAL_MODEL

def call_local_api(messages, max_retries=3):
    """Call local LM Studio API"""
    model = get_local_model()

    for attempt in range(max_retries):
        try:
            data = json.dumps({
                "model": model,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 4096
            }).encode('utf-8')

            req = urllib.request.Request(
                LOCAL_API_URL,
                data=data,
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=120) as response:
                result = json.loads(response.read().decode('utf-8'))
                with stats_lock:
                    stats["local_calls"] += 1
                return result['choices'][0]['message']['content']
        except urllib.error.HTTPError as e:
            log(f"      Local API Error {e.code} (attempt {attempt+1})")
            time.sleep(2)
        except urllib.error.URLError as e:
            log(f"      Local API URL Error: {e.reason} (attempt {attempt+1})")
            time.sleep(2)
        except Exception as e:
            log(f"      Local API Error: {e} (attempt {attempt+1})")
            time.sleep(2)

    return None

def call_nvidia_api(messages, max_retries=3):
    """Call NVIDIA API with fast retries and model logging"""
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }

    models_to_try = [NVIDIA_MODEL] + NVIDIA_FALLBACK_MODELS
    model_index = 0

    for attempt in range(max_retries * len(models_to_try)):
        current_model = models_to_try[model_index]
        try:
            data = json.dumps({
                "model": current_model,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 4096
            }).encode('utf-8')

            req = urllib.request.Request(NVIDIA_API_URL, data=data, headers=headers)
            with urllib.request.urlopen(req, timeout=120) as response:
                result = json.loads(response.read().decode('utf-8'))
                with stats_lock:
                    stats["nvidia_calls"] += 1
                    # Track model usage
                    model_name = current_model.split('/')[-1]
                    stats["model_usage"][model_name] = stats["model_usage"].get(model_name, 0) + 1
                return result['choices'][0]['message']['content']
        except urllib.error.HTTPError as e:
            if e.code == 429:
                model_index = (model_index + 1) % len(models_to_try)
                time.sleep(2)
            elif e.code in [400, 404, 503]:
                model_index = (model_index + 1) % len(models_to_try)
                time.sleep(1)
            else:
                time.sleep(2)
        except Exception as e:
            time.sleep(2)

    return None

def process_backfill_queue(wait_seconds):
    """Process backfill queue during wait times"""
    start = time.time()
    while time.time() - start < wait_seconds - 5:  # Leave 5s buffer
        if backfill_queue.empty():
            time.sleep(1)
            continue

        try:
            topic_path, topic_title, context = backfill_queue.get_nowait()
            summary_path = os.path.join(topic_path, "summary.md")

            if not os.path.exists(summary_path):
                log(f"      [Backfill] Generating summary for {topic_title[:30]}...")
                prompt = generate_summary_prompt(topic_title, context)
                response = call_local_api([{"role": "user", "content": prompt}])
                if response:
                    with open(summary_path, 'w') as f:
                        f.write(response)
        except:
            pass

# ============== PROMPT GENERATORS ==============
def generate_read_prompt(topic_title, context):
    return f"""Write comprehensive study material for the topic "{topic_title}".

{context}

Requirements:
- Write 2-3 pages of educational content
- Use clear headings and subheadings
- Include definitions, explanations, and examples
- Use bullet points for key concepts
- Format in Markdown

Write the complete study material:"""

def generate_full_prompt(topic_title, context):
    return f"""Write a detailed, comprehensive deep-dive on the topic "{topic_title}".

{context}

Requirements:
- Write 5+ pages of in-depth educational content
- Cover all aspects thoroughly with detailed explanations
- Include multiple examples, case studies, and applications
- Discuss historical context and modern developments
- Include diagrams descriptions where helpful
- Add "Further Reading" suggestions at the end
- Format in Markdown with clear structure

Write the complete detailed content:"""

def generate_summary_prompt(topic_title, context):
    return f"""Write a concise summary/revision notes for the topic "{topic_title}".

{context}

Requirements:
- Maximum 1 page
- Key points only in bullet format
- Include important formulas, definitions, theorems
- Perfect for quick revision before exams
- Format in Markdown

Write the summary:"""

def generate_purpose_prompt(topic_title, context):
    return f"""Explain the purpose and importance of learning "{topic_title}".

{context}

Write 3-4 sentences explaining:
1. Why this topic matters
2. Real-world applications
3. How it connects to other concepts"""

def generate_mcqs_prompt(topic_title, context):
    return f"""Create 5 multiple choice questions for the topic "{topic_title}".

{context}

Return ONLY valid JSON in this exact format:
{{
  "questions": [
    {{
      "question": "Question text here?",
      "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
      "correct": 0,
      "explanation": "Brief explanation"
    }}
  ]
}}"""

def generate_flashcards_prompt(topic_title, context):
    return f"""Create 5 flashcards for the topic "{topic_title}".

{context}

Return ONLY valid JSON in this exact format:
{{
  "cards": [
    {{
      "front": "Question or term",
      "back": "Answer or definition"
    }}
  ]
}}"""

def generate_questions_prompt(topic_title, context):
    return f"""Create 3 exam-style questions for the topic "{topic_title}".

{context}

Return ONLY valid JSON in this exact format:
{{
  "questions": [
    {{
      "question": "Question text",
      "type": "short_answer",
      "marks": 5,
      "hint": "Optional hint"
    }}
  ]
}}"""

def generate_memory_prompt(topic_title, context):
    return f"""Create memory aids for the topic "{topic_title}".

{context}

Return ONLY valid JSON in this exact format:
{{
  "mnemonics": ["Mnemonic 1", "Mnemonic 2"],
  "keyPoints": ["Key point 1", "Key point 2", "Key point 3"]
}}"""

def generate_visual_prompt(topic_title, context):
    return f"""Create an SVG diagram description for the topic "{topic_title}".

{context}

Return ONLY valid JSON in this exact format:
{{
  "title": "{topic_title}",
  "type": "flowchart",
  "elements": ["Element 1", "Element 2", "Element 3"],
  "connections": ["Element 1 -> Element 2", "Element 2 -> Element 3"]
}}"""

# ============== CONTENT GENERATION ==============
def generate_topic_content_hybrid(topic_title, subject_name, module_title, dest_path):
    """Generate ALL content using NVIDIA API in parallel for maximum speed"""
    os.makedirs(dest_path, exist_ok=True)

    context = f"Subject: {subject_name}\nModule: {module_title}\nTopic: {topic_title}"

    # ALL content via NVIDIA - parallel execution
    all_content = [
        ("read.md", generate_read_prompt, False),
        ("full.md", generate_full_prompt, False),
        ("summary.md", generate_summary_prompt, False),
        ("purpose.md", generate_purpose_prompt, False),
        ("mcqs.json", generate_mcqs_prompt, True),
        ("flashcards.json", generate_flashcards_prompt, True),
        ("questions.json", generate_questions_prompt, True),
        ("memory.json", generate_memory_prompt, True),
        ("visual.json", generate_visual_prompt, True),
    ]

    generated_count = 0
    futures = []

    # Run ALL API calls in parallel (max 9 concurrent)
    with ThreadPoolExecutor(max_workers=9) as executor:
        for filename, prompt_func, is_json in all_content:
            filepath = os.path.join(dest_path, filename)
            if os.path.exists(filepath):
                generated_count += 1
                continue

            def api_task(fn, pf, fp, is_j, ctx=context, tt=topic_title):
                prompt = pf(tt, ctx)
                response = call_nvidia_api([{"role": "user", "content": prompt}])
                return (fn, fp, response, is_j)

            future = executor.submit(api_task, filename, prompt_func, filepath, is_json)
            futures.append(future)

        # Collect results
        for future in as_completed(futures):
            try:
                filename, filepath, response, is_json = future.result()
                if response:
                    if is_json:
                        content = extract_json_content(response, filename)
                        with open(filepath, 'w') as f:
                            json.dump(content, f, indent=2)
                    else:
                        with open(filepath, 'w') as f:
                            f.write(response)
                    generated_count += 1
                else:
                    # Create placeholder for failed content
                    if is_json:
                        with open(filepath, 'w') as f:
                            json.dump({"topic": topic_title, "status": "pending"}, f, indent=2)
            except Exception as e:
                log(f"      Error: {filename} - {e}")

    return generated_count >= 5

def extract_json_content(response, filename):
    """Extract JSON from API response"""
    try:
        # Try to find JSON in response
        json_match = re.search(r'\{[\s\S]*\}', response)
        if json_match:
            return json.loads(json_match.group())
    except:
        pass
    return {"topic": filename.replace('.json', ''), "content": response[:500]}

# ============== GIT FUNCTIONS ==============
def commit_and_push_topic(topic_title, subject_code):
    """Git commit and push after each topic"""
    original_dir = os.getcwd()
    try:
        os.chdir(VTU_OUTPUT_DIR)

        # Add all changes
        subprocess.run(['git', 'add', '-A'], check=True, capture_output=True, timeout=30)

        # Check if there are changes
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True, timeout=30)
        if not result.stdout.strip():
            return

        # Commit
        commit_msg = f"Add: {subject_code} - {topic_title[:50]}"
        subprocess.run(['git', 'commit', '-m', commit_msg], check=True, capture_output=True, timeout=60)

        # Push (async, don't wait)
        subprocess.Popen(['git', 'push'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    except Exception as e:
        pass  # Don't block on git errors
    finally:
        os.chdir(original_dir)

# ============== HELPER FUNCTIONS ==============
def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:50].rstrip('-')

def extract_pdf_text(pdf_path):
    """Extract text from PDF"""
    result = subprocess.run(
        ['pdftotext', '-layout', pdf_path, '-'],
        capture_output=True, text=True
    )
    return result.stdout

def find_matching_topic(vtu_topic, generic_index):
    """Find matching topic in generic content using fuzzy matching"""
    vtu_clean = vtu_topic.lower().strip()

    best_match = None
    best_score = 0

    for topic in generic_index:
        generic_title = topic.get("title", "").lower().strip()
        score = SequenceMatcher(None, vtu_clean, generic_title).ratio()

        if score > best_score and score >= FUZZY_MATCH_THRESHOLD:
            best_score = score
            best_match = topic

    return best_match

def copy_topic_content(src_path, dest_path):
    """Copy topic content from generic to VTU"""
    os.makedirs(dest_path, exist_ok=True)

    files_to_copy = ['read.md', 'mcqs.json', 'flashcards.json', 'visual.json',
                     'purpose.md', 'questions.json', 'memory.json']

    for filename in files_to_copy:
        src_file = os.path.join(src_path, filename)
        dest_file = os.path.join(dest_path, filename)
        if os.path.exists(src_file):
            shutil.copy2(src_file, dest_file)

    # Add to backfill queue for full.md and summary.md
    backfill_queue.put((dest_path, os.path.basename(dest_path), ""))

def build_generic_topic_index(generic_dir):
    """Build index of all generic topics

    Structure: generic_dir/domain/subject/chapters/chapter/topics/topic/
    """
    index = []

    for domain in os.listdir(generic_dir):
        domain_path = os.path.join(generic_dir, domain)
        if not os.path.isdir(domain_path) or domain.startswith('.'):
            continue

        # Domain contains subjects (e.g., computer-science/operating-systems)
        for subject in os.listdir(domain_path):
            subject_path = os.path.join(domain_path, subject)
            if not os.path.isdir(subject_path) or subject.startswith('.'):
                continue

            chapters_dir = os.path.join(subject_path, "chapters")
            if not os.path.exists(chapters_dir):
                continue

            for chapter in os.listdir(chapters_dir):
                chapter_path = os.path.join(chapters_dir, chapter)
                if not os.path.isdir(chapter_path) or chapter.startswith('.') or chapter.startswith('_'):
                    continue

                topics_dir = os.path.join(chapter_path, "topics")
                if not os.path.exists(topics_dir):
                    continue

                for topic in os.listdir(topics_dir):
                    topic_path = os.path.join(topics_dir, topic)
                    if os.path.isdir(topic_path) and not topic.startswith('.'):
                        # Build multiple title variants for better matching
                        title = topic.replace('-', ' ').title()
                        index.append({
                            "title": title,
                            "slug": topic,
                            "path": topic_path,
                            "domain": domain,
                            "subject": subject,
                            "chapter": chapter
                        })

    log(f"Built generic index with {len(index)} topics")
    return index

# ============== SYLLABUS PARSING ==============
def parse_syllabus(pdf_path):
    """Parse VTU syllabus PDF to extract subjects and topics"""
    text = extract_pdf_text(pdf_path)
    subjects = []

    # VTU 2022 format: Subject name is on the same line as "Semester" but before it
    # Example: "Mathematics for Computer Science                           Semester          3"
    # Then:   "Course Code                                        BCS301"

    # Pattern to find subject blocks
    code_pattern = r'Course Code\s+([A-Z]{2,4}\d{2,3}[A-Z]?)'

    # Find all course codes and their positions
    code_matches = list(re.finditer(code_pattern, text))

    for i, code_match in enumerate(code_matches):
        code = code_match.group(1).strip()

        # Look backwards from code position to find subject name
        # Subject name is on the line containing "Semester" (before the word Semester)
        search_start = max(0, code_match.start() - 500)
        before_text = text[search_start:code_match.start()]

        subject_name = None
        lines = before_text.strip().split('\n')

        for line in reversed(lines):
            # Look for line containing "Semester" - subject name is at the start
            if 'Semester' in line:
                # Extract text before "Semester"
                parts = line.split('Semester')
                if parts[0].strip():
                    subject_name = re.sub(r'\s+', ' ', parts[0]).strip()
                    # Clean trailing numbers, dates, etc.
                    subject_name = re.sub(r'\s*\d+$', '', subject_name).strip()
                    break

        if not subject_name or len(subject_name) < 5:
            # Fallback: try looking for standalone subject name line
            for line in reversed(lines):
                line = line.strip()
                if (line and len(line) > 10 and len(line) < 80 and
                    not line.startswith('Annexure') and
                    not any(x in line for x in ['Course Code', 'CIE', 'SEE', 'Credits', 'Hours', 'http']) and
                    not line[0].isdigit()):
                    subject_name = re.sub(r'\s+', ' ', line).strip()
                    break

        if not subject_name:
            continue

        # Skip labs
        if 'LAB' in subject_name.upper() or 'LABORATORY' in subject_name.upper():
            continue

        # Find end of this subject section (start of next subject or end of text)
        if i + 1 < len(code_matches):
            section_end = code_matches[i + 1].start()
        else:
            section_end = len(text)

        subject_text = text[code_match.start():section_end]

        # Extract modules
        modules = extract_modules(subject_text)

        if modules:
            subjects.append({
                "code": code,
                "name": subject_name,
                "modules": modules
            })
            log(f"  Found subject: {code} - {subject_name[:50]}... ({len(modules)} modules)")

    return subjects

def extract_modules(subject_text):
    """Extract modules and topics from subject section"""
    modules = []

    # Pattern for module headers: "Module-1: Title" or "Module 1: Title"
    module_pattern = r'Module[- ]*(\d+)[:\s]*([^\n]*)'

    module_matches = list(re.finditer(module_pattern, subject_text, re.IGNORECASE))

    for i, match in enumerate(module_matches):
        module_num = match.group(1)
        module_title = match.group(2).strip()

        # Clean up module title (remove trailing punctuation)
        module_title = re.sub(r'[:\s]+$', '', module_title)
        if not module_title:
            module_title = f"Module {module_num}"

        # Get content until next module or end
        content_start = match.end()
        if i + 1 < len(module_matches):
            content_end = module_matches[i + 1].start()
        else:
            # Stop at common endings
            end_markers = ['Course outcome', 'Assessment Details', 'Suggested Learning', 'Textbooks:']
            content_end = len(subject_text)
            for marker in end_markers:
                marker_pos = subject_text.find(marker, content_start)
                if marker_pos != -1 and marker_pos < content_end:
                    content_end = marker_pos

        module_content = subject_text[content_start:content_end]

        # Extract topics from module content
        # VTU format: topics are mentioned in prose, separated by commas, periods, or colons
        # Clean the content
        module_content = re.sub(r'\([^)]*Hours?\)', '', module_content)  # Remove (12 Hours)
        module_content = re.sub(r'\(RBT Levels[^)]*\)', '', module_content)  # Remove RBT levels
        module_content = re.sub(r'Pedagogy[^\n]*', '', module_content)  # Remove pedagogy lines
        module_content = re.sub(r'\s+', ' ', module_content).strip()

        # Split into potential topics
        # First split by major separators
        parts = re.split(r'[.;]\s+', module_content)

        topics = []
        for part in parts:
            part = part.strip()
            if len(part) < 5 or len(part) > 200:
                continue
            # Further split by commas for compound topics
            sub_parts = [p.strip() for p in part.split(',') if len(p.strip()) > 5]
            if len(sub_parts) <= 3:
                topics.extend(sub_parts)
            else:
                # Too many commas, keep as single topic
                topics.append(part[:150])

        # Clean up topics
        clean_topics = []
        for topic in topics:
            topic = topic.strip()
            # Skip if too short, too long, or looks like garbage
            if len(topic) < 5 or len(topic) > 150:
                continue
            # Skip common non-topic text
            skip_words = ['introduction to', 'problems', 'illustrative examples', 'applications',
                         'derivations for', 'problems on', 'numerical problems']
            if any(topic.lower() == skip for skip in skip_words):
                continue
            # Capitalize properly
            topic = topic[0].upper() + topic[1:] if topic else topic
            clean_topics.append(topic)

        # Limit topics per module
        clean_topics = clean_topics[:12]

        if clean_topics:
            modules.append({
                "number": module_num,
                "title": module_title,
                "topics": clean_topics
            })

    return modules

# ============== MAIN PROCESSING ==============
def process_subject(subject, branch_id, semester, generic_index):
    """Process a single subject"""
    subject_id = slugify(f"{subject['code']}-{subject['name']}")
    subject_dir = os.path.join(VTU_OUTPUT_DIR, branch_id, f"sem-{semester}", subject_id)

    log(f"\n{'='*60}")
    log(f"Processing: {subject['code']} - {subject['name']}")
    log(f"{'='*60}")

    os.makedirs(subject_dir, exist_ok=True)

    # Create subject metadata
    meta = {
        "code": subject["code"],
        "name": subject["name"],
        "semester": semester,
        "branch": branch_id
    }
    with open(os.path.join(subject_dir, "_meta.json"), 'w') as f:
        json.dump(meta, f, indent=2)

    chapters_dir = os.path.join(subject_dir, "chapters")
    os.makedirs(chapters_dir, exist_ok=True)

    chapters_index = []

    for module in subject.get("modules", []):
        module_num = module["number"]
        module_title = module["title"]
        module_id = f"module-{module_num}"

        log(f"\n  Module: {module_title}")

        chapter_dir = os.path.join(chapters_dir, module_id)
        topics_dir = os.path.join(chapter_dir, "topics")
        os.makedirs(topics_dir, exist_ok=True)

        topics_info = []

        for idx, topic_title in enumerate(module.get("topics", []), 1):
            topic_id = slugify(topic_title)
            if not topic_id:
                continue

            topic_path = os.path.join(topics_dir, topic_id)

            # Check if already exists
            read_file = os.path.join(topic_path, "read.md")
            if os.path.exists(read_file):
                log(f"    ⏭ SKIP: {topic_title[:50]}... (exists)")
                topics_info.append({
                    "id": topic_id,
                    "title": topic_title,
                    "order": idx
                })
                # Add to backfill queue for new content types
                backfill_queue.put((topic_path, topic_title, f"Subject: {subject['name']}\nModule: {module_title}"))
                continue

            # Check for generic match
            match = find_matching_topic(topic_title, generic_index)

            if match:
                log(f"    ✓ COPY: {topic_title[:40]}... <- {match['title'][:30]}...")
                copy_topic_content(match["path"], topic_path)
                with stats_lock:
                    stats["topics_copied"] += 1
            else:
                log(f"    ○ GENERATE: {topic_title[:50]}...")
                try:
                    generate_topic_content_hybrid(
                        topic_title,
                        subject["name"],
                        module_title,
                        topic_path
                    )
                    with stats_lock:
                        stats["topics_generated"] += 1
                except Exception as e:
                    log(f"      ERROR: {e}")
                    with stats_lock:
                        stats["topics_failed"] += 1

            topics_info.append({
                "id": topic_id,
                "title": topic_title,
                "order": idx
            })

            # Commit after each topic
            commit_and_push_topic(topic_title, subject["code"])

        # Create chapter index
        chapter_index = {
            "chapterId": module_id,
            "chapterTitle": module_title,
            "topics": topics_info
        }
        with open(os.path.join(chapter_dir, "_index.json"), 'w') as f:
            json.dump(chapter_index, f, indent=2)

        chapters_index.append({
            "id": module_id,
            "title": module_title,
            "order": int(module_num),
            "topicCount": len(topics_info)
        })

    # Create chapters index
    with open(os.path.join(chapters_dir, "_index.json"), 'w') as f:
        json.dump({"chapters": chapters_index}, f, indent=2)

    with stats_lock:
        stats["subjects_processed"] += 1

    return subject_dir

def process_branch(branch_name, branch_id, generic_index):
    """Process all PDFs for a branch"""
    branch_path = os.path.join(VTU_SYLLABUS_DIR, branch_name)

    if not os.path.exists(branch_path):
        log(f"Branch path not found: {branch_path}")
        return

    pdf_files = sorted([f for f in os.listdir(branch_path) if f.endswith('.pdf')])

    for pdf_file in pdf_files:
        pdf_path = os.path.join(branch_path, pdf_file)

        # Handle various naming: Sem_3-4_Syllabus.pdf, Sem_5_Syllabus.pdf, etc.
        sem_match = re.search(r'Sem_(\d+)(?:-(\d+))?', pdf_file)
        if not sem_match:
            continue

        # For combined PDFs (Sem_3-4), we'll parse all and assign semester from subject code
        start_sem = int(sem_match.group(1))
        end_sem = int(sem_match.group(2)) if sem_match.group(2) else start_sem

        log(f"\n\n{'#'*70}")
        log(f"# Processing: {branch_name} - Semesters {start_sem}-{end_sem}")
        log(f"# PDF: {pdf_file}")
        log(f"{'#'*70}")

        subjects = parse_syllabus(pdf_path)
        log(f"Found {len(subjects)} theory subjects")

        for subject in subjects:
            # Try to detect semester from course code (e.g., BCS301 = Sem 3)
            code = subject.get('code', '')
            if len(code) >= 4:
                try:
                    # BCS301 -> 3, BCS501 -> 5
                    sem_digit = int(code[3])
                    semester = sem_digit
                except:
                    semester = start_sem
            else:
                semester = start_sem

            process_subject(subject, branch_id, semester, generic_index)

def main():
    """Main entry point"""
    log("="*70)
    log("VTU 2022 SCHEME HYBRID CONTENT GENERATOR")
    log("="*70)
    log(f"Local API: {LOCAL_API_URL}")
    log(f"NVIDIA API: {NVIDIA_API_URL}")
    log("="*70)

    # Test local API
    log("\nTesting local LM Studio API...")
    test_response = call_local_api([{"role": "user", "content": "Say 'ready' in one word"}])
    if test_response:
        log(f"  ✓ Local API ready: {test_response[:50]}")
    else:
        log("  ✗ Local API not responding. Please load a model in LM Studio.")
        log("  Continuing with NVIDIA API only...")

    # Build generic topic index
    log("\nBuilding generic content index...")
    generic_index = build_generic_topic_index(GENERIC_CONTENT_DIR)

    # Process branches
    for branch_name, branch_id in BRANCH_FOLDERS.items():
        process_branch(branch_name, branch_id, generic_index)

    # Final stats
    log("\n" + "="*70)
    log("GENERATION COMPLETE")
    log("="*70)
    log(f"Subjects processed: {stats['subjects_processed']}")
    log(f"Topics copied: {stats['topics_copied']}")
    log(f"Topics generated: {stats['topics_generated']}")
    log(f"Topics failed: {stats['topics_failed']}")
    log(f"Local API calls: {stats['local_calls']}")
    log(f"NVIDIA API calls: {stats['nvidia_calls']}")
    log("\nModel Usage:")
    for model, count in sorted(stats['model_usage'].items(), key=lambda x: -x[1]):
        log(f"  {model}: {count} calls")

if __name__ == "__main__":
    main()
