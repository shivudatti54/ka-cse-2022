#!/usr/bin/env python3
"""
Step 4a: Consolidate SVGs - rename -rich.svg to .svg and update visual.json.

Actions:
  1. Rename {topic}-rich.svg → {topic}.svg
  2. Update visual.json: remove -rich entries, keep single entry per topic
  3. Report results

Usage:
  python3 consolidate-svgs.py [--dry-run]
"""

import json
import sys
from pathlib import Path

CONTENT_ROOT = Path(__file__).resolve().parent.parent
BRANCHES = ["cse", "ise"]


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


def update_visual_json(topic_dir, dry_run=False):
    """
    Update visual.json to remove -rich entries and point to consolidated .svg.
    Returns (updated: bool, details: str).
    """
    vj_path = topic_dir / "visual.json"
    if not vj_path.is_file():
        return False, "no visual.json"

    try:
        data = json.loads(vj_path.read_text(encoding="utf-8"))
    except Exception as e:
        return False, f"JSON parse error: {e}"

    if "visuals" not in data or not isinstance(data["visuals"], list):
        return False, "no visuals array"

    original_count = len(data["visuals"])
    new_visuals = []
    seen_base_ids = set()

    for v in data["visuals"]:
        vid = v.get("id", "")
        vfile = v.get("file", "")

        # If this is a -rich entry, convert it to the base entry
        if vid.endswith("-rich") or "-rich.svg" in vfile:
            base_id = vid.replace("-rich", "")
            base_file = vfile.replace("-rich.svg", ".svg")

            if base_id not in seen_base_ids:
                new_entry = {
                    "id": base_id,
                    "title": v.get("title", "").replace(" (Rich)", ""),
                    "type": "animated-svg",
                    "file": base_file,
                    "animated": True,
                }
                desc = v.get("description", "")
                if desc:
                    new_entry["description"] = desc.replace(" - Enhanced with CSS animations", "")
                new_visuals.append(new_entry)
                seen_base_ids.add(base_id)
        else:
            # Original entry - keep if no rich version already handled
            base_id = vid
            if base_id not in seen_base_ids:
                # Update file path to remove -rich if needed
                v_copy = dict(v)
                v_copy["animated"] = True
                v_copy["type"] = "animated-svg"
                new_visuals.append(v_copy)
                seen_base_ids.add(base_id)

    if new_visuals == data["visuals"]:
        return False, "no changes needed"

    data["visuals"] = new_visuals

    if not dry_run:
        with vj_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")

    return True, f"{original_count} → {len(new_visuals)} entries"


def main():
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print("  SVG Consolidation: Rename -rich.svg → .svg")
    print("=" * 60)
    if dry_run:
        print("  MODE: DRY RUN (no files will be changed)")
    print()

    topics = find_all_topics()
    print(f"Scanning {len(topics)} topics...\n")

    renamed = 0
    vj_updated = 0
    skipped = 0

    for topic_dir in topics:
        assets = topic_dir / "assets"
        if not assets.is_dir():
            continue

        # Rename -rich.svg files
        for rich_svg in assets.glob("*-rich.svg"):
            base_name = rich_svg.stem.replace("-rich", "")
            target = assets / f"{base_name}.svg"

            if dry_run:
                print(f"  [RENAME] {rich_svg.name} → {target.name}")
            else:
                # Remove original if it exists (shouldn't after cleanup step)
                if target.is_file():
                    target.unlink()
                rich_svg.rename(target)
            renamed += 1

        # Update visual.json
        updated, details = update_visual_json(topic_dir, dry_run)
        if updated:
            vj_updated += 1
        else:
            skipped += 1

    print()
    print("=" * 60)
    print("  CONSOLIDATION RESULTS")
    print("=" * 60)
    print(f"  SVGs renamed (-rich → base):  {renamed}")
    print(f"  visual.json files updated:    {vj_updated}")
    print(f"  Skipped (no changes):         {skipped}")
    if dry_run:
        print(f"\n  [DRY RUN] No files were actually changed.")
    else:
        print(f"\n  Next: Simplify StepSvgPlayer.tsx and build-content-db.ts")
    print()


if __name__ == "__main__":
    main()
