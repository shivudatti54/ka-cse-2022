# Cache Coherence in Parallel Programming

## 1. Introduction and Formal Definition

In shared-memory multiprocessor systems, each processor typically possesses private cache memory to reduce access latency and improve performance. However, this architectural optimization introduces a fundamental challenge known as **cache coherence**. Cache coherence refers to the property ensuring that all processors observe a consistent view of shared memory at any given instant.

Formally, a memory system is said to be coherent if it satisfies three axioms:

1. **Write Invariance**: If processor P writes a value V to location X, any subsequent read of X by P must return V.
2. **Write Serialization**: All writes to the same memory location appear to occur in some sequential order.
3. **Coherence Obligation**: If processor P1 writes V to location X, and processor P2 subsequently reads X, P2 must either observe V or a value written by P1 after the write.

These axioms ensure that shared data remains consistent across all processor views, preventing race conditions and ensuring program correctness in parallel execution.

## 2. The Cache Coherence Problem

Consider a dual-processor system (P1 and P2) sharing a variable X stored at memory location 0x1000:

```
Initial State: X = 5 stored in main memory

Step 1: P1 reads X → Cache₁ receives copy with value 5
Step 2: P2 reads X → Cache₂ receives copy with value 5
Step 3: P1 writes X = 10 → Cache₁ updates to 10, main memory still shows 5
Step 4: P2 reads X → Cache₂ returns stale value 5 (incoherent state)
```

This inconsistency arises because modern systems maintain multiple copies of the same memory location across different caches, requiring sophisticated protocols to maintain coherence.

## 3. Write Policies in Cache Memory

### 3.1 Write-Through Policy

In the write-through policy, every write operation updates both the cache and main memory simultaneously:

```
Processor Write → Cache Update → Main Memory Update (immediate)
```

**Advantages**: Main memory always holds the most recent value; simple coherence management.

**Disadvantages**: Generates significant memory bandwidth consumption; write performance limited by main memory latency.

### 3.2 Write-Back Policy

In write-back policy, writes modify only the cache line, with main memory updated upon eviction:

```
Processor Write → Cache Update → Main Memory Update (on eviction)
```

**Advantages**: Reduces memory traffic; write operations complete at cache speed.

**Disadvantages**: Requires complex coherence tracking; memory may hold stale data.

## 4. Snooping-Based Cache Coherence Protocols

Snooping protocols employ a broadcast mechanism where all cache controllers monitor a shared interconnect (typically a bus) for memory transactions. Each cache controller independently determines whether the transaction affects its cached data.

### 4.1 Write-Invalidate Protocol

When a processor acquires exclusive ownership for a write operation, it broadcasts an invalidation message to all other caches holding copies:

```
Timeline:
T0: P1, P2 both have Shared copy of X (value=5)
T1: P1 initiates write to X=10
T2: P1 broadcasts Invalidate(X) on bus
T3: Cache₂ detects invalidation, marks X as Invalid
T4: P1 upgrades to Modified state, writes X=10 locally
T5: P2 reads X → Cache miss → fetches X=10 from P1 or memory
```

### 4.2 Write-Update Protocol

When a processor writes to a shared location, it broadcasts the updated data to all caches:

```
P1 writes X=10 → Broadcast Update(X=10) to all caches
All caches holding X update their copies to 10
```

### 4.3 Comparative Analysis

| Protocol         | Bus Traffic | Read Latency       | Implementation | Optimal Workload |
| ---------------- | ----------- | ------------------ | -------------- | ---------------- |
| Write-Invalidate | Lower       | Higher after write | Simpler        | Write-intensive  |
| Write-Update     | Higher      | Lower              | Complex        | Read-intensive   |

The write-invalidate protocol predominates in commercial implementations due to lower bandwidth requirements for typical workloads.

## 5. Directory-Based Cache Coherence

For large-scale systems with numerous processors, snooping protocols create excessive interconnect traffic. Directory-based protocols employ a centralized directory that maintains metadata about cache line sharing.

### 5.1 Directory Structure

The directory maintains, for each memory block:

- **State**: Uncached, Shared, or Exclusive
- **Owner**: Processor holding exclusive copy (if applicable)
- **Sharers**: Set of processors holding shared copies

### 5.2 Write Operation Protocol

```
Scenario: P1 wishes to write to block X currently Shared among P1, P2, P3

1. P1 sends Request-for-Ownership to directory
2. Directory identifies sharers (P2, P3), sends Invalidate messages
3. P2, P3 receive invalidations, acknowledge to directory
4. Directory receives all acknowledgments, sends Grant to P1
5. P1 obtains exclusive ownership, writes new value
6. Directory updates state to Exclusive, owner=P1
```

### 5.3 Directory States

- **Uncached (U)**: No processor possesses a copy
- **Shared (S)**: One or more processors hold read-only copies
- **Exclusive (E)**: Exactly one processor holds a modified (dirty) copy
- **Owned (O)**: Similar to exclusive, with ownership transfer responsibilities

## 6. The MESI Protocol

The MESI protocol is a widely-implemented four-state write-invalidate protocol. Each cache line maintains one of four states:

### 6.1 State Definitions

- **Modified (M)**: Cache line is dirty (differs from memory); this cache holds the sole valid copy; memory is stale.
- **Exclusive (E)**: Cache line is clean (matches memory); this cache holds the only copy.
- **Shared (S)**: Cache line is clean; identical copies may exist in other caches.
- **Invalid (I)**: Cache line is not present or contains invalid data.

### 6.2 State Transition Diagram

```
 +----------+
 | |
 +---------->| Invalid |<----------+
 | | (I) | |
 | +----------+ |
 | ^ | |
 | | v |
 Read Hit Read Miss Write Miss
 | | | |
 | | v |
 +----------+ +----------+ +----------+
 | | | | | |
 | Shared |----|Exclusive | | Modified |
 | (S) | | (E) | | (M) |
 | | | | | |
 +----------+ +----------+ +----------+
 | | |
 | | |
 Write Hit Write Hit Write Hit
 | | |
 v v v
 +----------+ +----------+ +----------+
 | | | | | |
 | Modified |<---| Exclusive|------| Modified |
 | (M) | | (E) | | (M) |
 | | | | | |
 +----------+ +----------+ +----------+
```

### 6.3 State Transition Scenarios

**Read Miss (I → E/S)**:

- Bus transaction: BusRd
- If no other cache holds copy → fetch from memory → E state
- If other caches hold copies → fetch from memory → S state

**Write Miss (I → M)**:

- Bus transaction: BusRdX (read-exclusive)
- Acquire ownership from memory → M state

**Write Hit (S → M)**:

- Bus transaction: BusUpgr (upgrade/invalidate)
- Invalidate all other copies → M state

**Other Processor Read (M → S)**:

- Bus transaction: BusRd from another processor
- Write-back to memory → transition to S state

## 7. Memory Consistency Models

Memory consistency models define the ordering constraints on memory operations, significantly impacting program correctness and performance.

### 7.1 Sequential Consistency (SC)

Under SC, the result of any execution appears as if all operations execute in some sequential order, with operations of each processor appearing in program order:

```
// Thread 1 // Thread 2
x = 1; while (y == 0);
y = 1; print(x);
```

Under SC, if y=1 is observed by Thread 2, then x=1 must also be observed (no load buffering).

### 7.2 Release Consistency (RC)

RC distinguishes between synchronize operations (acquire and release):

- **Acquire**: Synchronization operation establishing memory barrier
- **Release**: Synchronization operation preceding critical section exit

RC permits more aggressive compiler and hardware optimizations while requiring explicit synchronization primitives.

## 8. Performance Analysis

### 8.1 Bus Traffic Calculation

Consider a system with N processors, each performing R reads and W writes to shared data:

**Write-Invalidate Protocol**:

- Initial read by all N processors: N bus transactions (BusRd)
- Each write: 1 BusUpgr (invalidate) + potential write-backs
- Total for W writes: W × (1 + α) transactions, where α is write-back probability

**Write-Update Protocol**:

- Each write: (N-1) update broadcasts
- Total for W writes: W × (N-1) transactions

### 8.2 Miss Rate Analysis

```
Coherence Miss Categories:

1. True Sharing Miss: Processor's write followed by another processor's read
 - Invalidation-based: First write invalidates → read misses

2. False Sharing Miss: Different variables on same cache line
 - Line transfer required despite different data access

3. Capacity Miss: Working set exceeds cache capacity

Example Calculation:
- Private data hit rate: 95%
- Shared read-only hit rate: 85%
- Coherence miss rate: (1-0.85) = 15%
- Effective hit rate: 0.95 × 0.85 = 80.75%
```

## 9. False Sharing

False sharing occurs when processors access distinct variables residing on the same cache line. The coherence protocol treats the entire line as a single unit, causing unnecessary invalidations:

```
struct Data {
 int counter1; // Accessed by P1
 int counter2; // Accessed by P2
} data[1000];

// Both counters on same cache line (64-byte alignment)
// P1: data[i].counter1++
// P2: data[j].counter2++
// False sharing: independent updates cause coherence overhead
```

**Mitigation Techniques**:

- Padding variables to separate cache lines
- Data layout restructuring
- Thread-local accumulation with periodic aggregation

## 10. Commercial Implementations

Modern multiprocessors employ sophisticated coherence protocols:

- **Intel QuickPath Interconnect (QPI)**: Point-to-point interconnect with snoop filters
- **AMD HyperTransport**: High-bandwidth coherence with directory-like structures
- **ARM ACE**: AXI Coherency Extension for AMBA systems

These implementations combine snoop and directory-based approaches, employing hierarchical coherence domains for scalability.

---

## Assessment Questions

### Question 1 (Hard - Numerical)

Consider a 4-processor system with write-invalidate MESI protocol. Initially, all caches have the shared line X in Invalid state. Processor P1 performs the following operations in sequence:

1. P1 reads X
2. P2 reads X
3. P1 writes X
4. P3 reads X
5. P4 writes X

Calculate the total number of bus transactions generated, identifying each transaction type.

### Question 2 (Hard - Protocol Analysis)

Two processors P1 and P2 share a cache line containing variable V. Using the MESI protocol, provide the state transitions in both caches when P1 performs: read V, write V=10, read V; while P2 simultaneously performs: read V, write V=20. Assume both processors start with Invalid state.

### Question 3 (Hard - Performance)

A 8-processor system executes a parallel loop where each iteration reads a shared counter, increments it, and writes back. If each cache line contains 4 independent counters, calculate the performance degradation due to false sharing compared to padding each counter to separate cache lines. Assume each iteration generates one coherence transaction with false sharing.
