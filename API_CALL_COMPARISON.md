# API Call Comparison: nvidia_content_generator.py vs topic_upgrader_parallel_async.py

## Key Differences

| Aspect                  | `content_generator_nvidia.py`                                       | `topic_upgrader_parallel_async.py`             |
| ----------------------- | ------------------------------------------------------------------- | ---------------------------------------------- |
| **HTTP Library**        | `urllib.request` (blocking, synchronous)                            | `aiohttp` (async, non-blocking)                |
| **Execution Model**     | Sequential (one at a time)                                          | Parallel async (27 concurrent calls)           |
| **API Calls per Topic** | **2 calls** (batched)                                               | **9 calls** (one per file)                     |
| **Timeout**             | **300 seconds** (5 minutes)                                         | ~~60s~~ → **180 seconds** (3 minutes)          |
| **Socket Read Timeout** | None (relies on total timeout)                                      | ~~30s~~ → **120 seconds**                      |
| **Batching Strategy**   | Smart batching (3 markdown files in 1 call, 6 JSON files in 1 call) | Individual files (9 separate calls)            |
| **Speed per Topic**     | 30-90 seconds (2 sequential calls)                                  | 60-180 seconds (9 parallel calls with retries) |
| **Concurrency**         | 1 topic at a time                                                   | 3 topics at a time (27 API calls)              |
| **APIs Used**           | NVIDIA only                                                         | Chutes (DeepSeek-R1) + MiniMax (M2.5)          |

---

## Detailed Breakdown

### 1. nvidia_content_generator.py (SEQUENTIAL, BATCHED)

**HTTP Implementation:**

```python
import urllib.request

def call_api(api_key, messages):
    payload = json.dumps({
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
        "messages": messages,
    }).encode()

    req = urllib.request.Request(API_URL, data=payload, headers={...})
    resp = urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)  # TIMEOUT = 300s
    return json.loads(resp.read().decode())
```

**Batching Strategy:**

```python
# Call 1: Generate 3 markdown files in ONE API call
def generate_markdown(api_key, ctx):
    # Asks LLM to generate ALL 3 markdown files at once:
    # - read.md
    # - purpose.md
    # - summary.md
    # Returns delimited text: ===READ_MD=== ... ===PURPOSE_MD=== ... ===SUMMARY_MD===
    # Takes 30-50 seconds

# Call 2: Generate 6 JSON files in ONE API call
def generate_assessment(api_key, ctx, read_content):
    # Asks LLM to generate ALL 6 JSON files at once:
    # - flashcards.json
    # - mcqs.json
    # - memory.json
    # - questions.json
    # - visual.json (actually generated locally)
    # - code.json
    # Returns single large JSON object
    # Takes 50-90 seconds
```

**Execution Flow (Per Topic):**

```
Topic 1:
  └─ Call 1 (markdown)  ──── 30-50s ──── write read.md, purpose.md, summary.md
  └─ Call 2 (assessment) ─── 50-90s ──── write flashcards.json, mcqs.json, memory.json, questions.json, code.json

Topic 2:
  └─ Call 1 (markdown)  ──── 30-50s ──── ...
  └─ Call 2 (assessment) ─── 50-90s ──── ...
```

**Total Time for 3 Topics:**

- Sequential: 3 × (30s + 70s) = **~300 seconds (5 minutes)**

---

### 2. topic_upgrader_parallel_async.py (PARALLEL ASYNC)

**HTTP Implementation:**

```python
import aiohttp
import asyncio

async def call_api_for_file(session, api_name, topic_idx, ..., filename, semaphore):
    async with semaphore:  # Limit concurrent calls
        async with session.post(
            api["base_url"],
            headers=headers,
            json=payload,
            timeout=aiohttp.ClientTimeout(
                total=180,      # 3 minutes max (was 60s - too short!)
                connect=15,     # 15s to establish connection
                sock_read=120   # 120s between data chunks (was 30s - caused timeouts!)
            ),
        ) as resp:
            data = await resp.json()
            # Process one file at a time
```

**Individual File Strategy:**

```python
# Call 1: read.md only
# Call 2: purpose.md only
# Call 3: summary.md only
# Call 4: flashcards.json only
# Call 5: mcqs.json only
# Call 6: memory.json only
# Call 7: questions.json only
# Call 8: visual.json only
# Call 9: code.json only

# All 9 calls happen in PARALLEL
```

**Execution Flow (3 Topics Concurrently):**

```
Topic 1: ┬─ read.md       ──┐
         ├─ purpose.md     ──┤
         ├─ summary.md     ──┤
         ├─ flashcards.json─┤
         ├─ mcqs.json      ──┤── All 9 parallel ── 60-180s
         ├─ memory.json    ──┤
         ├─ questions.json ──┤
         ├─ visual.json    ──┤
         └─ code.json      ──┘

Topic 2: [9 parallel calls] ─── Same time as Topic 1
Topic 3: [9 parallel calls] ─── Same time as Topic 1

Semaphore limits to 30 concurrent calls (out of 27 total)
```

**Total Time for 3 Topics:**

- Parallel: **~60-180 seconds** (all 3 topics processed simultaneously)

---

## Why nvidia_content_generator.py Was Working Fine

### Timeout Configuration:

```python
TIMEOUT = 300  # 5 minutes - plenty of time for LLM to generate
```

### Simple urllib Timeout:

```python
urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)
```

- **One timeout value:** 300 seconds total
- **No socket read timeout:** Waits patiently for LLM to finish generating
- **Blocking call:** Waits until response is fully received

### Result:

✅ LLM can take 30-90 seconds to generate content without timing out
✅ Simple, reliable, works consistently

---

## Why topic_upgrader_parallel_async.py Was Failing (Before Fix)

### Original Timeout Configuration:

```python
REQUEST_TIMEOUT = 60  # Too short!
sock_read = 30        # CRITICAL ISSUE: Kills request if no data for 30s
```

### Complex aiohttp Timeout:

```python
timeout=aiohttp.ClientTimeout(
    total=60,       # Max 60s total - not enough for long content!
    connect=15,     # 15s to connect
    sock_read=30    # 30s between chunks - LLM takes 40-90s to generate!
)
```

### What Happened:

1. API call starts
2. LLM starts generating content (takes 40-90 seconds for read.md)
3. **After 30 seconds of silence** → `sock_read` timeout triggers
4. Request cancelled ❌
5. Retry (same thing happens)
6. All files fail except small ones (purpose.md)

### Result:

❌ **All calls timeout at exactly 30 seconds**
❌ Only 1/9 files succeed per topic (purpose.md is small)
❌ Batch takes 63 seconds (30s timeout × 2 attempts)

---

## After Fix: topic_upgrader_parallel_async.py

### New Timeout Configuration:

```python
REQUEST_TIMEOUT = 180  # 3 minutes - matches LLM generation time
sock_read = 120        # 2 minutes - allows time for LLM to think
```

### Expected Behavior:

✅ LLM can take up to 120s before sending first chunk
✅ Total request can take up to 180s
✅ Matches nvidia_content_generator.py speeds (30-90s per call)
✅ 7-9/9 files should succeed per topic

---

## Trade-offs

### nvidia_content_generator.py

**Pros:**

- ✅ Simple, reliable
- ✅ Fewer API calls (2 vs 9 per topic)
- ✅ Batching is efficient
- ✅ Long timeout (300s) accommodates LLMs

**Cons:**

- ❌ Sequential only (1 topic at a time)
- ❌ Slow for large batches (348 topics × 100s = 10 hours)
- ❌ Single API only (NVIDIA)
- ❌ If one file fails, whole batch fails

### topic_upgrader_parallel_async.py

**Pros:**

- ✅ Parallel async (3 topics × 9 files = 27 concurrent calls)
- ✅ Fast for large batches (116 batches × 3 min = ~6 hours)
- ✅ Dual APIs (Chutes + MiniMax for redundancy)
- ✅ Individual file retry (1 file fails, others succeed)
- ✅ Detailed logging

**Cons:**

- ❌ More complex (async, semaphore, timeout tuning)
- ❌ More API calls (9 vs 2 per topic)
- ❌ Timeout tuning required for different APIs

---

## Recommendation

### For Initial Content Generation (Empty Topics):

Use **`content_generator_nvidia.py`**

- Simpler, more reliable
- Batched API calls (fewer, more efficient)
- Good for 50-100 topics

### For Upgrading Existing Content (Quality Improvement):

Use **`topic_upgrader_parallel_async.py`** (with fixed timeouts)

- Much faster for large batches (348 topics)
- Dual API support (better coverage)
- Individual file retry (partial success better than total failure)
- Good for 200+ topics

---

## Summary

| Metric                 | nvidia_content_generator.py | topic_upgrader_parallel_async.py |
| ---------------------- | --------------------------- | -------------------------------- |
| **Library**            | urllib (sync)               | aiohttp (async)                  |
| **API calls/topic**    | 2 (batched)                 | 9 (individual)                   |
| **Timeout**            | 300s (simple)               | 180s total, 120s sock_read       |
| **Concurrency**        | 1 topic                     | 3 topics (27 API calls)          |
| **Speed (3 topics)**   | ~300s (5 min)               | ~180s (3 min)                    |
| **Speed (348 topics)** | ~10 hours                   | ~6 hours                         |
| **APIs**               | NVIDIA only                 | Chutes + MiniMax                 |
| **Complexity**         | Low                         | High                             |
| **Reliability**        | Very high                   | High (after timeout fix)         |
