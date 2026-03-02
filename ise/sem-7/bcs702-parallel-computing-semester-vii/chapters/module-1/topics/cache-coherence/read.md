# Cache Coherence in Parallel Programming

## Introduction to Cache Coherence

In parallel computing systems with multiple processors, each processor typically has its own local cache memory to reduce memory access latency and improve performance. However, this introduces a critical problem: **cache coherence**. Cache coherence refers to the consistency of data stored in multiple local caches for a shared resource. When multiple processors can cache copies of the same memory location, inconsistent views of memory can occur if one processor updates its cached copy without updating other copies.

The cache coherence problem arises because modern computer systems maintain multiple copies of data in different caches. Without a mechanism to ensure coherence, different processors might see different values for the same memory location, leading to incorrect program behavior.

## Why Cache Coherence Matters

Consider a simple scenario with two processors (P1 and P2) sharing a variable X in main memory:
1. Both P1 and P2 read X into their local caches (value = 5)
2. P1 updates X to 10 in its cache
3. P2 reads X from its cache (still value = 5)

This inconsistency creates a serious problem for parallel programs that rely on shared data. Cache coherence protocols ensure that all processors see a consistent view of memory by managing how cached copies are updated and invalidated.

## Cache Coherence Protocols

### Write-Through Protocol
In write-through, every write to cache also writes to main memory immediately. This ensures main memory always has the most recent value, but generates high memory traffic.

```
Processor → Cache → Main Memory (simultaneously)
```

### Write-Back Protocol
In write-back, writes only update the cache. The main memory is updated only when the cache line is evicted or explicitly written back. This reduces memory traffic but requires careful coherence management.

```
Processor → Cache → (Later) Main Memory
```

## Snooping-Based Cache Coherence

Snooping protocols use a broadcast-based approach where all cache controllers monitor (snoop) the shared bus for memory transactions. When a processor writes to a shared memory location, other caches see this activity and take appropriate action.

### Write-Invalidate Protocol
When a processor writes to a shared location, it invalidates all other copies in other caches. Subsequent reads by other processors will miss in their caches and fetch the updated value.

Example:
1. P1 and P2 both have cached copy of X
2. P1 writes to X → broadcast invalidate message
3. P2's cache marks its copy as invalid
4. P2 reads X → cache miss → fetches updated value from memory

### Write-Update Protocol
When a processor writes to a shared location, it updates all other copies in real-time. This keeps all caches current but generates more bus traffic.

```
P1 writes X=10 → Broadcast update: X=10 to all caches
P2's cache immediately updates its copy to 10
```

### Comparison of Snooping Protocols

| Protocol | Bus Traffic | Read Latency | Implementation Complexity |
|----------|-------------|--------------|---------------------------|
| Write-Invalidate | Lower | Higher after writes | Simpler |
| Write-Update | Higher | Lower | More complex |

## Directory-Based Cache Coherence

For larger systems with many processors, snooping becomes inefficient due to bus contention. Directory-based protocols use a central directory that tracks which caches have copies of each memory block.

### Basic Operation
1. Directory maintains state for each memory block (shared, exclusive, etc.)
2. Before a write, the processor checks the directory
3. Directory sends invalidation or update messages to relevant caches only
4. Directory updates state information

```
Memory Block X: [Owner: P1, Sharers: P2, P3]
P4 wants to write X → Directory sends invalidate to P1, P2, P3
Directory updates: [Owner: P4, Sharers: none]
```

### Directory States
- **Uncached**: No cache has a copy
- **Shared**: One or more caches have read-only copies
- **Exclusive**: One cache has read-write copy (dirty)
- **Owned**: Similar to exclusive but with additional responsibilities

## MESI Protocol

The MESI protocol is a widely used write-invalidate protocol with four states:

### MESI States
- **Modified (M)**: The cache line is dirty (different from main memory) and is the only copy
- **Exclusive (E)**: The cache line is clean (matches main memory) and is the only copy
- **Shared (S)**: The cache line is clean and may exist in other caches
- **Invalid (I)**: The cache line is not valid

### State Transitions
```
Processor Read:
  If Invalid → fetch from memory, state becomes Exclusive or Shared
  If Shared/Exclusive/Modified → use cached copy

Processor Write:
  If Exclusive/Modified → update locally, state becomes Modified
  If Shared → send invalidations to other caches, state becomes Modified
  If Invalid → fetch ownership, then update

Other Processor Access:
  If Modified → write back to memory, state changes based on request type
```

ASCII Diagram of MESI State Transitions:
```
      +-----------+
      | Invalid   |<----------------+
      +-----------+                 |
        |     ^                     |
        |     |                     |
        v     |                     |
+-----------+ |      +-----------+  |
| Shared    |------->| Exclusive |--+
+-----------+        +-----------+
        |                 |
        |                 |
        v                 v
+-----------+        +-----------+
| Modified  |<-------|           |
+-----------+        +-----------+
```

## False Sharing

False sharing occurs when multiple processors access different variables that happen to reside on the same cache line. Even though the variables are unrelated, the cache coherence protocol treats them as the same memory location, causing unnecessary invalidations and performance degradation.

Example:
```cpp
struct {
    int x; // Accessed by P1
    int y; // Accessed by P2
} data;
```
If x and y are on the same cache line, writing to x will invalidate the cache line in P2's cache, even though P2 only accesses y.

Solution: Padding or aligning variables to separate cache lines.

## Performance Implications

Cache coherence protocols introduce overhead in terms of:
- Additional bus/memory traffic for coherence messages
- Latency for synchronization operations
- Complexity in hardware implementation

The performance impact depends on:
- **Sharing pattern**: How frequently shared data is accessed/written
- **Protocol choice**: Write-invalidate vs write-update
- **System size**: Number of processors sharing data

## Exam Tips

1. **Understand the difference between write-through and write-back caching** and how each affects coherence protocols.
2. **Be able to trace through MESI state transitions** for given read/write patterns.
3. **Recognize false sharing scenarios** and suggest solutions.
4. **Compare snooping vs directory-based protocols** and when each is appropriate.
5. **Calculate performance impact** of coherence overhead for given access patterns.
6. **Remember that coherence protocols only solve the cache coherence problem** - they don't solve higher-level synchronization issues like race conditions.