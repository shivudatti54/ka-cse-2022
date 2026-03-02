#!/usr/bin/env python3
"""
Fix remaining broken files for CG topics.
1. light-and-matter: code.json, memory.json (still has fiber optic content)
2. four-major-tasks: read.md, purpose.md, summary.md, code.json (empty/broken)
"""

import json
import os
import re
import sys
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

API_URL = "https://api.minimax.io/v1/chat/completions"
API_KEY = "sk-cp-r--6hiKCzLgU9QbQREFxR4v336s2kP0vDCeb3x7-iNJxAAdDwQeXhInB8zgfwcduBNoBtQBSj33uci2eCKcCu7q4VjmMGWDhKYHXu_lpv1fmWctproM4cAg"
MODEL = "MiniMax-M2.5"
BASE = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/ka-cse-2022"


def call_api(system_msg, user_msg, max_tokens=8192, retries=3):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
        "temperature": 0.3,
        "max_tokens": max_tokens,
    }).encode("utf-8")

    for attempt in range(retries):
        try:
            print(f"  API call (attempt {attempt+1}, max_tokens={max_tokens})...")
            req = Request(API_URL, data=payload, headers=headers)
            with urlopen(req, timeout=180) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                text = result["choices"][0]["message"]["content"]
                # Strip <think>...</think> blocks from MiniMax M2.5
                text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
                print(f"  Got {len(text)} chars")
                return text
        except HTTPError as e:
            print(f"  HTTP {e.code}")
            if e.code == 429:
                time.sleep(10 * (attempt + 1))
            else:
                time.sleep(5)
        except Exception as e:
            print(f"  Error: {e}")
            time.sleep(5)
    return None


def parse_json(text):
    if not text:
        raise ValueError("Empty response")
    # Strip markdown fences
    if "```json" in text:
        start = text.find("```json") + 7
        end = text.rfind("```")
        if end > start:
            text = text[start:end].strip()
    elif "```" in text:
        start = text.find("```") + 3
        end = text.rfind("```")
        if end > start:
            text = text[start:end].strip()
    # Try direct parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Try extracting JSON object
    brace_start = text.find("{")
    brace_end = text.rfind("}")
    if brace_start != -1 and brace_end > brace_start:
        try:
            return json.loads(text[brace_start:brace_end + 1])
        except json.JSONDecodeError:
            pass
    print(f"  PARSE FAILED. First 300 chars: {text[:300]}")
    raise ValueError("Could not parse JSON")


# ============================================================================
# FIX 1: light-and-matter code.json + memory.json
# ============================================================================
def fix_light_and_matter():
    topic_dir = f"{BASE}/cse/sem-5/bcs515a-computer-graphics/module-4/topics/light-and-matter"
    topic_id = "light-and-matter"
    subject = "Computer Graphics (BCS515A)"
    title = "Light and Matter"
    module = "Module 4: Lighting and Shading"

    system = (
        f"You are an expert CS educator. Generate content ONLY about '{title}' "
        f"in {subject} - illumination models, Phong reflection, ambient/diffuse/specular, "
        f"light sources, shading. NOT about optics, fiber, or physics."
    )

    # -- code.json --
    print("\n[1/2] Generating light-and-matter code.json...")
    user_msg = f"""Generate code examples for: {title} in {subject}

Return JSON:
{{
  "code": [
    {{
      "id": "code-1",
      "language": "pseudocode",
      "title": "Example title",
      "description": "What it demonstrates",
      "code": "// pseudocode here",
      "explanation": "Step by step explanation",
      "timeComplexity": "O(?)",
      "spaceComplexity": "O(?)"
    }}
  ]
}}

Generate 2-3 examples about:
- Phong reflection model calculation (ambient + diffuse + specular)
- Point light attenuation
- Gouraud or Phong shading interpolation

CRITICAL: Computer Graphics illumination code, NOT fiber optics. Return ONLY JSON."""

    resp = call_api(system, user_msg, max_tokens=4096)
    if resp:
        data = parse_json(resp)
        code_data = {"topicId": topic_id, "examples": data.get("code", [])}
        with open(f"{topic_dir}/code.json", "w") as f:
            json.dump(code_data, f, indent=2, ensure_ascii=False)
        print(f"  Wrote code.json ({len(code_data['examples'])} examples)")
    else:
        print("  FAILED code.json")

    time.sleep(2)

    # -- memory.json --
    print("\n[2/2] Generating light-and-matter memory.json...")
    user_msg2 = f"""Generate memory aids for: {title} in {subject}

Return JSON:
{{
  "memory": [
    {{
      "id": "m-1",
      "title": "Mnemonic title",
      "content": "A memorable mnemonic or memory aid"
    }}
  ]
}}

Generate 3-4 mnemonics about:
- Phong reflection components (Ambient, Diffuse, Specular)
- Types of light sources in CG
- Shading models (Flat, Gouraud, Phong)
- Material properties (ka, kd, ks, shininess)

CRITICAL: Computer Graphics illumination, NOT fiber optics or LASER. Return ONLY JSON."""

    resp = call_api(system, user_msg2, max_tokens=2048)
    if resp:
        data = parse_json(resp)
        memory_data = {
            "topicId": topic_id,
            "mnemonics": data.get("memory", []),
            "acronyms": [],
            "visualTips": [],
            "analogies": [],
        }
        with open(f"{topic_dir}/memory.json", "w") as f:
            json.dump(memory_data, f, indent=2, ensure_ascii=False)
        print(f"  Wrote memory.json ({len(memory_data['mnemonics'])} mnemonics)")
    else:
        print("  FAILED memory.json")


# ============================================================================
# FIX 2: four-major-tasks read.md, purpose.md, summary.md, code.json
# ============================================================================
def fix_four_major_tasks():
    topic_dir = f"{BASE}/cse/sem-5/bcs515a-computer-graphics/module-5/topics/four-major-tasks"
    topic_id = "four-major-tasks"
    subject = "Computer Graphics (BCS515A)"
    title = "Four Major Tasks in the Graphics Pipeline"
    module = "Module 5: Implementation"

    system = (
        f"You are an expert CS educator. Generate content ONLY about '{title}' "
        f"in {subject}. The four tasks are: (1) Modeling - creating geometric "
        f"representations, (2) Geometric Processing - transformations/clipping/projection, "
        f"(3) Rasterization - scan conversion/fragment generation, "
        f"(4) Fragment Processing - texturing/blending/framebuffer. "
        f"NOT about OS tasks or any other subject."
    )

    # -- Markdown files --
    print("\n[1/2] Generating four-major-tasks markdown (read.md, purpose.md, summary.md)...")
    user_msg = f"""Generate study material for: {title} in {subject}, {module}

Generate THREE sections separated by these EXACT delimiters:

===READ_MD===
Comprehensive study material (150-250 lines). Include:
- # heading, ## sections
- Detailed explanation of each of the 4 major tasks in the graphics pipeline
- Modeling: geometric representations (polygons, NURBS, subdivision surfaces)
- Geometric Processing: transformations, viewing, clipping, projection
- Rasterization: scan conversion, fragment generation, antialiasing
- Fragment/Display Processing: texturing, blending, depth testing, framebuffer ops
- Diagrams described in text, tables for comparisons
- Real OpenGL/graphics API examples where relevant
Write for university CS students.

===PURPOSE_MD===
5-8 learning objectives using Bloom's taxonomy verbs. Format as bullet points.

===SUMMARY_MD===
20-35 line quick reference card with:
- Key definitions (2-3 lines each)
- Pipeline stages in order
- Comparison table of the 4 tasks
- Must-remember points

===END===

CRITICAL: About COMPUTER GRAPHICS pipeline tasks, NOT operating systems."""

    resp = call_api(system, user_msg, max_tokens=16384)
    if resp:
        # Parse sections
        for fname, start_marker, end_marker in [
            ("read.md", "===READ_MD===", "===PURPOSE_MD==="),
            ("purpose.md", "===PURPOSE_MD===", "===SUMMARY_MD==="),
            ("summary.md", "===SUMMARY_MD===", "===END==="),
        ]:
            si = resp.find(start_marker)
            ei = resp.find(end_marker) if end_marker != "===END===" else resp.find(end_marker)
            if si == -1:
                print(f"  WARNING: {start_marker} not found")
                continue
            content = resp[si + len(start_marker):ei if ei != -1 else len(resp)].strip()
            if len(content) < 50:
                print(f"  WARNING: {fname} too short ({len(content)} chars)")
                continue
            with open(f"{topic_dir}/{fname}", "w") as f:
                f.write(content)
            print(f"  Wrote {fname} ({len(content)} chars)")
    else:
        print("  FAILED markdown generation")

    time.sleep(2)

    # -- code.json --
    print("\n[2/2] Generating four-major-tasks code.json...")
    user_msg2 = f"""Generate code examples for: {title} in {subject}

Return JSON:
{{
  "code": [
    {{
      "id": "code-1",
      "language": "pseudocode",
      "title": "Example title",
      "description": "What it demonstrates",
      "code": "// pseudocode here",
      "explanation": "Step by step explanation",
      "timeComplexity": "O(?)",
      "spaceComplexity": "O(?)"
    }}
  ]
}}

Generate 2 examples about:
- Simple graphics pipeline stage processing (vertex transform → clip → rasterize → fragment)
- Scan line rasterization of a triangle

CRITICAL: Computer Graphics pipeline code, NOT OS code. Return ONLY JSON."""

    resp = call_api(system, user_msg2, max_tokens=4096)
    if resp:
        data = parse_json(resp)
        code_data = {"topicId": topic_id, "examples": data.get("code", [])}
        with open(f"{topic_dir}/code.json", "w") as f:
            json.dump(code_data, f, indent=2, ensure_ascii=False)
        print(f"  Wrote code.json ({len(code_data['examples'])} examples)")
    else:
        print("  FAILED code.json")


if __name__ == "__main__":
    print("=" * 60)
    print("FIXING REMAINING BROKEN FILES")
    print("=" * 60)

    print("\n--- light-and-matter (code.json + memory.json) ---")
    fix_light_and_matter()

    print("\n--- four-major-tasks (read.md + purpose.md + summary.md + code.json) ---")
    fix_four_major_tasks()

    print("\n" + "=" * 60)
    print("DONE")
    print("=" * 60)
