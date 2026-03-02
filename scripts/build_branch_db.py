#!/usr/bin/env python3
"""
build_branch_db.py — Builds a per-branch content.db from branch-map.json.

Walks content directories (cse/, ise/, aiml/, etc.) and builds a SQLite DB
containing only the subjects mapped to the specified branch.

Usage:
    python3 scripts/build_branch_db.py ise
    python3 scripts/build_branch_db.py aiml
    python3 scripts/build_branch_db.py cse   # same as build_content_db.py
"""

import hashlib
import json
import re
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

# Resolve paths relative to this script
SCRIPT_DIR = Path(__file__).resolve().parent
CONTENT_PACK_DIR = SCRIPT_DIR.parent  # ka-cse-2022/
APP_ROOT = CONTENT_PACK_DIR.parent.parent  # study-app-template/
OUTPUT_DIR = APP_ROOT / "assets" / "data"

# Reuse icon/color map from build_content_db.py
SUBJECTS_EXTRA = {
    "mathematics-for-computer-science": {"icon": "calculator-variant", "color": "#6366f1"},
    "digital-design-and-computer-organization": {"icon": "chip", "color": "#dc2626"},
    "operating-systems": {"icon": "cog-outline", "color": "#7c3aed"},
    "data-structures-and-applications": {"icon": "graph-outline", "color": "#059669"},
    "object-oriented-programming-with-java": {"icon": "language-java", "color": "#ea580c"},
    "object-oriented-programming-with-c++": {"icon": "language-cpp", "color": "#3b82f6"},
    "analysis-design-of-algorithms": {"icon": "function-variant", "color": "#16a34a"},
    "microcontrollers": {"icon": "chip", "color": "#795548"},
    "database-management-system": {"icon": "database", "color": "#ea580c"},
    "discrete-mathematical-structures": {"icon": "math-compass", "color": "#6366f1"},
    "graph-theory": {"icon": "graph-outline", "color": "#0891b2"},
    "optimization-technique": {"icon": "trending-up", "color": "#d97706"},
    "linear-algebra": {"icon": "matrix", "color": "#8b5cf6"},
    "green-it-and-sustainability": {"icon": "leaf", "color": "#10b981"},
    "capacity-planning-for-it": {"icon": "chart-bar", "color": "#f59e0b"},
    "uiux": {"icon": "palette-outline", "color": "#ec4899"},
    "software-engineering-project-management": {"icon": "cog", "color": "#8b5cf6"},
    "computer-networks": {"icon": "lan", "color": "#0284c7"},
    "theory-of-computation": {"icon": "state-machine", "color": "#d97706"},
    "environmental-studies": {"icon": "earth", "color": "#22c55e"},
    "computer-graphics": {"icon": "image", "color": "#2563eb"},
    "artificial-intelligence": {"icon": "robot", "color": "#7c3aed"},
    "unix-system-programming": {"icon": "console", "color": "#475569"},
    "distributed-systems": {"icon": "lan", "color": "#0891b2"},
    "introduction-to-artificial-intelligence": {"icon": "robot", "color": "#7c3aed"},
    "cloud-computing": {"icon": "cloud-outline", "color": "#3b82f6"},
    "machine-learning": {"icon": "chart-scatter-plot", "color": "#2563eb"},
    "blockchain-technology": {"icon": "link-variant", "color": "#2563eb"},
    "computer-vision": {"icon": "eye", "color": "#0891b2"},
    "compiler-design": {"icon": "code-braces", "color": "#9333ea"},
    "advanced-java": {"icon": "language-java", "color": "#ea580c"},
    "introduction-to-data-structures": {"icon": "graph-outline", "color": "#059669"},
    "fundamentals-of-operating-systems": {"icon": "cog-outline", "color": "#7c3aed"},
    "mobile-application-development": {"icon": "cellphone", "color": "#14b8a6"},
    "internet-of-things": {"icon": "devices", "color": "#2563eb"},
    "parallel-computing": {"icon": "server-network", "color": "#6366f1"},
    "cryptography-network-security": {"icon": "key-variant", "color": "#7c3aed"},
    # ISE-specific
    "ise-data-visualization-lab": {"icon": "chart-bar", "color": "#f59e0b"},
    "ise-computer-vision": {"icon": "eye", "color": "#0891b2"},
    "ise-full-stack-development": {"icon": "web", "color": "#059669"},
    "ise-internet-of-things": {"icon": "devices", "color": "#2563eb"},
    "ise-cloud-computing-and-security": {"icon": "cloud-lock-outline", "color": "#3b82f6"},
    "ise-big-data-analytics": {"icon": "database-search", "color": "#dc2626"},
    "ise-information-and-network-security": {"icon": "shield-lock-outline", "color": "#7c3aed"},
    # AIML-specific
    "aiml-computer-vision": {"icon": "eye", "color": "#0891b2"},
    "aiml-exploratory-data-analysis": {"icon": "chart-scatter-plot", "color": "#f59e0b"},
    "aiml-big-data-analytics": {"icon": "database-search", "color": "#dc2626"},
    "aiml-natural-language-processing": {"icon": "text-recognition", "color": "#7c3aed"},
    "aiml-deep-learning": {"icon": "brain", "color": "#ec4899"},
    # AIDS-specific
    "aids-data-warehousing": {"icon": "database-export", "color": "#d97706"},
    "aids-cloud-computing": {"icon": "cloud-outline", "color": "#3b82f6"},
    "aids-big-data-analytics": {"icon": "database-search", "color": "#dc2626"},
    "aids-natural-language-processing": {"icon": "text-recognition", "color": "#7c3aed"},
    "aids-deep-learning": {"icon": "brain", "color": "#ec4899"},
    "aids-data-security-and-privacy": {"icon": "shield-lock-outline", "color": "#7c3aed"},
    "aids-statistical-machine-learning": {"icon": "chart-scatter-plot", "color": "#2563eb"},
    # BCA-specific
    "bca-problem-solving-using-c": {"icon": "language-c", "color": "#6366f1"},
    # MCA-specific
    "mca-operating-systems": {"icon": "cog-outline", "color": "#7c3aed"},
    "mca-data-structures": {"icon": "graph-outline", "color": "#059669"},
    "mca-java-programming": {"icon": "language-java", "color": "#ea580c"},
    "mca-computer-networks": {"icon": "lan", "color": "#0284c7"},
}

CONTENT_VERSION = 1


def read_file(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError):
        return None


def read_json(path: Path) -> dict | list | None:
    text = read_file(path)
    if text is None:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        print(f"  WARNING: Invalid JSON in {path}")
        return None


def find_first_svg(topic_dir: Path) -> str | None:
    assets_dir = topic_dir / "assets"
    if not assets_dir.is_dir():
        return None
    svgs = sorted(assets_dir.glob("*.svg"))
    if not svgs:
        return None
    return read_file(svgs[0])


def _heading_to_anchor(title: str) -> str:
    anchor = title.strip().lower()
    anchor = re.sub(r'[^\w\s-]', '', anchor)
    anchor = re.sub(r'\s+', '-', anchor)
    return anchor


def prepend_toc(markdown: str) -> str:
    if '## Table of Contents' in markdown:
        return markdown
    heading_re = re.compile(r'^(#{2,3})\s+(.+)$', re.MULTILINE)
    headings = heading_re.findall(markdown)
    if len(headings) < 3:
        return markdown
    toc_lines = ["## Table of Contents\n"]
    for hashes, title in headings:
        level = len(hashes)
        clean = title.strip()
        anchor = _heading_to_anchor(clean)
        indent = "  " * (level - 2)
        toc_lines.append(f"{indent}- [{clean}](#{anchor})")
    toc = "\n".join(toc_lines) + "\n\n---\n\n"
    h1_match = re.match(r'^#\s+.+\n+', markdown)
    if h1_match:
        insert_pos = h1_match.end()
        return markdown[:insert_pos] + toc + markdown[insert_pos:]
    return toc + markdown


def extract_subject_id(folder_name: str) -> str:
    parts = folder_name.split("-", 1)
    if len(parts) == 2:
        return parts[1]
    return folder_name


def normalize_mcq_options(options):
    if not isinstance(options, list):
        return options
    if len(options) > 0 and isinstance(options[0], str):
        keys = ["A", "B", "C", "D", "E", "F"]
        return [{"key": keys[i] if i < len(keys) else chr(65 + i), "text": t}
                for i, t in enumerate(options)]
    return options


def find_subject_folder(location_dir: Path, code: str, subject_id: str) -> tuple[Path | None, bool]:
    """Find the content folder for a subject by matching code prefix.

    Returns (subject_dir, uses_chapters_layout) where uses_chapters_layout
    indicates that _index.json and modules live under a chapters/ subdirectory.

    Handles duplicate folders (e.g., bcs405a-discrete-mathematical-structures
    and bcs405a-discrete-mathematical-structures-semester-iv) by preferring
    the -semester- variant (usually has more complete content).
    """
    code_lower = code.lower()

    # Search across all semester dirs in the location
    for sem_dir in sorted(location_dir.glob("sem-*")):
        if not sem_dir.is_dir():
            continue
        candidates = []
        for d in sem_dir.iterdir():
            if d.is_dir() and d.name.startswith(code_lower + "-"):
                # Accept root _index.json OR chapters/_index.json
                if (d / "_index.json").exists() or (d / "chapters" / "_index.json").exists():
                    candidates.append(d)

        if not candidates:
            continue

        # Pick the best candidate
        if len(candidates) > 1:
            # Prefer the longest name — handles both -semester- variants
            # (more complete content) and truncated folder names
            pick = max(candidates, key=lambda c: len(c.name))
        else:
            pick = candidates[0]

        uses_chapters = not (pick / "_index.json").exists() and (pick / "chapters" / "_index.json").exists()
        return pick, uses_chapters

    return None, False


def compute_content_hash(dirs: list[Path]) -> str:
    h = hashlib.sha256()
    for d in dirs:
        for f in sorted(d.rglob("*")):
            if f.is_file() and f.suffix in (".md", ".json", ".svg"):
                h.update(f.read_bytes())
    return h.hexdigest()[:16]


def create_schema(conn: sqlite3.Connection):
    c = conn.cursor()
    c.execute("CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT)")
    c.execute("""CREATE TABLE content_packs (
        id TEXT PRIMARY KEY, name TEXT NOT NULL, description TEXT,
        version TEXT, domain TEXT, icon TEXT, color TEXT,
        loaded_at DATETIME DEFAULT CURRENT_TIMESTAMP, is_active INTEGER DEFAULT 1)""")
    c.execute("""CREATE TABLE subjects (
        id TEXT PRIMARY KEY, pack_id TEXT, name TEXT NOT NULL, code TEXT,
        description TEXT, category TEXT, category_order INTEGER,
        icon TEXT, color TEXT, total_chapters INTEGER DEFAULT 0, branch TEXT, metadata TEXT,
        FOREIGN KEY (pack_id) REFERENCES content_packs(id) ON DELETE CASCADE)""")
    c.execute("""CREATE TABLE chapters (
        id TEXT PRIMARY KEY, subject_id TEXT, chapter_number INTEGER,
        title TEXT NOT NULL, description TEXT, content TEXT, summary TEXT,
        reading_time INTEGER, order_index INTEGER, metadata TEXT,
        content_file TEXT, content_loaded INTEGER DEFAULT 0,
        has_topics INTEGER DEFAULT 0, topic_count INTEGER DEFAULT 0,
        FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE)""")
    c.execute("""CREATE TABLE topics (
        id TEXT PRIMARY KEY, chapter_id TEXT, subject_id TEXT,
        title TEXT NOT NULL, description TEXT, order_index INTEGER,
        estimated_minutes INTEGER, has_visual INTEGER DEFAULT 0,
        has_code INTEGER DEFAULT 0, has_questions INTEGER DEFAULT 0,
        read_file TEXT, visual_file TEXT, code_file TEXT, questions_file TEXT,
        purpose_file TEXT, memory_file TEXT, mcqs_file TEXT, flashcards_file TEXT,
        base_path TEXT, read_content TEXT, summary_content TEXT, purpose_content TEXT,
        code_json TEXT, questions_json TEXT, memory_json TEXT, visual_json TEXT,
        mcqs_json TEXT, flashcards_json TEXT, svg_raw TEXT,
        FOREIGN KEY (chapter_id) REFERENCES chapters(id) ON DELETE CASCADE,
        FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE)""")
    c.execute("""CREATE TABLE mcqs (
        id TEXT PRIMARY KEY, subject_id TEXT, chapter_id TEXT,
        question TEXT NOT NULL, options TEXT NOT NULL, correct_answer TEXT,
        explanation TEXT, difficulty TEXT DEFAULT 'medium' CHECK(difficulty IN ('easy','medium','hard')),
        tags TEXT, source TEXT, metadata TEXT,
        FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE,
        FOREIGN KEY (chapter_id) REFERENCES chapters(id) ON DELETE CASCADE)""")
    c.execute("""CREATE TABLE flashcards (
        id TEXT PRIMARY KEY, subject_id TEXT, chapter_id TEXT,
        front TEXT NOT NULL, back TEXT NOT NULL, category TEXT,
        difficulty TEXT DEFAULT 'medium' CHECK(difficulty IN ('easy','medium','hard')), tags TEXT,
        FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE,
        FOREIGN KEY (chapter_id) REFERENCES chapters(id) ON DELETE CASCADE)""")
    c.execute("""CREATE VIRTUAL TABLE search_index USING fts5(
        title, subtitle, type UNINDEXED, item_id UNINDEXED,
        subject_id UNINDEXED, chapter_id UNINDEXED)""")
    c.execute("CREATE INDEX idx_subjects_pack ON subjects(pack_id)")
    c.execute("CREATE INDEX idx_subjects_branch ON subjects(branch)")
    c.execute("CREATE INDEX idx_chapters_subject ON chapters(subject_id)")
    c.execute("CREATE INDEX idx_topics_chapter ON topics(chapter_id)")
    c.execute("CREATE INDEX idx_topics_subject ON topics(subject_id)")
    c.execute("CREATE INDEX idx_mcqs_subject ON mcqs(subject_id)")
    c.execute("CREATE INDEX idx_mcqs_chapter ON mcqs(chapter_id)")
    c.execute("CREATE INDEX idx_flashcards_subject ON flashcards(subject_id)")
    c.execute("CREATE INDEX idx_flashcards_chapter ON flashcards(chapter_id)")
    conn.commit()


def build_branch_db(branch: str):
    """Build a content.db for a specific branch."""
    # Load branch map
    branch_map_path = CONTENT_PACK_DIR / "branch-map.json"
    with open(branch_map_path) as f:
        branch_map = json.load(f)

    if branch not in branch_map["branches"]:
        print(f"ERROR: Branch '{branch}' not found in branch-map.json")
        print(f"Available: {', '.join(branch_map['branches'].keys())}")
        sys.exit(1)

    branch_config = branch_map["branches"][branch]
    output_db = OUTPUT_DIR / f"content-{branch}.db"

    print(f"=== Building content-{branch}.db ===")
    print(f"Branch:  {branch_config['shortName']} ({branch_config['name']})")
    print(f"Output:  {output_db}")

    # Build subject list: {subject_id: {code, location, semester}}
    subject_list = {}
    for sem_key, subjects in branch_config["subjects"].items():
        sem_num = int(sem_key.split("-")[1])
        for s in subjects:
            subject_list[s["id"]] = {
                "code": s["code"],
                "location": s["location"],
                "semester": sem_num,
            }

    print(f"Subjects: {len(subject_list)} total")

    # Gather unique location dirs
    location_dirs = set(s["location"] for s in subject_list.values())
    print(f"Locations: {', '.join(sorted(location_dirs))}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if output_db.exists():
        output_db.unlink()

    conn = sqlite3.connect(str(output_db))
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = NORMAL")
    create_schema(conn)
    c = conn.cursor()

    content_pack_id = f"ka-{branch}-2022"
    content_pack_name = f"KA {branch_config['shortName']} 2022 - Study Guide"
    c.execute(
        "INSERT INTO content_packs (id, name, description, version, domain, is_active) VALUES (?, ?, ?, ?, ?, ?)",
        (content_pack_id, content_pack_name, f"KA {branch_config['shortName']} 2022 Scheme Study Guide", "1.0.0", "engineering", 1)
    )

    total_subjects = 0
    total_chapters = 0
    total_topics = 0
    total_mcqs = 0
    total_flashcards = 0
    warnings = []
    missing_subjects = []

    for subject_id, info in subject_list.items():
        location = info["location"]
        code = info["code"]
        sem_num = info["semester"]
        category = f"Semester {sem_num}"

        location_dir = CONTENT_PACK_DIR / location
        if not location_dir.is_dir():
            warnings.append(f"Location dir missing: {location_dir}")
            missing_subjects.append(subject_id)
            continue

        subject_dir, uses_chapters_layout = find_subject_folder(location_dir, code, subject_id)
        if subject_dir is None:
            warnings.append(f"Subject folder not found: {subject_id} (code={code}, location={location})")
            missing_subjects.append(subject_id)
            continue

        # Read _meta.json
        meta = read_json(subject_dir / "_meta.json") or {}

        subject_name = meta.get("name", subject_id.replace("-", " ").title())
        subject_code = meta.get("code", code)
        # Always use location from branch-map (not _meta.json branch which may differ)
        subject_branch = location

        extra = SUBJECTS_EXTRA.get(subject_id, {"icon": "book", "color": "#6366f1"})

        # Read chapter index — may be at root or under chapters/
        if uses_chapters_layout:
            index_data = read_json(subject_dir / "chapters" / "_index.json")
        else:
            index_data = read_json(subject_dir / "_index.json")
        if not index_data or "chapters" not in index_data:
            warnings.append(f"Invalid _index.json for {subject_id} at {subject_dir}")
            missing_subjects.append(subject_id)
            continue

        chapters = index_data["chapters"]
        num_chapters = len(chapters)

        # Insert subject — use branch-map ID, not _meta.json id
        c.execute(
            """INSERT OR REPLACE INTO subjects (id, pack_id, name, code, description, category, category_order,
               icon, color, total_chapters, branch)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (subject_id, content_pack_id, subject_name, subject_code, subject_name,
             category, sem_num, extra["icon"], extra["color"], num_chapters, subject_branch)
        )
        total_subjects += 1

        subject_mcqs = []
        subject_flashcards = []

        for chapter_data in chapters:
            chapter_short_id = chapter_data["id"]
            chapter_title = chapter_data["title"]
            chapter_order = chapter_data.get("order", 0)
            chapter_topic_count = chapter_data.get("topicCount", 0)
            has_topics = chapter_data.get("hasTopics", False)

            chapter_db_id = f"{subject_id}-{chapter_short_id}"

            c.execute(
                """INSERT INTO chapters (id, subject_id, chapter_number, title, description,
                   content, summary, order_index, has_topics, topic_count)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (chapter_db_id, subject_id, chapter_order, chapter_title, None,
                 "", None, chapter_order, 1 if has_topics else 0, chapter_topic_count)
            )
            total_chapters += 1

            if uses_chapters_layout:
                topics_dir = subject_dir / "chapters" / chapter_short_id / "topics"
            else:
                topics_dir = subject_dir / chapter_short_id / "topics"
            if not topics_dir.is_dir():
                continue

            topic_folders = sorted([d for d in topics_dir.iterdir() if d.is_dir()])

            for topic_idx, topic_dir in enumerate(topic_folders):
                topic_short_id = topic_dir.name
                topic_id = f"{subject_id}-{chapter_short_id}-{topic_short_id}"
                topic_title = topic_short_id.replace("-", " ").title()

                read_content = read_file(topic_dir / "read.md")
                summary_content = read_file(topic_dir / "summary.md")
                purpose_content = read_file(topic_dir / "purpose.md")
                code_data = read_json(topic_dir / "code.json")
                questions_data = read_json(topic_dir / "questions.json")
                memory_data = read_json(topic_dir / "memory.json")
                visual_data = read_json(topic_dir / "visual.json")
                mcqs_data = read_json(topic_dir / "mcqs.json")
                flashcards_data = read_json(topic_dir / "flashcards.json")
                svg_raw = find_first_svg(topic_dir)

                if read_content:
                    read_content = prepend_toc(read_content)

                if not read_content or len(read_content.strip()) == 0:
                    warnings.append(f"Empty read.md: {topic_id}")

                has_visual = bool(visual_data) or bool(svg_raw)
                has_code = bool(code_data)
                has_questions = bool(questions_data)

                est_minutes = None
                if read_content:
                    word_count = len(read_content.split())
                    est_minutes = max(1, word_count // 200)

                c.execute(
                    """INSERT INTO topics (id, chapter_id, subject_id, title, description,
                       order_index, estimated_minutes, has_visual, has_code, has_questions,
                       read_content, summary_content, purpose_content,
                       code_json, questions_json, memory_json, visual_json,
                       mcqs_json, flashcards_json, svg_raw)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (topic_id, chapter_db_id, subject_id, topic_title, None,
                     topic_idx, est_minutes, 1 if has_visual else 0,
                     1 if has_code else 0, 1 if has_questions else 0,
                     read_content, summary_content, purpose_content,
                     json.dumps(code_data) if code_data else None,
                     json.dumps(questions_data) if questions_data else None,
                     json.dumps(memory_data) if memory_data else None,
                     json.dumps(visual_data) if visual_data else None,
                     json.dumps(mcqs_data) if mcqs_data else None,
                     json.dumps(flashcards_data) if flashcards_data else None,
                     svg_raw)
                )
                total_topics += 1

                # Extract individual MCQs
                if mcqs_data:
                    mcqs_list = []
                    if isinstance(mcqs_data, dict):
                        mcqs_list = mcqs_data.get("mcqs", mcqs_data.get("questions", []))
                    elif isinstance(mcqs_data, list):
                        mcqs_list = mcqs_data
                    for mcq in mcqs_list:
                        if not isinstance(mcq, dict) or not mcq.get("question") or not mcq.get("options"):
                            continue
                        mcq_id = f"{topic_id}-{mcq.get('id', 'mcq-0')}"
                        options = normalize_mcq_options(mcq["options"])
                        difficulty = mcq.get("difficulty", "medium")
                        if difficulty not in ("easy", "medium", "hard"):
                            difficulty = "medium"
                        subject_mcqs.append((
                            mcq_id, subject_id, chapter_db_id,
                            mcq["question"], json.dumps(options),
                            mcq.get("correctAnswer", ""),
                            mcq.get("explanation", ""),
                            difficulty,
                            json.dumps(mcq.get("tags")) if mcq.get("tags") else None,
                            mcq.get("source"), None
                        ))

                # Extract individual flashcards
                if flashcards_data:
                    fc_list = []
                    if isinstance(flashcards_data, dict):
                        fc_list = flashcards_data.get("flashcards", [])
                    elif isinstance(flashcards_data, list):
                        fc_list = flashcards_data
                    for fc in fc_list:
                        if not isinstance(fc, dict) or not fc.get("front") or not fc.get("back"):
                            continue
                        fc_id = f"{topic_id}-{fc.get('id', 'fc-0')}"
                        difficulty = fc.get("difficulty", "medium")
                        if difficulty not in ("easy", "medium", "hard"):
                            difficulty = "medium"
                        subject_flashcards.append((
                            fc_id, subject_id, chapter_db_id,
                            fc["front"], fc["back"],
                            fc.get("category"), difficulty,
                            json.dumps(fc.get("tags")) if fc.get("tags") else None
                        ))

        if subject_mcqs:
            c.executemany(
                """INSERT OR REPLACE INTO mcqs (id, subject_id, chapter_id, question, options,
                   correct_answer, explanation, difficulty, tags, source, metadata)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                subject_mcqs
            )
            total_mcqs += len(subject_mcqs)

        if subject_flashcards:
            c.executemany(
                """INSERT OR REPLACE INTO flashcards (id, subject_id, chapter_id, front, back,
                   category, difficulty, tags) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                subject_flashcards
            )
            total_flashcards += len(subject_flashcards)

        print(f"  {subject_id}: {num_chapters} ch, {len(subject_mcqs)} MCQs, {len(subject_flashcards)} fc")

    conn.commit()

    # Build FTS5 search index
    print("\nBuilding search index...")
    c.execute("""INSERT INTO search_index (type, item_id, title, subtitle, subject_id, chapter_id)
        SELECT 'subject', id, name, COALESCE(description, ''), '', '' FROM subjects""")
    c.execute("""INSERT INTO search_index (type, item_id, title, subtitle, subject_id, chapter_id)
        SELECT 'chapter', id, title, COALESCE(description, ''), subject_id, '' FROM chapters""")
    c.execute("""INSERT INTO search_index (type, item_id, title, subtitle, subject_id, chapter_id)
        SELECT 'topic', id, title, COALESCE(description, ''), subject_id, chapter_id FROM topics""")
    c.execute("""INSERT INTO search_index (type, item_id, title, subtitle, subject_id, chapter_id)
        SELECT 'mcq', id, question, '', subject_id, '' FROM mcqs""")
    c.execute("""INSERT INTO search_index (type, item_id, title, subtitle, subject_id, chapter_id)
        SELECT 'flashcard', id, front, back, subject_id, '' FROM flashcards""")
    conn.commit()

    # Metadata
    content_dirs = [CONTENT_PACK_DIR / loc for loc in location_dirs if (CONTENT_PACK_DIR / loc).is_dir()]
    content_hash = compute_content_hash(content_dirs)
    c.execute("INSERT INTO metadata VALUES ('content_version', ?)", (str(CONTENT_VERSION),))
    c.execute("INSERT INTO metadata VALUES ('build_date', ?)", (datetime.now().isoformat(),))
    c.execute("INSERT INTO metadata VALUES ('content_hash', ?)", (content_hash,))
    c.execute("INSERT INTO metadata VALUES ('content_pack', ?)", (content_pack_id,))
    c.execute("INSERT INTO metadata VALUES ('topic_count', ?)", (str(total_topics),))
    c.execute("INSERT INTO metadata VALUES ('subject_count', ?)", (str(total_subjects),))
    c.execute("INSERT INTO metadata VALUES ('mcq_count', ?)", (str(total_mcqs),))
    c.execute("INSERT INTO metadata VALUES ('flashcard_count', ?)", (str(total_flashcards),))
    conn.commit()

    # Optimize
    print("Optimizing database...")
    c.execute("ANALYZE")
    conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    conn.close()

    # Switch to DELETE journal for single-file distribution
    conn = sqlite3.connect(str(output_db))
    conn.execute("PRAGMA journal_mode = DELETE")
    conn.close()

    db_size = output_db.stat().st_size
    print(f"\n=== Build complete ===")
    print(f"Branch:     {branch_config['shortName']}")
    print(f"Subjects:   {total_subjects}/{len(subject_list)} mapped")
    print(f"Chapters:   {total_chapters}")
    print(f"Topics:     {total_topics}")
    print(f"MCQs:       {total_mcqs}")
    print(f"Flashcards: {total_flashcards}")
    print(f"DB size:    {db_size / 1024 / 1024:.1f} MB")
    print(f"Output:     {output_db}")

    if missing_subjects:
        print(f"\nMISSING SUBJECTS ({len(missing_subjects)}):")
        for s in missing_subjects:
            info = subject_list[s]
            print(f"  - {s} (code={info['code']}, location={info['location']})")

    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for w in warnings[:30]:
            print(f"  - {w}")

    # Verify
    conn = sqlite3.connect(str(output_db))
    c = conn.cursor()
    for table in ["subjects", "chapters", "topics", "mcqs", "flashcards"]:
        count = c.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"  {table}: {count} rows")
    search_count = c.execute("SELECT COUNT(*) FROM search_index").fetchone()[0]
    print(f"  search_index: {search_count} rows")
    conn.close()

    return len(missing_subjects)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 build_branch_db.py <branch>")
        print("  e.g.: python3 build_branch_db.py ise")
        sys.exit(1)

    branch = sys.argv[1].lower()
    missing = build_branch_db(branch)
    sys.exit(1 if missing > 0 else 0)
