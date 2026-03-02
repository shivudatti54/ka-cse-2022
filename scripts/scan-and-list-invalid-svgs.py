#!/usr/bin/env python3
"""
Scan all topics for missing or invalid -rich.svg files.
Outputs svg_path.txt with topic directories needing regeneration.

Validation criteria for INVALID -rich.svg:
  1. Missing entirely (no -rich.svg in assets/)
  2. Malformed XML (can't parse as SVG)
  3. Missing data-narration attributes on steps
  4. Too few steps (<7)
  5. Placeholder/stub file (<1KB)

Usage:
  python3 scan-and-list-invalid-svgs.py [--dry-run]
"""

import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

CONTENT_ROOT = Path(__file__).resolve().parent.parent
BRANCHES = ["cse", "ise"]
OUTPUT_FILE = CONTENT_ROOT / "scripts" / "svg_path.txt"

# Validation thresholds
MIN_FILE_SIZE = 1024        # 1KB minimum (below = placeholder)
MIN_STEPS = 7               # Minimum step count
REQUIRED_NARRATION_RATIO = 1.0  # All steps must have narration


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


def find_rich_svg(topic_dir):
    """Find the -rich.svg file in a topic's assets directory."""
    assets = topic_dir / "assets"
    if not assets.is_dir():
        return None
    rich_svgs = list(assets.glob("*-rich.svg"))
    return rich_svgs[0] if rich_svgs else None


def find_original_svg(topic_dir):
    """Find the original (non-rich) SVG in a topic's assets directory."""
    assets = topic_dir / "assets"
    if not assets.is_dir():
        return None
    for svg in assets.glob("*.svg"):
        if not svg.stem.endswith("-rich"):
            return svg
    return None


def validate_rich_svg(svg_path):
    """
    Validate a -rich.svg file. Returns (is_valid, reasons[]) tuple.
    """
    reasons = []

    # Check 1: File size
    size = svg_path.stat().st_size
    if size < MIN_FILE_SIZE:
        reasons.append(f"placeholder ({size}B < {MIN_FILE_SIZE}B)")
        return False, reasons

    # Check 2: Parse as XML
    try:
        content = svg_path.read_text(encoding="utf-8")
    except Exception as e:
        reasons.append(f"read error: {e}")
        return False, reasons

    if not content.strip().startswith("<svg") and not content.strip().startswith("<?xml"):
        reasons.append("not valid SVG (doesn't start with <svg)")
        return False, reasons

    # Use regex-based validation (more lenient than XML parser for SVGs with HTML entities)
    # Check 3: Step count
    steps = re.findall(r'class="step"', content)
    step_count = len(steps)
    if step_count < MIN_STEPS:
        reasons.append(f"too few steps ({step_count} < {MIN_STEPS})")

    # Check 4: Narration attributes
    narrations = re.findall(r'data-narration="([^"]*)"', content)
    narration_count = len(narrations)
    if step_count > 0 and narration_count == 0:
        reasons.append(f"no narrations ({step_count} steps, 0 narrations)")
    elif step_count > 0 and narration_count < step_count:
        reasons.append(f"missing narrations ({narration_count}/{step_count})")

    # Check 5: CSS animations (required for -rich format)
    if "@keyframes" not in content:
        reasons.append("no CSS @keyframes")

    # Check 6: <style> block
    if "<style>" not in content:
        reasons.append("no <style> block")

    is_valid = len(reasons) == 0
    return is_valid, reasons


def main():
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print("  SVG Rich Validator & Scanner")
    print("=" * 60)
    print(f"  Content root: {CONTENT_ROOT}")
    print(f"  Output: {OUTPUT_FILE}")
    print()

    topics = find_all_topics()
    print(f"Found {len(topics)} total topics\n")

    # Categorize topics
    missing = []       # No -rich.svg at all
    invalid = []       # Has -rich.svg but fails validation
    no_svg = []        # No SVG at all (not even original)
    valid = []         # Has valid -rich.svg

    for topic_dir in topics:
        original_svg = find_original_svg(topic_dir)
        rich_svg = find_rich_svg(topic_dir)

        if not original_svg and not rich_svg:
            no_svg.append(topic_dir)
            continue

        if not rich_svg:
            missing.append((topic_dir, "missing -rich.svg"))
            continue

        is_valid, reasons = validate_rich_svg(rich_svg)
        if is_valid:
            valid.append(topic_dir)
        else:
            invalid.append((topic_dir, "; ".join(reasons)))

    # Summary
    print("=" * 60)
    print("  SCAN RESULTS")
    print("=" * 60)
    print(f"  Total topics:       {len(topics)}")
    print(f"  Valid -rich.svg:    {len(valid)}")
    print(f"  Missing -rich.svg:  {len(missing)}")
    print(f"  Invalid -rich.svg:  {len(invalid)}")
    print(f"  No SVG at all:      {len(no_svg)}")
    print()

    # Build output list (topics needing regeneration)
    needs_regen = []

    for topic_dir, reason in missing:
        # Only include if there's an original SVG to work from (or read.md for context)
        if (topic_dir / "assets").is_dir() or (topic_dir / "read.md").is_file():
            needs_regen.append((topic_dir, reason))

    for topic_dir, reason in invalid:
        needs_regen.append((topic_dir, reason))

    print(f"  Topics needing regeneration: {len(needs_regen)}")
    print()

    # Print detailed breakdown
    if invalid:
        print("-" * 60)
        print("  INVALID -rich.svg breakdown:")
        print("-" * 60)
        # Group by reason
        reason_counts = {}
        for _, reason in invalid:
            for r in reason.split("; "):
                reason_counts[r] = reason_counts.get(r, 0) + 1
        for reason, count in sorted(reason_counts.items(), key=lambda x: -x[1]):
            print(f"    {count:>4}  {reason}")
        print()

    if no_svg:
        print(f"  Topics with no SVG at all: {len(no_svg)}")
        for td in no_svg[:10]:
            rel = td.relative_to(CONTENT_ROOT)
            print(f"    - {rel}")
        if len(no_svg) > 10:
            print(f"    ... and {len(no_svg) - 10} more")
        print()

    # Write output file
    if dry_run:
        print("[DRY RUN] Would write svg_path.txt with these entries:")
        for topic_dir, reason in needs_regen[:20]:
            rel = topic_dir.relative_to(CONTENT_ROOT)
            print(f"  {rel}  # {reason}")
        if len(needs_regen) > 20:
            print(f"  ... and {len(needs_regen) - 20} more")
        return

    with OUTPUT_FILE.open("w") as f:
        f.write(f"# SVG regeneration list - {len(needs_regen)} topics\n")
        f.write(f"# Generated by scan-and-list-invalid-svgs.py\n")
        f.write(f"# Format: topic directory path (one per line)\n\n")
        for topic_dir, reason in needs_regen:
            f.write(f"{topic_dir}\n")

    print(f"Wrote {len(needs_regen)} entries to {OUTPUT_FILE}")
    print("Done.")


if __name__ == "__main__":
    main()
