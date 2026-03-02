# Set Associativity in Cache Memory

## Table of Contents

- [Set Associativity in Cache Memory](#set-associativity-in-cache-memory)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Structure of Set-Associative Cache](#basic-structure-of-set-associative-cache)
  - [Address Division](#address-division)
  - [Cache Hit and Cache Miss](#cache-hit-and-cache-miss)
  - [Replacement Policies](#replacement-policies)
  - [Write Policies](#write-policies)
- [Examples](#examples)
  - [Example 1: Calculating Set Index and Tag Bits](#example-1-calculating-set-index-and-tag-bits)
  - [Example 2: Cache Hit/Miss Determination](#example-2-cache-hitmiss-determination)
  - [Example 3: Performance Comparison](#example-3-performance-comparison)
- [Exam Tips](#exam-tips)

## Introduction

Set associativity is a fundamental concept in computer memory organization that plays a crucial role in determining the performance of cache memory systems. In modern microcontrollers and microprocessors, the cache memory serves as a high-speed buffer between the slower main memory and the CPU, significantly reducing memory access times. The organization of this cache memory, particularly how data is mapped from main memory to cache, directly impacts hit rates, miss penalties, and overall system performance.

Set-associative mapping represents a compromise between the simplicity of direct-mapped cache and the flexibility of fully associative cache. This hybrid approach combines the advantages of both mapping techniques while minimizing their drawbacks. Understanding set associativity is essential for embedded systems designers and computer engineers, as it helps in optimizing memory hierarchies for specific applications. In microcontroller-based systems, particularly those with limited resources, choosing the appropriate set-associativity can make significant differences in real-time performance and power consumption.

This topic covers the fundamental principles of set-associative cache mapping, including the structure of cache blocks, the address division mechanism, hit and miss scenarios, and performance analysis. These concepts form the backbone of memory hierarchy design in contemporary computing systems.

## Key Concepts

### Basic Structure of Set-Associative Cache

In a set-associative cache, the cache memory is divided into a number of sets, where each set contains a fixed number of ways (or lines). Each way can store one block of data along with its tag information. The total number of lines in the cache is given by the product of the number of sets and the number of ways. For example, a cache with 128 sets and 4 ways per set has 512 total cache lines.

The fundamental equation governing set-associative cache is:

**Number of Sets = (Cache Size) / (Block Size × Number of Ways)**

When the CPU needs to access a memory location, it calculates the set index using a portion of the address bits. All ways within that particular set are then searched in parallel to determine if the requested data is present (cache hit) or not (cache miss).

### Address Division

The main memory address is divided into three distinct fields when using set-associative mapping:

1. **Tag Field**: The most significant bits of the address that identify which block from main memory is stored in the cache line. The number of tag bits depends on the cache size and block size.

2. **Set Index Field**: The middle bits that identify which set the block should map to in the cache. If there are 2^s sets, then s bits are needed for the set index.

3. **Block Offset Field**: The least significant bits that identify the specific byte within the cache block. If each block contains 2^b bytes, then b bits are required for the block offset.

### Cache Hit and Cache Miss

**Cache Hit**: Occurs when the requested data is found in the cache. In a set-associative cache, the CPU compares the tag bits of the address with the tag stored in each way of the selected set. If a match is found along with valid bits set, it is a cache hit. The data is then retrieved from the appropriate way and forwarded to the CPU.

**Cache Miss**: Occurs when the requested data is not found in any way of the accessed set. Upon a cache miss, the CPU must fetch the data from the main memory (or a lower-level cache). The fetched block is then stored in one of the ways of the corresponding set, potentially replacing an existing block based on the replacement policy.

### Replacement Policies

When a cache miss occurs and all ways in the selected set are already occupied, the cache controller must decide which block to replace. The common replacement algorithms include:

1. **Least Recently Used (LRU)**: The block that has not been accessed for the longest time is replaced. This policy provides good performance but requires additional hardware to track access history.

2. **First In First Out (FIFO)**: The block that has been in the cache for the longest time is replaced. This is simpler to implement but may not reflect actual usage patterns.

3. **Random**: A randomly selected block is replaced. This eliminates the overhead of tracking but provides unpredictable performance.

### Write Policies

Cache memory must handle both read and write operations. The write policies determine how write operations are handled:

1. **Write Through**: Data is written to both the cache and main memory simultaneously. This ensures data consistency but increases memory traffic.

2. **Write Back**: Data is written only to the cache, and main memory is updated only when the block is replaced. This reduces memory writes but requires additional complexity to maintain coherence.

## Examples

### Example 1: Calculating Set Index and Tag Bits

**Problem**: A system has a main memory of 64 MB with word size 1 byte. The cache has 64 KB capacity with block size 16 bytes and is 4-way set-associative. Calculate the number of sets, tag bits, set index bits, and offset bits.

**Solution**:

Given:

- Main memory address = 64 MB = 2^26 bytes, so address bits = 26
- Cache size = 64 KB = 2^16 bytes
- Block size = 16 bytes = 2^4 bytes
- Associativity = 4-way

Step 1: Calculate number of sets

```
Number of Sets = Cache Size / (Block Size × Number of Ways)
 = 2^16 / (2^4 × 4)
 = 2^16 / (2^4 × 2^2)
 = 2^16 / 2^6
 = 2^10 = 1024 sets
```

Step 2: Calculate offset bits

```
Offset bits = log2(Block size) = log2(16) = 4 bits
```

Step 3: Calculate set index bits

```
Set Index bits = log2(Number of sets) = log2(1024) = 10 bits
```

Step 4: Calculate tag bits

```
Tag bits = Address bits - Set Index bits - Offset bits
 = 26 - 10 - 4
 = 12 bits
```

Therefore: Number of sets = 1024, Tag = 12 bits, Set Index = 10 bits, Offset = 4 bits

### Example 2: Cache Hit/Miss Determination

**Problem**: Consider a 2-way set-associative cache with 4 sets (initially empty). The block size is 1 word. The following memory accesses occur: Read 0, Read 4, Read 8, Read 0, Read 12, Read 8. Determine whether each access is a hit or miss, assuming FIFO replacement.

**Solution**:

With 4 sets, we need 2 bits for set index (2^2 = 4).
Address calculation: Set Index = Address mod 4

Initial cache state: All ways empty

| Access  | Address | Set Index | Hit/Miss | Action                                           |
| ------- | ------- | --------- | -------- | ------------------------------------------------ |
| Read 0  | 0       | 0         | Miss     | Load block 0 into Way 0 of Set 0                 |
| Read 4  | 4       | 0         | Miss     | Load block 4 into Way 1 of Set 0                 |
| Read 8  | 8       | 0         | Miss     | Replace block 0 (FIFO), load block 8 into Way 0  |
| Read 0  | 0       | 0         | Miss     | Replace block 4 (FIFO), load block 0 into Way 1  |
| Read 12 | 12      | 0         | Miss     | Replace block 8 (FIFO), load block 12 into Way 0 |
| Read 8  | 8       | 0         | Miss     | Replace block 0 (FIFO), load block 8 into Way 1  |

Result: All accesses are misses (0 hits, 6 misses)

### Example 3: Performance Comparison

**Problem**: Compare the hit ratio of direct-mapped, 2-way set-associative, and 4-way set-associative caches for the following sequence of block accesses: 0, 2, 4, 0, 2, 6, 0, 2, 4, 6. Assume the cache has 4 slots (blocks) and uses LRU replacement.

**Solution**:

**Direct-Mapped (4 slots)**:

- Block 0 maps to slot 0, Block 2 maps to slot 2, Block 4 maps to slot 0, Block 6 maps to slot 2

| Access | Block | Slot | Hit/Miss |
| ------ | ----- | ---- | -------- |
| 0      | 0     | 0    | Miss     |
| 2      | 2     | 2    | Miss     |
| 4      | 4     | 0    | Miss     |
| 0      | 0     | 0    | Hit      |
| 2      | 2     | 2    | Hit      |
| 6      | 6     | 2    | Miss     |
| 0      | 0     | 0    | Miss     |
| 2      | 2     | 2    | Miss     |
| 4      | 4     | 0    | Miss     |
| 6      | 6     | 2    | Miss     |

Hits = 2, Hit Ratio = 2/10 = 0.2

**2-Way Set-Associative (2 sets, 2 ways each)**:

- Blocks 0, 4 → Set 0; Blocks 2, 6 → Set 1

| Access | Block | Set | Hit/Miss |
| ------ | ----- | --- | -------- |
| 0      | 0     | 0   | Miss     |
| 2      | 2     | 1   | Miss     |
| 4      | 4     | 0   | Miss     |
| 0      | 0     | 0   | Hit      |
| 2      | 2     | 1   | Hit      |
| 6      | 6     | 1   | Miss     |
| 0      | 0     | 0   | Hit      |
| 2      | 2     | 1   | Hit      |
| 4      | 4     | 0   | Miss     |
| 6      | 6     | 1   | Miss     |

Hits = 4, Hit Ratio = 4/10 = 0.4

**4-Way Set-Associative (1 set, 4 ways)**:
All blocks can be stored in the single set.

| Access | Block | Hit/Miss |
| ------ | ----- | -------- |
| 0      | 0     | Miss     |
| 2      | 2     | Miss     |
| 4      | 4     | Miss     |
| 0      | 0     | Hit      |
| 2      | 2     | Hit      |
| 6      | 6     | Miss     |
| 0      | 0     | Hit      |
| 2      | 2     | Hit      |
| 4      | 4     | Hit      |
| 6      | 6     | Hit      |

Hits = 7, Hit Ratio = 7/10 = 0.7

This demonstrates that higher associativity improves hit ratio, though at the cost of increased hardware complexity and access time.

## Exam Tips

1. **Remember the address division formula**: Address = Tag + Set Index + Block Offset. Always know how to calculate each field given cache parameters.

2. **Set associativity formula**: Number of Sets = Cache Size / (Block Size × Number of Ways). This is frequently tested in university exams.

3. **Cache hit occurs when**: The tag matches AND the valid bit is set. Never forget to check the valid bit in problems.

4. **Higher associativity means**: Better hit rate but more complex hardware, higher power consumption, and potentially slower access time due to parallel comparison of all ways.

5. **Replacement policies**: Know LRU, FIFO, and Random policies. LRU is most commonly implemented and provides the best performance for typical programs.

6. **Write through vs Write back**: Write through is simpler and maintains consistency but uses more memory bandwidth. Write back is faster but requires dirty bits and can cause coherence issues in multiprocessor systems.

7. **Trade-offs in cache design**: When solving problems, remember that increasing associativity reduces conflict misses but increases hit time and hardware cost.

8. **Block size considerations**: Larger blocks reduce miss rate (capacity misses) but increase miss penalty and may increase conflict misses.
