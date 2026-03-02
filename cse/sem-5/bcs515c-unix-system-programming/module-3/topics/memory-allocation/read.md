# Memory Allocation

## Introduction

Memory allocation constitutes a fundamental aspect of operating system design, encompassing the systematic assignment of memory space to processes and data structures. In any computer system, the physical memory (RAM) represents a finite resource that must be managed efficiently to support multiple concurrent processes. The operating system functions as a memory manager, maintaining precise records of memory usage, allocating memory to processes upon request, and reclaiming memory upon process termination.

The significance of memory allocation in modern computing cannot be overstated. Effective memory management directly influences system performance, throughput, and multiprogramming efficiency. When memory allocation occurs efficiently, the system can accommodate more processes in memory simultaneously, resulting in improved CPU utilization. Conversely, inadequate memory management leads to fragmentation, excessive swapping, and degraded performance. Comprehending various memory allocation techniques is essential for computer science engineers, as this knowledge forms the foundation for understanding how operating systems manage one of the most critical resources in a computer system.

This topic examines fundamental approaches to memory allocation, including contiguous allocation methods, non-contiguous techniques such as paging and segmentation, and the algorithms employed to satisfy memory requests. We analyze the advantages and disadvantages of each method, along with the fragmentation problem that inherently affects memory management systems.

## Key Concepts

### Contiguous Memory Allocation

In contiguous memory allocation, each process occupies a single continuous block of memory. This approach represents the earliest and simplest method of memory management in operating systems.

**Fixed Partitioning:** Memory divides into a fixed number of partitions at system initialization. Each partition can accommodate one process, and the number of partitions determines the maximum degree of multiprogramming. Two variants exist:

- **Equal-size partitions:** All partitions maintain identical dimensions. Any process fitting within a partition may be loaded into it. However, when a process is smaller than the partition size, valuable memory space remains unused, creating internal fragmentation.
- **Unequal-size partitions:** Partitions vary in size, enabling better matching between process requirements and available partitions. This reduces internal fragmentation but increases complexity in the allocation algorithm.

**Variable Partitioning:** Memory is not pre-partitioned. Instead, when a process arrives, a partition of exactly the required size is created dynamically. This approach eliminates internal fragmentation but requires sophisticated allocation algorithms to manage the free memory space effectively. The system maintains a list of free holes (available memory blocks) and updates this list upon each allocation and deallocation.

### Memory Allocation Algorithms

When a process requires memory, the operating system must locate a suitable hole (free block) in memory. Several algorithms address this requirement:

**First Fit:** The memory manager scans the list of free holes from the beginning and allocates the first hole sufficiently large to accommodate the process. This algorithm executes quickly because it minimizes search time. Empirical studies demonstrate that first fit tends to leave larger holes toward the beginning of memory, though it may prematurely consume smaller holes that could satisfy future requests.

**Best Fit:** The entire list of free holes is searched to find the smallest hole that can accommodate the process. This algorithm produces the smallest leftover hole, theoretically minimizing wasted space. However, it requires searching the entire list and tends to produce numerous small fragments that may be unusable for larger processes. Best fit, despite its name, does not always yield optimal memory utilization in practice.

**Worst Fit:** The largest available hole is selected for allocation. This approach attempts to preserve large leftover holes that may accommodate future larger processes. However, it rapidly consumes the largest holes and may prove impractical in scenarios with predominantly small process sizes.

**Next Fit:** Similar to first fit, but the search begins from the point where the last allocation ended. This distributes allocations more uniformly throughout memory. Performance characteristics remain comparable to first fit, with both algorithms typically requiring O(n) time where n represents the number of free holes.

### Fragmentation

Fragmentation represents a major challenge in memory management, wherein memory space cannot be utilized effectively despite adequate total capacity.

**Internal Fragmentation:** Occurs when allocated memory exceeds the requested memory. The difference between allocated and requested sizes constitutes wasted space. This phenomenon prevails in fixed partitioning and paging systems. For instance, if a process requests 10 KB and the system allocates in 4 KB pages, 2 KB remains wasted per page. Internal fragmentation percentage is calculated as (allocated - requested) / allocated × 100.

**External Fragmentation:** Occurs when sufficient total memory space exists to satisfy a request, but the available space is not contiguous. This manifests in systems using variable partitioning and segmentation. The "50-percent rule" empirically suggests that external fragmentation may affect approximately 50% of memory in systems employing first fit allocation. External fragmentation is formally defined as the sum of sizes of all holes minus the actual memory requests.

**Compaction:** A technique to combat external fragmentation wherein the operating system periodically moves all free memory into one contiguous block. This process requires relocating all processes in memory, which necessitates complex address translation mechanisms and significant CPU time. Compaction is typically performed during system idle periods or when memory allocation fails due to insufficient contiguous space.

### Paging

Paging is a non-contiguous memory management technique that eliminates external fragmentation by dividing both physical memory and process address spaces into fixed-size blocks.

**Basic Concepts:**

- **Frames:** Physical memory divides into fixed-size blocks called frames, typically ranging from 4 KB to 8 KB in modern systems.
- **Pages:** Logical memory (process address space) divides into pages of identical size to frames.
- **Page Table:** A data structure maintained by the operating system that maps virtual page numbers to physical frame numbers. Each process possesses its own page table.
- **Offset:** The remaining bits after the page number, representing the displacement within the page.

**Address Translation:** The CPU generates a virtual address comprising two components: the page number (p) and the offset (d). The page number indexes the page table to retrieve the corresponding frame number (f). The physical address is constructed by combining the frame number with the offset: Physical Address = (f × page_size) + d. This translation is performed by the Memory Management Unit (MMU), a hardware component dedicated to address translation.

**Advantages of Paging:**

- Eliminates external fragmentation completely
- Allows non-contiguous allocation of physical memory
- Simplifies memory allocation as any free frame can satisfy a request
- Facilitates process isolation and memory protection
- Supports efficient virtual memory implementation

**Disadvantages of Paging:**

- Introduces internal fragmentation (last page of each process may be partially unused)
- Requires additional hardware support (MMU) and complex page tables
- Page table overhead increases with larger address spaces
- Memory access time increases due to two memory accesses (page table lookup + actual memory access)

**Translation Lookaside Buffer (TLB):** To mitigate the performance overhead of page table lookups, modern systems employ a specialized hardware cache called the TLB. The TLB stores recently used page table entries, enabling faster address translation. TLB hit rates typically exceed 90% in well-designed systems, significantly improving effective memory access time.

### Segmentation

Segmentation represents an alternative memory management technique that divides a process's address space into logically meaningful segments such as code, data, stack, and heap. Unlike paging, which uses fixed-size blocks, segmentation employs variable-sized segments defined by the programmer or compiler.

Each segment possesses a segment number and an offset within that segment. A segment table maps segment numbers to base addresses and limit (size) values. The hardware ensures that offsets do not exceed segment limits, providing natural memory protection. Segmentation naturally reflects program structure but may suffer from external fragmentation as segments must be allocated contiguously.

Modern operating systems frequently combine segmentation with paging, using segmentation for logical organization and paging for physical memory management. This hybrid approach leverages advantages of both techniques while minimizing their respective drawbacks.