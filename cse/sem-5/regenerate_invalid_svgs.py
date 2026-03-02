#!/usr/bin/env python3
"""
Regenerate only invalid/problematic SVG files

Identifies SVGs that need regeneration and creates a list.
User can then regenerate just those specific files.
"""

import os
import re
import xml.etree.ElementTree as ET

BASE_PATH = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse/sem-5"

def validate_svg(svg_path):
    """Check if SVG needs regeneration"""
    try:
        with open(svg_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, ["Read error"]

    issues = []

    # Check narration count
    narration_count = content.count('data-narration=')
    if narration_count < 4:
        issues.append(f"Too few narrations ({narration_count})")
    elif narration_count > 6:
        issues.append(f"Too many narrations ({narration_count})")

    # Check for HTML elements
    html_elements = ['<div', '<span', '<p>', '<br', '<button', '<input']
    for elem in html_elements:
        if elem in content.lower():
            issues.append(f"Contains HTML: {elem}")
            break

    # Try XML parse
    try:
        ET.fromstring(content)
    except Exception as e:
        issues.append("Invalid XML")

    needs_regen = len(issues) > 0
    return needs_regen, issues

def discover_svgs():
    """Find all SVG files"""
    svgs = []
    for root, dirs, files in os.walk(BASE_PATH):
        for file in files:
            if file.endswith('.svg'):
                svg_path = os.path.join(root, file)
                svgs.append(svg_path)
    return sorted(svgs)

def extract_topic_info(svg_path):
    """Extract subject, module, topic from path"""
    parts = svg_path.replace(BASE_PATH, '').lstrip('/').split('/')
    if len(parts) >= 5:
        subject = parts[0]
        module = parts[2]
        topic = parts[4]
        return subject, module, topic
    return None, None, None

def main():
    print("=" * 80)
    print("Identify SVGs Needing Regeneration")
    print("=" * 80)

    svgs = discover_svgs()
    print(f"\nFound {len(svgs)} SVG files")

    # Check all
    need_regen = []
    for svg_path in svgs:
        needs_it, issues = validate_svg(svg_path)
        if needs_it:
            subject, module, topic = extract_topic_info(svg_path)
            need_regen.append({
                'path': svg_path,
                'subject': subject,
                'module': module,
                'topic': topic,
                'issues': issues
            })

    print(f"\n{len(need_regen)} SVGs need regeneration")

    if not need_regen:
        print("\n✓ All SVGs are valid!")
        return

    # Group by issue type
    by_issue = {}
    for item in need_regen:
        issue_key = item['issues'][0].split('(')[0].strip()
        if issue_key not in by_issue:
            by_issue[issue_key] = []
        by_issue[issue_key].append(item)

    # Print summary by issue
    print("\n" + "=" * 80)
    print("ISSUES BREAKDOWN")
    print("=" * 80)
    for issue_key, items in sorted(by_issue.items()):
        print(f"\n{issue_key}: {len(items)} SVGs")
        for item in items[:5]:
            print(f"  - {item['subject']} / {item['module']} / {item['topic']}")
        if len(items) > 5:
            print(f"  ... and {len(items) - 5} more")

    # Save list to file
    output_path = os.path.join(BASE_PATH, "svgs_to_regenerate.txt")
    with open(output_path, 'w') as f:
        f.write("# SVGs that need regeneration\n")
        f.write(f"# Total: {len(need_regen)}\n\n")
        for item in need_regen:
            f.write(f"{item['path']}\n")

    print("\n" + "=" * 80)
    print(f"✓ List saved to: svgs_to_regenerate.txt")
    print(f"\nTo regenerate these {len(need_regen)} SVGs:")
    print("  1. Set your NVIDIA_API_KEY environment variable")
    print("  2. Run: python3 regenerate_from_list.py")
    print("=" * 80)

if __name__ == "__main__":
    main()
