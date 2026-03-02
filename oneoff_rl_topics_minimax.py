#!/usr/bin/env python3
"""
Generate missing Reinforcement Learning topics for ML Module 5.
Calls MiniMax M2.5 once per topic, writes all files, then quality checks.
"""

import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

API_URL = "https://api.minimax.io/anthropic/v1/messages"
MODEL = "MiniMax-M2.5"
MAX_TOKENS = 8192
TIMEOUT = 300

MODULE_DIR = Path("cse/sem-6/bcs602-machine-learning/chapters/module-5")

TOPICS = [
    ("overview-of-reinforcement-learning", "Overview of Reinforcement Learning", 8,
     "Overview of RL: what it is, how agents learn from rewards, trial-and-error, exploration vs exploitation"),
    ("scope-of-reinforcement-learning", "Scope of Reinforcement Learning", 9,
     "Scope: applications (robotics, game playing, autonomous vehicles, recommendation systems, resource management)"),
    ("reinforcement-learning-as-machine-learning", "Reinforcement Learning as Machine Learning", 10,
     "RL vs supervised/unsupervised learning, where RL fits in ML taxonomy, key differences"),
    ("components-of-reinforcement-learning", "Components of Reinforcement Learning", 11,
     "Agent, Environment, State, Action, Reward, Policy, Value Function, Model"),
    ("markov-decision-process", "Markov Decision Process", 12,
     "MDP formulation: states, actions, transition probabilities, rewards, discount factor, Bellman equation"),
    ("multi-arm-bandit-problem", "Multi-Arm Bandit Problem and Reinforcement Problem Types", 13,
     "MAB problem, epsilon-greedy, UCB, Thompson sampling, exploration-exploitation tradeoff, RL problem types"),
    ("model-based-learning", "Model-based Learning", 14,
     "Model-based RL: learning transition/reward models, planning with learned models, Dyna architecture"),
    ("model-free-methods", "Model Free Methods", 15,
     "Model-free RL: Monte Carlo methods, Temporal Difference learning, TD(0), TD(lambda), advantages over model-based"),
    ("q-learning", "Q-Learning", 16,
     "Q-Learning algorithm: off-policy TD control, Q-table, update rule, convergence, epsilon-greedy exploration"),
    ("sarsa-learning", "SARSA Learning", 17,
     "SARSA: on-policy TD control, update rule, comparison with Q-learning, expected SARSA"),
]

SYSTEM_PROMPT = """You are an expert CS professor creating content for a VTU 2022 Scheme study app (BCS602 Machine Learning, Module 5).

Generate content for ONE Reinforcement Learning topic. Return a single JSON object.

OUTPUT FORMAT — Return ONLY valid JSON (no markdown fences, no text outside JSON):

{
  "read_md": "# Topic Title\\n\\n## Introduction\\n\\nFull educational content...",
  "purpose_md": "# Learning Objectives\\n\\nAfter studying this topic, you should be able to:\\n\\n1. ...\\n2. ...",
  "summary_md": "Topic Title\\n================\\n\\n## Overview\\nBrief overview.\\n\\n## Key Points\\n- **Point 1**: ...\\n\\n## Important Concepts\\n- Detail 1\\n\\n## Notes\\n- Quick recall note 1",
  "flashcards": {
    "topicId": "TOPIC_SLUG",
    "flashcards": [
      {"id": "fc1", "front": "Question?", "back": "Answer with key details."}
    ]
  },
  "mcqs": {
    "topicId": "TOPIC_SLUG",
    "questions": [
      {"id": "mcq1", "question": "Question?", "options": ["A", "B", "C", "D"], "correctAnswer": "B", "explanation": "Why B is correct."}
    ]
  },
  "memory": {
    "topicId": "TOPIC_SLUG",
    "mnemonics": [
      {"id": "m1", "title": "Short Mnemonic Name", "content": "Memory aid description."}
    ]
  },
  "questions": {
    "topicId": "TOPIC_SLUG",
    "questions": [
      {"id": "q1", "question": "Long answer question?", "type": "long", "expectedPoints": ["Point 1", "Point 2"]},
      {"id": "q2", "question": "Short answer question?", "type": "short", "expectedPoints": ["Point 1"]}
    ]
  },
  "visual": {
    "topicId": "TOPIC_SLUG",
    "visuals": [],
    "diagrams": [
      {"id": "d1", "title": "Diagram Title", "type": "flow", "content": {"nodes": [{"id": "n1", "label": "Node"}], "edges": [{"from": "n1", "to": "n2"}]}}
    ]
  }
}

CONTENT REQUIREMENTS:
- read_md: 800-1200 words, detailed educational content with examples and formulas. Use bullet lists NOT tables (tables render poorly on mobile). Use markdown headings, bold, bullets.
- purpose_md: 5-6 learning objectives
- summary_md: Concise key points for quick revision
- flashcards: 6-8 cards per topic
- mcqs: 5-6 MCQs with 4 options each, correctAnswer is "A"/"B"/"C"/"D"
- memory: 3-5 mnemonics
- questions: 3-4 exam questions (mix of "long" and "short" types)
- visual: 1-2 diagrams using flow/comparison/process types with nodes and edges

IMPORTANT: Return ONLY the JSON object. No markdown fences. No explanation text."""


def call_minimax(api_key, slug, title, description):
    """Call MiniMax for a single topic."""
    user_msg = (
        f'Generate content for topic: "{title}"\n'
        f'Topic slug (use as topicId): "{slug}"\n'
        f'Content scope: {description}\n\n'
        f'Return ONLY the JSON object.'
    )

    payload = json.dumps({
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": user_msg}],
    }).encode("utf-8")

    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )

    start = time.time()
    resp = urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)
    data = json.loads(resp.read().decode("utf-8"))
    elapsed = time.time() - start

    usage = data.get("usage", {})
    print(f"    API: {elapsed:.1f}s (in:{usage.get('input_tokens', '?')} out:{usage.get('output_tokens', '?')})")

    # Extract text from Anthropic-format response
    text = ""
    for block in data.get("content", []):
        if block.get("type") == "text":
            text += block["text"]

    text = text.strip()
    if text.startswith("```"):
        first_nl = text.index("\n") if "\n" in text else 3
        text = text[first_nl + 1:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

    if not text.startswith("{"):
        start_idx = text.find("{")
        if start_idx != -1:
            text = text[start_idx:]

    return repair_and_parse_json(text)


def repair_and_parse_json(text):
    """Try to parse JSON, repairing common LLM issues if needed."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    fixed = text

    # Fix 1: Literal \n between JSON properties → actual newline
    # The model sometimes outputs backslash+n outside strings
    fixed = fixed.replace(',\\n\\n', ',\n\n').replace(',\\n', ',\n')
    fixed = fixed.replace('{\\n', '{\n').replace('}\\n', '}\n')
    fixed = fixed.replace('[\\n', '[\n').replace(']\\n', ']\n')

    # Fix 2: Remove trailing commas before } or ]
    fixed = re.sub(r',\s*([}\]])', r'\1', fixed)

    # Fix 3: Balance braces (truncated output)
    depth = 0
    for ch in fixed:
        if ch == '{': depth += 1
        elif ch == '}': depth -= 1
    fixed = fixed.rstrip()
    while depth > 0:
        fixed += '}'
        depth -= 1

    try:
        return json.loads(fixed, strict=False)
    except json.JSONDecodeError as e:
        # Save debug file and re-raise
        debug_path = f"/tmp/minimax_debug_{int(time.time())}.json"
        with open(debug_path, "w") as f:
            f.write(text)
        raise ValueError(f"JSON repair failed: {e}. Raw saved to {debug_path}")


def write_topic_files(topic_slug, title, topic_data, topic_dir):
    """Write all files for a single topic. Fills defaults for missing keys."""
    topic_dir.mkdir(parents=True, exist_ok=True)

    # Defaults for truncated responses
    defaults = {
        "read_md": f"# {title}\n\n(Content pending)",
        "purpose_md": f"# Learning Objectives\n\n1. Understand {title}",
        "summary_md": f"{title}\n====\n\n## Overview\n(Summary pending)",
        "flashcards": {"topicId": topic_slug, "flashcards": []},
        "mcqs": {"topicId": topic_slug, "questions": []},
        "memory": {"topicId": topic_slug, "mnemonics": []},
        "questions": {"topicId": topic_slug, "questions": []},
        "visual": {"topicId": topic_slug, "visuals": [], "diagrams": []},
    }

    for key in defaults:
        if key not in topic_data:
            topic_data[key] = defaults[key]
            print(f"    (filled default for missing {key})")

    for name, key in [("read.md", "read_md"), ("purpose.md", "purpose_md"), ("summary.md", "summary_md")]:
        with open(topic_dir / name, "w") as f:
            f.write(topic_data[key])

    for name, key in [("flashcards.json", "flashcards"), ("mcqs.json", "mcqs"),
                       ("memory.json", "memory"), ("questions.json", "questions"),
                       ("visual.json", "visual")]:
        obj = topic_data[key]
        # Fix topicId if wrong
        if isinstance(obj, dict) and "topicId" in obj:
            obj["topicId"] = topic_slug
        with open(topic_dir / name, "w") as f:
            json.dump(obj, f, indent=2, ensure_ascii=False)
            f.write("\n")


def update_index_json(index_path):
    """Add the 10 RL topics to _index.json."""
    with open(index_path) as f:
        index = json.load(f)

    existing_ids = {t["id"] for t in index["topics"]}

    for slug, title, order, _ in TOPICS:
        if slug not in existing_ids:
            index["topics"].append({
                "id": slug,
                "title": title,
                "order": order,
                "estimatedMinutes": 15,
                "hasVisual": True,
                "hasQuestions": True,
            })

    index["topics"].sort(key=lambda t: t.get("order", 0))

    with open(index_path, "w") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Updated _index.json ({len(index['topics'])} topics)")


def quality_check(topic_slug, topic_dir):
    """Quick quality check. Returns list of issues."""
    issues = []

    read_md = (topic_dir / "read.md").read_text()
    if len(read_md.split()) < 200:
        issues.append(f"read.md too short ({len(read_md.split())} words)")

    fc = json.loads((topic_dir / "flashcards.json").read_text())
    if len(fc.get("flashcards", [])) < 3:
        issues.append(f"Only {len(fc.get('flashcards', []))} flashcards")
    if fc.get("topicId") != topic_slug:
        issues.append(f"flashcards topicId mismatch")

    mcqs = json.loads((topic_dir / "mcqs.json").read_text())
    for q in mcqs.get("questions", []):
        if q.get("correctAnswer") not in ("A", "B", "C", "D"):
            issues.append(f"MCQ {q['id']} bad correctAnswer: {q.get('correctAnswer')}")
        if len(q.get("options", [])) != 4:
            issues.append(f"MCQ {q['id']} has {len(q.get('options', []))} options")

    qs = json.loads((topic_dir / "questions.json").read_text())
    if len(qs.get("questions", [])) < 2:
        issues.append(f"Only {len(qs.get('questions', []))} questions")

    return issues


def main():
    api_key = os.environ.get("MINIMAX_API_KEY")
    if not api_key:
        print("ERROR: Set MINIMAX_API_KEY environment variable")
        sys.exit(1)

    base = Path(__file__).resolve().parent
    module_dir = base / MODULE_DIR

    print(f"=== RL Topic Generator (1-by-1) ===")
    print(f"Target: {module_dir}")
    print(f"Topics: {len(TOPICS)}")
    print()

    stats = {"ok": 0, "failed": 0, "skipped": 0}

    for i, (slug, title, order, desc) in enumerate(TOPICS, 1):
        topic_dir = module_dir / "topics" / slug

        # Skip if already exists
        if (topic_dir / "read.md").is_file():
            print(f"[{i}/10] {slug} — SKIP (exists)")
            stats["skipped"] += 1
            continue

        print(f"[{i}/10] {slug}")
        try:
            data = call_minimax(api_key, slug, title, desc)
            write_topic_files(slug, title, data, topic_dir)
            issues = quality_check(slug, topic_dir)
            if issues:
                print(f"    WARN: {issues}")
            else:
                print(f"    OK")
            stats["ok"] += 1
        except Exception as e:
            print(f"    FAILED: {e}")
            stats["failed"] += 1

        # Rate limit courtesy
        if i < len(TOPICS):
            time.sleep(2)

    # Update _index.json
    print()
    update_index_json(module_dir / "_index.json")

    print(f"\n{'=' * 50}")
    print(f"  Generated: {stats['ok']}  Skipped: {stats['skipped']}  Failed: {stats['failed']}")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
