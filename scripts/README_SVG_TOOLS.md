# SVG Tools Documentation

This folder contains all SVG generation and fixing tools for content packs.

## Installation

To install the `fix_svg` command globally:

```bash
./install_fix_svg.sh
source ~/.zshrc  # or ~/.bashrc
```

## Tools

### 1. minimax-fix-svg.sh

**Main SVG quality fixer using MiniMax AI**

- Uses MiniMax M2.5 model for high-quality SVG generation
- Reads topic content (read.md, purpose.md, summary.md)
- Validates output against spec requirements
- Auto-retries on validation failures (up to 2 retries)
- Requires: `MINIMAX_API_KEY` environment variable

**Usage:**

```bash
fix_svg /path/to/topic/directory
fix_svg /path/to/topic/assets/diagram.svg
fix_svg ./topics/deadlock-avoidance
```

**Features:**

- 5-7 step diagrams with TTS narration
- Viewbox validation (800x600)
- Narration word count checks (20-35 words per step)
- Layout containment validation
- Overflow detection

### 2. svg_fixer_cse.py

**Parallel SVG quality fixer using NVIDIA models**

- Uses 5 fast NVIDIA models (100B+ parameters) in parallel
- Processes entire CSE semester directories
- Creates high-quality TTS-compatible diagrams
- Auto-commits changes to git

**Usage:**

```bash
python3 svg_fixer_cse.py
```

**Models used:**

- Mistral Large 3 (675B)
- Llama 3.1 (405B)
- Colosseum (355B)
- Nemotron Ultra (253B)
- Devstral 2 (123B)

### 3. fix_svg_issues.py

**Auto-fix common SVG structural issues**

Fixes:

- HTML elements in SVG (<br>, <div>, etc.)
- XML escaping issues
- Duplicate attributes
- Excess narration groups (reduces 7+ to 5)

**Usage:**

```bash
python3 fix_svg_issues.py
```

### 4. fix_svg_viewbox.py

**Fix viewBox and dimension issues**

- Standardizes viewBox to "0 0 800 600"
- Removes fixed width/height attributes
- Ensures proper SVG structure

**Usage:**

```bash
python3 fix_svg_viewbox.py
```

### 5. svg_fixer_utils.py

**Shared utility functions**

Provides common validation and fixing functions used by other tools:

- SVG validation
- Narration extraction
- Layout analysis
- Content parsing

## Workflow

### For single topic:

```bash
fix_svg /path/to/topic
```

### For bulk fixes:

1. Use `svg_fixer_cse.py` for parallel processing across semesters
2. Use `fix_svg_issues.py` to clean up common issues
3. Use `fix_svg_viewbox.py` to standardize dimensions
4. Use `minimax-fix-svg.sh` for individual quality improvements

## SVG Specification

All SVGs must follow:

- viewBox="0 0 800 600"
- Background: `<rect width="800" height="600" fill="#f8f9fa"/>`
- 5-7 steps as `<g class="step" id="stepN" data-narration="...">`
- Step IDs: step0, step1, step2... (0-indexed)
- Narration: 20-35 words per step, TTS-friendly
- No fixed width/height on root <svg>
- All content within viewBox bounds (max y=588)

## Environment Variables

```bash
export MINIMAX_API_KEY="your-key-here"
export NVIDIA_API_KEY="your-key-here"  # for svg_fixer_cse.py
```

Add to ~/.zshrc for persistence:

```bash
echo 'export MINIMAX_API_KEY="your-key-here"' >> ~/.zshrc
source ~/.zshrc
```
