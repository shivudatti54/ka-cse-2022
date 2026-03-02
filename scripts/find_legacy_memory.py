#!/usr/bin/env python3
"""
Find topics with legacy memory.json format (mnemonics/acronyms arrays instead of aids).

Legacy format: {mnemonics: [], acronyms: [], visualTips: [], analogies: []}
New format:    {aids: [{type, title, content, forRemembering}]}

Usage:
  python find_legacy_memory.py                # scan cse/
  python find_legacy_memory.py --branch ise   # scan ise/
"""

import json
import os
import sys
import argparse
from pathlib import Path
from collections import defaultdict

CONTENT_ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser(description="Find legacy memory.json format topics")
    parser.add_argument("--branch", default="cse", help="Branch folder to scan (default: cse)")
    args = parser.parse_args()

    branch_dir = CONTENT_ROOT / args.branch
    legacy_count = 0
    new_count = 0
    empty_count = 0
    by_subject = defaultdict(int)

    for root, dirs, files in os.walk(branch_dir):
        if "memory.json" not in files:
            continue
        root_path = Path(root)
        if root_path.parent.name != "topics":
            continue

        fpath = root_path / "memory.json"
        try:
            with open(fpath) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue

        rel = root_path.relative_to(CONTENT_ROOT)
        parts = str(rel).split("/")
        subject = f"{parts[1]}/{parts[2]}" if len(parts) >= 3 else "unknown"

        if "aids" in data and isinstance(data["aids"], list):
            new_count += 1
        elif any(k in data for k in ("mnemonics", "acronyms", "visualTips", "analogies")):
            legacy_count += 1
            by_subject[subject] += 1
        else:
            empty_count += 1

    total = legacy_count + new_count + empty_count
    print(f"Total memory.json files: {total}")
    print(f"  New format (aids):     {new_count}")
    print(f"  Legacy format:         {legacy_count}")
    print(f"  Empty/unknown:         {empty_count}")

    if by_subject:
        print(f"\nLegacy format by subject:")
        for subject, count in sorted(by_subject.items()):
            print(f"  {subject}: {count} topics")


if __name__ == "__main__":
    main()
