# Contiguous Memory Allocation


## Table of Contents

- [Contiguous Memory Allocation](#contiguous-memory-allocation)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Fundamental Principles of Contiguous Memory Allocation](#fundamental-principles-of-contiguous-memory-allocation)
  - [Fixed Partitioning](#fixed-partitioning)
  - [Variable Partitioning](#variable-partitioning)
  - [Memory Allocation Algorithms](#memory-allocation-algorithms)
  - [Fragmentation Analysis](#fragmentation-analysis)
- [Examples](#examples)
  - [Example 1: Fixed Partitioning Calculation](#example-1-fixed-partitioning-calculation)
  - [Example 2: Variable Partitioning with First Fit](#example-2-variable-partitioning-with-first-fit)
  - [Example 3: Comparing Allocation Algorithms](#example-3-comparing-allocation-algorithms)
- [Exam Tips](#exam-tips)

## Introduction

Memory management is one of the fundamental responsibilities of any operating system, serving as the backbone for efficient program execution and system resource utilization. Among the various memory management strategies employed in operating systems, contiguous memory allocation represents the earliest and most straightforward approach to allocating primary memory to processes. This method ensures that each process occupies a single, continuous block of memory during its entire execution lifetime, simplifying both hardware implementation and memory access patterns.

The significance of contiguous memory allocation extends beyond its historical importance. While modern operating systems have evolved to employ more sophisticated techniques like paging and segmentation, understanding contiguous allocation remains crucial for several reasons. First, it provides the foundational concepts upon which more advanced memory management schemes are built. Second, embedded systems and certain real-time operating systems still utilize contiguous allocation due to its predictability and low overhead. Third, the problems of fragmentation that arise in contiguous allocation—internal and external fragmentation—reappear in various forms throughout computer science, making this topic essential for developing problem-solving skills in memory management.

In the context of the University of Delhi's Computer Science program, this topic forms a critical component of the operating systems curriculum. Students must master the mechanics of memory allocation, the various algorithms used to satisfy memory requests, and the trade-offs inherent in each approach. The examination patterns at DU emphasize conceptual clarity and practical problem-solving, making thorough understanding of contiguous allocation essential for academic success.

## Key Concepts

### Fundamental Principles of Contiguous Memory Allocation

Contiguous memory allocation is a memory management technique where each process is stored in a single continuous block of physical memory addresses. When a process arrives for execution, the operating system allocates a partition of memory large enough to hold the entire process image, including the code segment, data segment, stack segment, and any other memory regions the process requires. This partition remains assigned to the process until the process terminates, at which point the memory is released and becomes available for other processes.

The operating system maintains a memory allocation table that tracks which portions of physical memory are allocated to processes and which remain free. This table can be implemented using various data structures, including bitmaps, linked lists, or simple arrays, depending on the system's requirements and complexity. Each entry in this table typically records the starting address of a partition, its length, and its allocation status (either allocated to a specific process or free).

The CPU generates logical addresses during program execution, which must be translated into physical addresses before memory access can occur. In contiguous allocation systems, this translation is handled by two special registers: the base register and the limit register. The base register holds the starting physical address of the current process's partition, while the limit register contains the size of the partition. Every memory access is verified against these registers to ensure processes cannot access memory outside their allocated partitions, providing a simple form of memory protection.

### Fixed Partitioning

Fixed partitioning divides the entire physical memory into a predetermined number of partitions at system startup. These partitions can be either equal-sized or unequal-sized, each approach presenting distinct advantages and disadvantages. In equal-sized partitioning, memory is divided into N partitions of identical size, regardless of the actual memory requirements of processes. This approach simplifies the allocation logic but inevitably leads to inefficient memory utilization, as a small process occupying a large partition leaves wasted space that cannot be used by other processes.

Unequal-sized partitioning attempts to address this limitation by creating partitions of varying sizes. The system administrator or operating system configures partitions such that a variety of process sizes can be accommodated more efficiently. However, this approach introduces additional complexity in the allocation algorithm, as the system must decide which partition to assign to an incoming process. The number of partitions in fixed partitioning remains constant throughout the system's operation, limiting flexibility and potentially creating bottlenecks when all partitions are occupied.

Fixed partitioning inherently suffers from internal fragmentation, which refers to the unused memory space within an allocated partition. When a process of size 50 KB is assigned to a partition of size 100 KB, the remaining 50 KB cannot be utilized by other processes, representing wasted memory. The degree of internal fragmentation depends on the match between process sizes and partition sizes, making partition size selection a critical system design decision.

### Variable Partitioning

Variable partitioning, also known as dynamic partitioning, represents a more flexible approach where partitions are created dynamically based on the exact memory requirements of incoming processes. Unlike fixed partitioning, the number and size of partitions vary throughout system operation, with memory divided only when processes require allocation. This approach eliminates internal fragmentation in its purest form, as each partition exactly matches the size of the process it accommodates.

When a process arrives, the system searches for a free block of memory large enough to hold the process. Upon finding such a block, the system allocates exactly the amount of memory required, potentially splitting the free block into two: one allocated to the process and another containing the remaining free memory. When a process terminates, its allocated memory is released and merged with adjacent free blocks, a process called coalescing.

Variable partitioning introduces external fragmentation, where free memory exists in scattered non-contiguous blocks throughout the system. Although the total free memory might equal or exceed the memory requirement of a waiting process, no single block may be large enough to accommodate it. External fragmentation can become severe over time as processes are loaded and terminated, ultimately making it impossible to satisfy large memory requests despite sufficient total free memory.

### Memory Allocation Algorithms

When allocating memory using variable partitioning, the operating system must select which free block to use when multiple candidates exist. Several algorithms have been developed to make this selection, each with distinct characteristics affecting memory utilization and allocation speed.

The First Fit algorithm begins scanning memory from the beginning and selects the first free block large enough to accommodate the process. This approach is computationally efficient, requiring minimal search time on average, and tends to allocate memory quickly. However, it may not provide optimal memory utilization, as small processes placed early in memory can fragment large blocks needed for larger processes.

The Best Fit algorithm examines all free blocks and selects the one closest in size to the requested memory. This approach attempts to minimize wasted space by finding the smallest suitable block, theoretically providing the best memory utilization. However, best fit requires scanning the entire free space list and may produce smaller, less useful free fragments. Additionally, the computational overhead of searching all blocks can be significant in systems with many small free regions.

The Worst Fit algorithm selects the largest available free block, splitting it to accommodate the process and leaving a large remaining free block. This approach aims to leave large free areas capable of satisfying future large memory requests, potentially reducing external fragmentation. However, worst fit often produces smaller leftover blocks that may be useless for subsequent allocations, and the algorithm requires searching for the largest block.

The Next Fit algorithm functions similarly to first fit but maintains a pointer to the last allocated position. When a new allocation request arrives, scanning begins from this pointer rather than from the beginning of memory. This circular scanning approach distributes allocations throughout memory more evenly, potentially improving performance in certain scenarios and reducing the tendency for memory to become heavily fragmented in specific regions.

### Fragmentation Analysis

Internal fragmentation occurs in fixed partitioning when allocated partitions exceed process requirements, leaving unused space within the partition boundaries. The total internal fragmentation in a system equals the sum of differences between allocated partition sizes and actual process sizes across all active processes. With fixed partitioning, internal fragmentation is unavoidable unless process sizes perfectly match partition sizes, which rarely occurs in practice.

External fragmentation manifests as scattered free memory blocks following processes of varying sizes. The coalescing of adjacent free blocks can partially combat external fragmentation, but the fundamental problem persists as processes are loaded and terminated over time. The effectiveness of coalescing depends on the allocation and deallocation patterns, with some scenarios producing severe fragmentation despite coalescing efforts.

The 50-percent rule provides an empirical analysis of external fragmentation in first fit allocation. Research has demonstrated that, on average, external fragmentation consumes approximately 50 percent of total memory when using first fit allocation. This significant overhead represents a substantial inefficiency that motivated the development of alternative memory management techniques like paging and segmentation.

Memory compaction represents a technique for combating external fragmentation by periodically moving all allocated processes in memory to create one large contiguous free block. During compaction, all processes are temporarily suspended, their contents are copied to new locations, and the base registers are updated accordingly. While compaction eliminates external fragmentation, it imposes significant processing overhead and introduces pause times that make it unsuitable for real-time systems. The decision to perform compaction involves trade-offs between memory efficiency and system responsiveness.

## Examples

### Example 1: Fixed Partitioning Calculation

Consider a system with fixed partitioning using four partitions of sizes 100 KB, 200 KB, 150 KB, and 250 KB respectively. Three processes arrive with memory requirements of 80 KB, 180 KB, and 120 KB in that order.

The first process (80 KB) can be accommodated in any partition larger than 80 KB. The system typically assigns it to the smallest suitable partition, which is the 100 KB partition, leaving 20 KB of internal fragmentation.

The second process (180 KB) requires at least 180 KB. The smallest suitable partition is the 200 KB partition, which is allocated, leaving 20 KB of internal fragmentation.

The third process (120 KB) requires at least 120 KB. The remaining partitions are 150 KB and 250 KB. The 150 KB partition is allocated, leaving 30 KB of internal fragmentation.

Total internal fragmentation = 20 + 20 + 30 = 70 KB. Total memory allocated to processes = 80 + 180 + 120 = 380 KB. Total partition size = 100 + 200 + 150 + 250 = 700 KB. Memory utilization efficiency = 380/700 = 54.3%.

### Example 2: Variable Partitioning with First Fit

Assume memory starts with a single free block of 600 KB. Three processes arrive with requirements of 100 KB, 250 KB, and 150 KB respectively.

Process 1 (100 KB): The free block of 600 KB is sufficient. Allocating 100 KB creates a new free block of 500 KB. Allocated: 0-100 KB, Free: 100-600 KB.

Process 2 (250 KB): Scanning from beginning, the first free block of 500 KB can accommodate 250 KB. Allocating creates a new free block of 250 KB. Allocated: 0-100 KB and 100-350 KB, Free: 350-600 KB.

Process 3 (150 KB): The free block of 250 KB accommodates 150 KB, leaving a free block of 100 KB. Final state: Process 1 at 0-100 KB, Process 2 at 100-350 KB, Process 3 at 350-500 KB, Free blocks at 500-600 KB (100 KB) and 100-200 KB was already used.

External fragmentation total: Two free blocks totaling 200 KB. No single block exceeds 200 KB, so if a process requiring 200 KB arrives, it cannot be accommodated despite 200 KB total free memory.

### Example 3: Comparing Allocation Algorithms

Consider a scenario with initial free memory of 1000 KB and the following sequence of events: allocate 200 KB, allocate 300 KB, free the first allocation, allocate 150 KB, allocate 400 KB.

Using First Fit: Start with 1000 KB free. After allocating 200 KB: Used 0-200, Free 200-1000 (800 KB). After allocating 300 KB: Used 0-200, 200-500, Free 500-1000 (500 KB). After freeing first allocation: Free 0-200, Used 200-500, Free 500-1000. Allocating 150 KB finds first fit at 0-150: Used 0-150, 200-500, Free 150-200 (50 KB), 500-1000. Allocating 400 KB finds first fit at 500-900: Final Used 0-150, 200-500, 500-900, Free 150-200 (50 KB), 900-1000 (100 KB).

Using Best Fit: Same initial allocations produce similar results, but the 50 KB fragment from first fit would remain as a small unusable block. Best fit would have attempted to place the 150 KB allocation to minimize the resulting fragment, potentially producing different fragmentation patterns.

## Exam Tips

1. UNDERSTAND THE FUNDAMENTAL DIFFERENCE between fixed and variable partitioning—fixed partitioning creates internal fragmentation while variable partitioning creates external fragmentation.

2. MEMORIZE THE DEFINITIONS of internal and external fragmentation precisely, as these are frequently tested in examinations with specific examples requiring identification of the fragmentation type.

3. KNOW THE MEMORY ALLOCATION ALGORITHMS (First Fit, Best Fit, Worst Fit, Next Fit) including their time complexities and typical use cases.

4. REMEMBER THAT FIRST FIT IS GENERALLY THE FASTEST algorithm, while best fit typically provides the best memory utilization in theory but may produce more small fragments.

5. UNDERSTAND THE 50-PERCENT RULE for external fragmentation in first fit allocation, as this provides practical insight into the severity of the problem.

6. KNOW THE ROLE OF BASE AND LIMIT REGISTERS in address translation and memory protection for contiguous allocation systems.

7. BE PREPARED TO CALCULATE MEMORY UTILIZATION EFFICIENCY when given partition sizes and process sizes—practice numerical problems involving internal fragmentation sums.

8. UNDERSTAND COALESCING (also called coalescence) of free blocks and its role in managing external fragmentation, including when it can and cannot occur.

9. KNOW THE ADVANTAGES AND DISADVANTAGES of memory compaction, including why it may be unsuitable for real-time systems.

10. RECOGNIZE THAT CONTIGUOUS ALLOCATION IS SIMPLE but can become inefficient due to fragmentation, leading to the development of paging and segmentation techniques.