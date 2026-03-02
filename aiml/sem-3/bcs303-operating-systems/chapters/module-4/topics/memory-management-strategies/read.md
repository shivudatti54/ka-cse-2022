# Memory Management Strategies

## Introduction

Memory management is one of the most critical functions of any operating system. In modern computer systems, the main memory (RAM) is a finite and expensive resource that must be efficiently allocated among multiple processes. Memory management strategies refer to the various techniques and approaches that operating systems employ to manage the allocation, deallocation, and organization of main memory for processes.

The importance of memory management cannot be overstated in the context of DU's Computer Science curriculum. Understanding these strategies is essential for several reasons. First, they enable multiprogramming, allowing multiple processes to reside in memory simultaneously, which maximizes CPU utilization. Second, they provide memory protection, ensuring that one process cannot interfere with the memory space of another. Third, they offer memory efficiency by minimizing internal and external fragmentation. Finally, they enable virtual memory, which gives the illusion of having more memory than physically available.

This topic builds upon fundamental concepts of memory management and explores the three primary strategies: Contiguous Memory Allocation, Paging, and Segmentation. Each strategy has its advantages and disadvantages, and modern operating systems often employ hybrid approaches that combine the best features of each.

## Key Concepts

### 1. Contiguous Memory Allocation

Contiguous memory allocation is the simplest memory management strategy where each process is allocated a single continuous block of memory. This approach is further divided into two types:

**Fixed Partitioning:** The memory is divided into a fixed number of partitions at system startup. Each partition can hold one process. The number of partitions limits the maximum number of processes that can be in memory simultaneously (degree of multiprogramming). This method suffers from internal fragmentation—wasted space within a partition when the process is smaller than the partition.

**Variable Partitioning:** Memory is divided dynamically based on the exact size of each process. When a process arrives, a block of memory exactly matching its size is allocated. This method uses only the exact memory required, eliminating internal fragmentation. However, it suffers from external fragmentation—small holes of free memory scattered throughout that cannot satisfy large requests.

**Memory Allocation Algorithms:**
- **First Fit:** Allocate the first hole that is large enough. Fast and typically allocates quickly.
- **Best Fit:** Allocate the smallest hole that is large enough. Minimizes wasted space but requires searching all holes.
- **Worst Fit:** Allocate the largest hole available. Creates larger leftover holes that may be useful.

### 2. Paging

Paging is a memory management strategy that eliminates external fragmentation by dividing both physical memory and logical memory into fixed-size blocks. Physical memory is divided into frames, and logical memory is divided into pages. The size of frames and pages must be equal, typically being powers of 2 (ranging from 512 bytes to 8KB).

The operating system maintains a page table for each process. The page table maps virtual page numbers to physical frame numbers. When a process accesses a memory location, the CPU uses the page number to index into the page table and obtain the corresponding frame number. The offset within the page is then added to the frame number to get the physical address.

**Advantages of Paging:**
- Eliminates external fragmentation
- Provides simple memory allocation (any free frame can be assigned to any process)
- Facilitates memory protection through page-level permissions
- Supports efficient sharing of memory pages between processes

**Disadvantages:**
- Introduces internal fragmentation (unused space in the last page)
- Requires hardware support (MMU - Memory Management Unit)
- Page tables can become large for processes with large address spaces (解决方案: multi-level page tables, inverted page tables)

### 3. Segmentation

Segmentation is a memory management strategy that divides memory into variable-sized segments based on the logical divisions of a program (code, data, stack, heap). Each segment has a name (segment number) and a length. Unlike paging, segmentation reflects the user's view of memory.

The logical address in segmentation consists of a segment number and an offset within that segment. A segment table stores the base address (starting location) and limit (length) for each segment. The CPU verifies that the offset is within the segment's limit before adding the base to get the physical address.

**Advantages of Segmentation:**
- Reflects natural logical structure of programs
- Eliminates internal fragmentation within segments (variable-sized)
- Provides easier code and data protection (different permissions per segment)
- Enables dynamic linking of libraries
- Simplifies sharing of code and data segments

**Disadvantages:**
- Suffers from external fragmentation (segments must be placed contiguously)
- Requires hardware support
- Segment allocation and deallocation is more complex

### 4. Virtual Memory and Demand Paging

Virtual memory is an extension of both paging and segmentation that gives processes access to more memory than physically available. It uses the concept of demand paging—pages are loaded into memory only when needed (upon a page fault).

When a process accesses a page not in memory, the operating system:
1. Identifies the location of the page on disk
2. Finds a free frame in physical memory
3. Loads the page from disk into the frame
4. Updates the page table
5. Restarts the interrupted instruction

### 5. Page Replacement Algorithms

When all frames are occupied and a page fault occurs, the operating system must replace an existing page. The choice of which page to replace is critical for performance:

- **FIFO (First In First Out):** Replace the oldest page. Simple but performs poorly because it may evict frequently used pages.
- **Optimal (OPT):** Replace the page that will not be used for the longest time in the future. Theoretical optimum but impossible to implement practically.
- **LRU (Least Recently Used):** Replace the page that has not been used for the longest time. Excellent approximation of OPT but requires hardware support.
- **NFU (Not Frequently Used):** Counts page references; replaces the page with lowest count.
- **Second Chance:** Modification of FIFO; gives pages a second chance if their reference bit is set.

## Examples

### Example 1: Contiguous Memory Allocation - First Fit

Consider a memory with holes at the following addresses (size in KB):
- Hole A: 100KB starting at 0K
- Hole B: 300KB starting at 200K
- Hole C: 150KB starting at 600K
- Hole D: 200KB starting at 800K

A process requesting 250KB arrives. Using First Fit:
- Check Hole A (100KB) - Too small
- Check Hole B (300KB) - Sufficient!
- Allocate process to Hole B at address 200K

After allocation, Hole B becomes: 50KB at address 450K

### Example 2: Paging Translation

A system uses paging with:
- Page size: 4KB (2^12 bytes)
- Logical address space: 32 bits
- Physical memory: 4GB (2^32 bytes)

Given a logical address: 0x1234A7B8

**Step 1: Calculate page number and offset**
- Offset bits = log2(4096) = 12 bits
- Page number = 0x1234A7B8 >> 12 = 0x1234A
- Offset = 0x1234A7B8 & 0xFFF = 0x7B8

**Step 2: Look up page table**
If page table entry for page 0x1234A shows frame number 0x54321:
- Physical address = (frame number << 12) + offset
- Physical address = (0x54321 << 12) + 0x7B8
- Physical address = 0x543217B8

### Example 3: Page Fault Calculation

A process has 5 pages (0-4) and the system can hold 3 frames. The page reference string is: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5

Using LRU replacement:
- Frame 1: Load page 1 (1 fault)
- Frame 2: Load page 2 (2 faults)
- Frame 3: Load page 3 (3 faults)
- Need page 4: Replace page 1 (LRU), load page 4 (4 faults)
- Need page 1: Replace page 2 (LRU), load page 1 (5 faults)
- Need page 2: Replace page 3 (LRU), load page 2 (6 faults)
- Need page 5: Replace page 4 (LRU), load page 5 (7 faults)
- Need page 1: Already in memory (hit)
- Need page 2: Already in memory (hit)
- Need page 3: Replace page 1 (LRU), load page 3 (8 faults)
- Need page 4: Replace page 2 (LRU), load page 4 (9 faults)
- Need page 5: Already in memory (hit)

Total page faults: 9

## Exam Tips

1. **Understand the difference between internal and external fragmentation**: Internal fragmentation occurs in fixed-sized units (paging, fixed partitions) when allocated memory exceeds needed memory. External fragmentation occurs in variable-sized allocation (variable partitions, segmentation) when free memory becomes scattered.

2. **Know when to use each strategy**: Contiguous allocation for simple systems; paging for systems requiring efficient memory utilization and protection; segmentation when logical program structure matters; virtual memory for systems needing more memory than physically available.

3. **Remember the page replacement algorithms**: FIFO is simple but suboptimal; LRU is excellent but requires special hardware; Optimal is theoretical. Understand Belady's anomaly—FIFO can have more faults with more frames.

4. **Calculate effective access time**: For demand paging, effective access time = (1 - p) × memory access time + p × page fault time, where p is page fault probability.

5. **Understand working set model**: The working set is the set of pages a process is currently using. The operating system must maintain enough frames to hold the working set to minimize thrashing.

6. **Address translation**: Be able to convert between logical and physical addresses for both paging and segmentation. Know that physical address = base + offset (segmentation) or (frame × page size) + offset (paging).

7. **Compare advantages and disadvantages**: In exam questions, you may be asked to compare strategies. Paging eliminates external fragmentation but has internal fragmentation; segmentation reflects logical structure but suffers from external fragmentation.

8. **Virtual memory benefits**: Remember that virtual memory provides memory isolation, simplifies memory allocation for processes, enables sharing, and allows execution of programs larger than physical memory.