#!/usr/bin/env python3
"""
Upgrade VTU topic content to 8+ rating via parallel API calls.

FAST MODE: Makes 9 parallel API calls per topic (one per file type).
Each API call generates only ONE file, making requests 5-10x faster.

Usage:
  python upgrade_topics_to_8plus.py sem4-topic-paths.txt
  python upgrade_topics_to_8plus.py sem4-topic-paths.txt --dry-run
  python upgrade_topics_to_8plus.py sem4-topic-paths.txt --batch-size 2 --resume
  python upgrade_topics_to_8plus.py sem4-topic-paths.txt --log --minimax-only
  python upgrade_topics_to_8plus.py sem4-topic-paths.txt --debug  # Very verbose

Requires: aiohttp
"""

import argparse
import asyncio
import json
import logging
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import aiohttp

# Logging configuration
logger = logging.getLogger("vtu_upgrade")
log_handler = logging.StreamHandler()
log_formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
log_handler.setFormatter(log_formatter)
logger.addHandler(log_handler)
logger.setLevel(logging.WARNING)  # Default: only warnings and errors

# ── API configuration ──────────────────────────────────────────────────────
APIS = {
    "chutes": {
        "base_url": os.environ.get("CHUTES_BASE_URL", "https://llm.chutes.ai/v1/chat/completions"),
        "api_key": os.environ.get("CHUTES_API_KEY", "cpk_a744b82c5b9c4e8b9c7c8e1442e8d160.c3a84cdb26e850c9b8f358af872bca49.ymNhlwAf2nbhnTZJE620p8sv1aTgEGwx"),
        "model": os.environ.get("CHUTES_MODEL", "deepseek-ai/DeepSeek-R1-TEE"),
    },
    "minimax": {
        "base_url": os.environ.get("MINIMAX_BASE_URL", "https://api.minimax.io/v1/chat/completions"),
        "api_key": os.environ.get("MINIMAX_API_KEY", "sk-cp-r--6hiKCzLgU9QbQREFxR4v336s2kP0vDCeb3x7-iNJxAAdDwQeXhInB8zgfwcduBNoBtQBSj33uci2eCKcCu7q4VjmMGWDhKYHXu_lpv1fmWctproM4cAg"),
        "model": os.environ.get("MINIMAX_MODEL", "MiniMax-M2.5"),
    },
}

# File types to generate (each gets its own API call)
FILE_CONFIGS = {
    "read.md": {
        "type": "markdown",
        "prompt": """Generate an 8+ quality read.md file for VTU engineering students.

STRUCTURE REQUIREMENTS:
- Start with: # <Topic Title>
- Use ## for major sections, ### for sub-sections
- Include: ## Introduction (2-3 paragraphs explaining the topic and its importance)
- Cover all key concepts, definitions, formulas, theorems with detailed explanations
- Include ## Examples section with 2-3 worked examples showing step-by-step solutions
- Describe relevant diagrams/charts in text (what they show, key components)
- End with ## Exam Tips section listing 5-7 exam-relevant points for VTU exams

QUALITY REQUIREMENTS:
- Length: 1500-3000 words minimum
- Write at B.E./B.Tech level — technically accurate, detailed, exam-focused
- Use proper markdown formatting with code blocks for formulas/algorithms
- Include real-world applications and engineering context
- Ensure content is directly relevant to VTU 2022 scheme syllabus"""
    },
    "purpose.md": {
        "type": "markdown",
        "prompt": """Generate a concise purpose.md explaining learning objectives.

STRUCTURE REQUIREMENTS:
- Start with: # Learning Objectives
- Next line: "After studying this topic, you should be able to:"
- Numbered list of 6-8 specific, measurable learning outcomes
- Each outcome should start with action verbs: Understand, Explain, Apply, Analyze, Design, Implement, etc.

QUALITY REQUIREMENTS:
- Each objective must be clear, specific, and testable
- Focus on skills students will gain, not just knowledge
- Align with VTU exam pattern and syllabus outcomes"""
    },
    "summary.md": {
        "type": "markdown",
        "prompt": """Generate a comprehensive 1-page summary.md for quick revision.

STRUCTURE REQUIREMENTS:
- Start with: # <Topic Title> - Summary
- ## Key Definitions and Concepts (bullet points with concise definitions)
- ## Important Formulas and Theorems (list all formulas with brief descriptions)
- ## Key Points (7-10 bullet points covering main concepts)
- ## Common Mistakes to Avoid (3-4 points)
- ## Revision Tips (3-4 practical tips for exam preparation)

QUALITY REQUIREMENTS:
- Length: 400-800 words
- Use concise language suitable for last-minute revision
- Include all exam-relevant formulas and key terms
- Format formulas in markdown code blocks or inline code"""
    },
    "mcqs.json": {
        "type": "json",
        "prompt": """Generate 15-20 high-quality multiple-choice questions.

JSON STRUCTURE (return array):
[
  {
    "id": "mcq-1",
    "question": "Question text here",
    "options": ["Option A text", "Option B text", "Option C text", "Option D text"],
    "correctAnswer": "A",
    "explanation": "Detailed explanation why A is correct and why others are wrong (2-3 sentences)",
    "difficulty": "easy"
  }
]

GENERATION RULES:
- Total: 15-20 questions minimum
- Difficulty distribution: 4-5 easy, 8-10 medium, 3-5 hard
- Question types: Mix of conceptual, numerical, application-based, and scenario-based
- Distractors must be PLAUSIBLE (common mistakes or related concepts)
- Explanations must teach, not just state the answer
- correctAnswer must be one of: "A", "B", "C", "D"
- Cover all major concepts in the topic"""
    },
    "flashcards.json": {
        "type": "json",
        "prompt": """Generate 20-25 effective flashcards for memorization.

JSON STRUCTURE (return array):
[
  {
    "id": "fc-1",
    "front": "Concise question or term (one line)",
    "back": "Clear answer or definition (1-3 sentences, focused)"
  }
]

GENERATION RULES:
- Total: 20-25 flashcards minimum
- Front: Short, specific question or key term
- Back: Concise answer (not too verbose, suitable for quick review)
- Cover: Definitions, formulas, key concepts, important facts
- Mix question types: "What is...", "Define...", "Formula for...", "Purpose of...", etc.
- Ensure progressive difficulty (start basic, then advanced)"""
    },
    "questions.json": {
        "type": "json",
        "prompt": """Generate 12-15 VTU-style exam questions.

JSON STRUCTURE (return array):
[
  {
    "id": "q-1",
    "type": "short",
    "question": "Question text",
    "expectedPoints": ["Point 1 expected in answer", "Point 2", "Point 3"],
    "marks": 5,
    "difficulty": "medium",
    "hint": "Optional hint for solving"
  }
]

GENERATION RULES:
- Total: 12-15 questions minimum
- Types distribution:
  * "short" (5 marks): 5-6 questions with 3-5 expected points
  * "long" (10 marks): 4-5 questions with 6-8 expected points
  * "numerical" (5-10 marks): 3-4 questions with step-by-step solution points
- Difficulty: Mix easy, medium, hard aligned with VTU exam patterns
- Question starters: "Explain...", "Derive...", "Compare...", "Discuss...", "Calculate...", "Design..."
- expectedPoints: List all key points that should appear in a complete answer"""
    },
    "memory.json": {
        "type": "json",
        "prompt": """Generate powerful memory aids and mnemonics.

JSON STRUCTURE (return object):
{
  "topicId": "TOPIC_ID",
  "mnemonics": [
    {"id": "m-1", "title": "Mnemonic title", "content": "ACRONYM or memory phrase with explanation"}
  ],
  "acronyms": [
    {"term": "ACRONYM", "expansion": "Full form", "usage": "What it helps remember"}
  ],
  "visualTips": [
    {"concept": "Concept name", "visualization": "How to visualize/remember it"}
  ],
  "analogies": [
    {"concept": "Technical concept", "analogy": "Real-world analogy that makes it easier to understand"}
  ]
}

GENERATION RULES:
- mnemonics: 4-6 memory devices for lists, steps, or sequences
- acronyms: 3-5 helpful acronyms used in the topic
- visualTips: 4-6 ways to visualize abstract concepts
- analogies: 3-5 real-world analogies for complex concepts
- Make them memorable, clever, and educationally sound"""
    },
    "visual.json": {
        "type": "json",
        "prompt": """Generate comprehensive visual learning aids descriptions.

JSON STRUCTURE (return object):
{
  "topicId": "TOPIC_ID",
  "diagrams": [
    {
      "id": "diagram-1",
      "title": "Diagram title",
      "description": "What this diagram shows",
      "elements": ["Element 1 description", "Element 2", "Relationship between elements"],
      "purpose": "What students learn from this diagram"
    }
  ],
  "charts": [
    {"type": "flowchart/comparison/table", "title": "Chart title", "content": "What it illustrates"}
  ],
  "mindMaps": [
    {"centralConcept": "Main topic", "branches": ["Branch 1", "Branch 2"], "purpose": "Overview purpose"}
  ]
}

GENERATION RULES:
- diagrams: 3-5 essential diagrams (block diagrams, architectures, flows)
- charts: 2-4 comparison tables, flowcharts, or classification charts
- mindMaps: 1-2 concept maps showing relationships
- Each visual must have clear educational purpose
- Describe visual elements precisely (shapes, arrows, labels, relationships)"""
    },
    "code.json": {
        "type": "json",
        "prompt": """Generate code examples and algorithm implementations.

JSON STRUCTURE (return array):
[
  {
    "id": "code-1",
    "language": "pseudocode",
    "title": "Algorithm: Title",
    "description": "What this code demonstrates",
    "code": "ALGORITHM Name\\nBEGIN\\n  step 1\\n  step 2\\nEND",
    "explanation": "Line-by-line explanation of key parts",
    "complexity": {"time": "O(n)", "space": "O(1)"}
  }
]

GENERATION RULES:
- Generate 3-5 examples IF topic is code-applicable (algorithms, data structures, protocols)
- If topic is purely conceptual (definitions, theory only), return empty array []
- Language options: "pseudocode" (always include if applicable), "python", "c", "java"
- Include at least 1 pseudocode version for every algorithm
- For each code: clear comments, proper formatting, complete working example
- Add time/space complexity analysis where relevant
- Ensure code is syntactically correct and follows best practices"""
    },
}

DEFAULT_BATCH_SIZE = 3  # 3 topics = 27 API calls max
MAX_TOKENS_RESPONSE = 8192  # Smaller since we're generating one file at a time
REQUEST_TIMEOUT = 180  # 3 minutes - LLMs need time to generate long content (especially read.md with 1500-3000 words)
MAX_RETRIES = 1  # Only 1 retry to avoid wasting time on persistent failures
RETRY_DELAY = 2  # 2 seconds between retries
PROGRESS_FILE = "upgrade_progress.json"  # Track completed topics

BASE_SYSTEM_PROMPT = """You are an expert university lecturer creating study material for VTU (Visvesvaraya Technological University) 2022 Scheme, Computer Science & Engineering branch.

Your content must achieve 8+ quality rating on:
- Coverage: Complete, comprehensive treatment of the topic
- Depth: Appropriate for B.E./B.Tech level engineering students
- Clarity: Well-structured, easy to understand, with examples
- Exam readiness: Aligned with VTU exam patterns and syllabus

CRITICAL OUTPUT RULES:
- For JSON files: Respond with ONLY valid JSON (array or object). No markdown fences, no explanatory text, no code blocks.
- For Markdown files: Respond with ONLY the markdown content. No JSON wrapper, no code fences around the entire response.
- Content must be technically accurate and exam-focused
- Use proper terminology, formulas, and engineering conventions
- Include practical examples and real-world applications where relevant"""


def read_topic_paths(filepath: str) -> list[str]:
    """Read topic paths from file."""
    paths = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                paths.append(line)
    return paths


def load_progress() -> set[str]:
    """Load set of completed topic paths from progress file."""
    if not Path(PROGRESS_FILE).exists():
        return set()
    try:
        data = json.loads(Path(PROGRESS_FILE).read_text())
        return set(data.get("completed", []))
    except Exception:
        return set()


def save_progress(completed: set[str]):
    """Save completed topics to progress file."""
    try:
        Path(PROGRESS_FILE).write_text(json.dumps({
            "completed": list(completed),
            "last_updated": datetime.now().isoformat()
        }, indent=2))
    except Exception as e:
        print(f"Warning: Could not save progress: {e}")


def get_topic_context(topic_path: str) -> dict:
    """Extract subject/module/topic metadata from the directory path."""
    topic_dir = Path(topic_path)
    parts = topic_dir.parts

    # Walk up: topics/<id> -> module-N -> chapters -> <subject> -> sem-N
    try:
        ti = len(parts) - 1                      # topic_id
        topics_i = ti - 1                         # "topics"
        module_i = topics_i - 1                   # "module-N"
        chapters_i = module_i - 1                 # "chapters"
        subject_i = chapters_i - 1                # subject dir name
        sem_i = subject_i - 1                     # sem-N
    except Exception:
        return None

    topic_id = parts[ti]
    module_id = parts[module_i]
    subject_dir = parts[subject_i]
    sem_dir = parts[sem_i]

    # Parse subject code + name
    m = re.match(r"(bcsl?\d+[a-d]?)-(.+)", subject_dir)
    if m:
        subject_code = m.group(1).upper()
        subject_name = m.group(2).replace("-", " ").title()
    else:
        subject_code = subject_dir.upper()
        subject_name = subject_dir.replace("-", " ").title()

    module_num = module_id.split("-")[-1]

    # Get proper title and sibling topics from _index.json
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
        "sem": sem_dir.replace("sem-", ""),
        "siblings": sibling_topics,
    }


def load_existing_content(topic_path: str, max_chars: int = 3000) -> str:
    """Load existing topic files for context (what needs upgrading)."""
    parts = []
    topic_dir = Path(topic_path)

    # Load key existing files for context
    for fname in ["read.md", "purpose.md"]:
        fpath = topic_dir / fname
        if fpath.exists():
            content = fpath.read_text(encoding="utf-8", errors="replace")
            if len(content) > 1500:
                content = content[:1500] + "\n... [content truncated]"
            parts.append(f"=== CURRENT {fname.upper()} ===\n{content}\n")

    return "\n".join(parts)[:max_chars]


def extract_content(text: str, file_type: str) -> str | dict | list | None:
    """Extract content from API response."""
    content = text.strip()

    # Remove <think> blocks
    content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL | re.IGNORECASE)
    content = content.strip()

    # Remove markdown code fences if present
    if content.startswith("```"):
        lines = content.split("\n")
        if len(lines) > 2:
            content = "\n".join(lines[1:-1]) if lines[-1].strip() == "```" else "\n".join(lines[1:])

    content = content.strip()

    # For JSON files, parse the JSON
    if file_type == "json":
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return None

    # For markdown files, return as-is
    return content


async def call_api_for_file(
    session: aiohttp.ClientSession,
    api_name: str,
    topic_idx: int,
    topic_path: str,
    ctx: dict,
    existing_content: str,
    filename: str,
    semaphore: asyncio.Semaphore,
) -> tuple[str, str | dict | list | None]:
    """Call API to generate one specific file with retry logic. Returns (filename, content)."""

    file_config = FILE_CONFIGS[filename]
    logger.info(f"Topic #{topic_idx} | {filename} | Starting API call via {api_name.upper()}")

    # Build rich context-aware prompt
    siblings_str = ", ".join(ctx["siblings"][:10]) if ctx["siblings"] else "(no sibling info)"
    prompt_with_context = file_config["prompt"].replace("TOPIC_ID", ctx["topic_id"])

    user_prompt = f"""Subject: {ctx["subject_code"]} — {ctx["subject_name"]} (VTU 2022 Scheme, Semester {ctx["sem"]})
Module {ctx["module_num"]} topics: {siblings_str}

TOPIC TO UPGRADE: "{ctx["topic_title"]}"
Topic ID: {ctx["topic_id"]}

{existing_content}

TASK: Generate ONLY the file: {filename}

{prompt_with_context}

OUTPUT FORMAT:
- For JSON files: Respond with ONLY valid JSON (no markdown fences, no extra text)
- For Markdown files: Respond with ONLY the markdown content (no JSON wrapper, no fences)
"""

    api = APIS[api_name]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api['api_key']}",
    }
    payload = {
        "model": api["model"],
        "messages": [
            {"role": "system", "content": BASE_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.3,
        "max_tokens": MAX_TOKENS_RESPONSE,
    }

    # Retry logic
    last_error = None
    for attempt in range(MAX_RETRIES + 1):
        attempt_num = attempt + 1
        logger.debug(f"Topic #{topic_idx} | {filename} | Attempt {attempt_num}/{MAX_RETRIES + 1} via {api_name.upper()}")

        async with semaphore:
            start_time = time.time()
            try:
                async with session.post(
                    api["base_url"],
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(
                        total=REQUEST_TIMEOUT,  # 180s total - LLMs need time for long content
                        connect=15,  # 15s to establish connection
                        sock_read=120  # 120s between data chunks - LLMs can take 60-90s to generate before streaming
                    ),
                ) as resp:
                    elapsed = time.time() - start_time

                    if resp.status != 200:
                        body = await resp.text()
                        last_error = f"HTTP {resp.status}"
                        logger.warning(f"Topic #{topic_idx} | {filename} | {last_error} after {elapsed:.1f}s (attempt {attempt_num})")
                        if attempt < MAX_RETRIES:
                            await asyncio.sleep(RETRY_DELAY)
                            continue
                        return (filename, {"_error": last_error})

                    data = await resp.json()
                    content = (data.get("choices") or [{}])[0].get("message", {}).get("content", "")

                    if not content:
                        last_error = "Empty response"
                        logger.warning(f"Topic #{topic_idx} | {filename} | {last_error} after {elapsed:.1f}s (attempt {attempt_num})")
                        if attempt < MAX_RETRIES:
                            await asyncio.sleep(RETRY_DELAY)
                            continue
                        return (filename, {"_error": last_error})

                    parsed = extract_content(content, file_config["type"])

                    if parsed is None:
                        last_error = "Invalid format"
                        logger.warning(f"Topic #{topic_idx} | {filename} | {last_error} after {elapsed:.1f}s (attempt {attempt_num})")
                        if attempt < MAX_RETRIES:
                            await asyncio.sleep(RETRY_DELAY)
                            continue
                        return (filename, {"_error": last_error})

                    # Success!
                    logger.info(f"Topic #{topic_idx} | {filename} | ✓ Success in {elapsed:.1f}s via {api_name.upper()}")
                    return (filename, parsed)

            except asyncio.TimeoutError:
                elapsed = time.time() - start_time
                last_error = "Timeout"
                logger.warning(f"Topic #{topic_idx} | {filename} | Timeout after {elapsed:.1f}s (attempt {attempt_num})")
                if attempt < MAX_RETRIES:
                    await asyncio.sleep(RETRY_DELAY)
                    continue
                return (filename, {"_error": last_error})
            except Exception as e:
                elapsed = time.time() - start_time
                last_error = str(e)[:50]
                logger.error(f"Topic #{topic_idx} | {filename} | Exception: {last_error} after {elapsed:.1f}s (attempt {attempt_num})")
                if attempt < MAX_RETRIES:
                    await asyncio.sleep(RETRY_DELAY)
                    continue
                return (filename, {"_error": last_error})

    # Should not reach here, but just in case
    return (filename, {"_error": last_error or "Unknown error"})


async def process_topic(
    session: aiohttp.ClientSession,
    topic_idx: int,
    topic_path: str,
    available_apis: list[str],
    semaphore: asyncio.Semaphore,
    dry_run: bool,
) -> tuple[int, str, dict]:
    """Process one topic by making parallel API calls for each file."""
    topic_dir = Path(topic_path)
    topic_name = topic_dir.name
    start_time = time.time()
    timestamp = datetime.now().strftime("%H:%M:%S")

    # Extract VTU context (subject, module, semester, etc.)
    ctx = get_topic_context(topic_path)
    if not ctx:
        # Fallback context if path parsing fails
        ctx = {
            "topic_id": topic_name,
            "topic_title": topic_name.replace("-", " ").title(),
            "module_num": "?",
            "module_id": "unknown",
            "subject_code": "UNKNOWN",
            "subject_name": "Unknown Subject",
            "sem": "?",
            "siblings": [],
        }

    display_label = f"{ctx['subject_code']} M{ctx['module_num']}: {ctx['topic_title']}"
    print(f"  [{timestamp}] 🚀 START  #{topic_idx:<4} {display_label:<45} (9 parallel API calls)")

    # Load existing content for upgrade context
    existing_content = load_existing_content(topic_path)

    # Create tasks for all files (9 parallel API calls)
    tasks = []
    api_assignments = []
    for i, filename in enumerate(FILE_CONFIGS.keys()):
        api_name = available_apis[i % len(available_apis)]  # Round-robin
        api_assignments.append((filename, api_name))
        tasks.append(call_api_for_file(
            session, api_name, topic_idx, topic_path, ctx, existing_content, filename, semaphore
        ))

    logger.debug(f"Topic #{topic_idx} | API assignments: {dict(api_assignments)}")

    # Execute all 9 API calls in parallel
    logger.debug(f"Topic #{topic_idx} | Launching 9 parallel API calls...")
    results = await asyncio.gather(*tasks)
    logger.debug(f"Topic #{topic_idx} | All API calls completed")

    # Collect results
    files_data = {}
    success_count = 0
    error_count = 0

    errors_detail = []
    for filename, content in results:
        if isinstance(content, dict) and "_error" in content:
            error_count += 1
            files_data[filename] = None
            errors_detail.append(f"{filename}: {content['_error']}")
        else:
            success_count += 1
            files_data[filename] = content

    elapsed = time.time() - start_time
    timestamp = datetime.now().strftime("%H:%M:%S")

    # Write files
    written_count = 0
    if not dry_run and success_count > 0:
        topic_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Topic #{topic_idx} | Writing {success_count} files to {topic_dir}")

        for filename, content in files_data.items():
            if content is None:
                continue

            fpath = topic_dir / filename
            if isinstance(content, (dict, list)):
                file_size = len(json.dumps(content, indent=2, ensure_ascii=False))
                fpath.write_text(json.dumps(content, indent=2, ensure_ascii=False), encoding="utf-8")
                logger.debug(f"Topic #{topic_idx} | Wrote {filename} ({file_size} bytes)")
            else:
                file_size = len(str(content))
                fpath.write_text(str(content), encoding="utf-8")
                logger.debug(f"Topic #{topic_idx} | Wrote {filename} ({file_size} bytes)")
            written_count += 1

    status_icon = "✅" if error_count == 0 else "⚠️" if success_count > 0 else "❌"
    print(f"  [{timestamp}] {status_icon} DONE   #{topic_idx:<4} {display_label:<45} ({elapsed:>5.1f}s) {success_count}/9 files {'(DRY)' if dry_run else 'written'}")
    if error_count > 0 and len(errors_detail) <= 3:
        for err in errors_detail:
            print(f"            ↳ {err}")

    return (topic_idx, topic_path, {
        "success": success_count,
        "errors": error_count,
        "elapsed": elapsed,
        "written": written_count
    })


def main():
    parser = argparse.ArgumentParser(description="Upgrade VTU topics via parallel API calls (9 calls per topic)")
    parser.add_argument("paths_file", help="Text file with topic paths")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE, help=f"Topics concurrent (default {DEFAULT_BATCH_SIZE})")
    parser.add_argument("--chutes-only", action="store_true", help="Use only Chutes")
    parser.add_argument("--minimax-only", action="store_true", help="Use only MiniMax")
    parser.add_argument("--resume", action="store_true", help="Skip already completed topics")
    parser.add_argument("--log", action="store_true", help="Enable detailed real-time logging")
    parser.add_argument("--debug", action="store_true", help="Enable debug-level logging (very verbose)")
    args = parser.parse_args()

    # Configure logging based on flags
    if args.debug:
        logger.setLevel(logging.DEBUG)
    elif args.log:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARNING)

    paths_file = Path(args.paths_file)
    if not paths_file.exists():
        print(f"Error: File not found: {paths_file}")
        sys.exit(1)

    all_topics = read_topic_paths(str(paths_file))
    if not all_topics:
        print("Error: No topics found")
        sys.exit(1)

    # Load completed topics if resuming
    completed = load_progress() if args.resume else set()
    topics = [t for t in all_topics if t not in completed] if args.resume else all_topics

    if args.resume and completed:
        print(f"\n📁 Resume mode: Found {len(completed)} completed topics")
        print(f"   Processing remaining {len(topics)} topics\n")

    # Determine APIs
    use_chutes = not args.minimax_only
    use_minimax = not args.chutes_only
    available_apis = []
    if use_chutes:
        available_apis.append("chutes")
    if use_minimax:
        available_apis.append("minimax")

    if not available_apis:
        print("Error: No APIs selected")
        sys.exit(1)

    batch_size = max(1, args.batch_size)
    num_batches = (len(topics) + batch_size - 1) // batch_size

    print(f"\n{'='*100}")
    print("  VTU TOPIC UPGRADE - FAST PARALLEL MODE (9 API calls per topic)")
    print(f"{'='*100}")
    print(f"  Source file     : {paths_file.name}")
    if args.resume and completed:
        print(f"  Total topics    : {len(all_topics)} ({len(completed)} completed, {len(topics)} remaining)")
    else:
        print(f"  Total topics    : {len(topics)}")
    print(f"  APIs            : {', '.join(api.upper() for api in available_apis)}")
    print(f"  Batch size      : {batch_size} topics concurrent")
    print(f"  Total batches   : {num_batches}")
    print(f"  API calls/topic : 9 (parallel, with retry)")
    print(f"  Total API calls : {len(topics) * 9}")
    mode_str = 'DRY RUN' if args.dry_run else ('LIVE (RESUME)' if args.resume else 'LIVE')
    print(f"  Mode            : {mode_str}")
    print(f"{'='*100}\n")

    async def run():
        # Increased concurrency since we reduced batch size and timeout
        semaphore = asyncio.Semaphore(30)  # 30 concurrent API calls (increased from 20)
        connector = aiohttp.TCPConnector(
            limit=50,  # Increased connection pool
            keepalive_timeout=60,  # Reduced keepalive (was 300s - too long)
            force_close=False,  # Keep connections alive for reuse
            enable_cleanup_closed=True,
            ttl_dns_cache=300  # DNS cache to speed up reconnections
        )
        start_time = time.time()

        stats = {
            "total_topics": 0,
            "total_files_success": 0,
            "total_files_errors": 0,
            "total_api_calls": 0,
        }

        # Track completed topics for progress saving
        completed_topics = completed.copy() if args.resume else set()

        async with aiohttp.ClientSession(connector=connector) as session:
            for batch_num in range(num_batches):
                batch_start = batch_num * batch_size
                batch_end = min(batch_start + batch_size, len(topics))
                batch_topics = topics[batch_start:batch_end]

                print(f"\n{'─'*100}")
                print(f"  BATCH {batch_num + 1}/{num_batches}  |  Topics {batch_start + 1}-{batch_end} of {len(topics)}")
                print(f"{'─'*100}")
                logger.info(f"Starting batch {batch_num + 1}/{num_batches} with {len(batch_topics)} topics")

                # Process batch
                tasks = []
                for i, topic_path in enumerate(batch_topics):
                    topic_idx = batch_start + i + 1
                    logger.debug(f"Creating task for topic #{topic_idx}: {topic_path}")
                    tasks.append(process_topic(session, topic_idx, topic_path, available_apis, semaphore, args.dry_run))

                batch_start_time = time.time()
                logger.info(f"Launching {len(tasks)} topic tasks ({len(tasks) * 9} API calls)...")
                results = await asyncio.gather(*tasks, return_exceptions=True)
                batch_elapsed = time.time() - batch_start_time
                logger.info(f"Batch {batch_num + 1} completed in {batch_elapsed:.1f}s")

                # Process results
                batch_success = 0
                batch_files_ok = 0
                batch_files_err = 0
                batch_completed = []

                for i, result in enumerate(results):
                    if isinstance(result, Exception):
                        print(f"  ERROR: Topic {batch_topics[i]} raised exception: {str(result)[:100]}")
                        continue

                    topic_idx, topic_path_name, topic_stats = result
                    topic_path = batch_topics[i]
                    stats["total_topics"] += 1
                    stats["total_files_success"] += topic_stats["success"]
                    stats["total_files_errors"] += topic_stats["errors"]
                    stats["total_api_calls"] += 9

                    batch_files_ok += topic_stats["success"]
                    batch_files_err += topic_stats["errors"]
                    if topic_stats["success"] >= 7:  # 78% success rate (7/9 files)
                        batch_success += 1
                        if not args.dry_run:
                            batch_completed.append(topic_path)

                # Save progress after each batch
                if not args.dry_run and batch_completed:
                    completed_topics.update(batch_completed)
                    save_progress(completed_topics)

                # Batch summary
                elapsed_total = time.time() - start_time
                progress_pct = (batch_end / len(topics)) * 100
                topics_per_sec = stats["total_topics"] / elapsed_total if elapsed_total > 0 else 0
                eta_sec = (len(topics) - batch_end) / topics_per_sec if topics_per_sec > 0 else 0

                print(f"\n  Batch: {batch_success}/{len(batch_topics)} topics OK, {batch_files_ok} files success, {batch_files_err} errors in {batch_elapsed:.1f}s")
                print(f"  Progress: {batch_end}/{len(topics)} ({progress_pct:.1f}%) | {topics_per_sec:.2f} topics/sec | ETA: {eta_sec/60:.1f}min")
                if batch_completed:
                    print(f"  💾 Saved progress: {len(completed_topics)} total completed topics")

        # Final summary
        total_elapsed = time.time() - start_time
        print(f"\n{'='*100}")
        print(f"  COMPLETED IN {total_elapsed/60:.1f} MINUTES")
        print(f"{'='*100}")
        print(f"  Topics processed  : {stats['total_topics']}")
        print(f"  Total API calls   : {stats['total_api_calls']}")
        print(f"  Files generated   : {stats['total_files_success']} / {stats['total_api_calls']} ({stats['total_files_success']*100//stats['total_api_calls'] if stats['total_api_calls'] > 0 else 0}%)")
        print(f"  File errors       : {stats['total_files_errors']}")
        print(f"  Speed             : {stats['total_topics']/total_elapsed:.2f} topics/sec, {stats['total_api_calls']/total_elapsed:.2f} API calls/sec")
        print(f"{'='*100}\n")

        if not args.dry_run and completed_topics:
            print(f"📁 Progress saved to {PROGRESS_FILE}")
            print(f"   To resume: python3 {sys.argv[0]} {args.paths_file} --resume\n")

    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user (Ctrl+C)")
        print(f"   Progress has been saved to {PROGRESS_FILE}")
        print(f"   To resume: python3 {sys.argv[0]} {args.paths_file} --resume")
        sys.exit(0)


if __name__ == "__main__":
    main()
