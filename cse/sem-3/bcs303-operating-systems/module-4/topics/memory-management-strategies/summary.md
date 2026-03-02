# Memory Management Strategies - Summary

## Key Definitions

- **Memory Management**: The OS subsystem that controls and coordinates computer memory, allocating portions to processes and ensuring isolation between them.

- **Physical Memory**: The actual RAM in the system with fixed size and specific addresses.

- **Virtual Memory**: The logical view of memory presented to processes, which may be larger than physical memory.

- **Contiguous Allocation**: A memory management approach where each process occupies a single continuous block of physical memory.

- **Non-Contiguous Allocation**: A memory management approach where processes can be divided into blocks placed in scattered physical memory locations.

- **Internal Fragmentation**: Wasted memory within an allocated block due to rounding up of allocation requests.

- **External Fragmentation**: Wasted memory in small non-contiguous blocks between allocated segments, making it impossible to satisfy large requests.

- **Compaction**: The process of moving memory contents to consolidate free space and combat external fragmentation.

- **Swapping**: Moving entire processes between physical memory and secondary storage to free memory for other processes.

- **MMU (Memory Management Unit)**: Hardware component that translates virtual addresses to physical addresses.

## Important Formulas

- **Physical Address Calculation**: Physical Address = (Frame Number × Frame Size) + Offset

- **Page Number**: Virtual Address / Page Size

- **Offset**: Virtual Address % Page Size

## Key Points

1. Memory management must balance efficiency, protection, isolation, and transparency in allocating limited physical memory to multiple processes.

2. Contiguous allocation (fixed or variable partitioning) is simpler to implement but suffers from fragmentation problems.

3. Fixed partitioning creates internal fragmentation and limits concurrent process count; variable partitioning creates external fragmentation.

4. Non-contiguous allocation via paging and segmentation eliminates external fragmentation at the cost of address translation overhead.

5. The MMU hardware works with OS software to provide address translation, enabling virtual memory to exceed physical memory.

6. Swapping extends available memory by using disk storage but significantly impacts performance due to I/O operations.

7. The choice of memory management strategy depends on system type, hardware support, and performance requirements.

8. Demand loading and paging allow processes to start execution before all their memory is loaded, improving responsiveness.

## Common Mistakes

1. Confusing internal and external fragmentation—internal occurs within allocated blocks; external occurs in free space between blocks.

2. Believing that more physical memory eliminates the need for memory management—all systems require memory management for protection and isolation.

3. Underestimating the performance cost of swapping and compaction operations in contiguous allocation systems.

4. Ignoring the role of hardware (MMU) in memory management—software alone cannot achieve efficient address translation.

5. Failing to recognize that virtual memory and physical memory use different address schemes, requiring translation.