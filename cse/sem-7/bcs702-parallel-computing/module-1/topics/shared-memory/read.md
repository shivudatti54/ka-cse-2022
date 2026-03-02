# Shared Memory in Parallel Computing

## Introduction

Shared memory represents one of the fundamental memory organization paradigms in parallel computing systems, where multiple processors or processing elements access a common address space. In this architecture, all processors can directly read and write to the same physical memory locations, enabling efficient communication through simple load and store operations without the overhead of explicit message passing. The shared memory model forms the foundation for symmetric multiprocessing (SMP) systems and provides the conceptual basis for thread-based parallel programming models.

The significance of shared memory in parallel computing stems from its ability to expose memory latency to the programmer, allowing explicit control over data placement and access patterns. This model supports fine-grained parallelism where multiple threads can collaborate on a common task with low communication overhead. However, the very nature of concurrent memory access introduces challenges related to data consistency, synchronization, and cache coherence that must be carefully addressed to ensure correct program execution.

## Key Concepts

### Uniform Memory Access (UMA) Architecture

In Uniform Memory Access (UMA) systems, also known as Symmetric Multiprocessors (SMP), all processors share a common memory through a single interconnect with uniform access latency. The bus-based or crossbar-based interconnection provides equal memory access times from any processor, simplifying programming but limiting scalability. Contemporary SMP systems typically employ point-to-point interconnects like QuickPath Interconnect (QPI) or HyperTransport while maintaining the logical shared memory abstraction. The memory controller ensures that all memory requests are serialized, maintaining a global memory order essential for correctness.

### Non-Uniform Memory Access (NUMA) Architecture

Non-Uniform Memory Access (NUMA) architectures organize memory into nodes, where each processor has local memory with lower access latency compared to remote memory belonging to other nodes. Modern multi-socket systems inherently exhibit NUMA characteristics, and operating systems provide mechanisms to optimize data placement. The memory access latency in NUMA systems varies based on the physical location of data relative to the accessing processor, with local accesses typically 2-3 times faster than remote accesses. Effective parallel programs on NUMA systems require careful data layout and thread affinity management.

### Memory Consistency Models

The memory consistency model defines the permitted ordering of memory operations from the perspective of concurrent threads. **Sequential Consistency** guarantees that the execution appears as if all operations occur in some sequential order, with each processor's operations appearing in program order. This strong model simplifies reasoning but restricts hardware optimizations. **Release Consistency** distinguishes between acquire (read) and release (write) operations, allowing programmers to specify synchronization boundaries more precisely. The C11/C++11 memory model and similar specifications provide explicit atomics supporting relaxed models for performance optimization.

### Cache Coherence Protocols

Cache coherence ensures that multiple caches holding copies of the same memory location present a consistent view. The **snooping protocol** broadcasts memory transactions on a shared bus, with each cache monitoring transactions and taking appropriate actions (invalidate, update, or supply data). The MESI protocol (Modified, Exclusive, Shared, Invalid) tracks cache line states efficiently. **Directory-based protocols** maintain a directory structure tracking which caches hold copies of each memory block, enabling scalability to larger systems by avoiding broadcast traffic.

### Synchronization Primitives

Parallel programs require synchronization to coordinate access to shared data. **Mutexes** provide exclusive access through lock acquisition and release operations, guaranteeing that only one thread executes the protected critical section at any time. **Spinlocks** busy-wait for lock acquisition, suitable for short critical sections where context switching overhead exceeds the wait time. **Barriers** synchronize a group of threads, blocking until all participants arrive, essential for phased parallel algorithms. **Atomic operations** provide lock-free updates to shared variables using hardware-supported instructions like compare-and-swap (CAS).

### False Sharing

False sharing occurs when two threads access different variables that happen to reside in the same cache line, causing unnecessary coherence traffic. Even though the threads access distinct data, the hardware must maintain coherence at cache line granularity, forcing invalidation and reload when one thread modifies its variable. Padding and alignment techniques mitigate false sharing by ensuring frequently co-accessed variables map to different cache lines. This phenomenon can cause severe performance degradation in highly parallel programs, often reducing scalability dramatically.

## Examples

### Example 1: Cache Line Analysis and False Sharing

Consider two threads updating separate counters stored in the same cache line:

```c
struct Counter { long long a; long long b; } counter;
// Thread 1: counter.a++ (10000000 iterations)
// Thread 2: counter.b++ (10000000 iterations)
```

With false sharing, performance scales poorly due to constant cache line ping-ponging. By padding:

```c
struct PaddedCounter {
    long long a;
    char pad[64 - sizeof(long long)];  // Force different cache lines
    long long b;
};
```

The padded structure ensures counter.a and counter.b occupy separate cache lines, eliminating false sharing and enabling linear speedup.

### Example 2: Speedup Calculation with Synchronization Overhead

For a parallel program with parallel portion taking time T_parallel and serial portion T_serial, theoretical speedup is: S = T_serial / (T_serial + T_parallel/p), where p is processor count.

Given: T_serial = 2 seconds, T_parallel = 8 seconds, p = 4
Actual time: T_actual = 2 + 8/4 = 4 seconds
Theoretical ideal: T_ideal = 2 + 8/4 = 4 seconds
Speedup: 10/4 = 2.5x (Amdahl's Law demonstrates diminishing returns)

If synchronization adds 20% overhead to the parallel portion:
T_actual = 2 + (8 × 1.2)/4 = 2 + 2.4 = 4.4 seconds
Speedup: 10/4.4 ≈ 2.27x

### Example 3: Sequential Consistency vs Release Consistency

For a parallel initialization pattern:

```c
// Sequential consistency (strict ordering)
data[i] = value;           // Must complete before flag write
flag = 1;                  // Visible to all threads immediately

// Release consistency (optimized)
atomic_store(&data[i], value, memory_order_release);
atomic_store(&flag, 1, memory_order_release);
// Reader uses acquire:
while(atomic_load(&flag, memory_order_acquire) == 0);
value = atomic_load(&data[i], memory_order_acquire);
```

The release/acquire pattern permits hardware and compiler optimizations while guaranteeing synchronization at designated points.

## Exam Tips

1. **Distinguish between UMA and NUMA** by understanding that NUMA has non-uniform memory access latency based on memory location, while UMA provides uniform access time but limited scalability.

2. **Remember MESI protocol states**: Modified (exclusive, dirty), Exclusive (exclusive, clean), Shared (multiple caches, clean), Invalid (not present).

3. **Apply Amdahl's Law** to calculate theoretical speedup and identify the serial fraction limiting scalability: S ≤ 1/(f + (1-f)/p), where f is serial fraction.

4. **Identify false sharing** when performance degrades despite threads accessing independent data; solve by cache line alignment.

5. **Choose appropriate synchronization**: spinlocks for short waits, mutexes for long critical sections, barriers for phase synchronization.

6. **Understand memory ordering** distinctions between sequential, release, and relaxed consistency for reasoning about correct concurrent programs.

7. **Calculate memory bandwidth requirements** using access patterns to predict parallel performance limitations.
