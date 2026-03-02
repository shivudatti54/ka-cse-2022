#!/usr/bin/env python3
"""
Validate SVG quality across CSE semesters 3-7
"""

import os
import re
from pathlib import Path
import xml.etree.ElementTree as ET

BASE_PATH = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse"

def validate_svg(svg_path):
    """
    Validate SVG quality
    Returns: (is_valid, issues_list)
    """
    issues = []

    try:
        with open(svg_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse XML
        try:
            root = ET.fromstring(content)
        except ET.ParseError as e:
            issues.append(f"XML parse error: {e}")
            return False, issues

        # Check viewBox
        viewbox = root.get('viewBox')
        if not viewbox or viewbox != "0 0 800 600":
            issues.append(f"Invalid viewBox: {viewbox}")

        # Find all step groups
        step_groups = root.findall(".//{http://www.w3.org/2000/svg}g[@id]")
        steps = [g for g in step_groups if g.get('id', '').startswith('step')]

        # Check step count
        step_count = len(steps)
        if step_count < 4:
            issues.append(f"Too few steps: {step_count}")

        # Check sequential step IDs
        step_ids = [g.get('id') for g in steps]
        expected_ids = [f'step{i}' for i in range(len(steps))]
        if step_ids != expected_ids:
            issues.append(f"Non-sequential step IDs: {step_ids}")

        # Check data-narration attributes
        missing_narration = []
        for step in steps:
            if not step.get('data-narration'):
                missing_narration.append(step.get('id'))

        if missing_narration:
            issues.append(f"Missing data-narration: {missing_narration}")

        # Check for generic/template content
        generic_markers = [
            'Generic Template',
            'Example Step',
            'Placeholder',
            'TODO',
            'lorem ipsum'
        ]

        for marker in generic_markers:
            if marker.lower() in content.lower():
                issues.append(f"Generic content detected: {marker}")
                break

        return len(issues) == 0, issues

    except Exception as e:
        issues.append(f"Error reading file: {e}")
        return False, issues

def main():
    # Find all SVGs
    svg_files = []
    for sem in ['sem-3', 'sem-4', 'sem-5', 'sem-6', 'sem-7']:
        sem_path = Path(BASE_PATH) / sem
        if sem_path.exists():
            svgs = list(sem_path.rglob('*.svg'))
            svg_files.extend(svgs)

    print(f"Found {len(svg_files)} SVG files")

    # Validate each
    invalid_svgs = []
    valid_count = 0

    for svg_path in svg_files:
        is_valid, issues = validate_svg(svg_path)
        if not is_valid:
            relative_path = svg_path.relative_to(BASE_PATH)
            invalid_svgs.append({
                'path': str(relative_path),
                'full_path': str(svg_path),
                'issues': issues
            })
        else:
            valid_count += 1

    # Report
    print(f"\n{'='*80}")
    print(f"VALIDATION REPORT")
    print(f"{'='*80}")
    print(f"Total SVGs scanned: {len(svg_files)}")
    print(f"Valid SVGs: {valid_count}")
    print(f"Invalid SVGs: {len(invalid_svgs)}")
    print(f"{'='*80}\n")

    # Group by issue type
    issue_types = {}
    for svg_info in invalid_svgs:
        for issue in svg_info['issues']:
            issue_key = issue.split(':')[0]
            if issue_key not in issue_types:
                issue_types[issue_key] = []
            issue_types[issue_key].append(svg_info['path'])

    print("ISSUES BY TYPE:")
    for issue_type, paths in sorted(issue_types.items()):
        print(f"\n{issue_type}: {len(paths)} files")
        for path in paths[:5]:  # Show first 5
            print(f"  - {path}")
        if len(paths) > 5:
            print(f"  ... and {len(paths) - 5} more")

    # Save detailed report
    report_path = Path(BASE_PATH) / 'svg_validation_report.txt'
    with open(report_path, 'w') as f:
        f.write(f"SVG Validation Report\n")
        f.write(f"{'='*80}\n\n")
        f.write(f"Total SVGs: {len(svg_files)}\n")
        f.write(f"Valid: {valid_count}\n")
        f.write(f"Invalid: {len(invalid_svgs)}\n\n")

        f.write(f"INVALID SVGs:\n")
        f.write(f"{'-'*80}\n")
        for svg_info in invalid_svgs:
            f.write(f"\n{svg_info['path']}\n")
            for issue in svg_info['issues']:
                f.write(f"  - {issue}\n")

    print(f"\nDetailed report saved to: {report_path}")

    # Save list of files to regenerate
    regen_list_path = Path(BASE_PATH) / 'svgs_to_regenerate.txt'
    with open(regen_list_path, 'w') as f:
        for svg_info in invalid_svgs:
            f.write(f"{svg_info['full_path']}\n")

    print(f"Regeneration list saved to: {regen_list_path}")

if __name__ == '__main__':
    main()
