# Contiguous Memory Allocation

## Introduction

Contiguous memory allocation is one of the fundamental memory management techniques used in operating systems. In this approach, each process is allocated a single continuous block of physical memory that is sufficient to hold the entire process. This means that when a program is loaded into memory, it occupies a single, unbroken segment of RAM, and all its instructions and data are stored in consecutive memory locations. This method represents the simplest form of memory management and was widely used in early operating systems before the advent of more sophisticated techniques like paging and segmentation.

The importance of contiguous memory allocation lies in its simplicity and efficiency. When a process is allocated a contiguous block of memory, the CPU can access any part of the process using simple arithmetic operations. The memory addresses within the process can be easily translated to physical addresses by adding a base address, making the memory management unit (MMU) implementation relatively straightforward. However, this technique also presents significant challenges, particularly regarding memory fragmentation, which has led to the development of alternative approaches in modern operating systems.

Understanding contiguous memory allocation is crucial for computer science students because it provides the foundation for understanding more complex memory management techniques. The problems of external and internal fragmentation, the various allocation algorithms, and the concept of memory compaction all originate from the constraints imposed by contiguous allocation. Moreover, many concepts in virtual memory and paging systems build upon the principles established in contiguous memory allocation.

## Key Concepts

### Fixed Partitioning

Fixed partitioning was the earliest approach to memory management, where the operating system divides main memory into a predetermined number of partitions at system startup. These partitions can be of equal size or unequal sizes, with the latter approach being more flexible as it can accommodate processes of varying sizes more efficiently. When a process needs to be loaded, the operating system selects a partition that is large enough to hold the entire process.

The major drawback of fixed partitioning is internal fragmentation. Since each partition has a fixed size, a process that is smaller than its allocated partition will not use the entire partition, leaving some memory unused. For example, if a process requiring 10 MB is loaded into a 16 MB partition, 6 MB of memory remains wasted. This inefficiency becomes more pronounced when there are many small processes or when the distribution of process sizes does not match the partition sizes.

Fixed partitioning also suffer from a limitation on the degree of multiprogramming. Since the number of partitions is fixed, the maximum number of processes that can be in memory at any given time is limited by this number. This constraint reduces system throughput and CPU utilization, especially in environments where many processes compete for memory.

### Variable Partitioning

Variable partitioning addresses some of the limitations of fixed partitioning by allowing partitions to be created dynamically based on the exact memory requirements of each process. When a process arrives, the operating system allocates exactly the amount of memory requested, creating a partition that precisely fits the process. This eliminates internal fragmentation and allows for more efficient memory utilization.

In variable partitioning, the memory is initially a single large hole. As processes are loaded and terminated, the memory becomes partitioned into regions of allocated memory and regions of free memory called holes. The operating system must maintain a record of these holes and allocate memory from them when new processes require memory. This dynamic nature of variable partitioning requires more sophisticated memory management data structures and algorithms.

Variable partitioning introduces the problem of external fragmentation. When processes terminate and their memory is released, the resulting holes may be too small or scattered to be useful for larger processes. Even though the total free memory might be sufficient for a new process, none of the individual holes may be large enough. This external fragmentation can eventually make it impossible to load new processes even when adequate total memory is available.

### Memory Allocation Algorithms

Several algorithms exist for allocating memory from the collection of holes in a variable partitioning system. Each algorithm has its own characteristics in terms of speed, memory utilization, and overhead.

First Fit allocates memory by scanning the list of holes from the beginning and selecting the first hole that is large enough to accommodate the process. This algorithm is fast because it minimizes the number of holes examined, and it tends to allocate memory from holes near the beginning of memory, which often contain larger holes. First Fit is generally efficient in terms of both time and memory utilization, making it a popular choice in practice.

Best Fit allocates memory by scanning all holes and selecting the smallest hole that is large enough to accommodate the process. This algorithm attempts to minimize wasted memory by finding the closest fit possible. However, Best Fit requires scanning all holes, making it slower than First Fit, especially in systems with many small holes. Additionally, Best Fit tends to create many small holes, which can increase external fragmentation over time.

Worst Fit selects the largest available hole for allocation. The rationale behind this approach is that the remaining portion after allocation will still be large enough to be useful for other processes. However, Worst Fit performs poorly in practice because it tends to break down large holes into smaller ones, accelerating the fragmentation problem. It also requires scanning all holes, similar to Best Fit.

Next Fit is a variant of First Fit that starts searching from where the last allocation ended. This circular scanning approach tends to distribute allocations more evenly throughout memory, reducing the likelihood of all small holes accumulating at one end. Next Fit performs similarly to First Fit in terms of speed and memory utilization.

### Address Translation in Contiguous Allocation

In a system using contiguous memory allocation, the logical (or virtual) address generated by a CPU must be translated to a physical address in main memory. This translation is managed by the Memory Management Unit (MMU) using two special registers: the base register and the limit register.

The base register holds the starting physical address of the process's memory partition, while the limit register holds the size of the partition. When the CPU generates a logical address, the MMU adds the base register value to the logical address to produce the physical address. Before performing this translation, the MMU checks whether the logical address is within the bounds specified by the limit register. If the address exceeds the limit, a trap to the operating system is generated, indicating a memory protection violation.

The translation process can be expressed as: Physical Address = Base Register + Logical Address. The logical address must be in the range [0, limit register] for the access to be valid. This mechanism provides both memory management and protection, preventing processes from accessing memory belonging to other processes.

### Compaction

Compaction is a technique used to combat external fragmentation in contiguous memory allocation systems. It works by moving all allocated memory blocks together, effectively consolidating all free memory into a single large hole. This allows the operating system to allocate larger processes that would otherwise fail due to insufficient contiguous space.

However, compaction is an expensive operation that requires moving entire processes in memory. During compaction, all processes must be temporarily stopped, and their memory contents must be copied to new locations while updating all pointers and references. This process can be time-consuming and may significantly impact system performance. Additionally, compaction requires that processes be relocatable, meaning they can be moved during execution without incorrect behavior.

The decision of when and how often to perform compaction involves trade-offs. Running compaction too frequently wastes CPU time, while running it too infrequently may lead to excessive external fragmentation and inability to load new processes. Many operating systems use heuristic approaches to determine when compaction is necessary.

## Examples

### Example 1: First Fit Allocation

Consider a memory system with holes at the following locations: Hole A from 0KB to 100KB, Hole B from 150KB to 300KB, Hole C from 400KB to 500KB. A new process P1 requires 80KB of memory.

Using First Fit, we scan from the beginning:
- Hole A (0-100KB): 100KB >= 80KB ✓, allocate here
- Physical address: Base of Hole A = 0KB
- Remaining free memory in Hole A: 100KB - 80KB = 20KB (from 80KB to 100KB)

After allocation, the holes become:
- Hole A' (80KB to 100KB): 20KB
- Hole B (150KB to 300KB): 150KB
- Hole C (400KB to 500KB): 100KB

### Example 2: Best Fit Allocation

Using the same initial memory configuration with holes A (0-100KB), B (150-300KB), and C (400-500KB), allocate a process P2 requiring 120KB of memory.

Using Best Fit, we examine all holes:
- Hole A: 100KB < 120KB (not large enough)
- Hole B: 150KB >= 120KB, leftover = 150KB - 120KB = 30KB
- Hole C: 100KB < 120KB (not large enough)

Hole B is the smallest suitable hole, so we allocate from Hole B:
- Base address: 150KB
- Remaining in Hole B: 30KB (from 270KB to 300KB)

After allocation:
- Hole A (0-100KB): 100KB
- Hole B' (270KB to 300KB): 30KB
- Hole C (400KB to 500KB): 100KB

Note that Best Fit has created a smaller hole compared to what First Fit would have created (allocating from Hole B at 150KB would leave 30KB, while allocating from the larger hole is more efficient for future large allocations).

### Example 3: Address Translation

Assume a process is loaded at physical memory location 1000 and has a limit (size) of 500. The process generates the following logical addresses: 0, 100, 200, 450, 500.

For each logical address:
- Logical address 0: Physical = 1000 + 0 = 1000 (valid)
- Logical address 100: Physical = 1000 + 100 = 1100 (valid)
- Logical address 200: Physical = 1000 + 200 = 1200 (valid)
- Logical address 450: Physical = 1000 + 450 = 1450 (valid)
- Logical address 500: Physical = 1000 + 500 = 1500 (INVALID - exceeds limit of 500)

When the process attempts to access logical address 500, the MMU detects that 500 is not in the range [0, 500] and triggers a memory fault, causing a trap to the operating system.

## Exam Tips

1. Remember the key difference between internal and external fragmentation. Internal fragmentation occurs in fixed partitioning when allocated memory exceeds process requirements, while external fragmentation occurs in variable partitioning when free memory becomes scattered in small non-contiguous blocks.

2. For exam questions involving allocation algorithms, always show your working step by step. Start by listing initial holes, then show how each allocation modifies the hole list.

3. In address translation questions, always verify that the logical address is within bounds before performing the base register addition. An out-of-bounds address indicates a memory protection error.

4. Know the relative advantages and disadvantages of each allocation algorithm. First Fit is generally preferred in practice due to its speed and reasonable memory utilization.

5. Remember that compaction is the only solution for external fragmentation in contiguous allocation systems, but it has significant performance overhead.

6. The degree of multiprogramming in fixed partitioning is limited by the number of partitions, regardless of total available memory.

7. Variable partitioning eliminates internal fragmentation but cannot completely avoid external fragmentation. This trade-off is an important concept in memory management.