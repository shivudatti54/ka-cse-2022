# Memory Management Strategies


## Table of Contents

- [Memory Management Strategies](#memory-management-strategies)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Contiguous Memory Allocation](#contiguous-memory-allocation)
  - [Memory Allocation Algorithms](#memory-allocation-algorithms)
  - [Non-Contiguous Memory Allocation](#non-contiguous-memory-allocation)
  - [Swapping](#swapping)
  - [Virtual Memory](#virtual-memory)
  - [Page Replacement Algorithms](#page-replacement-algorithms)
- [Examples](#examples)
  - [Example 1: Memory Allocation Using First Fit](#example-1-memory-allocation-using-first-fit)
  - [Example 2: Paging Address Translation](#example-2-paging-address-translation)
  - [Example 3: Page Replacement with FIFO](#example-3-page-replacement-with-fifo)
- [Exam Tips](#exam-tips)

## Introduction

Memory management is one of the most critical functions of any operating system, serving as the backbone for efficient program execution and system performance. In modern computing environments, where multiple processes compete for limited physical memory resources, the operating system must employ sophisticated strategies to allocate, deallocate, and protect memory regions while maximizing utilization and minimizing fragmentation. The importance of memory management cannot be overstated—it directly impacts system throughput, response time, and the overall user experience.

The fundamental challenge that memory management strategies address is the mismatch between the requirements of user programs and the finite physical memory available in a computer system. Users expect to run applications that require more memory than physically exists, and they expect these applications to run efficiently without interfering with each other. Operating systems achieve this through various memory management strategies that create the illusion of abundant memory through techniques like virtual memory, paging, and segmentation. Understanding these strategies is essential for any computer science professional, as they form the foundation upon which modern computing systems are built.

This topic explores the various memory management strategies employed by operating systems, from simple contiguous allocation schemes to sophisticated virtual memory systems. We will examine the advantages and disadvantages of each approach, the problems they solve, and the new challenges they introduce. The concepts discussed here are applicable across all major operating systems, including Windows, Linux, and UNIX variants, making this knowledge valuable for system administrators, software developers, and system programmers alike.

## Key Concepts

### Contiguous Memory Allocation

Contiguous memory allocation is the simplest form of memory management where each process is allocated a single continuous block of memory. This approach was common in early operating systems and serves as the foundation for understanding more complex strategies.

**Fixed Partitioning**: In fixed partitioning, physical memory is divided into a predetermined number of partitions at system startup. Each partition can accommodate one process. The number of partitions is typically static, meaning the system can run at most N processes simultaneously if there are N partitions. This approach suffers from internal fragmentation—wasted space within a partition that is not usable by other processes. For example, if a process requiring 10 MB is loaded into a 20 MB partition, 10 MB remains unused. The degree of internal fragmentation depends on the partition sizes chosen by the system administrator.

**Variable Partitioning**: Variable or dynamic partitioning allocates exactly the amount of memory requested by a process, eliminating internal fragmentation. However, this approach introduces external fragmentation—scattered blocks of free memory throughout the system that cannot satisfy large memory requests. External fragmentation occurs because allocated memory blocks create holes between them as processes terminate and release their memory. Over time, the memory becomes fragmented into small, non-contiguous pieces.

### Memory Allocation Algorithms

When a process requests memory, the operating system must decide which free block to allocate. Several algorithms exist for this purpose:

**First Fit**: The system scans memory from the beginning and allocates the first free block that is large enough to satisfy the request. This algorithm is fast because it minimizes search time and tends to allocate memory quickly. However, it may leave large free blocks near the beginning of memory, potentially making it difficult to satisfy large requests later.

**Best Fit**: This algorithm searches the entire free space list and allocates the smallest block that can accommodate the request. Best Fit minimizes wasted space by finding the closest match to the requested size. However, it requires searching the entire free list and tends to create small leftover fragments, potentially increasing external fragmentation.

**Worst Fit**: The system allocates from the largest available free block, hoping that the remaining portion will be large enough to satisfy future requests. While this approach tries to leave large free blocks for big requests, it tends to create smaller fragments and is generally less efficient in terms of memory utilization.

**Next Fit**: Similar to First Fit, but begins searching from where the last allocation ended. This distributes allocations throughout memory more evenly and can reduce search time for subsequent allocations.

### Non-Contiguous Memory Allocation

Non-contiguous memory allocation allows a process to be stored in multiple separate memory regions, solving the external fragmentation problem inherent in contiguous allocation.

**Paging**: Paging divides both physical memory and logical memory into fixed-size blocks called frames and pages respectively. A process's pages can be placed in any available frames in physical memory, completely eliminating external fragmentation. The system maintains a page table that maps virtual page numbers to physical frame numbers. Paging introduces a small amount of internal fragmentation (the last page of a process may not be completely filled) but eliminates the need for contiguous memory allocation. The page table itself requires memory overhead, and every memory access requires an additional memory access to consult the page table, though Translation Lookaside Buffers (TLB) mitigate this performance impact.

**Segmentation**: Segmentation divides a program into logically meaningful units such as code, data, stack, and heap segments. Each segment can be of variable length and represents a logical division of the program. Segmentation provides logical protection and allows different permissions for different segments (read-only code, read-write data). Like paging, segmentation eliminates external fragmentation but requires hardware support in the form of segment tables that translate segment numbers and offsets into physical addresses.

**Segmented Paging**: This hybrid approach combines the benefits of both segmentation and paging. The logical address space is first divided into segments, and each segment is then divided into pages. This approach provides the logical benefits of segmentation (meaningful divisions, different access rights) while gaining the physical memory management benefits of paging (no external fragmentation, simple memory allocation).

### Swapping

Swapping is a memory management technique where entire processes can be moved between main memory and secondary storage (typically disk). When physical memory becomes full, the operating system may swap out a least recently used process to disk to free up memory for other processes. The swapped-out process can be swapped back into memory when it needs to execute again. While swapping enables the system to run more processes than physically fit in memory, it incurs significant I/O overhead. Modern operating systems generally prefer paging over swapping because paging allows partial process movement, which is more efficient than moving entire processes.

### Virtual Memory

Virtual memory is a memory management technique that provides the illusion of a larger, contiguous address space than actually exists in physical memory. It combines physical memory and disk space to create an address space that appears much larger than available RAM. Virtual memory addresses are translated to physical addresses through the memory management unit (MMU) using page tables. When a process accesses a page that is not in physical memory (a page fault), the operating system must bring the required page from disk, potentially evicting another page if memory is full.

### Page Replacement Algorithms

When physical memory is full and a new page must be loaded, the operating system must choose which page to evict. Page replacement algorithms determine this decision:

**FIFO (First-In-First-Out)**: The oldest page in memory is replaced. This algorithm is simple to implement but can suffer from Belady's anomaly—increasing the number of frames can sometimes increase page faults.

**Optimal Page Replacement**: The optimal algorithm replaces the page that will not be used for the longest time in the future. While this algorithm produces the minimum possible page faults, it is impossible to implement in practice because it requires future knowledge of page references.

**LRU (Least Recently Used)**: The page that has not been used for the longest time is replaced. LRU approximates optimal replacement and performs well in practice, but requires hardware support for accurate implementation.

**Clock (Second Chance)**: This algorithm uses a reference bit for each page and gives pages a second chance if they have been recently used. Pages without recent references are replaced in a circular manner, providing a practical approximation of LRU.

## Examples

### Example 1: Memory Allocation Using First Fit

Consider a memory with the following free blocks in order: Block A (50 KB), Block B (200 KB), Block C (100 KB), Block D (80 KB). A process requests 75 KB of memory.

**Solution**: Starting from the beginning, we check Block A (50 KB) - too small. Block B (200 KB) - sufficient. We allocate 75 KB from Block B, leaving a remainder of 125 KB. The resulting free blocks are: Block A (50 KB), Block B' (125 KB), Block C (100 KB), Block D (80 KB).

### Example 2: Paging Address Translation

A system uses paging with page size of 4 KB (4096 bytes). A process generates the virtual address 5000. Determine the page number and offset.

**Solution**: 
- Page size = 4 KB = 4096 bytes
- Offset = virtual address mod page size = 5000 mod 4096 = 904
- Page number = virtual address / page size = 5000 / 4096 = 1 (integer division)

If the page table indicates that virtual page 1 is mapped to physical frame 7, the physical address would be: (7 × 4096) + 904 = 28672 + 904 = 29576.

### Example 3: Page Replacement with FIFO

Consider a reference string: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 with 3 frames. Calculate the number of page faults using FIFO.

**Solution**:
- Frame 1: Reference 1 → Page fault (1 loaded)
- Frame 2: Reference 2 → Page fault (2 loaded)  
- Frame 3: Reference 3 → Page fault (3 loaded)
- Reference 4: All frames occupied, 1 is oldest → Replace 1 with 4, Page fault
- Reference 1: 2 is oldest → Replace 2 with 1, Page fault
- Reference 2: 3 is oldest → Replace 3 with 2, Page fault
- Reference 5: 4 is oldest → Replace 4 with 5, Page fault
- Reference 1: Already in memory, No fault
- Reference 2: Already in memory, No fault
- Reference 3: 1 is oldest → Replace 1 with 3, Page fault
- Reference 4: 2 is oldest → Replace 2 with 4, Page fault
- Reference 5: 3 is oldest → Replace 3 with 5, Page fault

Total page faults: 9

## Exam Tips

1. Understand the fundamental difference between internal and external fragmentation and how each memory management strategy addresses them.

2. Remember that paging eliminates external fragmentation but may have internal fragmentation, while variable partitioning eliminates internal fragmentation but suffers from external fragmentation.

3. For page replacement algorithms, be able to manually trace through reference strings and count page faults for FIFO, LRU, and Optimal algorithms.

4. Know the formula for calculating page number and offset: Given virtual address V and page size P, page number = V / P (integer division), offset = V mod P.

5. In address translation problems, always verify that the offset does not exceed the page size, otherwise the address is invalid.

6. Remember that segmentation provides logical protection while paging provides physical memory management benefits.

7. The page table size can be significant—know how to calculate page table size given the number of pages and entries.

8. For exam problems involving memory allocation algorithms (First Fit, Best Fit, Worst Fit), carefully trace through the allocation process and track remaining free blocks after each allocation.

9. Understand Belady's anomaly and which algorithms are susceptible to it (FIFO).

10. Virtual memory enables processes to use more memory than physically available—understand the role of page faults in this mechanism.