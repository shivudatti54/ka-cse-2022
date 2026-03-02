#!/usr/bin/env python3
"""
Validate SVG files for TTS structure compliance

Checks all SVGs in VTU Sem 5 CSE for:
1. Required attributes (xmlns, data-topic-id, viewBox)
2. <defs> section present
3. 4-5 data-narration sections
4. No HTML elements
5. Valid XML structure
"""

import os
import re
import xml.etree.ElementTree as ET

BASE_PATH = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse/sem-5"

def validate_svg(svg_path):
    """Validate a single SVG file"""
    issues = []

    try:
        with open(svg_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, [f"Read error: {e}"], None

    # Check basic structure
    if not content.strip().startswith('<svg'):
        issues.append("Missing <svg> start tag")
    if not content.strip().endswith('</svg>'):
        issues.append("Missing </svg> end tag")

    # Check required attributes
    if 'xmlns=' not in content:
        issues.append("Missing xmlns attribute")
    if 'data-topic-id=' not in content:
        issues.append("Missing data-topic-id attribute")
    if 'viewBox=' not in content:
        issues.append("Missing viewBox attribute")

    # Check for <defs> section
    if '<defs>' not in content:
        issues.append("Missing <defs> section")

    # Check for data-narration attributes
    narration_count = content.count('data-narration=')
    if narration_count < 4:
        issues.append(f"Too few narrations ({narration_count}, need 4-5)")
    elif narration_count > 6:
        issues.append(f"Too many narrations ({narration_count}, should be 4-5)")

    # Check for HTML elements
    html_elements = ['<div', '<span', '<p>', '<br', '<button', '<input']
    found_html = []
    for elem in html_elements:
        if elem in content.lower():
            found_html.append(elem)
    if found_html:
        issues.append(f"Contains HTML: {', '.join(found_html)}")

    # Try XML parse
    try:
        ET.fromstring(content)
    except Exception as e:
        issues.append(f"Invalid XML: {str(e)[:80]}")

    is_valid = len(issues) == 0

    return is_valid, issues, narration_count

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
    print("VTU Sem 5 CSE - TTS SVG Validation")
    print("=" * 80)

    svgs = discover_svgs()
    print(f"\nFound {len(svgs)} SVG files\n")

    if not svgs:
        print("No SVG files found!")
        return

    # Validate all
    results = {
        'valid': [],
        'missing_viewbox': [],
        'missing_narration': [],
        'few_narrations': [],
        'many_narrations': [],
        'other_issues': []
    }

    for svg_path in svgs:
        is_valid, issues, narration_count = validate_svg(svg_path)

        if is_valid:
            results['valid'].append(svg_path)
        else:
            # Categorize issues
            if any('viewBox' in i for i in issues):
                results['missing_viewbox'].append((svg_path, issues, narration_count))
            elif any('Too few' in i for i in issues):
                results['few_narrations'].append((svg_path, issues, narration_count))
            elif any('Too many' in i for i in issues):
                results['many_narrations'].append((svg_path, issues, narration_count))
            elif any('narration' in i.lower() for i in issues):
                results['missing_narration'].append((svg_path, issues, narration_count))
            else:
                results['other_issues'].append((svg_path, issues, narration_count))

    # Print summary
    print("=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    print(f"✓ Fully valid:         {len(results['valid'])}")
    print(f"⚠ Missing viewBox:     {len(results['missing_viewbox'])}")
    print(f"⚠ Missing narrations:  {len(results['missing_narration'])}")
    print(f"⚠ Too few narrations:  {len(results['few_narrations'])}")
    print(f"⚠ Too many narrations: {len(results['many_narrations'])}")
    print(f"✗ Other issues:        {len(results['other_issues'])}")
    print(f"TOTAL:                 {len(svgs)}")
    print("=" * 80)

    # Show details for non-valid
    if results['missing_viewbox']:
        print("\n" + "=" * 80)
        print("SVGs MISSING viewBox (EASY FIX)")
        print("=" * 80)
        for svg_path, issues, narration_count in results['missing_viewbox'][:10]:
            rel_path = svg_path.replace(BASE_PATH, '').lstrip('/')
            print(f"\n{rel_path}")
            print(f"  Narrations: {narration_count}")
            for issue in issues:
                if 'viewBox' not in issue:
                    print(f"  - {issue}")
        if len(results['missing_viewbox']) > 10:
            print(f"\n... and {len(results['missing_viewbox']) - 10} more")

    if results['few_narrations']:
        print("\n" + "=" * 80)
        print("SVGs WITH TOO FEW NARRATIONS")
        print("=" * 80)
        for svg_path, issues, narration_count in results['few_narrations'][:10]:
            rel_path = svg_path.replace(BASE_PATH, '').lstrip('/')
            print(f"\n{rel_path}")
            print(f"  Narrations: {narration_count} (need 4-5)")
        if len(results['few_narrations']) > 10:
            print(f"\n... and {len(results['few_narrations']) - 10} more")

    if results['missing_narration']:
        print("\n" + "=" * 80)
        print("SVGs MISSING NARRATION STRUCTURE")
        print("=" * 80)
        for svg_path, issues, narration_count in results['missing_narration'][:10]:
            rel_path = svg_path.replace(BASE_PATH, '').lstrip('/')
            print(f"\n{rel_path}")
            print(f"  Issues:")
            for issue in issues:
                print(f"    - {issue}")
        if len(results['missing_narration']) > 10:
            print(f"\n... and {len(results['missing_narration']) - 10} more")

    if results['other_issues']:
        print("\n" + "=" * 80)
        print("SVGs WITH OTHER ISSUES")
        print("=" * 80)
        for svg_path, issues, narration_count in results['other_issues'][:5]:
            rel_path = svg_path.replace(BASE_PATH, '').lstrip('/')
            print(f"\n{rel_path}")
            print(f"  Issues:")
            for issue in issues:
                print(f"    - {issue}")
        if len(results['other_issues']) > 5:
            print(f"\n... and {len(results['other_issues']) - 5} more")

    # Overall status
    total_invalid = len(svgs) - len(results['valid'])
    print("\n" + "=" * 80)
    if total_invalid == 0:
        print("✓ ALL SVGs ARE VALID!")
    else:
        print(f"⚠ {total_invalid} SVGs need attention")
        print("\nRECOMMENDATION:")
        if results['missing_viewbox']:
            print("  1. Add viewBox='0 0 420 400' to SVGs missing it")
        if results['few_narrations'] or results['missing_narration']:
            print("  2. Regenerate SVGs with too few narrations")
            print("     Run: python3 generate_tts_svgs.py --workers 4")
    print("=" * 80)

if __name__ == "__main__":
    main()
