# Thrashing in Operating Systems

## Introduction

In a multiprogramming environment, the CPU utilization is heavily dependent on the number of processes in memory. Ideally, as the **degree of multiprogramming** increases, so should CPU utilization. However, after a certain point, the system can enter a catastrophic state called **thrashing**, where the system spends more time swapping pages in and out of memory than executing actual processes. This module explains the cause, effect, and solutions for thrashing.

## Core Concepts

### 1. The Cause: Locality and Page Faults

Processes exhibit **locality of reference**, meaning they tend to access a specific set of addresses (like a loop or a function) for a period before moving to a new set. The set of pages actively used by a process is called its **working set**.

The OS uses demand paging, loading a page only when it is needed (i.e., a **page fault** occurs). A moderate number of page faults is normal. However, if a process does not have enough frames to hold its current working set, it will generate page faults frequently.

### 2. The Domino Effect: Thrashing

Consider a scenario where the degree of multiprogramming is very high. The OS allocates just a few frames to each process.

1. Process A needs a page not in its allocated frames, causing a page fault.
2. The OS initiates a disk I/O to bring the required page in. To do so, it may have to swap out another page from Process A (or another process).
3. While the I/O for Process A is in the queue, the OS switches to Process B.
4. Process B immediately needs a page that was just swapped out, causing another page fault. This cycle repeats.

The CPU sees a high rate of page faults. The **paging device** (disk) utilization rises to 100% as it is flooded with swap requests. The ready queue empties out because every process is waiting for an I/O operation (a page swap) to complete. From the user's perspective, the system becomes incredibly sluggish or completely unresponsive. This high I/O, low CPU utilization condition is **thrashing**.

### 3. The Formal Relationship

The key insight is that thrashing is a direct result of **allocating too few frames** to active processes. If a process is allocated fewer frames than its minimum working set size, it will thrash. The OS must ensure that the total demand of all processes (sum of their working sets) does not exceed the total number of available frames in the system.

## Example

Imagine a system has 100 frames total. The working set for a video editing program is 40 frames, for a compiler it's 25, and for a web browser it's 20.

- **Stable State:** If the system runs only the video editor and the compiler (40 + 25 = 65 frames used), each process has enough frames for its working set. Page faults are low, and CPU utilization is high.
- **Thrashing State:** If the OS decides to also run the web browser, the total demand becomes 40+25+20 = 85 frames. This is still under the 100-frame limit, so it might be okay. But if the OS then launches another large application with a working set of 30 frames, the total demand (115 frames) now exceeds the physical available frames (100). The system is **over-committed**. The OS, to accommodate everyone, starts taking frames from each process. Now, no process has its required working set. All processes start generating constant page faults, and the system begins thrashing.

## Solutions to Thrashing

The primary solution is to **limit the degree of multiprogramming**. The OS must prevent the sum of working sets from exceeding the total available memory.

- **Working Set Model:** The OS approximates the working set for each process. It only allows a process to run if its working set is currently in memory. If there aren't enough frames for a new process, an existing process is suspended (swapped out entirely).
- **Page-Fault Frequency (PFF):** The OS monitors the rate of page faults for each process.
- If the rate is **too high**, it means the process needs more frames. The OS allocates it more frames (if available).
- If the rate is **too low**, it means the process has more frames than it needs. The OS can take frames away from it.
  This dynamic adjustment helps keep each process's page-fault rate within an acceptable range, preventing thrashing.

Another crucial solution is to use **local** (or **priority**) **replacement algorithms**. If a process starts thrashing, it will only cause page faults for itself and only take frames from itself, containing the damage instead of stealing frames from other processes and causing them to thrash as well.

## Key Points / Summary

- **Thrashing** is a state where the OS spends more time swapping pages to and from disk than executing user processes, leading to drastically low CPU utilization and a frozen system.
- **Primary Cause:** The total memory demand (sum of the working sets of all active processes) exceeds the available physical memory.
- **Effect:** Extremely high page fault rate, 100% disk I/O utilization for the paging device, and an unresponsive system.
- **Solution:** The main solution is to **control the degree of multiprogramming**.
- The **Working Set Model** prevents thrashing by only running processes whose working sets fit in memory.
- The **Page-Fault Frequency (PFF)** scheme dynamically allocates frames to keep the fault rate per process within bounds.
- Using **local page replacement** algorithms helps contain the thrashing effect to a single process.
