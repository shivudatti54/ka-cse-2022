# Paging, Segmentation, and Virtual Memory - Summary

## Key Definitions and Concepts

- **Paging**: Memory management scheme that divides virtual and physical memory into fixed-size blocks called pages and frames, eliminating external fragmentation.
- **Page Table**: Data structure mapping virtual page numbers to physical frame numbers, stored in memory and accessed by the Memory Management Unit (MMU).
- **Translation Lookaside Buffer (TLB)**: Hardware cache storing recent page table entries for faster address translation.
- **Segmentation**: Memory management technique dividing memory into variable-sized logical units (segments) based on program structure (code, data, stack).
- **Virtual Memory**: Technique allowing execution of processes that may not be completely in memory, using demand paging to swap pages between disk and RAM.
- **Page Fault**: Exception raised when a process accesses a page not currently in physical memory.
- **Thrashing**: Performance degradation when system spends excessive time in page swapping, typically due to insufficient memory allocation.
- **Working Set**: Set of pages a process has referenced in the recent past, representing its current memory needs.

## Important Formulas and Theorems

- **Virtual Address Breakdown**: For page size 2^n, the offset requires n bits, and remaining bits represent page number.
- **Effective Access Time (EAT)** = Hit Ratio × (TLB + Memory) + (1 - Hit Ratio) × (TLB + 2 × Memory)
- **Page Fault Rate**: Number of page faults divided by total memory references.
- **Belady's Anomaly**: Phenomenon where increasing the number of frames can increase page faults in FIFO algorithm.

## Key Points

- Paging eliminates external fragmentation but may cause internal fragmentation due to fixed page sizes.
- TLB provides significant speedup in address translation; typical hit ratios exceed 90%.
- Multi-level page tables reduce memory overhead for sparse address spaces.
- Segmentation provides logical protection boundaries but suffers from external fragmentation.
- Combined segmentation and paging offers both logical organization and efficient memory utilization.
- FIFO is simple but suboptimal; LRU approximates optimal but is expensive; Second Chance provides good practical performance.
- Demand paging uses lazy loading—pages are loaded only when referenced.
- The optimal page replacement algorithm produces minimum page faults but cannot be implemented.
- Thrashing occurs when processes lack sufficient frames for their working sets.

## Common Mistakes to Avoid

- Confusing pages with frames: pages are in virtual memory, frames are in physical memory.
- Forgetting that page table entries themselves require memory and contribute to overhead.
- Assuming that increasing memory always improves performance—considering thrashing threshold.
- Overlooking the fact that context switches invalidate TLB entries, affecting subsequent performance.
- Mishandling the offset during address translation—offset bits remain unchanged.

## Revision Tips

1. Practice drawing address translation diagrams for both paging and segmentation repeatedly.
2. Work through at least 3-4 different reference strings with each page replacement algorithm.
3. Memorize the sequence of operations during a page fault—know the exact OS steps.
4. Review numerical problems involving address calculations and effective access time computations.
5. Understand the trade-offs between the three main approaches: pure paging, pure segmentation, and combined systems.