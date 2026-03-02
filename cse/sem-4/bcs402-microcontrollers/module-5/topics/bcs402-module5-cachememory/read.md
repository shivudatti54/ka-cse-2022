# The Relationship Between Cache and Main Memory

## Table of Contents

- [The Relationship Between Cache and Main Memory](#the-relationship-between-cache-and-main-memory)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Cache Memory Fundamentals](#cache-memory-fundamentals)
  - [Main Memory (RAM)](#main-memory-ram)
  - [Cache Mapping Techniques](#cache-mapping-techniques)
  - [Cache Write Policies](#cache-write-policies)
  - [Write Allocation Policies](#write-allocation-policies)
  - [Cache Coherence](#cache-coherence)
  - [Hit Rate and Miss Rate](#hit-rate-and-miss-rate)
- [Examples](#examples)
  - [Example 1: Calculating Average Memory Access Time](#example-1-calculating-average-memory-access-time)
  - [Example 2: Direct Mapped Cache Address Decoding](#example-2-direct-mapped-cache-address-decoding)
  - [Example 3: Set Associative Cache Configuration](#example-3-set-associative-cache-configuration)
- [Exam Tips](#exam-tips)

## Introduction

In modern computer systems, especially in microcontroller applications, the relationship between cache memory and main memory is fundamental to achieving high performance while maintaining cost-effectiveness. Cache memory serves as a high-speed buffer between the fast processor and the relatively slower main memory (typically DRAM). This hierarchical memory organization addresses the growing speed gap between processors and memory subsystems, which would otherwise create a severe bottleneck in system performance.

For students studying microcontrollers, understanding this relationship is crucial because most embedded systems and microcontroller applications operate under strict timing constraints and power limitations. The cache-main memory relationship directly impacts instruction execution speed, power consumption, and overall system efficiency. As microcontroller architectures become increasingly sophisticated with higher clock speeds, the importance of effective cache management becomes even more pronounced.

This topic explores how cache and main memory work together, the various techniques used to maintain consistency between them, the mapping strategies that determine how data is stored in cache, and the write policies that govern how modifications are propagated. Mastery of these concepts is essential for engineers designing efficient embedded systems and optimizing software for microcontroller platforms.

## Key Concepts

### Cache Memory Fundamentals

Cache memory is a small, fast memory located between the CPU and main memory. It stores frequently accessed data and instructions to reduce the average memory access time. The fundamental principle behind cache is temporal and spatial locality:

- **Temporal Locality**: Recently accessed items are likely to be accessed again soon
- **Spatial Locality**: Items near recently accessed items are likely to be accessed soon

Cache is organized into multiple levels, with L1 (Level 1) being the smallest and fastest, followed by L2 and possibly L3 caches. In microcontroller contexts, we typically deal with single-level or two-level caches.

### Main Memory (RAM)

Main memory, typically implemented as Dynamic RAM (DRAM) in microcontroller systems, provides larger storage capacity at the cost of slower access times. DRAM requires periodic refreshing and has access times measured in tens to hundreds of nanoseconds, compared to cache access times measured in nanoseconds or picoseconds.

### Cache Mapping Techniques

The mapping technique determines how main memory blocks are placed in cache:

**1. Direct Mapping**
Each main memory block maps to exactly one cache line. The cache line is determined by the block address modulo the number of cache lines.

- Address structure: Tag | Index | Block Offset
- Advantages: Simple hardware, fast lookup
- Disadvantage: Conflict misses

**2. Fully Associative Mapping**
Any main memory block can be placed in any cache line.

- Address structure: Tag | Block Offset
- Advantages: Maximum flexibility, lowest miss rate
- Disadvantage: Requires expensive comparison hardware (CAM)

**3. Set Associative Mapping**
A compromise between direct and fully associative mapping. Cache is divided into sets, and each set contains multiple lines. A block can be placed in any line within a specific set.

- Address structure: Tag | Set Index | Block Offset
- Most common: 2-way, 4-way, 8-way set associative
- Provides good balance of hit rate and hardware cost

### Cache Write Policies

When the processor writes data to cache, the write policy determines how main memory is updated:

**1. Write Through**
Every write to cache also writes through to main memory.

- Advantages: Simple consistency, main memory always has latest data
- Disadvantage: Slower writes, bus traffic on every write

**2. Write Back**
Writes are only made to cache, and main memory is updated only when the block is replaced.

- Advantages: Faster writes, reduced memory traffic
- Disadvantage: More complex hardware, potential consistency issues

### Write Allocation Policies

**Write Allocate (Fetch on Write)**
If the write misses in cache, the block is loaded into cache before the write is performed.

**No-Write Allocate (Write Around)**
If the write misses in cache, the data is written directly to main memory without loading into cache.

### Cache Coherence

In systems with multiple caches (common in multi-core microcontrollers), cache coherence ensures that all caches have a consistent view of main memory. Key protocols include:

**MESI Protocol** (Modified, Exclusive, Shared, Invalid):

- **M (Modified)**: Cache line is dirty (modified) and only this cache has it
- **E (Exclusive)**: Cache line is clean and only this cache has it
- **S (Shared)**: Cache line is clean and multiple caches may have it
- **I (Invalid)**: Cache line is not valid

### Hit Rate and Miss Rate

- **Hit**: Requested data is found in cache
- **Miss**: Requested data is not in cache and must be fetched from main memory
- **Hit Rate**: Percentage of memory accesses satisfied by cache
- **Miss Rate**: 1 - Hit Rate

Average Memory Access Time (AMAT) = Hit Time + (Miss Rate × Miss Penalty)

## Examples

### Example 1: Calculating Average Memory Access Time

**Problem**: A microcontroller has a cache with a hit time of 2 ns and a miss penalty of 20 ns. If the hit rate is 95%, calculate the average memory access time.

**Solution**:

Given:

- Hit Time (T_hit) = 2 ns
- Miss Penalty (T_miss) = 20 ns
- Hit Rate (H) = 95% = 0.95

Using the formula:
AMAT = T_hit + (Miss Rate × Miss Penalty)
AMAT = 2 ns + ((1 - 0.95) × 20 ns)
AMAT = 2 ns + (0.05 × 20 ns)
AMAT = 2 ns + 1 ns
AMAT = 3 ns

The average memory access time is 3 ns.

### Example 2: Direct Mapped Cache Address Decoding

**Problem**: A microcontroller has a 16 KB direct-mapped cache with 64-byte block size. Main memory is 1 MB. Determine:
(a) Number of cache lines
(b) Number of index bits
(c) Number of offset bits
(d) Number of tag bits

**Solution**:

Given:

- Cache size = 16 KB = 16 × 1024 = 16384 bytes
- Block size = 64 bytes = 2^6 bytes
- Main memory = 1 MB = 2^20 bytes

(a) Number of cache lines = Cache size / Block size
= 16384 / 64 = 256 lines = 2^8 lines

(b) Number of index bits = log₂(Number of cache lines)
= log₂(256) = 8 bits

(c) Number of offset bits = log₂(Block size)
= log₂(64) = 6 bits

(d) Number of tag bits = Address bits - Index bits - Offset bits
Main memory address bits = log₂(1 MB) = 20 bits
Tag bits = 20 - 8 - 6 = 6 bits

### Example 3: Set Associative Cache Configuration

**Problem**: A 4-way set-associative cache has 1024 sets, 64 bytes per block, and uses 32-bit addresses. Calculate:
(a) Cache size
(b) Total number of cache lines

**Solution**:

Given:

- Associativity = 4-way
- Number of sets = 1024 = 2^10
- Block size = 64 bytes = 2^6 bytes

(a) Cache size = Associativity × Sets × Block size
= 4 × 1024 × 64 bytes
= 4 × 65536 bytes
= 262144 bytes = 256 KB

(b) Total cache lines = Associativity × Sets
= 4 × 1024 = 4096 lines

## Exam Tips

1. **Remember the locality principles**: Temporal and spatial locality are the fundamental reasons cache memory works effectively.

2. **Know the mapping techniques**: Be able to distinguish between direct, fully associative, and set-associative mapping, including their advantages and disadvantages.

3. **Write policy selection**: Write-back is faster but more complex; write-through is simpler but slower. Understand when each is appropriate.

4. **Calculate AMAT**: This is a common exam question. Remember the formula: AMAT = Hit Time + (Miss Rate × Miss Penalty).

5. **Cache address decomposition**: Be able to break down a memory address into tag, index, and offset bits given cache parameters.

6. **MESI protocol states**: Know what Modified, Exclusive, Shared, and Invalid states mean and when transitions occur.

7. **Understand miss types**: Compulsory (cold start), capacity, and conflict misses are important concepts.

8. **Power considerations**: In microcontroller applications, cache can significantly impact power consumption due to reduced main memory accesses.

9. **Hit rate improvement**: Larger cache, larger block size, and higher associativity generally improve hit rate but increase cost and latency.

10. **Word alignment**: Remember that block offset bits determine how many bytes within a block can be accessed.
