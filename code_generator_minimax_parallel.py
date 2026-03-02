#!/usr/bin/env python3
"""
MiniMax Code Generator — generates code.json for VTU study app topics.

Parallelized version using MiniMax API (MiniMax-M2).

Usage:
    python3 minimax_code_generator.py                          # sequential, reads code_gen_remaining.txt
    python3 minimax_code_generator.py 10                       # 10 parallel workers
    python3 minimax_code_generator.py custom_list.txt 10       # custom file + 10 workers
"""

import json
import os
import ssl
import sys
import time
import threading
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# --- Configuration ---
SCRIPT_DIR = Path(__file__).resolve().parent
ENV_FILE = SCRIPT_DIR / ".minimax.env"

# Load env from .minimax.env
if ENV_FILE.is_file():
    with ENV_FILE.open() as f:
        for line in f:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                key, _, val = line.partition("=")
                val = val.strip().strip("'\"")
                os.environ.setdefault(key.strip(), val)

API_KEY = os.environ.get("MINIMAX_API_KEY", "")
API_URL = os.environ.get("MINIMAX_ENDPOINT", "https://api.minimax.io/v1/text/chatcompletion_v2")
MODEL = os.environ.get("MINIMAX_MODEL", "MiniMax-M2")

MAX_TOKENS = 12000
TEMPERATURE = 0.3
TIMEOUT = 300

BASE_PATH = SCRIPT_DIR / "cse"

VALID_LANGUAGES = {"pseudocode", "python", "c", "java"}

SYSTEM_PROMPT = r"""You are an expert programming instructor creating code examples for a university study app (VTU 2022 Scheme, CSE branch).

Your task: Given a topic's educational content, generate code examples in JSON format.

DECISION PROCESS:
1. Read the topic content carefully.
2. Determine if code examples are applicable:
   - APPLICABLE: algorithms, data structures, programming concepts, mathematical computations, system operations, network protocols, database operations, ML/AI techniques, any concept that can be demonstrated with code
   - NOT APPLICABLE: pure history/biography topics, exam schedules, textbook references, suggested reading lists, course evaluation criteria, purely conceptual overviews with zero algorithmic content
3. When in doubt, generate code. Most CS topics benefit from code examples.

IF APPLICABLE — Generate 3-4 code examples:
- Example 1: **Pseudocode** (MANDATORY) — clean, structured pseudocode showing the algorithm/concept
- Example 2: **Python** implementation
- Example 3: **C** or **Java** implementation (pick whichever is most relevant)
- Example 4 (optional): The other language (C or Java) if both are relevant

IF NOT APPLICABLE — Return JSON with empty examples array.

OUTPUT FORMAT — Return ONLY valid JSON (no markdown fences, no explanation outside JSON):

For applicable topics:
{
  "topicId": "TOPIC_ID_HERE",
  "examples": [
    {
      "id": "pseudocode-descriptive-name",
      "title": "Algorithm: Descriptive Title",
      "description": "What this pseudocode demonstrates",
      "language": "pseudocode",
      "code": "ALGORITHM Name\nINPUT: ...\nOUTPUT: ...\n\nBEGIN\n  step 1\n  step 2\nEND",
      "explanation": "Step-by-step explanation of the algorithm"
    },
    {
      "id": "python-descriptive-name",
      "title": "Python: Descriptive Title",
      "description": "What this implementation demonstrates",
      "language": "python",
      "code": "# Full working Python code\ndef function_name(params):\n    ...",
      "explanation": "Key implementation details and how it relates to the concept",
      "timeComplexity": "O(...)",
      "spaceComplexity": "O(...)"
    },
    {
      "id": "c-descriptive-name",
      "title": "C: Descriptive Title",
      "description": "What this implementation demonstrates",
      "language": "c",
      "code": "#include <stdio.h>\n...",
      "explanation": "Key implementation details",
      "timeComplexity": "O(...)",
      "spaceComplexity": "O(...)"
    }
  ]
}

For NOT applicable topics:
{
  "topicId": "TOPIC_ID_HERE",
  "examples": []
}

RULES:
- "language" must be one of: pseudocode, python, c, java
- Code must be complete, compilable/runnable, and educational
- Include comments in code explaining key steps
- Pseudocode should use clear ALGORITHM/BEGIN/END or similar structured format
- Each code string must be > 10 characters
- The "id" field should be kebab-case: "language-descriptive-name"
- Do NOT wrap the JSON in markdown code fences
- Return ONLY the JSON object, nothing else"""

# Thread-safe stats
_lock = threading.Lock()
stats = {"generated": 0, "skipped": 0, "failed": 0, "not_applicable": 0}


def bump(key):
    with _lock:
        stats[key] += 1


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except (FileNotFoundError, PermissionError):
        return ""


def call_minimax_api(messages, max_retries=3):
    """Call MiniMax API with retries."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    ctx = ssl.create_default_context()

    for attempt in range(1, max_retries + 1):
        try:
            data = json.dumps({
                "model": MODEL,
                "messages": messages,
                "temperature": TEMPERATURE,
                "max_tokens": MAX_TOKENS,
            }).encode("utf-8")

            req = urllib.request.Request(API_URL, data=data, headers=headers, method="POST")
            resp = urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)
            body = json.loads(resp.read().decode("utf-8"))

            # Check MiniMax-specific error codes
            code = body.get("base_resp", {}).get("status_code", 0)
            if code != 0:
                msg = body.get("base_resp", {}).get("status_msg", "unknown")
                raise RuntimeError(f"MiniMax error {code}: {msg}")

            # Extract content — MiniMax uses both reply and choices formats
            text = ""
            if body.get("reply"):
                text = body["reply"]
            elif body.get("choices"):
                text = body["choices"][0].get("message", {}).get("content", "")

            return text

        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = min(5 * attempt, 30)
                time.sleep(wait)
                continue
            if attempt == max_retries:
                raise
            time.sleep(2)
        except Exception:
            if attempt == max_retries:
                raise
            time.sleep(2)

    return None


def extract_json_from_text(text):
    """Parse JSON from API response text."""
    text = text.strip()

    # Strip markdown fences
    if text.startswith("```"):
        first_nl = text.index("\n") if "\n" in text else 3
        text = text[first_nl + 1:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

    # Find JSON object
    if not text.startswith("{"):
        start = text.find("{")
        if start == -1:
            raise ValueError("No JSON object found")
        text = text[start:]

    # Find matching closing brace
    if not text.endswith("}"):
        depth = 0
        for i, ch in enumerate(text):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    text = text[:i + 1]
                    break

    return json.loads(text)


def validate_code_json(data, topic_id):
    """Validate code.json structure. Returns (ok, errors)."""
    errors = []

    if not isinstance(data, dict):
        return False, ["Root is not an object"]

    examples = data.get("examples")
    if not isinstance(examples, list):
        return False, ["'examples' is not an array"]

    if len(examples) == 0:
        return True, []

    has_pseudocode = False
    for i, ex in enumerate(examples):
        prefix = f"examples[{i}]"
        for field in ("id", "title", "language", "code"):
            if not ex.get(field):
                errors.append(f"{prefix} missing '{field}'")

        lang = ex.get("language", "")
        if lang not in VALID_LANGUAGES:
            errors.append(f"{prefix} invalid language '{lang}'")

        code = ex.get("code", "")
        if isinstance(code, str) and len(code) <= 10:
            errors.append(f"{prefix} code too short")

        if lang == "pseudocode":
            has_pseudocode = True

    if not has_pseudocode:
        errors.append("No pseudocode example (mandatory)")

    return len(errors) == 0, errors


def build_user_message(topic_id, topic_dir):
    """Build the user prompt with topic context."""
    read_md = read_file(topic_dir / "read.md")
    purpose_md = read_file(topic_dir / "purpose.md")
    summary_md = read_file(topic_dir / "summary.md")

    if len(read_md) > 8000:
        read_md = read_md[:8000] + "\n... (truncated)"

    parts = [f'Generate code examples for the topic: "{topic_id}"']
    if read_md:
        parts.append(f"== FULL TOPIC CONTENT (read.md) ==\n{read_md}")
    if purpose_md:
        parts.append(f"== LEARNING OBJECTIVE (purpose.md) ==\n{purpose_md}")
    if summary_md:
        parts.append(f"== KEY POINTS (summary.md) ==\n{summary_md}")

    if not read_md and not purpose_md and not summary_md:
        parts.append("(No content files found. Infer from the topic name.)")

    parts.append(f'\nRemember: topicId must be exactly "{topic_id}". Return ONLY JSON.')
    return "\n\n".join(parts)


def process_topic(topic_dir, index, total):
    """Process a single topic. Returns (topic_name, status, detail)."""
    topic_dir = Path(topic_dir)
    topic_id = topic_dir.name
    code_json_path = topic_dir / "code.json"
    label = f"[{index}/{total}]"

    if code_json_path.is_file():
        bump("skipped")
        return topic_id, "skip", "code.json exists"

    has_content = any((topic_dir / f).is_file() for f in ("read.md", "purpose.md", "summary.md"))
    if not has_content:
        bump("skipped")
        return topic_id, "skip", "no content files"

    user_message = build_user_message(topic_id, topic_dir)
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    for attempt in range(1, 3):
        try:
            text = call_minimax_api(messages)
            if not text:
                continue

            data = extract_json_from_text(text)

            # Fix topicId
            if data.get("topicId") != topic_id:
                data["topicId"] = topic_id

            ok, errors = validate_code_json(data, topic_id)

            if ok:
                with open(code_json_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                    f.write("\n")

                n = len(data.get("examples", []))
                if n == 0:
                    bump("not_applicable")
                    return topic_id, "n/a", "not applicable"
                else:
                    langs = [e.get("language") for e in data["examples"]]
                    bump("generated")
                    return topic_id, "ok", f"{n} examples: {', '.join(langs)}"

            # Retry with error feedback
            if attempt == 1:
                messages.append({"role": "assistant", "content": text})
                messages.append({
                    "role": "user",
                    "content": (
                        f"Validation errors:\n"
                        + "\n".join(f"- {e}" for e in errors)
                        + f'\n\nFix these. topicId must be "{topic_id}". Return ONLY JSON.'
                    ),
                })
                continue

            # Second attempt failed — write if structurally sound
            if isinstance(data.get("examples"), list):
                data["topicId"] = topic_id
                with open(code_json_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                    f.write("\n")
                bump("generated")
                return topic_id, "ok", f"wrote with warnings: {errors}"

        except Exception as e:
            if attempt == 1:
                messages = messages[:2]
                continue
            bump("failed")
            return topic_id, "fail", str(e)

    bump("failed")
    return topic_id, "fail", "all attempts exhausted"


def load_topics(path_file):
    """Load topic directory paths from file."""
    topics = []
    seen = set()
    with path_file.open() as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # Handle both SVG paths and topic dir paths
            p = Path(line)
            if p.suffix == ".svg":
                topic_dir = p.parent.parent
            elif p.name == "assets":
                topic_dir = p.parent
            else:
                topic_dir = p

            # Make absolute if relative
            if not topic_dir.is_absolute():
                topic_dir = BASE_PATH / topic_dir

            key = str(topic_dir)
            if key not in seen and topic_dir.is_dir():
                seen.add(key)
                topics.append(topic_dir)
    return topics


def main():
    if not API_KEY:
        print("ERROR: MINIMAX_API_KEY not set. Check .minimax.env")
        sys.exit(1)

    path_file = Path("code_gen_remaining.txt")
    workers = 1

    for arg in sys.argv[1:]:
        if arg.isdigit():
            workers = int(arg)
        else:
            path_file = Path(arg)

    if not path_file.is_file():
        print(f"ERROR: Path file not found: {path_file}")
        sys.exit(1)

    topics = load_topics(path_file)
    total = len(topics)

    print(f"MiniMax Code Generator")
    print(f"Model: {MODEL}")
    print(f"Workers: {workers}")
    print(f"Topics: {total}")
    print(f"{'=' * 60}\n")

    if workers <= 1:
        # Sequential mode
        for i, topic_dir in enumerate(topics, 1):
            name, status, detail = process_topic(topic_dir, i, total)
            sym = {"ok": "✓", "n/a": "○", "skip": "—", "fail": "✗"}.get(status, "?")
            print(f"[{i}/{total}] {sym} {name}  {detail}")
            if status in ("ok", "n/a", "fail"):
                time.sleep(0.5)
    else:
        # Parallel mode
        done = 0
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {
                pool.submit(process_topic, td, i, total): (i, td)
                for i, td in enumerate(topics, 1)
            }
            for future in as_completed(futures):
                done += 1
                name, status, detail = future.result()
                sym = {"ok": "✓", "n/a": "○", "skip": "—", "fail": "✗"}.get(status, "?")
                print(f"[{done}/{total}] {sym} {name}  {detail}")

    print(f"\n{'=' * 60}")
    print(f"  SUMMARY")
    print(f"{'=' * 60}")
    print(f"  Total topics:    {total}")
    print(f"  Generated:       {stats['generated']}")
    print(f"  Not applicable:  {stats['not_applicable']}")
    print(f"  Skipped:         {stats['skipped']}")
    print(f"  Failed:          {stats['failed']}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
