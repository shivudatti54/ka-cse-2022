#!/usr/bin/env python3
"""
Bulk update ALL visual.json files across CSE content to add -rich.svg entries.
Scans all topic directories, checks for existing -rich.svg files, and updates
visual.json to include them (without overwriting originals).

Usage:
    python3 bulk_update_visual_json_rich.py              # CSE only
    python3 bulk_update_visual_json_rich.py cse          # CSE only
    python3 bulk_update_visual_json_rich.py all          # All branches
    python3 bulk_update_visual_json_rich.py 4            # Use 4 parallel workers
"""

import json
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

SCRIPT_DIR = Path(__file__).resolve().parent
CONTENT_ROOT = SCRIPT_DIR.parent  # vtu-2022-scheme directory

def update_visual_json(visual_json_path):
    """
    Update a single visual.json file to include -rich.svg entries.
    Returns (visual_json_path, updated_count, error_msg)
    """
    try:
        topic_path = visual_json_path.parent

        # Read existing visual.json
        with visual_json_path.open('r', encoding='utf-8') as f:
            data = json.load(f)

        updated_count = 0

        # Process 'visuals' array if it exists
        if 'visuals' in data and isinstance(data['visuals'], list):
            new_entries = []

            for visual in data['visuals']:
                if visual.get('type') == 'animated-svg' and 'file' in visual:
                    svg_file = visual['file']  # e.g., "assets/topic-name.svg"

                    # Generate -rich.svg filename
                    svg_path = Path(svg_file)
                    rich_svg_name = f"{svg_path.stem}-rich.svg"
                    rich_svg_file = str(svg_path.parent / rich_svg_name)

                    # Check if -rich.svg exists
                    rich_svg_path = topic_path / rich_svg_file
                    if rich_svg_path.is_file():
                        # Check if this -rich entry already exists
                        rich_id = f"{visual['id']}-rich"
                        already_exists = any(
                            v.get('id') == rich_id for v in data['visuals']
                        )

                        if not already_exists:
                            # Create new entry for -rich.svg
                            rich_entry = {
                                "id": rich_id,
                                "title": f"{visual['title']} (Rich)",
                                "description": f"{visual['description']} - Enhanced with CSS animations",
                                "type": "animated-svg",
                                "file": rich_svg_file,
                                "animated": True
                            }
                            new_entries.append(rich_entry)
                            updated_count += 1

            # Add new entries to visuals array
            if new_entries:
                data['visuals'].extend(new_entries)

        # Save updated visual.json if changes were made
        if updated_count > 0:
            with visual_json_path.open('w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                f.write('\n')  # Add trailing newline

        return str(visual_json_path), updated_count, "ok"

    except Exception as e:
        return str(visual_json_path), 0, f"Error: {str(e)}"


def find_all_visual_json_files(branch='cse'):
    """
    Find all visual.json files in the specified branch (or all branches).
    Returns list of Path objects.
    """
    visual_json_files = []

    if branch == 'all':
        # Find all visual.json files across all branches
        pattern = "**/visual.json"
        base_path = CONTENT_ROOT
    else:
        # Find visual.json files in specific branch (e.g., cse)
        pattern = "**/visual.json"
        base_path = CONTENT_ROOT / branch

    if not base_path.is_dir():
        print(f"Error: Branch directory not found: {base_path}")
        return []

    # Find all visual.json files
    for visual_json in base_path.glob(pattern):
        # Skip any in node_modules, .git, etc.
        if any(part.startswith('.') or part == 'node_modules' for part in visual_json.parts):
            continue
        visual_json_files.append(visual_json)

    return visual_json_files


def main():
    # Parse args: bulk_update_visual_json_rich.py [branch] [workers]
    branch = 'cse'  # Default to CSE branch
    workers = 1

    for arg in sys.argv[1:]:
        if arg.isdigit():
            workers = int(arg)
        elif arg in ['cse', 'all']:
            branch = arg

    print(f"{'=' * 70}")
    print(f"  BULK VISUAL.JSON UPDATER FOR RICH SVGs")
    print(f"{'=' * 70}")
    print(f"  Branch: {branch.upper()}")
    print(f"  Workers: {workers}")
    print(f"{'=' * 70}\n")

    # Find all visual.json files
    visual_json_files = find_all_visual_json_files(branch)

    if not visual_json_files:
        print("No visual.json files found.")
        return

    total = len(visual_json_files)
    print(f"Found {total} visual.json file(s) to process\n")

    if workers <= 1:
        # Sequential mode
        total_updated = 0
        total_entries = 0

        for i, visual_json_path in enumerate(visual_json_files, 1):
            topic_name = visual_json_path.parent.name
            path_str, count, msg = update_visual_json(visual_json_path)

            if count > 0:
                print(f"[{i}/{total}] ✓ {topic_name} - Added {count} rich SVG(s)")
                total_updated += 1
                total_entries += count
            elif msg != "ok":
                print(f"[{i}/{total}] ✗ {topic_name} - {msg}")

        print(f"\n{'=' * 70}")
        print(f"  SUMMARY")
        print(f"{'=' * 70}")
        print(f"  Files updated: {total_updated}/{total}")
        print(f"  Rich SVG entries added: {total_entries}")
        print(f"{'=' * 70}\n")

    else:
        # Parallel mode
        done = 0
        total_updated = 0
        total_entries = 0
        failed = 0

        print(f"Processing {total} visual.json files in parallel...\n")

        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(update_visual_json, vj): vj for vj in visual_json_files}
            for future in as_completed(futures):
                path_str, count, msg = future.result()
                done += 1
                visual_json_path = Path(path_str)
                topic_name = visual_json_path.parent.name

                if count > 0:
                    print(f"[{done}/{total}] ✓ {topic_name} - Added {count} rich SVG(s)")
                    total_updated += 1
                    total_entries += count
                elif msg != "ok":
                    print(f"[{done}/{total}] ✗ {topic_name} - {msg}")
                    failed += 1

        print(f"\n{'=' * 70}")
        print(f"  SUMMARY")
        print(f"{'=' * 70}")
        print(f"  Files processed: {done}/{total}")
        print(f"  Files updated: {total_updated}/{total}")
        print(f"  Rich SVG entries added: {total_entries}")
        print(f"  Failed: {failed}/{total}")
        print(f"{'=' * 70}\n")

        if total_entries > 0:
            print(f"🎉 Successfully added {total_entries} rich SVG entries to visual.json files!")
        elif failed == 0:
            print(f"ℹ️  No new rich SVG entries needed (all up to date)")
        print()


if __name__ == "__main__":
    main()
