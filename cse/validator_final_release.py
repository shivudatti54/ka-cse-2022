#!/usr/bin/env python3
"""
Final validation of regenerated SVGs
"""

import os
from pathlib import Path
import xml.etree.ElementTree as ET

BASE_PATH = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse"

def validate_svg(svg_path):
    """Validate SVG quality"""
    try:
        with open(svg_path, 'r', encoding='utf-8') as f:
            content = f.read()

        root = ET.fromstring(content)
        viewbox = root.get('viewBox')

        steps = root.findall(".//{http://www.w3.org/2000/svg}g[@id]")
        step_groups = [g for g in steps if g.get('id', '').startswith('step')]

        step_count = len(step_groups)
        has_narration = all(g.get('data-narration') for g in step_groups)

        return {
            'valid': viewbox == "0 0 800 600" and step_count >= 4 and has_narration,
            'viewbox': viewbox,
            'steps': step_count,
            'narrations': has_narration
        }
    except Exception as e:
        return {
            'valid': False,
            'error': str(e)
        }

def main():
    print("="*80)
    print("FINAL SVG VALIDATION")
    print("="*80)
    print()

    # Find all SVGs
    all_svgs = []
    for sem in ['sem-3', 'sem-4', 'sem-5', 'sem-6', 'sem-7']:
        sem_path = Path(BASE_PATH) / sem
        if sem_path.exists():
            svgs = list(sem_path.rglob('*.svg'))
            all_svgs.extend(svgs)

    print(f"Total SVGs found: {len(all_svgs)}")

    # Validate all
    valid = 0
    invalid = 0
    issues = []

    for svg_path in all_svgs:
        result = validate_svg(svg_path)
        if result['valid']:
            valid += 1
        else:
            invalid += 1
            issues.append((svg_path.relative_to(BASE_PATH), result))

    print(f"\nValidation Results:")
    print(f"  Valid: {valid}")
    print(f"  Invalid: {invalid}")
    print(f"  Success Rate: {100*valid/len(all_svgs):.1f}%")

    if issues:
        print(f"\nRemaining Issues ({len(issues)} files):")
        for path, result in issues[:20]:
            print(f"  {path}")
            if 'error' in result:
                print(f"    Error: {result['error']}")
            else:
                if result.get('viewbox') != "0 0 800 600":
                    print(f"    ViewBox: {result.get('viewbox')}")
                if result.get('steps', 0) < 4:
                    print(f"    Steps: {result.get('steps')}")
                if not result.get('narrations'):
                    print(f"    Missing narrations")

        if len(issues) > 20:
            print(f"  ... and {len(issues) - 20} more")

    print()
    print("="*80)

if __name__ == '__main__':
    main()
