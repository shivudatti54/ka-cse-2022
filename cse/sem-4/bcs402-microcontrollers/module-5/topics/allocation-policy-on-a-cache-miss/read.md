# Cache Miss Allocation Policy

## Introduction

Cache memory constitutes a fundamental component of modern computer architectures, functioning as a high-speed buffering layer between the CPU and main memory. The efficacy of this memory hierarchy directly impacts overall system performance, particularly in resource-constrained embedded systems employing ARM-based microcontrollers. When the processor requests data, the cache hierarchy is consulted sequentially; a **cache hit** occurs when the requested data resides in the cache, enabling access with minimal latency. Conversely, a **cache miss** necessitates fetching the data from the slower main memory, incurring substantial performance penalties.

The **allocation policy on a cache miss** governs the fundamental decision of whether and how newly fetched data blocks from main memory are incorporated into the cache structure. This policy operates in conjunction with write policies (write-through versus write-back) and replacement algorithms (LRU, FIFO, Random) to determine cache behavior. In ARM-based microcontroller systems, Coprocessor 15 (CP15) provides architectural mechanisms for configuring cache allocation behaviors, making comprehensive understanding of these policies essential for embedded systems designers.

This content addresses the BCS402 Microcontrollers course requirements, specifically connecting to CP15 cache configuration registers and practical implementation considerations in ARM embedded systems.

## Theoretical Foundation

### Cache Miss Taxonomy

Understanding allocation policies requires precise classification of cache miss types, as each category presents distinct optimization challenges:

**Definition 1 (Compulsory Miss)**: A compulsory miss, also termed a cold miss, occurs when a memory block is accessed for the first time since system initialization. Formally, if $B$ represents the set of memory blocks and $C$ represents cache contents, a compulsory miss occurs when $b \in B$ is accessed and $b \notin C$ at time $t=0$ (cache initialization). These misses are architecturally inevitable and constitute the minimum miss rate, denoted as $M_{compulsory}$.

**Definition 2 (Capacity Miss)**: A capacity miss arises when the cache cannot retain all recently accessed blocks due to finite storage capacity. If $S_c$ represents cache capacity in bytes and $W$ represents the working set size, a capacity miss occurs when $W > S_c$. The miss rate $M_{capacity}$ increases monotonically as $S_c$ decreases.

**Definition 3 (Conflict Miss)**: In set-associative and direct-mapped configurations, conflict misses occur when multiple memory blocks compete for the same cache set. For a $k$-way set-associative cache with $S$ sets, the miss rate $M_{conflict}$ depends on the degree of set conflict, formally: a conflict miss occurs when block $b_i$ and $b_j$ map to the same set $s$, where $s = f(b_i) = f(b_j)$ and $i \neq j$.

### Average Memory Access Time Analysis

The allocation policy fundamentally influences the **Average Memory Access Time (AMAT)**, a critical performance metric:

$$AMAT = t_{hit} + M \times t_{miss}$$

Where:

- $t_{hit}$ = cache hit latency
- $M$ = miss rate (fraction of accesses resulting in misses)
- $t_{miss}$ = miss penalty (additional latency on cache miss)

**Theorem 1**: For a cache with fetch-on-miss allocation policy, the effective miss penalty $t_{miss}^{eff}$ is given by:

$$t_{miss}^{eff} = t_{memory} + t_{transfer} + t_{allocation}$$

Where $t_{memory}$ represents main memory access latency, $t_{transfer}$ denotes block transfer time ($t_{transfer} = B \times t_{bus}$, where $B$ is block size in words and $t_{bus}$ is bus transfer time per word), and $t_{allocation}$ represents cache controller overhead for tag verification and line allocation.

**Proof**: Consider a memory access sequence where a miss occurs. The CPU must: (1) detect the miss via tag comparison, (2) arbitrate for bus ownership, (3) issue main memory read, (4) receive data block, (5) allocate cache line, (6) update tag and status bits, and (7) deliver data to CPU. Summing these sequential operations yields the effective miss penalty. $\square$

## Cache Miss Allocation Policies

### Policy 1: Fetch-on-Miss (Allocate on Miss)

The **fetch-on-miss** policy, alternatively termed **allocate-on-miss**, mandates that upon a cache miss, the requested data block is retrieved from main memory and stored in the cache before the processor receives the data. This policy represents the predominant allocation strategy in contemporary processor architectures.

**Formal Definition**: Let $A$ denote the address requested by the CPU, and let $B(A)$ represent the corresponding memory block. Upon a cache miss, fetch-on-miss requires:

$$\text{Allocate}(B(A)) \implies B(A) \in C_{new}$$

Where $C_{new}$ represents the post-allocation cache state.

**Algorithmic Representation**:

```
1. CPU generates memory request for address A
2. Cache tag lookup performed
3. IF (hit) THEN
 Return data from cache
 ELSE
 // Miss handling
 Fetch block B(A) from main memory
 Select victim block V (if cache full)
 IF (victim V is dirty AND write-back) THEN
 Write V back to main memory
 Allocate B(A) in freed cache line
 Update tag array and status bits (valid, dirty)
 Return data to CPU
```

**Performance Analysis**: Fetch-on-miss exploits temporal locality by retaining accessed blocks in cache. The hit ratio improvement is quantified by:

$$H_{new} = H_{old} + (1 - H_{old}) \times \alpha$$

Where $\alpha$ represents the probability of re-accessing the fetched block, dependent on program locality characteristics.

**Advantages**:

- Exploits temporal locality effectively
- Reduces subsequent access latency for repeated references
- Simplifies memory consistency management

**Disadvantages**:

- Introduces initial access latency (fetch + allocate before delivery)
- Potential cache pollution when fetched data exhibits low temporal reuse
- Increased memory bandwidth consumption

### Policy 2: Write-Allocate (Fetch-on-Miss for Writes)

The **write-allocate** policy specifically governs write miss handling, stipulating that the target block must be fetched into the cache before the write operation modifies the data. This policy necessarily combines with write-through or write-back mechanisms.

**Definition 4 (Write-Allocate)**: For a write operation to address $A$ resulting in a cache miss, write-allocate requires:

$$\text{WriteMiss}(A) \implies \text{Fetch}(B(A)) \land \text{Allocate}(B(A)) \land \text{Modify}(B(A))$$

**Interaction with Write Policies**:

| Allocation Policy | Write Policy  | Behavior on Write Miss                                        |
| ----------------- | ------------- | ------------------------------------------------------------- |
| Write-Allocate    | Write-Through | Fetch block, modify cache, write-through to memory            |
| Write-Allocate    | Write-Back    | Fetch block, modify cache, set dirty bit, defer memory update |
| No-Write-Allocate | Write-Through | Write directly to memory, do not cache                        |
| No-Write-Allocate | Write-Back    | Write directly to memory, do not cache                        |

**CP15 Configuration**: In ARM architectures, the System Control Register (SCTLR) bit [12] (I bit) controls instruction cache enable, while bit [2] (C bit) controls data cache enable. The Cache Type Registers (CTR) provide information about cache geometry and allocation policies supported by the implementation.

### Policy 3: No-Allocate (Write-Around)

The **no-allocate** policy, equivalently termed **write-around**, prevents block allocation on write misses. Data is written directly to main memory without cache incorporation.

**Formal Definition**: For a write miss on address $A$:

$$\text{WriteMiss}(A) \implies \text{Write}(A) \to \text{Memory} \land A \notin C$$

**Algorithmic Representation**:

```
1. CPU generates write request for address A
2. Cache tag lookup performed
3. IF (hit) THEN
 Modify data in cache line
 IF (write-through) THEN Write to main memory
 Set dirty bit (if write-back)
 ELSE
 // Miss handling with no-allocate
 Write data directly to main memory
 DO NOT allocate block in cache
 Continue without cache update
```

**Performance Implications**: No-allocate prevents cache pollution from write-intensive streams but forfeits potential read hits on recently written data. The trade-off is quantified by:

$$AMAT_{no-alloc} = t_{hit} + M_w \times t_{memory} + M_r \times t_{miss}^{read}$$

Where $M_w$ and $M_r$ represent write and read miss rates respectively.

## Placement and Replacement Policies

### Cache Placement Strategies

The allocation policy operates in conjunction with placement policies determining valid cache locations:

**Direct-Mapping**: Each memory block $B$ maps to exactly one cache line $L$:

$$L = f(B) = (B \mod N)$$

Where $N$ represents the number of cache lines.

**Set-Associative**: Cache is organized into $S$ sets, each containing $k$ ways:

$$S = (B \mod S_{count})$$

Block $B$ may occupy any way within set $S$.

**Fully-Associative**: Any memory block may reside in any cache line:

$$L \in \{0, 1, 2, ..., N-1\} \text{ (any line available)}$$

### Victim Selection (Replacement Algorithms)

When cache allocation is required but all ways within the target set are occupied, a victim block must be evicted:

**LRU (Least Recently Used)**: Evicts the block with the earliest last-access timestamp:
$$V_{LRU} = \arg\min_{b \in S} \{t_{last}(b)\}$$

**FIFO (First In First Out)**: Evicts the oldest allocated block regardless of access pattern:
$$V_{FIFO} = \arg\min_{b \in S} \{t_{alloc}(b)\}$$

**LFU (Least Frequently Used)**: Evicts the block with lowest access frequency count:
$$V_{LFU} = \arg\min_{b \in S} \{f_{access}(b)\}$$

**Random**: Probabilistically selects victim:
$$P(V_i) = \frac{1}{k} \text{ for each way } i \text{ in set}$$

## Numerical Examples

### Example 1: Hit Ratio Calculation with Fetch-on-Miss

Consider a 4KB direct-mapped cache with 16-byte blocks. The processor executes a loop accessing 64 bytes of data sequentially.

**Given**:

- Cache capacity: 4KB = 4096 bytes
- Block size: 16 bytes
- Number of cache lines: 4096/16 = 256 lines
- Working set: 64 bytes (4 blocks)
- Access pattern: Sequential reads, loop repeated 100 times

**Solution**:

The mapping function for direct-mapped cache:
$$\text{Line} = \left\lfloor \frac{\text{Address}}{\text{BlockSize}} \right\rfloor \mod 256$$

For 64-byte working set (blocks 0, 1, 2, 3):

- Block 0 → Line 0
- Block 1 → Line 1
- Block 2 → Line 2
- Block 3 → Line 3

Since all 4 blocks map to distinct lines, there is no conflict.

**First iteration**: 4 misses (one per unique block)
**Subsequent 99 iterations**: 4 hits per iteration (all blocks in cache)

Total accesses = 4 × 100 = 400
Total misses = 4 (only first iteration)
Hit ratio = 396/400 = 0.99 = 99%

### Example 2: AMAT Comparison for Allocation Policies

**Given**:

- Cache hit time ($t_{hit}$): 1 cycle
- Miss rate ($M$): 5% = 0.05
- Memory access time: 100 cycles
- Cache allocation overhead: 5 cycles
- Block transfer time: 20 cycles

**Calculate AMAT for fetch-on-miss and no-allocate policies**:

**Fetch-on-Miss**:
$$t_{miss}^{FM} = 100 + 20 + 5 = 125 \text{ cycles}$$
$$AMAT_{FM} = 1 + 0.05 \times 125 = 1 + 6.25 = 7.25 \text{ cycles}$$

**No-Allocate** (assuming write-intensive workload with 80% writes):

- On write miss: Direct memory write = 100 cycles (no cache overhead)
- On read miss: Fetch from memory = 125 cycles (same as fetch-on-miss)

Effective miss penalty:
$$t_{miss}^{NA} = 0.8 \times 100 + 0.2 \times 125 = 80 + 25 = 105 \text{ cycles}$$
$$AMAT_{NA} = 1 + 0.05 \times 105 = 1 + 5.25 = 6.25 \text{ cycles}$$

**Conclusion**: For write-intensive workloads, no-allocate demonstrates superior AMAT due to reduced allocation overhead on writes.

## ARM Coprocessor 15 Integration

In ARM-based microcontroller systems, Coprocessor 15 (CP15) provides system control functionality including cache management. Key registers relevant to allocation policy configuration include:

**SCTLR (System Control Register)**:

- Bit [2]: C bit - Data cache enable
- Bit [12]: I bit - Instruction cache enable
- Bit [4]: WB bit - Write buffer enable

**CTR (Cache Type Register)**: Provides cache geometry information including:

- Cache line size
- Associativity
- Number of sets

**CCSIDR (Cache Size ID Registers)**: Specifies the size, associativity, and line length for each cache level.

Software can query these registers to determine supported allocation policies and configure cache behavior appropriately for specific application requirements.

## Summary

Cache miss allocation policies fundamentally determine how fetched data enters the cache hierarchy. The **fetch-on-miss** policy prioritizes temporal locality by always allocating fetched blocks, suitable for read-dominated workloads. **Write-allocate** extends this to write operations, enabling subsequent reads to hit in cache. **No-allocate** (write-around) bypasses cache on write misses, reducing pollution for write-intensive streams. Selection among these policies requires careful analysis of workload characteristics, with AMAT modeling providing quantitative guidance. In ARM microcontrollers, CP15 registers enable runtime configuration of these behaviors, facilitating adaptive cache management strategies.
