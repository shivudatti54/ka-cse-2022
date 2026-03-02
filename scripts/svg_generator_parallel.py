#!/usr/bin/env python3
"""
Parallel SVG Generator - Creates base SVGs for topics with empty asset dirs
Uses MiniMax-M2.5 API (456B params)

Usage:
  python3 svg_generator_parallel.py <topic-paths-file> [--workers N] [--resume]
"""

import argparse
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

sys.stdout = sys.stderr = open(sys.stdout.fileno(), mode='w', buffering=1)


# ── Context Extraction ────────────────────────────────────────────────────────

def _slug_to_title(slug: str) -> str:
    """Convert a directory slug to a human-readable title.
    E.g. 'bcs502-computer-networks' -> 'Computer Networks'
    """
    cleaned = re.sub(r'^[a-z]{2,5}\d{3}[a-z]?-', '', slug)
    return cleaned.replace('-', ' ').title()


def get_topic_context(topic_path: str) -> dict:
    """Extract subject, module, and topic info from a topic directory path."""
    topic_dir = Path(topic_path)
    topic_slug = topic_dir.name
    context = {
        'topic': topic_slug.replace('-', ' ').title(),
        'topic_slug': topic_slug,
        'module': '',
        'subject': '',
        'sibling_topics': [],
    }
    try:
        module_dir = topic_dir.parent.parent
        module_index = module_dir / '_index.json'
        if module_index.exists():
            with open(module_index) as f:
                mod_data = json.load(f)
            context['module'] = mod_data.get('title', module_dir.name.replace('-', ' ').title())
            for t in mod_data.get('topics', []):
                t_title = t.get('title', t.get('id', ''))
                if t.get('id') == topic_slug:
                    context['topic'] = t_title or context['topic']
                else:
                    context['sibling_topics'].append(t_title)

        subject_dir = module_dir.parent.parent
        subject_index = subject_dir / '_index.json'
        if subject_index.exists():
            with open(subject_index) as f:
                subj_data = json.load(f)
            context['subject'] = subj_data.get('title', _slug_to_title(subject_dir.name))
        else:
            context['subject'] = _slug_to_title(subject_dir.name)
    except Exception:
        for part in topic_dir.parts:
            if re.match(r'^[a-z]{2,5}\d{3}', part):
                context['subject'] = _slug_to_title(part)
                break
    return context


# ── Config ────────────────────────────────────────────────────────────────────
API_KEY = os.environ.get(
    "MINIMAX_API_KEY",
    "sk-cp-r--6hiKCzLgU9QbQREFxR4v336s2kP0vDCeb3x7-iNJxAAdDwQeXhInB8zgfwcduBNoBtQBSj33uci2eCKcCu7q4VjmMGWDhKYHXu_lpv1fmWctproM4cAg"
)
API_URL = "https://api.minimax.io/v1/chat/completions"
MODEL = "MiniMax-M2.5"
MAX_RETRIES = 3

SVG_PROMPT = """\
Create an animated educational SVG diagram for the topic: "{topic_title}"
Subject: {subject}
{siblings_line}
IMPORTANT: This SVG must be specifically about "{topic_title}" in the context of "{subject}". Do not confuse with similarly named topics from other subjects.

Context from study material:
{context}

Requirements:
1. SVG dimensions: width="420" height="400" viewBox="0 0 420 400"
2. Include data-topic-id="{topic_id}" attribute on root <svg>
3. Use gradient background with pastel colors
4. Include 4-6 sections with data-narration attributes explaining each part
5. Add smooth CSS animations using <style> with @keyframes (sequential delays)
6. Use professional color scheme (indigo #4F46E5, teal #0D9488, orange #F59E0B accents)
7. Include clear labels and annotations with readable font sizes (14-16px)
8. Add arrow markers for connections between concepts
9. Include a title at top and brief footer at bottom
10. Make it educational and visually clear - this is for university students

Return ONLY the complete SVG code starting with <svg and ending with </svg>. No explanations, no markdown fences."""


def log(msg):
    print(msg, flush=True)


def call_api(messages, max_retries=MAX_RETRIES):
    """Call MiniMax API with retries."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    for attempt in range(max_retries):
        try:
            data = json.dumps({
                "model": MODEL,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 10000,
            }).encode("utf-8")

            req = Request(API_URL, data=data, headers=headers)
            with urlopen(req, timeout=180) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                return result["choices"][0]["message"]["content"]

        except HTTPError as e:
            if e.code == 429:
                wait = min(30, 5 * (attempt + 1))
                log(f"    Rate limited, waiting {wait}s...")
                time.sleep(wait)
            elif e.code >= 500:
                time.sleep(3)
            else:
                log(f"    HTTP {e.code}")
                return None
        except (URLError, TimeoutError):
            time.sleep(3)
        except Exception as e:
            log(f"    Error: {e}")
            time.sleep(2)

    return None


def extract_svg(text):
    """Extract SVG content from API response."""
    if not text:
        return None
    match = re.search(r'<svg[^>]*>[\s\S]*?</svg>', text, re.IGNORECASE)
    return match.group() if match else None


def read_topic_paths(filepath):
    """Parse topic paths file. Format: number→/path/to/topic or plain paths."""
    topics = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "→" in line:
                parts = line.split("→", 1)
                idx = int(parts[0].strip())
                path = parts[1].strip()
            else:
                idx = len(topics) + 1
                path = line
            topics.append((idx, path))
    return topics


def process_topic(idx, topic_path, progress_file):
    """Generate SVG for a single topic."""
    topic_id = os.path.basename(topic_path)
    assets_dir = os.path.join(topic_path, "assets")
    svg_filename = f"{topic_id}.svg"
    svg_path = os.path.join(assets_dir, svg_filename)

    # Skip if SVG already exists
    if os.path.exists(svg_path) and os.path.getsize(svg_path) > 100:
        return idx, topic_id, "skipped", "SVG exists"

    # Read topic content for context
    read_path = os.path.join(topic_path, "read.md")
    if not os.path.exists(read_path):
        return idx, topic_id, "skipped", "No read.md"

    with open(read_path, "r", errors="replace") as f:
        read_content = f.read()

    # Extract subject context from directory structure
    ctx = get_topic_context(topic_path)
    topic_title = ctx['topic']
    subject = ctx['subject']
    siblings = ctx.get('sibling_topics', [])
    siblings_line = f"Other topics in this module: {', '.join(siblings)}" if siblings else ""
    context = read_content[:2500]

    prompt = SVG_PROMPT.format(
        topic_title=topic_title,
        topic_id=topic_id,
        context=context,
        subject=subject,
        siblings_line=siblings_line,
    )

    response = call_api([{"role": "user", "content": prompt}])
    svg_content = extract_svg(response)

    if svg_content:
        os.makedirs(assets_dir, exist_ok=True)
        with open(svg_path, "w") as f:
            f.write(svg_content)

        # Update visual.json
        visual_json_path = os.path.join(topic_path, "visual.json")
        visual_data = {
            "topicId": topic_id,
            "visuals": [{
                "id": f"{topic_id}-svg",
                "title": topic_title,
                "description": f"Animated diagram for {topic_title}",
                "type": "animated-svg",
                "file": f"assets/{svg_filename}",
                "animated": True,
            }],
        }
        with open(visual_json_path, "w") as f:
            json.dump(visual_data, f, indent=2)

        return idx, topic_id, "success", svg_path
    else:
        return idx, topic_id, "failed", "API returned no valid SVG"


def main():
    parser = argparse.ArgumentParser(description="Parallel SVG Generator (MiniMax-M2.5)")
    parser.add_argument("paths_file", help="Topic paths file")
    parser.add_argument("--workers", type=int, default=10, help="Number of parallel workers (default: 10)")
    parser.add_argument("--resume", action="store_true", help="Skip topics that already have SVGs")
    args = parser.parse_args()

    topics = read_topic_paths(args.paths_file)
    progress_file = Path(args.paths_file).parent / "svg_gen_progress.json"

    log("=" * 70)
    log(f"  SVG GENERATOR (MiniMax-M2.5, 456B)")
    log(f"  Topics: {len(topics)}")
    log(f"  Workers: {args.workers}")
    log("=" * 70)

    stats = {"success": 0, "failed": 0, "skipped": 0}
    failed_topics = []
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(process_topic, idx, path, progress_file): (idx, path)
            for idx, path in topics
        }

        for i, future in enumerate(as_completed(futures), 1):
            try:
                idx, topic_id, status, detail = future.result()
                stats[status] += 1

                if status == "success":
                    log(f"  [{i}/{len(topics)}] ✓ #{idx} {topic_id[:50]}")
                elif status == "failed":
                    log(f"  [{i}/{len(topics)}] ✗ #{idx} {topic_id[:50]} - {detail}")
                    failed_topics.append(futures[future])
                # skipped topics are silent

                # Save progress periodically
                if i % 50 == 0:
                    elapsed = time.time() - start_time
                    rate = (stats["success"] + stats["failed"]) / max(elapsed, 1) * 60
                    log(f"\n  Progress: {stats['success']} ok, {stats['failed']} failed, "
                        f"{stats['skipped']} skipped | {rate:.1f} topics/min\n")

            except Exception as e:
                stats["failed"] += 1
                log(f"  [{i}/{len(topics)}] ERROR: {e}")

    elapsed = time.time() - start_time

    # Save final progress
    progress = {
        "completed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "stats": stats,
        "elapsed_seconds": round(elapsed, 1),
        "failed_topics": [{"idx": idx, "path": path} for idx, path in failed_topics],
    }
    with open(progress_file, "w") as f:
        json.dump(progress, f, indent=2)

    log("\n" + "=" * 70)
    log("  SVG GENERATION COMPLETE")
    log("=" * 70)
    log(f"  Success: {stats['success']}")
    log(f"  Failed:  {stats['failed']}")
    log(f"  Skipped: {stats['skipped']}")
    log(f"  Time:    {elapsed:.0f}s ({elapsed/60:.1f}m)")
    log(f"  Progress file: {progress_file}")
    if failed_topics:
        log(f"\n  {len(failed_topics)} failed topics saved to progress file")
    log("=" * 70)


if __name__ == "__main__":
    main()
