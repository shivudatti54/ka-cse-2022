# Cache Memory

## Introduction to Cache

Cache memory is a small, fast memory that stores frequently accessed data to reduce average memory access time. It acts as a buffer between the CPU and main memory, exploiting the principle of locality.

## Cache Organization Basics

### Cache Line (Block)

The basic unit of data transfer between cache and main memory. Typical sizes: 32, 64, or 128 bytes.

```
Cache Line Structure:
+-------+-------+------------------+
| Valid | Tag   |   Data Block     |
| Bit   |       | (32-128 bytes)   |
+-------+-------+------------------+
```

### Address Partitioning

Memory address is divided into three parts:

```
|<------- Tag ------->|<-- Index -->|<- Offset ->|
|       t bits        |   s bits    |   b bits   |

Example: 32-bit address, 64-byte line, 256 sets
- Offset: log2(64) = 6 bits
- Index: log2(256) = 8 bits
- Tag: 32 - 6 - 8 = 18 bits
```

## Cache Mapping Techniques

### 1. Direct Mapped Cache

Each memory block maps to exactly one cache line.

```
Cache Line = (Memory Block Address) mod (Number of Cache Lines)

Example: 8-line cache
Block 0, 8, 16, 24... -> Line 0
Block 1, 9, 17, 25... -> Line 1
...
```

**Advantages:**

- Simple hardware
- Fast access (single lookup)

**Disadvantages:**

- Conflict misses (ping-pong effect)
- Low flexibility

### 2. Fully Associative Cache

Any memory block can go in any cache line.

```
Search all lines in parallel using CAM (Content Addressable Memory)
```

**Advantages:**

- No conflict misses
- Maximum flexibility

**Disadvantages:**

- Expensive hardware (comparators for each line)
- Slower for large caches
- Complex replacement logic

### 3. Set-Associative Cache

Compromise between direct-mapped and fully associative.

```
n-way set associative:
- Cache divided into sets
- Each set has n lines
- Block maps to one set, can use any line in set

Cache Set = (Memory Block Address) mod (Number of Sets)
```

**Common configurations:**

- 2-way: Intel Pentium L1
- 4-way: Common L2 design
- 8-way: Modern L1/L2
- 16-way: Large L3 caches

## Cache Operations

### Read Operation

```
1. Extract index bits from address
2. Access the corresponding set
3. Compare tag with stored tags
4. If match (hit): return data
5. If no match (miss): fetch from lower level
```

### Write Policies

#### Write-Through

Write to both cache and memory immediately.

**Advantages:**

- Memory always consistent
- Simpler recovery

**Disadvantages:**

- Slower writes
- Higher memory traffic

#### Write-Back

Write only to cache; update memory on eviction.

**Advantages:**

- Faster writes
- Less memory traffic

**Disadvantages:**

- Memory may be stale
- Need dirty bit per line

### Write Miss Policies

#### Write-Allocate (Fetch-on-Write)

On write miss, fetch block to cache, then write.

- Typically paired with write-back

#### No-Write-Allocate (Write-Around)

On write miss, write directly to memory.

- Typically paired with write-through

## Replacement Policies

When cache is full, which line to replace?

### 1. LRU (Least Recently Used)

Replace the line not used for the longest time.

```
Access sequence: A, B, C, A, D (3-line cache)
After D: B is LRU, replaced with D
```

**Implementation:**

- Counters or pseudo-LRU for 4+ way
- Expensive for high associativity

### 2. FIFO (First-In-First-Out)

Replace the oldest line.

- Simpler than LRU
- Doesn't consider usage pattern

### 3. Random

Randomly select line to replace.

- Simplest implementation
- Surprisingly effective
- Used in some ARM processors

### 4. Pseudo-LRU (PLRU)

Approximation of LRU using tree structure.

- Used in 4/8-way caches
- Single bit per level

## Cache Performance

### Miss Types (3 Cs)

1. **Compulsory (Cold) Misses**: First access to a block
2. **Capacity Misses**: Cache cannot hold all needed blocks
3. **Conflict Misses**: Limited associativity causes replacement

### Miss Rate Calculation

```
Miss Rate = Number of Misses / Total Accesses
Hit Rate = 1 - Miss Rate

AMAT = Hit Time + Miss Rate × Miss Penalty
```

### Reducing Miss Rates

| Miss Type  | Solution                           |
| ---------- | ---------------------------------- |
| Compulsory | Prefetching, larger blocks         |
| Capacity   | Larger cache                       |
| Conflict   | Higher associativity, victim cache |

## Cache Parameters Summary

| Parameter     | Trade-off                                    |
| ------------- | -------------------------------------------- |
| Size          | Larger → higher hit rate, slower access      |
| Block Size    | Larger → better spatial locality, more waste |
| Associativity | Higher → fewer conflicts, slower access      |
| Write Policy  | Write-back faster but more complex           |

## Modern Cache Features

### Multi-Level Caches

- L1: Small, fast (1-4 cycles)
- L2: Medium (10-20 cycles)
- L3: Large, shared (30-50 cycles)

### Prefetching

- Hardware detects access patterns
- Fetches blocks before needed
- Stride prefetching for arrays

### Victim Cache

- Small fully-associative buffer
- Holds recently evicted lines
- Reduces conflict misses

## Summary

- Cache bridges speed gap between CPU and memory
- Three mapping types: direct, fully associative, set-associative
- Write policies: write-through vs write-back
- Replacement: LRU, FIFO, Random, PLRU
- Miss types: Compulsory, Capacity, Conflict
- Modern designs use multi-level caches with prefetching
