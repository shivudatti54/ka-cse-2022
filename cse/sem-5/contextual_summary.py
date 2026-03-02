#!/usr/bin/env python3
"""
Generate a summary of contextual validation issues by subject
"""

import json
from collections import defaultdict
from pathlib import Path

def extract_subject_from_path(path):
    """Extract subject code from path"""
    parts = path.split('/')
    for part in parts:
        if part.startswith('bcs'):
            return part
    return 'Unknown'

def main():
    base_path = '/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse/sem-5'
    report_path = f'{base_path}/CONTEXTUAL_VALIDATION_REPORT.md'

    # Parse the report
    content_mismatches = []
    wrong_subject = []
    mcq_errors_unique_topics = set()

    with open(report_path, 'r') as f:
        lines = f.readlines()

    current_section = None
    current_path = None

    for line in lines:
        line = line.strip()

        if line == '## Content Mismatches':
            current_section = 'content'
        elif line == '## Wrong Subject Content':
            current_section = 'subject'
        elif line == '## MCQ Errors':
            current_section = 'mcq'
        elif line.startswith('### /Users/'):
            current_path = line[4:]  # Remove "### "

            if current_section == 'content':
                content_mismatches.append(current_path)
            elif current_section == 'subject':
                wrong_subject.append(current_path)
            elif current_section == 'mcq':
                mcq_errors_unique_topics.add(current_path)

    # Count by subject
    subjects = {
        'bcs501-software-engineering-project-management': 'Software Engineering & PM',
        'bcs502-computer-networks': 'Computer Networks',
        'bcs503-theory-of-computation': 'Theory of Computation',
        'bcs508-environmental-studies': 'Environmental Studies',
        'bcs515a-computer-graphics': 'Computer Graphics',
        'bcs515b-artificial-intelligence': 'Artificial Intelligence',
        'bcs515c-unix-system-programming': 'Unix System Programming',
        'bcs515d-distributed-systems': 'Distributed Systems'
    }

    # Statistics by subject
    stats = defaultdict(lambda: {'content_mismatch': 0, 'wrong_subject': 0, 'mcq_errors': 0})

    for path in content_mismatches:
        subject = extract_subject_from_path(path)
        stats[subject]['content_mismatch'] += 1

    for path in wrong_subject:
        subject = extract_subject_from_path(path)
        stats[subject]['wrong_subject'] += 1

    for path in mcq_errors_unique_topics:
        subject = extract_subject_from_path(path)
        stats[subject]['mcq_errors'] += 1

    # Print summary
    print("\n" + "="*80)
    print("CONTEXTUAL VALIDATION SUMMARY BY SUBJECT")
    print("="*80 + "\n")

    print(f"{'Subject':<40} {'Content':<10} {'Wrong':<10} {'MCQ':<10} {'Total':<10}")
    print(f"{'':40} {'Mismatch':<10} {'Subject':<10} {'Errors':<10} {'Issues':<10}")
    print("-" * 80)

    total_content = 0
    total_wrong = 0
    total_mcq = 0

    for subject_code in sorted(subjects.keys()):
        subject_name = subjects[subject_code]
        s = stats[subject_code]
        total = s['content_mismatch'] + s['wrong_subject'] + s['mcq_errors']

        total_content += s['content_mismatch']
        total_wrong += s['wrong_subject']
        total_mcq += s['mcq_errors']

        print(f"{subject_name:<40} {s['content_mismatch']:<10} {s['wrong_subject']:<10} {s['mcq_errors']:<10} {total:<10}")

    print("-" * 80)
    total_all = total_content + total_wrong + total_mcq
    print(f"{'TOTAL':<40} {total_content:<10} {total_wrong:<10} {total_mcq:<10} {total_all:<10}")

    print("\n" + "="*80)
    print("KEY FINDINGS")
    print("="*80 + "\n")

    print(f"1. Content Mismatches: {len(content_mismatches)} topics")
    print("   - Topic name doesn't match actual content")
    print("   - May indicate wrong content was added to topic\n")

    print(f"2. Wrong Subject Content: {len(wrong_subject)} topics")
    print("   - Content belongs to a different subject entirely")
    print("   - Serious issue requiring content replacement\n")

    print(f"3. MCQ Format Errors: {len(mcq_errors_unique_topics)} topics")
    print("   - All errors are due to options stored as objects {key, text}")
    print("   - This is a DATA FORMAT issue, not content quality issue")
    print("   - MCQ validation script needs to be updated\n")

    # Most problematic subjects
    print("="*80)
    print("SUBJECTS NEEDING MOST ATTENTION")
    print("="*80 + "\n")

    subject_totals = []
    for subject_code in subjects.keys():
        s = stats[subject_code]
        # Exclude MCQ errors from this calculation since they're format issues
        real_issues = s['content_mismatch'] + s['wrong_subject']
        if real_issues > 0:
            subject_totals.append((subjects[subject_code], real_issues, s['content_mismatch'], s['wrong_subject']))

    subject_totals.sort(key=lambda x: x[1], reverse=True)

    for subject_name, total, content, wrong in subject_totals:
        print(f"{subject_name}:")
        print(f"  - {content} content mismatches")
        print(f"  - {wrong} wrong subject issues")
        print(f"  - Total content issues: {total}\n")

if __name__ == '__main__':
    main()
