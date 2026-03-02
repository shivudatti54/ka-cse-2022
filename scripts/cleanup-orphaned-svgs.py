#!/usr/bin/env python3
"""
Step 3: Delete invalid/orphaned SVGs after regeneration.

Actions:
  1. Delete original non-rich SVGs that now have a valid -rich.svg replacement
  2. Delete any -rich.svg files that still failed validation
  3. Report results

Usage:
  python3 cleanup-orphaned-svgs.py [--dry-run]
"""

import re
import sys
from pathlib import Path

CONTENT_ROOT = Path(__file__).resolve().parent.parent
BRANCHES = ["cse", "ise"]
MIN_FILE_SIZE = 1024
MIN_STEPS = 7


def find_all_topics():
    """Find all topic directories across cse/ and ise/."""
    topics = []
    for branch in BRANCHES:
        branch_dir = CONTENT_ROOT / branch
        if not branch_dir.is_dir():
            continue
        for sem_dir in sorted(branch_dir.iterdir()):
            if not sem_dir.is_dir() or not sem_dir.name.startswith("sem-"):
                continue
            for subj_dir in sorted(sem_dir.iterdir()):
                if not subj_dir.is_dir() or subj_dir.name.startswith(("_", ".")):
                    continue
                for mod_dir in sorted(subj_dir.iterdir()):
                    if not mod_dir.is_dir() or not mod_dir.name.startswith("module-"):
                        continue
                    topics_dir = mod_dir / "topics"
                    if not topics_dir.is_dir():
                        continue
                    for topic_dir in sorted(topics_dir.iterdir()):
                        if topic_dir.is_dir() and not topic_dir.name.startswith(("_", ".")):
                            topics.append(topic_dir)
    return topics


def validate_rich_svg(svg_path):
    """Returns True if -rich.svg is valid."""
    if not svg_path.is_file():
        return False
    if svg_path.stat().st_size < MIN_FILE_SIZE:
        return False
    try:
        content = svg_path.read_text(encoding="utf-8")
    except Exception:
        return False
    if not content.strip().startswith("<svg") and not content.strip().startswith("<?xml"):
        return False
    steps = re.findall(r'class="step"', content)
    if len(steps) < MIN_STEPS:
        return False
    narrations = re.findall(r'data-narration="([^"]*)"', content)
    if len(narrations) == 0:
        return False
    if "@keyframes" not in content:
        return False
    return True


def main():
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print("  SVG Cleanup: Delete orphaned/invalid files")
    print("=" * 60)
    if dry_run:
        print("  MODE: DRY RUN (no files will be deleted)")
    print()

    topics = find_all_topics()
    print(f"Scanning {len(topics)} topics...\n")

    deleted_originals = 0
    deleted_invalid_rich = 0
    kept_rich = 0
    still_missing = 0

    for topic_dir in topics:
        assets = topic_dir / "assets"
        if not assets.is_dir():
            continue

        # Find all SVGs
        originals = [f for f in assets.glob("*.svg") if not f.stem.endswith("-rich")]
        rich_svgs = list(assets.glob("*-rich.svg"))

        for rich_svg in rich_svgs:
            if validate_rich_svg(rich_svg):
                kept_rich += 1
                # Delete original if valid rich exists
                base_name = rich_svg.stem.replace("-rich", "")
                original = assets / f"{base_name}.svg"
                if original.is_file():
                    if dry_run:
                        print(f"  [DELETE original] {original.relative_to(CONTENT_ROOT)}")
                    else:
                        original.unlink()
                    deleted_originals += 1
            else:
                # Invalid rich SVG - delete it
                if dry_run:
                    print(f"  [DELETE invalid rich] {rich_svg.relative_to(CONTENT_ROOT)}")
                else:
                    rich_svg.unlink()
                deleted_invalid_rich += 1

        # Check for topics with no valid SVG at all
        if not rich_svgs and not originals:
            still_missing += 1

    print()
    print("=" * 60)
    print("  CLEANUP RESULTS")
    print("=" * 60)
    print(f"  Valid -rich.svg kept:        {kept_rich}")
    print(f"  Original SVGs deleted:       {deleted_originals}")
    print(f"  Invalid -rich.svg deleted:   {deleted_invalid_rich}")
    print(f"  Topics with no SVG:          {still_missing}")
    if dry_run:
        print(f"\n  [DRY RUN] No files were actually deleted.")
    print()


if __name__ == "__main__":
    main()
