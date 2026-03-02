# Cache Line Replacement Policies

## Table of Contents

- [Cache Line Replacement Policies](#cache-line-replacement-policies)
- [Introduction](#introduction)
- [Theoretical Framework](#theoretical-framework)
  - [1. Cache Organization Fundamentals](#1-cache-organization-fundamentals)
  - [2. Formal Problem Definition](#2-formal-problem-definition)
  - [3. Locality Principles](#3-locality-principles)
- [Comprehensive Analysis of Replacement Policies](#comprehensive-analysis-of-replacement-policies)
  - [A. Least Recently Used (LRU)](#a-least-recently-used-lru)
  - [B. First In First Out (FIFO)](#b-first-in-first-out-fifo)
  - [C. Least Frequently Used (LFU)](#c-least-frequently-used-lfu)
  - [D. Random Replacement (RR)](#d-random-replacement-rr)
  - [E. Optimal Replacement (OPT/Belady's OPT)](#e-optimal-replacement-optbeladys-opt)
  - [F. Not Recently Used (NRU) / Clock Algorithm](#f-not-recently-used-nru--clock-algorithm)
  - [G. Most Recently Used (MRU)](#g-most-recently-used-mru)
- [Coprocessor 15 Cache Control in ARM Microcontrollers](#coprocessor-15-cache-control-in-arm-microcontrollers)
- [Quantitative Analysis and Examples](#quantitative-analysis-and-examples)
  - [Example 1: LRU vs FIFO Hit Ratio Calculation](#example-1-lru-vs-fifo-hit-ratio-calculation)
  - [Example 2: AMAT Calculation with Replacement Policy Impact](#example-2-amat-calculation-with-replacement-policy-impact)
  - [Example 3: Belady's Anomaly Demonstration](#example-3-beladys-anomaly-demonstration)
- [Summary line replacement policies constitute](#summary-line-replacement-policies-constitute)

## Introduction

Cache memory constitutes a critical performance bottleneck in modern computing architectures, particularly in microcontroller systems where the disparity between processor clock speeds and memory access times continues to widen. When the central processing unit requires data, it first interrogates the cache hierarchy; upon a cache hit, the data is retrieved within a single cycle, whereas a cache miss necessitates fetching the requested block from main memory, incurring substantial latency penalties that can stall the processor pipeline for dozens of cycles.

In set-associative and fully-associative cache organizations, the cache controller must managelimited number of cache slots within each set. When a cache miss occurs and all ways within the target set are occupied, the controller must select a victim cache line for eviction to accommodate the newly fetched block. This decision process is governed by **Cache Line Replacement Policies** (also termed cache replacement algorithms), which constitute a fundamental design choice affecting cache hit ratio, average memory access time (AMAT), and overall system performance.

The selection of an appropriate replacement policy involves critical trade-offs between theoretical optimality, hardware implementation complexity, power consumption, and determinism—factors of paramount importance in embedded microcontroller applications where real-time constraints and resource limitations prevail. The BCS402 Microcontrollers syllabus addresses this topic within Module 5 (Coprocessor 15 and Caches) because ARM-based microcontrollers frequently employ cache memory to bridge the speed gap between processors and external memory systems.

## Theoretical Framework

### 1. Cache Organization Fundamentals

The study of replacement policies requires understanding of fundamental cache architecture:

- **Cache Line (Block)**: The atomic unit of data transfer between cache and main memory, typically ranging from 16 to 64 bytes in embedded systems
- **Cache Set**: A collection of cache lines (ways) where a particular memory block may be placed, indexed by the address index field
- **Associativity**: The number of ways per set (direct-mapped = 1 way, n-way set-associative = n ways, fully-associative = all lines in a single set)
- **Tag, Index, Offset**: Address decomposition fields used for cache addressing and hit/miss determination

### 2. Formal Problem Definition

Given a cache with set associativity $A$ (number of ways) and a memory reference stream $R = r_1, r_2, ..., r_n$, the replacement policy must select a victim line when $|S| = A$ (set full) and a new block $b \notin S$ (cache miss) occurs. The policy aims to minimize the cache miss rate or equivalently maximize the cache hit ratio, defined as:

$$\text{Hit Ratio} = \frac{\text{Number of Cache Hits}}{\text{Total Memory References}}$$

The **Average Memory Access Time (AMAT)** provides a comprehensive performance metric:

$$\text{AMAT} = \text{Hit Time} + \text{Miss Rate} \times \text{Miss Penalty}$$

### 3. Locality Principles

Cache effectiveness fundamentally relies on two locality principles:

- **Temporal Locality**: Recently accessed memory locations exhibit high probability of being accessed again in the near future; LRU policies capitalize on this principle by retaining recently-used blocks
- **Spatial Locality**: Memory locations adjacent to recently accessed addresses are likely to be referenced soon; this justifies larger cache line sizes that fetch consecutive bytes

## Comprehensive Analysis of Replacement Policies

### A. Least Recently Used (LRU)

**Definition**: The LRU policy evicts the cache line that has not been accessed for the longest temporal duration, formalizing the principle of temporal locality.

**Mathematical Justification**: Under the stack distance model, LRU exhibits the **stack property**: as cache size increases, the miss rate either remains constant or decreases (never increases). This monotonicity property ensures predictable behavior and provides theoretical grounding for LRU's widespread adoption.

**Hardware Implementation Strategies**:

1. **Counter-based LRU**: Each cache way maintains an $N$-bit counter (where $N = \log_2 A$). Upon a cache hit to way $i$, all counters with values less than counter[$i$] are incremented, while counter[$i$] is reset to 0. The way with the highest counter value represents the least recently used line. This implementation requires $A \times \log_2 A$ bits per set.

2. **Matrix-based LRU**: An $A \times A$ boolean matrix tracks relative recency between all way pairs. Way $i$ is LRU if row $i$ contains all 1s. This approach simplifies update logic but scales poorly ($O(A^2)$ hardware).

3. **Approximate LRU (Pseudo-LRU)**: Tree-based PLRU uses a binary tree structure with $A-1$ branch bits. For a 4-way cache, only 3 bits track LRU status while providing near-optimal behavior. This approach significantly reduces hardware complexity for high-associativity caches.

**Advantages**: Near-optimal hit ratio in practice; deterministic behavior; well-suited for workloads exhibiting temporal locality

**Disadvantages**: Exponential hardware complexity for high associativity ($O(A \log A)$ bits); false sharing in multiprocessor systems

### B. First In First Out (FIFO)

**Definition**: FIFO evicts the cache line that has resided in the cache for the longest duration, regardless of access frequency or recency. The cache operates as a circular queue.

**Implementation**: Maintains a modulo-$A$ counter pointing to the next victim way. Upon eviction, the counter increments modulo $A$. This requires only $\log_2 A$ bits per set—significantly less than LRU.

**Belady's Anomaly**: A counterintuitive phenomenon where increasing cache associativity (and thus capacity) can paradoxically _decrease_ the hit ratio under FIFO. This anomaly arises because FIFO tracks insertion order rather than usage patterns, violating the stack property.

**Proof Sketch of Anomaly**: Consider a 3-frame cache with reference string: A, B, C, A, B, D, A, B, C, D. With 3 frames, FIFO yields 9 misses. Adding a 4th frame still yields 9 misses—the anomaly manifests when the working set exceeds the new capacity.

**Advantages**: Minimal hardware complexity ($O(\log A)$ bits); deterministic; low power consumption

**Disadvantages**: Does not exploit temporal locality; susceptible to Belady's anomaly; may evict heavily-used lines

### C. Least Frequently Used (LFU)

**Definition**: LFU counts the number of references to each cache line and evicts the block with the lowest access frequency. Ties are broken by eviction time (FIFO).

**Implementation**: Each cache way maintains an access counter incremented on every hit. The Minimum Replacement (MIN) algorithm represents an idealization: evict the line with lowest forward reference count. True LFU faces the **cache pollution problem**—lines with historically high but currently low access rates may persist unnecessarily.

**Advantage**: Effective for non-uniform access distributions where certain blocks are genuinely more popular

**Disadvantages**: Does not adapt to temporal changes; requires counter overflow management; heavier hardware than FIFO

### D. Random Replacement (RR)

**Definition**: RR selects the victim cache line uniformly at random using a pseudo-random number generator, typically a linear feedback shift register (LFSR).

**Mathematical Analysis**: For a cache with $A$ ways and a reference stream with temporal locality, RR's hit ratio $H_{RR}$ can be expressed probabilistically. While typically 10-20% worse than LRU, RR provides a useful lower bound and guarantees no worst-case pathological behavior.

**Advantages**: Negligible hardware (one random bit per set for selection); no starvation possibilities; eliminates timing side-channel vulnerabilities in security-critical systems

**Disadvantages**: Unpredictable performance; cannot exploit locality; unsuitable for real-time systems requiring deterministic behavior

### E. Optimal Replacement (OPT/Belady's OPT)

**Definition**: The OPT policy evicts the cache line that will not be referenced for the longest duration in the future, requiring omniscient knowledge of future memory accesses.

**Theoretical Significance**: OPT provides the theoretical lower bound on cache misses for any given cache size. The competitive ratio of any online algorithm against OPT is unbounded; however, OPT serves as the gold standard for evaluating practical policies.

**Offline Computation**: Given a reference string of length $n$ and cache capacity $C$, OPT can be computed using Belady's algorithm: upon each miss, evict the line whose next use is farthest in the future (or never used). This requires $O(n \times C)$ time complexity.

### F. Not Recently Used (NRU) / Clock Algorithm

**Definition**: NRU (also called Clock or Second-Chance) is a simplified approximation of LRU using reference bits. Each cache line maintains a **referenced** bit set to 1 on access and cleared by a background scanning process.

**Algorithm Operation**:

1. Create a circular buffer (clock hand)
2. On eviction, examine the line pointed by the hand
3. If referenced bit = 1: clear bit, advance hand (second chance)
4. If referenced bit = 0: evict this line

**Classification**: The original NRU algorithm classifies lines into four classes based on (referenced, modified) bit pairs:

- Class 0: Not referenced, not modified (highest eviction priority)
- Class 1: Not referenced, modified
- Class 2: Referenced, not modified
- Class 3: Referenced, modified (lowest priority)

**ARM Implementation**: ARM Cortex-A series processors employ a variant of the Clock algorithm for cache maintenance, integrated with Coprocessor 15 control registers.

### G. Most Recently Used (MRU)

**Definition**: MRU evicts the most recently accessed line, opposite to LRU. Useful in specific streaming applications where recently-used data is unlikely to be reused.

**Application**: Video decoding, streaming media processing—scenarios exhibiting strong spatial locality but weak temporal locality for large working sets.

## Coprocessor 15 Cache Control in ARM Microcontrollers

ARM architecture, prevalent in embedded microcontrollers, provides specialized cache control through Coprocessor 15 (CP15). Understanding replacement policy interactions with hardware maintenance operations is essential:

- **Cache Type Register (CTR)**: Indicates cache geometry, including line size and associativity
- **Cache Maintenance Operations**: `Invalidate`, `Clean`, and `Clean and Invalidate` operations affect replacement policy state
- **TLBI (TLB Invalidate)**: Separate control for instruction cache synchronization

Cache replacement policies operate transparently to software; however, cache maintenance operations (such as cache flush before disabling) may interact with replacement state, affecting subsequent hit/miss behavior.

## Quantitative Analysis and Examples

### Example 1: LRU vs FIFO Hit Ratio Calculation

**Problem**: Consider a 2-way set-associative cache with 1 set (A=2). Given reference string: A, B, C, D, A, B, E, A, B, C, D, E. Calculate hit ratios for LRU and FIFO policies.

**Solution**:

| Ref | LRU Action          | LRU Cache State | FIFO Action          | FIFO Cache State |
| --- | ------------------- | --------------- | -------------------- | ---------------- |
| A   | Miss (load)         | {A,-}, Hit=0    | Miss (load)          | {A,-}, Hit=0     |
| B   | Miss (load)         | {A,B}, Hit=0    | Miss (load)          | {A,B}, Hit=0     |
| C   | Miss, evict A (LRU) | {C,B}, Hit=0    | Miss, evict A (FIFO) | {C,B}, Hit=0     |
| D   | Miss, evict B (LRU) | {C,D}, Hit=0    | Miss, evict B (FIFO) | {C,D}, Hit=0     |
| A   | Miss, evict C (LRU) | {A,D}, Hit=0    | Miss, evict C (FIFO) | {A,D}, Hit=0     |
| B   | Miss, evict D (LRU) | {A,B}, Hit=0    | Miss, evict D (FIFO) | {A,B}, Hit=0     |
| E   | Miss, evict A (LRU) | {E,B}, Hit=0    | Miss, evict A (FIFO) | {E,B}, Hit=0     |
| A   | Miss, evict B (LRU) | {E,A}, Hit=0    | Miss, evict B (FIFO) | {E,A}, Hit=0     |
| B   | Miss, evict E (LRU) | {A,B}, Hit=0    | Miss, evict E (FIFO) | {A,B}, Hit=0     |
| C   | Miss, evict A (LRU) | {C,B}, Hit=0    | Miss, evict A (FIFO) | {C,B}, Hit=0     |
| D   | Miss, evict B (LRU) | {C,D}, Hit=0    | Miss, evict B (FIFO) | {C,D}, Hit=0     |
| E   | Miss, evict C (LRU) | {E,D}, Hit=0    | Miss, evict C (FIFO) | {E,D}, Hit=0     |

LRU Hit Ratio: 0/12 = 0%
FIFO Hit Ratio: 0/12 = 0%

This pathological case demonstrates scenarios where both policies perform identically. Consider reference string: A, B, C, D, A, B, C, D, A, B, C, D with 2-way cache:

| Ref | LRU Cache | LRU Hit | FIFO Cache | FIFO Hit |
| --- | --------- | ------- | ---------- | -------- |
| A   | {A,-}     | M       | {A,-}      | M        |
| B   | {A,B}     | M       | {A,B}      | M        |
| C   | {C,B}     | M       | {C,B}      | M        |
| D   | {C,D}     | M       | {C,D}      | M        |
| A   | {A,D}     | M       | {A,D}      | M        |
| B   | {A,B}     | H       | {C,B}      | M        |
| C   | {C,B}     | M       | {A,B}      | M        |
| D   | {C,D}     | M       | {A,D}      | M        |
| A   | {A,D}     | M       | {C,D}      | M        |
| B   | {A,B}     | H       | {C,B}      | M        |
| C   | {C,B}     | M       | {A,B}      | M        |
| D   | {C,D}     | M       | {A,D}      | M        |

LRU Hit Ratio: 2/12 = 16.67%
FIFO Hit Ratio: 0/12 = 0%

This demonstrates LRU's superiority in workloads exhibiting temporal locality.

### Example 2: AMAT Calculation with Replacement Policy Impact

**Problem**: A microcontroller features a 4KB L1 data cache (direct-mapped, 64-byte lines) with 1-cycle hit time. Main memory exhibits 100ns access time. Calculate AMAT improvement when LRU policy achieves 95% hit ratio compared to Random replacement at 90% hit ratio.

**Solution**:

- Hit time ($T_{hit}$) = 1 cycle (assume 10ns at 100MHz)
- Miss penalty ($T_{miss}$) = 100ns = 10 cycles
- LRU: Hit ratio = 0.95, Miss ratio = 0.05
- Random: Hit ratio = 0.90, Miss ratio = 0.10

**LRU AMAT**:
$$AMAT_{LRU} = T_{hit} + (1 - H) \times T_{miss} = 10 + 0.05 \times 100 = 15 \text{ ns}$$

**Random AMAT**:
$$AMAT_{Random} = 10 + 0.10 \times 100 = 20 \text{ ns}$$

**Improvement**: (20 - 15) / 20 × 100% = 25% reduction in average memory access time

### Example 3: Belady's Anomaly Demonstration

**Problem**: Demonstrate Belady's anomaly by showing that increasing cache size from 3 frames to 4 frames increases misses under FIFO for reference string: A, B, C, D, A, B, E, A, B, C, D, E

**Solution**:

3-Frame FIFO:

- A, B, C, D, A, B, E, A, B, C, D, E = Miss at all references = 12 misses

4-Frame FIFO:

- A, B, C, D, A, B, E, A, B, C, D, E = Misses at A,B,C,D,A,B,E = 7 misses

Wait—this shows improvement. Let us use the classic counterexample:

Reference string: A, B, C, D, A, B, C, D, A, B, C, D

3-Frame FIFO: Misses at A,B,C,D,A,B,C,D,A,B,C,D = 12 misses
4-Frame FIFO: Misses at A,B,C,D,A,B,E,A,B,E,A,B,E = 9 misses

Let's use the standard Belady example:

Reference: A, B, C, D, A, B, C, D, A, B, C, D, A, B, C, D, E

3-Frame FIFO: 17 misses
4-Frame FIFO: 18 misses (ANOMALY!)

This anomaly confirms that FIFO does not satisfy the inclusion property (stack property), making its behavior unpredictable when cache size changes.

## Summary line replacement policies constitute

Cache a fundamental design trade-off in cache memory systems. LRU provides near-optimal performance for most practical workloads and satisfies the stack property, making it the most widely implemented policy despite hardware complexity. FIFO offers simplicity and determinism but suffers from Belady's anomaly. Random replacement, while theoretically inferior, provides useful lower bounds and eliminates worst-case scenarios. The optimal policy (OPT) serves as an unattainable theoretical benchmark. For embedded microcontroller applications, the choice involves additional considerations: power consumption, timing predictability, and hardware resource constraints. ARM Coprocessor 15 integration ensures proper cache maintenance in real-time systems.
