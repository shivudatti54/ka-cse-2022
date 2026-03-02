#!/usr/bin/env python3
"""
Update visual.json files to include -rich.svg versions alongside originals.
This script:
1. Reads visual.json files from topic directories
2. For each SVG reference, checks if a -rich.svg version exists
3. Adds new entries for -rich.svg files (without overwriting originals)
4. Saves updated visual.json files
"""

import json
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

def update_visual_json(topic_dir):
    """
    Update visual.json in a topic directory to include -rich.svg entries.
    Returns (topic_dir, updated_count, error_msg)
    """
    topic_path = Path(topic_dir)
    visual_json_path = topic_path / "visual.json"

    if not visual_json_path.is_file():
        return topic_dir, 0, "No visual.json found"

    try:
        # Read existing visual.json
        with visual_json_path.open('r', encoding='utf-8') as f:
            data = json.load(f)

        # Track if we made any changes
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

        return topic_dir, updated_count, "ok"

    except Exception as e:
        return topic_dir, 0, f"Error: {str(e)}"

def load_topic_paths(path_file):
    """Read topic paths from file, skipping blanks and comments."""
    paths = []
    with path_file.open() as f:
        for line in f:
            path = line.strip()
            if path and not path.startswith("#"):
                paths.append(path)
    return paths

def main():
    # Parse args: update_visual_json_rich.py [path_file] [workers]
    path_file = Path("svg_path.txt")
    workers = 1

    for arg in sys.argv[1:]:
        if arg.isdigit():
            workers = int(arg)
        else:
            path_file = Path(arg)

    if not path_file.is_file():
        print(f"Path file not found: {path_file}")
        return

    topic_paths = load_topic_paths(path_file)
    if not topic_paths:
        print("No topic paths to process.")
        return

    total = len(topic_paths)
    print(f"Updating visual.json files in {total} topics")
    print(f"Using {workers} worker(s)\n")

    if workers <= 1:
        # Sequential mode
        total_updated = 0
        for i, topic_dir in enumerate(topic_paths, 1):
            topic_name = Path(topic_dir).name
            topic_dir_path, count, msg = update_visual_json(topic_dir)

            if count > 0:
                print(f"[{i}/{total}] ✓ {topic_name} - Added {count} rich SVG(s)")
                total_updated += count
            elif msg != "No visual.json found":
                print(f"[{i}/{total}] - {topic_name} - {msg}")

        print(f"\nDone: Added {total_updated} rich SVG entries to visual.json files")
    else:
        # Parallel mode
        done = 0
        total_updated = 0
        failed = 0

        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(update_visual_json, t): t for t in topic_paths}
            for future in as_completed(futures):
                topic_dir, count, msg = future.result()
                done += 1
                topic_name = Path(topic_dir).name

                if count > 0:
                    print(f"[{done}/{total}] ✓ {topic_name} - Added {count} rich SVG(s)")
                    total_updated += count
                elif msg not in ["No visual.json found", "ok"]:
                    print(f"[{done}/{total}] ✗ {topic_name} - {msg}")
                    failed += 1

        print(f"\nDone: Added {total_updated} rich SVG entries across {done - failed} visual.json files")

if __name__ == "__main__":
    main()
