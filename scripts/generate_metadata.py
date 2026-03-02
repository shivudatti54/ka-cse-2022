#!/usr/bin/env python3
"""
Generate _meta.json and _index.json files for all subjects/modules in a content directory.
Scans directory structure and creates metadata files where missing.

Usage:
  python3 generate_metadata.py <content-dir> [--branch <branch-name>]
  python3 generate_metadata.py /path/to/BCA/content --branch bca
"""

import argparse
import json
import os
import re
from pathlib import Path


def slugify_to_title(slug):
    """Convert slug to title case: 'data-structures-and-applications' -> 'Data Structures And Applications'"""
    return slug.replace("-", " ").title()


def extract_subject_code(dirname):
    """Extract subject code from directory name like 'bcs301-mathematics-for-computer-science' -> 'BCS301'"""
    match = re.match(r'^([a-zA-Z]+\d+[a-zA-Z]?)-', dirname)
    if match:
        return match.group(1).upper()
    return dirname.upper()[:8]


def extract_subject_name(dirname):
    """Extract subject name from directory name."""
    match = re.match(r'^[a-zA-Z]+\d+[a-zA-Z]?-(.+)$', dirname)
    if match:
        return slugify_to_title(match.group(1))
    return slugify_to_title(dirname)


def extract_semester(sem_dir):
    """Extract semester number from 'sem-3' -> 3"""
    match = re.match(r'sem-(\d+)', sem_dir)
    return int(match.group(1)) if match else 0


def extract_module_order(module_dir):
    """Extract module number from 'module-1' -> 1"""
    match = re.match(r'module-(\d+)', module_dir)
    return int(match.group(1)) if match else 0


def has_questions(topic_dir):
    """Check if a topic has question files."""
    return any((topic_dir / f).exists() for f in ["mcqs.json", "questions.json"])


def has_visual(topic_dir):
    """Check if a topic has visual content."""
    assets_dir = topic_dir / "assets"
    if assets_dir.is_dir():
        return any(assets_dir.glob("*.svg"))
    return False


def get_module_title_from_content(module_dir):
    """Try to extract module title from existing _index.json or first topic's read.md."""
    index_file = module_dir / "_index.json"
    if index_file.exists():
        try:
            data = json.loads(index_file.read_text())
            return data.get("chapterTitle", "")
        except Exception:
            pass
    return ""


def generate_module_index(module_dir, module_id):
    """Generate _index.json for a module directory."""
    topics_dir = module_dir / "topics"
    if not topics_dir.is_dir():
        return None

    topics = []
    for i, topic_dir in enumerate(sorted(topics_dir.iterdir()), 1):
        if not topic_dir.is_dir():
            continue
        if not (topic_dir / "read.md").exists():
            continue

        topic_id = topic_dir.name
        topics.append({
            "id": topic_id,
            "title": slugify_to_title(topic_id),
            "order": i,
            "estimatedMinutes": 15,
            "hasVisual": has_visual(topic_dir),
            "hasQuestions": has_questions(topic_dir),
        })

    if not topics:
        return None

    title = get_module_title_from_content(module_dir)
    if not title:
        title = f"Module {extract_module_order(module_id)}"

    return {
        "chapterId": module_id,
        "chapterTitle": title,
        "hasTopics": True,
        "topics": topics,
    }


def generate_subject_index(subject_dir):
    """Generate subject-level _index.json listing all modules."""
    chapters = []
    for module_dir in sorted(subject_dir.iterdir()):
        if not module_dir.is_dir() or not module_dir.name.startswith("module-"):
            continue

        module_id = module_dir.name
        topics_dir = module_dir / "topics"
        topic_count = 0
        if topics_dir.is_dir():
            topic_count = sum(1 for t in topics_dir.iterdir()
                              if t.is_dir() and (t / "read.md").exists())

        if topic_count == 0:
            continue

        title = get_module_title_from_content(module_dir)
        if not title:
            title = f"Module {extract_module_order(module_id)}"

        chapters.append({
            "id": module_id,
            "title": title,
            "order": extract_module_order(module_id),
            "topicCount": topic_count,
            "hasTopics": True,
        })

    return {"chapters": chapters} if chapters else None


def generate_meta(subject_dir, semester, branch):
    """Generate _meta.json for a subject directory."""
    dirname = subject_dir.name
    return {
        "code": extract_subject_code(dirname),
        "name": extract_subject_name(dirname),
        "semester": semester,
        "branch": branch,
    }


def process_content_dir(content_dir, branch):
    """Process all subjects in a content directory and generate missing metadata."""
    content_path = Path(content_dir)
    stats = {"meta_created": 0, "meta_skipped": 0, "index_created": 0, "index_skipped": 0}

    for sem_dir in sorted(content_path.iterdir()):
        if not sem_dir.is_dir() or not sem_dir.name.startswith("sem-"):
            continue

        semester = extract_semester(sem_dir.name)

        for subject_dir in sorted(sem_dir.iterdir()):
            if not subject_dir.is_dir():
                continue
            # Skip non-subject dirs
            if subject_dir.name.startswith(".") or subject_dir.name.startswith("_"):
                continue

            # Generate _meta.json if missing
            meta_path = subject_dir / "_meta.json"
            if not meta_path.exists():
                meta = generate_meta(subject_dir, semester, branch)
                meta_path.write_text(json.dumps(meta, indent=2) + "\n")
                stats["meta_created"] += 1
                print(f"  Created: {meta_path.relative_to(content_path)}")
            else:
                stats["meta_skipped"] += 1

            # Generate subject-level _index.json if missing
            subject_index_path = subject_dir / "_index.json"
            if not subject_index_path.exists():
                subject_index = generate_subject_index(subject_dir)
                if subject_index:
                    subject_index_path.write_text(json.dumps(subject_index, indent=2) + "\n")
                    stats["index_created"] += 1
                    print(f"  Created: {subject_index_path.relative_to(content_path)}")
            else:
                stats["index_skipped"] += 1

            # Generate module-level _index.json for each module
            for module_dir in sorted(subject_dir.iterdir()):
                if not module_dir.is_dir() or not module_dir.name.startswith("module-"):
                    continue

                module_index_path = module_dir / "_index.json"
                if not module_index_path.exists():
                    module_index = generate_module_index(module_dir, module_dir.name)
                    if module_index:
                        module_index_path.write_text(json.dumps(module_index, indent=2) + "\n")
                        stats["index_created"] += 1
                        print(f"  Created: {module_index_path.relative_to(content_path)}")
                else:
                    stats["index_skipped"] += 1

    return stats


def main():
    parser = argparse.ArgumentParser(description="Generate _meta.json and _index.json metadata files")
    parser.add_argument("content_dir", help="Path to content directory")
    parser.add_argument("--branch", default="", help="Branch name (e.g., cse, ise, bca)")
    args = parser.parse_args()

    if not os.path.isdir(args.content_dir):
        print(f"Error: Not a directory: {args.content_dir}")
        return

    branch = args.branch or Path(args.content_dir).parent.name.lower().replace("_", "-")
    print(f"Generating metadata for: {args.content_dir}")
    print(f"Branch: {branch}")
    print()

    stats = process_content_dir(args.content_dir, branch)

    print(f"\nDone!")
    print(f"  _meta.json: {stats['meta_created']} created, {stats['meta_skipped']} already existed")
    print(f"  _index.json: {stats['index_created']} created, {stats['index_skipped']} already existed")


if __name__ == "__main__":
    main()
