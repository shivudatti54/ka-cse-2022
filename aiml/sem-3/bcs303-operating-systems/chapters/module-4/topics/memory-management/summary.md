# Memory Management - Summary

## Key Definitions and Concepts

- **Memory Management**: The OS function controlling allocation and deallocation of physical memory to processes
- **Swapping**: Moving entire processes between main memory and secondary storage
- **Contiguous Allocation**: Assigning each process a single continuous block of physical memory
- **Paging**: Dividing physical and logical memory into fixed-size blocks (frames and pages) to eliminate external fragmentation
- **Segmentation**: Memory management scheme using variable-sized segments representing logical program units
- **Virtual Memory**: Abstraction providing processes with larger address space than physical memory
- **Page Fault**: Exception occurring when a referenced page is not in physical memory
- **Thrashing**: Excessive paging activity causing poor system performance when processes need more pages than available memory
- **Working Set**: Set of pages a process actively references over a specific time interval

## Important Formulas and Theorems

- **Logical Address**: (page number × page size) + offset
- **Physical Address**: (frame number × frame size) + offset
- **Effective Access Time**: (1 - p) × Ma + p × Pf, where p = page fault rate, Ma = memory access time, Pf = page fault service time
- **Belady's Anomaly**: Adding more frames can increase page faults with FIFO algorithm

## Key Points

- Memory management is essential for multiprogramming, process isolation, and efficient memory utilization
- Contiguous allocation suffers from external fragmentation; paging eliminates external fragmentation but introduces internal fragmentation
- Segmentation provides logical protection but combined with paging (segmented paging) for efficient physical memory use
- Virtual memory enables execution of programs larger than physical memory through demand paging
- Page replacement algorithms aim to minimize page faults; LRU approximates Optimal better than FIFO
- Thrashing occurs when page fault rate becomes extremely high; controlled by adjusting degree of multiprogramming
- Modern systems use multi-level page tables to handle large address spaces efficiently

## Common Mistakes to Avoid

- Confusing internal and external fragmentation—internal is unused space within allocated block, external is scattered free blocks
- Forgetting that offset remains unchanged during address translation in paging
- Assuming more frames always reduces page faults—Belady's anomaly disproves this for FIFO
- Confusing page and segment—the former is fixed-size, the latter is variable-sized logical unit

## Revision Tips

1. Practice numerical problems on address translation until comfortable with binary and hexadecimal calculations
2. Trace through page replacement algorithms multiple times with different reference strings
3. Create comparison tables for all memory management schemes covering fragmentation, complexity, and use cases
4. Memorize the steps in page fault handling as this is a frequently asked examination topic
5. Understand the tradeoff between hit ratio and effective access time through example calculations