# Scripts Rename Summary

**Date:** 2026-02-15

## ✅ Files Renamed (25 total)

### Content Generation Scripts

| Old Name                      | New Name                               | Status     |
| ----------------------------- | -------------------------------------- | ---------- |
| `nvidia_content_generator.py` | `content_generator_nvidia.py`          | ✅ Renamed |
| `nvidia_code_generator.py`    | `code_generator_nvidia.py`             | ✅ Renamed |
| `minimax_code_generator.py`   | `code_generator_minimax_parallel.py`   | ✅ Renamed |
| `generate_vtu_content.py`     | `content_generator_legacy_nvidia.py`   | ✅ Renamed |
| `generate_hybrid.py`          | `content_generator_hybrid_lmstudio.py` | ✅ Renamed |
| `generate_rl_topics.py`       | `oneoff_rl_topics_minimax.py`          | ✅ Renamed |
| `generate_svgs.py`            | `svg_generator.py`                     | ✅ Renamed |

### Validation Scripts

| Old Name                  | New Name                         | Status     |
| ------------------------- | -------------------------------- | ---------- |
| `validate_only.py`        | `validator_structure_only.py`    | ✅ Renamed |
| `validate_and_fix.py`     | `validator_with_autofixer.py`    | ✅ Renamed |
| `cse/final_validation.py` | `cse/validator_final_release.py` | ✅ Renamed |
| `cse/validate_svgs.py`    | `cse/svg_validator.py`           | ✅ Renamed |

### Fixer Scripts

| Old Name                | New Name                  | Status     |
| ----------------------- | ------------------------- | ---------- |
| `read_md_fixer.py`      | `fixer_read_md.py`        | ✅ Renamed |
| `fix_external_links.py` | `fixer_external_links.py` | ✅ Renamed |
| `fix_fake_citations.py` | `fixer_fake_citations.py` | ✅ Renamed |
| `cse_parallel_fix.py`   | `fixer_cse_parallel.py`   | ✅ Renamed |
| `cse_nonstop_fix.py`    | `fixer_cse_nonstop.py`    | ✅ Renamed |
| `cse_deepseek_fix.py`   | `fixer_cse_deepseek.py`   | ✅ Renamed |
| `cse_svg_fix.py`        | `svg_fixer_cse.py`        | ✅ Renamed |
| `svg_fixers.py`         | `svg_fixer_utils.py`      | ✅ Renamed |

### SVG Scripts

| Old Name                 | New Name                 | Status     |
| ------------------------ | ------------------------ | ---------- |
| `cse/regenerate_svgs.py` | `cse/svg_regenerator.py` | ✅ Renamed |

### Quality Management Scripts

| Old Name                         | New Name                               | Status     |
| -------------------------------- | -------------------------------------- | ---------- |
| `cse/upgrade_topics_to_8plus.py` | `cse/topic_upgrader_parallel_async.py` | ✅ Renamed |
| `cse/rate_topics.py`             | `cse/topic_rater_dual_api.py`          | ✅ Renamed |

### Reporting Scripts

| Old Name                                 | New Name                              | Status     |
| ---------------------------------------- | ------------------------------------- | ---------- |
| `cse/estimate_completion.py`             | `cse/reporter_completion_estimate.py` | ✅ Renamed |
| `cse/generate_syllabus_review_excels.py` | `cse/reporter_syllabus_excel.py`      | ✅ Renamed |

### Utility Scripts

| Old Name                   | New Name                        | Status     |
| -------------------------- | ------------------------------- | ---------- |
| `cse/extract_svg_paths.py` | `cse/util_extract_svg_paths.py` | ✅ Renamed |

---

## ⚠️ CRITICAL FINDING: Missing MiniMax Content Generator

### What Exists:

✅ **NVIDIA Full Content Generator**

- **File:** `content_generator_nvidia.py` (renamed from `nvidia_content_generator.py`)
- **API:** NVIDIA NIM (Llama-3.1-405B)
- **Generates:** ALL 9 files per topic (read.md, purpose.md, summary.md, flashcards.json, mcqs.json, questions.json, memory.json, visual.json, code.json)
- **Mode:** Sequential

✅ **MiniMax Code Generator**

- **File:** `code_generator_minimax_parallel.py` (renamed from `minimax_code_generator.py`)
- **API:** MiniMax M2.5
- **Generates:** ONLY code.json
- **Mode:** Parallel (ThreadPoolExecutor)

### What's MISSING:

❌ **MiniMax Full Content Generator**

- **Expected file:** `content_generator_minimax.py`
- **Would generate:** ALL 9 files per topic
- **Status:** DOES NOT EXIST

---

## 🔧 Recommendations

### Option 1: Create MiniMax Content Generator (Recommended)

Create `content_generator_minimax.py` by adapting `content_generator_nvidia.py`:

- Replace NVIDIA API calls with MiniMax API
- Use parallel execution (like `code_generator_minimax_parallel.py`)
- Support async/await for better performance

### Option 2: Make Existing Generator API-Agnostic

Refactor `content_generator_nvidia.py` to support multiple APIs:

```python
# Usage:
python content_generator_nvidia.py --api nvidia
python content_generator_nvidia.py --api minimax
```

### Option 3: Use Hybrid Upgrader

The current `cse/topic_upgrader_parallel_async.py` (formerly `upgrade_topics_to_8plus.py`) already supports both APIs:

- Uses Chutes (DeepSeek-R1) + MiniMax M2.5
- Parallel async execution
- Can upgrade existing topics to 8+ quality

---

## 📋 File Naming Convention (Applied)

**Pattern:** `<category>_<action>_<modifier>.py`

**Categories:**

- `content_generator_*` - Full 9-file content generation
- `code_generator_*` - Code examples only
- `topic_upgrader_*` / `topic_rater_*` - Quality management
- `validator_*` - Structure/content validation
- `fixer_*` - Auto-repair tools
- `svg_generator_*` / `svg_validator_*` / `svg_fixer_*` - Visual content
- `reporter_*` - Analytics and reports
- `util_*` - Utility scripts
- `oneoff_*` - One-time/special purpose scripts

**Modifiers:**

- `_nvidia` - Uses NVIDIA NIM API
- `_minimax` - Uses MiniMax API
- `_parallel` - Uses parallel execution
- `_async` - Uses async/await
- `_dual_api` - Uses multiple APIs
- `_legacy` - Old/deprecated version
- `_hybrid` - Mixed approach

---

## 📊 Summary Statistics

- **Total files renamed:** 25
- **Content generators:** 7 (1 missing for MiniMax)
- **Validators:** 4
- **Fixers:** 8
- **SVG tools:** 3
- **Quality tools:** 2
- **Reporters:** 2
- **Utilities:** 1

**Git command to commit renames:**

```bash
git commit -m "Refactor: Standardize script naming convention

- Rename 25 scripts to follow <category>_<action>_<modifier>.py pattern
- Improve discoverability and clarity
- Identify missing minimax_content_generator.py
- See RENAME_SUMMARY.md for full details"
```
