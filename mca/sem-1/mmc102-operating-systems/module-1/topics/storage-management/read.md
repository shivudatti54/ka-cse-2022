# Storage Management


## Table of Contents

- [Storage Management](#storage-management)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Memory Hierarchy and Organization](#memory-hierarchy-and-organization)
  - [Contiguous Memory Allocation](#contiguous-memory-allocation)
  - [Non-Contiguous Memory Allocation: Paging](#non-contiguous-memory-allocation-paging)
  - [Segmentation](#segmentation)
  - [Virtual Memory](#virtual-memory)
  - [Thrashing and Performance Tuning](#thrashing-and-performance-tuning)
- [Examples](#examples)
  - [Example 1: Calculating Internal and External Fragmentation](#example-1-calculating-internal-and-external-fragmentation)
  - [Example 2: Two-Level Page Table Address Translation](#example-2-two-level-page-table-address-translation)
  - [Example 3: Page Replacement with LRU](#example-3-page-replacement-with-lru)
- [Exam Tips](#exam-tips)

## Introduction

Storage management constitutes one of the most critical functions of any modern operating system. In the context of operating systems, "storage" encompasses both primary memory (RAM) and secondary storage (hard disks, SSDs, optical media), each serving distinct but interconnected roles in the overall computing ecosystem. The operating system must efficiently allocate, track, and manage these storage resources to ensure optimal system performance while providing seamless execution of multiple processes simultaneously.

The importance of storage management cannot be overstated in contemporary computing environments. With the proliferation of large-scale applications, cloud services, and data-intensive workloads, the demand for efficient memory utilization has reached unprecedented levels. An operating system without robust storage management would fail to provide process isolation, security, and the illusion of simultaneous execution that users expect. Furthermore, the discrepancy between the vast address space requirements of modern applications and the limited physical RAM available makes virtual memory management absolutely essential. This topic examines the fundamental techniques, algorithms, and mechanisms that operating systems employ to manage storage resources effectively, from simple contiguous memory allocation to sophisticated virtual memory systems with demand paging.

## Key Concepts

### Memory Hierarchy and Organization

Modern computer systems employ a hierarchical storage structure that balances speed, capacity, and cost. At the fastest level, processor registers provide immediate access to data but are extremely limited in capacity (typically 8-256 bytes). Cache memory (L1, L2, L3) sits between the processor and main memory, offering faster access times than RAM but at higher cost and lower capacity. Main memory (RAM) serves as the primary workspace for executing processes, while secondary storage provides permanent data retention at the lowest cost per byte but with significantly higher access latencies.

The operating system manages this hierarchy through various techniques, including caching algorithms, prefetching strategies, and write-back mechanisms. Understanding this hierarchy is fundamental to comprehending why different storage management techniques exist and how they interact to deliver acceptable system performance.

### Contiguous Memory Allocation

In contiguous memory allocation, each process is assigned a single continuous block of physical memory. The operating system maintains a memory allocation table (MAT) or use a bitmap to track which memory regions are free and which are occupied. When a process requests memory, the system searches for a contiguous block large enough to accommodate it using one of three placement strategies: first-fit (allocates the first available block of sufficient size), best-fit (finds the smallest available block that can accommodate the request), or worst-fit (allocates the largest available block to leave larger remaining holes).

Contiguous allocation suffers from two fundamental problems: external fragmentation occurs when free memory is divided into small non-contiguous blocks, making it impossible to satisfy large allocation requests despite sufficient total free memory; and internal fragmentation arises when allocated memory blocks are larger than requested, wasting the unused portion. The degree of external fragmentation can be quantified using the formula: total free memory divided by total memory, though this metric often overestimates the ability to satisfy allocation requests.

### Non-Contiguous Memory Allocation: Paging

Paging eliminates external fragmentation by dividing both physical and logical memory into fixed-size blocks called pages (logical) and frames (physical), typically sized at 4KB, 8KB, or power-of-two multiples. Each process maintains a page table that maps virtual page numbers to physical frame numbers, allowing non-contiguous physical allocation while presenting each process with a contiguous virtual address space.

The page table entry (PTE) contains several critical fields: the valid/invalid bit indicates whether the page is currently in physical memory; the frame number specifies the physical location; protection bits define read, write, and execute permissions; and the referenced and modified bits support page replacement algorithms. Modern systems employ multi-level page tables (typically 2-level or 4-level) to handle large address spaces efficiently, reducing the memory overhead of storing page tables for sparse address spaces.

Translation Lookaside Buffers (TLBs) provide hardware-accelerated virtual-to-physical address translation by caching recently used page table entries. A TLB hit avoids the expensive page table walk, significantly improving memory access latency. TLB performance depends on hit rate, which is influenced by temporal and spatial locality in program behavior.

### Segmentation

Segmentation provides a logical view of memory by dividing a process's address space into variable-sized segments based on program structure: code segment, data segment, stack segment, heap, and shared libraries. Each segment has a base address (starting physical address) and limit (segment length), with the hardware checking that offsets do not exceed the limit to prevent unauthorized memory access.

Unlike paging, which is invisible to the programmer, segmentation reflects program semantics and provides natural protection boundaries. Segments can have different access permissions (read-only code, read-write data), and shared segments enable efficient inter-process communication. However, segmentation alone does not eliminate external fragmentation, as segments must still be placed contiguously in physical memory. Many systems combine segmentation with paging to gain the benefits of both: logical transparency from paging and semantic meaning from segmentation.

### Virtual Memory

Virtual memory extends the available logical address space beyond physical memory capacity by using secondary storage as a backing store. When a process accesses a page not currently in physical memory, a page fault occurs, triggering the operating system's page fault handler to load the required page from secondary storage. This demand paging approach allows programs to execute with only portions of their address space resident in physical memory.

The virtual memory system must manage three key resources: the physical memory frames holding currently active pages, the backing store containing all pages not in physical memory, and the page tables tracking the status and location of each virtual page. Page replacement algorithms determine which existing page to evict when a new page must be brought into physical memory. The optimal algorithm (Belady's MIN) evicts the page that will not be referenced for the longest time in the future, serving as a theoretical benchmark. Practical algorithms include FIFO (First In First Out), which is simple but suffers from Belady's anomaly where increasing frame count can increase page faults; LRU (Least Recently Used), which approximates optimal behavior but requires hardware support or software approximation; and the working set model, which maintains pages that a process has actively used within a time window.

### Thrashing and Performance Tuning

Thrashing occurs when the system spends excessive time paging rather than executing useful work, typically when physical memory is insufficient for the current workload. The operating system detects thrashing through CPU utilization monitoring and memory pressure indicators. Several strategies address thrashing: increasing physical memory, reducing multiprogramming degree (running fewer processes concurrently), adjusting page replacement algorithms, and implementing working set estimation to dynamically allocate frames based on process needs.

Memory allocation algorithms must balance competing objectives: maximizing throughput (processes completing per unit time), maximizing CPU utilization (keeping the processor busy), and minimizing turnaround time (average time from submission to completion). These objectives often conflict, requiring careful tuning based on workload characteristics.

## Examples

### Example 1: Calculating Internal and External Fragmentation

Consider a system with 1000 KB of physical memory usingcontiguous allocation with variable-sized partitions. Three processes arrive in sequence: P1 requests 200 KB, P2 requests 300 KB, and P3 requests 250 KB. After allocating these processes, 250 KB remains as a single hole.

If P2 then terminates and releases its 300 KB, two scenarios emerge based on placement strategy. With first-fit, if a new process P4 requests 150 KB, it would be placed in the first hole of sufficient size (the 250 KB hole), leaving 100 KB internal fragmentation within P4's allocation and 100 KB external fragmentation in the remaining hole. With best-fit, P4 would be placed in the smallest hole that accommodates it, optimizing for minimal leftover space but potentially creating more small holes (increasing external fragmentation).

Internal fragmentation in this case equals the difference between allocated and requested memory: 100 KB. External fragmentation equals the total scattered free memory that cannot satisfy large requests: 100 KB.

### Example 2: Two-Level Page Table Address Translation

Consider a system with 32-bit virtual addresses, 4 KB pages (2^12 bytes), and page table entries of 4 bytes. With single-level paging, the virtual address divides into 20 bits for page number and 12 bits for offset, requiring 2^20 entries (4 MB) per process—excessive for large address spaces.

Using two-level paging, divide the 20-bit VPN into two 10-bit parts: first-level page table index (PT1) and second-level page table index (PT2). Each level contains 2^10 = 1024 entries, requiring 1024 × 4 = 4 KB per page table. Only first-level page table must always be resident; second-level tables are allocated on-demand. For a process using only 10 MB of virtual space (approximately 2560 pages), only a few second-level tables need allocation, dramatically reducing page table memory overhead compared to single-level paging.

### Example 3: Page Replacement with LRU

Assume a physical memory with 3 frames and the following reference string: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1.

Using LRU replacement: Initially, frames are empty. References 7, 0, 1 fill frames 1, 2, 3 respectively. When reference 2 arrives, all frames are occupied. LRU identifies page 7 as least recently used (referenced earliest at position 1) and evicts it, bringing in page 2. Subsequent references follow this pattern, tracking the most recent use of each page in physical memory. The total page faults using LRU can be counted by tracing each reference that requires loading a new page.

Compare with FIFO: At reference 2, the page loaded earliest (7 at position 1) is evicted regardless of recent usage. FIFO may perform poorly on sequences with good locality because it ignores access patterns, potentially evicting frequently used pages.

## Exam Tips

1. Memorize the formula for external fragmentation calculation and understand that it represents a necessary but not sufficient condition for allocation—actual fragmentation impact depends on request sizes.

2. When answering questions about page tables, always specify the components: valid bit, frame number, protection bits, and their purposes in memory management and protection.

3. Distinguish clearly between segmentation (logical/visible to programmers, variable-sized, based on program structure) and paging (physical/invisible, fixed-sized, for memory management efficiency).

4. Remember that thrashing occurs when page fault rate becomes excessive; the solution involves either adding physical memory or reducing degree of multiprogramming.

5. For page replacement algorithm comparisons, know that optimal (MIN) provides theoretical lower bound, LRU approximates optimal but is difficult to implement, and FIFO suffers from Belady's anomaly.

6. Understand TLB function as a cache for page table entries and its role in reducing memory access time; a TLB miss requires full page table walk.

7. Be prepared to calculate effective memory access time (EMAT) given TLB hit rate, TLB access time, and memory access time using the formula: EMAT = TLB_hit_rate × (TLB_time + Memory_time) + TLB_miss_rate × (TLB_time + 2 × Memory_time).

8. Recognize that multi-level page tables solve the problem of large single-level page tables consuming excessive memory in sparse address spaces.