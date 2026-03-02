# Virtual Memory Management - Summary

## Key Definitions

- **Virtual Memory**: A memory management technique that provides processes with the illusion of having a large, contiguous address space larger than physical memory.
- **Page Fault**: An interrupt that occurs when a process accesses a page not currently in physical memory, requiring the OS to load it from secondary storage.
- **Page Table**: A data structure maintained by the OS that maps virtual page numbers to physical frame numbers, stored in main memory.
- **Translation Lookaside Buffer (TLB)**: A hardware cache that stores recent virtual-to-physical address translations for fast lookup.
- **Working Set**: The set of pages that a process has referenced within a recent time window (τ).
- **Thrashing**: Excessive paging activity where the system spends more time swapping pages than executing processes.
- **Copy-on-Write**: An optimization where pages are shared between processes until modification occurs.

## Important Formulas

- **Physical Address Calculation**: Physical Address = (Frame Number × Page Size) + Offset
- **Effective Access Time**: EAT = (1 - p) × Memory Access Time + p × Page Fault Service Time
- **Number of Virtual Pages**: 2^(virtual address bits - offset bits)
- **Page Fault Rate**: Number of page faults / Total memory accesses

## Key Points

1. Virtual memory enables execution of programs larger than physical memory through paging and demand loading.

2. The MMU hardware performs address translation on every memory access, using page tables maintained by the OS.

3. Multi-level page tables reduce memory overhead for large virtual address spaces but increase translation latency.

4. TLB improves performance by caching translations; TLB miss penalty significantly impacts overall memory access time.

5. Demand paging loads pages only when referenced, reducing startup time and allowing more processes in memory.

6. Optimal page replacement is theoretical; LRU is the best practical algorithm but Clock provides efficient approximation.

7. Thrashing occurs when processes' combined working sets exceed available physical memory.

8. The OS uses reference and dirty bits to make intelligent page replacement decisions and minimize I/O.

9. Copy-on-write optimizes fork() by deferring page duplication until actual modification.

10. Page size involves trade-offs: larger pages mean smaller page tables but more internal fragmentation.

## Common Mistakes

1. Confusing virtual memory with swap space - virtual memory is the abstraction; swap is the backing store on disk.

2. Assuming that valid bit = page in memory; forgetting that valid=0 indicates a page fault is needed.

3. Forgetting that page fault handling requires disk I/O, making the cost orders of magnitude higher than memory access.

4. Misunderstanding that LRU requires future knowledge - it is optimal only with complete reference string knowledge.

5. Believing that adding more memory always prevents thrashing; the solution is proper working set management.