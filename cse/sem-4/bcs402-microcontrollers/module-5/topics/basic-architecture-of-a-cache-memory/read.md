# Basic Architecture of Cache Memory

## Table of Contents

- [Basic Architecture of Cache Memory](#basic-architecture-of-cache-memory)
- [Introduction](#introduction)
- [1. Memory Hierarchy and Cache Positioning](#1-memory-hierarchy-and-cache-positioning)
- [2. Cache Organization and Address Mapping Techniques](#2-cache-organization-and-address-mapping-techniques)
  - [2.1 Direct-Mapped Cache](#21-direct-mapped-cache)
  - [2.2 Fully Associative Cache](#22-fully-associative-cache)
  - [2.3 Set-Associative Cache](#23-set-associative-cache)
- [3. Cache Line Structure and Tag Comparison](#3-cache-line-structure-and-tag-comparison)
- [4. Cache Write Policies](#4-cache-write-policies)
  - [4.1 Write-Through Policy](#41-write-through-policy)
  - [4.2 Write-Back Policy](#42-write-back-policy)
- [5. Cache Replacement Policies](#5-cache-replacement-policies)
  - [5.1 Least Recently Used (LRU)](#51-least-recently-used-lru)
  - [5.2 First In First Out (FIFO)](#52-first-in-first-out-fifo)
  - [5.3 Random Replacement](#53-random-replacement)
- [6. Cache Miss Classification](#6-cache-miss-classification)
- [7. ARM Coprocessor 15 Cache Control](#7-arm-coprocessor-15-cache-control)
- [Examples](#examples)
  - [Example 1: Address Decomposition for Set-Associative Cache](#example-1-address-decomposition-for-set-associative-cache)
  - [Example 2: Cache Hit Rate Calculation](#example-2-cache-hit-rate-calculation)
  - [Example 3: Direct-Mapped Cache Line Determination](#example-3-direct-mapped-cache-line-determination)
  - [Example 4: Fully Associative Cache Tag Comparison](#example-4-fully-associative-cache-tag-comparison)
- [Assessment](#assessment)
  - [Hard Level MCQ](#hard-level-mcq)
  - [Flashcard](#flashcard)
  - [Problem Solving](#problem-solving)

## Introduction

Cache memory constitutes a fundamental component in contemporary computing architectures, serving as a high-speed intermediary between the central processing unit (CPU) and the slower main memory subsystem. The exponential increase in processor clock frequencies over recent decades has created a significant disparity between CPU execution speeds and memory access latencies—a phenomenon commonly referred to as the "memory wall" problem. This architectural bottleneck necessitates the incorporation of multi-level cache hierarchies to mitigate the performance degradation associated with main memory accesses.

In microcontroller architectures, particularly those implementing ARM Cortex-M and similar processors, cache memory operates as a transparent buffering mechanism that stores frequently accessed data and instruction operands. The fundamental operational principle underlying cache effectiveness derives from the **principle of locality of reference**, which encompasses two complementary characteristics: **temporal locality** (the tendency to revisit recently accessed memory locations) and **spatial locality** (the tendency to access adjacent memory locations). By exploiting these locality characteristics, cache memory substantially reduces the effective memory access latency without requiring fundamental changes to the main memory technology.

For the university's BCS402-Microcontrollers course, comprehensive understanding of cache memory architecture is essential, as modern microcontrollers increasingly incorporate integrated cache subsystems to bridge the performance differential between processors and external memory systems. This module examines the fundamental architectural aspects of cache memory, including mapping techniques, replacement algorithms, write policies, and the specific cache control mechanisms provided by ARM Coprocessor 15.

## 1. Memory Hierarchy and Cache Positioning

The memory hierarchy represents a structured arrangement of various memory technologies, organized according to their access latency, storage capacity, and cost per bit. This hierarchical organization follows three fundamental design principles:

- **Proximity Principle**: Faster but smaller memory units are positioned closer to the CPU
- **Inclusivity Principle**: Each hierarchical level contains a subset of data present in lower levels
- **Trade-off Principle**: Performance is optimized through strategic placement of data based on access frequency

The cache hierarchy typically comprises three levels: **L1 (Level 1) cache** operating at processor clock speed with capacities ranging from 4 KiB to 64 KiB; **L2 (Level 2) cache** providing larger capacity (typically 256 KiB to several megabytes) with moderate latency; and **L3 (Level 3) cache** serving as a shared buffer across multiple processor cores. In ARM Cortex-M7 microcontrollers, the cache architecture commonly implements separate instruction and data caches (I-cache and D-cache) at the L1 level, with optional L2 cache integration.

## 2. Cache Organization and Address Mapping Techniques

The method by which main memory blocks are mapped to cache storage locations fundamentally determines cache performance characteristics, hardware complexity, and implementation cost. Three primary mapping techniques are employed in cache design:

### 2.1 Direct-Mapped Cache

In direct-mapped cache organization, each main memory block possesses exactly one predetermined cache line location, determined by the modulo operation:

**Cache Line Index = (Block Address) mod (Number of Cache Lines)**

The memory address is decomposed into three distinct fields: the **tag field** (identifying the memory block), the **index field** (specifying the cache line), and the **offset field** (identifying the byte within the cache line). This technique offers minimal hardware complexity but suffers from **conflict misses** when multiple frequently-accessed blocks map to identical cache lines.

### 2.2 Fully Associative Cache

Fully associative cache permits placement of any memory block in any cache line, providing maximum flexibility and eliminating conflict misses. However, this organization necessitates parallel comparison of the incoming address tag against all cache line tags, requiring **N comparators for N cache lines**. The hardware implementation complexity grows proportionally with cache capacity, rendering this approach impractical for large caches. The lookup operation executes in O(1) time complexity relative to tag comparison, though the hardware overhead limits typical implementations to small cache configurations.

### 2.3 Set-Associative Cache

Set-associative cache represents a balanced compromise between direct-mapped and fully associative organizations. The cache is partitioned into **S sets**, each containing **W ways** (or lines per set), where W denotes the associativity degree. The mapping function is:

**Set Index = (Block Address) mod (Number of Sets)**

A memory block maps to a specific set but may occupy any way within that set. The 4-way set-associative configuration represents the predominant implementation in modern microcontrollers due to its favorable trade-off between conflict reduction and hardware complexity. When a miss occurs within a set, the replacement policy determines which way gets evicted.

**Address Decomposition Formula**:
For a byte-addressable system with cache size **C**, line size **L**, and associativity **W**:

- **Offset bits** = log₂(L)
- **Index bits** = log₂(C / (L × W))
- **Tag bits** = Address bits - (Offset bits + Index bits)

## 3. Cache Line Structure and Tag Comparison

A cache line (also termed a cache block) comprises multiple structural components beyond the actual data storage:

| Component     | Width     | Function                                                     |
| ------------- | --------- | ------------------------------------------------------------ |
| **Valid Bit** | 1 bit     | Indicates whether the cache line contains valid data         |
| **Dirty Bit** | 1 bit     | Signals modification of cached data relative to main memory  |
| **Tag**       | Variable  | Upper portion of memory address identifying the stored block |
| **Data**      | Line Size | Actual cached memory contents (typically 16-64 bytes)        |

The cache controller performs tag comparison by extracting the index and tag fields from the incoming address, accessing the corresponding cache line, and comparing the stored tag against the extracted tag. A cache **hit** occurs when the valid bit is set AND the tag comparison succeeds.

## 4. Cache Write Policies

Write operations to cached data require careful synchronization between the cache and main memory to maintain data consistency. Two primary write policies are implemented:

### 4.1 Write-Through Policy

Under write-through policy, every write operation to cache simultaneously updates both the cache entry and the corresponding main memory location. This approach guarantees **strong data consistency** and simplifies cache coherence protocols, albeit at the cost of increased memory bandwidth consumption. The effective write latency approaches main memory access time for each write operation.

**Advantages**: Simplified coherence management, guaranteed data consistency
**Disadvantages**: High memory traffic, increased effective write latency

### 4.2 Write-Back Policy

Write-back policy initially updates only the cache line, marking it as **dirty** via the dirty bit. The main memory receives the updated data only when the dirty cache line is evicted to accommodate new data. This approach minimizes memory write traffic significantly but requires sophisticated coherence management in multi-processor systems.

**Advantages**: Reduced memory traffic, lower effective write latency
**Disadvantages**: Potential data inconsistency, complex coherence protocols

The **write-allocate** and **no-write-allocate** policies complement the write policies, determining whether a cache line is allocated on a write miss.

## 5. Cache Replacement Policies

When a cache miss occurs and all ways within the target set are occupied, the replacement policy determines which existing cache line gets evicted. The selection algorithm significantly impacts cache hit ratios:

### 5.1 Least Recently Used (LRU)

LRU maintains temporal access history and evicts the cache line that has not been accessed for the longest duration. True LRU implementation requires tracking **W! possible orderings for W-way associativity**, making precise LRU impractical for high associativity. **Pseudo-LRU** algorithms provide approximate LRU behavior with reduced hardware overhead.

### 5.2 First In First Out (FIFO)

FIFO evicts the oldest cache line regardless of access pattern, implementing a simple queue structure. This policy exhibits lower hardware complexity than LRU but may perform poorly when older lines retain temporal locality.

### 5.3 Random Replacement

Random replacement selects a victim cache line arbitrarily, providing predictable behavior and minimal hardware complexity. While theoretically appearing suboptimal, random replacement often achieves performance comparable to more complex policies in practice.

## 6. Cache Miss Classification

Cache misses are categorized into three fundamental types, each requiring distinct optimization strategies:

- **Compulsory Miss (Cold Miss)**: Occurs upon first access to any memory block; unavoidable for initial data placement
- **Capacity Miss**: Results from finite cache capacity when working set exceeds cache size
- **Conflict Miss**: Arises in direct-mapped/set-associative caches when multiple blocks compete for identical cache locations

The **average memory access time (AMAT)** formula incorporating miss penalties:

**AMAT = Hit Time + (Miss Rate × Miss Penalty)**

## 7. ARM Coprocessor 15 Cache Control

ARM architecture implements cache management through **Coprocessor 15 (CP15)**, particularly in processors lacking dedicated cache controllers. Key control registers include:

- **SCTLR (System Control Register)**: Bit 12 (I) enables instruction cache; Bit 2 (C) enables data cache
- **ACTLR (Auxiliary Control Register)**: Provides implementation-specific cache configuration
- **CSSELR (Cache Size Selection Register)**: Selects cache level for subsequent operations
- **CCR (Cache Configuration Register)**: Specifies cache size, associativity, and line length

Cache invalidation and cleaning operations (e.g., `ICIVAU`, `DCIVAU`, `DCVAC`) maintain cache coherence with main memory during software-managed cache operations.

## Examples

### Example 1: Address Decomposition for Set-Associative Cache

**Problem**: Given a 16 KiB 4-way set-associative cache with 32-byte blocks in a 32-bit addressable system, determine the number of tag bits, index bits, and offset bits.

**Solution**:

Given parameters:

- Cache Size (C) = 16 KiB = 16 × 1024 = 16384 bytes
- Associativity (W) = 4
- Block Size (L) = 32 bytes = 2⁵ bytes

**Step 1: Calculate Offset Bits**
Offset = log₂(32) = 5 bits

**Step 2: Calculate Number of Sets**
Number of Sets = Cache Size / (Associativity × Block Size)
= 16384 / (4 × 32)
= 16384 / 128
= 128 sets = 2⁷

**Step 3: Calculate Index Bits**
Index = log₂(128) = 7 bits

**Step 4: Calculate Tag Bits**
Tag = Address bits - (Index bits + Offset bits)
= 32 - (7 + 5)
= 20 bits

**Answer**: Offset = 5 bits, Index = 7 bits, Tag = 20 bits

---

### Example 2: Cache Hit Rate Calculation

**Problem**: A processor executes a program with the following memory access pattern: 150 instruction fetches (100 hits), 100 data reads (80 hits), and 50 data writes (40 hits). The cache hit time is 1 clock cycle, and the miss penalty is 20 clock cycles. Calculate the average memory access time (AMAT).

**Solution**:

**Step 1: Calculate Total Accesses**
Total accesses = 150 + 100 + 50 = 300

**Step 2: Calculate Overall Hit Count**
Total hits = 100 + 80 + 40 = 220

**Step 3: Calculate Hit Rate and Miss Rate**
Hit Rate = 220 / 300 = 0.7333 (73.33%)
Miss Rate = 1 - 0.7333 = 0.2667 (26.67%)

**Step 4: Calculate AMAT**
AMAT = Hit Time + (Miss Rate × Miss Penalty)
= 1 + (0.2667 × 20)
= 1 + 5.334
= 6.334 clock cycles

**Answer**: Average Memory Access Time = 6.334 clock cycles

---

### Example 3: Direct-Mapped Cache Line Determination

**Problem**: A direct-mapped cache has 256 cache lines, each storing 64 bytes. For the memory address 0x1A2B3C4D, determine: (a) the cache line index, (b) the tag value, and (c) the byte offset.

**Solution**:

Given parameters:

- Number of cache lines = 256 = 2⁸
- Line size = 64 bytes = 2⁶ bytes

**Step 1: Determine Bit Allocation**

- Offset bits = log₂(64) = 6 bits
- Index bits = log₂(256) = 8 bits
- Tag bits = 32 - (6 + 8) = 18 bits

**Step 2: Convert Address to Binary**
0x1A2B3C4D = 0001 1010 0010 1011 0011 1100 0100 1101

**Step 3: Extract Fields (from LSB)**

- Offset (bits 0-5): 00 1101 = 0x0D = 13
- Index (bits 6-13): 11 0010 10 = 0xCA/4? Let's recalculate

Better approach:

- Address = 0x1A2B3C4D = 00011010001010110011110001001101
- Bits 0-5 (offset): 001101 = 13
- Bits 6-13 (index): 10001010 = 0x8A = 138
- Bits 14-31 (tag): 000110100010101100 = 0x6A2C / 4? Let's use proper extraction

**Using modulo method directly:**

- Line Index = Address mod Number of Lines = (0x1A2B3C4D mod 256)
- 0x1A2B3C4D = 439041389 decimal
- Line Index = 439041389 mod 256 = 138

**Step 4: Calculate Tag**
Tag = Address / Number of Lines (integer division)
= floor(439041389 / 256)
= floor(1715787.45) = 1715787

**(a) Cache Line Index = 138**
**(b) Tag Value = 1715787 (or 0x1A2B3C in upper 24 bits)**
**(c) Byte Offset = 13**

---

### Example 4: Fully Associative Cache Tag Comparison

**Problem**: In a fully associative cache with 64 cache lines, each storing 32 bytes, how many tag comparators are required? If the cache operates at 1 GHz with each comparator introducing 0.2 ns delay, what is the minimum cache lookup time?

**Solution**:

**Step 1: Determine Comparator Requirement**
In fully associative cache, every cache line must be checked in parallel:

- Number of tag comparators = Number of cache lines = 64

**Step 2: Calculate Lookup Time**

- Comparator delay = 0.2 ns
- Cache lookup time is dominated by parallel tag comparison
- Minimum lookup time = 0.2 ns (assuming ideal multiplexer selection)

**Answer**: 64 comparators required; minimum lookup time = 0.2 ns

---

## Assessment

### Hard Level MCQ

**Question**: Consider a processor with separate instruction and data caches, each being 32 KiB direct-mapped with 64-byte blocks. The processor executes a loop that sequentially accesses 16 KiB of instruction data and 8 KiB of data. Assuming both caches start empty, calculate the total number of cache misses for instruction cache, given that the loop executes 1000 iterations.

_Hint: Consider both compulsory misses and conflict misses arising from the sequential instruction access pattern._

**Answer**:

- Instruction cache: 32 KiB / 64 bytes = 512 lines
- 16 KiB instruction footprint spans 256 cache lines
- First iteration causes 256 compulsory misses (one per unique line)
- Subsequent iterations access the same 256 lines repeatedly → all hits (temporal locality)
- **Total instruction cache misses = 256**

---

### Flashcard

**Q**: Why does increasing set-associativity typically reduce conflict misses while potentially increasing access latency?
**A**: Higher set-associativity provides more candidate locations (ways) within each set, reducing the probability that multiple frequently-accessed blocks map to identical cache lines and compete for the same location. However, the cache controller must perform tag comparisons across multiple ways before determining a hit or miss, and the multiplexer selection logic introduces additional delay proportional to log₂(W), where W represents the number of ways.

---

### Problem Solving

**Problem**: A microcontroller implements a 2-way set-associative data cache with 256 sets, 64-byte blocks, and a write-back policy. The processor writes to consecutive 32-bit integers at addresses 0x1000, 0x1004, 0x1008, 0x100C (four consecutive writes). Analyze the cache behavior and determine which cache lines get dirty.

**Solution**:

**Step 1: Determine Address Fields**

- Block size = 64 bytes = 2⁶ → Offset bits = 6
- Number of sets = 256 = 2⁸ → Index bits = 8
- Tag bits = 32 - (6 + 8) = 18

**Step 2: Analyze Address Mapping**

- 0x1000 = 0001 0000 0000 0000 → Index = 0x00 (line 0)
- 0x1004 = 0001 0000 0000 0100 → Index = 0x00 (same line, offset 4)
- 0x1008 = 0001 0000 0000 1000 → Index = 0x00 (same line, offset 8)
- 0x100C = 0001 0000 0000 1100 → Index = 0x00 (same line, offset 12)

**Step 3: Cache Behavior**

- First write (0x1000): Cache miss → fetch block containing bytes 0x1000-0x103F → write updates Way 0 or Way 1 → mark dirty
- Second write (0x1004): Cache hit (same block, different offset) → write to cache line → remains dirty
- Third write (0x1008): Cache hit → write to cache line → remains dirty
- Fourth write (0x100C): Cache hit → write to cache line → remains dirty

**Answer**: Only one cache line (index 0) gets dirty, containing all four written values. The write-back policy delays main memory update until this line gets evicted.
