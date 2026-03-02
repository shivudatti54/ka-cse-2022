#!/usr/bin/env python3
"""
Generate topicContent.ts for all branches.
SVGs are imported as separate files (not embedded inline) to reduce bundle size.
Also generates contentLoader_additions.ts with imports, subject configs, and topic mappings.
"""

import os
import re
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path(__file__).resolve().parent.parent  # content-packs/ka-cse-2022/

BRANCHES = ['ise', 'aiml', 'aids', 'bca', 'mca', 'du_bsc_hons_cs', 'du_bsc_prog_cs', 'du_mca', 'du_msc_cs']

# Content files per topic (order matters for import naming)
CONTENT_FILES = [
    ('read.md', 'R'),
    ('code.json', 'C'),
    ('questions.json', 'Q'),
    ('memory.json', 'M'),
    ('mcqs.json', 'X'),
    ('flashcards.json', 'F'),
    ('visual.json', 'V'),
    ('purpose.md', 'P'),
    ('summary.md', 'S'),
]

# Material Design icons by subject keyword
ICON_MAP = {
    'math': 'calculator-variant',
    'algorithm': 'function-variant',
    'database': 'database',
    'network': 'lan',
    'security': 'key-variant',
    'web': 'web',
    'java': 'language-java',
    'python': 'language-python',
    'c++': 'language-cpp',
    'c-programming': 'language-c',
    'operating': 'cog-outline',
    'machine-learning': 'robot',
    'artificial-intelligence': 'brain',
    'ai': 'brain',
    'data-structure': 'graph-outline',
    'cloud': 'cloud-outline',
    'iot': 'devices',
    'internet-of-things': 'devices',
    'blockchain': 'link-variant',
    'compiler': 'code-braces',
    'software': 'cog',
    'computer-graphics': 'palette-outline',
    'vision': 'eye',
    'big-data': 'database',
    'full-stack': 'code-braces',
    'mobile': 'cellphone',
    'electronics': 'chip',
    'digital': 'chip',
    'microcontroller': 'chip',
    'environment': 'earth',
    'management': 'briefcase-variant',
    'communication': 'message-text',
    'statistics': 'chart-bar',
    'probability': 'dice-multiple',
    'discrete': 'math-compass',
    'graph-theory': 'graph-outline',
    'optimization': 'trending-up',
    'linear-algebra': 'matrix',
    'parallel': 'cpu-64-bit',
    'cryptography': 'key-variant',
    'theory-of-computation': 'state-machine',
    'deep-learning': 'brain',
    'natural-language': 'translate',
    'robotics': 'robot-industrial',
    'data-science': 'chart-scatter-plot',
    'data-visualization': 'chart-bar',
    'data-analytics': 'chart-scatter-plot',
    'data-mining': 'pickaxe',
    'image-processing': 'image-filter-vintage',
    'cyber': 'shield-lock',
    'accounting': 'calculator',
    'commerce': 'cart',
    'economics': 'currency-inr',
    'lab': 'flask',
    'green': 'leaf',
    'sustainability': 'leaf',
    'ui': 'palette-outline',
    'ux': 'palette-outline',
    'default': 'book-open-variant',
}

COLORS = [
    '#6366f1', '#dc2626', '#059669', '#f59e0b', '#3b82f6',
    '#7c3aed', '#0891b2', '#ea580c', '#16a34a', '#8b5cf6',
    '#d97706', '#ec4899', '#0284c7', '#22c55e', '#795548',
    '#2563eb', '#10b981', '#ef4444',
]


def strip_code_prefix(slug: str) -> str:
    """Strip course code prefix from directory slug.
    e.g., 'bcs301-mathematics-for-computer-science' -> 'mathematics-for-computer-science'
    Also handles DU codes: 'dsc01-foo' -> 'foo', 'ge1b-foo' -> 'foo', 'dse-cg-foo' -> 'foo'
    """
    # Standard pattern: letters+digits+optional_letters then hyphen
    match = re.match(r'^[a-z]+\d+[a-z]*-(.+)$', slug)
    if match:
        return match.group(1)
    # DU elective pattern: dse-XX-rest
    match2 = re.match(r'^[a-z]+-[a-z]+-(.+)$', slug)
    if match2:
        return match2.group(1)
    return slug


def get_icon(subject_slug: str) -> str:
    slug_lower = subject_slug.lower()
    for keyword, icon in ICON_MAP.items():
        if keyword in slug_lower:
            return icon
    return ICON_MAP['default']


def find_svg(topic_dir: Path) -> Path | None:
    """Find SVG file in topic's assets dir. Prefer -rich.svg."""
    assets_dir = topic_dir / 'assets'
    if not assets_dir.is_dir():
        return None
    svgs = sorted(assets_dir.glob('*-rich.svg'))
    if not svgs:
        svgs = sorted(assets_dir.glob('*.svg'))
    return svgs[0] if svgs else None


def scan_topics(branch_dir: Path) -> list:
    """Scan branch directory for all topics."""
    topics = []
    for sem_dir in sorted(branch_dir.iterdir()):
        if not sem_dir.is_dir() or not sem_dir.name.startswith('sem-'):
            continue
        for subject_dir in sorted(sem_dir.iterdir()):
            if not subject_dir.is_dir() or subject_dir.name.startswith('_'):
                continue
            for module_dir in sorted(subject_dir.iterdir()):
                if not module_dir.is_dir() or module_dir.name.startswith('_'):
                    continue
                topics_dir = module_dir / 'topics'
                if not topics_dir.is_dir():
                    continue
                for topic_dir in sorted(topics_dir.iterdir()):
                    if not topic_dir.is_dir() or not (topic_dir / 'read.md').exists():
                        continue
                    svg_path = find_svg(topic_dir)
                    topics.append({
                        'sem': sem_dir.name,
                        'subject_slug': subject_dir.name,
                        'subject_name': strip_code_prefix(subject_dir.name),
                        'module': module_dir.name,
                        'topic_slug': topic_dir.name,
                        'topic_dir': topic_dir,
                        'svg_path': svg_path,
                        'rel_path': f"./{sem_dir.name}/{subject_dir.name}/{module_dir.name}/topics/{topic_dir.name}",
                    })
    return topics


def generate_topic_content_ts(branch: str, topics: list, output_path: Path):
    """Generate topicContent.ts for a branch. SVGs are imported as files, not inlined."""
    lines = []
    now = datetime.now(timezone.utc).isoformat()
    svg_count = sum(1 for t in topics if t['svg_path'])

    lines.append(f'// Auto-generated topic content loader - {now}')
    lines.append(f'// Total topics: {len(topics)}, SVGs: {svg_count} (KA {branch.upper()} 2022 Scheme)')
    lines.append('')
    lines.append('// Topic imports')

    # Generate content file imports
    for i, topic in enumerate(topics, 1):
        rel = topic['rel_path']
        for filename, suffix in CONTENT_FILES:
            if (topic['topic_dir'] / filename).exists():
                lines.append(f"import t{i}{suffix} from '{rel}/{filename}';")

    lines.append('')
    lines.append('// SVG imports (loaded as raw strings by Metro transformer)')

    # Generate SVG imports (as separate file imports, not inline)
    for i, topic in enumerate(topics, 1):
        if topic['svg_path']:
            svg_rel = topic['svg_path'].relative_to(output_path.parent)
            lines.append(f"import s{i} from './{svg_rel}';")

    lines.append('')
    lines.append('// Topic content map')

    prefix = f"{branch}-"
    lines.append('const topicContent: Record<string, any> = {')

    for i, topic in enumerate(topics, 1):
        subject_id = f"{prefix}{topic['subject_name']}"
        topic_id = f"{subject_id}-{topic['module']}-{topic['topic_slug']}"

        lines.append(f"  '{topic_id}': {{")
        suffix_keys = {'R': 'read', 'C': 'code', 'Q': 'questions', 'M': 'memory',
                       'X': 'mcqs', 'F': 'flashcards', 'V': 'visual', 'P': 'purpose', 'S': 'summary'}
        for filename, suffix in CONTENT_FILES:
            if (topic['topic_dir'] / filename).exists():
                lines.append(f"    {suffix_keys[suffix]}: t{i}{suffix},")
        if topic['svg_path']:
            lines.append(f"    svgRaw: s{i},")
        lines.append('  },')

    lines.append('};')
    lines.append('')
    lines.append('export function getTopicContent(topicId: string) {')
    lines.append('  return topicContent[topicId] || null;')
    lines.append('}')
    lines.append('')
    lines.append('export function getAllTopicIds(): string[] {')
    lines.append('  return Object.keys(topicContent);')
    lines.append('}')
    lines.append('')

    output_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"  Generated {output_path.name} ({len(topics)} topics, {len(lines)} lines)")


def scan_subjects(branch: str, branch_dir: Path) -> list:
    """Scan for subjects in a branch directory."""
    subjects = []
    prefix = f"{branch}-"

    for sem_dir in sorted(branch_dir.iterdir()):
        if not sem_dir.is_dir() or not sem_dir.name.startswith('sem-'):
            continue
        sem_num = int(sem_dir.name.split('-')[1])

        for subject_dir in sorted(sem_dir.iterdir()):
            if not subject_dir.is_dir() or subject_dir.name.startswith('_'):
                continue
            if not (subject_dir / '_index.json').exists():
                continue

            meta = {}
            meta_path = subject_dir / '_meta.json'
            if meta_path.exists():
                try:
                    meta = json.loads(meta_path.read_text())
                except:
                    pass

            code = meta.get('code', subject_dir.name.split('-')[0].upper())
            # Support both 'name' (VTU style) and 'title' (DU style) in _meta.json
            name = meta.get('name', meta.get('title', strip_code_prefix(subject_dir.name).replace('-', ' ').title()))
            name_slug = strip_code_prefix(subject_dir.name)
            subject_id = f"{prefix}{name_slug}"

            # Scan modules/topics
            modules_with_topics = {}
            for module_dir in sorted(subject_dir.iterdir()):
                if not module_dir.is_dir() or module_dir.name.startswith('_'):
                    continue
                topics_dir = module_dir / 'topics'
                if topics_dir.is_dir():
                    topic_slugs = sorted([
                        t.name for t in topics_dir.iterdir()
                        if t.is_dir() and (t / 'read.md').exists()
                    ])
                    if topic_slugs:
                        modules_with_topics[module_dir.name] = topic_slugs

            import_var = re.sub(r'[^a-zA-Z0-9]', '', name_slug.replace('-', ''))

            subjects.append({
                'slug': subject_dir.name,
                'name_slug': name_slug,
                'id': subject_id,
                'code': code.upper(),
                'name': name,
                'sem': sem_num,
                'icon': get_icon(subject_dir.name),
                'modules': modules_with_topics,
                'import_var': import_var,
            })

    return subjects


def generate_content_loader_additions(branch: str, subjects: list) -> str:
    """Generate TypeScript additions for contentLoader.ts."""
    lines = []
    bup = branch.upper()

    # Import _index.json files
    lines.append(f'\n// {bup}-specific subject _index.json imports')
    for s in subjects:
        var = f"{branch}{s['import_var']}Chapters"
        path = f"../content-packs/ka-cse-2022/{branch}/sem-{s['sem']}/{s['slug']}/_index.json"
        lines.append(f"import {var} from '{path}';")

    # TopicContent import
    lines.append(f"\nimport {{ getTopicContent as get{bup}TopicContent }} from '../content-packs/ka-cse-2022/{branch}/topicContent';")

    # Subject configs
    lines.append(f'\n// {bup}-specific subjects ({len(subjects)} subjects)')
    lines.append(f'const {bup}_SUBJECTS: SubjectConfig[] = [')

    for i, s in enumerate(subjects):
        color = COLORS[i % len(COLORS)]
        var = f"{branch}{s['import_var']}Chapters"
        esc_name = s['name'].replace("'", "\\'")
        lines.append('  {')
        lines.append('    meta: {')
        lines.append(f"      id: '{s['id']}',")
        lines.append(f"      name: '{esc_name}',")
        lines.append(f"      description: '{esc_name} study material',")
        lines.append(f"      icon: '{s['icon']}',")
        lines.append(f"      color: '{color}',")
        lines.append('    },')
        lines.append(f"    chapters: {var},")
        lines.append(f"    category: 'Semester {s['sem']}',")
        lines.append(f"    categoryOrder: {s['sem']},")
        lines.append(f"    subjectCode: '{s['code']}',")
        lines.append('  },')

    lines.append('];')

    # ALL_SUBJECTS_MAP
    lines.append(f'\nfor (const s of {bup}_SUBJECTS) ALL_SUBJECTS_MAP[s.meta.id] = s;')

    # Topic mappings
    lines.append(f'\n// {bup} topic mappings (add to topicMappings object)')
    for s in subjects:
        for mod, topic_slugs in s['modules'].items():
            key = f"{s['id']}:{mod}"
            topics_str = ', '.join(f"'{t}'" for t in topic_slugs)
            lines.append(f"  '{key}': [{topics_str}],")

    return '\n'.join(lines)


def update_branch_map(branch: str, subjects: list):
    """Generate updated branch-map entries with prefixed IDs."""
    bm_path = BASE_DIR / 'branch-map.json'
    bm = json.loads(bm_path.read_text())

    config = bm['branches'].get(branch)
    if not config:
        print(f"  Warning: branch '{branch}' not in branch-map", file=sys.stderr)
        return

    # Build lookup: name_slug -> subject info
    subj_lookup = {}
    for s in subjects:
        subj_lookup[s['name_slug']] = s

    # Update subject IDs for branch-specific subjects
    updated = 0
    for sem, subj_list in config['subjects'].items():
        for entry in subj_list:
            if entry['location'] == branch:
                old_id = entry['id']
                new_id = f"{branch}-{old_id}"
                if not old_id.startswith(f"{branch}-"):
                    entry['id'] = new_id
                    updated += 1

    # Update freeSubjects too
    new_free = []
    for fid in config.get('freeSubjects', []):
        # Check if this is a branch-specific subject
        is_branch_specific = False
        for sem, subj_list in config['subjects'].items():
            for entry in subj_list:
                if entry['id'] == f"{branch}-{fid}" or (entry['id'] == fid and entry['location'] == branch):
                    is_branch_specific = True
                    break
        if is_branch_specific and not fid.startswith(f"{branch}-"):
            new_free.append(f"{branch}-{fid}")
        else:
            new_free.append(fid)
    config['freeSubjects'] = new_free

    bm_path.write_text(json.dumps(bm, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f"  Updated branch-map: {updated} subject IDs prefixed for {branch}")


def main():
    print(f"=== Generating content for {len(BRANCHES)} branches ===")
    print(f"Base: {BASE_DIR}")

    all_additions = []
    total_topics = 0
    total_subjects = 0

    for branch in BRANCHES:
        branch_dir = BASE_DIR / branch
        if not branch_dir.is_dir():
            print(f"Warning: {branch_dir} not found", file=sys.stderr)
            continue

        print(f"\n--- {branch.upper()} ---")

        # Scan topics
        topics = scan_topics(branch_dir)
        print(f"  {len(topics)} topics found")

        # Generate topicContent.ts
        output = branch_dir / 'topicContent.ts'
        generate_topic_content_ts(branch, topics, output)

        # Scan subjects
        subjects = scan_subjects(branch, branch_dir)
        print(f"  {len(subjects)} subjects found")

        # Generate contentLoader additions
        additions = generate_content_loader_additions(branch, subjects)
        all_additions.append(additions)

        # Update branch-map with prefixed IDs
        update_branch_map(branch, subjects)

        total_topics += len(topics)
        total_subjects += len(subjects)

    # Write all additions
    out = BASE_DIR / 'scripts' / 'contentLoader_additions.ts'
    out.write_text('\n'.join(all_additions), encoding='utf-8')

    print(f"\n=== Done ===")
    print(f"Total: {total_topics} topics, {total_subjects} subjects, {len(BRANCHES)} branches")
    print(f"Additions: {out}")

    # Show file sizes
    print(f"\ntopicContent.ts sizes:")
    for branch in BRANCHES:
        path = BASE_DIR / branch / 'topicContent.ts'
        if path.exists():
            size_mb = path.stat().st_size / 1024 / 1024
            print(f"  {branch}: {size_mb:.1f} MB")


if __name__ == '__main__':
    main()
