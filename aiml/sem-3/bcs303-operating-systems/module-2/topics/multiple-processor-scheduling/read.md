# Multiple-Processor Scheduling


## Table of Contents

- [Multiple-Processor Scheduling](#multiple-processor-scheduling)
- [Introduction](#introduction)
- [Core Concepts](#core-concepts)
  - [1. Approaches to Multiprocessor Scheduling](#1-approaches-to-multiprocessor-scheduling)
  - [2. Processor Affinity](#2-processor-affinity)
  - [3. Load Balancing](#3-load-balancing)
  - [4. Multicore Processors and Synchronization](#4-multicore-processors-and-synchronization)
  - [Example](#example)
- [Key Points / Summary](#key-points--summary)

## Introduction

In traditional single-processor systems, the scheduling problem revolves around choosing which single process from the ready queue gets to execute on the CPU. However, most modern systems, from high-performance servers to personal laptops, are equipped with **multiple processor cores**. This multiprocessing hardware introduces new complexities and opportunities for the operating system's scheduler. Multiple-processor scheduling (or multiprocessor scheduling) extends the concepts of uniprocessor scheduling to systems with more than one CPU, aiming to efficiently utilize all available computing power while maintaining stability and fairness.

## Core Concepts

The goal of multiprocessor scheduling is similar to its uniprocessor counterpart: to assign processes to processors effectively. However, it must address several new challenges:

### 1. Approaches to Multiprocessor Scheduling

There are two primary architectural approaches:

- **Asymmetric Multiprocessing (ASMP):** In this master-slave model, one processor, the master, is responsible for all scheduling decisions, I/O processing, and other system activities. The other processors, the slaves, only execute user code. This approach is simpler because it centralizes the scheduling logic on a single CPU, but it can create a bottleneck at the master processor.

- **Symmetric Multiprocessing (SMP):** This is the most common approach in modern operating systems (like Linux and Windows). Here, each processor is self-scheduling. All processors are peers; each checks its own ready queue and selects a process to run. This eliminates the master CPU bottleneck but introduces the challenge of ensuring that the schedulers on each processor operate correctly without interfering with each other.

### 2. Processor Affinity

A process that has been running on a specific processor builds up a state in that processor's cache (e.g., L1, L2). If the process is migrated to another processor, the cached data must be invalidated and repopulated on the new processor, which is a costly operation leading to a performance penalty known as **cache cold start**.

To mitigate this, schedulers implement **processor affinity**, a concept where a process has a preference to continue running on the processor it is currently using.

- **Soft Affinity:** The scheduler tries to keep a process on the same CPU but does not guarantee it. It is the most common policy and offers a good balance between performance and load balancing.
- **Hard Affinity:** Allows a process to explicitly specify a set of CPUs on which it is allowed to run. This is often used for specialized, real-time applications.

### 3. Load Balancing

In SMP systems where each processor has its own ready queue, it's possible for one CPU to be overloaded with processes while another sits idle. **Load balancing** is the mechanism that redistributes the workload among processors to ensure no CPU is idle when there is work to be done in other queues.

Load balancing is typically handled by a separate kernel thread, the _load balancer_, which periodically checks the load on each processor. If an imbalance is found, it can push processes from a busy CPU's queue to an idle one (**push migration**) or have an idle processor pull a process from a busy processor's queue (**pull migration**). Excessive load balancing can negate the benefits of processor affinity, so it must be done judiciously.

### 4. Multicore Processors and Synchronization

Modern CPUs are not just multiprocessor but **multicore**—multiple computing cores on a single physical chip. These cores often share hardware resources like caches (e.g., L3 cache) and memory buses. This introduces another scheduling consideration:

- If two processes that communicate heavily (are **cooperating processes**) are scheduled on cores that share a cache, they can run more efficiently due to faster communication (data is in a shared cache) than if they were on separate processors with no shared cache. This is sometimes called **cache affinity**.

Furthermore, scheduling on multicore systems must carefully handle synchronization for shared ready queues to avoid race conditions, often using sophisticated locking mechanisms to prevent CPUs from contending for the same scheduler data structures.

### Example

Consider a system with two CPUs, each with its own ready queue.

- **Initial State:** CPU 1 is running a compute-intensive process `P1`, and CPU 2 is idle.
- **New Process:** A new process `P2` becomes ready and is placed in CPU 1's queue.
- **Without Load Balancing:** `P2` waits behind `P1` on CPU 1, while CPU 2 remains idle—an inefficient scenario.
- **With Load Balancing:** The load balancer detects that CPU 1 has two processes while CPU 2 has zero. It may push `P2` from CPU 1's queue to CPU 2's queue. Now both CPUs are utilized, improving overall system throughput.

## Key Points / Summary

- **Objective:** Efficiently schedule processes across multiple CPUs to maximize throughput and utilization while minimizing overhead.
- **SMP vs. ASMP:** Symmetric Multiprocessing (each CPU self-schedules) is the dominant model, overcoming the bottleneck of the master CPU in Asymmetric Multiprocessing.
- **Processor Affinity:** Crucial for performance, it strives to keep a process on the same CPU to avoid the cost of invalidating and repopulating the processor cache (soft vs. hard affinity).
- **Load Balancing:** Essential for stability, it redistributes work from busy CPUs to idle ones (via push or pull migration) to ensure all processors are utilized. It must be balanced against the benefits of processor affinity.
- **Multicore Considerations:** Schedulers can leverage shared caches by scheduling cooperating processes on cores that share cache, improving performance. Synchronization of scheduler data structures is a critical concern.
