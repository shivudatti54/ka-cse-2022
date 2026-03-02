# Virtual Memory Management - Summary

## Key Definitions and Concepts

- **Virtual Memory**: Abstraction giving illusion of large contiguous memory space
- **Demand Paging**: Load pages into memory only when needed (non-preemptive)
- **Page Fault**: Occurs when accessing page not in physical memory
- **Copy-on-Write**: Share pages until modification occurs (used in fork())
- **Thrashing**: Excessive page faults due to insufficient physical frames
- **Working Set**: Set of pages actively used by process in time window
- **TLB (Translation Lookaside Buffer)**: Cache for frequent page table entries

## Important Formulas and Theorems

```
1. Effective Access Time (EAT):
EAT = (1 - p) × memory_access + p × page_fault_overhead
Where p = page fault rate

2. Page Fault Rate Calculation:
Page Faults / Total Memory Accesses

3. Belady's Anomaly (FIFO):
Increasing frames can increase page faults (observed in FIFO only)
```

## Key Points

- Virtual memory enables running larger processes than physical memory through paging
- Demand paging reduces I/O and memory usage by loading pages on-demand
- Page replacement algorithms prevent over-allocation:
  - **OPT**: Replace page not used longest (optimal but unrealizable)
  - **FIFO**: Replace first-in page (suffers Belady's anomaly)
  - **LRU**: Replace least-recently used (good approximation)
- Copy-on-write optimizes process creation (used in fork())
- TLB reduces address translation overhead (hit ratio critical)
- Thrashing prevention methods:
  - Working set model
  - Page fault frequency threshold
  - Load control through process suspension

## Common Mistakes to Avoid

1. Confusing page replacement algorithms (e.g., using FIFO when question specifies LRU)
2. Forgetting to multiply page fault service time by p in EAT calculations
3. Assuming all page faults are equally expensive (disk vs. swap file access differs)
4. Mixing virtual memory fragmentation with contiguous allocation fragmentation types

## Revision Tips

1. Practice numericals on:
   - Page replacement sequence analysis (draw tables)
   - EAT calculations with given hit ratios
   - Working set determination
2. Use mnemonic "FOLK" for algorithms: FIFO, OPTIMAL, LRU, CLOCK (K=Clock)
3. Compare algorithms using:
   - Implementation complexity
   - Hardware requirements
   - Performance characteristics
4. Remember real-world applications:
   - Copy-on-write in fork()
   - LRU approximations in web caching
   - Working set model for memory allocation
