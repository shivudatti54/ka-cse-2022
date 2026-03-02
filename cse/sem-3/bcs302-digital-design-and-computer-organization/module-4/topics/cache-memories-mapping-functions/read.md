# Cache Memories – Mapping Functions

## Introduction

Cache memory is a small, fast SRAM-based memory interposed between the processor and main memory, designed to reduce the average memory access time through the principle of locality. Since the cache capacity is substantially smaller than main memory, only a subset of memory blocks can reside in the cache at any given time. A **mapping function** defines the deterministic rule that establishes the location(s) where a particular main memory block may be placed within the cache structure. The selection of an appropriate mapping function constitutes a critical cache design decision, directly influencing the hit ratio, hardware complexity, and overall system performance.

## Cache Organization Fundamentals

Before proceeding to mapping functions, the following fundamental terminology must be established with mathematical precision:

- **Block (or Line):** The fundamental unit of data transfer between main memory and cache, typically comprising $2^m$ bytes where $m \in \{4, 5, 6\}$ (i.e., 16–64 bytes).

- **Tag:** The most significant portion of the main memory address stored concurrently with each cache line, serving to identify which specific memory block is currently resident.

- **Index (or Set Index):** The field comprising $k$ address bits utilized to select a particular cache line or set, depending on the mapping strategy employed.

- **Offset (or Word/Byte Offset):** The least significant $m$ address bits that identify the specific byte within a block.

- **Hit:** The condition wherein the requested data is found in the cache (tag comparison yields a match).

- **Miss:** The condition wherein the requested data is absent from the cache, necessitating retrieval from main memory with subsequent cache update.

For an $n$-bit physical address, the generic address field structure is:

```
|<---- Tag ---->|<--- Index --->|<--- Offset --->|
```

Given main memory of $2^n$ addressable bytes, cache comprising $2^k$ lines, and block size of $2^m$ bytes, the fundamental relationship governing cache organization is:

$$n = \text{tag\_bits} + k + m$$

## 1. Direct Mapping

Direct mapping represents the simplest mapping function, wherein each main memory block maps to **exactly one** predetermined cache line according to a modular arithmetic relationship.

### Mapping Function Derivation

Let $B$ denote the main memory block number and $C$ denote the total number of cache lines. The cache line number $L$ to which block $B$ maps is given by:

$$L = B \mod C = B \mod 2^k$$

**Proof:** Since $C = 2^k$ (a power of 2), the modulo operation reduces to selecting the least significant $k$ bits of the binaryB$. Therefore, $L$ is representation of $ uniquely determined by these $k$ bits, constituting the index field.

### Address Field Breakdown

| Field  | Bits        | Purpose                                                   |
| ------ | ----------- | --------------------------------------------------------- |
| Tag    | $n - k - m$ | Uniquely identifies which memory block occupies this line |
| Index  | $k$         | Selects the specific cache line (line number)             |
| Offset | $m$         | Selects the specific byte within the block                |

### Numerical Example

Consider a system with the following specifications:

- Main memory: 16 MB (24-bit address, $n = 24$)
- Cache: 256 lines ($2^k = 256 \Rightarrow k = 8$)
- Block size: 64 bytes ($2^m = 64 \Rightarrow m = 6$)

**Address field decomposition:**

- Offset bits: $\log_2(64) = 6$ bits
- Index bits: $\log_2(256) = 8$ bits
- Tag bits: $24 - 8 - 6 = 10$ bits

Consequently, main memory blocks $0, 256, 512, 768, \ldots$ all map to cache line 0 (sharing identical index, distinguished by distinct tags).

### Advantages and Disadvantages

**Advantages:**

- Hardware implementation is straightforward and cost-effective
- Only a single tag comparison is required per memory access
- Critical path delay is minimal due to simplified multiplexer logic

**Disadvantages:**

- **Conflict misses (thrashing):** Two or more frequently accessed blocks mapping to the same line will repeatedly evict each other, degrading performance even when cache capacity remains available
- Fixed placement leads to suboptimal utilization of cache resources

## 2. Fully Associative Mapping

In fully associative mapping, a main memory block may occupy **any** cache line, providing maximum flexibility in block placement.

### Mapping Function

Unlike direct mapping, there exists no deterministic function governing placement:

$$L \in \{0, 1, 2, \ldots, C-1\} \text{ for any block } B$$

The block may be placed in any available cache line; the choice is typically governed by the replacement policy.

### Address Field Breakdown

| Field  | Bits    | Purpose                                            |
| ------ | ------- | -------------------------------------------------- |
| Tag    | $n - m$ | Identifies the memory block (entire block address) |
| Offset | $m$     | Selects the specific byte within the block         |

The index field is entirely eliminated since placement is unconstrained.

### Hardware Implementation

To determine cache hit/miss, the tag of the requested address must be compared against tags of **all** cache lines simultaneously. This necessitates **Content-Addressable Memory (CAM)**, which performs parallel associative search in $O(1)$ time complexity. The hardware comprises:

- $C$ tag comparators operating in parallel
- Priority encoder to select the matching line
- Match signal generation

### Advantages and Disadvantages

**Advantages:**

- Maximum flexibility eliminates conflict misses entirely
- Highest theoretical hit rate for a given cache capacity
- Optimal utilization of available cache lines

**Disadvantages:**

- CAM implementation incurs significant silicon area overhead ($O(C)$ comparators)
- Tag comparison latency increases with cache size
- Practical only for small caches (typically $C \leq 64$) due to hardware cost constraints

## 3. Set-Associative Mapping

Set-associative mapping represents a **balanced compromise** between direct and fully associative approaches. The cache is partitioned into $S$ sets, each containing $N$ lines (ways), where $N$-way set-associativity implies $N$ lines per set.

### Mapping Function Derivation

Given total cache lines $C$ and associativity $N$:

$$S = \frac{C}{N} = 2^s \text{ where } s = \log_2(S)$$

The set number $S_{num}$ to which block $B$ maps is:

$$S_{num} = B \mod S = B \mod 2^s$$

Within the designated set, the block may occupy any of the $N$ ways.

### Address Field Breakdown

| Field     | Bits        | Purpose                                                   |
| --------- | ----------- | --------------------------------------------------------- |
| Tag       | $n - s - m$ | Identifies the memory block within the set                |
| Set Index | $s$         | Selects the specific set ($s = \log_2$ of number of sets) |
| Offset    | $m$         | Selects the specific byte within the block                |

### Example: 2-Way Set-Associative Cache

Given:

- Cache: 256 lines total
- Associativity: 2-way

**Computation:**

- Number of sets: $256 / 2 = 128 = 2^7 \Rightarrow s = 7$
- Set index bits: 7
- Tag bits: $24 - 7 - 6 = 11$ bits

Two memory blocks that would conflict in direct-mapped organization (sharing identical index) can now coexist within the same set using different ways.

### Advantages and Disadvantages

**Advantages:**

- Dramatically reduces conflict misses relative to direct mapping
- Hardware cost scales linearly with associativity $N$ (not with $C$)
- Practical for modern processors: 4-way, 8-way, 16-way implementations are common

**Disadvantages:**

- Increased hardware complexity compared to direct mapping
- Requires $N$ tag comparisons per access
- Necessitates a replacement policy when all ways within a set are occupied

### Special Cases

- **1-way set-associative:** Reduces to direct-mapped cache
- **N-way set-associative where $N = C$:** Equivalent to fully associative cache

## 4. Replacement Policies

When a cache miss occurs and the target set (or the entire cache in fully associative mapping) is fully occupied, a replacement policy determines which existing block to evict. The choice significantly impacts hit ratio.

### Least Recently Used (LRU)

The LRU policy evicts the block that has not been accessed for the longest duration. Implementation requires maintaining access history:

- **True LRU:** Maintains a total ordering of all ways; computationally expensive ($O(N!)$ states for $N$-way)
- **Approximate LRU (Pseudo-LRU):** Uses a binary tree structure; common in modern processors

**Theorem:** For a given access pattern exhibiting temporal locality, LRU minimizes the miss rate (proved via stack depth analysis).

### First In First Out (FIFO)

The oldest block in the set is evicted, regardless of access history. Simpler to implement than LRU but may perform poorly with looping access patterns.

### Random

A randomly selected block is evicted. Hardware implementation is trivial but provides no temporal locality exploitation. Useful for eliminating worst-case scenarios.

### Policy Comparison

| Policy | Hardware Complexity | Miss Rate | Vulnerability        |
| ------ | ------------------- | --------- | -------------------- |
| LRU    | High                | Lowest    | Sequential scan      |
| FIFO   | Medium              | Moderate  | Loop access patterns |
| Random | Minimal             | Variable  | None                 |

## 5. Performance Analysis and Comparison

### Hit Rate Equations

For direct-mapped cache with access pattern exhibiting uniform block reuse:
$$\text{Hit Rate} \approx 1 - \frac{C}{M}$$
where $M$ is the number of distinct blocks accessed.

For $N$-way set-associative:
$$\text{Hit Rate}_{N\text{-way}} > \text{Hit Rate}_{1\text{-way}}$$

### Quantitative Comparison

| Mapping Type | Tag Comparisons | Conflict Misses | Hardware Cost |
| ------------ | --------------- | --------------- | ------------- |
| Direct       | 1               | High            | Minimal       |
| Fully Assoc. | $C$             | None            | Maximum       |
| N-way        | $N$             | Moderate        | Moderate      |

## 6. Solved Numerical Problem

**Problem:** A computer system has:

- Main memory: 4 GB ($n = 32$ bits)
- Cache: 16 KB with 64-byte blocks
- Determine tag, index, and offset bits for:
  (a) Direct-mapped cache with 256 lines
  (b) 4-way set-associative cache

**Solution:**

Given: Block size = 64 bytes $\Rightarrow m = \log_2(64) = 6$ bits

**(a) Direct-mapped with 256 lines:**

- Number of lines = $256 = 2^8 \Rightarrow k = 8$ bits
- Tag bits = $32 - 8 - 6 = 18$ bits

**(b) 4-way set-associative:**

- Total lines = 16 KB / 64 B = 256 lines
- Sets = $256 / 4 = 64 = 2^6 \Rightarrow s = 6$ bits
- Tag bits = $32 - 6 - 6 = 20$ bits

## 7. Assessment Questions

**Question 1:** A 32-bit address system has a 4 KB cache with 64-byte blocks organized as 4-way set-associative. Determine the tag, index, and offset bit widths.

**Question 2:** In a direct-mapped cache with 1024 lines, blocks 0, 1024, and 2048 are accessed sequentially in a loop. Calculate the hit ratio after 3 accesses and explain the phenomenon observed.

**Question 3:** Prove that for a cache of capacity $C$ with block size $B$, the number of cache lines is $C/B$, and show how this relationship derives from the address field decomposition.
