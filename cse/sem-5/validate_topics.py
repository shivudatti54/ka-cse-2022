#!/usr/bin/env python3
"""
VTU Content Validator - Systematically validate all topics in Sem 5 CSE
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

class VTUContentValidator:
    def __init__(self, sem_path: str):
        self.sem_path = Path(sem_path)
        self.stats = {
            'total_topics': 0,
            'valid_topics': 0,
            'fixed_topics': 0,
            'error_topics': 0,
            'missing_files': [],
            'json_errors': [],
            'svg_errors': [],
            'external_links': [],
            'fake_citations': [],
        }
        self.start_time = datetime.now()

    def validate_json_structure(self, file_path: Path, json_type: str) -> Tuple[bool, List[str]]:
        """Validate MCQs or Flashcards JSON structure"""
        issues = []

        if not file_path.exists():
            return False, [f"File not found: {file_path.name}"]

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            return False, [f"Invalid JSON: {str(e)}"]

        # Check structure
        if json_type == 'mcqs':
            if isinstance(data, list):
                issues.append("MCQs stored as array - needs topicId wrapper")
                return False, issues

            if 'topicId' not in data:
                issues.append("Missing topicId field")

            if 'mcqs' not in data:
                issues.append("Missing mcqs array")
                return False, issues

            mcqs = data.get('mcqs', [])
            if len(mcqs) < 5:
                issues.append(f"Only {len(mcqs)} MCQs (need 5+)")

            for idx, mcq in enumerate(mcqs):
                if 'question' not in mcq:
                    issues.append(f"MCQ {idx}: missing question")
                if 'options' not in mcq:
                    issues.append(f"MCQ {idx}: missing options")
                if 'correctAnswer' not in mcq:
                    issues.append(f"MCQ {idx}: missing correctAnswer")
                elif isinstance(mcq['correctAnswer'], str):
                    issues.append(f"MCQ {idx}: correctAnswer is string, should be number")
                if 'explanation' not in mcq:
                    issues.append(f"MCQ {idx}: missing explanation")

        elif json_type == 'flashcards':
            if isinstance(data, list):
                issues.append("Flashcards stored as array - needs topicId wrapper")
                return False, issues

            if 'topicId' not in data:
                issues.append("Missing topicId field")

            if 'flashcards' not in data:
                issues.append("Missing flashcards array")
                return False, issues

            cards = data.get('flashcards', [])
            if len(cards) < 5:
                issues.append(f"Only {len(cards)} flashcards (need 5+)")

            for idx, card in enumerate(cards):
                if 'front' not in card:
                    issues.append(f"Card {idx}: missing front")
                if 'back' not in card:
                    issues.append(f"Card {idx}: missing back")

        return len(issues) == 0, issues

    def check_external_links(self, file_path: Path) -> List[str]:
        """Check for external links in markdown"""
        if not file_path.exists():
            return []

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find external image links
        external_images = re.findall(r'!\[.*?\]\((https?://.*?)\)', content)

        # Find external URLs in Further Reading sections
        fake_citations = []
        if 'Further Reading' in content or 'References' in content:
            lines = content.split('\n')
            in_reading_section = False
            for line in lines:
                if 'Further Reading' in line or 'References' in line:
                    in_reading_section = True
                elif line.startswith('#'):
                    in_reading_section = False
                elif in_reading_section and 'http' in line:
                    fake_citations.append(line.strip())

        return external_images + fake_citations

    def validate_svg(self, file_path: Path) -> Tuple[bool, List[str]]:
        """Validate SVG structure"""
        issues = []

        if not file_path.exists():
            return False, ["SVG file not found"]

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for required attributes
        if 'xmlns="http://www.w3.org/2000/svg"' not in content:
            issues.append("Missing xmlns attribute")

        if 'data-topic-id' not in content:
            issues.append("Missing data-topic-id attribute")

        # Check for narration sections
        narration_count = content.count('data-narration=')
        if narration_count < 4:
            issues.append(f"Only {narration_count} narration sections (need 4+)")

        # Check for HTML elements (should not be in SVG)
        # Use word boundaries to avoid false positives with linearGradient
        html_elements = [
            (r'<div[\s>]', '<div'),
            (r'<section[\s>]', '<section'),
            (r'<ul[\s>]', '<ul'),
            (r'<li[\s>]', '<li'),
            (r'<footer[\s>]', '<footer'),
            (r'<header[\s>]', '<header'),
            (r'<p[\s>]', '<p'),
            (r'</ul>', '</ul>'),
            (r'</ol>', '</ol>'),
            (r'</li>', '</li>'),
        ]
        for pattern, element_name in html_elements:
            if re.search(pattern, content):
                issues.append(f"Contains HTML element: {element_name}")

        return len(issues) == 0, issues

    def validate_topic(self, topic_path: Path) -> Dict:
        """Validate a single topic folder"""
        result = {
            'path': str(topic_path),
            'name': topic_path.name,
            'valid': True,
            'issues': [],
            'fixed': False
        }

        # Check required files
        required_files = ['read.md', 'mcqs.json', 'flashcards.json', 'visual.json']
        for file_name in required_files:
            file_path = topic_path / file_name
            if not file_path.exists():
                result['issues'].append(f"Missing {file_name}")
                result['valid'] = False

        # Check SVG
        svg_path = topic_path / 'assets' / f"{topic_path.name}.svg"
        if not svg_path.exists():
            result['issues'].append(f"Missing SVG: {svg_path.name}")
            result['valid'] = False
        else:
            svg_valid, svg_issues = self.validate_svg(svg_path)
            if not svg_valid:
                result['issues'].extend([f"SVG: {issue}" for issue in svg_issues])
                result['valid'] = False

        # Validate MCQs
        mcqs_path = topic_path / 'mcqs.json'
        if mcqs_path.exists():
            mcqs_valid, mcqs_issues = self.validate_json_structure(mcqs_path, 'mcqs')
            if not mcqs_valid:
                result['issues'].extend([f"MCQs: {issue}" for issue in mcqs_issues])
                result['valid'] = False

        # Validate Flashcards
        flashcards_path = topic_path / 'flashcards.json'
        if flashcards_path.exists():
            fc_valid, fc_issues = self.validate_json_structure(flashcards_path, 'flashcards')
            if not fc_valid:
                result['issues'].extend([f"Flashcards: {issue}" for issue in fc_issues])
                result['valid'] = False

        # Check for external links
        read_md_path = topic_path / 'read.md'
        if read_md_path.exists():
            external = self.check_external_links(read_md_path)
            if external:
                result['issues'].extend([f"External link: {link}" for link in external])
                result['valid'] = False

        return result

    def validate_all(self):
        """Validate all topics in all subjects"""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting validation...")
        print("=" * 60)

        subjects = sorted([d for d in self.sem_path.iterdir() if d.is_dir()])

        all_results = []

        for subject in subjects:
            print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Subject: {subject.name}")

            chapters_path = subject / 'chapters'
            if not chapters_path.exists():
                print(f"  WARNING: No chapters folder found")
                continue

            modules = sorted([d for d in chapters_path.iterdir() if d.is_dir() and d.name.startswith('module-')])

            for module in modules:
                topics_folder = module / 'topics'
                if not topics_folder.exists():
                    continue
                topics = sorted([d for d in topics_folder.iterdir() if d.is_dir() and not d.name.startswith('.')])

                print(f"  {module.name}: {len(topics)} topics")

                for topic in topics:
                    self.stats['total_topics'] += 1
                    result = self.validate_topic(topic)
                    all_results.append(result)

                    if result['valid']:
                        self.stats['valid_topics'] += 1
                    else:
                        self.stats['error_topics'] += 1
                        print(f"    ✗ {topic.name}: {len(result['issues'])} issues")

        return all_results

    def generate_report(self, results: List[Dict]) -> str:
        """Generate validation report"""
        report = []
        report.append("# VTU 2022 Scheme Sem 5 CSE - Validation Report")
        report.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("\n## Summary Statistics")
        report.append(f"- Total Topics: {self.stats['total_topics']}")
        report.append(f"- Valid Topics: {self.stats['valid_topics']} ({self.stats['valid_topics']/self.stats['total_topics']*100:.1f}%)")
        report.append(f"- Topics with Issues: {self.stats['error_topics']} ({self.stats['error_topics']/self.stats['total_topics']*100:.1f}%)")

        report.append("\n## Topics with Issues")

        for result in results:
            if not result['valid']:
                report.append(f"\n### {result['name']}")
                report.append(f"Path: `{result['path']}`")
                report.append("\nIssues:")
                for issue in result['issues']:
                    report.append(f"- {issue}")

        return '\n'.join(report)

if __name__ == '__main__':
    sem_path = '/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse/sem-5'

    validator = VTUContentValidator(sem_path)
    results = validator.validate_all()

    print("\n" + "=" * 60)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] VALIDATION COMPLETE")
    print("=" * 60)
    print(f"Total Topics: {validator.stats['total_topics']}")
    print(f"Valid: {validator.stats['valid_topics']} ({validator.stats['valid_topics']/validator.stats['total_topics']*100:.1f}%)")
    print(f"Issues: {validator.stats['error_topics']} ({validator.stats['error_topics']/validator.stats['total_topics']*100:.1f}%)")

    # Generate report
    report = validator.generate_report(results)
    report_path = Path(sem_path) / 'VALIDATION_REPORT.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nReport saved to: {report_path}")
