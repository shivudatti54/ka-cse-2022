# 2022 Scheme Scripts Inventory

**Date:** 2026-02-15
**Location:** `/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/-2022-scheme/`

---

## 📋 Content Generation Scripts

### Full Content Generators (9 files: read.md, purpose.md, summary.md, flashcards.json, mcqs.json, questions.json, memory.json, visual.json, code.json)

| Current Name                  | API                | Model          | Status             | Recommended Name               |
| ----------------------------- | ------------------ | -------------- | ------------------ | ------------------------------ |
| `nvidia_content_generator.py` | NVIDIA NIM         | Llama-3.1-405B | ✅ Active          | `content_generator_nvidia.py`  |
| **MISSING**                   | MiniMax            | M2.5           | ❌ Does not exist  | `content_generator_minimax.py` |
| `generate_vtu_content.py`     | NVIDIA             | DeepSeek-V3.1  | ⚠️ Old/legacy      | `content_generator_legacy.py`  |
| `generate_hybrid.py`          | LM Studio + NVIDIA | Mixed          | ⚠️ Hybrid approach | `content_generator_hybrid.py`  |
| `generate_rl_topics.py`       | MiniMax            | M2.5           | 🎯 One-off for RL  | `one_off_rl_topics_minimax.py` |

**Conclusion:**

- ❌ **NO MiniMax equivalent** for full content generation (nvidia_content_generator.py has no minimax counterpart)
- ✅ Recommendation: Create `content_generator_minimax.py` or make nvidia_content_generator.py API-agnostic

---

### Code-Only Generators (code.json only)

| Current Name                | API        | Model          | Parallelization                  | Recommended Name            |
| --------------------------- | ---------- | -------------- | -------------------------------- | --------------------------- |
| `nvidia_code_generator.py`  | NVIDIA NIM | Llama-3.1-405B | Sequential                       | `code_generator_nvidia.py`  |
| `minimax_code_generator.py` | MiniMax    | M2.5           | ✅ Parallel (ThreadPoolExecutor) | `code_generator_minimax.py` |

**Conclusion:** Both APIs have code generators ✅

---

## 🔧 Quality & Upgrade Scripts

### Topic Quality Management

| Current Name                     | API(s)                                | Purpose                                | Recommended Name                   |
| -------------------------------- | ------------------------------------- | -------------------------------------- | ---------------------------------- |
| `cse/upgrade_topics_to_8plus.py` | Chutes (DeepSeek-R1) + MiniMax (M2.5) | Upgrade low-rated topics to 8+ quality | `topic_upgrader_parallel_async.py` |
| `cse/rate_topics.py`             | Chutes + MiniMax                      | Rate topic quality (1-10 scale)        | `topic_rater_dual_api.py`          |

---

## 🛠️ Validation & Fixing Scripts

### Content Validators

| Current Name                         | Purpose                            | Recommended Name               |
| ------------------------------------ | ---------------------------------- | ------------------------------ |
| `validate_only.py`                   | Validate structure only (no fixes) | `validator_structure_only.py`  |
| `validate_and_fix.py`                | Validate + auto-fix issues         | `validator_with_autofixer.py`  |
| `cse/final_validation.py`            | Final quality check before release | `validator_final_release.py`   |
| `cse/sem-5/validate_topics.py`       | Validate sem-5 topics              | `validator_sem5_topics.py`     |
| `cse/sem-5/contextual_validation.py` | Context-aware validation           | `validator_contextual_sem5.py` |

### Content Fixers

| Current Name              | Purpose                        | Recommended Name          |
| ------------------------- | ------------------------------ | ------------------------- |
| `cse_parallel_fix.py`     | Parallel fixer for CSE content | `fixer_cse_parallel.py`   |
| `cse_nonstop_fix.py`      | Non-stop batch fixer for CSE   | `fixer_cse_nonstop.py`    |
| `cse_deepseek_fix.py`     | CSE fixer using DeepSeek API   | `fixer_cse_deepseek.py`   |
| `read_md_fixer.py`        | Fix read.md formatting issues  | `fixer_read_md.py`        |
| `fix_external_links.py`   | Remove/fix external links      | `fixer_external_links.py` |
| `fix_fake_citations.py`   | Remove fake citations          | `fixer_fake_citations.py` |
| `cse/sem-5/fix_topics.py` | Fix sem-5 topic issues         | `fixer_sem5_topics.py`    |

---

## 🎨 SVG & Visual Content Scripts

### SVG Generators

| Current Name                        | Purpose                          | Recommended Name            |
| ----------------------------------- | -------------------------------- | --------------------------- |
| `generate_svgs.py`                  | Generate SVG diagrams            | `svg_generator.py`          |
| `cse/sem-5/generate_tts_svgs.py`    | Generate SVGs with TTS narration | `svg_generator_tts_sem5.py` |
| `ai-ml/sem-6/generate_sem6_svgs.py` | Generate sem-6 SVGs              | `svg_generator_sem6.py`     |
| `cse/regenerate_svgs.py`            | Regenerate invalid SVGs          | `svg_regenerator.py`        |

### SVG Validators & Fixers

| Current Name                           | Purpose                      | Recommended Name            |
| -------------------------------------- | ---------------------------- | --------------------------- |
| `cse/validate_svgs.py`                 | Validate SVG structure       | `svg_validator.py`          |
| `cse_svg_fix.py`                       | Fix CSE SVG issues           | `svg_fixer_cse.py`          |
| `svg_fixers.py`                        | Generic SVG fixing utilities | `svg_fixer_utils.py`        |
| `cse/sem-5/validate_tts_svgs.py`       | Validate TTS-enabled SVGs    | `svg_validator_tts_sem5.py` |
| `cse/sem-5/fix_svg_viewbox.py`         | Fix SVG viewBox issues       | `svg_fixer_viewbox_sem5.py` |
| `cse/sem-5/regenerate_invalid_svgs.py` | Regenerate broken SVGs       | `svg_regenerator_sem5.py`   |
| `cse/sem-5/fix_svg_issues.py`          | Fix various SVG issues       | `svg_fixer_sem5.py`         |

---

## 📊 Reporting & Analysis Scripts

| Current Name                                   | Purpose                             | Recommended Name                      |
| ---------------------------------------------- | ----------------------------------- | ------------------------------------- |
| `cse/estimate_completion.py`                   | Estimate content completion %       | `reporter_completion_estimate.py`     |
| `cse/generate_syllabus_review_excels.py`       | Generate syllabus review Excel      | `reporter_syllabus_excel.py`          |
| `cse/sem-5/contextual_summary.py`              | Generate contextual summary reports | `reporter_contextual_summary_sem5.py` |
| `cse/reports/extract_low_rated_topic_paths.py` | Extract paths of low-rated topics   | `reporter_extract_low_rated.py`       |

---

## 🔍 Utility Scripts

| Current Name                     | Purpose                   | Recommended Name             |
| -------------------------------- | ------------------------- | ---------------------------- |
| `cse/extract_svg_paths.py`       | Extract SVG file paths    | `util_extract_svg_paths.py`  |
| `cse/sem-3/list_read_mds.py`     | List all read.md files    | `util_list_read_mds_sem3.py` |
| `cse/sem-5/add_data_topic_id.py` | Add data-topic-id to SVGs | `util_add_topic_id_sem5.py`  |

---

## ⚠️ Key Findings

### Missing Scripts

1. **❌ NO `minimax_content_generator.py`** - There's NO MiniMax equivalent of nvidia_content_generator.py
   - nvidia_content_generator.py exists (full 9-file generation)
   - minimax_code_generator.py exists (only code.json)
   - **GAP:** No minimax version for full content generation

### Recommended Actions

1. Create `content_generator_minimax.py` by adapting nvidia_content_generator.py
2. Or refactor nvidia_content_generator.py to be API-agnostic (support both NVIDIA and MiniMax)
3. Standardize naming: `<category>_<purpose>_<api/modifier>.py`

---

## 📦 Recommended File Naming Convention

**Pattern:** `<category>_<action>_<modifier>.py`

**Categories:**

- `content_generator` - Full content generation
- `code_generator` - Code examples only
- `topic_upgrader` / `topic_rater` - Quality management
- `validator` - Structure/content validation
- `fixer` - Auto-repair tools
- `svg_generator` / `svg_validator` / `svg_fixer` - Visual content
- `reporter` - Analytics and reports
- `util` - Utility scripts

**Examples:**

- ✅ `content_generator_nvidia.py`
- ✅ `content_generator_minimax.py`
- ✅ `code_generator_nvidia.py`
- ✅ `topic_upgrader_parallel_async.py`
- ✅ `fixer_read_md.py`
- ✅ `svg_generator_tts_sem5.py`
