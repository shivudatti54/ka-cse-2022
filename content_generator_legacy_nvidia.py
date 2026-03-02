#!/usr/bin/env python3
"""
VTU 2022 Scheme Content Generator

Features:
- Parse VTU syllabi PDFs
- Match with generic content using fuzzy matching
- Copy matched content or generate new via NVIDIA API
- Commit and push after each subject

Usage:
    python3 generate_vtu_content.py [--branch CSE] [--semester 3]
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
from pathlib import Path
from difflib import SequenceMatcher
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import argparse

# Unbuffered output
sys.stdout = sys.stderr = open(sys.stdout.fileno(), mode='w', buffering=1)

def log(msg):
    """Print with flush for real-time logging"""
    print(msg, flush=True)

# ============== CONFIGURATION ==============
API_KEY_FILE = "/Users/ggoudar/Documents/GitHub/smalltools/vtu_engg_model_answers/vtu_syllabus/2022_Scheme/api_key.txt"
with open(API_KEY_FILE, 'r') as f:
    API_KEY = f.read().strip()

API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODEL = "deepseek-ai/deepseek-v3.1"
FALLBACK_MODELS = [
    "meta/llama-3.3-70b-instruct",
    "nvidia/llama-3.1-nemotron-70b-instruct",
    "mistralai/mistral-large-2-instruct",
    "google/gemma-2-27b-it",
    "meta/llama-3.1-70b-instruct",
]

VTU_SYLLABUS_DIR = "/Users/ggoudar/Documents/GitHub/smalltools/vtu_engg_model_answers/vtu_syllabus/2022_Scheme"
GENERIC_CONTENT_DIR = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/cs_generic_content"
VTU_OUTPUT_DIR = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme"

MAX_WORKERS = 1  # Sequential processing to avoid rate limits
FUZZY_MATCH_THRESHOLD = 0.65

# Branch mappings
BRANCH_FOLDERS = {
    "Computer_Science_Engineering": "cse",
    "Information_Science_Engineering": "ise",
    "AI_Machine_Learning": "ai-ml",
    "Artificial_Intelligence_Data_Science": "aids",
    "CSE_Specializations/AI": "cse-spec/ai",
    "CSE_Specializations/AI_ML": "cse-spec/ai-ml",
    "CSE_Specializations/Business_Systems": "cse-spec/business-systems",
    "CSE_Specializations/Communication_Engineering": "cse-spec/comm-eng",
    "CSE_Specializations/Data_Science": "cse-spec/data-science",
    "CSE_Specializations/Design": "cse-spec/design",
    "CSE_Specializations/IoT": "cse-spec/iot",
    "CSE_Specializations/IoT_Cyber_Security": "cse-spec/iot-cyber-security",
}

# Statistics tracking
stats = {
    "subjects_processed": 0,
    "topics_copied": 0,
    "topics_generated": 0,
    "topics_failed": 0,
    "mapping_table": []
}
stats_lock = Lock()

# ============== PDF PARSING ==============
def extract_pdf_text(pdf_path):
    """Extract text from PDF using pdftotext"""
    result = subprocess.run(
        ['pdftotext', '-layout', pdf_path, '-'],
        capture_output=True, text=True
    )
    return result.stdout

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:50].rstrip('-')

def parse_syllabus(pdf_path):
    """Parse VTU syllabus PDF to extract subjects and modules"""
    text = extract_pdf_text(pdf_path)
    subjects = []

    lines = text.split('\n')

    current_subject = None
    current_module = None
    module_content_lines = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Check for subject name (usually before Course Code line)
        if i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            code_match = re.search(r'Course Code\s+(B[A-Z]{2,3}[0-9]{3}[A-Z]?)', next_line)
            if code_match and line and not line.startswith('Course Code'):
                subject_name = re.sub(r'\s+Semester\s+\d+', '', line).strip()
                subject_name = re.sub(r'\s+\d+\s*$', '', subject_name).strip()
                if subject_name and len(subject_name) > 3:
                    # Save previous module and subject
                    if current_module and module_content_lines:
                        current_module["topics"] = extract_topics_from_content(module_content_lines)
                    if current_subject and current_module:
                        current_subject["modules"].append(current_module)
                    if current_subject:
                        subjects.append(current_subject)

                    current_subject = {
                        "code": code_match.group(1),
                        "name": subject_name,
                        "modules": []
                    }
                    current_module = None
                    module_content_lines = []
                    i += 1
                    continue

        # Check for MODULE-N pattern
        module_match = re.search(r'MODULE[-\s]*(\d+)[:\s]*([^\n]*)', line, re.IGNORECASE)
        if module_match and current_subject:
            # Save previous module
            if current_module and module_content_lines:
                current_module["topics"] = extract_topics_from_content(module_content_lines)
                current_subject["modules"].append(current_module)

            module_num = module_match.group(1)
            module_title = module_match.group(2).strip()
            module_title = re.sub(r'\d+\s*Hr(s)?.*$', '', module_title, flags=re.IGNORECASE).strip()
            module_title = re.sub(r'No\.\s*of\s*Hours.*$', '', module_title, flags=re.IGNORECASE).strip()

            current_module = {
                "id": f"module-{module_num}",
                "title": f"Module {module_num}" + (f": {module_title}" if module_title else ""),
                "topics": []
            }
            module_content_lines = []
            i += 1
            continue

        # Collect module content
        if current_module:
            if re.search(r'(RBT Levels|Pedagogy|Text\s*book|Course outcome|Assessment|PRACTICAL|Sl\.N)', line, re.IGNORECASE):
                pass  # Skip these lines
            elif line and len(line) > 3:
                module_content_lines.append(line)

        i += 1

    # Save last module and subject
    if current_module and module_content_lines:
        current_module["topics"] = extract_topics_from_content(module_content_lines)
    if current_subject and current_module:
        current_subject["modules"].append(current_module)
    if current_subject:
        subjects.append(current_subject)

    # Filter out lab courses
    subjects = [s for s in subjects if s["modules"] and 'Lab' not in s["name"] and 'LAB' not in s["code"]]

    return subjects


def extract_topics_from_content(lines):
    """Extract meaningful topics from module content lines"""
    # Join all lines into one text block
    full_text = ' '.join(lines)

    # Clean up
    full_text = re.sub(r'\(\d+\s*Hours?\)', '', full_text, flags=re.IGNORECASE)
    full_text = re.sub(r'\d+\s*Hr(s)?', '', full_text, flags=re.IGNORECASE)
    full_text = re.sub(r'Annexure-[IVX]+\s*\d*', '', full_text, flags=re.IGNORECASE)
    full_text = re.sub(r'\s+', ' ', full_text).strip()

    topics = []

    # Strategy 1: Extract "Topic: subtopic1, subtopic2" patterns
    # E.g., "Process Management: Process concept, Process scheduling"
    section_pattern = r'([A-Z][A-Za-z\s&-]+?):\s*([^:]+?)(?=(?:[A-Z][A-Za-z\s&-]+?:|$))'
    sections = re.findall(section_pattern, full_text)

    for section_title, section_content in sections:
        section_title = section_title.strip()
        if len(section_title) > 3 and len(section_title) < 60:
            # Add main section as a topic
            if is_valid_topic(section_title):
                topics.append(section_title)

            # Add subtopics
            subtopics = re.split(r'[,;]', section_content)
            for sub in subtopics:
                sub = sub.strip().strip('.')
                if is_valid_topic(sub) and sub.lower() != section_title.lower():
                    topics.append(sub)

    # Strategy 2: If no sections found, split by commas/semicolons
    if not topics:
        parts = re.split(r'[,;.]', full_text)
        for part in parts:
            part = part.strip()
            if is_valid_topic(part):
                topics.append(part)

    # Deduplicate while preserving order
    seen = set()
    unique_topics = []
    for t in topics:
        t_lower = t.lower()
        if t_lower not in seen:
            seen.add(t_lower)
            unique_topics.append(t)

    return unique_topics[:15]  # Limit to 15 topics per module


def is_valid_topic(topic):
    """Check if a string is a valid topic"""
    if not topic or len(topic) < 4 or len(topic) > 80:
        return False
    if topic.isdigit() or re.match(r'^[\d\s.]+$', topic):
        return False
    if re.match(r'^\d+\.\d+', topic):
        return False
    if re.search(r'(Text\s*book|Reference|http|www\.|Annexure|CIE|SEE|marks|Chapter)', topic, re.IGNORECASE):
        return False
    if topic.startswith('&') or topic.startswith('(') or topic.startswith('-'):
        return False
    if not re.search(r'[a-zA-Z]{3,}', topic):
        return False
    # Must start with a letter
    if not re.match(r'^[A-Za-z]', topic):
        return False
    return True

# ============== GENERIC CONTENT MATCHING ==============
def build_generic_topic_index():
    """Build index of all topics in generic content"""
    topic_index = {}

    for domain_dir in Path(GENERIC_CONTENT_DIR).iterdir():
        if not domain_dir.is_dir() or domain_dir.name.startswith('.'):
            continue

        for subject_dir in domain_dir.iterdir():
            if not subject_dir.is_dir() or subject_dir.name.startswith('.'):
                continue

            chapters_dir = subject_dir / "chapters"
            if not chapters_dir.exists():
                continue

            for chapter_dir in chapters_dir.iterdir():
                if not chapter_dir.is_dir() or chapter_dir.name.startswith('.') or chapter_dir.name.startswith('_'):
                    continue

                topics_dir = chapter_dir / "topics"
                if not topics_dir.exists():
                    continue

                # Read chapter index for topic titles
                index_file = chapter_dir / "_index.json"
                if index_file.exists():
                    with open(index_file, 'r') as f:
                        try:
                            index_data = json.load(f)
                            topics_list = index_data.get("topics", [])

                            # Handle both list of dicts and list of strings
                            for topic_info in topics_list:
                                if isinstance(topic_info, dict):
                                    topic_id = topic_info.get("id", "")
                                    topic_title = topic_info.get("title", "")
                                elif isinstance(topic_info, str):
                                    topic_id = topic_info
                                    topic_title = topic_info.replace("-", " ").title()
                                else:
                                    continue

                                topic_path = topics_dir / topic_id

                                if topic_path.exists() and (topic_path / "read.md").exists():
                                    # Index by normalized title
                                    normalized = normalize_text(topic_title)
                                    topic_index[normalized] = {
                                        "path": str(topic_path),
                                        "title": topic_title,
                                        "id": topic_id,
                                        "subject": subject_dir.name,
                                        "chapter": chapter_dir.name
                                    }

                                    # Also index by topic_id (for direct matches)
                                    topic_index[normalize_text(topic_id.replace("-", " "))] = topic_index[normalized]
                        except json.JSONDecodeError:
                            pass

    return topic_index

def normalize_text(text):
    """Normalize text for comparison"""
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    # Remove common prefixes/suffixes
    text = re.sub(r'^(introduction to|basics of|fundamentals of)\s+', '', text)
    text = re.sub(r'\s+(concepts?|basics?|fundamentals?)$', '', text)
    return text.strip()

def find_matching_topic(vtu_topic, generic_index):
    """Find matching generic topic using fuzzy matching"""
    normalized_vtu = normalize_text(vtu_topic)

    # Try exact match first
    if normalized_vtu in generic_index:
        return generic_index[normalized_vtu]

    # Fuzzy match
    best_match = None
    best_score = 0

    for generic_normalized, generic_info in generic_index.items():
        # Calculate similarity
        score = SequenceMatcher(None, normalized_vtu, generic_normalized).ratio()

        # Also check if key words match
        vtu_words = set(normalized_vtu.split())
        generic_words = set(generic_normalized.split())
        word_overlap = len(vtu_words & generic_words) / max(len(vtu_words), 1)

        # Combined score
        combined_score = (score * 0.6) + (word_overlap * 0.4)

        if combined_score > best_score and combined_score >= FUZZY_MATCH_THRESHOLD:
            best_score = combined_score
            best_match = generic_info

    return best_match

# ============== CONTENT OPERATIONS ==============
def copy_topic_content(source_path, dest_path):
    """Copy all topic files from generic to VTU"""
    os.makedirs(dest_path, exist_ok=True)

    files_to_copy = ['read.md', 'mcqs.json', 'flashcards.json', 'visual.json',
                     'purpose.md', 'questions.json', 'memory.json', 'code.json']

    for filename in files_to_copy:
        src = os.path.join(source_path, filename)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dest_path, filename))

    return True

def call_api(messages, model=MODEL, max_retries=5):
    """Call NVIDIA API with robust retries and model fallback"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    models_to_try = [model] + FALLBACK_MODELS
    model_index = 0
    current_model = models_to_try[model_index]
    consecutive_rate_limits = 0

    for attempt in range(max_retries * 3):  # More attempts with aggressive model cycling
        try:
            data = json.dumps({
                "model": current_model,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 4096
            }).encode('utf-8')

            req = urllib.request.Request(API_URL, data=data, headers=headers)
            with urllib.request.urlopen(req, timeout=180) as response:
                result = json.loads(response.read().decode('utf-8'))
                return result['choices'][0]['message']['content']
        except urllib.error.HTTPError as e:
            log(f"      API Error {e.code} with {current_model.split('/')[-1]} (attempt {attempt+1})")
            if e.code == 429:  # Rate limit
                consecutive_rate_limits += 1
                if consecutive_rate_limits >= 2:
                    # Switch model after 2 consecutive rate limits
                    model_index = (model_index + 1) % len(models_to_try)
                    current_model = models_to_try[model_index]
                    log(f"      Switching to model: {current_model.split('/')[-1]}")
                    consecutive_rate_limits = 0
                    time.sleep(10)
                else:
                    wait_time = 30 + attempt * 10
                    log(f"      Rate limited. Waiting {wait_time}s...")
                    time.sleep(wait_time)
            elif e.code in [400, 404, 503]:  # Model unavailable/error
                model_index = (model_index + 1) % len(models_to_try)
                current_model = models_to_try[model_index]
                log(f"      Trying model: {current_model.split('/')[-1]}")
                consecutive_rate_limits = 0
                time.sleep(5)
            elif e.code >= 500:
                time.sleep(10 + attempt * 5)
                model_index = (model_index + 1) % len(models_to_try)
                current_model = models_to_try[model_index]
                consecutive_rate_limits = 0
            else:
                time.sleep(3 + attempt * 2)
        except urllib.error.URLError as e:
            log(f"      URL Error: {e.reason} (attempt {attempt+1})")
            time.sleep(10 + attempt * 5)
        except Exception as e:
            log(f"      Error: {e} (attempt {attempt+1})")
            time.sleep(5 + attempt * 3)
            model_index = (model_index + 1) % len(models_to_try)
            current_model = models_to_try[model_index]
            consecutive_rate_limits = 0

    log(f"      API failed after all attempts")
    return None

def generate_topic_content(topic_title, subject_name, module_title, dest_path):
    """Generate new content for a topic using NVIDIA API with robust error handling"""
    os.makedirs(dest_path, exist_ok=True)

    content_types = [
        ("read.md", generate_read_prompt),
        ("mcqs.json", generate_mcqs_prompt),
        ("flashcards.json", generate_flashcards_prompt),
        ("questions.json", generate_questions_prompt),
        ("memory.json", generate_memory_prompt),
        ("visual.json", generate_visual_prompt),
        ("purpose.md", generate_purpose_prompt),
    ]

    context = f"Subject: {subject_name}\nModule: {module_title}\nTopic: {topic_title}"
    generated_count = 0

    for filename, prompt_func in content_types:
        filepath = os.path.join(dest_path, filename)

        # Skip if file already exists
        if os.path.exists(filepath):
            generated_count += 1
            continue

        for retry in range(3):  # Retry each file up to 3 times
            try:
                prompt = prompt_func(topic_title, context)
                response = call_api([{"role": "user", "content": prompt}])

                if response:
                    content = extract_content(response, filename)

                    with open(filepath, 'w') as f:
                        if filename.endswith('.json'):
                            if isinstance(content, str):
                                try:
                                    content = json.loads(content)
                                except:
                                    content = {"topic": topic_title, "content": content[:1000]}
                            json.dump(content, f, indent=2)
                        else:
                            f.write(content if isinstance(content, str) else str(content))

                    generated_count += 1
                    break  # Success, move to next file
                else:
                    if retry < 2:
                        time.sleep(2)
            except Exception as e:
                log(f"      Error generating {filename} (attempt {retry+1}): {e}")
                if retry < 2:
                    time.sleep(2)

        # If all retries failed, create placeholder
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                if filename.endswith('.json'):
                    json.dump({"topic": topic_title, "status": "generation_failed"}, f, indent=2)
                else:
                    f.write(f"# {topic_title}\n\nContent generation pending.\n")

    return generated_count >= 4  # Consider success if at least 4 files generated

def extract_content(response, filename):
    """Extract content from API response"""
    if filename.endswith('.json'):
        # Find JSON in response
        json_match = re.search(r'```(?:json)?\s*([\s\S]*?)```', response)
        if json_match:
            try:
                return json.loads(json_match.group(1))
            except:
                pass

        # Try direct parse
        try:
            # Find first { or [ and last } or ]
            start = min(response.find('{'), response.find('['))
            if start == -1:
                start = response.find('{') if response.find('{') != -1 else response.find('[')
            end = max(response.rfind('}'), response.rfind(']')) + 1
            if start >= 0 and end > start:
                return json.loads(response[start:end])
        except:
            pass

        return {"content": response}
    else:
        # Markdown - extract from code block or return as is
        md_match = re.search(r'```(?:markdown)?\s*([\s\S]*?)```', response)
        if md_match:
            return md_match.group(1).strip()
        return response.strip()

# ============== PROMPT GENERATORS ==============
def generate_read_prompt(topic, context):
    return f"""Write educational content for the following topic. This is for VTU engineering students.

{context}

Write a comprehensive explanation in markdown format:
1. Start with a brief introduction
2. Explain core concepts clearly
3. Include examples where appropriate
4. Add key points or summary at the end

Keep it concise but thorough (500-800 words). Use proper markdown formatting."""

def generate_mcqs_prompt(topic, context):
    return f"""Create 5 multiple choice questions for the following topic:

{context}

Return ONLY a JSON array with this exact structure:
```json
[
  {{
    "id": "q1",
    "question": "Question text here?",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "correctIndex": 0,
    "explanation": "Brief explanation of why this answer is correct."
  }}
]
```

Make questions progressively harder (easy to challenging). Cover different aspects of the topic."""

def generate_flashcards_prompt(topic, context):
    return f"""Create 5 flashcards for studying the following topic:

{context}

Return ONLY a JSON array with this exact structure:
```json
[
  {{
    "id": "f1",
    "front": "Question or term on front of card",
    "back": "Answer or definition on back of card"
  }}
]
```

Cover key concepts, definitions, and important facts."""

def generate_questions_prompt(topic, context):
    return f"""Create 3 short answer/essay questions for the following topic:

{context}

Return ONLY a JSON array with this exact structure:
```json
[
  {{
    "id": "sa1",
    "question": "Question requiring detailed answer?",
    "expectedPoints": ["Key point 1", "Key point 2", "Key point 3"],
    "marks": 5
  }}
]
```

Include questions of varying difficulty (2, 5, and 10 marks)."""

def generate_memory_prompt(topic, context):
    return f"""Create memory aids for the following topic:

{context}

Return ONLY a JSON object with this exact structure:
```json
{{
  "mnemonics": ["Mnemonic 1 for remembering key concept"],
  "keyPoints": ["Key point 1", "Key point 2", "Key point 3"],
  "commonMistakes": ["Common mistake 1", "Common mistake 2"]
}}
```"""

def generate_visual_prompt(topic, context):
    return f"""Describe a visual diagram that would help explain the following topic:

{context}

Return ONLY a JSON object with this exact structure:
```json
{{
  "type": "flowchart|diagram|graph|timeline",
  "title": "Diagram title",
  "description": "Brief description of what the diagram shows",
  "elements": ["Element 1", "Element 2", "Element 3"],
  "relationships": ["Relationship between elements"]
}}
```"""

def generate_purpose_prompt(topic, context):
    return f"""Write the learning purpose for the following topic:

{context}

Write in markdown format:
1. Why is this topic important?
2. What will students learn?
3. How does it connect to other concepts?
4. Real-world applications

Keep it concise (150-250 words)."""

# ============== SUBJECT PROCESSING ==============
def process_subject(subject, branch_id, semester, generic_index):
    """Process a single subject - match/generate all topics"""
    subject_id = slugify(subject["name"])
    subject_code = subject["code"]

    log(f"\n{'='*60}")
    log(f"Processing: {subject_code} - {subject['name']}")
    log(f"{'='*60}")

    # Create subject directory
    subject_dir = os.path.join(VTU_OUTPUT_DIR, branch_id, f"sem-{semester}",
                               f"{subject_code.lower()}-{subject_id}")
    chapters_dir = os.path.join(subject_dir, "chapters")
    os.makedirs(chapters_dir, exist_ok=True)

    # Create _meta.json
    meta = {
        "id": subject_id,
        "code": subject_code,
        "name": subject["name"],
        "scheme": "2022",
        "branch": branch_id,
        "semester": semester,
        "credits": 4
    }
    with open(os.path.join(subject_dir, "_meta.json"), 'w') as f:
        json.dump(meta, f, indent=2)

    chapters_index = []

    for module in subject["modules"]:
        module_id = module["id"]
        module_title = module["title"]

        log(f"\n  Module: {module_title}")

        # Create chapter directory
        chapter_dir = os.path.join(chapters_dir, module_id)
        topics_dir = os.path.join(chapter_dir, "topics")
        os.makedirs(topics_dir, exist_ok=True)

        topics_info = []

        for idx, topic_title in enumerate(module["topics"], 1):
            topic_id = slugify(topic_title) or f"topic-{idx}"
            topic_path = os.path.join(topics_dir, topic_id)

            # SKIP if topic already has content (read.md exists)
            read_file = os.path.join(topic_path, "read.md")
            if os.path.exists(read_file):
                log(f"    ⏭ SKIP: {topic_title[:50]}... (already exists)")
                topics_info.append({
                    "id": topic_id,
                    "title": topic_title,
                    "order": idx,
                    "estimatedMinutes": 15,
                    "hasVisual": True,
                    "hasQuestions": True
                })
                continue

            # Check for matching generic content
            match = find_matching_topic(topic_title, generic_index)

            if match:
                log(f"    ✓ COPY: {topic_title[:40]}... <- {match['title'][:30]}...")
                copy_topic_content(match["path"], topic_path)

                with stats_lock:
                    stats["topics_copied"] += 1
                    stats["mapping_table"].append({
                        "vtu_topic": topic_title,
                        "generic_topic": match["title"],
                        "action": "copied",
                        "source": match["path"]
                    })
            else:
                log(f"    ○ GENERATE: {topic_title[:50]}...")
                try:
                    generate_topic_content(topic_title, subject["name"], module_title, topic_path)
                    with stats_lock:
                        stats["topics_generated"] += 1
                        stats["mapping_table"].append({
                            "vtu_topic": topic_title,
                            "generic_topic": None,
                            "action": "generated",
                            "source": None
                        })
                except Exception as e:
                    log(f"      ERROR: {e}")
                    with stats_lock:
                        stats["topics_failed"] += 1

            topics_info.append({
                "id": topic_id,
                "title": topic_title,
                "order": idx,
                "estimatedMinutes": 15,
                "hasVisual": True,
                "hasQuestions": True
            })

        # Create chapter _index.json
        chapter_index = {
            "chapterId": module_id,
            "chapterTitle": module_title,
            "hasTopics": True,
            "topics": topics_info
        }
        with open(os.path.join(chapter_dir, "_index.json"), 'w') as f:
            json.dump(chapter_index, f, indent=2)

        chapters_index.append({
            "id": module_id,
            "title": module_title,
            "order": int(module_id.split('-')[-1]),
            "topicCount": len(topics_info)
        })

    # Create chapters _index.json
    with open(os.path.join(chapters_dir, "_index.json"), 'w') as f:
        json.dump({"chapters": chapters_index}, f, indent=2)

    with stats_lock:
        stats["subjects_processed"] += 1

    return subject_dir

def commit_and_push(subject_name, subject_code, branch):
    """Git commit and push after each subject"""
    os.chdir(VTU_OUTPUT_DIR)

    try:
        # Add all changes
        subprocess.run(['git', 'add', '-A'], check=True, capture_output=True)

        # Check if there are changes to commit
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        if not result.stdout.strip():
            log("  No changes to commit")
            return

        # Commit
        commit_msg = f"Add VTU content: {subject_code} - {subject_name} ({branch})"
        subprocess.run(['git', 'commit', '-m', commit_msg], check=True, capture_output=True)

        # Push
        subprocess.run(['git', 'push'], check=True, capture_output=True)
        log(f"  ✓ Committed and pushed: {subject_code}")
    except subprocess.CalledProcessError as e:
        log(f"  Git error: {e}")

# ============== MAIN PROCESSING ==============
def process_branch(branch_name, branch_id, generic_index):
    """Process all PDFs for a branch"""
    branch_path = os.path.join(VTU_SYLLABUS_DIR, branch_name)

    if not os.path.exists(branch_path):
        log(f"Branch path not found: {branch_path}")
        return

    # Find all semester PDFs
    pdf_files = sorted([f for f in os.listdir(branch_path) if f.endswith('.pdf')])

    for pdf_file in pdf_files:
        pdf_path = os.path.join(branch_path, pdf_file)

        # Extract semester(s) from filename
        sem_match = re.search(r'Sem_(\d+)(?:-(\d+))?', pdf_file)
        if not sem_match:
            continue

        sem_start = int(sem_match.group(1))
        sem_end = int(sem_match.group(2)) if sem_match.group(2) else sem_start

        log(f"\n\n{'#'*70}")
        log(f"# Processing: {branch_name} - {pdf_file}")
        log(f"{'#'*70}")

        # Parse syllabus
        subjects = parse_syllabus(pdf_path)
        log(f"Found {len(subjects)} theory subjects")

        for subject in subjects:
            # Determine semester based on course code
            code = subject["code"]
            sem_digit = re.search(r'\d', code)
            semester = int(sem_digit.group()) if sem_digit else sem_start

            # Process subject
            process_subject(subject, branch_id, semester, generic_index)

            # Commit and push
            commit_and_push(subject["name"], subject["code"], branch_id)

def main():
    parser = argparse.ArgumentParser(description='Generate VTU 2022 Scheme content')
    parser.add_argument('--branch', help='Specific branch to process')
    parser.add_argument('--semester', type=int, help='Specific semester to process')
    args = parser.parse_args()

    log("="*70)
    log("VTU 2022 Scheme Content Generator")
    log("="*70)

    # Build generic topic index
    log("\nBuilding generic content index...")
    generic_index = build_generic_topic_index()
    log(f"Indexed {len(generic_index)} topics from generic content")

    # Create manifest
    manifest = {
        "id": "vtu-2022-scheme",
        "name": "VTU 2022 Scheme",
        "description": "Complete syllabus content for VTU 2022 Scheme - All CS branches",
        "version": "1.0.0",
        "branches": list(BRANCH_FOLDERS.values())
    }
    with open(os.path.join(VTU_OUTPUT_DIR, "manifest.json"), 'w') as f:
        json.dump(manifest, f, indent=2)

    # Process branches
    branches_to_process = BRANCH_FOLDERS.items()
    if args.branch:
        branches_to_process = [(k, v) for k, v in BRANCH_FOLDERS.items() if args.branch.lower() in k.lower()]

    for branch_name, branch_id in branches_to_process:
        process_branch(branch_name, branch_id, generic_index)

    # Save mapping table
    log("\n\n" + "="*70)
    log("GENERATION COMPLETE - SUMMARY")
    log("="*70)
    log(f"Subjects processed: {stats['subjects_processed']}")
    log(f"Topics copied from generic: {stats['topics_copied']}")
    log(f"Topics generated via API: {stats['topics_generated']}")
    log(f"Topics failed: {stats['topics_failed']}")

    # Save mapping table
    mapping_file = os.path.join(VTU_OUTPUT_DIR, "mapping_table.json")
    with open(mapping_file, 'w') as f:
        json.dump({
            "stats": stats,
            "mapping": stats["mapping_table"]
        }, f, indent=2)
    log(f"\nMapping table saved to: {mapping_file}")

    # Final commit
    commit_and_push("Final summary and mapping table", "FINAL", "all")

if __name__ == "__main__":
    main()
