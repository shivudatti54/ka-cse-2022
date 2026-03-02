Of course. Here is a comprehensive educational note on Multiple-Processor Scheduling for  engineering students.

# Module 2: Multiple-Processor Scheduling

## 1. Introduction

In modern computing, single-processor systems are increasingly rare. To handle complex computational tasks and improve performance, **multiprocessor systems** (also called parallel or tightly-coupled systems) with two or more processors are the standard. These processors share the same physical memory and peripheral devices. While this architecture boosts throughput and efficiency, it introduces new challenges for the operating system, particularly in how it schedules processes across these multiple CPUs. This unit explores the core concepts and strategies of **Multiple-Processor Scheduling**.

## 2. Core Concepts

### Types of Multiprocessor Systems

1.  **Symmetric Multiprocessing (SMP):** This is the most common approach. Each processor is peers; they are self-scheduling and operate independently. Each processor has its own private queue of ready processes, or all processors draw from a common ready queue. The OS must ensure synchronization to avoid conflicts.
    - **Example:** A dual-core laptop, a quad-core server.

2.  **Asymmetric Multiprocessing (ASMP):** In this model, one master processor controls the system and manages all scheduling decisions, I/O processing, and other system activities. The other processors execute only user code. This is simpler to implement but can create a bottleneck at the master processor.
    - **Example:** Older server systems often used this design.

### Key Challenges in Multiple-Processor Scheduling

Scheduling for multiple CPUs is inherently more complex than for a single CPU due to:

- **Processor Affinity:** When a process runs on a specific processor, the data it frequently accesses gets cached in that processor's cache memory. Migrating the process to another processor (**_process migration_**) invalidates these caches, and the new processor's cache must be repopulated, which is a costly operation known as a **cache miss**. To mitigate this, schedulers try to keep a process running on the same processor.
  - **Soft Affinity:** The scheduler tries to keep a process on the same processor but is not guaranteed to do so (e.g., if that CPU is overloaded).
  - **Hard Affinity:** Allows a process to specify a set of processors it is allowed to run on. This is often used in applications requiring high performance.

- **Load Balancing:** This is essential for keeping all processors busy and maximizing CPU utilization. It is the process of distributing work evenly across all processors. Load balancing is typically performed by a kernel thread called the **balancer**.
  - **Push Migration:** A specific task (e.g., the balancer thread) periodically checks the load on each processor. If it finds an imbalance, it pushes processes from overloaded CPUs onto idle or less busy ones.
  - **Pull Migration:** An idle processor pulls a waiting task from a busy processor's queue. This is often more efficient than push migration.

### Scheduling Approaches

Multiple-processor systems generally use one of two scheduling architectures:

1.  **Asymmetric Scheduling (Master-Slave):**
    - A single processor (the master) handles all scheduling decisions, I/O processing, and other system activities.
    - Other processors (slaves) execute only user code.
    - **Advantage:** Simplicity; data structures for scheduling need not be synchronized.
    - **Disadvantage:** The master can become a performance bottleneck.

2.  **Symmetric Scheduling (SMP):**
    - Each processor is self-scheduling and selects its own process to run. All processors are peers.
    - Processes may be in a **common ready queue** accessed by all processors, or each processor may have its own **private ready queue**.
    - **Common Queue (e.g., Linux O(1) Scheduler):** All processors take the next available task from a single shared queue. This requires efficient locking mechanisms to prevent two processors from grabbing the same process.
    - **Private Queues:** Each processor schedules only the processes in its own queue. This eliminates the need for a common lock but requires effective load balancing to prevent a situation where one processor is idle while another is overloaded.

## 3. Example: Linux Scheduler (CFS)

The Linux Completely Fair Scheduler (CFS) is a prime example of symmetric multiprocessor scheduling. It uses a **per-CPU runqueue**. Each processor has its own data structure containing the tasks it should run. This design minimizes locking contention.

To handle load balancing, CFS uses a combination of **push** and **pull** migration. A kernel thread periodically checks for load imbalance. If one CPU's queue is significantly longer than another's, it moves tasks from the busy CPU's runqueue to the idle one (push). Furthermore, when a CPU is about to go idle, it will "steal" tasks from a busier CPU's runqueue (pull), ensuring no processor is left without work.

## 4. Key Points / Summary

- **Multiprocessor Systems** use multiple CPUs to improve performance and throughput.
- **Symmetric Multiprocessing (SMP)** is the standard model where each processor self-schedules.
- **Processor Affinity** (soft and hard) is crucial for performance to minimize costly cache invalidations.
- **Load Balancing** (push and pull migration) is necessary to keep all processors utilized efficiently and is handled by a dedicated kernel thread.
- Scheduling can use a **common ready queue** (requires locking) or **per-processor private queues** (requires load balancing).
- Real-world implementations, like the **Linux CFS**, use private per-CPU queues with sophisticated load balancing algorithms to achieve high efficiency on multiprocessor systems.
