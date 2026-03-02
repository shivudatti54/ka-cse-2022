#!/usr/bin/env python3
import os
import json
from pathlib import Path

# Base path
BASE_PATH = Path("/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse")

# Placeholder SVG template
PLACEHOLDER_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <rect width="800" height="600" fill="#f0f0f0"/>
  <text x="400" y="300" text-anchor="middle" font-family="Arial" font-size="24" fill="#666">
    <tspan x="400" dy="0">PLACEHOLDER SVG</tspan>
    <tspan x="400" dy="30">Topic: {topic_name}</tspan>
    <tspan x="400" dy="30">This will be replaced with actual content</tspan>
  </text>
</svg>'''

def create_placeholder_svg_structure():
    """Create placeholder SVGs and update visual.json files for sem-4 and sem-5"""

    svg_paths = []

    for sem in ['sem-4', 'sem-5']:
        sem_path = BASE_PATH / sem

        if not sem_path.exists():
            print(f"Skipping {sem} - directory not found")
            continue

        print(f"\n{'='*60}")
        print(f"Processing {sem}")
        print(f"{'='*60}")

        # Find all subjects in this semester
        for subject_dir in sem_path.iterdir():
            if not subject_dir.is_dir() or subject_dir.name.startswith('.'):
                continue

            subject_code = subject_dir.name
            print(f"\n  Subject: {subject_code}")

            # Create assets folder at subject level
            assets_dir = subject_dir / "assets"
            assets_dir.mkdir(exist_ok=True)

            # Find all topics in this subject
            chapters_dir = subject_dir / "chapters"
            if not chapters_dir.exists():
                continue

            topic_count = 0

            for module_dir in chapters_dir.iterdir():
                if not module_dir.is_dir() or module_dir.name.startswith('.'):
                    continue

                topics_dir = module_dir / "topics"
                if not topics_dir.exists():
                    continue

                for topic_dir in topics_dir.iterdir():
                    if not topic_dir.is_dir() or topic_dir.name.startswith('.'):
                        continue

                    topic_name = topic_dir.name
                    visual_json_path = topic_dir / "visual.json"

                    if not visual_json_path.exists():
                        continue

                    topic_count += 1

                    # Read visual.json
                    try:
                        with open(visual_json_path, 'r') as f:
                            visual_data = json.load(f)
                    except Exception as e:
                        print(f"    Error reading {visual_json_path}: {e}")
                        continue

                    # Generate SVG filename
                    svg_filename = f"{subject_code}_{topic_name}.svg"
                    svg_path = assets_dir / svg_filename

                    # Relative path from topic to assets (../../../assets/filename.svg)
                    relative_svg_path = f"../../../assets/{svg_filename}"

                    # Update visual.json if it has visuals array
                    modified = False
                    if "visuals" in visual_data and isinstance(visual_data["visuals"], list):
                        for visual in visual_data["visuals"]:
                            if "file" not in visual:
                                visual["file"] = relative_svg_path
                                modified = True

                    # If no visuals array exists or it's empty, create one
                    if "visuals" not in visual_data or not visual_data["visuals"]:
                        visual_data["visuals"] = [{
                            "id": f"{topic_name}-svg",
                            "title": topic_name.replace('-', ' ').title(),
                            "description": f"Visual diagram for {topic_name.replace('-', ' ')}",
                            "type": "animated-svg",
                            "file": relative_svg_path,
                            "svgContent": "<placeholder>"
                        }]
                        modified = True

                    # Write updated visual.json
                    if modified:
                        try:
                            with open(visual_json_path, 'w') as f:
                                json.dump(visual_data, f, indent=2)
                        except Exception as e:
                            print(f"    Error writing {visual_json_path}: {e}")

                    # Create placeholder SVG
                    placeholder_content = PLACEHOLDER_SVG.format(topic_name=topic_name)
                    try:
                        with open(svg_path, 'w') as f:
                            f.write(placeholder_content)
                        svg_paths.append(str(svg_path.absolute()))
                    except Exception as e:
                        print(f"    Error creating {svg_path}: {e}")

            print(f"    Created {topic_count} placeholder SVGs")

    return svg_paths

def main():
    print("Creating placeholder SVG structure for sem-4 and sem-5...")

    svg_paths = create_placeholder_svg_structure()

    # Write paths to file
    output_file = BASE_PATH.parent / "placeholder_svg_paths.txt"
    with open(output_file, 'w') as f:
        for path in sorted(svg_paths):
            f.write(path + '\n')

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Total placeholder SVGs created: {len(svg_paths)}")
    print(f"  Paths written to: {output_file}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
