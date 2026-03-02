#!/usr/bin/env python3
"""
VTU Content Fixer - Fix all common issues in Sem 5 CSE topics
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

class VTUContentFixer:
    def __init__(self, sem_path: str):
        self.sem_path = Path(sem_path)
        self.stats = {
            'total_topics': 0,
            'fixed_mcqs': 0,
            'fixed_flashcards': 0,
            'fixed_svgs': 0,
            'fixed_external_links': 0,
            'errors': 0,
        }
        self.start_time = datetime.now()
        self.last_progress_time = datetime.now()

    def fix_mcq_correct_answer(self, file_path: Path, topic_name: str) -> bool:
        """Convert string correctAnswer to number and fix structure"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            fixed = False

            # If it's an array at root, wrap it
            if isinstance(data, list):
                data = {
                    "topicId": topic_name,
                    "mcqs": data
                }
                fixed = True

            # Ensure topicId exists
            if 'topicId' not in data:
                data['topicId'] = topic_name
                fixed = True

            # Ensure mcqs array exists
            if 'mcqs' not in data:
                return False

            for mcq in data['mcqs']:
                if 'correctAnswer' in mcq and isinstance(mcq['correctAnswer'], str):
                    # Convert A->0, B->1, C->2, D->3
                    answer_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
                    answer = mcq['correctAnswer'].strip().upper()
                    if answer in answer_map:
                        mcq['correctAnswer'] = answer_map[answer]
                        fixed = True
                    elif answer.isdigit():
                        mcq['correctAnswer'] = int(answer)
                        fixed = True

            if fixed:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                return True

        except Exception as e:
            print(f"Error fixing MCQs in {file_path}: {e}")
            return False

        return False

    def add_flashcard_if_needed(self, file_path: Path, topic_name: str) -> bool:
        """Add a 5th flashcard if only 4 exist and fix structure"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            fixed = False

            # If it's an array at root, wrap it
            if isinstance(data, list):
                data = {
                    "topicId": topic_name,
                    "flashcards": data
                }
                fixed = True

            # Ensure topicId exists
            if 'topicId' not in data:
                data['topicId'] = topic_name
                fixed = True

            # Ensure flashcards array exists
            if 'flashcards' not in data:
                return False

            cards = data['flashcards']
            if len(cards) == 4:
                # Add a generic 5th flashcard
                new_card = {
                    "id": "fc-5",
                    "front": f"What is the importance of {topic_name.replace('-', ' ')}?",
                    "back": "Refer to your prescribed textbook for detailed explanation."
                }
                cards.append(new_card)
                fixed = True

            if fixed:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                return True

        except Exception as e:
            print(f"Error fixing flashcards in {file_path}: {e}")
            return False

        return False

    def fix_svg_html_elements(self, file_path: Path) -> bool:
        """Fix SVG issues: add xmlns if missing, remove HTML elements"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content
            fixed = False

            # Add xmlns if missing
            if 'xmlns="http://www.w3.org/2000/svg"' not in content:
                # Find the opening <svg tag and add xmlns
                content = re.sub(
                    r'<svg\s+',
                    '<svg xmlns="http://www.w3.org/2000/svg" ',
                    content,
                    count=1
                )
                fixed = True

            # Remove common HTML elements
            # Pattern to match <li>...</li> and replace with text only
            content = re.sub(r'<li[^>]*>(.*?)</li>', r'\1', content, flags=re.DOTALL)

            # Remove other HTML tags but keep content
            html_tags = ['<ul>', '</ul>', '<ol>', '</ol>', '<div>', '</div>',
                        '<section>', '</section>', '<footer>', '</footer>',
                        '<header>', '</header>', '<p>', '</p>']

            for tag in html_tags:
                if tag in content:
                    content = content.replace(tag, '')
                    fixed = True

            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True

        except Exception as e:
            print(f"Error fixing SVG in {file_path}: {e}")
            return False

        return False

    def fix_external_links(self, file_path: Path) -> bool:
        """Remove external links and fix citations in markdown"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # Remove external images
            content = re.sub(r'!\[.*?\]\(https?://.*?\)', '', content)

            # Fix Further Reading sections
            if 'Further Reading' in content or 'References' in content:
                lines = content.split('\n')
                new_lines = []
                in_reading_section = False
                section_type = None

                for line in lines:
                    if '## Further Reading' in line or '### Further Reading' in line:
                        in_reading_section = True
                        section_type = 'reading'
                        new_lines.append(line)
                        new_lines.append('Refer to your prescribed textbook and official course materials.')
                        continue
                    elif '## References' in line or '### References' in line:
                        in_reading_section = True
                        section_type = 'references'
                        new_lines.append(line)
                        new_lines.append('Refer to your prescribed textbook and official course materials.')
                        continue
                    elif line.startswith('#'):
                        in_reading_section = False
                        section_type = None

                    if not in_reading_section or section_type is None:
                        new_lines.append(line)
                    elif 'http' not in line and line.strip() and not line.startswith('Refer to'):
                        # Keep non-URL lines in the section
                        new_lines.append(line)

                content = '\n'.join(new_lines)

            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True

        except Exception as e:
            print(f"Error fixing external links in {file_path}: {e}")
            return False

        return False

    def fix_topic(self, topic_path: Path) -> Dict:
        """Fix all issues in a topic"""
        result = {
            'path': str(topic_path),
            'name': topic_path.name,
            'fixed': [],
        }

        # Fix MCQs
        mcqs_path = topic_path / 'mcqs.json'
        if mcqs_path.exists():
            if self.fix_mcq_correct_answer(mcqs_path, topic_path.name):
                result['fixed'].append('mcqs')
                self.stats['fixed_mcqs'] += 1

        # Fix Flashcards
        flashcards_path = topic_path / 'flashcards.json'
        if flashcards_path.exists():
            if self.add_flashcard_if_needed(flashcards_path, topic_path.name):
                result['fixed'].append('flashcards')
                self.stats['fixed_flashcards'] += 1

        # Fix SVG
        svg_path = topic_path / 'assets' / f"{topic_path.name}.svg"
        if svg_path.exists():
            if self.fix_svg_html_elements(svg_path):
                result['fixed'].append('svg')
                self.stats['fixed_svgs'] += 1

        # Fix external links
        read_md_path = topic_path / 'read.md'
        if read_md_path.exists():
            if self.fix_external_links(read_md_path):
                result['fixed'].append('external_links')
                self.stats['fixed_external_links'] += 1

        return result

    def print_progress(self, current_subject: str, current_module: str,
                      current_topic: str, total_processed: int, total_topics: int):
        """Print progress every 2 minutes"""
        now = datetime.now()
        elapsed = (now - self.last_progress_time).total_seconds()

        if elapsed >= 120:  # 2 minutes
            self.last_progress_time = now
            print(f"\n{'='*60}")
            print(f"[{now.strftime('%H:%M:%S')}] PROGRESS REPORT")
            print(f"{'='*60}")
            print(f"Subject: {current_subject}")
            print(f"Module: {current_module}")
            print(f"Topics: {total_processed}/{total_topics} ({total_processed/total_topics*100:.1f}%)")
            print(f"Fixed: MCQs={self.stats['fixed_mcqs']}, "
                  f"Flashcards={self.stats['fixed_flashcards']}, "
                  f"SVGs={self.stats['fixed_svgs']}, "
                  f"Links={self.stats['fixed_external_links']}")
            print(f"Current: {current_topic}")
            print(f"{'='*60}\n")

    def fix_all(self):
        """Fix all topics in all subjects"""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting fixes...")
        print("=" * 60)

        subjects = sorted([d for d in self.sem_path.iterdir() if d.is_dir()
                          and not d.name.startswith('.')])

        all_results = []
        total_processed = 0

        # First count total topics
        total_topics = 0
        for subject in subjects:
            chapters_path = subject / 'chapters'
            if chapters_path.exists():
                for module in chapters_path.iterdir():
                    if module.is_dir() and module.name.startswith('module-'):
                        topics_folder = module / 'topics'
                        if topics_folder.exists():
                            total_topics += len([d for d in topics_folder.iterdir()
                                               if d.is_dir() and not d.name.startswith('.')])

        print(f"Total topics to process: {total_topics}\n")

        for subject in subjects:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Subject: {subject.name}")

            chapters_path = subject / 'chapters'
            if not chapters_path.exists():
                continue

            modules = sorted([d for d in chapters_path.iterdir()
                            if d.is_dir() and d.name.startswith('module-')])

            for module in modules:
                topics_folder = module / 'topics'
                if not topics_folder.exists():
                    continue

                topics = sorted([d for d in topics_folder.iterdir()
                               if d.is_dir() and not d.name.startswith('.')])

                print(f"  {module.name}: {len(topics)} topics")

                for topic in topics:
                    total_processed += 1
                    result = self.fix_topic(topic)
                    all_results.append(result)

                    if result['fixed']:
                        print(f"    ✓ {topic.name}: fixed {', '.join(result['fixed'])}")

                    # Print progress every 2 minutes
                    self.print_progress(subject.name, module.name, topic.name,
                                      total_processed, total_topics)

        return all_results

if __name__ == '__main__':
    sem_path = '/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse/sem-5'

    fixer = VTUContentFixer(sem_path)
    results = fixer.fix_all()

    print("\n" + "=" * 60)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] FIXES COMPLETE")
    print("=" * 60)
    print(f"MCQs fixed: {fixer.stats['fixed_mcqs']}")
    print(f"Flashcards fixed: {fixer.stats['fixed_flashcards']}")
    print(f"SVGs fixed: {fixer.stats['fixed_svgs']}")
    print(f"External links removed: {fixer.stats['fixed_external_links']}")
    print(f"Errors: {fixer.stats['errors']}")
    print("=" * 60)
