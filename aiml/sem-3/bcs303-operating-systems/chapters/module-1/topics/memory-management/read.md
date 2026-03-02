# Memory Management

## Introduction

Memory management is one of the most critical functions of any operating system. It refers to the techniques and mechanisms that OS uses to manage the computer's primary memory (RAM). The primary memory is the core of computer architecture where data and instructions are stored for immediate processing. Since primary memory is finite and expensive, operating systems must efficiently allocate and deallocate memory spaces to various processes while ensuring protection, isolation, and optimal utilization.

In modern computing environments, memory management has become even more crucial due to the increasing demands of applications and the need for multiprogramming. Without proper memory management, multiple processes cannot coexist in memory simultaneously, and the system would either be inefficient or unstable. The operating system acts as a memory manager, keeping track of which portions of memory are in use, which are free, and implementing allocation strategies that balance performance with memory efficiency. This topic forms the foundation for understanding how operating systems enable features like virtual memory, process isolation, and efficient multitasking.

The evolution of memory management techniques reflects the progression of computing needs—from simple single-user systems to complex multi-user, multi-tasking environments. Understanding these techniques is essential for any computer science student, as they form the backbone of system performance and reliability.

## Key Concepts

### Memory Hierarchy

Computer memory is organized in a hierarchical structure based on speed and cost. At the top of the hierarchy is CPU registers, which provide the fastest access but are limited in number. Cache memory comes next, followed by main memory (RAM), which is the primary focus of memory management. Secondary storage devices like hard drives and SSDs form the lowest tier. The operating system's memory management subsystem primarily deals with main memory, implementing mechanisms to bridge the gap between the fast CPU requirements and the relatively slower main memory.

### Memory Allocation Methods

**Contiguous Allocation** is the simplest method where each process is allocated a single continuous block of memory. Under this approach, memory is divided into partitions, and each process occupies one partition. The two main variants are fixed partition allocation (where memory is divided into fixed-sized partitions) and variable partition allocation (where partitions are created dynamically based on process requirements). However, contiguous allocation suffers from external fragmentation, where free memory becomes fragmented into small non-contiguous blocks.

**Paged Memory Management** solves the fragmentation problem by dividing both memory and processes into fixed-size blocks called pages (for processes) and frames (for memory). Each process occupies multiple pages that can be scattered throughout physical memory. The operating system maintains a page table for each process that maps virtual page numbers to physical frame numbers. This method eliminates external fragmentation but introduces internal fragmentation.

**Segmented Memory Management** divides a process into logical segments such as code, data, stack, and heap. Each segment is allocated contiguous memory space, and the operating system maintains a segment table containing the base address and limit (length) of each segment. This approach provides logical organization of memory but still suffers from external fragmentation.

**Segmented-Paged Memory Management** combines both approaches, dividing each segment into pages. This provides the benefits of both logical segmentation and efficient physical memory utilization.

### Virtual Memory

Virtual memory is a technique that allows the execution of processes that may not be completely in physical memory. It creates an illusion for users that the computer has much more memory than actually available. Virtual memory uses the concept of virtual addresses, which are translated to physical addresses through the Memory Management Unit (MMU). When a process accesses a virtual address that is not in physical memory, a page fault occurs, and the OS must bring the required page from secondary storage into memory.

### Page Replacement Algorithms

When physical memory is full and a new page must be loaded, the operating system must decide which page to evict. Several algorithms exist for this purpose:

**FIFO (First-In-First-Out)** removes the oldest page in memory. It is simple but does not always provide the best performance since it may evict frequently used pages.

**Optimal Page Replacement** selects the page that will not be used for the longest time in the future. This algorithm provides the minimum page faults but is impractical to implement since it requires future knowledge.

**LRU (Least Recently Used)** evicts the page that has not been used for the longest time. It approximates optimal behavior and is widely used in practice, though it requires hardware support for tracking page usage.

**Second Chance** is a modification of FIFO that checks if a page's reference bit is set before eviction, giving pages a second chance if recently referenced.

### Memory Protection and Sharing

Memory protection ensures that one process cannot access the memory space of another process. This is typically implemented using base and limit registers or through the page table mechanism that defines access rights (read, write, execute) for each page. Memory sharing allows multiple processes to access the same memory region when needed, such as shared libraries or inter-process communication buffers. This is achieved through shared pages in paged systems or shared segments in segmented systems.

### Swapping

Swapping is a technique where entire processes are moved between main memory and secondary storage. When memory becomes full, the OS may move inactive processes to swap space (a portion of secondary storage) to free up memory for active processes. While swapping was common in early operating systems, modern systems primarily use paging instead due to its finer granularity and efficiency.

### Thrashing

Thrashing occurs when the system spends more time managing page faults than executing processes. This happens when a process does not have enough pages in physical memory to work efficiently, causing constant page evictions and loads. The operating system monitors CPU utilization and may reduce the degree of multiprogramming or adjust memory allocation to alleviate thrashing.

## Examples

### Example 1: Calculating Internal Fragmentation in Paging

Consider a system with page size of 4KB and a process of 100,000 bytes.

**Solution:**
Page size = 4KB = 4096 bytes
Process size = 100,000 bytes
Number of pages required = ceil(100000 / 4096) = ceil(24.41) = 25 pages

Total memory allocated = 25 × 4096 = 102,400 bytes
Internal fragmentation = 102,400 - 100,000 = 2,400 bytes

Maximum internal fragmentation per page = page size - 1 = 4095 bytes (when a process needs just 1 byte more than a full page)

### Example 2: Working of Page Replacement (FIFO)

Consider a reference string: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 with 3 frames.

**Solution:**
Initially all frames are empty.

- Reference 1: Page fault, load into frame [1] - Frames: [1, -, -]
- Reference 2: Page fault, load into frame [1,2,-] - Frames: [1, 2, -]
- Reference 3: Page fault, load into frame [1,2,3] - Frames: [1, 2, 3]
- Reference 4: Page fault, replace 1 (oldest) - Frames: [4, 2, 3]
- Reference 1: Page fault, replace 2 - Frames: [4, 1, 3]
- Reference 2: Page fault, replace 3 - Frames: [4, 1, 2]
- Reference 5: Page fault, replace 4 - Frames: [5, 1, 2]
- Reference 1: Page hit - Frames: [5, 1, 2]
- Reference 2: Page hit - Frames: [5, 1, 2]
- Reference 3: Page fault, replace 1 - Frames: [5, 3, 2]
- Reference 4: Page fault, replace 2 - Frames: [5, 3, 4]
- Reference 5: Page hit - Frames: [5, 3, 4]

Total page faults = 9

### Example 3: Logical to Physical Address Translation

A system uses paging with page size 1024 bytes. A process has a page table entry for virtual page 5 with frame number 12. Calculate the physical address for virtual address 5243.

**Solution:**
Page size = 1024 bytes
Virtual address = 5243
Virtual page number = floor(5243 / 1024) = floor(5.12) = 5
Offset within page = 5243 - (5 × 1024) = 5243 - 5120 = 123

Given: Frame number for page 5 = 12
Physical address = (frame number × page size) + offset
Physical address = (12 × 1024) + 123 = 12288 + 123 = 12411

## Exam Tips

1. MEMORY MANAGEMENT IS A HIGH-WEIGHTAGE TOPIC in DU examinations. Expect 8-15 marks questions from this unit, often requiring detailed explanations and diagrams.

2. UNDERSTAND THE DIFFERENCE BETWEEN INTERNAL AND EXTERNAL FRAGMENTATION. Internal fragmentation occurs within allocated memory blocks (paging), while external fragmentation occurs between free blocks (contiguous allocation).

3. FOR PAGE REPLACEMENT ALGORITHMS, ALWAYS SHOW YOUR WORK step-by-step in exams. Draw frames and mark page hits and faults clearly.

4. KNOW THE ADVANTAGES AND DISADVANTAGES of each memory management technique. Questions often ask to compare paging with segmentation or explain when each method is suitable.

5. REMEMBER THAT VIRTUAL MEMORY EXTENDS PHYSICAL MEMORY using disk space. It enables programs larger than physical memory to run and provides process isolation.

6. THE MMU (MEMORY MANAGEMENT UNIT) is hardware that translates virtual addresses to physical addresses. Understand its role in memory management.

7. PAGE FAULT is not an error—it is a normal event when a required page is not in memory. Know the steps that occur when a page fault happens.

8. THRASHING negatively impacts performance significantly. Know how to detect and prevent thrashing through working set models or page fault frequency.