# Allocation of Frames


## Table of Contents

- [Allocation of Frames](#allocation-of-frames)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Frame Allocation Basics](#frame-allocation-basics)
  - [Equal Allocation Strategy](#equal-allocation-strategy)
  - [Proportional Allocation Strategy](#proportional-allocation-strategy)
  - [Priority-Based Allocation Strategy](#priority-based-allocation-strategy)
  - [Global vs. Local Replacement](#global-vs-local-replacement)
  - [Working Set Model](#working-set-model)
  - [Thrashing and Its Relationship to Allocation](#thrashing-and-its-relationship-to-allocation)
- [Examples](#examples)
  - [Example 1: Equal Allocation Calculation](#example-1-equal-allocation-calculation)
  - [Example 2: Proportional Allocation Calculation](#example-2-proportional-allocation-calculation)
  - [Example 3: Working Set and Thrashing Analysis](#example-3-working-set-and-thrashing-analysis)
- [Exam Tips](#exam-tips)

## Introduction

In virtual memory systems that use paging, the physical memory is divided into fixed-size blocks called frames. The allocation of frames refers to the process of distributing these physical memory frames among the processes in the system. When a process needs to execute, its pages must be loaded into physical memory, and the operating system must decide how many frames to allocate to each process and which pages should reside in those frames.

The allocation of frames is a critical aspect of memory management because it directly impacts system performance, process execution, and overall throughput. If too few frames are allocated to a process, it will experience excessive page faults, leading to thrashing—a condition where the system spends more time swapping pages than executing instructions. Conversely, allocating too many frames reduces the degree of multiprogramming and wastes precious physical memory that could serve other processes.

In the context of the University of Delhi MCA program, understanding frame allocation strategies is essential because it represents a fundamental trade-off in operating system design: balancing memory efficiency against system responsiveness. This topic builds upon the concepts of paging and virtual memory, forming the foundation for advanced memory management techniques.

## Key Concepts

### Frame Allocation Basics

A frame is a fixed-size block of physical memory, typically ranging from 1KB to 8KB depending on the system architecture. The total number of frames in physical memory determines the maximum number of pages that can reside in memory simultaneously. The frame allocation problem addresses the question: how should these frames be distributed among competing processes?

Each process has a working set—the set of pages that process is actively using during a particular time interval. If a process is allocated enough frames to hold its working set, it will experience minimal page faults. However, the working set changes over time as the process executes different code segments and accesses different data structures.

### Equal Allocation Strategy

In equal allocation, the available frames are divided equally among all processes in the system. If there are m frames and n processes, each process receives m/n frames. This approach is simple to implement and provides fairness in the sense that all processes get the same amount of physical memory.

The advantage of equal allocation is its simplicity—both in understanding and implementation. However, it suffers from a significant drawback: it ignores the actual memory requirements of different processes. A process running a small utility program needs far fewer frames than a process handling a large database query, but equal allocation gives them the same number of frames regardless.

### Proportional Allocation Strategy

Proportional allocation addresses the limitation of equal allocation by allocating frames based on the size of each process. A larger process receives more frames, while a smaller process receives fewer. The allocation is calculated as:

**Frames allocated to process i = (Size of process i / Total size of all processes) × Total available frames**

This approach provides a more sensible distribution that aligns memory allocation with process needs. However, it still does not consider the actual execution characteristics of processes—a large process might be mostly idle while a small process is actively executing.

### Priority-Based Allocation Strategy

In priority-based allocation, processes with higher priority receive more frames than lower-priority processes. This approach recognizes that critical system processes or interactive applications should have preferential access to memory to ensure responsive performance. When a high-priority process experiences a page fault, the system may even steal frames from a lower-priority process to satisfy the request immediately.

This strategy is particularly useful in real-time systems where certain processes must meet strict timing constraints. However, it requires careful design to prevent low-priority processes from starving completely.

### Global vs. Local Replacement

The allocation strategy must be considered alongside the page replacement policy. There are two fundamental approaches:

**Global Replacement**: When a page fault occurs, the system can replace frames from any process in the system. This allows for dynamic adjustment of allocations—a process can gain frames when others don't need them. However, it makes it difficult for a process to control its own page fault rate.

**Local Replacement**: Each process can only replace pages from its own allocated frames. This provides more predictable performance for each process but prevents the system from adapting to changing demands efficiently. A process with insufficient frames will continue to suffer page faults even if other processes have surplus frames.

### Working Set Model

The working set model, introduced by Peter Denning, provides a theoretical framework for frame allocation. A process's working set W(t, τ) is the set of pages referenced during the time interval from t-τ to t, where τ is the working set window—a look-back interval measured in page references.

The key principle is: if a process is allocated at least as many frames as its current working set size, it will experience very few page faults. If allocated fewer, it will thrash. The operating system can dynamically adjust allocations to maintain the working set of each process.

### Thrashing and Its Relationship to Allocation

Thrashing occurs when a process spends more time in page fault handling than in actual execution. This typically happens when a process is allocated fewer frames than its working set size. As the process executes, it quickly exhausts its allocated frames, causing repeated page faults.

The relationship between frame allocation and thrashing is direct: insufficient allocation leads to thrashing, which degrades system performance dramatically. The operating system must monitor page fault rates and dynamically adjust allocations to prevent thrashing while maximizing system throughput.

## Examples

### Example 1: Equal Allocation Calculation

**Problem**: The system has 100 frames and 5 processes (P1, P2, P3, P4, P5). Using equal allocation, how many frames does each process receive?

**Solution**:

Step 1: Identify the total number of frames (m) = 100
Step 2: Identify the number of processes (n) = 5
Step 3: Apply equal allocation formula: Frames per process = m/n = 100/5 = 20

Each process receives 20 frames regardless of process size or priority.

### Example 2: Proportional Allocation Calculation

**Problem**: The system has 50 frames and three processes with the following sizes: P1 = 10 pages, P2 = 15 pages, P3 = 25 pages. Calculate frames allocated to each process using proportional allocation.

**Solution**:

Step 1: Calculate total process size = 10 + 15 + 25 = 50 pages
Step 2: Calculate allocation for each process:
- P1: (10/50) × 50 = 10 frames
- P2: (15/50) × 50 = 15 frames
- P3: (25/50) × 50 = 25 frames

Total allocated = 10 + 15 + 25 = 50 frames (all frames used)

### Example 3: Working Set and Thrashing Analysis

**Problem**: A process has a working set window of 5000 page references. During the last 5000 references, it referenced 120 distinct pages. The system currently allocates 100 frames to this process. Will the process thrash? What happens if frames are reduced to 80?

**Solution**:

Step 1: Working set size = number of distinct pages referenced = 120
Step 2: Currently allocated frames = 100
Step 3: Compare: Allocated frames (100) < Working set size (120)
Step 4: Result: The process will experience frequent page faults because its allocated frames are insufficient for its working set. This is the beginning of thrashing.

If frames are reduced to 80:
- Allocated frames (80) < Working set size (120)
- The process will definitely thrash, spending most of its time handling page faults rather than executing.

To prevent thrashing, the process needs at least 120 frames (or the working set window should be reduced by the OS).

## Exam Tips

1. Remember the fundamental difference between equal and proportional allocation: equal gives all processes the same frames, while proportional gives frames based on process size.

2. In exam questions, carefully read whether the system uses global or local replacement—this affects how page faults are handled and how allocations change during execution.

3. The working set model is frequently tested: understand that working set size represents the minimum frames needed to avoid thrashing for a given time window.

4. Thrashing is always caused by insufficient frame allocation relative to the process's current working set—memorize this causal relationship.

5. Priority-based allocation can lead to starvation of low-priority processes if not carefully managed—consider this disadvantage in comparative questions.

6. Remember that proportional allocation adapts better to varying process sizes but still doesn't consider actual execution behavior like priority-based allocation does.

7. The formula for proportional allocation (process size / total size × total frames) is essential and frequently appears in numerical problems.