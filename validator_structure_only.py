#!/usr/bin/env python3
"""
Quick Validation Script - No API calls, just identifies broken files
"""

import os
import json
import xml.etree.ElementTree as ET
from datetime import datetime

CSE_DIR = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse"

def validate_svg(filepath):
    """Validate SVG file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        errors = []

        if not content.strip().startswith('<svg'):
            errors.append("Does not start with <svg>")

        if '</svg>' not in content:
            errors.append("Missing closing </svg>")

        try:
            ET.fromstring(content)
        except ET.ParseError as e:
            errors.append(f"XML error: {str(e)[:80]}")

        if 'width=' not in content or 'height=' not in content:
            errors.append("Missing width/height")

        invalid_html = ['<ul>', '<li>', '<div>', '<footer>', '<section>']
        for elem in invalid_html:
            if elem in content.lower():
                errors.append(f"Invalid HTML: {elem}")
                break

        if len(content) < 200:
            errors.append("Too short (<200 chars)")

        if 'data-narration' not in content:
            errors.append("Missing data-narration")

        return errors

    except Exception as e:
        return [f"Read error: {e}"]

def validate_json(filepath):
    """Validate JSON file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if not content.strip():
            return ["Empty file"]

        data = json.loads(content)
        errors = []
        filename = os.path.basename(filepath)

        if filename == "mcqs.json":
            if "mcqs" not in data:
                errors.append("Missing 'mcqs' key")
            elif len(data.get("mcqs", [])) < 3:
                errors.append(f"Only {len(data.get('mcqs', []))} MCQs")

        elif filename == "flashcards.json":
            if "flashcards" not in data:
                errors.append("Missing 'flashcards' key")
            elif len(data.get("flashcards", [])) < 3:
                errors.append(f"Only {len(data.get('flashcards', []))} cards")

        elif filename == "questions.json":
            if "questions" not in data:
                errors.append("Missing 'questions' key")

        elif filename == "visual.json":
            if "visuals" not in data:
                errors.append("Missing 'visuals' key")

        return errors

    except json.JSONDecodeError as e:
        return [f"JSON error: {str(e)[:80]}"]
    except Exception as e:
        return [f"Read error: {e}"]

def main():
    print("=" * 70)
    print("VTU CONTENT VALIDATOR (Quick Check)")
    print("=" * 70)

    # Find files
    svg_files = []
    json_files = {"mcqs.json": [], "flashcards.json": [], "questions.json": [], "visual.json": []}

    for root, dirs, files in os.walk(CSE_DIR):
        for f in files:
            path = os.path.join(root, f)
            if f.endswith('.svg'):
                svg_files.append(path)
            elif f in json_files:
                json_files[f].append(path)

    print(f"\nFiles found:")
    print(f"  SVGs: {len(svg_files)}")
    for jf, paths in json_files.items():
        print(f"  {jf}: {len(paths)}")

    # Validate SVGs
    print("\n" + "=" * 70)
    print("SVG VALIDATION")
    print("=" * 70)

    svg_issues = {"xml_error": 0, "missing_svg_tag": 0, "invalid_html": 0, "too_short": 0, "no_narration": 0, "other": 0}
    svg_broken = []

    for filepath in svg_files:
        errors = validate_svg(filepath)
        if errors:
            svg_broken.append({"path": filepath, "errors": errors})
            for e in errors:
                if "XML error" in e:
                    svg_issues["xml_error"] += 1
                elif "svg>" in e.lower():
                    svg_issues["missing_svg_tag"] += 1
                elif "HTML" in e:
                    svg_issues["invalid_html"] += 1
                elif "short" in e:
                    svg_issues["too_short"] += 1
                elif "narration" in e:
                    svg_issues["no_narration"] += 1
                else:
                    svg_issues["other"] += 1

    print(f"\nSVG Summary:")
    print(f"  Total: {len(svg_files)}")
    print(f"  Valid: {len(svg_files) - len(svg_broken)}")
    print(f"  Broken: {len(svg_broken)}")
    print(f"\nIssue Breakdown:")
    for issue, count in svg_issues.items():
        if count > 0:
            print(f"  {issue}: {count}")

    # Validate JSONs
    print("\n" + "=" * 70)
    print("JSON VALIDATION")
    print("=" * 70)

    json_broken = {"mcqs.json": [], "flashcards.json": [], "questions.json": [], "visual.json": []}
    json_valid = {"mcqs.json": 0, "flashcards.json": 0, "questions.json": 0, "visual.json": 0}

    for jf, paths in json_files.items():
        for filepath in paths:
            errors = validate_json(filepath)
            if errors:
                json_broken[jf].append({"path": filepath, "errors": errors})
            else:
                json_valid[jf] += 1

    print(f"\nJSON Summary:")
    for jf in json_files:
        total = len(json_files[jf])
        broken = len(json_broken[jf])
        print(f"  {jf}: {total - broken}/{total} valid ({broken} broken)")

    # Save detailed report
    report = {
        "timestamp": datetime.now().isoformat(),
        "summary": {
            "svg_total": len(svg_files),
            "svg_broken": len(svg_broken),
            "svg_issues": svg_issues,
            "json_broken": {k: len(v) for k, v in json_broken.items()}
        },
        "svg_broken_samples": svg_broken[:20],
        "json_broken_samples": {k: v[:10] for k, v in json_broken.items()}
    }

    report_path = CSE_DIR.replace("/cse", "/validation_quick_report.json")
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"\n" + "=" * 70)
    print("SAMPLE BROKEN SVGs (first 10)")
    print("=" * 70)
    for item in svg_broken[:10]:
        rel_path = item["path"].replace(CSE_DIR, "")
        print(f"\n{rel_path}")
        for e in item["errors"]:
            print(f"  - {e}")

    print(f"\n\nFull report saved to: {report_path}")

if __name__ == "__main__":
    main()
