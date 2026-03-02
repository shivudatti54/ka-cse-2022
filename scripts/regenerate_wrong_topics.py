#!/usr/bin/env python3
"""
Regenerate content for 4 topics that have completely wrong content.
Uses MiniMax API (MiniMax-M2.5) to generate correct content.
"""

import json
import os
import sys
import time
import requests

# MiniMax API configuration
API_URL = "https://api.minimax.io/v1/chat/completions"
API_KEY = "sk-cp-r--6hiKCzLgU9QbQREFxR4v336s2kP0vDCeb3x7-iNJxAAdDwQeXhInB8zgfwcduBNoBtQBSj33uci2eCKcCu7q4VjmMGWDhKYHXu_lpv1fmWctproM4cAg"
MODEL = "MiniMax-M2.5"
TEMPERATURE = 0.3

BASE_PATH = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/ka-cse-2022"

# Topics to regenerate
TOPICS = [
    {
        "path": "cse/sem-5/bcs515a-computer-graphics/module-4/topics/light-and-matter",
        "topicId": "light-and-matter",
        "subject": "Computer Graphics (BCS515A)",
        "module": "Module 4: Lighting and Shading",
        "title": "Light and Matter",
        "description": (
            "Light and Matter interaction in Computer Graphics - how light interacts with surfaces, "
            "reflection models (ambient, diffuse, specular), the Phong reflection model, "
            "light sources (point, directional, spotlight), material properties, shading equations, "
            "rendering equation basics. This is about COMPUTER GRAPHICS illumination models, "
            "NOT physics optics or optical fiber communication."
        ),
        "has_code": True,
    },
    {
        "path": "cse/sem-5/bcs515a-computer-graphics/module-5/topics/four-major-tasks",
        "topicId": "four-major-tasks",
        "subject": "Computer Graphics (BCS515A)",
        "module": "Module 5: Implementation",
        "title": "Four Major Tasks in the Graphics Pipeline",
        "description": (
            "Four Major Tasks in the Computer Graphics Pipeline: "
            "1) Modeling (creating geometric representations of objects), "
            "2) Geometric Processing (transformations, clipping, projection), "
            "3) Rasterization (scan conversion, fragment generation), "
            "4) Fragment/Display Processing (texturing, blending, framebuffer operations). "
            "This is about the COMPUTER GRAPHICS rendering pipeline, NOT operating system tasks."
        ),
        "has_code": True,
    },
    {
        "path": "cse/sem-5/bcs515a-computer-graphics/module-5/topics/basic-implementation-strategies",
        "topicId": "basic-implementation-strategies",
        "subject": "Computer Graphics (BCS515A)",
        "module": "Module 5: Implementation",
        "title": "Basic Implementation Strategies",
        "description": (
            "Basic Implementation Strategies for Computer Graphics rendering: "
            "scan line algorithms, z-buffer (depth buffer) method, painter's algorithm, "
            "BSP trees, pipeline architecture for rendering, hardware vs software rendering, "
            "display lists, immediate mode vs retained mode rendering. "
            "This is about COMPUTER GRAPHICS rendering strategies, NOT data structures or general algorithm strategies."
        ),
        "has_code": True,
    },
    {
        "path": "cse/sem-5/bcs515b-artificial-intelligence/module-1/topics/the-nature-of-environment",
        "topicId": "the-nature-of-environment",
        "subject": "Artificial Intelligence (BCS515B)",
        "module": "Module 1: Introduction to AI",
        "title": "The Nature of Environment",
        "description": (
            "The Nature of Environment in AI agent design (from Russell & Norvig textbook): "
            "fully vs partially observable, deterministic vs stochastic, "
            "episodic vs sequential, static vs dynamic, discrete vs continuous, "
            "single-agent vs multi-agent, known vs unknown environments, "
            "with real-world examples for each type. "
            "This is about AI AGENT ENVIRONMENTS, NOT environmental science or ecology."
        ),
        "has_code": False,
    },
]


def call_minimax(system_prompt: str, user_prompt: str, max_tokens: int, retries: int = 3) -> str:
    """Call MiniMax API and return the response text."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": TEMPERATURE,
        "max_tokens": max_tokens,
    }

    for attempt in range(retries):
        try:
            print(f"    API call (attempt {attempt + 1}/{retries}, max_tokens={max_tokens})...")
            resp = requests.post(API_URL, headers=headers, json=payload, timeout=180)
            resp.raise_for_status()
            data = resp.json()
            if "choices" in data and len(data["choices"]) > 0:
                text = data["choices"][0]["message"]["content"]
                print(f"    Response received: {len(text)} chars")
                return text
            else:
                print(f"    WARNING: No choices in response: {json.dumps(data)[:200]}")
        except requests.exceptions.Timeout:
            print(f"    TIMEOUT on attempt {attempt + 1}")
        except requests.exceptions.HTTPError as e:
            print(f"    HTTP Error: {e}")
            print(f"    Response body: {resp.text[:500]}")
        except Exception as e:
            print(f"    Error: {e}")

        if attempt < retries - 1:
            wait = (attempt + 1) * 10
            print(f"    Retrying in {wait}s...")
            time.sleep(wait)

    raise RuntimeError("All API call attempts failed")


def parse_markdown_response(text: str, topic_id: str):
    """Parse the markdown response into read.md, purpose.md, summary.md."""
    files = {}

    markers = {
        "read.md": ("===READ_MD===", "===PURPOSE_MD==="),
        "purpose.md": ("===PURPOSE_MD===", "===SUMMARY_MD==="),
        "summary.md": ("===SUMMARY_MD===", "===END==="),
    }

    for filename, (start_marker, end_marker) in markers.items():
        start_idx = text.find(start_marker)
        end_idx = text.find(end_marker)

        if start_idx == -1:
            print(f"    WARNING: Could not find {start_marker}")
            files[filename] = f"# {topic_id}\n\nContent generation failed - marker not found."
            continue

        content = text[start_idx + len(start_marker):end_idx if end_idx != -1 else len(text)]
        content = content.strip()
        files[filename] = content

    return files


def parse_json_response(text: str, topic_id: str):
    """Extract JSON from a response that may contain markdown code fences."""
    cleaned = text.strip()

    if "```json" in cleaned:
        start = cleaned.find("```json") + len("```json")
        end = cleaned.rfind("```")
        if end > start:
            cleaned = cleaned[start:end].strip()
    elif "```" in cleaned:
        start = cleaned.find("```") + 3
        end = cleaned.rfind("```")
        if end > start:
            cleaned = cleaned[start:end].strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        brace_start = cleaned.find("{")
        brace_end = cleaned.rfind("}")
        if brace_start != -1 and brace_end != -1:
            try:
                return json.loads(cleaned[brace_start:brace_end + 1])
            except json.JSONDecodeError:
                pass
        print(f"    ERROR: Could not parse JSON: {e}")
        print(f"    First 300 chars: {cleaned[:300]}")
        raise


def process_topic(topic: dict):
    """Process a single topic: make API calls and write files."""
    topic_dir = os.path.join(BASE_PATH, topic["path"])
    topic_id = topic["topicId"]
    subject = topic["subject"]
    title = topic["title"]
    description = topic["description"]
    module = topic["module"]

    print(f"\n{'='*70}")
    print(f"PROCESSING: {subject} / {title}")
    print(f"  Path: {topic_dir}")
    print(f"{'='*70}")

    if not os.path.isdir(topic_dir):
        print(f"  ERROR: Directory does not exist: {topic_dir}")
        return False

    # =========================================================================
    # CALL 1: Markdown files (read.md, purpose.md, summary.md)
    # =========================================================================
    print("\n  [CALL 1] Generating markdown files...")

    system_prompt_md = (
'CRITICAL OUTPUT RULES (MUST follow):\n- Output ONLY in English. Never use Chinese, Japanese, Korean, or any non-Latin characters.\n- Do NOT start with conversational preambles like "Of course", "Sure", "Certainly", "Here is a comprehensive", etc. Start directly with the content.\n- Do NOT include metadata headers like "Subject:", "Module:", "Topic:" in the content body.\n- Do NOT mention the target audience scope (no "B.Tech", "MSc", "MCA", "engineering students", "undergraduate students"). Write as if the reader is simply a student studying this topic.\n- For memory aids/mnemonics: Do NOT use markdown bold (**text**). Use UPPERCASE for emphasis instead. ' +

        f"You are an expert educational content writer for a university Computer Science study app. "
        f"IMPORTANT: Generate content ONLY about '{title}' as it relates to {subject}. "
        f"Do NOT confuse with similarly named topics from other subjects. "
        f"The topic is part of {module} in the {subject} course."
    )

    user_prompt_md = f"""Generate educational content for the following topic:

Subject: {subject}
Module: {module}
Topic: {title}
Topic Description: {description}

Generate THREE sections separated by these EXACT delimiters (each on its own line):

===READ_MD===
A comprehensive study material document (150-300 lines). Include:
- Clear topic heading with # 
- Multiple sections with ## headings
- Detailed explanations with examples
- Key formulas/equations where applicable
- Tables for comparisons where useful
- Code blocks or pseudocode where relevant
- Real-world applications and examples
- Important points highlighted with **bold**
- Bullet points and numbered lists for clarity
Write it as if explaining to a university student studying {subject}.

===PURPOSE_MD===
5-8 learning objectives using Bloom's taxonomy verbs (Understand, Analyze, Apply, Evaluate, Create). Format:
- Each objective as a bullet point starting with an action verb
- Cover different cognitive levels
- Be specific to this topic

===SUMMARY_MD===
A 20-35 line quick reference card including:
- Key definitions (2-3 lines each)
- Important formulas or rules
- Quick comparison tables
- Must-remember points
- Use bullet points and bold for key terms

===END===

CRITICAL: All content must be about {title} in the context of {subject}. NOT about any other subject."""

    md_response = call_minimax(system_prompt_md, user_prompt_md, max_tokens=16384)
    md_files = parse_markdown_response(md_response, topic_id)

    for filename, content in md_files.items():
        filepath = os.path.join(topic_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"    Wrote {filename} ({len(content)} chars)")

    time.sleep(2)

    # =========================================================================
    # CALL 2: Assessment JSON (flashcards, mcqs, questions)
    # =========================================================================
    print("\n  [CALL 2] Generating assessment JSON (flashcards, mcqs, questions)...")

    system_prompt_json = (
        f"You are an expert educational content writer for a university Computer Science study app. "
        f"IMPORTANT: Generate content ONLY about '{title}' as it relates to {subject}. "
        f"Do NOT confuse with similarly named topics from other subjects. "
        f"The topic is part of {module} in the {subject} course. "
        f"You MUST return ONLY valid JSON with no extra text or markdown fences."
    )

    user_prompt_assessment = f"""Generate assessment content for:
Subject: {subject}
Module: {module}  
Topic: {title}
Topic Description: {description}

Return a SINGLE JSON object with these keys:

{{
  "flashcards": [
    {{
      "id": "fc-1",
      "front": "Question about {title} in {subject}",
      "back": "Answer with explanation"
    }}
  ],
  "mcqs": [
    {{
      "id": "mcq-1",
      "question": "Question about {title} in {subject}?",
      "options": [
        {{"key": "A", "text": "Option A"}},
        {{"key": "B", "text": "Option B"}},
        {{"key": "C", "text": "Option C"}},
        {{"key": "D", "text": "Option D"}}
      ],
      "correctAnswer": "The correct option text exactly",
      "explanation": "Why this is correct",
      "difficulty": "easy|medium|hard"
    }}
  ],
  "questions": [
    {{
      "id": "q-1",
      "type": "short",
      "question": "Descriptive question about {title}",
      "marks": 5,
      "difficulty": "medium",
      "keyPoints": ["point 1", "point 2", "point 3", "point 4"]
    }}
  ]
}}

Requirements:
- flashcards: 6-8 items
- mcqs: 8-10 items with 4 options each, mix of easy/medium/hard
- questions: 4-5 items with keyPoints arrays

CRITICAL: All content must be about {title} in {subject} context. Return ONLY the JSON object."""

    assessment_response = call_minimax(system_prompt_json, user_prompt_assessment, max_tokens=8192)
    assessment_data = parse_json_response(assessment_response, topic_id)

    # Write flashcards.json
    flashcards_data = {"topicId": topic_id, "flashcards": assessment_data.get("flashcards", [])}
    filepath = os.path.join(topic_dir, "flashcards.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(flashcards_data, f, indent=2, ensure_ascii=False)
    print(f"    Wrote flashcards.json ({len(flashcards_data['flashcards'])} items)")

    # Write mcqs.json
    mcqs_data = {"topicId": topic_id, "mcqs": assessment_data.get("mcqs", [])}
    filepath = os.path.join(topic_dir, "mcqs.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(mcqs_data, f, indent=2, ensure_ascii=False)
    print(f"    Wrote mcqs.json ({len(mcqs_data['mcqs'])} items)")

    # Write questions.json
    questions_data = {"topicId": topic_id, "questions": assessment_data.get("questions", [])}
    filepath = os.path.join(topic_dir, "questions.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(questions_data, f, indent=2, ensure_ascii=False)
    print(f"    Wrote questions.json ({len(questions_data['questions'])} items)")

    time.sleep(2)

    # =========================================================================
    # CALL 3: Remaining JSON (memory, visual, code)
    # =========================================================================
    print("\n  [CALL 3] Generating remaining JSON (memory, visual, code)...")

    if topic["has_code"]:
        code_instruction = f'''"code": [
    {{
      "id": "code-1",
      "language": "pseudocode",
      "title": "Example title related to {title}",
      "description": "What this code demonstrates",
      "code": "ALGORITHM Name\\nBEGIN\\n    // pseudocode here\\nEND",
      "explanation": "Step by step explanation",
      "timeComplexity": "O(?)",
      "spaceComplexity": "O(?)"
    }}
  ]'''
    else:
        code_instruction = '"code": []'

    user_prompt_remaining = f"""Generate supplementary content for:
Subject: {subject}
Module: {module}
Topic: {title}
Topic Description: {description}

Return a SINGLE JSON object with these keys:

{{
  "memory": [
    {{
      "id": "m-1",
      "title": "Mnemonic title",
      "content": "A memorable mnemonic, acronym, or memory aid for a key concept in {title}"
    }}
  ],
  "visual": {{
    "visuals": [
      {{
        "id": "{topic_id}-svg",
        "title": "{title}",
        "description": "Visual diagram for {title}",
        "type": "animated-svg",
        "file": "assets/{topic_id}.svg",
        "svgContent": "<placeholder>",
        "animated": true
      }}
    ],
    "diagrams": [
      {{
        "id": "d-1",
        "title": "Diagram title relevant to {title}",
        "description": "What this diagram shows",
        "elements": ["element1", "element2", "element3"],
        "purpose": "Why this diagram helps understanding"
      }}
    ]
  }},
  {code_instruction}
}}

Requirements:
- memory: 2-3 mnemonics
- visual.diagrams: 3-4 diagram descriptions
- code: {'1-2 pseudocode examples' if topic["has_code"] else 'empty array'}

CRITICAL: All content must be about {title} in {subject} context. Return ONLY the JSON object."""

    remaining_response = call_minimax(system_prompt_json, user_prompt_remaining, max_tokens=4096)
    remaining_data = parse_json_response(remaining_response, topic_id)

    # Write memory.json
    memory_items = remaining_data.get("memory", [])
    memory_data = {
        "topicId": topic_id,
        "mnemonics": memory_items,
        "acronyms": [],
        "visualTips": [],
        "analogies": [],
    }
    filepath = os.path.join(topic_dir, "memory.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(memory_data, f, indent=2, ensure_ascii=False)
    print(f"    Wrote memory.json ({len(memory_items)} mnemonics)")

    # Write visual.json
    visual_data_raw = remaining_data.get("visual", {})
    visual_data = {
        "topicId": topic_id,
        "diagrams": visual_data_raw.get("diagrams", []),
        "visuals": visual_data_raw.get("visuals", [
            {
                "id": f"{topic_id}-svg",
                "title": title,
                "description": f"Visual diagram for {title}",
                "type": "animated-svg",
                "file": f"assets/{topic_id}.svg",
                "svgContent": "<placeholder>",
                "animated": True,
            }
        ]),
    }
    filepath = os.path.join(topic_dir, "visual.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(visual_data, f, indent=2, ensure_ascii=False)
    print(f"    Wrote visual.json ({len(visual_data['diagrams'])} diagrams)")

    # Write code.json
    code_items = remaining_data.get("code", [])
    code_data = {"topicId": topic_id, "examples": code_items}
    filepath = os.path.join(topic_dir, "code.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(code_data, f, indent=2, ensure_ascii=False)
    print(f"    Wrote code.json ({len(code_items)} examples)")

    return True


def verify_all_files():
    """Verify all generated files exist and JSON files are valid."""
    print(f"\n{'='*70}")
    print("VERIFICATION")
    print(f"{'='*70}")

    all_ok = True
    required_files = [
        "read.md", "purpose.md", "summary.md",
        "flashcards.json", "mcqs.json", "questions.json",
        "memory.json", "visual.json", "code.json",
    ]

    for topic in TOPICS:
        topic_dir = os.path.join(BASE_PATH, topic["path"])
        print(f"\n  {topic['subject']} / {topic['title']}:")

        for filename in required_files:
            filepath = os.path.join(topic_dir, filename)
            if not os.path.exists(filepath):
                print(f"    MISSING: {filename}")
                all_ok = False
                continue

            size = os.path.getsize(filepath)
            if size < 50:
                print(f"    TOO SMALL: {filename} ({size} bytes)")
                all_ok = False
                continue

            if filename.endswith(".json"):
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    if data.get("topicId") != topic["topicId"]:
                        print(f"    WRONG topicId in {filename}: {data.get('topicId')}")
                        all_ok = False
                    else:
                        print(f"    OK: {filename} ({size} bytes)")
                except json.JSONDecodeError as e:
                    print(f"    INVALID JSON: {filename} - {e}")
                    all_ok = False
            else:
                print(f"    OK: {filename} ({size} bytes)")

    return all_ok


def main():
    print("=" * 70)
    print("REGENERATING WRONG CONTENT FOR 4 TOPICS")
    print(f"API: MiniMax ({MODEL})")
    print(f"Temperature: {TEMPERATURE}")
    print("=" * 70)

    success_count = 0
    fail_count = 0

    for i, topic in enumerate(TOPICS, 1):
        print(f"\n[{i}/{len(TOPICS)}] Starting: {topic['title']}")
        try:
            result = process_topic(topic)
            if result:
                success_count += 1
                print(f"\n  SUCCESS: {topic['title']}")
            else:
                fail_count += 1
                print(f"\n  FAILED: {topic['title']}")
        except Exception as e:
            fail_count += 1
            print(f"\n  ERROR processing {topic['title']}: {e}")
            import traceback
            traceback.print_exc()

        if i < len(TOPICS):
            print("\n  Waiting 3s before next topic...")
            time.sleep(3)

    all_ok = verify_all_files()

    print(f"\n{'='*70}")
    print(f"SUMMARY: {success_count} succeeded, {fail_count} failed")
    print(f"Verification: {'ALL OK' if all_ok else 'SOME ISSUES FOUND'}")
    print(f"{'='*70}")

    return 0 if (fail_count == 0 and all_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
