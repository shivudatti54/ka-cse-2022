# Memory Management Strategies - Summary

## Key Definitions and Concepts

- **Contiguous Memory Allocation**: A strategy where each process is allocated a single continuous block of memory; can be fixed or variable partitioning.
- **Paging**: Memory management technique dividing both physical and logical memory into fixed-size blocks (frames and pages) to eliminate external fragmentation.
- **Segmentation**: Memory management strategy dividing memory into variable-sized segments based on logical program divisions (code, data, stack).
- **Virtual Memory**: Technique providing the illusion of more memory than physically available by using disk storage for pages not currently in memory.
- **Page Fault**: Occurs when a process accesses a page not currently in physical memory, triggering its transfer from disk.
- **Thrashing**: Excessive paging activity that degrades system performance when processes lack sufficient frames.

## Important Formulas and Theorems

- **Logical Address Translation (Paging)**: Physical address = (frame number × page size) + offset
- **Number of Pages**: Pages = ceiling(logical address space / page size)
- **Effective Access Time**: EAT = (1 - p) × ma + p × ft, where p = page fault rate, ma = memory access time, ft = fault time
- **Belady's Anomaly**: Page faults may increase when adding more frames using FIFO replacement
- **Working Set**: W(t, w) = set of pages referenced in the time interval [t - w, t]

## Key Points

- Contiguous allocation suffers from fragmentation: internal in fixed partitions, external in variable partitions
- Paging eliminates external fragmentation but introduces internal fragmentation
- Segmentation reflects programmer's view of memory but suffers from external fragmentation
- Page size trade-off: larger pages reduce page table size but increase internal fragmentation
- LRU approximates Optimal page replacement but requires specialized hardware support
- Demand paging loads pages only when referenced, reducing I/O and memory requirements
- Frame allocation algorithms include equal allocation, proportional allocation, and priority-based allocation
- Thrashing occurs when page fault frequency is too high; solved by reducing degree of multiprogramming

## Common Mistakes to Avoid

1. Confusing internal and external fragmentation—internal occurs within allocated units; external is scattered free memory
2. Forgetting that segmentation requires both base and limit (length) in the segment table
3. Assuming larger page size always improves performance—trade-offs exist with internal fragmentation
4. Confusing page replacement algorithms—FIFO evicts oldest, LRU evicts least recently used
5. Ignoring the role of the Memory Management Unit (MMU) in address translation

## Revision Tips

1. Practice address translation problems for both paging and segmentation—these are frequently asked in DU exams
2. Memorize the key differences between strategies: paging (fixed-size, hardware-supported), segmentation (variable-size, logical), contiguous (simplest, fragmentation issues)
3. Understand when each algorithm (First Fit, Best Fit, LRU, FIFO) is appropriate and their relative efficiencies
4. Review the relationship between virtual memory, demand paging, and page fault handling
5. Solve numerical problems on page fault counts, effective access time, and memory utilization