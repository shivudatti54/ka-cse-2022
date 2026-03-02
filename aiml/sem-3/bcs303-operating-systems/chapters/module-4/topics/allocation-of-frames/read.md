# Allocation of Frames

## Introduction

In virtual memory systems that use paging, the physical memory is divided into fixed-size blocks called frames, while the logical memory (process address space) is divided into pages of the same size. The allocation of frames is a critical memory management function that determines how physical memory frames are distributed among competing processes. This decision directly impacts system performance, throughput, and memory utilization.

When a process needs to execute, its pages must be loaded into physical memory frames before the CPU can access them. The operating system must decide how many frames to allocate to each process, which processes should receive frames when memory is scarce, and how to handle situations where all frames are occupied. Efficient frame allocation becomes particularly crucial in systems with multiple processes competing for limited physical memory, as poor allocation decisions can lead to excessive page faults, thrashing, and degraded system performance.

The University of Delhi Computer Science curriculum covers this topic as part of the broader Memory Management module, building upon concepts of paging and serving as a foundation for understanding page replacement algorithms. Mastery of frame allocation strategies is essential for understanding how operating systems balance the memory requirements of multiple processes while maximizing overall system efficiency.

## Key Concepts

### Frames and Page Tables

A frame represents the smallest unit of physical memory in a paging system. Typically, frame sizes range from 512 bytes to 8 KB, depending on the system architecture. Each frame can hold exactly one page of data. The page table serves as the mapping structure that tracks which frames are assigned to which pages of a process. When a process accesses a page that is not currently in memory (page fault occurs), the operating system must allocate a free frame, load the required page into that frame, and update the page table accordingly.

The total number of frames in physical memory is determined by the amount of physical RAM divided by the frame size. For example, a system with 64 MB of physical memory and 4 KB frames has 16,384 total frames. These frames must be carefully managed and allocated among all running processes.

### Equal Allocation Strategy

In equal allocation, each process receives the same number of frames regardless of its size or priority. If there are m available frames and n processes in the system, each process receives m/n frames. This approach is simple to implement and provides fair treatment to all processes.

However, equal allocation has significant drawbacks. A small process with only a few pages does not need as many frames as a large process with extensive memory requirements. Conversely, a large process may suffer from excessive page faults if allocated only the same number of frames as a smaller process. For instance, if a system has 100 frames and 5 processes, each process receives 20 frames. A process needing only 15 frames wastes 5 frames, while a process requiring 50 frames faces severe memory pressure with only 20 frames.

### Proportional Allocation Strategy

Proportional allocation allocates frames to processes based on their size or other characteristics. A process with a larger address space receives a proportionally larger share of available frames. The allocation is calculated using the formula: allocation for process i = (size of process i / total size of all processes) × total available frames.

This approach addresses the main limitation of equal allocation by matching frame allocation to actual memory needs. A process with 100 KB of virtual memory in a system with 1000 KB total would receive 10% of available frames. Proportional allocation generally results in better memory utilization and fewer page faults compared to equal allocation, especially in systems with processes of varying sizes.

### Priority-Based Allocation

In priority-based allocation, processes with higher priority receive more frames than lower-priority processes. This approach recognizes that certain critical processes should receive preferential treatment in terms of memory allocation to ensure smooth execution. When a page fault occurs, the system may use a page replacement algorithm that considers process priority, potentially allowing lower-priority processes to lose frames to higher-priority ones.

This strategy is particularly useful in real-time systems or interactive environments where certain applications (such as operating system services or user-interactive programs) must maintain acceptable performance levels regardless of overall system load. However, priority-based allocation can lead to starvation of low-priority processes if not carefully managed.

### Global vs Local Allocation

Global frame allocation allows the page replacement algorithm to consider frames belonging to any process when replacing pages. A process can take frames from other processes if needed. This approach maximizes overall system throughput but can cause unpredictable performance for individual processes, as the number of frames available to a process may vary over time.

Local frame allocation restricts each process to using only its own allocated frames. When a page fault occurs, the process can only replace one of its own pages. This provides more predictable performance for each process but may lead to suboptimal system-wide resource utilization, as frames cannot be dynamically reallocated based on current needs.

### Working Set Model

The working set of a process is the set of pages that the process is currently using. According to the working set model, a process performs efficiently as long as its working set fits in allocated frames. The working set changes over time as the process executes different portions of its code and data.

The operating system can use the working set model to make intelligent frame allocation decisions. By monitoring which pages a process has accessed recently (using a reference bit or other hardware support), the system can estimate the working set size and adjust frame allocation accordingly. If a process's working set exceeds its allocated frames, the system may experience thrashing, where excessive time is spent on page fault handling rather than actual computation.

### Free Frame List

The operating system maintains a list of free (unallocated) frames that can be assigned to processes when needed. When a page fault occurs and no free frames are available, the system must first reclaim frames by either using a page replacement algorithm or, in extreme cases, swapping entire processes out to secondary storage.

The free frame list is typically managed using data structures like linked lists or bitmaps. When frames are allocated, they are removed from the free list; when frames are freed (such as when a process terminates or a page is evicted), they are returned to the list. Maintaining an adequate number of free frames is essential for system responsiveness, as a shortage of free frames forces the system to perform expensive page replacement operations frequently.

## Examples

### Example 1: Equal Allocation Calculation

Consider a system with 64 frames and 4 processes in memory. Using equal allocation:

Frames per process = 64 / 4 = 16 frames

Process sizes: P1 = 10 pages, P2 = 25 pages, P3 = 5 pages, P4 = 30 pages

Analysis:
- P1 with 10 pages gets 16 frames (6 frames wasted)
- P2 with 25 pages gets 16 frames (likely insufficient, causing page faults)
- P3 with 5 pages gets 16 frames (11 frames wasted)
- P4 with 30 pages gets 16 frames (likely insufficient)

This example demonstrates the inefficiency of equal allocation when process sizes vary significantly.

### Example 2: Proportional Allocation Calculation

Using the same system with 64 frames and the process sizes from Example 1:

Total pages across all processes = 10 + 25 + 5 + 30 = 70 pages

Allocation for each process:
- P1: (10/70) × 64 = 9.14 ≈ 9 frames
- P2: (25/70) × 64 = 22.86 ≈ 23 frames
- P3: (5/70) × 64 = 4.57 ≈ 5 frames
- P4: (30/70) × 64 = 27.43 ≈ 27 frames

Total allocated: 9 + 23 + 5 + 27 = 64 frames

This allocation better matches actual process needs, providing more frames to larger processes while giving smaller processes only what they require.

### Example 3: Global vs Local Replacement Impact

Suppose process P1 has 10 frames allocated and experiences a page fault. With local replacement, P1 can only replace one of its own pages. If P1's pages are all frequently used, this leads to repeated page faults. With global replacement, P1 might steal a frame from P2 if P2's pages are less frequently accessed, potentially reducing overall page faults. However, P2 might then experience a page fault when it needs its stolen page, illustrating the trade-off between local and global allocation strategies.

## Exam Tips

1. Understand the fundamental difference between frames and pages: frames are physical memory units, while pages are logical memory units.

2. Remember the three main allocation strategies: equal allocation, proportional allocation, and priority-based allocation, along with their respective advantages and disadvantages.

3. Clearly distinguish between global and local frame allocation, as this is a common examination question.

4. Know how to calculate proportional allocation using the formula: (process size / total size) × total frames.

5. The working set model helps determine if a process has sufficient frames to run efficiently without thrashing.

6. In exam questions, carefully read whether they ask for global or local replacement, as this changes the approach to solving the problem.

7. Free frame list management is essential for handling page faults—when all frames are allocated, the system must reclaim frames before servicing new page faults.

8. Realize that frame allocation directly impacts page fault rates and overall system performance, making it a critical design decision in operating systems.