#!/usr/bin/env python3
"""
Move placeholder SVGs from subject-level assets to topic-level assets
"""
import os
import shutil
from pathlib import Path

BASE_PATH = Path("/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse")

def move_svgs():
    moved = 0
    errors = 0

    for sem in ['sem-4', 'sem-5']:
        sem_path = BASE_PATH / sem

        if not sem_path.exists():
            continue

        print(f"\n{'='*60}")
        print(f"Processing {sem}")
        print(f"{'='*60}")

        # Find all subjects
        for subject_dir in sem_path.iterdir():
            if not subject_dir.is_dir() or subject_dir.name.startswith('.'):
                continue

            subject_code = subject_dir.name
            subject_assets = subject_dir / "assets"

            if not subject_assets.exists():
                continue

            print(f"\n  Subject: {subject_code}")

            # Get all SVGs in subject assets
            svgs = list(subject_assets.glob("*.svg"))

            if not svgs:
                continue

            # Find topics
            chapters_dir = subject_dir / "chapters"
            if not chapters_dir.exists():
                continue

            for svg_file in svgs:
                svg_name = svg_file.name

                # Extract topic name from filename
                # Format: bcs456c-uiux_topic-name.svg -> topic-name
                if '_' in svg_name:
                    topic_name = svg_name.split('_', 1)[1].replace('.svg', '')
                else:
                    topic_name = svg_name.replace('.svg', '')

                # Find the topic directory
                topic_dirs = list(chapters_dir.glob(f"*/topics/{topic_name}"))

                if not topic_dirs:
                    print(f"    ✗ No topic dir for: {topic_name}")
                    errors += 1
                    continue

                topic_dir = topic_dirs[0]

                # Create topic assets folder
                topic_assets = topic_dir / "assets"
                topic_assets.mkdir(exist_ok=True)

                # New SVG path (without subject code prefix)
                new_svg_name = f"{topic_name}.svg"
                new_svg_path = topic_assets / new_svg_name

                # Move (or copy) the SVG
                try:
                    shutil.copy2(svg_file, new_svg_path)
                    moved += 1
                    if moved % 50 == 0:
                        print(f"    Moved {moved} SVGs...")
                except Exception as e:
                    print(f"    ✗ Error moving {svg_name}: {e}")
                    errors += 1

            print(f"    ✓ Processed {len(svgs)} SVGs from {subject_code}")

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Moved: {moved}")
    print(f"  Errors: {errors}")
    print(f"{'='*60}")

if __name__ == "__main__":
    move_svgs()
