# Memory Management Strategies

## Introduction

Memory management is one of the most critical functions of any operating system. In modern computing environments, where multiple processes compete for limited physical memory, efficient memory management strategies determine system performance, throughput, and user experience. This topic explores the various techniques operating systems employ to manage memory effectively, from simple swapping mechanisms to sophisticated virtual memory systems.

The evolution of memory management strategies reflects the broader history of operating system development. Early systems used simple contiguous allocation schemes, while contemporary operating systems employ complex combinations of paging, segmentation, and demand paging to maximize memory utilization. Understanding these strategies is essential for any computer science student, as they form the foundation for comprehending how operating systems abstract physical memory and provide each process with its own virtual address space.

In the University of Delhi's Computer Science curriculum, memory management strategies carry significant weight in both internal assessments and end-semester examinations. The concepts covered here frequently appear in numerical problems and theoretical questions, making thorough understanding imperative for academic success.

## Key Concepts

### Swapping

Swapping is one of the simplest memory management strategies, where an entire process is moved between main memory and secondary storage (typically disk). When physical memory becomes full, the operating system selects a process to move to swap space (a reserved area on disk) to free up memory for other processes. When the swapped-out process needs to execute again, it is moved back into memory.

The key advantage of swapping is its simplicity—it allows the operating system to manage memory even when the total size of all running processes exceeds physical memory. However, swapping incurs significant overhead due to the time required to transfer data between memory and disk. Modern systems use swapping sparingly, preferring more granular approaches like paging.

### Contiguous Memory Allocation

In contiguous memory allocation, each process is assigned a single continuous block of memory. The operating system maintains a table (often called the memory allocation table) tracking which memory regions are free and which are allocated to processes.

Three main algorithms govern contiguous allocation:

**First-Fit**: The operating system scans memory from the beginning and allocates the first available block large enough to accommodate the process. This method is fast but may lead to external fragmentation.

**Best-Fit**: The system finds the smallest free block that can accommodate the process. While this minimizes wasted space, it requires scanning the entire memory table and can also lead to fragmentation.

**Worst-Fit**: The largest available block is selected for allocation. This approach attempts to leave large remaining blocks but generally performs poorly in practice due to inefficient memory utilization.

External fragmentation occurs when free memory is divided into small non-contiguous blocks, making it impossible to allocate a large process despite sufficient total free memory. Compaction (moving all allocated blocks together) can resolve fragmentation but requires significant CPU time.

### Paging

Paging eliminates external fragmentation by dividing both physical memory and virtual memory into fixed-size blocks called frames and pages respectively. Each process operates with its own page table that maps virtual pages to physical frames.

When a process accesses a memory location, the Memory Management Unit (MMU) translates the virtual address to a physical address using the page table. If the required page is not in memory (page fault), the operating system loads it from secondary storage.

The page table itself requires management. For systems with large address spaces, multi-level page tables reduce memory overhead by mapping only allocated pages. Inverted page tables store one entry per physical frame, reducing memory consumption for large systems.

### Segmentation

Segmentation provides a different approach by dividing memory into logical segments based on program structure—code, data, stack, heap. Each segment has a base address and limit, allowing variable-sized memory regions that reflect program organization.

Unlike paging (which is invisible to programmers), segmentation is programmer-visible. Developers can reference memory using segment:offset pairs, making code more readable and maintainable. For example, the stack segment and code segment are naturally separated, providing protection against certain programming errors.

Modern systems typically combine segmentation with paging, using segmentation for logical organization and paging for physical memory management.

### Virtual Memory Management

Virtual memory extends available memory beyond physical RAM by using disk space as an extension of physical memory. This allows programs larger than physical memory to execute and enables memory protection between processes.

**Demand Paging**: Pages are loaded into memory only when referenced (on-demand). This approach reduces initial load time and memory usage. When a page fault occurs, the operating system:
1. Determines the location of the required page on disk
2. Locates a free frame in memory
3. Loads the page from disk into the frame
4. Updates the page table
5. Restarts the interrupted instruction

**Copy-on-Write (COW)**: This optimization allows parent and child processes to share memory pages initially. When either process modifies a shared page, the operating system creates a separate copy for that process. This is particularly useful in fork() system calls, significantly improving performance for process creation.

### Page Replacement Algorithms

When all physical frames are occupied and a page fault occurs, the operating system must select a victim page to evict. The choice of replacement algorithm significantly impacts system performance.

**FIFO (First-In-First-Out)**: The oldest page in memory is replaced. Simple to implement but may evict frequently used pages.

**Optimal (OPT)**: Replaces the page that will not be used for the longest time in the future. This algorithm provides the best performance but requires future knowledge, making it unrealizable in practice. It serves as a theoretical benchmark.

**Least Recently Used (LRU)**: Replaces the page that has not been used for the longest time. This approximation of OPT works well in practice but requires hardware support for tracking page usage.

**Clock (Second Chance)**: A practical approximation of LRU using a reference bit. Pages are examined in circular order; those with reference bit set are given a second chance while those cleared are replaced.

### Thrashing

Thrashing occurs when the system spends excessive time swapping pages in and out rather than executing processes. It happens when processes do not have enough frames allocated—they constantly page fault, triggering more evictions, which causes more faults in a vicious cycle.

Symptoms of thrashing include high CPU utilization (due to context switching overhead), low throughput, and disk activity (constant paging). Solutions include:
- Working set model: Keep pages that a process has recently used in memory
- Page fault frequency: Adjust allocation based on page fault rates
- Suspending processes: Temporarily move some processes to disk

## Examples

### Example 1: Calculating Effective Access Time with Page Faults

**Problem**: A system has memory access time of 100 nanoseconds. If the page fault rate is 0.01 (1%) and page fault service time is 10 milliseconds, calculate the effective access time.

**Solution**:

Effective Access Time (EAT) = (1 - p) × Memory Access Time + p × Page Fault Service Time

Where p = page fault rate

EAT = (1 - 0.01) × 100 ns + 0.01 × 10,000,000 ns
EAT = 0.99 × 100 + 0.01 × 10,000,000
EAT = 99 ns + 100,000 ns
EAT = 100,099 ns ≈ 100 microseconds

This example demonstrates how even a small page fault rate dramatically increases access time when page fault service is expensive.

### Example 2: FIFO Page Replacement

**Problem**: Consider a system with 3 frames. The page reference string is: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5. Calculate the number of page faults using FIFO algorithm.

**Solution**:

Step-by-step execution:
- Reference 1: Page fault (load into frame 1)
- Reference 2: Page fault (load into frame 2)
- Reference 3: Page fault (load into frame 3)
- Reference 4: Page fault (evict page 1, load page 4)
- Reference 1: Page fault (evict page 2, load page 1)
- Reference 2: Page fault (evict page 3, load page 2)
- Reference 5: Page fault (evict page 4, load page 5)
- Reference 1: Hit (page 1 in memory)
- Reference 2: Hit (page 2 in memory)
- Reference 3: Page fault (evict page 1, load page 3)
- Reference 4: Page fault (evict page 2, load page 4)
- Reference 5: Page fault (evict page 3, load page 5)

Total page faults = 10

### Example 3: Working Set Calculation

**Problem**: A process has the following page references in its last 10 memory accesses: 2, 3, 5, 2, 3, 7, 2, 3, 5, 7. If the working set window is τ = 4, what is the working set size?

**Solution**:

Working set is defined as the set of pages referenced in the last τ (tau) references.

Last 4 references: 3, 5, 2, 7 (from position 7 to 10)
Unique pages in this window: {3, 5, 2, 7} = 4 pages

Therefore, working set size = 4

## Exam Tips

1. **Numerical Problems**: Examination questions frequently require calculating effective memory access time with page faults, counting page faults using FIFO/LRU algorithms, and computing hit ratios. Practice these problems extensively.

2. **Difference Between Paging and Segmentation**: Remember that paging eliminates external fragmentation while segmentation provides logical memory organization. Be prepared to explain when each is advantageous.

3. **Belady's Anomaly**: In FIFO page replacement, increasing the number of frames can sometimes increase page faults. This counter-intuitive phenomenon (Belady's anomaly) is a common examination topic.

4. **Page Table Types**: Know the differences between hierarchical page tables, inverted page tables, and hashed page tables. Understand when each is appropriate (e.g., inverted page tables for large address spaces).

5. **Thrashing Explanation**: Be prepared to explain thrashing conceptually, identify its causes, and suggest solutions. This is a frequently asked short-answer question.

6. **Virtual Memory Benefits**: Understand how virtual memory provides process isolation, simplifies memory allocation, and enables programs larger than physical memory.

7. **Internal vs External Fragmentation**: Paging suffers from internal fragmentation (unused space within allocated pages), while contiguous allocation suffers from external fragmentation (scattered free blocks). Know how to calculate fragmentation in each case.

8. **Address Translation**: Be able to convert logical addresses to physical addresses using page tables. Know how to calculate page number, offset, frame number, and physical address components.

9. **Copy-on-Write Purpose**: Understand how COW optimizes fork() operations by deferring page copies until necessary, reducing memory overhead and improving performance.

10. **Recent Exam Patterns**: DU examinations often include questions comparing different algorithms, analyzing page fault scenarios, and explaining memory management concepts in detail. Focus on understanding trade-offs between approaches.