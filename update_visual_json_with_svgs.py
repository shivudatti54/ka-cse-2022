#!/usr/bin/env python3
"""
Update visual.json files with actual SVG content from assets folders
"""
import os
import json
from pathlib import Path

BASE_PATH = Path("/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse")

def update_visual_jsons():
    updated = 0
    skipped = 0
    errors = 0

    for sem in ['sem-4', 'sem-5']:
        sem_path = BASE_PATH / sem

        if not sem_path.exists():
            continue

        print(f"\n{'='*60}")
        print(f"Processing {sem}")
        print(f"{'='*60}")

        # Find all visual.json files
        for visual_json_path in sem_path.rglob('visual.json'):
            topic_dir = visual_json_path.parent

            # Skip if not in a topics folder
            if 'topics' not in str(topic_dir):
                continue

            assets_dir = topic_dir / 'assets'

            if not assets_dir.exists():
                skipped += 1
                continue

            # Read visual.json
            try:
                with open(visual_json_path, 'r') as f:
                    visual_data = json.load(f)
            except Exception as e:
                print(f"  ✗ Error reading {visual_json_path}: {e}")
                errors += 1
                continue

            # Check if there are visuals
            if 'visuals' not in visual_data or not visual_data['visuals']:
                skipped += 1
                continue

            modified = False

            # Update each visual
            for visual in visual_data['visuals']:
                # Skip if svgContent is not placeholder
                if visual.get('svgContent') and visual['svgContent'] != '<placeholder>':
                    continue

                # Try to find the SVG file
                svg_files = list(assets_dir.glob('*.svg'))

                if not svg_files:
                    continue

                # Use the first SVG file (should only be one per topic)
                svg_file = svg_files[0]

                try:
                    with open(svg_file, 'r') as f:
                        svg_content = f.read()

                    # Update svgContent
                    visual['svgContent'] = svg_content
                    modified = True
                except Exception as e:
                    print(f"  ✗ Error reading SVG {svg_file}: {e}")
                    errors += 1

            # Write back if modified
            if modified:
                try:
                    with open(visual_json_path, 'w') as f:
                        json.dump(visual_data, f, indent=2)
                    updated += 1

                    if updated % 50 == 0:
                        print(f"  Updated {updated} visual.json files...")
                except Exception as e:
                    print(f"  ✗ Error writing {visual_json_path}: {e}")
                    errors += 1
            else:
                skipped += 1

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors: {errors}")
    print(f"{'='*60}")

if __name__ == "__main__":
    update_visual_jsons()
