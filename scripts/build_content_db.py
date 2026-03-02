#!/usr/bin/env python3
"""
build_content_db.py — Builds assets/data/content.db from raw cse/ content files.

Walks the cse/ directory (37 subjects), reads all topic files, validates,
and produces a single SQLite database with embedded content + FTS5 search index.

Usage:
    python3 content-packs/ka-cse-2022/scripts/build_content_db.py
"""

import hashlib
import json
import os
import re
import sqlite3
import sys
import glob as globmod
from datetime import datetime
from pathlib import Path

# Resolve paths relative to this script
SCRIPT_DIR = Path(__file__).resolve().parent
CONTENT_PACK_DIR = SCRIPT_DIR.parent  # ka-cse-2022/
CSE_DIR = CONTENT_PACK_DIR / "cse"
APP_ROOT = CONTENT_PACK_DIR.parent.parent  # study-app-template/
OUTPUT_DIR = APP_ROOT / "assets" / "data"
OUTPUT_DB = OUTPUT_DIR / "content.db"

# Subject metadata from contentLoader.ts SUBJECTS array
# Maps folder name (e.g. "bcs302-digital-design-and-computer-organization") to metadata
# We read _meta.json from each subject folder for code/name/semester/branch,
# and use the SUBJECTS_EXTRA dict below for icon/color (UI properties not in _meta.json).
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
}

CONTENT_PACK_ID = "ka-cse-2022"
CONTENT_PACK_NAME = "KA CSE 2022 - Study Guide"
CONTENT_VERSION = 1


def read_file(path: Path) -> str | None:
    """Read file contents, return None if missing."""
    try:
        return path.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError):
        return None


def read_json(path: Path) -> dict | list | None:
    """Read and parse JSON file, return None if invalid/missing."""
    text = read_file(path)
    if text is None:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        print(f"  WARNING: Invalid JSON in {path}")
        return None


def find_first_svg(topic_dir: Path) -> str | None:
    """Find first SVG file in topic's assets/ folder."""
    assets_dir = topic_dir / "assets"
    if not assets_dir.is_dir():
        return None
    svgs = sorted(assets_dir.glob("*.svg"))
    if not svgs:
        return None
    return read_file(svgs[0])


def _heading_to_anchor(title: str) -> str:
    """Convert a heading title to a GitHub-style markdown anchor."""
    anchor = title.strip().lower()
    anchor = re.sub(r'[^\w\s-]', '', anchor)   # remove punctuation
    anchor = re.sub(r'\s+', '-', anchor)        # spaces to hyphens
    return anchor


def prepend_toc(markdown: str) -> str:
    """Extract headings from markdown and prepend a Table of Contents.

    Skips files that already contain a TOC. Generates a linked markdown TOC
    from H2/H3 headings. Returns original content unchanged if fewer than 3
    headings are found.
    """
    # Skip if file already has a TOC
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
    # Insert after the first H1 line (topic title)
    h1_match = re.match(r'^#\s+.+\n+', markdown)
    if h1_match:
        insert_pos = h1_match.end()
        return markdown[:insert_pos] + toc + markdown[insert_pos:]
    return toc + markdown


def extract_subject_id(folder_name: str) -> str:
    """Extract subject ID from folder name by removing the code prefix.
    e.g. 'bcs302-digital-design-and-computer-organization' -> 'digital-design-and-computer-organization'
    """
    # Split on first hyphen after the code portion
    # Codes like bcs302, bcs306a, bcs405b, bcs456c, bai654d, bis654c, bis601
    parts = folder_name.split("-", 1)
    if len(parts) == 2:
        return parts[1]
    return folder_name


def compute_content_hash(cse_dir: Path) -> str:
    """Compute a hash of all content files for versioning."""
    h = hashlib.sha256()
    for f in sorted(cse_dir.rglob("*")):
        if f.is_file() and f.suffix in (".md", ".json", ".svg"):
            h.update(f.read_bytes())
    return h.hexdigest()[:16]


def create_schema(conn: sqlite3.Connection):
    """Create all tables in content.db."""
    c = conn.cursor()

    # Metadata
    c.execute("""
        CREATE TABLE metadata (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)

    # Content packs
    c.execute("""
        CREATE TABLE content_packs (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            version TEXT,
            domain TEXT,
            icon TEXT,
            color TEXT,
            loaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            is_active INTEGER DEFAULT 1
        )
    """)

    # Subjects
    c.execute("""
        CREATE TABLE subjects (
            id TEXT PRIMARY KEY,
            pack_id TEXT,
            name TEXT NOT NULL,
            code TEXT,
            description TEXT,
            category TEXT,
            category_order INTEGER,
            icon TEXT,
            color TEXT,
            total_chapters INTEGER DEFAULT 0,
            branch TEXT,
            metadata TEXT,
            FOREIGN KEY (pack_id) REFERENCES content_packs(id) ON DELETE CASCADE
        )
    """)

    # Chapters
    c.execute("""
        CREATE TABLE chapters (
            id TEXT PRIMARY KEY,
            subject_id TEXT,
            chapter_number INTEGER,
            title TEXT NOT NULL,
            description TEXT,
            content TEXT,
            summary TEXT,
            reading_time INTEGER,
            order_index INTEGER,
            metadata TEXT,
            content_file TEXT,
            content_loaded INTEGER DEFAULT 0,
            has_topics INTEGER DEFAULT 0,
            topic_count INTEGER DEFAULT 0,
            FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
        )
    """)

    # Topics with embedded content
    c.execute("""
        CREATE TABLE topics (
            id TEXT PRIMARY KEY,
            chapter_id TEXT,
            subject_id TEXT,
            title TEXT NOT NULL,
            description TEXT,
            order_index INTEGER,
            estimated_minutes INTEGER,
            has_visual INTEGER DEFAULT 0,
            has_code INTEGER DEFAULT 0,
            has_questions INTEGER DEFAULT 0,
            read_file TEXT,
            visual_file TEXT,
            code_file TEXT,
            questions_file TEXT,
            purpose_file TEXT,
            memory_file TEXT,
            mcqs_file TEXT,
            flashcards_file TEXT,
            base_path TEXT,
            read_content TEXT,
            summary_content TEXT,
            purpose_content TEXT,
            code_json TEXT,
            questions_json TEXT,
            memory_json TEXT,
            visual_json TEXT,
            mcqs_json TEXT,
            flashcards_json TEXT,
            svg_raw TEXT,
            FOREIGN KEY (chapter_id) REFERENCES chapters(id) ON DELETE CASCADE,
            FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
        )
    """)

    # Individual MCQ rows (for exam/mock test queries by subject)
    c.execute("""
        CREATE TABLE mcqs (
            id TEXT PRIMARY KEY,
            subject_id TEXT,
            chapter_id TEXT,
            question TEXT NOT NULL,
            options TEXT NOT NULL,
            correct_answer TEXT,
            explanation TEXT,
            difficulty TEXT DEFAULT 'medium' CHECK(difficulty IN ('easy', 'medium', 'hard')),
            tags TEXT,
            source TEXT,
            metadata TEXT,
            FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE,
            FOREIGN KEY (chapter_id) REFERENCES chapters(id) ON DELETE CASCADE
        )
    """)

    # Individual flashcard rows
    c.execute("""
        CREATE TABLE flashcards (
            id TEXT PRIMARY KEY,
            subject_id TEXT,
            chapter_id TEXT,
            front TEXT NOT NULL,
            back TEXT NOT NULL,
            category TEXT,
            difficulty TEXT DEFAULT 'medium' CHECK(difficulty IN ('easy', 'medium', 'hard')),
            tags TEXT,
            FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE,
            FOREIGN KEY (chapter_id) REFERENCES chapters(id) ON DELETE CASCADE
        )
    """)

    # FTS5 search index
    c.execute("""
        CREATE VIRTUAL TABLE search_index USING fts5(
            title,
            subtitle,
            type UNINDEXED,
            item_id UNINDEXED,
            subject_id UNINDEXED,
            chapter_id UNINDEXED
        )
    """)

    # Indexes
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


def normalize_mcq_options(options):
    """Normalize MCQ options to [{key, text}] format."""
    if not isinstance(options, list):
        return options
    if len(options) > 0 and isinstance(options[0], str):
        keys = ["A", "B", "C", "D", "E", "F"]
        return [{"key": keys[i] if i < len(keys) else chr(65 + i), "text": t}
                for i, t in enumerate(options)]
    return options


def build_db():
    """Main build function."""
    print(f"=== Building content.db ===")
    print(f"CSE dir: {CSE_DIR}")
    print(f"Output:  {OUTPUT_DB}")

    if not CSE_DIR.is_dir():
        print(f"ERROR: CSE directory not found: {CSE_DIR}")
        sys.exit(1)

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Remove old DB if exists
    if OUTPUT_DB.exists():
        OUTPUT_DB.unlink()

    conn = sqlite3.connect(str(OUTPUT_DB))
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = NORMAL")

    create_schema(conn)
    c = conn.cursor()

    # Insert content pack
    c.execute(
        "INSERT INTO content_packs (id, name, description, version, domain, is_active) VALUES (?, ?, ?, ?, ?, ?)",
        (CONTENT_PACK_ID, CONTENT_PACK_NAME, "KA CSE 2022 Scheme Study Guide", "1.0.0", "engineering", 1)
    )

    # Discover subjects from filesystem
    total_subjects = 0
    total_chapters = 0
    total_topics = 0
    total_mcqs = 0
    total_flashcards = 0
    warnings = []

    sem_dirs = sorted(CSE_DIR.glob("sem-*"))
    for sem_dir in sem_dirs:
        if not sem_dir.is_dir():
            continue
        sem_num = int(sem_dir.name.split("-")[1])
        category = f"Semester {sem_num}"

        subject_dirs = sorted(
            [d for d in sem_dir.iterdir()
             if d.is_dir() and (d / "_index.json").exists()]
        )

        for subject_dir in subject_dirs:
            subject_folder = subject_dir.name
            subject_id = extract_subject_id(subject_folder)

            # Read _meta.json
            meta = read_json(subject_dir / "_meta.json")
            if meta is None:
                warnings.append(f"Missing _meta.json for {subject_folder}")
                meta = {}

            subject_name = meta.get("name", subject_id.replace("-", " ").title())
            subject_code = meta.get("code", "")
            branch = meta.get("branch", "cse")

            # Get icon/color from extras
            extra = SUBJECTS_EXTRA.get(subject_id, {"icon": "book", "color": "#6366f1"})

            # Read chapter index
            index_data = read_json(subject_dir / "_index.json")
            if not index_data or "chapters" not in index_data:
                warnings.append(f"Invalid _index.json for {subject_folder}")
                continue

            chapters = index_data["chapters"]
            num_chapters = len(chapters)

            # Insert subject
            c.execute(
                """INSERT INTO subjects (id, pack_id, name, code, description, category, category_order,
                   icon, color, total_chapters, branch)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (subject_id, CONTENT_PACK_ID, subject_name, subject_code, subject_name,
                 category, sem_num, extra["icon"], extra["color"], num_chapters, branch)
            )
            total_subjects += 1

            subject_mcqs = []
            subject_flashcards = []

            for chapter_data in chapters:
                chapter_id = chapter_data["id"]
                chapter_title = chapter_data["title"]
                chapter_order = chapter_data.get("order", 0)
                chapter_topic_count = chapter_data.get("topicCount", 0)
                has_topics = chapter_data.get("hasTopics", False)

                chapter_db_id = f"{subject_id}-{chapter_id}"

                c.execute(
                    """INSERT INTO chapters (id, subject_id, chapter_number, title, description,
                       content, summary, order_index, has_topics, topic_count)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (chapter_db_id, subject_id, chapter_order, chapter_title, None,
                     "", None, chapter_order, 1 if has_topics else 0, chapter_topic_count)
                )
                total_chapters += 1

                # Walk topics
                topics_dir = subject_dir / chapter_id / "topics"
                if not topics_dir.is_dir():
                    continue

                topic_folders = sorted(
                    [d for d in topics_dir.iterdir() if d.is_dir()]
                )

                for topic_idx, topic_dir in enumerate(topic_folders):
                    topic_short_id = topic_dir.name
                    topic_id = f"{subject_id}-{chapter_id}-{topic_short_id}"
                    topic_title = topic_short_id.replace("-", " ").title()

                    # Read content files
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

                    # Prepend TOC to read content
                    if read_content:
                        read_content = prepend_toc(read_content)

                    # Validate: read.md should not be empty
                    if not read_content or len(read_content.strip()) == 0:
                        warnings.append(f"Empty read.md: {topic_id}")

                    # Determine flags
                    has_visual = bool(visual_data) or bool(svg_raw)
                    has_code = bool(code_data)
                    has_questions = bool(questions_data)

                    # Estimate reading time (~200 words/min)
                    est_minutes = None
                    if read_content:
                        word_count = len(read_content.split())
                        est_minutes = max(1, word_count // 200)

                    # Insert topic
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
                    if mcqs_data and isinstance(mcqs_data, dict):
                        mcqs_list = mcqs_data.get("mcqs", [])
                        for mcq in mcqs_list:
                            if not mcq.get("question") or not mcq.get("options"):
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
                                mcq.get("source"),
                                None
                            ))

                    # Extract individual flashcards
                    if flashcards_data and isinstance(flashcards_data, dict):
                        fc_list = flashcards_data.get("flashcards", [])
                        for fc in fc_list:
                            if not fc.get("front") or not fc.get("back"):
                                continue
                            fc_id = f"{topic_id}-{fc.get('id', 'fc-0')}"
                            difficulty = fc.get("difficulty", "medium")
                            if difficulty not in ("easy", "medium", "hard"):
                                difficulty = "medium"
                            subject_flashcards.append((
                                fc_id, subject_id, chapter_db_id,
                                fc["front"], fc["back"],
                                fc.get("category"),
                                difficulty,
                                json.dumps(fc.get("tags")) if fc.get("tags") else None
                            ))

            # Batch insert MCQs for this subject
            if subject_mcqs:
                c.executemany(
                    """INSERT OR REPLACE INTO mcqs (id, subject_id, chapter_id, question, options,
                       correct_answer, explanation, difficulty, tags, source, metadata)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    subject_mcqs
                )
                total_mcqs += len(subject_mcqs)

            # Batch insert flashcards for this subject
            if subject_flashcards:
                c.executemany(
                    """INSERT OR REPLACE INTO flashcards (id, subject_id, chapter_id, front, back,
                       category, difficulty, tags)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                    subject_flashcards
                )
                total_flashcards += len(subject_flashcards)

            print(f"  {subject_id}: {num_chapters} chapters, {len(subject_mcqs)} MCQs, {len(subject_flashcards)} flashcards")

    conn.commit()

    # Build FTS5 search index
    print("\nBuilding search index...")

    # Index subjects
    c.execute("""
        INSERT INTO search_index (type, item_id, title, subtitle, subject_id, chapter_id)
        SELECT 'subject', id, name, COALESCE(description, ''), '', ''
        FROM subjects
    """)

    # Index chapters
    c.execute("""
        INSERT INTO search_index (type, item_id, title, subtitle, subject_id, chapter_id)
        SELECT 'chapter', id, title, COALESCE(description, ''), subject_id, ''
        FROM chapters
    """)

    # Index topics
    c.execute("""
        INSERT INTO search_index (type, item_id, title, subtitle, subject_id, chapter_id)
        SELECT 'topic', id, title, COALESCE(description, ''), subject_id, chapter_id
        FROM topics
    """)

    # Index MCQs
    c.execute("""
        INSERT INTO search_index (type, item_id, title, subtitle, subject_id, chapter_id)
        SELECT 'mcq', id, question, '', subject_id, ''
        FROM mcqs
    """)

    # Index flashcards
    c.execute("""
        INSERT INTO search_index (type, item_id, title, subtitle, subject_id, chapter_id)
        SELECT 'flashcard', id, front, back, subject_id, ''
        FROM flashcards
    """)

    conn.commit()

    # Insert metadata
    content_hash = compute_content_hash(CSE_DIR)
    c.execute("INSERT INTO metadata VALUES ('content_version', ?)", (str(CONTENT_VERSION),))
    c.execute("INSERT INTO metadata VALUES ('build_date', ?)", (datetime.now().isoformat(),))
    c.execute("INSERT INTO metadata VALUES ('content_hash', ?)", (content_hash,))
    c.execute("INSERT INTO metadata VALUES ('topic_count', ?)", (str(total_topics),))
    c.execute("INSERT INTO metadata VALUES ('subject_count', ?)", (str(total_subjects),))
    c.execute("INSERT INTO metadata VALUES ('mcq_count', ?)", (str(total_mcqs),))
    c.execute("INSERT INTO metadata VALUES ('flashcard_count', ?)", (str(total_flashcards),))

    conn.commit()

    # Final optimization
    print("Optimizing database...")
    c.execute("ANALYZE")
    conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    conn.close()

    # Re-open without WAL for distribution (single-file)
    conn = sqlite3.connect(str(OUTPUT_DB))
    conn.execute("PRAGMA journal_mode = DELETE")
    conn.close()

    db_size = OUTPUT_DB.stat().st_size
    print(f"\n=== Build complete ===")
    print(f"Subjects:   {total_subjects}")
    print(f"Chapters:   {total_chapters}")
    print(f"Topics:     {total_topics}")
    print(f"MCQs:       {total_mcqs}")
    print(f"Flashcards: {total_flashcards}")
    print(f"DB size:    {db_size / 1024 / 1024:.1f} MB")
    print(f"Hash:       {content_hash}")
    print(f"Output:     {OUTPUT_DB}")

    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for w in warnings[:20]:
            print(f"  - {w}")
        if len(warnings) > 20:
            print(f"  ... and {len(warnings) - 20} more")

    # Verify row counts
    conn = sqlite3.connect(str(OUTPUT_DB))
    c = conn.cursor()
    for table in ["subjects", "chapters", "topics", "mcqs", "flashcards"]:
        count = c.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"  {table}: {count} rows")
    search_count = c.execute("SELECT COUNT(*) FROM search_index").fetchone()[0]
    print(f"  search_index: {search_count} rows")
    conn.close()


if __name__ == "__main__":
    build_db()
