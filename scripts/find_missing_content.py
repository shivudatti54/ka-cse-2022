#!/usr/bin/env python3
"""
Scan all topic folders and report missing content files.

Expected files per topic:
  read.md, summary.md, purpose.md, mcqs.json, flashcards.json,
  code.json, questions.json, memory.json, visual.json

Usage:
  python find_missing_content.py                    # scan cse/
  python find_missing_content.py --branch ise       # scan ise/
  python find_missing_content.py --file summary.md  # only check summary.md
  python find_missing_content.py --csv              # output as CSV
"""

import os
import sys
import argparse
from pathlib import Path
from collections import defaultdict

EXPECTED_FILES = [
    "read.md",
    "summary.md",
    "purpose.md",
    "mcqs.json",
    "flashcards.json",
    "code.json",
    "questions.json",
    "memory.json",
    "visual.json",
]

CONTENT_ROOT = Path(__file__).resolve().parent.parent


def find_topic_dirs(branch: str) -> list[Path]:
    """Find all topic directories (contain read.md or any expected content file)."""
    branch_dir = CONTENT_ROOT / branch
    if not branch_dir.exists():
        print(f"Error: branch directory not found: {branch_dir}")
        sys.exit(1)

    topic_dirs = []
    for root, dirs, files in os.walk(branch_dir):
        root_path = Path(root)
        # A topic dir is inside a 'topics' parent folder
        if root_path.parent.name == "topics":
            # Verify it has at least one expected file (not an empty/stale dir)
            if any(f in files for f in EXPECTED_FILES):
                topic_dirs.append(root_path)
    return sorted(topic_dirs)


def check_missing(topic_dirs: list[Path], check_files: list[str]) -> dict:
    """Check each topic dir for missing files. Returns {missing_file: [paths]}."""
    missing = defaultdict(list)
    for topic_dir in topic_dirs:
        for fname in check_files:
            fpath = topic_dir / fname
            if not fpath.exists():
                # Relative path from content root for readability
                rel = topic_dir.relative_to(CONTENT_ROOT)
                missing[fname].append(str(rel / fname))
            elif fpath.stat().st_size == 0:
                rel = topic_dir.relative_to(CONTENT_ROOT)
                missing[fname].append(str(rel / fname) + " (EMPTY)")
    return missing


def main():
    parser = argparse.ArgumentParser(description="Find missing content files in topic folders")
    parser.add_argument("--branch", default="cse", help="Branch folder to scan (default: cse)")
    parser.add_argument("--file", dest="only_file", help="Only check this specific file (e.g. summary.md)")
    parser.add_argument("--csv", action="store_true", help="Output as CSV")
    parser.add_argument("--full-path", action="store_true", help="Show full absolute paths")
    parser.add_argument("--output", "-o", help="Write full paths of missing files to a .txt file (one per line)")
    args = parser.parse_args()

    check_files = [args.only_file] if args.only_file else EXPECTED_FILES
    topic_dirs = find_topic_dirs(args.branch)

    if not topic_dirs:
        print(f"No topic directories found in {args.branch}/")
        sys.exit(1)

    missing = check_missing(topic_dirs, check_files)

    # Summary
    total_topics = len(topic_dirs)
    total_missing = sum(len(paths) for paths in missing.values())

    # Write full paths to file if --output specified
    if args.output:
        with open(args.output, "w") as f:
            for fname in check_files:
                for path in missing.get(fname, []):
                    clean_path = path.replace(" (EMPTY)", "")
                    full_path = str(CONTENT_ROOT / clean_path)
                    f.write(full_path + "\n")
        print(f"Wrote {total_missing} missing file paths to: {args.output}")

    if args.csv:
        print("file,topic_path,status")
        for fname in check_files:
            for path in missing.get(fname, []):
                is_empty = path.endswith(" (EMPTY)")
                clean_path = path.replace(" (EMPTY)", "")
                status = "empty" if is_empty else "missing"
                if args.full_path:
                    clean_path = str(CONTENT_ROOT / clean_path)
                print(f"{fname},{clean_path},{status}")
    else:
        print(f"=" * 70)
        print(f"Content Audit: {args.branch}/")
        print(f"Total topics scanned: {total_topics}")
        print(f"Total missing files:  {total_missing}")
        print(f"=" * 70)

        if total_missing == 0:
            print("\nAll content files present!")
        else:
            for fname in check_files:
                paths = missing.get(fname, [])
                if not paths:
                    print(f"\n{fname}: OK ({total_topics}/{total_topics})")
                    continue

                present = total_topics - len(paths)
                print(f"\n{fname}: {len(paths)} MISSING ({present}/{total_topics} present)")
                print("-" * 50)

                # Group by subject for readability
                by_subject = defaultdict(list)
                for p in paths:
                    parts = p.split("/")
                    # e.g. cse/sem-3/bcs302-.../module-1/topics/binary-logic/summary.md
                    if len(parts) >= 3:
                        subject_key = f"{parts[1]}/{parts[2]}"
                    else:
                        subject_key = "unknown"
                    by_subject[subject_key].append(p)

                for subject, spaths in sorted(by_subject.items()):
                    print(f"  {subject} ({len(spaths)} missing)")
                    for p in spaths:
                        if args.full_path:
                            print(f"    {CONTENT_ROOT / p.replace(' (EMPTY)', '')}")
                        else:
                            print(f"    {p}")

        print(f"\n{'=' * 70}")


if __name__ == "__main__":
    main()
