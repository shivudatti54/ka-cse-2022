# Demand Paging


## Table of Contents

- [Demand Paging](#demand-paging)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Mechanism of Demand Paging](#basic-mechanism-of-demand-paging)
  - [Page Fault Handling](#page-fault-handling)
  - [Page Replacement Algorithms](#page-replacement-algorithms)
  - [Thrashing](#thrashing)
  - [Performance of Demand Paging](#performance-of-demand-paging)
- [Examples](#examples)
  - [Example 1: Calculating Effective Access Time](#example-1-calculating-effective-access-time)
  - [Example 2: FIFO Page Replacement](#example-2-fifo-page-replacement)
  - [Example 3: LRU Page Replacement](#example-3-lru-page-replacement)
- [Exam Tips](#exam-tips)

## Introduction

Demand paging is a fundamental memory management technique in modern operating systems that implements virtual memory. In a computer system, the physical memory (RAM) is limited, while the demand for memory by applications continues to grow. Demand paging addresses this problem by loading pages into memory only when they are actually needed during program execution, rather than loading the entire program into memory at startup.

The concept revolutionized operating system design by allowing programs larger than the available physical memory to execute efficiently. When a process references a page that is not currently in memory, a page fault occurs, and the operating system must bring the required page from secondary storage (typically disk) into memory. This lazy loading approach significantly reduces memory usage and improves system throughput by keeping only actively used pages in memory.

Demand paging forms the backbone of virtual memory systems in all major operating systems, including Windows, Linux, and macOS. Understanding demand paging is essential for computer science students because it explains how operating systems create the illusion of a larger memory address space than physically available, enabling multiprogramming and efficient resource utilization.

## Key Concepts

### Basic Mechanism of Demand Paging

In a demand paging system, pages are loaded into memory on-demand when a process attempts to access them. Each process has its own page table, and the operating system maintains a valid-invalid bit for each page table entry. When this bit is set to "valid," the page is currently in memory. When set to "invalid," the page is either not allocated or is currently on disk.

When the CPU attempts to access a page marked as invalid, a page fault trap is generated. The operating system kernel gains control, identifies the required page on disk, allocates a free frame in memory, loads the page from secondary storage into the allocated frame, updates the page table, and then restarts the instruction that caused the fault.

### Page Fault Handling

The page fault service routine involves several critical steps. First, the trap is validated to ensure it is a legitimate page fault. Second, the operating system checks internal tables to determine whether the reference was valid or invalid. If invalid, the process is terminated. If valid, the system locates the required page on disk. Third, a free frame is located in memory; if no frame is free, a page replacement algorithm is invoked to evict an existing page. Fourth, the page is read from disk into the newly allocated frame. Finally, the page table is updated, the valid bit is set, and the interrupted process resumes execution.

### Page Replacement Algorithms

When all frames in memory are occupied and a new page must be loaded, the operating system must choose which page to evict. Several algorithms exist for this purpose.

The FIFO (First-In-First-Out) algorithm evicts the oldest page in memory. It maintains a queue of pages in memory order and removes the page at the front when replacement is needed. FIFO is simple to implement but suffers from Belady's anomaly, where increasing the number of frames can actually increase page faults.

The Optimal Page Replacement algorithm evicts the page that will not be used for the longest time in the future. This algorithm produces the minimum possible page faults but requires future knowledge, making it impractical for implementation. It serves as a theoretical benchmark for evaluating other algorithms.

The LRU (Least Recently Used) algorithm evicts the page that has not been used for the longest time. LRU approximates optimal behavior and does not suffer from Belady's anomaly. Implementation typically requires hardware support for tracking page usage, as maintaining an accurate LRU stack is computationally expensive.

### Thrashing

Thrashing occurs when a system spends most of its time servicing page faults rather than executing useful work. This happens when a process does not have enough frames allocated to hold its working set of pages. As the process executes, it频繁产生页面故障, causing excessive paging I/O and severely degrading system performance.

The working set model, proposed by Denning, defines the set of pages a process is currently using. If the allocated frames fall below the working set size, the process will thrash. Operating systems use various techniques to combat thrashing, including adjusting the degree of multiprogramming and allocating additional frames to thrashing processes.

### Performance of Demand Paging

The effective access time (EAT) in a demand paging system depends on the page fault rate and the time required to service a page fault. Let p represent the page fault rate (0 ≤ p ≤ 1), ma represent memory access time, and pf represent page fault time. The effective access time is calculated as: EAT = (1 - p) × ma + p × pf.

Page fault time includes the service time for the page fault handler, the disk I/O time to read the page (typically 8-12 milliseconds), and the restart time. With modern systems, memory access might take 100 nanoseconds while page fault service might take 8-12 milliseconds, making a page fault approximately 80,000 to 120,000 times slower than memory access.

## Examples

### Example 1: Calculating Effective Access Time

Consider a system with memory access time of 100 nanoseconds, average page fault service time of 8 milliseconds, and a page fault rate of 0.001 (one page fault per 1000 memory accesses). Calculate the effective access time.

Solution:
Given: ma = 100 ns = 0.1 μs, pf = 8 ms = 8000 μs, p = 0.001

Using the formula: EAT = (1 - p) × ma + p × pf
EAT = (1 - 0.001) × 0.1 + 0.001 × 8000
EAT = 0.999 × 0.1 + 8
EAT = 0.0999 + 8
EAT = 8.0999 μs ≈ 8.1 μs

The effective access time is approximately 8.1 microseconds, which is 81 times slower than the memory access time due to the page fault rate.

### Example 2: FIFO Page Replacement

Consider a reference string: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 with 3 frames. Calculate the number of page faults using FIFO algorithm.

Solution:
Initially all frames are empty.

Reference 1: Page 1 loaded into Frame A. Page Fault (1)
Reference 2: Page 2 loaded into Frame B. Page Fault (2)
Reference 3: Page 3 loaded into Frame C. Page Fault (3)
Reference 4: Page 4 replaces Page 1 (oldest). Page Fault (4)
Reference 1: Page 1 replaces Page 2. Page Fault (5)
Reference 2: Page 2 replaces Page 3. Page Fault (6)
Reference 5: Page 5 replaces Page 4. Page Fault (7)
Reference 1: Page 1 is already in memory. No Fault
Reference 2: Page 2 is already in memory. No Fault
Reference 3: Page 3 replaces Page 1. Page Fault (8)
Reference 4: Page 4 replaces Page 2. Page Fault (9)
Reference 5: Page 5 is already in memory. No Fault

Total page faults: 9

### Example 3: LRU Page Replacement

Using the same reference string: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 with 3 frames, calculate page faults using LRU algorithm.

Solution:

Reference 1: Page 1 loaded. Page Fault (1)
Reference 2: Page 2 loaded. Page Fault (2)
Reference 3: Page 3 loaded. Page Fault (3)
Reference 4: Page 4 replaces LRU page (1). Page Fault (4)
Reference 1: Page 1 replaces LRU page (2). Page Fault (5)
Reference 2: Page 2 replaces LRU page (3). Page Fault (6)
Reference 5: Page 5 replaces LRU page (4). Page Fault (7)
Reference 1: Page 1 is already in memory. No Fault
Reference 2: Page 2 is already in memory. No Fault
Reference 3: Page 3 replaces LRU page (5). Page Fault (8)
Reference 4: Page 4 replaces LRU page (1). Page Fault (9)
Reference 5: Page 5 replaces LRU page (2). Page Fault (10)

Total page faults: 10

In this example, FIFO performed better than LRU, demonstrating that LRU does not always outperform FIFO. This illustrates why algorithm performance depends heavily on the specific reference pattern.

## Exam Tips

1. Understand the complete page fault handling sequence: when a page fault occurs, the OS validates the reference, locates the page on disk, finds a free frame (or evicts one), reads the page, updates tables, and restarts the instruction.

2. Memorize the effective access time formula EAT = (1-p) × ma + p × pf and be prepared to substitute values to calculate average memory access time under demand paging.

3. Remember that page fault service time is dominated by disk I/O time (typically 8-12 ms), which is orders of magnitude slower than memory access time (50-200 ns).

4. Know the key difference between FIFO, Optimal, and LRU algorithms. FIFO is simple but suffers from Belady's anomaly; Optimal is theoretical; LRU is practical and approximates optimal behavior.

5. Understand thrashing: it occurs when processes spend more time in paging than executing, caused by insufficient frames allocated relative to the working set.

6. The valid-invalid bit in the page table is crucial: valid means the page is in memory, invalid means either not allocated or on disk.

7. For numerical problems, practice drawing the frame allocation table and tracking page replacements step by step for each reference in the string.

8. Remember that the page table itself also needs to be paged in demand paging systems, leading to multilevel page tables.