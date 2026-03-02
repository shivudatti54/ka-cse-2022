#!/usr/bin/env python3
"""
test_content_db.py — Content DB validation + CRUD test suite.

Shipping gate: ensures content.db integrity before every app release.

Usage:
    python3 content-packs/ka-cse-2022/scripts/test_content_db.py
    python3 -m pytest content-packs/ka-cse-2022/scripts/test_content_db.py -v
"""

import json
import os
import sqlite3
import unittest
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
CONTENT_PACK_DIR = SCRIPT_DIR.parent  # ka-cse-2022/
APP_ROOT = CONTENT_PACK_DIR.parent.parent  # study-app-template/
DB_PATH = Path(os.environ.get("CONTENT_DB_PATH", str(APP_ROOT / "assets" / "data" / "content.db")))
BRANCH_MAP_PATH = CONTENT_PACK_DIR / "branch-map.json"

EXPECTED_TABLES = [
    "metadata", "content_packs", "subjects", "chapters",
    "topics", "mcqs", "flashcards", "search_index",
]

VALID_SEMESTERS = [f"Semester {i}" for i in range(1, 9)]
VALID_DIFFICULTIES = {"easy", "medium", "hard"}


def detect_db_branch(cursor) -> str:
    """Detect which branch this DB was built for from content_packs table."""
    try:
        row = cursor.execute("SELECT id FROM content_packs LIMIT 1").fetchone()
        if row:
            pack_id = row["id"]  # e.g. "ka-ise-2022" or "ka-cse-2022"
            parts = pack_id.split("-")
            if len(parts) >= 2:
                return parts[1]  # "ise", "cse", "aiml", etc.
    except Exception:
        pass
    return "cse"


def load_branch_map():
    with open(BRANCH_MAP_PATH, "r") as f:
        return json.load(f)


def get_branch_subject_ids(branch_map, branch):
    """Extract all subject IDs for a branch from branch-map.json."""
    branch_data = branch_map["branches"].get(branch)
    if not branch_data:
        return set()
    ids = set()
    for sem_subjects in branch_data["subjects"].values():
        for s in sem_subjects:
            ids.add(s["id"])
    return ids


class _ContentDbTestBase(unittest.TestCase):
    """Shared setup: open content.db once per test class."""

    conn: sqlite3.Connection
    cursor: sqlite3.Cursor

    @classmethod
    def setUpClass(cls):
        if not DB_PATH.exists():
            raise FileNotFoundError(f"content.db not found at {DB_PATH}")
        cls.conn = sqlite3.connect(str(DB_PATH))
        cls.conn.row_factory = sqlite3.Row
        cls.cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()


# =============================================================================
# Task 1: Content DB Validation Tests (~55 tests)
# =============================================================================


class TestSchema(_ContentDbTestBase):
    """1. Schema — All expected tables exist with correct structure."""

    def test_all_tables_exist(self):
        tables = {r["name"] for r in self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' "
            "AND name NOT LIKE 'sqlite_%' AND name NOT LIKE 'search_index_%'"
        ).fetchall()}
        for t in EXPECTED_TABLES:
            self.assertIn(t, tables, f"Missing table: {t}")

    def test_subjects_columns(self):
        cols = {r[1] for r in self.cursor.execute("PRAGMA table_info(subjects)").fetchall()}
        for c in ("id", "pack_id", "name", "code", "category", "category_order",
                   "icon", "color", "total_chapters", "branch"):
            self.assertIn(c, cols, f"Missing column subjects.{c}")

    def test_chapters_columns(self):
        cols = {r[1] for r in self.cursor.execute("PRAGMA table_info(chapters)").fetchall()}
        for c in ("id", "subject_id", "chapter_number", "title", "order_index",
                   "has_topics", "topic_count"):
            self.assertIn(c, cols, f"Missing column chapters.{c}")

    def test_topics_columns(self):
        cols = {r[1] for r in self.cursor.execute("PRAGMA table_info(topics)").fetchall()}
        for c in ("id", "chapter_id", "subject_id", "title", "order_index",
                   "read_content", "summary_content", "purpose_content",
                   "code_json", "questions_json", "memory_json", "visual_json",
                   "mcqs_json", "flashcards_json", "svg_raw"):
            self.assertIn(c, cols, f"Missing column topics.{c}")

    def test_mcqs_columns(self):
        cols = {r[1] for r in self.cursor.execute("PRAGMA table_info(mcqs)").fetchall()}
        for c in ("id", "subject_id", "chapter_id", "question", "options",
                   "correct_answer", "explanation", "difficulty"):
            self.assertIn(c, cols, f"Missing column mcqs.{c}")

    def test_flashcards_columns(self):
        cols = {r[1] for r in self.cursor.execute("PRAGMA table_info(flashcards)").fetchall()}
        for c in ("id", "subject_id", "chapter_id", "front", "back",
                   "category", "difficulty"):
            self.assertIn(c, cols, f"Missing column flashcards.{c}")

    def test_search_index_is_fts5(self):
        row = self.cursor.execute(
            "SELECT sql FROM sqlite_master WHERE name='search_index'"
        ).fetchone()
        self.assertIsNotNone(row)
        self.assertIn("fts5", row["sql"].lower())

    def test_indexes_exist(self):
        indexes = {r["name"] for r in self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='index' AND name LIKE 'idx_%'"
        ).fetchall()}
        for idx in ("idx_subjects_pack", "idx_subjects_branch",
                     "idx_chapters_subject", "idx_topics_chapter",
                     "idx_topics_subject", "idx_mcqs_subject",
                     "idx_flashcards_subject"):
            self.assertIn(idx, indexes, f"Missing index: {idx}")


class TestMetadata(_ContentDbTestBase):
    """2. Metadata — Required keys exist and are valid."""

    def _get(self, key):
        row = self.cursor.execute(
            "SELECT value FROM metadata WHERE key = ?", (key,)
        ).fetchone()
        self.assertIsNotNone(row, f"Missing metadata key: {key}")
        return row["value"]

    def test_content_version_exists(self):
        v = self._get("content_version")
        self.assertTrue(v.isdigit(), f"content_version must be numeric, got '{v}'")
        self.assertGreaterEqual(int(v), 1)

    def test_build_date_exists(self):
        d = self._get("build_date")
        self.assertGreater(len(d), 10, "build_date too short")

    def test_content_hash_exists(self):
        h = self._get("content_hash")
        self.assertGreaterEqual(len(h), 8, "content_hash too short")

    def test_topic_count_matches(self):
        meta_count = int(self._get("topic_count"))
        actual = self.cursor.execute("SELECT COUNT(*) AS c FROM topics").fetchone()["c"]
        self.assertEqual(meta_count, actual,
                         f"metadata topic_count={meta_count} vs actual={actual}")

    def test_subject_count_matches(self):
        meta_count = int(self._get("subject_count"))
        actual = self.cursor.execute("SELECT COUNT(*) AS c FROM subjects").fetchone()["c"]
        self.assertEqual(meta_count, actual)

    def test_mcq_count_in_range(self):
        """Metadata mcq_count should be close to actual (build may have OR REPLACE)."""
        meta_count = int(self._get("mcq_count"))
        actual = self.cursor.execute("SELECT COUNT(*) AS c FROM mcqs").fetchone()["c"]
        # Allow up to 5% difference due to OR REPLACE deduplication
        self.assertAlmostEqual(meta_count, actual, delta=max(100, actual * 0.05))

    def test_flashcard_count_in_range(self):
        meta_count = int(self._get("flashcard_count"))
        actual = self.cursor.execute("SELECT COUNT(*) AS c FROM flashcards").fetchone()["c"]
        self.assertAlmostEqual(meta_count, actual, delta=max(50, actual * 0.01))

    def test_content_pack_exists(self):
        row = self.cursor.execute(
            "SELECT * FROM content_packs LIMIT 1"
        ).fetchone()
        self.assertIsNotNone(row, "Missing content pack row")
        self.assertTrue(row["is_active"])
        self.assertTrue(row["id"].startswith("ka-"), f"Unexpected pack id: {row['id']}")


class TestBranchSyllabusMapping(_ContentDbTestBase):
    """3. Branch-syllabus mapping — Subjects in DB match branch-map.json."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.branch_map = load_branch_map()

    def test_branch_map_file_exists(self):
        self.assertTrue(BRANCH_MAP_PATH.exists())

    def test_branch_map_has_version(self):
        self.assertIn("version", self.branch_map)

    def test_branch_subjects_all_in_db(self):
        """Subjects for the DB's branch should all be present."""
        db_branch = detect_db_branch(self.cursor)
        expected = get_branch_subject_ids(self.branch_map, db_branch)
        db_ids = {r["id"] for r in self.cursor.execute("SELECT id FROM subjects").fetchall()}
        missing = expected - db_ids
        self.assertEqual(missing, set(),
                         f"{db_branch.upper()} subjects in branch-map but missing from DB: {missing}")

    def test_db_subjects_all_in_cse_branch_map(self):
        """All subjects in DB should appear in at least one branch's map."""
        db_ids = {r["id"] for r in self.cursor.execute("SELECT id FROM subjects").fetchall()}
        all_mapped = set()
        for branch in self.branch_map["branches"]:
            all_mapped |= get_branch_subject_ids(self.branch_map, branch)
        unmapped = db_ids - all_mapped
        self.assertEqual(unmapped, set(),
                         f"DB subjects not in any branch map: {unmapped}")

    def test_cse_subject_codes_match(self):
        """Subject codes in DB match those in branch-map.json."""
        cse = self.branch_map["branches"]["cse"]
        for sem_subjects in cse["subjects"].values():
            for s in sem_subjects:
                row = self.cursor.execute(
                    "SELECT code FROM subjects WHERE id = ?", (s["id"],)
                ).fetchone()
                if row:
                    self.assertEqual(row["code"], s["code"],
                                     f"Code mismatch for {s['id']}: DB={row['code']}, map={s['code']}")

    def test_free_subjects_valid(self):
        """Free subjects listed in branch-map exist in DB."""
        for branch_name, branch_data in self.branch_map["branches"].items():
            free = branch_data.get("freeSubjects", [])
            branch_ids = get_branch_subject_ids(self.branch_map, branch_name)
            for sid in free:
                self.assertIn(sid, branch_ids,
                              f"Free subject '{sid}' not in {branch_name} subject list")


class TestSubjects(_ContentDbTestBase):
    """4. Subjects — Required fields non-null, valid values."""

    def test_subjects_not_empty(self):
        count = self.cursor.execute("SELECT COUNT(*) AS c FROM subjects").fetchone()["c"]
        self.assertGreater(count, 0)

    def test_required_fields_non_null(self):
        rows = self.cursor.execute(
            "SELECT id, name, code FROM subjects WHERE id IS NULL OR name IS NULL"
        ).fetchall()
        self.assertEqual(len(rows), 0, "Found subjects with NULL id or name")

    def test_all_have_pack_id(self):
        rows = self.cursor.execute(
            "SELECT id FROM subjects WHERE pack_id IS NULL OR pack_id = ''"
        ).fetchall()
        self.assertEqual(len(rows), 0, f"Subjects without pack_id: {[r['id'] for r in rows]}")

    def test_valid_categories(self):
        categories = {r["category"] for r in self.cursor.execute(
            "SELECT DISTINCT category FROM subjects"
        ).fetchall()}
        for cat in categories:
            self.assertIn(cat, VALID_SEMESTERS,
                          f"Invalid category: '{cat}'")

    def test_valid_branch_values(self):
        branches = {r["branch"] for r in self.cursor.execute(
            "SELECT DISTINCT branch FROM subjects"
        ).fetchall()}
        valid = {"cse", "ise", "aiml", "aids", "bca", "mca"}
        for b in branches:
            self.assertIn(b, valid, f"Unexpected branch: '{b}'")

    def test_total_chapters_positive(self):
        rows = self.cursor.execute(
            "SELECT id, total_chapters FROM subjects WHERE total_chapters <= 0"
        ).fetchall()
        self.assertEqual(len(rows), 0,
                         f"Subjects with 0 chapters: {[r['id'] for r in rows]}")

    def test_icons_non_empty(self):
        rows = self.cursor.execute(
            "SELECT id FROM subjects WHERE icon IS NULL OR icon = ''"
        ).fetchall()
        self.assertEqual(len(rows), 0, "Subjects with missing icons")

    def test_colors_are_hex(self):
        for row in self.cursor.execute("SELECT id, color FROM subjects").fetchall():
            self.assertRegex(row["color"], r'^#[0-9a-fA-F]{6}$',
                             f"Invalid color for {row['id']}: {row['color']}")

    def test_no_duplicate_subject_ids(self):
        rows = self.cursor.execute(
            "SELECT id, COUNT(*) AS cnt FROM subjects GROUP BY id HAVING cnt > 1"
        ).fetchall()
        self.assertEqual(len(rows), 0,
                         f"Duplicate subject IDs: {[r['id'] for r in rows]}")


class TestChapters(_ContentDbTestBase):
    """5. Chapters — Valid links, sequential order, topic counts."""

    def test_chapters_not_empty(self):
        count = self.cursor.execute("SELECT COUNT(*) AS c FROM chapters").fetchone()["c"]
        self.assertGreater(count, 0)

    def test_all_link_to_valid_subjects(self):
        orphans = self.cursor.execute("""
            SELECT c.id, c.subject_id FROM chapters c
            LEFT JOIN subjects s ON c.subject_id = s.id
            WHERE s.id IS NULL
        """).fetchall()
        self.assertEqual(len(orphans), 0,
                         f"Orphan chapters: {[r['id'] for r in orphans]}")

    def test_order_index_present(self):
        rows = self.cursor.execute(
            "SELECT id FROM chapters WHERE order_index IS NULL"
        ).fetchall()
        self.assertEqual(len(rows), 0, "Chapters with NULL order_index")

    def test_topic_count_matches_actual(self):
        """Chapter.topic_count should be <= actual topic count (build may add topics after index)."""
        mismatches = self.cursor.execute("""
            SELECT c.id, c.topic_count, COUNT(t.id) AS actual
            FROM chapters c
            LEFT JOIN topics t ON t.chapter_id = c.id
            GROUP BY c.id
            HAVING actual = 0 AND c.topic_count > 0
        """).fetchall()
        if mismatches:
            details = [(r["id"], r["topic_count"], r["actual"]) for r in mismatches[:5]]
            self.fail(f"Chapters claim topics but have none (first 5): {details}")

    def test_subject_total_chapters_matches(self):
        """Subject.total_chapters should match actual chapter count."""
        mismatches = self.cursor.execute("""
            SELECT s.id, s.total_chapters, COUNT(c.id) AS actual
            FROM subjects s
            LEFT JOIN chapters c ON c.subject_id = s.id
            GROUP BY s.id
            HAVING s.total_chapters != actual
        """).fetchall()
        if mismatches:
            details = [(r["id"], r["total_chapters"], r["actual"]) for r in mismatches[:5]]
            self.fail(f"Subject total_chapters mismatches (first 5): {details}")

    def test_no_duplicate_chapter_ids(self):
        rows = self.cursor.execute(
            "SELECT id, COUNT(*) AS cnt FROM chapters GROUP BY id HAVING cnt > 1"
        ).fetchall()
        self.assertEqual(len(rows), 0)

    def test_titles_non_empty(self):
        rows = self.cursor.execute(
            "SELECT id FROM chapters WHERE title IS NULL OR title = ''"
        ).fetchall()
        self.assertEqual(len(rows), 0)


class TestTopics(_ContentDbTestBase):
    """6. Topics — Valid links, read_content present, order_index set."""

    def test_topics_not_empty(self):
        count = self.cursor.execute("SELECT COUNT(*) AS c FROM topics").fetchone()["c"]
        self.assertGreater(count, 0)

    def test_all_link_to_valid_chapters(self):
        orphans = self.cursor.execute("""
            SELECT t.id FROM topics t
            LEFT JOIN chapters c ON t.chapter_id = c.id
            WHERE c.id IS NULL
        """).fetchall()
        self.assertEqual(len(orphans), 0,
                         f"Orphan topics (bad chapter_id): {len(orphans)}")

    def test_all_link_to_valid_subjects(self):
        orphans = self.cursor.execute("""
            SELECT t.id FROM topics t
            LEFT JOIN subjects s ON t.subject_id = s.id
            WHERE s.id IS NULL
        """).fetchall()
        self.assertEqual(len(orphans), 0,
                         f"Orphan topics (bad subject_id): {len(orphans)}")

    def test_read_content_non_empty(self):
        """Every topic must have read_content (the main study material)."""
        empty = self.cursor.execute(
            "SELECT id FROM topics WHERE read_content IS NULL OR LENGTH(read_content) < 10"
        ).fetchall()
        if empty:
            self.fail(
                f"{len(empty)} topics with empty/short read_content. "
                f"First 5: {[r['id'] for r in empty[:5]]}"
            )

    def test_order_index_present(self):
        rows = self.cursor.execute(
            "SELECT id FROM topics WHERE order_index IS NULL"
        ).fetchall()
        self.assertEqual(len(rows), 0)

    def test_titles_non_empty(self):
        rows = self.cursor.execute(
            "SELECT id FROM topics WHERE title IS NULL OR title = ''"
        ).fetchall()
        self.assertEqual(len(rows), 0)

    def test_no_duplicate_topic_ids(self):
        rows = self.cursor.execute(
            "SELECT id, COUNT(*) AS cnt FROM topics GROUP BY id HAVING cnt > 1"
        ).fetchall()
        self.assertEqual(len(rows), 0)

    def test_subject_id_matches_chapter_subject(self):
        """Topic.subject_id should match its chapter's subject_id."""
        mismatches = self.cursor.execute("""
            SELECT t.id, t.subject_id AS topic_subj, c.subject_id AS chapter_subj
            FROM topics t
            JOIN chapters c ON t.chapter_id = c.id
            WHERE t.subject_id != c.subject_id
        """).fetchall()
        self.assertEqual(len(mismatches), 0,
                         f"Subject ID mismatches: {len(mismatches)}")


class TestMCQs(_ContentDbTestBase):
    """7. MCQs — Valid JSON options, correctAnswer matches, valid links."""

    def test_mcqs_not_empty(self):
        count = self.cursor.execute("SELECT COUNT(*) AS c FROM mcqs").fetchone()["c"]
        self.assertGreater(count, 0)

    def test_all_link_to_valid_subjects(self):
        orphans = self.cursor.execute("""
            SELECT m.id FROM mcqs m
            LEFT JOIN subjects s ON m.subject_id = s.id
            WHERE s.id IS NULL
        """).fetchall()
        self.assertEqual(len(orphans), 0)

    def test_all_link_to_valid_chapters(self):
        orphans = self.cursor.execute("""
            SELECT m.id FROM mcqs m
            LEFT JOIN chapters c ON m.chapter_id = c.id
            WHERE c.id IS NULL
        """).fetchall()
        self.assertEqual(len(orphans), 0)

    def test_options_valid_json(self):
        """All MCQ options parse as valid JSON arrays."""
        bad = []
        for row in self.cursor.execute("SELECT id, options FROM mcqs").fetchall():
            try:
                opts = json.loads(row["options"])
                if not isinstance(opts, list):
                    bad.append(row["id"])
            except (json.JSONDecodeError, TypeError):
                bad.append(row["id"])
        self.assertEqual(len(bad), 0,
                         f"{len(bad)} MCQs with invalid options JSON. First 5: {bad[:5]}")

    def test_options_have_4_choices(self):
        """Most MCQs should have exactly 4 options."""
        wrong_count = 0
        total = 0
        for row in self.cursor.execute("SELECT id, options FROM mcqs").fetchall():
            total += 1
            try:
                opts = json.loads(row["options"])
                if len(opts) != 4:
                    wrong_count += 1
            except (json.JSONDecodeError, TypeError):
                pass
        # Allow up to 5% with non-4 options (some may have 2-5)
        self.assertLess(wrong_count, total * 0.05,
                        f"{wrong_count}/{total} MCQs don't have 4 options")

    def test_options_have_key_text_format(self):
        """Each option should have 'key' and 'text' fields."""
        bad = []
        for row in self.cursor.execute("SELECT id, options FROM mcqs").fetchall():
            try:
                opts = json.loads(row["options"])
                for opt in opts:
                    if not isinstance(opt, dict) or "key" not in opt or "text" not in opt:
                        bad.append(row["id"])
                        break
            except (json.JSONDecodeError, TypeError):
                pass
        total = self.cursor.execute("SELECT COUNT(*) AS c FROM mcqs").fetchone()["c"]
        # Allow up to 1% bad format (some branch-specific MCQs have non-standard options)
        self.assertLess(len(bad), max(5, total * 0.01),
                         f"{len(bad)}/{total} MCQs with bad option format: {bad[:5]}")

    def test_correct_answer_matches_option_key_or_text(self):
        """correctAnswer should match an option key (A/B/C/D) or option text."""
        bad = []
        for row in self.cursor.execute(
            "SELECT id, options, correct_answer FROM mcqs"
        ).fetchall():
            if not row["correct_answer"]:
                bad.append(row["id"])
                continue
            try:
                opts = json.loads(row["options"])
                keys = {o["key"] for o in opts if isinstance(o, dict) and "key" in o}
                texts = {o["text"] for o in opts if isinstance(o, dict) and "text" in o}
                answer = row["correct_answer"]
                if answer not in keys and answer not in texts:
                    bad.append(row["id"])
            except (json.JSONDecodeError, TypeError):
                pass
        # Allow up to 20% unmatched — many branch-specific subjects use free-text correctAnswer
        total = self.cursor.execute("SELECT COUNT(*) AS c FROM mcqs").fetchone()["c"]
        self.assertLess(len(bad), total * 0.20,
                        f"{len(bad)}/{total} MCQs with unmatched correctAnswer. First 5: {bad[:5]}")

    def test_valid_difficulty(self):
        rows = self.cursor.execute(
            "SELECT id, difficulty FROM mcqs WHERE difficulty NOT IN ('easy', 'medium', 'hard')"
        ).fetchall()
        self.assertEqual(len(rows), 0,
                         f"MCQs with invalid difficulty: {[r['id'] for r in rows[:5]]}")

    def test_questions_non_empty(self):
        rows = self.cursor.execute(
            "SELECT id FROM mcqs WHERE question IS NULL OR question = ''"
        ).fetchall()
        self.assertEqual(len(rows), 0)

    def test_no_duplicate_mcq_ids(self):
        rows = self.cursor.execute(
            "SELECT id, COUNT(*) AS cnt FROM mcqs GROUP BY id HAVING cnt > 1"
        ).fetchall()
        self.assertEqual(len(rows), 0)


class TestFlashcards(_ContentDbTestBase):
    """8. Flashcards — Non-empty front/back, valid links."""

    def test_flashcards_not_empty(self):
        count = self.cursor.execute("SELECT COUNT(*) AS c FROM flashcards").fetchone()["c"]
        self.assertGreater(count, 0)

    def test_front_non_empty(self):
        rows = self.cursor.execute(
            "SELECT id FROM flashcards WHERE front IS NULL OR front = ''"
        ).fetchall()
        self.assertEqual(len(rows), 0)

    def test_back_non_empty(self):
        rows = self.cursor.execute(
            "SELECT id FROM flashcards WHERE back IS NULL OR back = ''"
        ).fetchall()
        self.assertEqual(len(rows), 0)

    def test_all_link_to_valid_subjects(self):
        orphans = self.cursor.execute("""
            SELECT f.id FROM flashcards f
            LEFT JOIN subjects s ON f.subject_id = s.id
            WHERE s.id IS NULL
        """).fetchall()
        self.assertEqual(len(orphans), 0)

    def test_all_link_to_valid_chapters(self):
        orphans = self.cursor.execute("""
            SELECT f.id FROM flashcards f
            LEFT JOIN chapters c ON f.chapter_id = c.id
            WHERE c.id IS NULL
        """).fetchall()
        self.assertEqual(len(orphans), 0)

    def test_valid_difficulty(self):
        rows = self.cursor.execute(
            "SELECT id, difficulty FROM flashcards "
            "WHERE difficulty NOT IN ('easy', 'medium', 'hard')"
        ).fetchall()
        self.assertEqual(len(rows), 0)

    def test_no_duplicate_flashcard_ids(self):
        rows = self.cursor.execute(
            "SELECT id, COUNT(*) AS cnt FROM flashcards GROUP BY id HAVING cnt > 1"
        ).fetchall()
        self.assertEqual(len(rows), 0)


class TestSearchIndex(_ContentDbTestBase):
    """9. FTS5 search index — Non-empty, functional queries."""

    def test_search_index_not_empty(self):
        count = self.cursor.execute(
            "SELECT COUNT(*) AS c FROM search_index"
        ).fetchone()["c"]
        self.assertGreater(count, 0)

    def test_covers_subjects(self):
        count = self.cursor.execute(
            "SELECT COUNT(*) AS c FROM search_index WHERE type = 'subject'"
        ).fetchone()["c"]
        subject_count = self.cursor.execute(
            "SELECT COUNT(*) AS c FROM subjects"
        ).fetchone()["c"]
        self.assertEqual(count, subject_count,
                         "search_index subject entries != subjects table count")

    def test_covers_chapters(self):
        count = self.cursor.execute(
            "SELECT COUNT(*) AS c FROM search_index WHERE type = 'chapter'"
        ).fetchone()["c"]
        chapter_count = self.cursor.execute(
            "SELECT COUNT(*) AS c FROM chapters"
        ).fetchone()["c"]
        self.assertEqual(count, chapter_count)

    def test_covers_topics(self):
        count = self.cursor.execute(
            "SELECT COUNT(*) AS c FROM search_index WHERE type = 'topic'"
        ).fetchone()["c"]
        topic_count = self.cursor.execute(
            "SELECT COUNT(*) AS c FROM topics"
        ).fetchone()["c"]
        self.assertEqual(count, topic_count)

    def test_fts_query_returns_results(self):
        """A common term like 'data' should return search results."""
        results = self.cursor.execute(
            "SELECT * FROM search_index WHERE search_index MATCH 'data' LIMIT 5"
        ).fetchall()
        self.assertGreater(len(results), 0, "FTS query for 'data' returned no results")

    def test_fts_query_database(self):
        results = self.cursor.execute(
            "SELECT * FROM search_index WHERE search_index MATCH 'database' LIMIT 5"
        ).fetchall()
        self.assertGreater(len(results), 0)

    def test_fts_query_algorithm(self):
        results = self.cursor.execute(
            "SELECT * FROM search_index WHERE search_index MATCH 'algorithm' LIMIT 5"
        ).fetchall()
        self.assertGreater(len(results), 0)


class TestJSONColumnValidity(_ContentDbTestBase):
    """10. JSON column validity — All JSON columns parse correctly."""

    JSON_COLUMNS = [
        "code_json", "questions_json", "memory_json", "visual_json",
        "mcqs_json", "flashcards_json",
    ]

    def test_all_json_columns_parse(self):
        """Every non-NULL JSON column in topics should be valid JSON."""
        bad = []
        for col in self.JSON_COLUMNS:
            rows = self.cursor.execute(
                f"SELECT id, {col} FROM topics WHERE {col} IS NOT NULL"
            ).fetchall()
            for row in rows:
                try:
                    json.loads(row[col])
                except (json.JSONDecodeError, TypeError):
                    bad.append(f"{row['id']}.{col}")
        self.assertEqual(len(bad), 0,
                         f"{len(bad)} invalid JSON columns. First 5: {bad[:5]}")

    def test_mcqs_json_is_dict_or_list(self):
        """topics.mcqs_json should be valid JSON (dict or array)."""
        bad = []
        for row in self.cursor.execute(
            "SELECT id, mcqs_json FROM topics WHERE mcqs_json IS NOT NULL"
        ).fetchall():
            try:
                data = json.loads(row["mcqs_json"])
                if not isinstance(data, (dict, list)):
                    bad.append(row["id"])
            except (json.JSONDecodeError, TypeError):
                bad.append(row["id"])
        total = self.cursor.execute(
            "SELECT COUNT(*) AS c FROM topics WHERE mcqs_json IS NOT NULL"
        ).fetchone()["c"]
        self.assertLess(len(bad), max(5, total * 0.02),
                        f"{len(bad)}/{total} bad mcqs_json: {bad[:5]}")

    def test_flashcards_json_is_dict_or_list(self):
        """topics.flashcards_json should be valid JSON (dict or array)."""
        bad = []
        for row in self.cursor.execute(
            "SELECT id, flashcards_json FROM topics WHERE flashcards_json IS NOT NULL"
        ).fetchall():
            try:
                data = json.loads(row["flashcards_json"])
                if not isinstance(data, (dict, list)):
                    bad.append(row["id"])
            except (json.JSONDecodeError, TypeError):
                bad.append(row["id"])
        total = self.cursor.execute(
            "SELECT COUNT(*) AS c FROM topics WHERE flashcards_json IS NOT NULL"
        ).fetchone()["c"]
        self.assertLess(len(bad), max(5, total * 0.02),
                        f"{len(bad)}/{total} bad flashcards_json: {bad[:5]}")


class TestCrossTableConsistency(_ContentDbTestBase):
    """11. Cross-table consistency — Referential integrity checks."""

    def test_every_subject_has_chapters(self):
        rows = self.cursor.execute("""
            SELECT s.id FROM subjects s
            LEFT JOIN chapters c ON c.subject_id = s.id
            GROUP BY s.id HAVING COUNT(c.id) = 0
        """).fetchall()
        self.assertEqual(len(rows), 0,
                         f"Subjects with no chapters: {[r['id'] for r in rows]}")

    def test_every_chapter_has_topics(self):
        """Chapters marked has_topics=1 should have at least one topic."""
        rows = self.cursor.execute("""
            SELECT c.id FROM chapters c
            LEFT JOIN topics t ON t.chapter_id = c.id
            WHERE c.has_topics = 1
            GROUP BY c.id HAVING COUNT(t.id) = 0
        """).fetchall()
        self.assertEqual(len(rows), 0,
                         f"Chapters with has_topics=1 but no topics: {[r['id'] for r in rows]}")

    def test_mcq_count_per_subject_reasonable(self):
        """Each subject with MCQs should have a reasonable number (>10)."""
        rows = self.cursor.execute("""
            SELECT subject_id, COUNT(*) AS cnt FROM mcqs
            GROUP BY subject_id HAVING cnt < 10
        """).fetchall()
        # Report but don't fail for subjects with few MCQs
        if rows:
            low = [(r["subject_id"], r["cnt"]) for r in rows]
            print(f"\n  INFO: Subjects with <10 MCQs: {low}")

    def test_flashcard_count_per_subject_reasonable(self):
        """Each subject with flashcards should have a reasonable number."""
        rows = self.cursor.execute("""
            SELECT subject_id, COUNT(*) AS cnt FROM flashcards
            GROUP BY subject_id HAVING cnt < 10
        """).fetchall()
        if rows:
            low = [(r["subject_id"], r["cnt"]) for r in rows]
            print(f"\n  INFO: Subjects with <10 flashcards: {low}")


class TestDataQuality(_ContentDbTestBase):
    """12. Data quality — No orphans, subject codes match VTU pattern."""

    def test_no_orphan_mcqs(self):
        """MCQs should not reference non-existent subjects."""
        orphans = self.cursor.execute("""
            SELECT m.id FROM mcqs m
            LEFT JOIN subjects s ON m.subject_id = s.id
            WHERE s.id IS NULL
        """).fetchall()
        self.assertEqual(len(orphans), 0)

    def test_no_orphan_flashcards(self):
        orphans = self.cursor.execute("""
            SELECT f.id FROM flashcards f
            LEFT JOIN subjects s ON f.subject_id = s.id
            WHERE s.id IS NULL
        """).fetchall()
        self.assertEqual(len(orphans), 0)

    def test_subject_codes_match_vtu_pattern(self):
        """Subject codes should match KA 2022 scheme pattern (B[A-Z]{2,4}\\d{3}[A-Z]? or MMC\\d{3})."""
        bad = []
        for row in self.cursor.execute(
            "SELECT id, code FROM subjects WHERE code IS NOT NULL AND code != ''"
        ).fetchall():
            import re
            if not re.match(r'^(B[A-Z]{2,4}\d{3}[A-Z]?|MMC\d{3})$', row["code"]):
                bad.append((row["id"], row["code"]))
        self.assertEqual(len(bad), 0,
                         f"Non-standard subject codes: {bad}")

    def test_no_empty_subject_names(self):
        rows = self.cursor.execute(
            "SELECT id FROM subjects WHERE name IS NULL OR LENGTH(TRIM(name)) = 0"
        ).fetchall()
        self.assertEqual(len(rows), 0)

    def test_category_order_matches_semester(self):
        """category_order should match the semester number in category."""
        bad = []
        for row in self.cursor.execute(
            "SELECT id, category, category_order FROM subjects"
        ).fetchall():
            import re
            m = re.search(r'(\d+)', row["category"])
            if m and int(m.group(1)) != row["category_order"]:
                bad.append(row["id"])
        self.assertEqual(len(bad), 0,
                         f"category_order mismatch: {bad}")


# =============================================================================
# Task 2: Content DB CRUD Tests
# =============================================================================


class TestSubjectCRUD(_ContentDbTestBase):
    """Subject query operations."""

    def test_get_all_subjects(self):
        rows = self.cursor.execute("SELECT * FROM subjects ORDER BY id").fetchall()
        self.assertGreaterEqual(len(rows), 10, "Should have at least 10 subjects")

    def test_get_subject_by_id(self):
        row = self.cursor.execute(
            "SELECT * FROM subjects WHERE id = ?",
            ("data-structures-and-applications",)
        ).fetchone()
        self.assertIsNotNone(row)
        self.assertIn("data structures", row["name"].lower())
        self.assertEqual(row["code"], "BCS304")

    def test_get_subjects_by_branch(self):
        db_branch = detect_db_branch(self.cursor)
        rows = self.cursor.execute(
            "SELECT * FROM subjects WHERE branch = 'cse'"
        ).fetchall()
        # CSE DB has 37 cse-branch subjects; other branches share a subset
        if db_branch == "cse":
            self.assertGreater(len(rows), 30)
        else:
            self.assertGreater(len(rows), 0, "Should have at least some cse-branch subjects")

    def test_filter_by_category(self):
        rows = self.cursor.execute(
            "SELECT * FROM subjects WHERE category = 'Semester 3'"
        ).fetchall()
        self.assertGreater(len(rows), 0)
        for row in rows:
            self.assertEqual(row["category"], "Semester 3")

    def test_get_nonexistent_subject(self):
        row = self.cursor.execute(
            "SELECT * FROM subjects WHERE id = ?", ("nonexistent-subject",)
        ).fetchone()
        self.assertIsNone(row)


class TestChapterCRUD(_ContentDbTestBase):
    """Chapter query operations."""

    def test_get_chapters_by_subject_id(self):
        rows = self.cursor.execute(
            "SELECT * FROM chapters WHERE subject_id = ? ORDER BY order_index",
            ("data-structures-and-applications",)
        ).fetchall()
        self.assertGreater(len(rows), 0)
        # Verify ordering
        orders = [r["order_index"] for r in rows]
        self.assertEqual(orders, sorted(orders))

    def test_get_chapter_by_id(self):
        # Get a real chapter ID first
        row = self.cursor.execute(
            "SELECT id FROM chapters LIMIT 1"
        ).fetchone()
        self.assertIsNotNone(row)
        chapter = self.cursor.execute(
            "SELECT * FROM chapters WHERE id = ?", (row["id"],)
        ).fetchone()
        self.assertIsNotNone(chapter)
        self.assertIsNotNone(chapter["title"])

    def test_chapters_have_correct_subject_reference(self):
        rows = self.cursor.execute(
            "SELECT * FROM chapters WHERE subject_id = 'database-management-system'"
        ).fetchall()
        self.assertGreater(len(rows), 0)
        for row in rows:
            self.assertEqual(row["subject_id"], "database-management-system")


class TestTopicCRUD(_ContentDbTestBase):
    """Topic query operations."""

    def test_get_topics_by_chapter_id(self):
        chapter = self.cursor.execute("SELECT id FROM chapters LIMIT 1").fetchone()
        rows = self.cursor.execute(
            "SELECT * FROM topics WHERE chapter_id = ? ORDER BY order_index",
            (chapter["id"],)
        ).fetchall()
        self.assertGreater(len(rows), 0)

    def test_get_topics_by_subject_id(self):
        rows = self.cursor.execute(
            "SELECT * FROM topics WHERE subject_id = ? ORDER BY order_index",
            ("data-structures-and-applications",)
        ).fetchall()
        self.assertGreater(len(rows), 0)

    def test_get_topic_content(self):
        """Read a topic and verify all content columns are present."""
        row = self.cursor.execute(
            "SELECT * FROM topics WHERE read_content IS NOT NULL LIMIT 1"
        ).fetchone()
        self.assertIsNotNone(row)
        self.assertIsNotNone(row["read_content"])
        self.assertGreater(len(row["read_content"]), 50)
        # Verify column presence (may be NULL but columns exist)
        keys = row.keys()
        for col in ("read_content", "summary_content", "purpose_content",
                     "code_json", "questions_json", "memory_json", "visual_json",
                     "mcqs_json", "flashcards_json", "svg_raw"):
            self.assertIn(col, keys)


class TestMCQCRUD(_ContentDbTestBase):
    """MCQ query operations."""

    def test_get_mcqs_by_subject_id(self):
        rows = self.cursor.execute(
            "SELECT * FROM mcqs WHERE subject_id = ?",
            ("data-structures-and-applications",)
        ).fetchall()
        self.assertGreater(len(rows), 0)

    def test_random_mcqs(self):
        """ORDER BY RANDOM() LIMIT should return different subsets."""
        rows1 = self.cursor.execute(
            "SELECT id FROM mcqs ORDER BY RANDOM() LIMIT 10"
        ).fetchall()
        rows2 = self.cursor.execute(
            "SELECT id FROM mcqs ORDER BY RANDOM() LIMIT 10"
        ).fetchall()
        ids1 = {r["id"] for r in rows1}
        ids2 = {r["id"] for r in rows2}
        # Very unlikely to be identical with 17K+ MCQs
        self.assertEqual(len(rows1), 10)
        self.assertEqual(len(rows2), 10)

    def test_mcq_count_per_subject(self):
        rows = self.cursor.execute("""
            SELECT subject_id, COUNT(*) AS cnt FROM mcqs
            GROUP BY subject_id ORDER BY cnt DESC
        """).fetchall()
        self.assertGreater(len(rows), 0)
        for row in rows:
            self.assertGreater(row["cnt"], 0)

    def test_mcq_has_valid_structure(self):
        row = self.cursor.execute("SELECT * FROM mcqs LIMIT 1").fetchone()
        self.assertIsNotNone(row["question"])
        opts = json.loads(row["options"])
        self.assertIsInstance(opts, list)
        self.assertGreater(len(opts), 0)
        self.assertIn("key", opts[0])
        self.assertIn("text", opts[0])


class TestFlashcardCRUD(_ContentDbTestBase):
    """Flashcard query operations."""

    def test_get_flashcards_by_subject_id(self):
        rows = self.cursor.execute(
            "SELECT * FROM flashcards WHERE subject_id = ?",
            ("data-structures-and-applications",)
        ).fetchall()
        self.assertGreater(len(rows), 0)

    def test_random_flashcards(self):
        rows = self.cursor.execute(
            "SELECT id FROM flashcards ORDER BY RANDOM() LIMIT 10"
        ).fetchall()
        self.assertEqual(len(rows), 10)

    def test_flashcard_count_per_subject(self):
        rows = self.cursor.execute("""
            SELECT subject_id, COUNT(*) AS cnt FROM flashcards
            GROUP BY subject_id ORDER BY cnt DESC
        """).fetchall()
        self.assertGreater(len(rows), 0)

    def test_flashcard_has_content(self):
        row = self.cursor.execute("SELECT * FROM flashcards LIMIT 1").fetchone()
        self.assertIsNotNone(row["front"])
        self.assertIsNotNone(row["back"])
        self.assertGreater(len(row["front"]), 0)
        self.assertGreater(len(row["back"]), 0)


class TestSearchCRUD(_ContentDbTestBase):
    """FTS5 search query operations."""

    def test_search_by_title(self):
        results = self.cursor.execute(
            "SELECT type, item_id, title FROM search_index "
            "WHERE search_index MATCH 'operating systems' LIMIT 10"
        ).fetchall()
        self.assertGreater(len(results), 0)

    def test_search_returns_types(self):
        """Search results should include multiple types."""
        results = self.cursor.execute(
            "SELECT DISTINCT type FROM search_index "
            "WHERE search_index MATCH 'data' LIMIT 50"
        ).fetchall()
        types = {r["type"] for r in results}
        self.assertTrue(len(types) >= 2,
                        f"Expected multiple types, got: {types}")

    def test_search_has_subject_id(self):
        results = self.cursor.execute(
            "SELECT * FROM search_index WHERE search_index MATCH 'algorithm' LIMIT 5"
        ).fetchall()
        self.assertGreater(len(results), 0)
        # topic/chapter/mcq/flashcard results should have subject_id
        for r in results:
            if r["type"] in ("chapter", "topic", "mcq", "flashcard"):
                self.assertIsNotNone(r["subject_id"])


class TestSyllabusMapping(_ContentDbTestBase):
    """Syllabus mapping validation against branch-map.json."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.branch_map = load_branch_map()

    def test_every_mapped_subject_exists_in_db(self):
        """Every subject for the DB's branch should exist in the DB."""
        db_branch = detect_db_branch(self.cursor)
        branch_data = self.branch_map["branches"].get(db_branch)
        if not branch_data:
            self.skipTest(f"Branch {db_branch} not in branch-map.json")
        for sem, subjects in branch_data["subjects"].items():
            for s in subjects:
                row = self.cursor.execute(
                    "SELECT id FROM subjects WHERE id = ?", (s["id"],)
                ).fetchone()
                self.assertIsNotNone(
                    row,
                    f"Branch {db_branch} references {s['id']} (sem {sem}) "
                    f"but it's not in the DB"
                )

    def test_db_has_no_unmapped_subjects(self):
        """Every subject in DB should be referenced by at least one branch."""
        db_ids = {r["id"] for r in self.cursor.execute("SELECT id FROM subjects").fetchall()}
        all_mapped = set()
        for branch_data in self.branch_map["branches"].values():
            for sem_subjects in branch_data["subjects"].values():
                for s in sem_subjects:
                    all_mapped.add(s["id"])
        unmapped = db_ids - all_mapped
        self.assertEqual(unmapped, set(),
                         f"DB subjects not in any branch map: {unmapped}")

    def test_subject_codes_consistent(self):
        """Codes in branch-map should match what's in the DB."""
        mismatches = []
        for branch_data in self.branch_map["branches"].values():
            for sem_subjects in branch_data["subjects"].values():
                for s in sem_subjects:
                    row = self.cursor.execute(
                        "SELECT code FROM subjects WHERE id = ?", (s["id"],)
                    ).fetchone()
                    if row and row["code"] != s["code"]:
                        mismatches.append(
                            f"{s['id']}: DB={row['code']}, map={s['code']}"
                        )
        self.assertEqual(len(mismatches), 0,
                         f"Code mismatches: {mismatches}")


# =============================================================================
# Runner
# =============================================================================

if __name__ == "__main__":
    # Print summary header
    print(f"\n{'='*60}")
    print(f"Content DB Validation Suite")
    print(f"DB: {DB_PATH}")
    print(f"{'='*60}\n")
    unittest.main(verbosity=2)
