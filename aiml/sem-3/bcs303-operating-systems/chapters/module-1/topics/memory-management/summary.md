# Memory Management - Summary

## Key Definitions and Concepts

- **Memory Management**: OS function that controls how primary memory is allocated to processes and tracks its usage.
- **Contiguous Allocation**: Each process gets a single continuous block of memory; suffers from external fragmentation.
- **Paging**: Divides memory into fixed-size frames and processes into pages; eliminates external fragmentation but has internal fragmentation.
- **Segmentation**: Divides process into logical segments (code, data, stack); provides logical organization.
- **Virtual Memory**: Technique that allows execution of processes larger than physical memory by using disk space.
- **Page Fault**: Occurs when a requested page is not in physical memory; triggers page loading from secondary storage.
- **Thrashing**: Excessive paging activity that degrades system performance when CPU is busy swapping pages rather than executing processes.

## Important Formulas and Theorems

- Number of pages = ceil(Process size / Page size)
- Physical address = (Frame number × Page size) + Offset
- Virtual address = (Page number × Page size) + Offset
- Internal fragmentation = Allocated memory - Actual process size
- Effective Access Time = (1 - p) × ma + p × page fault time (where p = page fault probability, ma = memory access time)

## Key Points

- MEMORY HIERARCHY organizes storage by speed: registers → cache → main memory → secondary storage.
- FIXED PARTITIONING creates internal fragmentation; VARIABLE PARTITIONING creates external fragmentation.
- PAGING ELIMINATES external fragmentation but introduces internal fragmentation.
- PAGE REPLACEMENT algorithms include FIFO, LRU, Optimal, and Second Chance.
- LRU IS PRACTICAL AND EFFECTIVE but requires hardware support for tracking.
- VIRTUAL MEMORY provides process isolation and enables larger programs to run.
- MEMORY PROTECTION prevents processes from accessing each other's memory space.
- MMU TRANSLATES virtual addresses to physical addresses on every memory access.

## Common Mistakes to Avoid

- Confusing internal and external fragmentation—they have opposite causes and solutions.
- Forgetting that page size affects both internal fragmentation and page table size.
- Assuming optimal page replacement can be implemented—it serves only as a theoretical benchmark.
- Confusing page replacement with process swapping—they operate at different granularities.

## Revision Tips

- Practice numerical problems on page replacement with different reference strings.
- Memorize the steps that occur during a page fault handling sequence.
- Create comparison tables for different memory management techniques.
- Solve previous year DU question papers to understand the exam pattern and important topics.
- Focus on advantages-disadvantages format for exam preparation.