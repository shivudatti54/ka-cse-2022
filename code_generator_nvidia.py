#!/usr/bin/env python3
"""
NVIDIA Code Generator — generates code.json for VTU study app topics.

Reads topic paths from svg_path.txt, calls NVIDIA API to generate code examples
(Pseudocode + Python + C/Java), and writes code.json files.

Usage:
    export NVIDIA_API_KEY="nvapi-..."
    python3 nvidia_code_generator.py                    # uses svg_path.txt
    python3 nvidia_code_generator.py custom_list.txt    # custom path list

Requires: NVIDIA_API_KEY environment variable
"""

import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

# --- Configuration ---
API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
PRIMARY_MODEL = "meta/llama-3.1-405b-instruct"
FALLBACK_MODEL = "meta/llama-3.1-405b-instruct"
MAX_TOKENS = 12000
TEMPERATURE = 0.3
TIMEOUT = 300  # seconds

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


def read_file(path):
    """Read a file, return empty string if not found."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except (FileNotFoundError, PermissionError):
        return ""


def call_nvidia_api(api_key, messages, model=PRIMARY_MODEL):
    """Call NVIDIA API and return the parsed response dict."""
    payload = json.dumps({
        "model": model,
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
        "messages": messages,
    }).encode("utf-8")

    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )

    resp = urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)
    return json.loads(resp.read().decode("utf-8"))


def extract_json_from_response(response):
    """Extract the text content from the NVIDIA API response and parse as JSON."""
    text = response.get("choices", [{}])[0].get("message", {}).get("content", "")
    text = text.strip()

    # Strip markdown fences if present
    if text.startswith("```"):
        # Remove opening fence (```json or ```)
        first_newline = text.index("\n") if "\n" in text else 3
        text = text[first_newline + 1:]
        # Remove closing fence
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

    # Sometimes models wrap in extra text — find the JSON object
    if not text.startswith("{"):
        start = text.find("{")
        if start != -1:
            text = text[start:]
        else:
            raise ValueError("No JSON object found in response")

    # Find matching closing brace
    if not text.endswith("}"):
        # Find the last } that could close the top-level object
        depth = 0
        end = -1
        for i, ch in enumerate(text):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end = i
                    break
        if end != -1:
            text = text[:end + 1]

    return json.loads(text)


def validate_code_json(data, topic_id):
    """Validate code.json against the TopicCode schema. Returns (ok, errors)."""
    errors = []

    if not isinstance(data, dict):
        return False, ["Root is not an object"]

    if data.get("topicId") != topic_id:
        errors.append(f"topicId mismatch: expected '{topic_id}', got '{data.get('topicId')}'")

    examples = data.get("examples")
    if not isinstance(examples, list):
        return False, ["'examples' is not an array"]

    # Empty examples is valid (not-applicable topic)
    if len(examples) == 0:
        return len(errors) == 0, errors

    has_pseudocode = False
    for i, ex in enumerate(examples):
        prefix = f"examples[{i}]"
        for field in ("id", "title", "language", "code"):
            if not ex.get(field):
                errors.append(f"{prefix} missing required field '{field}'")

        lang = ex.get("language", "")
        if lang not in VALID_LANGUAGES:
            errors.append(f"{prefix} invalid language '{lang}' (must be one of {VALID_LANGUAGES})")

        code = ex.get("code", "")
        if isinstance(code, str) and len(code) <= 10:
            errors.append(f"{prefix} code too short ({len(code)} chars, need > 10)")

        if lang == "pseudocode":
            has_pseudocode = True

    if not has_pseudocode:
        errors.append("No pseudocode example found (mandatory)")

    return len(errors) == 0, errors


def build_user_message(topic_id, topic_dir):
    """Build the user message with topic context."""
    read_md = read_file(topic_dir / "read.md")
    purpose_md = read_file(topic_dir / "purpose.md")
    summary_md = read_file(topic_dir / "summary.md")

    # Truncate very long content to stay within token limits
    max_content = 8000
    if len(read_md) > max_content:
        read_md = read_md[:max_content] + "\n... (truncated)"

    parts = [f'Generate code examples for the topic: "{topic_id}"']
    if read_md:
        parts.append(f"== FULL TOPIC CONTENT (read.md) ==\n{read_md}")
    if purpose_md:
        parts.append(f"== LEARNING OBJECTIVE (purpose.md) ==\n{purpose_md}")
    if summary_md:
        parts.append(f"== KEY POINTS (summary.md) ==\n{summary_md}")

    if not read_md and not purpose_md and not summary_md:
        parts.append("(No topic content files found. Infer from the topic name.)")

    parts.append(f'\nRemember: topicId must be exactly "{topic_id}". Return ONLY JSON.')

    return "\n\n".join(parts)


def process_topic(api_key, topic_dir, stats):
    """Process a single topic: generate and write code.json."""
    topic_id = topic_dir.name
    code_json_path = topic_dir / "code.json"

    # Skip if already exists
    if code_json_path.is_file():
        stats["skipped"] += 1
        print(f"  SKIP (code.json exists)")
        return

    # Check we have at least some content
    has_content = any(
        (topic_dir / f).is_file()
        for f in ("read.md", "purpose.md", "summary.md")
    )
    if not has_content:
        stats["skipped"] += 1
        print(f"  SKIP (no content files)")
        return

    user_message = build_user_message(topic_id, topic_dir)
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    # Try primary model, then fallback
    for attempt, model in enumerate([PRIMARY_MODEL, FALLBACK_MODEL], 1):
        try:
            print(f"  Calling {model} (attempt {attempt})...")
            start = time.time()
            response = call_nvidia_api(api_key, messages, model)
            elapsed = time.time() - start

            usage = response.get("usage", {})
            print(f"  API response in {elapsed:.1f}s "
                  f"(in:{usage.get('prompt_tokens', '?')} out:{usage.get('completion_tokens', '?')})")

            data = extract_json_from_response(response)

            # Fix topicId if mismatched
            if data.get("topicId") != topic_id:
                data["topicId"] = topic_id

            ok, errors = validate_code_json(data, topic_id)
            if ok:
                with open(code_json_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                    f.write("\n")

                n_examples = len(data.get("examples", []))
                if n_examples == 0:
                    stats["not_applicable"] += 1
                    print(f"  WROTE code.json (not applicable — empty examples)")
                else:
                    langs = [e.get("language") for e in data["examples"]]
                    stats["generated"] += 1
                    print(f"  WROTE code.json ({n_examples} examples: {', '.join(langs)})")
                return

            # Validation failed — retry with error feedback
            print(f"  Validation errors: {errors}")
            if attempt == 1:
                print(f"  Retrying with error feedback...")
                messages.append({"role": "assistant", "content": json.dumps(data)})
                messages.append({
                    "role": "user",
                    "content": (
                        f"The JSON has validation errors:\n"
                        + "\n".join(f"- {e}" for e in errors)
                        + f"\n\nFix these issues. topicId must be exactly \"{topic_id}\". "
                        "Return ONLY the corrected JSON."
                    ),
                })
                continue

            # Second attempt also failed — write what we have if it's structurally sound
            if isinstance(data.get("examples"), list):
                data["topicId"] = topic_id
                with open(code_json_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                    f.write("\n")
                stats["generated"] += 1
                print(f"  WROTE code.json (with warnings: {errors})")
                return

        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            print(f"  HTTP error with {model}: {e}")
            if attempt == 1:
                print(f"  Falling back to {FALLBACK_MODEL}...")
                messages = messages[:2]  # Reset to original messages
                continue
        except (json.JSONDecodeError, ValueError, KeyError) as e:
            print(f"  Parse error: {e}")
            if attempt == 1:
                print(f"  Retrying with {FALLBACK_MODEL}...")
                messages = messages[:2]
                continue
        except Exception as e:
            print(f"  Unexpected error: {e}")
            if attempt == 1:
                messages = messages[:2]
                continue

    stats["failed"] += 1
    print(f"  FAILED after all attempts")


def main():
    api_key = os.environ.get("NVIDIA_API_KEY")
    if not api_key:
        print("ERROR: Set NVIDIA_API_KEY environment variable")
        print("  export NVIDIA_API_KEY='nvapi-...'")
        sys.exit(1)

    path_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("svg_path.txt")
    if not path_file.is_file():
        print(f"ERROR: Path file not found: {path_file}")
        sys.exit(1)

    # Parse topic dirs from SVG paths
    topic_dirs = []
    with path_file.open() as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # SVG path -> topic dir: .../topics/foo/assets/foo.svg -> .../topics/foo
            topic_dir = Path(line).parent.parent
            if topic_dir.is_dir() and topic_dir not in topic_dirs:
                topic_dirs.append(topic_dir)

    print(f"NVIDIA Code Generator")
    print(f"Model: {PRIMARY_MODEL} (fallback: {FALLBACK_MODEL})")
    print(f"Topics found: {len(topic_dirs)}")
    print(f"{'=' * 60}\n")

    stats = {"generated": 0, "skipped": 0, "failed": 0, "not_applicable": 0}
    total = len(topic_dirs)

    for i, topic_dir in enumerate(topic_dirs, 1):
        print(f"[{i}/{total}] {topic_dir.name}")
        try:
            process_topic(api_key, topic_dir, stats)
        except KeyboardInterrupt:
            print("\n\nInterrupted by user.")
            break
        except Exception as e:
            print(f"  ERROR: {e}")
            stats["failed"] += 1

        # Small delay between API calls to respect rate limits
        if i < total and stats.get("_last_was_skip") is not True:
            time.sleep(1)

    # Summary
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
