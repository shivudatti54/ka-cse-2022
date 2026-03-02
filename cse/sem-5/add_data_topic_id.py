#!/usr/bin/env python3
"""
Add data-topic-id attribute to SVG files

Extracts the topic ID from the file path and adds it to the <svg> tag.
"""

import os
import re

BASE_PATH = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse/sem-5"

def get_topic_id_from_path(svg_path):
    """Extract topic ID from path"""
    # Path structure: .../topics/TOPIC_ID/assets/TOPIC_ID.svg
    parts = svg_path.split('/')
    for i, part in enumerate(parts):
        if part == 'topics' and i + 1 < len(parts):
            return parts[i + 1]
    return None

def add_data_topic_id(svg_path):
    """Add data-topic-id attribute if missing"""
    try:
        with open(svg_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Read error: {e}"

    # Check if data-topic-id is already present
    if 'data-topic-id=' in content:
        return False, "Already has data-topic-id"

    # Get topic ID from path
    topic_id = get_topic_id_from_path(svg_path)
    if not topic_id:
        return False, "Could not extract topic ID from path"

    # Find the opening <svg tag
    svg_match = re.search(r'<svg([^>]*)>', content, re.IGNORECASE)
    if not svg_match:
        return False, "No <svg> tag found"

    # Get the attributes
    attrs = svg_match.group(1).rstrip()

    # Add data-topic-id attribute
    if not attrs.endswith(' '):
        attrs += ' '
    attrs += f'data-topic-id="{topic_id}"'

    # Replace the opening tag
    new_tag = f'<svg{attrs}>'
    new_content = content[:svg_match.start()] + new_tag + content[svg_match.end():]

    # Write back
    try:
        with open(svg_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, f"Added data-topic-id=\"{topic_id}\""
    except Exception as e:
        return False, f"Write error: {e}"

def discover_svgs():
    """Find all SVG files"""
    svgs = []
    for root, dirs, files in os.walk(BASE_PATH):
        for file in files:
            if file.endswith('.svg'):
                svg_path = os.path.join(root, file)
                svgs.append(svg_path)
    return sorted(svgs)

def main():
    print("=" * 80)
    print("Add data-topic-id Attribute to SVGs")
    print("=" * 80)

    svgs = discover_svgs()
    print(f"\nFound {len(svgs)} SVG files\n")

    # Process all
    added = 0
    skipped = 0
    errors = 0

    for i, svg_path in enumerate(svgs, 1):
        rel_path = svg_path.replace(BASE_PATH, '').lstrip('/')
        success, message = add_data_topic_id(svg_path)

        if success:
            added += 1
            if added <= 10 or added % 50 == 0:
                print(f"[{i}/{len(svgs)}] ✓ {rel_path}")
        elif "Already has" in message:
            skipped += 1
        else:
            errors += 1
            if errors <= 10:
                print(f"[{i}/{len(svgs)}] ✗ {rel_path} - {message}")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"✓ Added:   {added}")
    print(f"→ Skipped: {skipped}")
    print(f"✗ Errors:  {errors}")
    print(f"TOTAL:     {len(svgs)}")
    print("=" * 80)

    if added > 0:
        print("\n✓ Successfully added data-topic-id to all SVGs!")
        print("\nRun validation again:")
        print("  python3 validate_tts_svgs.py")

if __name__ == "__main__":
    main()
