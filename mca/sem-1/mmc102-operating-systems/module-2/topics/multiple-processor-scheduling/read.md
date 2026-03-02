# Multiple Processor Scheduling


## Table of Contents

- [Multiple Processor Scheduling](#multiple-processor-scheduling)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Types of Multiprocessor Systems](#types-of-multiprocessor-systems)
  - [Scheduling Approaches](#scheduling-approaches)
  - [Key Terminologies](#key-terminologies)
  - [Scheduling Algorithms](#scheduling-algorithms)
- [Examples](#examples)
  - [Example 1: Load Balancing Analysis](#example-1-load-balancing-analysis)
  - [Example 2: Processor Affinity Impact](#example-2-processor-affinity-impact)
  - [Example 3: Gang Scheduling for Parallel Application](#example-3-gang-scheduling-for-parallel-application)
- [Exam Tips](#exam-tips)

## Introduction

Multiple Processor Scheduling, also known as Multiprocessor Scheduling, is a critical area of study in modern operating systems that deals with the allocation of processes to multiple processors (CPUs) in a computer system. While traditional uniprocessor scheduling focuses on managing a single CPU, multiprocessor scheduling addresses the complexity arising from multiple processing units that must work collaboratively to execute processes efficiently.

The significance of multiple processor scheduling has grown tremendously in recent years due to the widespread adoption of multi-core processors, symmetric multiprocessing (SMP) systems, and distributed computing environments. In these systems, the operating system must not only decide which process to execute but also determine on which processor to execute it, considering factors such as load balancing, processor affinity, and cache coherence. A well-designed multiprocessor scheduling algorithm can significantly improve system throughput, reduce response time, and maximize resource utilization. Conversely, poor scheduling decisions can lead to cache thrashing, excessive context switching, and underutilization of available processing power.

This topic is particularly relevant for MCA students because modern computing infrastructure almost exclusively uses multi-core processors. Understanding multiprocessor scheduling prepares students to analyze and optimize performance in real-world systems, from mobile devices to cloud computing servers.

## Key Concepts

### Types of Multiprocessor Systems

Multiprocessor systems can be broadly classified into three categories based on their architectural design:

**Symmetric Multiprocessing (SMP):** In SMP systems, all processors are identical and share a common memory space. The operating system runs on all processors equally, and any process can execute on any processor. SMP provides good flexibility and resource sharing but requires sophisticated synchronization mechanisms. Modern multi-core processors are essentially SMP systems where multiple cores share the same physical chip and memory hierarchy.

**Asymmetric Multiprocessing (AMP):** In AMP systems, processors are not equal. One master processor controls the system and distributes work to slave processors. This approach simplifies scheduling but creates a single point of failure and cannot utilize all processors equally. AMP is commonly found in embedded systems and older multiprocessor designs.

**Clustered Multiprocessing:** This approach groups multiple independent systems (clusters) that work together. Each node in the cluster is an SMP system, and processes can be scheduled across nodes. Clustered systems are widely used in high-performance computing and enterprise applications requiring high availability.

### Scheduling Approaches

**Load Sharing:** This approach attempts to distribute the workload evenly across all available processors. When a processor becomes idle, it pulls work from a shared run queue. The Linux scheduler uses a variant of load balancing called the "buddy system" combined with idle CPU balancing. Load sharing helps prevent processor idle time but may cause processes to migrate frequently between processors, affecting cache performance.

**Gang Scheduling:** This technique schedules related processes (that communicate with each other) simultaneously on different processors. Gang scheduling is essential for parallel applications where processes frequently synchronize. If one process in a gang is blocked waiting for another, all related processes are scheduled together to avoid deadlock situations. This approach is particularly useful for parallel database operations and scientific computations.

**Dedicated Processor Assignment:** In this approach, processors are dedicated to specific processes or applications for their entire duration. This eliminates context switching overhead and maximizes cache affinity but may lead to poor resource utilization if dedicated processors remain idle while other processes wait.

**Dynamic Scheduling:** The operating system adjusts processor allocation dynamically based on current system load and process characteristics. This provides flexibility but adds scheduling overhead. Modern operating systems like Linux and Windows use hybrid approaches that combine elements of multiple scheduling strategies.

### Key Terminologies

**Processor Affinity:** This refers to the tendency of a process to run on the same processor repeatedly. Processor affinity improves performance because the process can benefit from cached data still present in the processor's local cache. Modern schedulers implement "soft affinity" (preferring the same processor but willing to migrate) and "hard affinity" (strictly binding a process to specific processors).

**Load Balancing:** The technique of distributing processes evenly across all available processors to ensure no processor is idle while processes wait on other processors. Load balancing can be performed proactively (periodically) or reactively (when a processor becomes idle).

**Migration:** The movement of a process from one processor to another. While migration can improve load balance, it incurs costs including cache invalidation, TLB (Translation Lookaside Buffer) flushes, and potential disruption of processor affinity benefits.

**Cache Coherence:** In multiprocessor systems with separate caches for each processor, maintaining consistent data across all caches is crucial. When a process migrates between processors, the new processor must obtain the latest data, potentially causing cache misses and performance degradation.

**NUMA (Non-Uniform Memory Access):** In NUMA systems, memory access time depends on the physical location of memory relative to the processor. A NUMA-aware scheduler attempts to allocate processes to processors closest to their memory pages to minimize memory access latency.

### Scheduling Algorithms

**Round-Robin for Multiprocessors:** Extends the traditional round-robin algorithm by maintaining separate run queues for each processor. Each processor schedules processes from its local queue, and periodic load balancing redistributes work.

**Priority-Based Scheduling:** Processes are assigned priorities, and the scheduler selects the highest priority process to run. In multiprocessor systems, priority inversion (where lower priority processes block higher priority ones) becomes more complex and requires protocols like Priority Inheritance.

**Work-Stealing Algorithms:** Idle processors actively "steal" work from busy processors' queues. This approach was pioneered by the Cilk programming language and is used in modern task-parallel frameworks. Work-stealing provides excellent load balance while keeping communication overhead minimal.

## Examples

### Example 1: Load Balancing Analysis

Consider a system with 4 processors and 8 processes with the following CPU burst times (in milliseconds): P1: 15, P2: 10, P3: 8, P4: 12, P5: 6, P6: 9, P7: 14, P8: 7.

**Scenario A: No Load Balancing (Static Assignment)**
If processes are evenly distributed without considering actual load:
- Processor 1: P1(15) + P5(6) = 21 ms total
- Processor 2: P2(10) + P6(9) = 19 ms total
- Processor 3: P3(8) + P7(14) = 22 ms total
- Processor 4: P4(12) + P8(7) = 19 ms total
Makespan (completion time): 22 ms

**Scenario B: With Load Balancing**
Redistribute to minimize makespan:
- Processor 1: P1(15) + P3(8) = 23 ms
- Processor 2: P2(10) + P4(12) = 22 ms
- Processor 3: P6(9) + P7(14) = 23 ms
- Processor 4: P5(6) + P8(7) = 13 ms (idle after 13 ms)

Better approach (bin-packing greedy):
- Sort in descending order: 15, 14, 12, 10, 9, 8, 7, 6
- Processor 1: 15 + 6 = 21
- Processor 2: 14 + 7 = 21
- Processor 3: 12 + 8 = 20
- Processor 4: 10 + 9 = 19
Makespan: 21 ms

This example demonstrates that optimal load balancing is analogous to the partition problem and is NP-hard in general.

### Example 2: Processor Affinity Impact

Consider a process P with 10000 CPU cycles that accesses a data set of 1000 bytes cached in L1 cache (hit time: 4 cycles) with a cache hit rate of 95% when running on the same processor. If it migrates to a new processor, cache must be reloaded (miss rate becomes 100% initially).

**Running on same processor (with affinity):**
- Cache hits: 9500 × 4 = 38000 cycles
- Cache misses: 500 × 100 (main memory access) = 50000 cycles
- Total: 88000 cycles

**Running after migration (no affinity):**
- All 10000 accesses require main memory: 10000 × 100 = 1,000,000 cycles

This calculation shows that maintaining processor affinity can improve performance by over 10× for cache-intensive processes. The scheduler should consider the cost of breaking cache affinity before migrating a process.

### Example 3: Gang Scheduling for Parallel Application

A parallel application consists of 4 threads that communicate frequently. Using gang scheduling:
- All 4 threads are scheduled simultaneously on 4 different processors
- Thread communication completes in 2 ms (while all are running)
- If scheduled individually with gaps:
  - Thread 1 runs (2 ms), waits (5 ms) for Thread 2
  - Thread 2 runs (2 ms), waits (3 ms) for Thread 3
  - Thread 3 runs (2 ms), waits (1 ms) for Thread 4
  - Total execution: 10 ms versus 4 ms with gang scheduling

Gang scheduling reduces total execution time by 60% in this scenario by eliminating synchronization delays.

## Exam Tips

1. **Differentiate SMP from AMP clearly:** Remember SMP treats all processors equally with shared memory, while AMP has a hierarchical structure with master-slave relationships.

2. **Understand the trade-offs in processor affinity:** While affinity improves cache performance, excessive affinity can cause load imbalance. Know when to sacrifice affinity for load balancing.

3. **Remember the three main multiprocessor scheduling approaches:** Load sharing, gang scheduling, and dedicated processor assignment. Be able to explain each with advantages and disadvantages.

4. **Know why migration has costs:** Context includes cache invalidation, TLB flushes, and loss of data locality. This frequently appears in exam questions.

5. **NUMA awareness is increasingly important:** Understand that in NUMA systems, memory access time varies based on processor-memory distance, affecting scheduling decisions.

6. **Be familiar with real-world schedulers:** Linux uses CFS (Completely Fair Scheduler) with O(1) scheduling for SMP. Windows uses multi-level feedback queue with NUMA optimization. These provide practical context.

7. **The relationship between degree of multiprogramming and CPU utilization:** In multiprocessor systems, higher CPU count allows higher degree of multiprogramming without degrading response time.

8. **Cache coherence impact:** Remember that in systems with separate caches, migration can cause cache misses and degrade performance significantly. This is why soft affinity is preferred over hard affinity in most systems.