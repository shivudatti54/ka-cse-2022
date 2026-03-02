# Virtual Memory Management - Summary

## Key Definitions and Concepts

- **Virtual Memory**: A technique that provides the illusion of a larger, contiguous address space than physically available by using secondary storage to hold inactive pages.
- **Page Table**: A data structure maintained by the OS that maps virtual page numbers to physical frame numbers, storing additional status bits (valid, dirty, referenced, protection).
- **Translation Lookaside Buffer (TLB)**: A hardware cache that stores recent virtual-to-physical address translations for faster access.
- **Page Fault**: An exception raised when a program accesses a virtual page not currently in physical memory, triggering the page fault handler.
- **Working Set**: The set of pages actively used by a process; the OS attempts to keep this in physical memory to minimize page faults.
- **Thrashing**: Excessive paging activity where the system spends more time swapping pages than executing processes, resulting in severe performance degradation.

## Important Formulas and Theorems

- **Effective Access Time (EAT)** = p × (TLB + Disk Access) + (1-p) × (TLB + Memory Access), where p = page fault rate
- **Belady's Anomaly**: In some page replacement algorithms (like FIFO), increasing the number of frames can increase page faults
- **Address Structure**: Virtual Address = (Page Number × Page Size) + Offset
- **Multi-level Page Table**: Total entries = 2^(bits per level), with each level reducing memory overhead for sparse address spaces

## Key Points

- Virtual memory enables execution of programs larger than physical RAM and provides process isolation through separate address spaces
- Demand paging loads pages only when referenced, improving startup time and allowing overcommitment of memory
- Page replacement algorithms aim to minimize future page faults; Optimal is theoretical, LRU is ideal but expensive, Clock is practical approximation
- TLB dramatically reduces address translation overhead, achieving 95-99% hit rates in typical workloads
- Copy-on-Write optimizes fork() by deferring page copying until modification, saving memory and CPU time
- Thrashing occurs when memory demand exceeds supply, causing a vicious cycle of page evictions and faults
- Multi-level page tables reduce memory overhead for large address spaces but increase translation complexity

## Common Mistakes to Avoid

1. Confusing pages with frames—pages are virtual divisions, frames are physical divisions
2. Forgetting that page fault service includes disk I/O time, making it thousands of times slower than memory access
3. Assuming more frames always reduces page faults—Belady's anomaly proves this false for FIFO
4. Overlooking the dirty bit—modified pages must be written back to disk before eviction
5. Misunderstanding that TLB misses require page table walks, adding extra memory accesses

## Revision Tips

1. Practice trace examples for all page replacement algorithms with various reference strings until the process becomes automatic
2. Draw memory access diagrams showing page table lookups, TLB hits/misses, and the complete page fault handling flow
3. Memorize the typical page fault service time breakdown: 10-20ms for disk I/O vs. 100ns for memory access
4. Review previous year question papers to understand the pattern and weightage of this topic in DU examinations
5. Implement a simple page replacement simulator to gain hands-on experience with LRU and FIFO algorithms