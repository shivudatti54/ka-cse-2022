# Memory Management

## Introduction

Memory Management is one of the most critical components of any modern operating system. It refers to the process of controlling and coordinating computer memory, assigning portions of memory to various programs and processes, and ensuring that each process has access to the memory it needs to execute efficiently. In the context of operating systems, memory management serves as the foundation upon which process execution, multi-tasking, and system performance depend.

The importance of memory management cannot be overstated in today's computing environment. With multiple processes running simultaneously on a computer system, the operating system must efficiently allocate limited physical memory resources among competing processes. Without proper memory management, systems would suffer from memory fragmentation, inefficient utilization, security vulnerabilities, and severe performance degradation. The memory management subsystem acts as an intermediary between application programs and the physical hardware, providing each process with the illusion of having dedicated memory space while maximizing overall system throughput and utilization.

This chapter explores the fundamental concepts of memory management, beginning with the basic memory hierarchy and progressing through various management strategies including swapping, contiguous allocation, paging, and segmentation. We also examine virtual memory management, which extends the logical view of memory beyond physical constraints, enabling programs larger than physical memory to execute efficiently.

## Key Concepts

### Memory Hierarchy and Organization

Computer memory is organized in a hierarchical structure based on speed, cost, and capacity. At the top of this hierarchy lies CPU registers, which offer the fastest access but minimal capacity (typically 8-128 bytes). Cache memory, both L1 and L2, provides faster access than main memory but at higher cost and lower capacity. Main memory (RAM) serves as the primary working storage for data and instructions, typically ranging from 4GB to 64GB in modern systems. Finally, secondary storage (hard drives, SSDs) offers the largest capacity but significantly slower access times.

Memory management operates primarily at the main memory level, coordinating how data moves between these levels and how physical memory is allocated to processes. The fundamental challenge is that physical memory is a finite resource, while processes collectively require more memory than physically available. This discrepancy is addressed through virtual memory techniques that create an abstraction layer between logical program addresses and physical memory locations.

### Swapping

Swapping is a memory management technique where entire processes are moved between main memory and secondary storage (typically a swap file or partition). When physical memory becomes insufficient to accommodate all active processes, the operating system selects a process that is not currently executing and moves its entire memory image to secondary storage. The freed physical memory can then be used for another process. When the swapped-out process needs to execute again, it is swapped back into memory, possibly replacing a different process.

Swapping was more common in early operating systems and allows systems to run programs larger than physical memory. However, it introduces significant overhead due to the time required to transfer entire process images between disk and memory. Modern systems prefer more granular memory management techniques like paging, which moves smaller memory units rather than entire processes.

### Contiguous Memory Allocation

Contiguous memory allocation is one of the oldest and simplest memory management schemes. In this approach, each process is allocated a single continuous block of physical memory. The operating system maintains a table of free and allocated memory blocks, and when a process requests memory, the system searches for a block large enough to accommodate it.

Two primary variants exist: fixed partitioning and variable partitioning. In fixed partitioning, memory is divided into a predetermined number of partitions of potentially different sizes. Each partition can hold exactly one process. While simple to implement, this method suffers from internal fragmentation (unused memory within a partition) and limits the number of concurrent processes to the number of partitions.

Variable partitioning allocates memory dynamically based on process requirements. When a process arrives, the system finds a hole (contiguous free memory) large enough to accommodate it. This approach reduces internal fragmentation but introduces external fragmentation, where free memory becomes divided into small non-contiguous blocks. Memory compaction (or garbage collection in this context) can periodically move processes to consolidate free memory, but this operation requires significant CPU time.

The three common strategies for finding suitable holes are: First-fit (allocate first hole large enough, fastest), Best-fit (search for smallest sufficient hole, minimizes wasted space but slower), and Worst-fit (allocate largest hole, leaves large remaining holes but rarely used).

### Paging

Paging is a memory management scheme that eliminates the requirement for contiguous allocation by dividing both physical and logical memory into fixed-size blocks called frames and pages respectively. The physical memory is divided into frames of size typically 4KB, while each process's logical address space is divided into pages of the same size. A page table maps virtual page numbers to physical frame numbers.

When a process accesses memory, the memory management unit (MMU) uses the page table to translate virtual addresses to physical addresses. If the required page is not in physical memory (a page fault occurs), the operating system must bring the page in from secondary storage. This approach eliminates external fragmentation completely and allows non-contiguous allocation of physical memory.

Paging introduces a small amount of internal fragmentation (at most one page per process) but significantly reduces memory management complexity. The page table itself can become large for processes with large address spaces, leading to the development of multi-level page tables and inverted page tables to manage table size efficiently.

### Segmentation

Segmentation is a memory management technique that recognizes that programs naturally consist of different logical units such as code, data, stack, and heap. Unlike paging, which uses fixed-size blocks, segmentation uses variable-sized segments that correspond to logical program divisions. Each segment has a name (or number) and a length, and addresses are specified as segment name:offset pairs.

Segmentation provides natural protection and isolation between different program components. Code segments can be marked read-only, data segments read-write, and stack segments read-write with expand-down capability. This logical organization makes it easier to implement security policies and allows programmers to think in terms of meaningful program units rather than arbitrary memory addresses.

The main drawback of segmentation is external fragmentation, as segments must still be placed contiguously in physical memory. Most modern systems combine segmentation with paging, using segmentation for logical organization and protection while using paging for physical memory allocation. This combination, known as segmented paging, leverages the benefits of both approaches.

### Virtual Memory Management

Virtual memory is an abstraction that provides processes with the illusion of having access to a large, contiguous address space, regardless of the actual physical memory available. It combines physical memory and secondary storage to create a larger, unified address space for each process. Virtual addresses are translated to physical addresses through hardware and software mechanisms, primarily the memory management unit and page tables.

Virtual memory enables several critical capabilities: it allows programs larger than physical memory to execute, provides process isolation by giving each process its own virtual address space, simplifies programming by eliminating the need to manage physical memory allocation, and enables efficient sharing of physical memory among multiple processes.

The effectiveness of virtual memory depends heavily on the locality of reference principle—that programs tend to access a relatively small portion of their address space at any given time. If programs exhibit good locality, virtual memory can provide near-native performance even when physical memory is significantly smaller than the virtual address space.

### Demand Paging

Demand paging is a virtual memory implementation that only loads pages into physical memory when they are explicitly referenced by a running process. Initially, a process begins execution with no pages in memory. When the process attempts to access a page not in physical memory, a page fault occurs, and the operating system loads the required page from secondary storage.

This lazy loading approach offers significant advantages: it reduces initial process startup time, allows more processes to run concurrently since each needs only a fraction of its pages in memory, and avoids loading unused code or data. The tradeoff is that the first reference to any page causes a page fault, introducing latency. However, with good locality, subsequent references to the same and nearby pages hit in memory.

The effectiveness of demand paging is measured by the hit ratio—the percentage of memory references that find the required page in physical memory. A hit ratio of 99% or higher is typically needed for acceptable performance, as each page fault requires disk access, which is orders of magnitude slower than memory access.

### Page Replacement Algorithms

When physical memory is full and a page fault occurs, the operating system must decide which page to evict from physical memory to make room for the requested page. Page replacement algorithms make this decision, attempting to minimize page faults by keeping frequently used pages in memory.

The FIFO (First-In-First-Out) algorithm evicts the oldest page in memory, regardless of whether it is actively used. While simple to implement, it suffers from Belady's anomaly—adding more frames can sometimes increase page faults.

The Optimal algorithm evicts the page that will not be referenced for the longest time in the future. This achieves the minimum possible page faults but requires future knowledge, making it unrealizable in practice. It serves as a theoretical benchmark for evaluating other algorithms.

The LRU (Least Recently Used) algorithm evicts the page that has not been referenced for the longest time. It approximates optimal behavior and performs well in practice but requires hardware support to track page references. Clock (Second Chance) is a practical approximation of LRU that uses a reference bit and circular scanning to achieve good performance with minimal overhead.

### Thrashing

Thrashing occurs when a system spends excessive time moving pages between memory and secondary storage rather than executing useful work. It happens when processes actively reference more pages than can fit in physical memory, causing constant page faults. The operating system spends most of its time servicing page faults rather than executing user instructions, leading to extremely poor system performance and near-zero CPU utilization.

Thrashing is typically triggered when the degree of multiprogramming (number of processes running simultaneously) increases beyond what physical memory can efficiently support, or when processes enter phases requiring more pages than allocated. The working set model, proposed by Denning, defines the set of pages a process needs to keep in memory to avoid thrashing.

To address thrashing, operating systems can use page fault frequency control to adjust the number of frames allocated to processes, implement working set tracking to ensure processes have sufficient memory, or simply reduce the degree of multiprogramming when thrashing is detected. Some systems use swap daemon processes that proactively pages out less-active processes to free memory before thrashing begins.

## Examples

### Example 1: Translating Logical Address to Physical Address in Paging

Consider a system with 16-bit logical addresses and a page size of 4KB (2^12 bytes). Therefore, the logical address is divided into a 4-bit page number (2^4 = 16 pages) and a 12-bit offset.

Given logical address 0x3A7C (in hexadecimal):
- Page number = 0x3A7C >> 12 = 0x3 (binary: 0011)
- Offset = 0x3A7C & 0x0FFF = 0xA7C (binary: 1010 0111 1100)

If the page table entry for virtual page 3 shows frame number 5, then the physical address is:
- Frame number: 5 (binary: 0101)
- Offset: 0xA7C (unchanged)
- Physical address = (5 << 12) + 0xA7C = 0x5A7C

Thus, logical address 0x3A7C maps to physical address 0x5A7C.

### Example 2: Calculating Effective Access Time

Assume a memory access time (Ma) of 100 nanoseconds and a page fault service time (Pf) of 25 milliseconds (25,000,000 nanoseconds). If the page fault rate (p) is 0.001 (0.1%):

Effective Access Time = (1 - p) × Ma + p × Pf
= (1 - 0.001) × 100 + 0.001 × 25,000,000
= 0.999 × 100 + 0.001 × 25,000,000
= 99.9 + 25,000
= 25,099.9 nanoseconds

This is approximately 251 times slower than normal access, demonstrating why minimizing page faults is critical.

### Example 3: Page Replacement with FIFO

Consider a reference string: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 with 3 frames initially empty.

Time 1: Page 1 loaded → Frames: [1, -, -]
Time 2: Page 2 loaded → Frames: [1, 2, -]
Time 3: Page 3 loaded → Frames: [1, 2, 3]
Time 4: Page 4 (fault) → Evict 1, load 4 → Frames: [4, 2, 3]
Time 5: Page 1 (fault) → Evict 2, load 1 → Frames: [4, 1, 3]
Time 6: Page 2 (fault) → Evict 3, load 2 → Frames: [4, 1, 2]
Time 7: Page 5 (fault) → Evict 4, load 5 → Frames: [5, 1, 2]
Time 8: Page 1 (hit) → Frames: [5, 1, 2]
Time 9: Page 2 (hit) → Frames: [5, 1, 2]
Time 10: Page 3 (fault) → Evict 5, load 3 → Frames: [3, 1, 2]
Time 11: Page 4 (fault) → Evict 1, load 4 → Frames: [3, 4, 2]
Time 12: Page 5 (fault) → Evict 2, load 5 → Frames: [3, 4, 5]

Total page faults: 9

## Exam Tips

For DU semester examinations, focus on the following key areas:

1. **Memory Management Basics**: Understand why memory management is necessary and the problems it solves—fragmentation, security, multiprogramming support, and efficiency.

2. **Fragmentation Types**: Know the difference between internal fragmentation (unused space within allocated block), external fragmentation (free space scattered in small blocks), and how each memory management scheme addresses them.

3. **Paging Calculations**: Be prepared to calculate page numbers, offsets, and physical addresses from logical addresses given page size and page table entries.

4. **Page Replacement Algorithms**: Know all major algorithms (FIFO, LRU, Optimal) and be able to trace through reference strings to determine page faults. Remember Belady's anomaly for FIFO.

5. **Virtual Memory Concepts**: Understand demand paging, page fault handling, and the components of page fault service time (trap to OS, page lookup, page swap, restart instruction).

6. **Thrashing**: Know what causes thrashing, its symptoms, and countermeasures including working set model and page fault frequency control.

7. **Comparison Questions**: Be prepared to compare memory management schemes—contiguous vs non-contiguous, paging vs segmentation, advantages and disadvantages of each approach.

8. **Numericals**: Practice numerical problems on effective access time calculations, hit ratio, and frame allocation.

9. **Page Table Structures**: Understand single-level, multi-level, and inverted page tables and their tradeoffs.

10. **Key Definitions**: Memorize definitions of working set, residence set, locality, and thrashing as these frequently appear in examination questions.