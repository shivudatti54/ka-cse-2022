# Module 2: Multiple-Processor Scheduling

## 1. Introduction

In modern computing, a single Central Processing Unit (CPU) is often a bottleneck for performance. To overcome this, systems employ multiple processors, creating Symmetric Multiprocessing (SMP) architectures. However, with multiple CPUs comes the new challenge of efficiently distributing processes among them. Multiple-processor scheduling is the set of algorithms and techniques used by an operating system to assign ready processes to available processors, aiming to maximize throughput, minimize latency, and maintain system stability. This is fundamentally more complex than single-processor scheduling due to issues like processor affinity and load balancing.

## 2. Core Concepts

### Symmetric Multiprocessing (SMP)
In an SMP system, all processors are peers; each has its own private set of registers and cache, but they all share the same main memory and I/O devices. There is typically one shared ready queue or a set of queues from which all processors select processes to execute. The operating system kernel can run on any processor, making the system symmetric.

### Approaches to Multiple-Processor Scheduling

#### 1. Asymmetric Multiprocessing (Master-Slave)
In this simpler model, one processor, the *master*, is responsible for all scheduling decisions, I/O processing, and other system activities. The other processors, the *slaves*, only execute user code. This approach eliminates the need for shared kernel data structures but creates a single point of failure and a potential bottleneck at the master processor. It is largely obsolete in modern general-purpose OS design.

#### 2. Symmetric Multiprocessing (SMP)
This is the standard approach. Each processor is self-scheduling. All processors look into a common ready queue and choose a process to run. This requires the kernel to be *reentrant* (or thread-safe) so that multiple processors can execute kernel code simultaneously without corrupting shared data.

### Key Challenges in SMP Scheduling

#### Processor Affinity
A process tends to have a *"affinity"* for the processor it last ran on. This is because a processor's cache holds data (cache lines) from the processes it was recently executing. Migrating a process to a new processor (a *soft affinity*) invalidates the old cache and requires warming up the new processor's cache, which is a performance cost. Operating systems try to avoid this migration.
*   **Soft Affinity:** The scheduler tries to keep a process on the same processor but is free to migrate it if needed for load balancing.
*   **Hard Affinity:** Allows a process to specify a set of processors it is allowed to run on, preventing migration entirely.

#### Load Balancing
This is the process of distributing work evenly across all processors. It is necessary to prevent a situation where one processor is overloaded with processes while others are idle. Load balancing is typically performed by a special kernel thread that periodically checks the load on each processor.
*   **Push Migration:** A dedicated thread (e.g., a *load balancer*) periodically checks the load on every processor. If it finds an imbalance, it pushes processes from overloaded CPUs to idle or less-busy ones.
*   **Pull Migration:** An idle processor actively pulls a waiting task from a busy processor's queue. This is often more efficient than push migration.

#### Multicore Processors
Modern CPUs are often *multicore*, meaning multiple processing cores (CPUs) reside on a single physical chip. These cores often share resources like L2/L3 cache and the main memory controller. This introduces another level of scheduling complexity.
*   **Memory Stall:** A core may spend significant time waiting for data from memory. To utilize this time effectively, many systems support **Simultaneous Multithreading (SMT)**, such as Intel's Hyper-Threading Technology. This allows a single core to have multiple *hardware threads* and switch between them when one is stalled, making the core appear as multiple logical processors to the OS. The scheduler must be aware of which logical processors share a physical core to avoid resource contention.

## 3. Example

Consider an SMP system with two processors (CPU0 and CPU1) and a shared ready queue containing processes P1, P2, P3, and P4.

1.  **Without Load Balancing:** CPU0 might pick up P1 and P2, while CPU1 picks up P3 and P4. If P1 and P2 are computationally intensive while P3 and P4 are I/O-bound and often wait, CPU0 becomes a bottleneck (100% busy) while CPU1 is often idle.
2.  **With Load Balancing:** The load balancer kernel thread detects that CPU0 is 100% utilized and CPU1 is 20% utilized. It uses **push migration** to move, for example, P2 from CPU0's run queue to CPU1's run queue. Now both CPUs share the computational load more evenly, increasing overall system throughput.

## 4. Summary & Key Points

*   **Purpose:** To efficiently schedule processes across multiple CPUs in an SMP system to maximize utilization and performance.
*   **SMP vs. AMP:** Modern systems use **Symmetric Multiprocessing (SMP)**, where all processors self-schedule from a common pool of processes.
*   **Processor Affinity:** The tendency of a process to stay on its last-used CPU to benefit from a warm cache. Can be *soft* (advisory) or *hard* (mandatory).
*   **Load Balancing:** Critical for preventing idle processors. Achieved through *push migration* (a central balancer moves processes) or *pull migration* (idle processors grab work).
*   **Multicore Considerations:** Schedulers must be aware of physical core layouts and SMT/hyper-threading to manage shared cache and memory bandwidth effectively.
*   **Complexity:** SMP scheduling is more complex than uniprocessor scheduling due to the need for sophisticated synchronization of shared queue data and intelligent load-balancing algorithms.