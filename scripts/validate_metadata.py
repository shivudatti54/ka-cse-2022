#!/usr/bin/env python3
"""
Validate content metadata consistency across _index.json files.

Checks:
1. Subject _index.json chapter titles vs module _index.json chapterTitle (mismatch/corruption)
2. Topic counts: subject _index.json topicCount vs actual topic dirs on disk
3. Module _index.json topic list vs actual topic dirs on disk
4. Corrupt/garbage titles (dates, template text, non-printable chars)
5. Missing _index.json files
6. Topic IDs in module _index.json vs actual topic directory names

Usage:
  python validate_metadata.py                # scan cse/
  python validate_metadata.py --branch ise   # scan ise/
  python validate_metadata.py --fix          # auto-fix title mismatches from module _index.json
"""

import json
import os
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

CONTENT_ROOT = Path(__file__).resolve().parent.parent


def is_corrupt_title(title: str) -> list[str]:
    """Check if a title looks corrupted. Returns list of reasons."""
    reasons = []
    if not title or not title.strip():
        reasons.append("empty title")
        return reasons

    # Date patterns (DD.MM.YYYY or YYYY-MM-DD)
    if re.search(r'\d{2}\.\d{2}\.\d{4}', title) or re.search(r'\d{4}-\d{2}-\d{2}', title):
        reasons.append("contains date pattern")

    # Template markers (case-sensitive to avoid false positives like "Templates")
    template_markers_exact = ['MKV-TEMPLATE', 'MKV-', 'IPCC', 'TODO', 'FIXME', 'PLACEHOLDER', 'DRAFT']
    title_upper = title.upper()
    for marker in template_markers_exact:
        if marker in title_upper:
            reasons.append(f"contains template marker '{marker}'")

    # Excessively long (normal titles are < 100 chars)
    if len(title) > 120:
        reasons.append(f"excessively long ({len(title)} chars)")

    # Contains file paths or extensions
    if re.search(r'\.[a-z]{2,4}(?:\s|$|,)', title, re.IGNORECASE):
        reasons.append("contains file extension pattern")

    # Multiple consecutive numbers (looks like data, not a title)
    if re.search(r'\d{5,}', title):
        reasons.append("contains long number sequence")

    # Non-ASCII control characters
    if any(ord(c) < 32 and c not in '\n\t' for c in title):
        reasons.append("contains control characters")

    return reasons


def validate_branch(branch: str, fix: bool = False) -> dict:
    """Validate all subjects in a branch. Returns summary stats."""
    branch_dir = CONTENT_ROOT / branch
    if not branch_dir.exists():
        print(f"Error: branch directory not found: {branch_dir}")
        sys.exit(1)

    issues = []
    stats = {
        'subjects': 0,
        'modules': 0,
        'topics_on_disk': 0,
        'title_mismatches': 0,
        'corrupt_titles': 0,
        'topic_count_mismatches': 0,
        'missing_index_files': 0,
        'orphan_topic_dirs': 0,
        'phantom_topics': 0,
    }

    # Find all subject dirs (contain _index.json)
    for sem_dir in sorted(branch_dir.iterdir()):
        if not sem_dir.is_dir() or sem_dir.name.startswith(('_', '.')):
            continue
        if sem_dir.name in ('__pycache__', 'reports', 'review_exports'):
            continue

        for subject_dir in sorted(sem_dir.iterdir()):
            if not subject_dir.is_dir() or subject_dir.name.startswith(('_', '.')):
                continue

            subject_index = subject_dir / '_index.json'
            if not subject_index.exists():
                continue

            stats['subjects'] += 1
            rel_subject = subject_dir.relative_to(CONTENT_ROOT)

            try:
                with open(subject_index) as f:
                    subject_data = json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                issues.append({
                    'type': 'CORRUPT_JSON',
                    'severity': 'ERROR',
                    'path': str(rel_subject / '_index.json'),
                    'detail': str(e),
                })
                continue

            chapters = subject_data.get('chapters', [])
            chapter_map = {ch['id']: ch for ch in chapters}

            # Check each module directory
            module_dirs = sorted([
                d for d in subject_dir.iterdir()
                if d.is_dir() and d.name.startswith('module-')
            ])

            for module_dir in module_dirs:
                stats['modules'] += 1
                module_id = module_dir.name
                rel_module = module_dir.relative_to(CONTENT_ROOT)

                # Check if module exists in subject _index.json
                if module_id not in chapter_map:
                    issues.append({
                        'type': 'ORPHAN_MODULE',
                        'severity': 'WARNING',
                        'path': str(rel_module),
                        'detail': f"Directory exists but not listed in subject _index.json",
                    })

                # Check module _index.json exists
                module_index = module_dir / '_index.json'
                if not module_index.exists():
                    stats['missing_index_files'] += 1
                    issues.append({
                        'type': 'MISSING_INDEX',
                        'severity': 'ERROR',
                        'path': str(rel_module / '_index.json'),
                        'detail': 'Module _index.json missing',
                    })
                    continue

                try:
                    with open(module_index) as f:
                        module_data = json.load(f)
                except (json.JSONDecodeError, IOError) as e:
                    issues.append({
                        'type': 'CORRUPT_JSON',
                        'severity': 'ERROR',
                        'path': str(rel_module / '_index.json'),
                        'detail': str(e),
                    })
                    continue

                module_title = module_data.get('chapterTitle', '')

                # === CHECK 1: Title corruption in subject _index.json ===
                if module_id in chapter_map:
                    subject_title = chapter_map[module_id].get('title', '')

                    # Check for corrupt title
                    corrupt_reasons = is_corrupt_title(subject_title)
                    if corrupt_reasons:
                        stats['corrupt_titles'] += 1
                        issues.append({
                            'type': 'CORRUPT_TITLE',
                            'severity': 'ERROR',
                            'path': str(rel_subject / '_index.json'),
                            'detail': f"Module '{module_id}' title is corrupt: {', '.join(corrupt_reasons)}",
                            'current': subject_title[:80] + ('...' if len(subject_title) > 80 else ''),
                            'expected': module_title,
                            'module_id': module_id,
                            'fix_file': str(subject_index),
                        })

                    # Check title mismatch (strip "Module N: " prefix for comparison)
                    subject_title_clean = re.sub(r'^Module\s+\d+:\s*', '', subject_title).strip()
                    if subject_title_clean and module_title and subject_title_clean.lower() != module_title.lower():
                        # Only flag if not already flagged as corrupt
                        if not corrupt_reasons:
                            stats['title_mismatches'] += 1
                            issues.append({
                                'type': 'TITLE_MISMATCH',
                                'severity': 'WARNING',
                                'path': str(rel_subject / '_index.json'),
                                'detail': f"Module '{module_id}' title differs from module _index.json",
                                'subject_title': subject_title,
                                'module_title': module_title,
                                'module_id': module_id,
                            })

                # === CHECK 2: Topic count mismatch ===
                topics_dir = module_dir / 'topics'
                actual_topic_dirs = []
                if topics_dir.exists():
                    actual_topic_dirs = sorted([
                        d.name for d in topics_dir.iterdir()
                        if d.is_dir() and not d.name.startswith(('_', '.'))
                    ])
                stats['topics_on_disk'] += len(actual_topic_dirs)

                # Check against subject _index.json topicCount
                if module_id in chapter_map:
                    expected_count = chapter_map[module_id].get('topicCount', 0)
                    if expected_count != len(actual_topic_dirs):
                        stats['topic_count_mismatches'] += 1
                        issues.append({
                            'type': 'TOPIC_COUNT_MISMATCH',
                            'severity': 'WARNING',
                            'path': str(rel_subject / '_index.json'),
                            'detail': f"Module '{module_id}': _index.json says {expected_count} topics, disk has {len(actual_topic_dirs)}",
                        })

                # === CHECK 3: Topic ID mismatches (module _index.json vs disk) ===
                module_topics = module_data.get('topics', [])
                index_topic_ids = {t['id'] for t in module_topics}
                disk_topic_ids = set(actual_topic_dirs)

                orphans = disk_topic_ids - index_topic_ids
                phantoms = index_topic_ids - disk_topic_ids

                if orphans:
                    stats['orphan_topic_dirs'] += len(orphans)
                    issues.append({
                        'type': 'ORPHAN_TOPICS',
                        'severity': 'WARNING',
                        'path': str(rel_module),
                        'detail': f"Topic dirs on disk but NOT in _index.json: {sorted(orphans)}",
                    })

                if phantoms:
                    stats['phantom_topics'] += len(phantoms)
                    issues.append({
                        'type': 'PHANTOM_TOPICS',
                        'severity': 'ERROR',
                        'path': str(rel_module),
                        'detail': f"Topics in _index.json but NO dir on disk: {sorted(phantoms)}",
                    })

            # Check for chapters in _index.json with no matching directory
            for ch in chapters:
                ch_dir = subject_dir / ch['id']
                if not ch_dir.exists():
                    issues.append({
                        'type': 'PHANTOM_MODULE',
                        'severity': 'ERROR',
                        'path': str(rel_subject),
                        'detail': f"Chapter '{ch['id']}' in _index.json but no directory on disk",
                    })

    # === AUTO-FIX corrupt titles ===
    if fix:
        fix_count = 0
        for issue in issues:
            if issue['type'] == 'CORRUPT_TITLE' and 'fix_file' in issue:
                fix_file = Path(issue['fix_file'])
                module_id = issue['module_id']
                expected = issue['expected']
                if not expected:
                    continue

                with open(fix_file) as f:
                    data = json.load(f)

                for ch in data.get('chapters', []):
                    if ch['id'] == module_id:
                        old = ch['title']
                        # Preserve "Module N: " prefix but avoid duplication
                        prefix_match = re.match(r'(Module\s+\d+:\s*)', old)
                        prefix = prefix_match.group(1) if prefix_match else f"Module {ch.get('order', '?')}: "
                        # Strip any existing prefix from the expected title
                        clean_expected = re.sub(r'^Module\s+\d+:\s*', '', expected).strip()
                        ch['title'] = f"{prefix}{clean_expected}"
                        fix_count += 1
                        break

                with open(fix_file, 'w') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                    f.write('\n')

        if fix_count:
            print(f"\n*** AUTO-FIXED {fix_count} corrupt title(s) ***\n")

    return stats, issues


def main():
    parser = argparse.ArgumentParser(description="Validate content metadata consistency")
    parser.add_argument("--branch", default="cse", help="Branch folder to scan (default: cse)")
    parser.add_argument("--fix", action="store_true", help="Auto-fix corrupt titles from module _index.json")
    args = parser.parse_args()

    stats, issues = validate_branch(args.branch, fix=args.fix)

    # Print report
    print("=" * 70)
    print(f"Metadata Validation Report: {args.branch}/")
    print(f"=" * 70)
    print(f"Subjects scanned:      {stats['subjects']}")
    print(f"Modules scanned:       {stats['modules']}")
    print(f"Topics on disk:        {stats['topics_on_disk']}")
    print(f"-" * 40)
    print(f"Corrupt titles:        {stats['corrupt_titles']}")
    print(f"Title mismatches:      {stats['title_mismatches']}")
    print(f"Topic count mismatches:{stats['topic_count_mismatches']}")
    print(f"Missing _index.json:   {stats['missing_index_files']}")
    print(f"Orphan topic dirs:     {stats['orphan_topic_dirs']}")
    print(f"Phantom topics:        {stats['phantom_topics']}")
    print(f"=" * 70)

    if not issues:
        print("\nAll metadata is consistent!")
        return

    # Group by severity
    errors = [i for i in issues if i['severity'] == 'ERROR']
    warnings = [i for i in issues if i['severity'] == 'WARNING']

    if errors:
        print(f"\n{'='*70}")
        print(f"ERRORS ({len(errors)})")
        print(f"{'='*70}")
        for i in errors:
            print(f"\n[{i['type']}] {i['path']}")
            print(f"  {i['detail']}")
            if 'current' in i:
                print(f"  Current:  {i['current']}")
            if 'expected' in i:
                print(f"  Expected: {i['expected']}")

    if warnings:
        print(f"\n{'='*70}")
        print(f"WARNINGS ({len(warnings)})")
        print(f"{'='*70}")
        for i in warnings:
            print(f"\n[{i['type']}] {i['path']}")
            print(f"  {i['detail']}")
            if 'subject_title' in i:
                print(f"  Subject _index: {i['subject_title']}")
                print(f"  Module _index:  {i['module_title']}")

    print(f"\n{'='*70}")
    if stats['corrupt_titles'] > 0 and not args.fix:
        print("TIP: Run with --fix to auto-repair corrupt titles from module _index.json")


if __name__ == "__main__":
    main()
