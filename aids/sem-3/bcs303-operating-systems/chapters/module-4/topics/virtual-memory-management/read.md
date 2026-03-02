# Virtual Memory Management

## Introduction

Virtual Memory Management is one of the most fundamental concepts in modern operating systems, enabling computers to execute programs larger than the available physical memory. This technology creates an illusion for each process that it has exclusive access to a large, contiguous address space, while the actual physical memory may be fragmented across different locations in RAM and on disk. The University of Delhi's Computer Science curriculum emphasizes this topic because it forms the backbone of memory protection, process isolation, and efficient resource utilization in multi-tasking environments.

The significance of virtual memory extends far beyond academic theory. Every modern computing device—from smartphones to enterprise servers—relies on virtual memory management to provide seamless user experiences while running multiple applications simultaneously. When you open dozens of browser tabs, run a video editor alongside a database application, or work with large datasets, virtual memory ensures that the system remains responsive by intelligently swapping data between RAM and secondary storage. Understanding how this mechanism works at a deep level is essential for any computer scientist, as it directly impacts system performance, application behavior, and security.

This chapter explores the theoretical foundations and practical implementations of virtual memory management, covering address translation mechanisms, page replacement strategies, performance optimization techniques, and the infamous thrashing phenomenon that can degrade system performance dramatically.

## Key Concepts

### Fundamentals of Virtual Memory

Virtual memory creates a mapping between virtual addresses used by programs and physical addresses in RAM. This mapping is maintained by the operating system through specialized data structures called page tables. When a CPU executes an instruction that references a memory address, the Memory Management Unit (MMU) intercepts the request and translates the virtual address to a physical address using these tables. If the requested page is not currently in physical memory, a page fault occurs, triggering the operating system's page fault handler.

The virtual address space for each process is typically divided into fixed-size blocks called pages, while physical memory is divided into corresponding blocks called frames. The size of pages and frames must be identical for simple implementation, commonly ranging from 4KB to 2MB depending on system architecture. This arrangement allows non-contiguous physical memory to appear contiguous to each process, eliminating external fragmentation while providing memory protection through hardware-enforced access controls.

### Address Translation Mechanisms

The translation from virtual to physical addresses involves several components working in concert. A virtual address is conceptually divided into two parts: the page number and the offset within that page. The page number serves as an index into the page table to retrieve the corresponding frame number, while the offset remains unchanged and is simply added to the frame's starting physical address.

Modern systems employ multi-level page tables to handle large address spaces efficiently. For a 32-bit address space with 4KB pages, a two-level page table structure uses the upper 10 bits as an index into the first-level (page directory) and the next 10 bits as an index into the second-level (page table). This hierarchical approach ensures that only required page tables are allocated, saving substantial memory. 64-bit systems may use four or more levels, adapting to the vastly larger address spaces they must manage.

The Translation Lookaside Buffer (TLB) serves as a hardware cache for recent address translations, dramatically speeding up the translation process. Without TLB, each memory access would require additional memory accesses to walk the page tables, effectively halving memory bandwidth. TLB hit rates of 95-99% are typical in well-behaved programs, making this optimization crucial for performance.

### Demand Paging and Page Fault Handling

Demand paging is the technique of loading pages into physical memory only when they are explicitly referenced, rather than loading entire programs at startup. This approach provides two significant benefits: faster process startup since only the essential code and data are loaded initially, and the ability to run programs larger than physical memory by keeping only active pages in RAM.

When a page fault occurs, the operating system must perform a specific sequence of operations. First, it validates the memory reference to ensure the access is legal. Then, it locates a free frame in physical memory, either from the free frame list or by evicting an existing page using a replacement algorithm. If the evicted page has been modified (dirty bit set), it must be written back to secondary storage. Finally, the requested page is read from disk into the freed frame, the page table is updated, and the faulting instruction is restarted.

The page fault service time depends heavily on whether the page must be retrieved from secondary storage. With modern SSDs, disk access may take 0.1-1 milliseconds, while traditional hard drives may require 10-20 milliseconds. Compared to memory access times of nanoseconds, page faults are extraordinarily expensive, making efficient page replacement critical for system performance.

### Page Replacement Algorithms

When all physical memory frames are occupied, the operating system must select a victim page to evict. The choice of replacement algorithm significantly impacts system performance and is a favorite topic in university examinations.

The **FIFO (First-In-First-Out)** algorithm maintains a queue of pages in memory order and evicts the oldest page. While simple to implement, FIFO suffers from Belady's anomaly—increasing the number of frames can actually increase page faults in certain access patterns.

The **Optimal (OPT)** algorithm represents the theoretical best, evicting the page that will not be referenced for the longest time in the future. This algorithm is unrealizable in practice since it requires perfect knowledge of future references but serves as a benchmark for evaluating other algorithms.

**LRU (Least Recently Used)** approximates optimal behavior by evicting the page that has not been referenced for the longest time. Hardware support for LRU is expensive, so many systems implement approximations like the **Clock (Second Chance)** algorithm, which uses a reference bit to distinguish recently used pages from those that can be evicted.

### Copy-on-Write and Memory Efficiency

Copy-on-Write (COW) is an optimization technique particularly valuable in fork() system calls, where a parent process creates a child. Rather than immediately copying all pages, the parent and child initially share the same physical pages marked as read-only. If either process attempts to modify a page, a page fault occurs, and the operating system creates a private copy for the modifying process. This approach dramatically reduces memory usage and startup time for new processes, especially when child processes primarily perform read-only operations or immediately call exec() to replace their address space.

Modern operating systems also implement techniques like memory compression (compressing inactive pages rather than swapping them to disk), memory deduplication (identifying identical pages and sharing them across processes), and huge pages (larger page sizes to reduce TLB pressure and page table overhead).

### Thrashing: The Performance Death Spiral

Thrashing occurs when the system spends more time managing page transfers than executing useful work. This happens when the working set of active processes exceeds available physical memory, causing constant page faults as pages are repeatedly evicted and retrieved. The CPU becomes saturated with I/O requests, utilization drops, and throughput plummets.

The fundamental cause of thrashing is overcommitment—attempting to run more concurrent processes than physical memory can accommodate. The operating system detects thrashing through various heuristics, such as monitoring page fault rates and CPU idle time. Mitigation strategies include temporarily suspending processes, reducing the degree of multiprogramming, or dynamically adjusting process priorities to favor those with smaller working sets.

## Examples

### Example 1: Two-Level Page Table Translation

Consider a system with 32-bit virtual addresses, 4KB pages, and a two-level page table where each level uses 10 bits for indexing.

Given virtual address 0x1234ABCD, let's determine the physical address translation:

**Step 1: Convert to binary**
0x1234ABCD = 0001 0010 0011 0100 1010 1100 1101 (binary)

**Step 2: Split the address**
- Page Directory Index (bits 31-22): 0001001001 = 0x49 = 73
- Page Table Index (bits 21-12): 0011010100 = 0xD4 = 212
- Offset (bits 11-0): 101011001101 = 0xACD = 2765

**Step 3: Translate**
The page directory entry at index 73 points to the page table, which is indexed at 212. Assuming the page table entry indicates frame number 0x1F800, the physical address becomes:
Physical Address = (0x1F800 << 12) | 0xACD = 0x1F80ABCD

This example demonstrates how hierarchical page tables enable efficient translation while keeping memory overhead manageable.

### Example 2: Page Replacement with LRU

Consider a system with 3 frames and the following reference string: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5

Using LRU replacement:

**Frames initially empty:**
- Reference 1: Page 1 loaded (Page Fault)
- Reference 2: Page 2 loaded (Page Fault)
- Reference 3: Page 3 loaded (Page Fault)
- Reference 4: Evict page 1 (LRU: 1 was used at step 1), load page 4 (Page Fault)
- Reference 1: Evict page 2 (LRU: 2 was used at step 2), load page 1 (Page Fault)
- Reference 2: Page 2 already in memory (No Fault)
- Reference 5: Evict page 3 (LRU: 3 was used at step 3), load page 5 (Page Fault)
- Reference 1: Page 1 already in memory (No Fault)
- Reference 2: Page 2 already in memory (No Fault)
- Reference 3: Evict page 5 (LRU: 5 was used at step 7), load page 3 (Page Fault)
- Reference 4: Evict page 1 (LRU: 1 was used at step 9), load page 4 (Page Fault)
- Reference 5: Evict page 2 (LRU: 2 was used at step 10), load page 5 (Page Fault)

Total Page Faults: 10

### Example 3: TLB Performance Calculation

A system has a TLB with 64 entries and a hit rate of 96%. Memory access time is 100 nanoseconds, and TLB lookup takes 20 nanoseconds. Calculate the average memory access time.

**With TLB:**
Average Access Time = (Hit Rate × (TLB Lookup + Memory Access)) + (Miss Rate × (TLB Lookup + 2 × Memory Access))

The miss penalty includes TLB lookup plus two memory accesses (one for page table walk, one for actual data).

**Calculation:**
= 0.96 × (20 + 100) + 0.04 × (20 + 2 × 100)
= 0.96 × 120 + 0.04 × 220
= 115.2 + 8.8
= 124 nanoseconds

**Without TLB:** Each access would require two memory accesses = 200 nanoseconds

The TLB provides a speedup of (200 - 124) / 200 = 38% reduction in effective access time.

## Exam Tips

1. **Understand the difference between paging and segmentation**: Paging uses fixed-size blocks (pages/frames) and provides uniform memory protection, while segmentation uses variable-sized logical divisions that match program structure. Combine both in systems for optimal results.

2. **Memorize page fault calculation formulas**: Remember that page fault rate = 1 - hit rate. Calculate effective access time using: EAT = p × (TLB + Disk) + (1-p) × (TLB + Memory), where p is the page fault rate.

3. **Be able to trace page replacement algorithms**: Practice working through FIFO, LRU, and Optimal algorithms with various reference strings. Pay attention to Belady's anomaly in FIFO.

4. **Know the page table entry structure**: Each PTE typically contains: Valid/Invalid bit, Frame number, Protection bits (read/write/execute), Modified (dirty) bit, Referenced (accessed) bit.

5. **Explain thrashing in interviews and exams**: Describe the cycle of high page fault rates → excessive I/O → low CPU utilization → more processes admitted → further memory pressure.

6. **Understand TLB and cache relationship**: Both use similar principles (temporal and spatial locality), but TLB caches address translations while CPU cache stores actual data. TLB misses are generally more costly.

7. **Differentiate between internal and external fragmentation**: Paging eliminates external fragmentation but may cause internal fragmentation (unused space in last page). Contiguous allocation suffers from external fragmentation.

8. **Know when copy-on-write is beneficial**: Particularly useful in fork() operations where child processes often call exec() immediately, making the initial copy unnecessary.