# Scripts Quick Reference

**Last Updated:** 2026-02-15

---

## 🎯 Quick Lookup

### "I want to generate content for topics..."

| Task                              | Script                                 | Command                                                                        |
| --------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------ |
| Generate ALL 9 files (NVIDIA)     | `content_generator_nvidia.py`          | `python3 content_generator_nvidia.py --sem 5`                                  |
| Generate ALL 9 files (MiniMax)    | ❌ **MISSING**                         | N/A - Needs to be created                                                      |
| Generate ONLY code.json (NVIDIA)  | `code_generator_nvidia.py`             | `python3 code_generator_nvidia.py`                                             |
| Generate ONLY code.json (MiniMax) | `code_generator_minimax_parallel.py`   | `python3 code_generator_minimax_parallel.py 10`                                |
| Upgrade low-rated topics to 8+    | `cse/topic_upgrader_parallel_async.py` | `python3 topic_upgrader_parallel_async.py sem4-paths.txt --batch-size 2 --log` |

### "I want to validate/fix content..."

| Task                     | Script                           | Command                               |
| ------------------------ | -------------------------------- | ------------------------------------- |
| Validate structure only  | `validator_structure_only.py`    | `python3 validator_structure_only.py` |
| Validate + auto-fix      | `validator_with_autofixer.py`    | `python3 validator_with_autofixer.py` |
| Final release validation | `cse/validator_final_release.py` | `python3 validator_final_release.py`  |
| Fix read.md formatting   | `fixer_read_md.py`               | `python3 fixer_read_md.py`            |
| Fix external links       | `fixer_external_links.py`        | `python3 fixer_external_links.py`     |
| Fix fake citations       | `fixer_fake_citations.py`        | `python3 fixer_fake_citations.py`     |

### "I want to work with SVGs..."

| Task                    | Script                   | Command                      |
| ----------------------- | ------------------------ | ---------------------------- |
| Generate SVG diagrams   | `svg_generator.py`       | `python3 svg_generator.py`   |
| Validate SVGs           | `cse/svg_validator.py`   | `python3 svg_validator.py`   |
| Regenerate invalid SVGs | `cse/svg_regenerator.py` | `python3 svg_regenerator.py` |
| Fix SVG issues          | `svg_fixer_cse.py`       | `python3 svg_fixer_cse.py`   |

### "I want reports and analytics..."

| Task                    | Script                                | Command                                          |
| ----------------------- | ------------------------------------- | ------------------------------------------------ |
| Rate topic quality      | `cse/topic_rater_dual_api.py`         | `python3 topic_rater_dual_api.py sem4-paths.txt` |
| Estimate completion %   | `cse/reporter_completion_estimate.py` | `python3 reporter_completion_estimate.py`        |
| Generate syllabus Excel | `cse/reporter_syllabus_excel.py`      | `python3 reporter_syllabus_excel.py`             |

---

## 📚 Detailed Script Descriptions

### Content Generators

#### `content_generator_nvidia.py`

**Purpose:** Generate ALL 9 content files for topics using NVIDIA API
**API:** NVIDIA NIM (Llama-3.1-405B)
**Files Generated:** read.md, purpose.md, summary.md, flashcards.json, mcqs.json, questions.json, memory.json, visual.json, code.json
**Mode:** Sequential (3-5 min per topic)
**Usage:**

```bash
export NVIDIA_API_KEY="nvapi-..."
python3 content_generator_nvidia.py                 # all semesters
python3 content_generator_nvidia.py --sem 5         # only sem-5
python3 content_generator_nvidia.py --topic dvr     # single topic
python3 content_generator_nvidia.py --resume        # skip completed
```

#### ❌ `content_generator_minimax.py` (MISSING)

**Status:** Does not exist (needs to be created)
**Expected Purpose:** Generate ALL 9 files using MiniMax M2.5 API
**Recommendation:** Create by adapting `content_generator_nvidia.py`

#### `code_generator_nvidia.py`

**Purpose:** Generate ONLY code.json (algorithms, pseudocode, Python/C/Java)
**API:** NVIDIA NIM (Llama-3.1-405B)
**Files Generated:** code.json only
**Usage:**

```bash
export NVIDIA_API_KEY="nvapi-..."
python3 code_generator_nvidia.py                    # uses svg_path.txt
python3 code_generator_nvidia.py custom_list.txt    # custom paths
```

#### `code_generator_minimax_parallel.py`

**Purpose:** Generate ONLY code.json using MiniMax (parallelized)
**API:** MiniMax M2.5
**Files Generated:** code.json only
**Mode:** Parallel (ThreadPoolExecutor)
**Usage:**

```bash
python3 code_generator_minimax_parallel.py                      # sequential
python3 code_generator_minimax_parallel.py 10                   # 10 parallel workers
python3 code_generator_minimax_parallel.py custom_list.txt 10   # custom + parallel
```

#### `content_generator_legacy_nvidia.py`

**Purpose:** OLD content generator (deprecated, kept for reference)
**API:** NVIDIA (DeepSeek-V3.1)
**Status:** Legacy - use `content_generator_nvidia.py` instead

#### `content_generator_hybrid_lmstudio.py`

**Purpose:** Hybrid approach - LM Studio for text, NVIDIA for structured data
**APIs:** LM Studio (local) + NVIDIA (cloud)
**Use Case:** Resource-constrained environments (8GB RAM)

---

### Quality Management

#### `cse/topic_upgrader_parallel_async.py`

**Purpose:** Upgrade low-rated topics to 8+ quality rating
**APIs:** Chutes (DeepSeek-R1-TEE) + MiniMax (M2.5)
**Mode:** Parallel async (9 API calls per topic)
**Performance:** 3-8 minutes per batch (with optimizations)
**Usage:**

```bash
python3 topic_upgrader_parallel_async.py sem4-paths.txt --batch-size 2 --resume
python3 topic_upgrader_parallel_async.py sem4-paths.txt --log              # with logging
python3 topic_upgrader_parallel_async.py sem4-paths.txt --minimax-only     # single API
```

#### `cse/topic_rater_dual_api.py`

**Purpose:** Rate topic quality on 1-10 scale using dual APIs
**APIs:** Chutes (DeepSeek-R1) + MiniMax (M2.5)
**Output:** JSON rating file + HTML report
**Usage:**

```bash
python3 topic_rater_dual_api.py topic-paths.txt            # rate topics
python3 topic_rater_dual_api.py --report-only ratings.json # HTML only
```

---

### Validators

#### `validator_structure_only.py`

**Purpose:** Validate topic structure (files, JSON syntax, required fields)
**Actions:** Read-only validation, no fixes
**Reports:** Lists all issues found

#### `validator_with_autofixer.py`

**Purpose:** Validate + automatically fix common issues
**Fixes:** JSON syntax, missing fields, file encoding, etc.
**Safer:** Creates backups before fixing

#### `cse/validator_final_release.py`

**Purpose:** Final quality check before app release
**Checks:** Completeness, quality ratings, SVG validity, etc.

#### `cse/svg_validator.py`

**Purpose:** Validate SVG files (syntax, viewBox, data-topic-id)
**Checks:** XML validity, required attributes, TTS compatibility

---

### Fixers

#### `fixer_read_md.py`

**Purpose:** Fix read.md formatting issues
**Fixes:** Markdown syntax, heading structure, code blocks

#### `fixer_external_links.py`

**Purpose:** Remove or fix external links in content
**Reason:** App works offline, external links break without internet

#### `fixer_fake_citations.py`

**Purpose:** Remove AI-generated fake citations and references
**Detection:** Recognizes common LLM hallucinated citation patterns

#### `fixer_cse_parallel.py`

**Purpose:** Parallel batch fixer for CSE content
**Mode:** Multi-threaded for speed

#### `fixer_cse_nonstop.py`

**Purpose:** Non-stop batch fixer (continues on errors)
**Use Case:** Large batches where some topics might fail

#### `fixer_cse_deepseek.py`

**Purpose:** Fix CSE content using DeepSeek API
**API:** DeepSeek AI

#### `svg_fixer_cse.py`

**Purpose:** Fix SVG-specific issues in CSE content
**Fixes:** viewBox, data-topic-id, invalid syntax

#### `svg_fixer_utils.py`

**Purpose:** Utility functions for SVG fixing
**Use:** Imported by other SVG fixers

---

### SVG Tools

#### `svg_generator.py`

**Purpose:** Generate SVG diagrams from topic content
**Output:** visual.json with SVG diagram descriptions

#### `cse/svg_regenerator.py`

**Purpose:** Regenerate invalid or broken SVG files
**Checks:** Validates before regeneration

---

### Reporters

#### `cse/reporter_completion_estimate.py`

**Purpose:** Calculate % completion of content pack
**Output:** Statistics on completed vs. missing content

#### `cse/reporter_syllabus_excel.py`

**Purpose:** Generate Excel files for syllabus review
**Output:** .xlsx files with topic mapping

---

### Utilities

#### `cse/util_extract_svg_paths.py`

**Purpose:** Extract paths to all SVG files
**Output:** Text file with SVG file paths

#### `oneoff_rl_topics_minimax.py`

**Purpose:** One-time script for generating RL topics
**API:** MiniMax M2.5
**Use Case:** Specific to Module 5 Reinforcement Learning

---

## 🔑 Key Takeaways

### Most Common Workflows

**1. Generate new content for a semester:**

```bash
# Option A: NVIDIA (high quality, slower)
python3 content_generator_nvidia.py --sem 6 --resume

# Option B: Code only (MiniMax, parallel, faster)
python3 code_generator_minimax_parallel.py sem6-paths.txt 10
```

**2. Upgrade low-rated topics:**

```bash
# Extract low-rated topics first
python3 cse/topic_rater_dual_api.py all-topics.txt

# Then upgrade them
python3 cse/topic_upgrader_parallel_async.py low-rated-paths.txt --batch-size 2 --log --resume
```

**3. Validate before release:**

```bash
# Step 1: Validate structure
python3 validator_structure_only.py

# Step 2: Auto-fix issues
python3 validator_with_autofixer.py

# Step 3: Final check
python3 cse/validator_final_release.py
```

---

## ⚠️ Important Notes

1. **Missing Script:** There's NO MiniMax equivalent for full content generation (`content_generator_minimax.py` doesn't exist)
2. **API Keys:** NVIDIA scripts require `NVIDIA_API_KEY` environment variable
3. **Resume Mode:** Most generators support `--resume` to skip completed topics
4. **Logging:** Use `--log` flag for real-time progress monitoring
5. **Parallel Execution:** MiniMax code generator is already parallelized, NVIDIA is sequential
