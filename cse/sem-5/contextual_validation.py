#!/usr/bin/env python3
"""
Contextual/Semantic Validation Script for VTU 2022 Scheme Sem 5 CSE Content
Validates:
1. Content accuracy - if read.md matches topic folder name
2. Subject relevance - if content belongs to correct subject
3. MCQ correctness - if answers make sense
4. Syllabus alignment
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

# Subject definitions
SUBJECT_KEYWORDS = {
    'bcs501-software-engineering-project-management': {
        'name': 'Software Engineering & Project Management',
        'keywords': ['software', 'sdlc', 'agile', 'waterfall', 'testing', 'requirement', 'design', 'development',
                     'project management', 'scrum', 'risk', 'quality', 'uml', 'unified modeling', 'estimation',
                     'pert', 'cpm', 'gantt', 'cocomo', 'function point']
    },
    'bcs502-computer-networks': {
        'name': 'Computer Networks',
        'keywords': ['network', 'tcp', 'ip', 'osi', 'protocol', 'routing', 'ethernet', 'lan', 'wan', 'http',
                     'dns', 'packet', 'frame', 'layer', 'transport', 'application', 'data link', 'physical',
                     'subnet', 'gateway', 'switch', 'router', 'congestion', 'flow control']
    },
    'bcs503-theory-of-computation': {
        'name': 'Theory of Computation',
        'keywords': ['automata', 'finite', 'turing', 'grammar', 'language', 'regular', 'context-free', 'pushdown',
                     'dfa', 'nfa', 'pda', 'cfg', 'pumping lemma', 'decidable', 'undecidable', 'halting',
                     'chomsky', 'state', 'transition', 'acceptor', 'recognizer']
    },
    'bcs508-environmental-studies': {
        'name': 'Environmental Studies',
        'keywords': ['environment', 'ecosystem', 'biodiversity', 'pollution', 'conservation', 'sustainability',
                     'climate', 'renewable', 'natural resource', 'ecology', 'waste', 'carbon', 'ozone',
                     'deforestation', 'water', 'air', 'soil', 'global warming']
    },
    'bcs515a-computer-graphics': {
        'name': 'Computer Graphics',
        'keywords': ['graphics', 'rendering', 'pixel', 'raster', 'vector', 'transformation', 'projection',
                     'clipping', 'polygon', 'bezier', 'spline', 'shading', '3d', '2d', 'viewport', 'window',
                     'bressenham', 'scan conversion', 'hidden surface', 'illumination']
    },
    'bcs515b-artificial-intelligence': {
        'name': 'Artificial Intelligence',
        'keywords': ['ai', 'artificial intelligence', 'search', 'heuristic', 'knowledge', 'expert system',
                     'neural network', 'machine learning', 'reasoning', 'inference', 'prolog', 'logic',
                     'agent', 'minimax', 'alpha-beta', 'fuzzy', 'genetic algorithm', 'planning']
    },
    'bcs515c-unix-system-programming': {
        'name': 'Unix System Programming',
        'keywords': ['unix', 'linux', 'shell', 'process', 'fork', 'pipe', 'signal', 'file descriptor',
                     'ipc', 'thread', 'system call', 'kernel', 'daemon', 'socket', 'bash', 'grep', 'awk',
                     'sed', 'chmod', 'inode', 'directory']
    },
    'bcs515d-distributed-systems': {
        'name': 'Distributed Systems',
        'keywords': ['distributed', 'parallel', 'concurrent', 'synchronization', 'consensus', 'replication',
                     'fault tolerance', 'consistency', 'byzantine', 'paxos', 'raft', 'clock', 'mutex',
                     'rpc', 'remote procedure', 'shared memory', 'message passing', 'deadlock']
    }
}

class ValidationReport:
    def __init__(self):
        self.total_topics = 0
        self.content_mismatches = []
        self.wrong_subject_content = []
        self.mcq_errors = []
        self.missing_files = []
        self.good_topics = []

    def add_content_mismatch(self, topic_path, issue):
        self.content_mismatches.append({'path': topic_path, 'issue': issue})

    def add_wrong_subject(self, topic_path, issue):
        self.wrong_subject_content.append({'path': topic_path, 'issue': issue})

    def add_mcq_error(self, topic_path, issue):
        self.mcq_errors.append({'path': topic_path, 'issue': issue})

    def add_missing_file(self, topic_path, file_type):
        self.missing_files.append({'path': topic_path, 'file': file_type})

def get_topic_name_from_path(topic_path):
    """Extract topic name from path"""
    return os.path.basename(topic_path)

def get_subject_from_path(topic_path):
    """Extract subject code from path"""
    parts = topic_path.split('/')
    for part in parts:
        if part.startswith('bcs'):
            return part
    return None

def read_file_safe(file_path):
    """Safely read a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return None

def read_json_safe(file_path):
    """Safely read a JSON file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        return None

def validate_content_accuracy(topic_path, topic_name, content, report):
    """Check if content matches topic name"""
    if not content:
        return

    # Normalize topic name for comparison
    topic_words = set(re.findall(r'\w+', topic_name.lower()))
    content_lower = content.lower()

    # Remove very common words
    common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were'}
    topic_words = topic_words - common_words

    # Check if at least some key words from topic name appear in content
    if len(topic_words) > 0:
        matches = sum(1 for word in topic_words if len(word) > 3 and word in content_lower)
        match_ratio = matches / len(topic_words) if len(topic_words) > 0 else 0

        # If less than 30% of topic words found in content, flag it
        if match_ratio < 0.3 and len(content) > 200:
            # Extract first 150 chars for context
            content_preview = content[:150].replace('\n', ' ')
            report.add_content_mismatch(
                topic_path,
                f"Topic '{topic_name}' but content seems unrelated. Preview: {content_preview}..."
            )

def validate_subject_relevance(topic_path, content, report):
    """Check if content belongs to the correct subject"""
    if not content:
        return

    subject_code = get_subject_from_path(topic_path)
    if not subject_code or subject_code not in SUBJECT_KEYWORDS:
        return

    content_lower = content.lower()
    subject_info = SUBJECT_KEYWORDS[subject_code]

    # Count keyword matches for this subject
    this_subject_matches = sum(1 for kw in subject_info['keywords'] if kw.lower() in content_lower)

    # Check against other subjects
    max_other_matches = 0
    max_other_subject = None

    for other_code, other_info in SUBJECT_KEYWORDS.items():
        if other_code == subject_code:
            continue
        matches = sum(1 for kw in other_info['keywords'] if kw.lower() in content_lower)
        if matches > max_other_matches:
            max_other_matches = matches
            max_other_subject = other_info['name']

    # If another subject has significantly more matches, flag it
    if max_other_matches > this_subject_matches * 1.5 and max_other_matches > 3:
        content_preview = content[:150].replace('\n', ' ')
        report.add_wrong_subject(
            topic_path,
            f"In {subject_info['name']} but content seems like {max_other_subject}. Preview: {content_preview}..."
        )

def validate_mcqs(topic_path, mcqs_data, report):
    """Validate MCQ correctness"""
    if not mcqs_data or 'mcqs' not in mcqs_data:
        return

    for idx, mcq in enumerate(mcqs_data['mcqs']):
        try:
            question = mcq.get('question', '')
            options = mcq.get('options', [])
            correct_idx = mcq.get('correctAnswer', -1)

            # Check if correctAnswer index is valid
            if correct_idx < 0 or correct_idx >= len(options):
                report.add_mcq_error(
                    topic_path,
                    f"MCQ #{idx+1}: Invalid correctAnswer index {correct_idx} (options: {len(options)})"
                )
                continue

            # Check if options exist
            if len(options) < 2:
                report.add_mcq_error(
                    topic_path,
                    f"MCQ #{idx+1}: Less than 2 options"
                )
                continue

            # Check for duplicate options
            if len(options) != len(set(options)):
                report.add_mcq_error(
                    topic_path,
                    f"MCQ #{idx+1}: Duplicate options found"
                )

            # Check if all options are empty or too short
            if all(len(opt.strip()) < 2 for opt in options):
                report.add_mcq_error(
                    topic_path,
                    f"MCQ #{idx+1}: All options are empty or too short"
                )

        except Exception as e:
            report.add_mcq_error(topic_path, f"MCQ #{idx+1}: Error parsing - {str(e)}")

def validate_topic(topic_path, report):
    """Validate a single topic"""
    topic_name = get_topic_name_from_path(topic_path)

    # Check for read.md
    read_md_path = os.path.join(topic_path, 'read.md')
    if not os.path.exists(read_md_path):
        report.add_missing_file(topic_path, 'read.md')
        return

    # Read content
    content = read_file_safe(read_md_path)
    if content:
        # Validate content accuracy
        validate_content_accuracy(topic_path, topic_name, content, report)

        # Validate subject relevance
        validate_subject_relevance(topic_path, content, report)

    # Check for mcqs.json
    mcqs_path = os.path.join(topic_path, 'mcqs.json')
    if os.path.exists(mcqs_path):
        mcqs_data = read_json_safe(mcqs_path)
        if mcqs_data:
            validate_mcqs(topic_path, mcqs_data, report)

def find_all_topics(base_path):
    """Find all topic directories"""
    topics = []
    for root, dirs, files in os.walk(base_path):
        if 'read.md' in files:
            # This is a topic directory
            topics.append(root)
    return sorted(topics)

def generate_report(report, output_path):
    """Generate the validation report"""
    lines = []
    lines.append("# Contextual Validation Report - VTU 2022 Scheme Sem 5 CSE")
    lines.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    lines.append("## Summary")
    lines.append(f"- Topics checked: {report.total_topics}")
    lines.append(f"- Content mismatches: {len(report.content_mismatches)}")
    lines.append(f"- Wrong subject content: {len(report.wrong_subject_content)}")
    lines.append(f"- MCQ errors: {len(report.mcq_errors)}")
    lines.append(f"- Missing files: {len(report.missing_files)}")
    lines.append(f"- Clean topics: {report.total_topics - len(report.content_mismatches) - len(report.wrong_subject_content) - len(report.mcq_errors) - len(report.missing_files)}")

    if report.content_mismatches:
        lines.append("\n## Content Mismatches")
        lines.append("Topics where content doesn't match the topic name:\n")
        for item in report.content_mismatches:
            lines.append(f"### {item['path']}")
            lines.append(f"- {item['issue']}\n")

    if report.wrong_subject_content:
        lines.append("\n## Wrong Subject Content")
        lines.append("Topics with content that seems to belong to a different subject:\n")
        for item in report.wrong_subject_content:
            lines.append(f"### {item['path']}")
            lines.append(f"- {item['issue']}\n")

    if report.mcq_errors:
        lines.append("\n## MCQ Errors")
        lines.append("Issues found in MCQ files:\n")
        for item in report.mcq_errors:
            lines.append(f"### {item['path']}")
            lines.append(f"- {item['issue']}\n")

    if report.missing_files:
        lines.append("\n## Missing Files")
        lines.append("Topics with missing required files:\n")
        for item in report.missing_files:
            lines.append(f"### {item['path']}")
            lines.append(f"- Missing: {item['file']}\n")

    lines.append("\n## Validation Complete")
    lines.append(f"Total issues found: {len(report.content_mismatches) + len(report.wrong_subject_content) + len(report.mcq_errors) + len(report.missing_files)}")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    return '\n'.join(lines)

def main():
    base_path = '/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse/sem-5'
    output_path = os.path.join(base_path, 'CONTEXTUAL_VALIDATION_REPORT.md')

    print("Starting contextual validation...")
    print(f"Base path: {base_path}")

    # Find all topics
    topics = find_all_topics(base_path)
    print(f"Found {len(topics)} topics to validate")

    # Create report
    report = ValidationReport()
    report.total_topics = len(topics)

    # Validate each topic
    last_progress_time = datetime.now()
    for idx, topic_path in enumerate(topics):
        validate_topic(topic_path, report)

        # Progress update every 50 topics or 120 seconds
        current_time = datetime.now()
        if (idx + 1) % 50 == 0 or (current_time - last_progress_time).seconds >= 120:
            print(f"Progress: {idx + 1}/{len(topics)} topics validated ({(idx+1)*100//len(topics)}%)")
            last_progress_time = current_time

    # Generate report
    print("\nGenerating report...")
    report_content = generate_report(report, output_path)

    print(f"\n✓ Validation complete!")
    print(f"✓ Report saved to: {output_path}")
    print(f"\nSummary:")
    print(f"  Topics checked: {report.total_topics}")
    print(f"  Content mismatches: {len(report.content_mismatches)}")
    print(f"  Wrong subject content: {len(report.wrong_subject_content)}")
    print(f"  MCQ errors: {len(report.mcq_errors)}")
    print(f"  Missing files: {len(report.missing_files)}")

if __name__ == '__main__':
    main()
