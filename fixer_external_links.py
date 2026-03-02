#!/usr/bin/env python3
"""
Fix External Links - Remove all external image/links and reference local SVG
"""

import os
import re
from pathlib import Path

CSE_DIR = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse"

# Patterns to remove
EXTERNAL_IMAGE_PATTERN = r'!\[([^\]]*)\]\(https?://[^\)]+\)'
EXTERNAL_LINK_PATTERN = r'\[([^\]]*)\]\(https?://[^\)]+\)'

stats = {"files_checked": 0, "files_fixed": 0, "images_removed": 0, "links_removed": 0}

def get_topic_id(file_path):
    """Extract topic ID from file path"""
    # Path like: .../topics/topic-name/full.md or .../topics/topic-name/read.md
    parts = Path(file_path).parts
    for i, part in enumerate(parts):
        if part == 'topics' and i + 1 < len(parts):
            return parts[i + 1]
    return None

def get_svg_reference(topic_id):
    """Generate local SVG reference"""
    return f'\n\n> **Diagram**: See the visual explanation in `assets/{topic_id}.svg`\n'

def fix_file(file_path):
    """Remove external links and add SVG reference"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False

    original_content = content

    # Count external images
    images = re.findall(EXTERNAL_IMAGE_PATTERN, content)
    stats["images_removed"] += len(images)

    # Remove external images (keep alt text as note)
    def replace_image(match):
        alt_text = match.group(1)
        if alt_text:
            return f'*[Diagram: {alt_text}]*'
        return ''

    content = re.sub(EXTERNAL_IMAGE_PATTERN, replace_image, content)

    # Remove external links but keep the text
    def replace_link(match):
        link_text = match.group(1)
        return link_text  # Keep just the text, remove the URL

    links_before = len(re.findall(EXTERNAL_LINK_PATTERN, content))
    content = re.sub(EXTERNAL_LINK_PATTERN, replace_link, content)
    stats["links_removed"] += links_before

    # Clean up empty image sections
    content = re.sub(r'\n### Diagrams\n+(\*\[Diagram:[^\]]*\]\*\n*)+', '', content)
    content = re.sub(r'\n#### [^\n]*\n+\*\[Diagram:[^\]]*\]\*\n*', '', content)

    # Clean up multiple blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Add SVG reference at the end if we removed images
    if images:
        topic_id = get_topic_id(file_path)
        if topic_id:
            # Check if SVG exists
            svg_path = os.path.join(os.path.dirname(file_path), 'assets', f'{topic_id}.svg')
            if os.path.exists(svg_path):
                if 'assets/' not in content and '## Visual' not in content:
                    content = content.rstrip() + f'\n\n---\n\n## Visual Diagram\n\nSee: `assets/{topic_id}.svg` for an interactive visual explanation of this topic.\n'

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    print("=" * 60)
    print("FIX EXTERNAL LINKS - Remove external refs, use local SVG")
    print("=" * 60)

    # Find all markdown files
    md_files = []
    for root, dirs, files in os.walk(CSE_DIR):
        for f in files:
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))

    print(f"Found {len(md_files)} markdown files")
    print("")

    for file_path in md_files:
        stats["files_checked"] += 1

        # Check if file has external links
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            continue

        if 'http://' in content or 'https://' in content:
            if fix_file(file_path):
                stats["files_fixed"] += 1
                topic = get_topic_id(file_path) or os.path.basename(file_path)
                print(f"  ✓ Fixed: {topic[:50]}")

    print("")
    print("=" * 60)
    print("COMPLETE")
    print("=" * 60)
    print(f"Files checked: {stats['files_checked']}")
    print(f"Files fixed: {stats['files_fixed']}")
    print(f"External images removed: {stats['images_removed']}")
    print(f"External links removed: {stats['links_removed']}")

if __name__ == "__main__":
    main()
