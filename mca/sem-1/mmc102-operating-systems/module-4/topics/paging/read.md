# Paging


## Table of Contents

- [Paging](#paging)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Page and Frame Structure](#page-and-frame-structure)
  - [Page Table Structure](#page-table-structure)
  - [Translation Lookaside Buffer (TLB)](#translation-lookaside-buffer-tlb)
  - [Virtual Memory and Demand Paging](#virtual-memory-and-demand-paging)
  - [Page Replacement Algorithms](#page-replacement-algorithms)
  - [Segmentation and Paging](#segmentation-and-paging)
- [Examples](#examples)
  - [Example 1: Logical to Physical Address Translation](#example-1-logical-to-physical-address-translation)
  - [Example 2: TLB Hit Rate Calculation](#example-2-tlb-hit-rate-calculation)
  - [Example 3: Page Fault Calculation with FIFO](#example-3-page-fault-calculation-with-fifo)
- [Exam Tips](#exam-tips)

## Introduction

Paging is a fundamental memory management technique used by modern operating systems to efficiently manage physical memory and provide the illusion of a larger, contiguous address space to processes. In a paged memory management system, both the physical memory and the logical address space of a process are divided into fixed-size blocks called frames and pages respectively. This technique eliminates external fragmentation, one of the most persistent problems in memory management, and enables efficient sharing of physical memory among multiple processes.

The concept of paging became essential when computer systems grew beyond the capacity to provide each process with a contiguous block of physical memory. Traditional contiguous memory allocation suffered from both external fragmentation and the inability to allocate memory to processes larger than available contiguous space. Paging solves these problems by allowing physical memory to be allocated non-contiguously while presenting each process with a uniform, linear address space. This abstraction is particularly crucial in modern computing environments where thousands of processes run concurrently, each requiring its own address space while sharing limited physical memory resources.

From the perspective of an operating system designer, paging provides numerous advantages including memory protection, memory sharing, and simplified memory allocation. The page table, which is the data structure maintaining the mapping between virtual pages and physical frames, serves as the cornerstone of this memory management strategy. Understanding paging is essential for any computer science student because it represents the foundation upon which modern virtual memory systems are built, and it directly impacts system performance, security, and multitasking capabilities.

## Key Concepts

### Page and Frame Structure

In a paging system, the logical address space of a process is divided into equal-sized blocks called PAGES, while the physical memory is divided into corresponding blocks called FRAMES. The size of a page must equal the size of a frame for the mapping to work efficiently. Page sizes are typically powers of two, commonly ranging from 4 KB to 2 MB in modern systems, though some architectures support larger pages. The choice of page size involves a trade-off: larger pages reduce the overhead of page table management but lead to more internal fragmentation, while smaller pages reduce fragmentation but require larger page tables.

The logical address in a paged system is divided into two components: the page number and the page offset. The page number serves as an index into the page table to retrieve the corresponding frame number, while the page offset indicates the byte's position within that frame. When combined, the frame number and offset produce the physical address. This two-step translation process, while introducing some overhead, enables the operating system to place any page in any available frame anywhere in physical memory.

### Page Table Structure

The page table is the data structure that maintains the mapping between virtual pages and physical frames. Each entry in the page table, known as a Page Table Entry (PTE), contains several pieces of information essential for memory management. A typical PTE includes the frame number where the corresponding page is stored, valid/invalid bits indicating whether the page is currently in physical memory, protection bits specifying read/write/execute permissions, and dirty bits indicating whether the page has been modified since being loaded into memory.

Modern operating systems employ various optimizations for page table storage. The simplest approach, called flat paging, uses a single-level page table, but this can become impractical for large address spaces. Multi-level page tables create a hierarchical structure, similar to a tree, where each level of the table maps to smaller regions of the virtual address space. This hierarchical approach allows the operating system to allocate page table pages only for valid portions of the address space, significantly reducing memory overhead for processes with sparse memory usage.

An inverted page table represents an alternative design where instead of maintaining one entry per virtual page, the system maintains one entry per physical frame. This approach reduces memory overhead for the page table itself but increases the time required to look up page mappings since the entire table must be searched. Most modern systems use some form of inverted page table combined with hardware-accelerated lookup structures to balance these concerns.

### Translation Lookaside Buffer (TLB)

The page table translation process, though conceptually simple, introduces significant overhead if performed entirely in software for every memory access. To address this performance concern, computer architectures incorporate a specialized hardware cache called the Translation Lookaside Buffer (TLB). The TLB is an associative memory cache that stores recently used page table entries, allowing hardware to perform address translation in a single cycle for cache hits.

When a memory access occurs, the CPU first checks the TLB for the corresponding page table entry. If found (a TLB hit), the physical address is generated immediately without consulting the main page table. If not found (a TLB miss), the system must perform a page table walk, accessing the actual page table in memory to retrieve the entry, which is then loaded into the TLB for future accesses. The TLB typically contains between 64 and 512 entries in most processors, and hit rates exceeding 95% are common in practice due to the temporal and spatial locality exhibited by most programs.

TLB entries also include additional metadata such as address space identifiers to prevent one process's entries from being incorrectly used for another process. Some advanced TLB designs implement hardware page table walkers that can traverse multi-level page tables automatically, further reducing the software overhead associated with page table access.

### Virtual Memory and Demand Paging

Paging forms the foundation of virtual memory systems, which allow processes to use more memory than physically available in the system. In a demand paging system, pages are loaded into physical memory only when they are first accessed, a technique known as lazy loading. This approach provides several benefits: processes can start execution with minimal memory footprint, the system can over-commit physical memory by allocating more virtual pages than available frames, and the overall system throughput improves by loading only necessary pages.

When a process accesses a page that is not currently resident in physical memory, a page fault occurs. The operating system must handle this fault by locating the page on secondary storage (typically a swap partition or file), allocating a free frame in physical memory, loading the page from secondary storage into that frame, updating the page table to reflect the new mapping, and resuming the interrupted process. Page faults are expensive operations, typically requiring thousands of processor cycles to complete, making efficient page replacement algorithms crucial for system performance.

### Page Replacement Algorithms

When all physical frames are occupied and a new page must be loaded, the operating system must select a victim page to evict from memory. The algorithm used to select this victim is called a page replacement algorithm, and its efficiency directly impacts system performance. Several standard algorithms exist, each with different characteristics regarding hit ratio and implementation complexity.

The FIFO (First-In-First-Out) algorithm evicts the oldest page in memory, treating physical memory as a simple queue. While simple to implement, FIFO suffers from Belady's anomaly, where increasing the number of frames can paradoxically increase the number of page faults. The Optimal algorithm, which theoretically yields the fewest possible page faults by evicting the page that will not be used for the longest time in the future, serves as a theoretical benchmark but cannot be implemented in practice since it requires future knowledge of page references.

The LRU (Least Recently Used) algorithm approximates optimal behavior by evicting the page that has not been used for the longest time. Though theoretically sound, pure LRU requires tracking the order of all memory references, making it expensive to implement. Most systems implement approximations such as the Clock algorithm (also called Second Chance), which uses a reference bit to distinguish between pages that have been recently used versus those that have not, providing good approximation of LRU with minimal overhead.

### Segmentation and Paging

While pure paging divides memory into fixed-size blocks, segmentation divides memory into variable-sized segments based on logical divisions within a program such as code, data, stack, and heap. The combination of segmentation and paging leverages the advantages of both approaches: segmentation provides logical organization and memory protection based on program structure, while paging eliminates external fragmentation and provides efficient memory management within each segment.

In a segmented and paged system, a logical address consists of three components: a segment selector, a page number within that segment, and an offset within that page. The segment selector identifies the segment, which is mapped through a segment table to obtain the base address of the page table for that segment. The page number then indexes into this page table to find the corresponding frame, and the offset specifies the exact byte within the frame. This two-level translation provides both logical flexibility and physical efficiency, though at the cost of increased hardware complexity and memory access overhead.

## Examples

### Example 1: Logical to Physical Address Translation

Consider a system with a 16-bit logical address space and page size of 4 KB (2^12 bytes). Determine the physical address for the logical address 0x3A7F.

First, calculate the number of bits required for the offset: log2(4096) = 12 bits. This leaves 16 - 12 = 4 bits for the page number, allowing for 2^4 = 16 virtual pages.

Extract the page number and offset from the logical address 0x3A7F:
- Logical address in binary: 0011 1010 0111 1111
- Offset (lower 12 bits): 1010 0111 1111 = 0xA7F
- Page number (upper 4 bits): 0011 = 3

Assume the page table entry for virtual page 3 contains:
- Valid bit = 1 (page is in memory)
- Frame number = 0xC (12 in decimal)

The physical address is constructed by combining the frame number with the offset:
- Frame number: 0xC = 1100 in binary (4 bits)
- Offset: 0xA7F (12 bits)
- Physical address: 1100 1010 0111 1111 = 0xCA7F

Therefore, logical address 0x3A7F maps to physical address 0xCA7F.

### Example 2: TLB Hit Rate Calculation

A system has a TLB with 64 entries and achieves a TLB hit rate of 98%. Memory access time is 100 nanoseconds without the TLB, and TLB lookup takes 5 nanoseconds. Calculate the effective memory access time.

For a TLB hit, the access time equals the TLB lookup time plus the physical memory access time: 5 + 100 = 105 nanoseconds.

For a TLB miss, the access time includes TLB lookup, page table access (which requires two memory accesses in a single-level page table), and finally the physical memory access: 5 + 2(100) + 100 = 305 nanoseconds.

The effective access time = (hit rate × hit time) + (miss rate × miss time)
= (0.98 × 105) + (0.02 × 305)
= 102.9 + 6.1
= 109 nanoseconds

This shows that even with a 98% hit rate, the TLB miss penalty significantly impacts average performance, highlighting the importance of maintaining high TLB hit rates.

### Example 3: Page Fault Calculation with FIFO

Consider a reference string: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 with 3 frames. Calculate the number of page faults using the FIFO algorithm.

Initially, all frames are empty:
- Reference 1: Page 1 loaded into frame 0 — FAULT
- Reference 2: Page 2 loaded into frame 1 — FAULT
- Reference 3: Page 3 loaded into frame 2 — FAULT
- Reference 4: Page 4 replaces page 1 (oldest) — FAULT
- Reference 1: Page 1 replaces page 2 (oldest) — FAULT
- Reference 2: Page 2 replaces page 3 (oldest) — FAULT
- Reference 5: Page 5 replaces page 4 (oldest) — FAULT
- Reference 1: Page 1 already in frame 0 — HIT
- Reference 2: Page 2 already in frame 1 — HIT
- Reference 3: Page 3 replaces page 1 (oldest) — FAULT
- Reference 4: Page 4 replaces page 2 (oldest) — FAULT
- Reference 5: Page 5 already in frame 2 — HIT

Total page faults: 9

## Exam Tips

For Operating Systems examinations at the University of Delhi, students should focus on several key areas when studying paging. First, ensure complete understanding of address translation: given a logical address and page table, students must be able to compute the physical address quickly and accurately. The page number and offset calculations are fundamental and frequently appear in examination questions.

Second, thoroughly study page replacement algorithms including FIFO, Optimal, and LRU. Students should be able to trace through reference strings manually, showing each step of the replacement process and counting page faults. The relationship between frame allocation and page fault rates is also important, including understanding Belady's anomaly in FIFO.

Third, TLB performance calculations appear regularly in exams. Students should memorize the effective access time formula and be prepared to calculate hit rates, average access times, and the impact of TLB performance on overall system performance. Understanding the trade-offs between TLB size, hit rate, and lookup time is essential.

Fourth, clearly differentiate between internal and external fragmentation and explain how paging eliminates external fragmentation while introducing internal fragmentation. This conceptual understanding is frequently tested in theory questions.

Fifth, be prepared to explain the purpose and structure of page tables, including multi-level page tables and inverted page tables. Understanding when each type is appropriate and their respective advantages and disadvantages demonstrates deep comprehension of memory management.

Sixth, know the components of a Page Table Entry and understand the purpose of each field including valid bits, protection bits, dirty bits, and reference bits. These details are crucial for understanding how operating systems implement memory protection and track page usage.

Finally, practice numerical problems involving page table entries, logical to physical address translation, and page replacement algorithm traces. Regular practice with these calculations builds speed and accuracy necessary for performing well in examinations.