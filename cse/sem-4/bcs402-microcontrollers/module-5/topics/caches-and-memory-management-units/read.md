# Caches and Memory Management Units

## Introduction

Cache memory and Memory Management Units (MMU) constitute fundamental components in modern computing architectures, bridging the performance gap between high-speed processors and relatively slow main memory. In the context of ARM-based microcontroller systems, particularly those utilizing the Advanced Microcontroller Bus Architecture (AMBA), understanding these components is essential for developing optimized firmware and appreciating the architectural complexities of contemporary embedded systems.

This chapter provides a comprehensive treatment of cache memory organization, operation, and performance analysis, alongside detailed coverage of the Memory Management Unit and its integration with Coprocessor 15 (CP15) in ARM processors. The material is structured to equip students with both theoretical foundations and practical analytical skills necessary for embedded systems development.

## Cache Memory Fundamentals

### The Memory Wall Problem and Cache Need

Modern processors execute instructions in nanosecond timescales, while main memory access requires hundreds of nanoseconds. This disparity, termed the "memory wall," creates a significant bottleneck. Consider a processor operating at 100 MHz with a single-cycle instruction time (10 ns), accessing DRAM with a 100 ns access time. Without intermediate storage, the processor would spend approximately 90% of its time waiting for memory operations to complete.

Cache memory resolves this mismatch by exploiting two fundamental program characteristics:

1. **Temporal Locality**: Recently accessed memory locations are likely to be accessed again in the near future
2. **Spatial Locality**: Memory locations adjacent to recently accessed locations are likely to be accessed soon

A cache hit eliminates the need to access main memory, reducing effective access time from $T_{memory}$ to $T_{cache}$, typically a 5-10x improvement.

### Cache Organization and Structure

**Three-Part Cache Architecture**

The cache subsystem comprises three interconnected components:

1. **Cache Controller**: Finite state machine managing all cache operations including hit/miss detection, line fills, evictions, and write handling
2. **Cache Memory Array**: High-speed SRAM storing actual data and instruction bytes (typically 4-64 KB in microcontrollers)
3. **Tag Memory**: Associative storage maintaining address information for each cache line

**Cache Line Structure**

A fundamental cache line (also called cache block) contains:

| Field     | Bits        | Purpose                                     |
| --------- | ----------- | ------------------------------------------- |
| Valid Bit | 1           | Indicates line contains valid data          |
| Dirty Bit | 1           | Indicates modified data (write-back)        |
| Tag       | N bits      | Upper address bits identifying memory block |
| Data      | 32-64 bytes | Actual cached memory contents               |

The cache line size represents a critical design parameter. Larger lines exploit spatial locality effectively but increase miss penalty and reduce the number of lines in a fixed-capacity cache.

### Cache Mapping Techniques

**Direct Mapping**

In direct-mapped cache organization, each main memory block maps to exactly one cache line determined by the index field:

$$Index = (Block\ Address) \ mod \ (Number\ of\ Lines)$$

**Advantages**:

- Simple hardware implementation using comparators
- Predictable access time (single tag comparison)
- Lower area and power overhead

**Disadvantages**:

- Fixed mapping causes conflict misses when multiple frequently-used blocks map to the same line
- Thrashing can significantly degrade performance

**Example**: For a 16 KB direct-mapped cache with 32-byte lines:

- Number of lines = 16KB / 32 = 512 lines
- Index bits = log₂(512) = 9 bits
- Block offset = log₂(32) = 5 bits
- For a 32-bit address: Tag = 32 - 9 - 5 = 18 bits

**Fully Associative Mapping**

Any memory block can occupy any cache line. Tag comparison requires parallel hardware (content-addressable memory or CAM):

**Advantages**:

- Maximum flexibility eliminates conflict misses
- Any line can hold any block

**Disadvantages**:

- Hardware complexity: N comparators required for N lines
- Increased latency and power consumption
- Impractical for large caches

**Set-Associative Mapping**

This approach represents the predominant industry implementation, combining direct-mapped efficiency with associativity benefits:

- Cache divided into $S$ sets, each containing $W$ ways (lines)
- Set index determined by address: $Set = (Block\ Address) \ mod \ S$
- Within a set, any of the $W$ ways can store the block

$$Total\ Lines = Sets \times Ways$$
$$Sets = \frac{Cache\ Size}{Line\ Size \times Ways}$$

**Common Configurations**:

- 2-way set-associative: Good compromise for embedded applications
- 4-way set-associative: Common in Cortex-A processors
- 8-way set-associative: Used in high-performance designs

The tag comparison reduces from $W$ parallel comparisons in fully-associative to checking only within the selected set.

## Cache Operations and Policies

### Write Policies

**Write-Through Protocol**

On a write hit, data updates both cache and main memory simultaneously:

```
if (cache_hit) {
    cache[line] = data;
    memory[address] = data;
}
```

**Characteristics**:

- Simple coherence maintenance
- Memory always reflects current processor state
- Higher memory bandwidth consumption
- Write buffer hides memory latency partially

**Write-Back Protocol**

On a write hit, data writes only to cache, with memory updated upon line eviction:

```
if (cache_hit) {
    cache[line] = data;
    dirty[line] = 1;
}
```

**Dirty Bit Handling**:

- On eviction: if dirty bit set, write cache line to memory before loading new block
- Reduces memory traffic significantly for write-intensive workloads

**Write Miss Policies**:

1. **Write Allocate**: Load block into cache after writing to memory (predicts future hits)
2. **No Write Allocate**: Write directly to memory, bypass cache

### Replacement Policies

When a cache miss occurs and the set has no invalid lines, a replacement policy determines which line to evict:

**1. Least Recently Used (LRU)**

- Evicts the line not accessed for the longest time
- Most effective for temporal locality
- Implementation: Counter per set tracking access history

**2. First-In-First-Out (FIFO)**

- Evicts oldest line regardless of access pattern
- Simple hardware: timestamp or queue structure

**3. Random Replacement**

- Evicts random line
- No hardware overhead
- Acceptable performance in practice

**Example - 2-Way LRU Implementation**:

For a 2-way set-associative cache, LRU can be tracked with a single bit per set:

- Bit = 0: Way 0 recently used
- Bit = 1: Way 1 recently used
- On access to Way 0: set bit = 1
- On eviction: replace the way not indicated by the bit

### Cache Coherence in Multi-Core Systems

Multi-core microcontrollers require coherent memory views across cores. The MESI protocol (Modified, Exclusive, Shared, Invalid) manages this:

| State     | Description                             |
| --------- | --------------------------------------- |
| Modified  | Line held exclusively, dirty (modified) |
| Exclusive | Line held exclusively, clean            |
| Shared    | Line potentially shared, clean          |
| Invalid   | Line not present in cache               |

**State Transitions** (simplified):

- Read miss → busRd → other caches respond or memory supplies data
- Write to shared line → busRdX → other caches invalidate copies
- Write to exclusive line → no bus transaction needed

## Cache Performance Analysis

### Fundamental Metrics

**Hit Rate ($h$)**: Fraction of memory accesses satisfied by cache
$$h = \frac{Hits}{Total\ Accesses}$$

**Miss Rate ($m$)**: $m = 1 - h$

**Hit Time ($T_h$)**: Time to access cache on hit (typically 1-2 processor cycles)

**Miss Penalty ($P$)**: Additional cycles required on miss to fetch from memory

### Average Memory Access Time (AMAT)

The fundamental performance equation:

$$AMAT = T_h + m \times P$$

**Proof Derivation**:

For $N$ memory accesses:

- $hN$ accesses take $T_h$ cycles each
- $mN$ accesses take $T_h + P$ cycles each (cache access plus penalty)

$$Total\ Cycles = hN \times T_h + mN \times (T_h + P)$$
$$Average = \frac{Total\ Cycles}{N} = hT_h + m(T_h + P)$$
$$= hT_h + mT_h + mP = T_h(h+m) + mP = T_h + mP$$

**Extended AMAT Formula** (with write buffer):

For write-through with write buffer:
$$AMAT_{wt} = T_h + m_w \times (P_{wb} + m_r \times P)$$

Where $m_w$ is write miss rate, $m_r$ is read miss rate, $P_{wb}$ is write buffer latency.

### Worked Numerical Examples

**Example 1: Direct-Mapped Cache Performance**

Given:

- Cache hit time: 1 cycle
- Miss penalty: 20 cycles
- Hit rate: 94%

Calculate AMAT:
$$AMAT = 1 + (1 - 0.94) \times 20 = 1 + 0.06 \times 20 = 2.2\ cycles$$

**Example 2: Set-Associative Cache Comparison**

Compare 1-way (direct-mapped) vs 4-way set-associative:

| Configuration | Hit Rate | Hit Time | Miss Penalty |
| ------------- | -------- | -------- | ------------ |
| 1-way         | 85%      | 1 cycle  | 20 cycles    |
| 4-way         | 94%      | 2 cycles | 20 cycles    |

AMAT (1-way): $1 + 0.15 \times 20 = 4.0$ cycles
AMAT (4-way): $2 + 0.06 \times 20 = 3.2$ cycles

The 4-way set-associative is 20% faster despite higher hit time due to significantly improved hit rate.

**Example 3: Multi-level Cache**

Given L1: 1 cycle hit, 5% miss; L2: 10 cycle hit, 20% L1 miss rate:
$$AMAT = 1 + 0.05 \times (10 + 0.20 \times 100) = 1 + 0.05 \times 30 = 2.5\ cycles$$

### Cache Conflict Analysis

**Conflict Miss Demonstration**:

For a 4 KB direct-mapped cache with 32-byte lines (128 lines):

- Consider two 4 KB memory regions at addresses 0x0000 and 0x1000
- Both map to cache lines 0-127
- Alternating access causes thrashing

Simulation: Access pattern A[0], B[0], A[1], B[1] with 4-slot cache:

- Without spatial locality: 100% miss rate
- With spatial locality (accessing full lines): reduces to ~50%

## Coprocessor 15 (CP15) - System Control Coprocessor

### Overview and Purpose

Coprocessor 15 (CP15) provides system control functions in ARM processors, including cache configuration, MMU control, and performance monitoring. All ARM microcontrollers with cache/MMU implement CP15 registers for software configuration.

### Key CP15 Registers for Cache/MMU Control

**c0 - ID Code and Cache Type Registers**:

| Register | Function                                          |
| -------- | ------------------------------------------------- |
| MIDR     | Main ID Register - processor identification       |
| CTR      | Cache Type Register - cache geometry and policies |
| TCMTR    | TCM Type Register                                 |
| ID_PFR   | Processor Feature Register                        |

**c1 - System Control Register**:

| Bit    | Function                 |
| ------ | ------------------------ |
| M (0)  | MMU enable               |
| A (1)  | Alignment fault enable   |
| C (2)  | Data cache enable        |
| I (3)  | Instruction cache enable |
| Z (24) | Branch prediction enable |

**c7 - Cache and TLB Operations**:

| Register | Function                         |
| -------- | -------------------------------- |
| c7, cr0  | Invalidate all instruction cache |
| c7, cr1  | Invalidate entire data cache     |
| c7, cr5  | Invalidate instruction TLB       |
| c7, cr6  | Invalidate data TLB              |
| c7, cr10 | Clean and invalidate data cache  |

**c9 - Cache Lockdown Registers**:

Enables locking critical code/data into cache:

- Way lockdown: lock specific ways
- L1 data cache lockdown

**c13 - Context ID Register**:

Process identifier for ASID (Address Space Identifier) in virtual memory.

### Cache Configuration Sequence

Typical initialization sequence for ARM Cortex-A with MMU:

```
// Enable caches
MRC p15, 0, r0, c1, c0, 0    // Read SCTLR
ORR r0, r0, #(1<<2)         // Enable C (data cache)
ORR r0, r0, #(1<<12)        // Enable I (instruction cache)
MCR p15, 0, r0, c1, c0, 0    // Write SCTLR

// Invalidate caches
MOV r0, #0
MCR p15, 0, r0, c7, c5, 0    // Invalidate instruction cache
MCR p15, 0, r0, c7, c6, 0    // Invalidate data cache
```

## Memory Management Unit (MMU)

### MMU Architecture and Functions

The Memory Management Unit provides three critical functions in ARM processors:

1. **Virtual Address Translation**: Converting software-generated virtual addresses to physical memory addresses
2. **Memory Protection**: Preventing unauthorized access through permission bits
3. **Access Control**: Implementing privilege levels (user/kernel separation)

### Virtual Address Translation

**Translation Lookaside Buffer (TLB)**:

The TLB is a specialized cache storing recent virtual-to-physical address translations. Structure:

| Field               | Description                          |
| ------------------- | ------------------------------------ |
| Virtual Address Tag | VPN (Virtual Page Number)            |
| Physical Address    | PPN (Physical Page Number)           |
| Attributes          | Permissions, cacheability, valid bit |

**TLB Lookup Process**:

```
1. Extract VPN from virtual address
2. Check TLB for matching tag
3. If hit: combine with offset for physical address
4. If miss: walk page tables, load translation into TLB
```

TLB miss penalty: typically 10-30 cycles for page table walk.

**Page Table Walk (First-Level)**:

For ARM Cortex-A with 4KB pages:

- Virtual address: [31:20] = Section/Page table index, [19:12] = Second-level index, [11:0] = offset
- First-level descriptor contains either:
  - Coarse second-level table pointer (for 1MB sections)
  - Fine second-level table pointer (for 1MB, 64KB, 4KB pages)

### Page Table Structure

**First-Level Descriptor Format**:

| Bits    | Field    | Description                                                                  |
| ------- | -------- | ---------------------------------------------------------------------------- |
| [1:0]   | Type     | 00 = fault, 01 = coarse page table, 10 = section (1MB), 11 = fine page table |
| [4:2]   | AP       | Access Permissions                                                           |
| [8]     | Domain   | 16 possible domains                                                          |
| [9]     | P        | Present bit                                                                  |
| [18:10] | Reserved | -                                                                            |
| [31:20] | Base     | Physical base address (section) or table base                                |

**Second-Level Descriptor (4KB Pages)**:

| Bits    | Field     | Description                                                               |
| ------- | --------- | ------------------------------------------------------------------------- |
| [1:0]   | Type      | 00 = fault, 01 = large page (64KB), 10 = small page (4KB), 11 = tiny page |
| [5:2]   | APX, AP   | Access permissions                                                        |
| [6]     | C         | Cacheable                                                                 |
| [7]     | B         | Bufferable                                                                |
| [11:8]  | Domain    | Ownership domain                                                          |
| [31:12] | Page Base | Physical page address                                                     |

### Memory Regions and Attributes

ARM defines memory regions with distinct attributes:

| Region           | Characteristics              |
| ---------------- | ---------------------------- |
| Strongly Ordered | No caching, strict ordering  |
| Device           | Memory-mapped peripherals    |
| Normal           | Cacheable, shareable options |

**Cacheability Bits**:

- C (bit 3): Data cacheable
- B (bit 2): Write bufferable
- For instruction: I (bit 12) in SCTLR

### Access Permissions

AP (Access Permission) bits in page tables:

| AP[2:0] | Privileged    | User       |
| ------- | ------------- | ---------- |
| 000     | No access     | No access  |
| 001     | Read/Write    | No access  |
| 010     | Read/Write    | Read-only  |
| 011     | Read/Write    | Read/Write |
| 100     | Unpredictable | Read-only  |
| 101     | Read-only     | Read-only  |
| 110     | Read-only     | Read-only  |
| 111     | Read-only     | Read-only  |

### TLB Management Operations

**TLB Invalidation**:

```assembly
; Invalidate entire TLB
MCR p15, 0, r0, c8, c7, 0

; Invalidate instruction TLB
MCR p15, 0, r0, c8, c5, 0

; Invalidate data TLB
MCR p15, 0, r0, c8, c6, 0
```

Context switch requires TLB flush or ASID management to prevent address space leakage.

## Integration in Microcontroller Systems

### ARM Cortex-M7 Cache Configuration

Cortex-M7 features optional separate L1 caches:

- 4-way set-associative instruction cache (I-Cache): 4-64 KB
- 4-way set-associative data cache (D-Cache): 4-64 KB

Configuration via CP15:

```
; Enable D-Cache
MRC p15, 0, r0, c1, c0, 0
ORR r0, r0, #(1 << 2)
MCR p15, 0, r0, c1, c0, 0

; Enable I-Cache
MRC p15, 0, r0, c1, c0, 0
ORR r0, r0, #(1 << 12)
MCR p15, 0, r0, c1, c0, 0
```

### Cache and MMU Interaction

The interaction between cache and MMU follows the structure:

```
Virtual Address → MMU Translation → Physical Address → Cache Lookup
```

**Memory Ordering Considerations**:

- Virtual indexing, physical tagging (VIPT) challenges
- aliasing: same physical address mapped to different virtual addresses -解决: cache coloring, ASID tagging

### Performance Optimization Strategies

1. **Cache Lockdown**: Lock frequently-accessed code/data
2. **Memory Alignment**: Prevent cache line splits
3. **Prefetching**: Hardware/software prefetch for sequential access
4. **Data Organization**: Structure data for cache friendliness

---

## Summary

This chapter examined the fundamental concepts of cache memory and Memory Management Units in ARM-based microcontroller systems. Cache memory addresses the processor-memory speed disparity through hierarchical storage exploiting temporal and spatial locality. The three primary mapping techniques—direct-mapped, fully-associative, and set-associative—represent trade-offs between hardware complexity and hit rate optimization. Write policies (write-through versus write-back) and replacement algorithms (LRU, FIFO, Random) significantly impact cache performance, with AMAT serving as the fundamental analytical metric.

Coprocessor 15 provides essential system control functions in ARM processors, with specific registers enabling cache configuration, invalidation operations, and system control. The MMU implements virtual memory through address translation via TLBs and page tables, with configurable access permissions providing memory protection. Understanding these components enables embedded systems developers to optimize memory access patterns and implement secure, efficient firmware for modern microcontroller applications.
