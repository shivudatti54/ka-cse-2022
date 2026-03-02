# Topic Content Upgrade Script

## Overview

The `upgrade_topics_to_8plus.py` script upgrades topic content to 8+ rating using two AI models in parallel:

- **Chutes** (DeepSeek-R1-TEE)
- **MiniMax** (MiniMax-M2.5)

## Key Features

### ✅ Fixed Issues

1. **All files generated**: Not just JSON, but ALL topic files (read.md, purpose.md, mcqs.json, flashcards.json, questions.json, memory.json, visual.json, code.json, summary.md, full.md, and SVG)
2. **Real-time status**: Live progress updates showing START, DONE, FAIL, WRITE for each topic with timestamps
3. **True parallel processing**: Batch-size N means N unique topics to MiniMax and N different topics to Chutes simultaneously

### 📊 Parallel Processing Logic

**Example with `--batch-size 5`:**

- Round 1: Topics 1-5 → Chutes, Topics 6-10 → MiniMax (parallel)
- Round 2: Topics 11-15 → Chutes, Topics 16-20 → MiniMax (parallel)
- Total: 10 topics processed per round

**Example with `--minimax-only --batch-size 25`:**

- Round 1: Topics 1-25 → MiniMax
- Round 2: Topics 26-50 → MiniMax
- Total: 25 topics processed per round

## Usage Examples

### Basic Usage (Both APIs)

```bash
python3 upgrade_topics_to_8plus.py sem4-topic-paths.txt --batch-size 5
```

- Processes 10 topics per round (5 to each API in parallel)

### MiniMax Only (High Speed)

```bash
python3 upgrade_topics_to_8plus.py sem4-topic-paths.txt --minimax-only --batch-size 25
```

- Processes 25 topics per round using only MiniMax
- Faster for large batches

### Chutes Only (DeepSeek R1)

```bash
python3 upgrade_topics_to_8plus.py sem4-topic-paths.txt --chutes-only --batch-size 10
```

- Processes 10 topics per round using only Chutes

### Dry Run (Test Mode)

```bash
python3 upgrade_topics_to_8plus.py sem4-topic-paths.txt --dry-run --batch-size 5
```

- Shows what would be done without writing files

## Output Format

### Real-time Status Messages

```
──────────────────────────────────────────────────────────────────────────────────────────────────
 ROUND 1/35
──────────────────────────────────────────────────────────────────────────────────────────────────
 [14:32:15] START #1 analysis-framework → CHUTES
 [14:32:15] START #6 binary-tree-traversals → MINIMAX
 [14:32:18] DONE #1 analysis-framework → CHUTES (3.2s) 10 files
 [14:32:19] WRITE analysis-framework → CHUTES (4 md, 6 json, 0 svg)
 [14:32:21] DONE #6 binary-tree-traversals → MINIMAX (6.1s) 10 files
 [14:32:21] WRITE binary-tree-traversals → MINIMAX (4 md, 6 json, 0 svg)
```

### Final Summary

```
====================================================================================================
 COMPLETED
 Time: 1847s | Topics: 348 | Errors: 2
 Files written: 1392 markdown, 2088 JSON, 0 SVG
====================================================================================================
```

## Files Generated Per Topic

### Markdown Files (4)

- `read.md` - Main learning content with sections, examples, exam tips
- `purpose.md` - Why this topic matters
- `summary.md` - 1-page concise summary
- `full.md` - Comprehensive detailed coverage

### JSON Files (6)

- `mcqs.json` - Multiple choice questions (minimum 10)
- `flashcards.json` - Flashcards for memorization (minimum 15)
- `questions.json` - Practice questions (minimum 8)
- `memory.json` - Mnemonics and memory techniques
- `visual.json` - Diagram descriptions and visual aids
- `code.json` - Code examples and implementations

### SVG (Optional)

- `assets/{topic-name}.svg` - Educational diagram if needed

## API Configuration

### Environment Variables (Optional)

```bash
export CHUTES_BASE_URL="https://llm.chutes.ai/v1/chat/completions"
export CHUTES_API_KEY="your-key-here"
export CHUTES_MODEL="deepseek-ai/DeepSeek-R1-TEE"

export MINIMAX_BASE_URL="https://api.minimax.io/v1/chat/completions"
export MINIMAX_API_KEY="your-key-here"
export MINIMAX_MODEL="MiniMax-M2.5"
```

### Default Settings

- **Timeout**: 300 seconds per request
- **Max Tokens**: 32,768 per response
- **Temperature**: 0.2 (focused, consistent output)
- **Semaphore**: 20 concurrent requests
- **TCP Connections**: 40 max

## Command Line Options

| Option           | Description                           | Default |
| ---------------- | ------------------------------------- | ------- |
| `paths_file`     | Text file with topic paths (required) | -       |
| `--dry-run`      | Test mode, don't write files          | False   |
| `--batch-size N` | Topics per API per round              | 5       |
| `--chutes-only`  | Use only Chutes (DeepSeek)            | Both    |
| `--minimax-only` | Use only MiniMax                      | Both    |

## Performance Tips

### For Maximum Speed

```bash
python3 upgrade_topics_to_8plus.py sem4-topic-paths.txt --minimax-only --batch-size 25
```

- MiniMax is generally faster
- Larger batch sizes = fewer rounds
- Single API = less coordination overhead

### For Best Quality

```bash
python3 upgrade_topics_to_8plus.py sem4-topic-paths.txt --batch-size 5
```

- Both models provide diverse perspectives
- Smaller batches = more focused attention per topic

### For Testing

```bash
python3 upgrade_topics_to_8plus.py test-topics.txt --dry-run --batch-size 2
```

- Dry run mode to verify without changes
- Small batch size for quick feedback

## Error Handling

### Common Errors

- **Timeout**: Request took > 300 seconds
- **HTTP 4xx/5xx**: API error (check keys, rate limits)
- **Invalid JSON**: Model response not properly formatted
- **Empty response**: Model returned no content

### Error Display

```
 [14:35:22] FAIL #23 hash-tables → CHUTES (301.0s) TIMEOUT
```

## Requirements

```bash
pip install aiohttp
```

## Example Workflow

```bash
# 1. Generate topic paths
find sem-4 -type d -name "topics" -exec find {} -mindepth 1 -maxdepth 1 -type d \; > sem4-topic-paths.txt

# 2. Test with small batch
head -10 sem4-topic-paths.txt > test-topics.txt
python3 upgrade_topics_to_8plus.py test-topics.txt --dry-run --batch-size 2

# 3. Run for real (recommended: start with one semester)
python3 upgrade_topics_to_8plus.py sem4-topic-paths.txt --batch-size 5

# 4. Or go fast with MiniMax only
python3 upgrade_topics_to_8plus.py sem4-topic-paths.txt --minimax-only --batch-size 25
```

## Monitoring Progress

The script provides real-time updates:

1. **START** - Topic sent to API
2. **DONE** - API response received (shows time + file count)
3. **WRITE** - Files written to disk (shows breakdown)
4. **FAIL** - Error occurred (shows reason)

Watch the output to monitor:

- Response times per topic
- Success/failure rate
- File generation counts
- Overall progress through rounds
