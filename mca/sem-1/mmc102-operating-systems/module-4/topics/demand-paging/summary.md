# Demand Paging - Summary

## Key Definitions and Concepts

- **Demand Paging**: A virtual memory management technique where pages are loaded into memory only when a process references them, rather than loading the entire program at startup.

- **Page Fault**: A trap raised by the hardware when a process attempts to access a page that is marked invalid (not currently in memory), requiring the operating system to load the page from secondary storage.

- **Valid-Invalid Bit**: A status flag in each page table entry indicating whether the corresponding page is currently resident in memory (valid) or not (invalid).

- **Thrashing**: Excessive paging activity where the system spends more time servicing page faults than executing processes, severely degrading performance.

- **Working Set**: The set of pages that a process is actively using during its current execution phase.

- **Belady's Anomaly**: The counter-intuitive phenomenon where increasing the number of frames can increase the number of page faults, specifically occurring in FIFO algorithm.

## Important Formulas and Theorems

- **Effective Access Time (EAT)** = (1 - p) × ma + p × pf
  - Where p = page fault rate, ma = memory access time, pf = page fault service time

- **Page Fault Service Time** ≈ Disk I/O read time + OS overhead + Restart overhead
  - Typical disk I/O time: 8-12 milliseconds
  - Memory access time: 50-200 nanoseconds

## Key Points

1. Demand paging allows programs larger than physical memory to execute by keeping only active pages in memory.

2. A page fault requires the OS to locate the page on disk, allocate a frame, read the page, update tables, and restart the interrupted instruction.

3. FIFO evicts the oldest page but suffers from Belady's anomaly; LRU approximates optimal behavior without this anomaly.

4. Optimal page replacement produces minimum page faults but requires future knowledge, making it unimplementable in practice.

5. Thrashing occurs when processes lack sufficient frames for their working set, causing excessive page I/O.

6. The valid-invalid bit enables the MMU to quickly determine whether a memory reference requires OS intervention.

7. Even page tables can be paged out, requiring multi-level page tables in large address spaces.

## Common Mistakes to Avoid

1. Confusing memory access time with page fault service time—they differ by approximately five orders of magnitude.

2. Assuming LRU always performs better than FIFO—performance depends on the specific reference pattern.

3. Forgetting that page fault handling includes both loading the page AND restarting the instruction that caused the fault.

4. Ignoring the fact that the first reference to any page will always cause a page fault in a demand paging system.

## Revision Tips

1. Practice numerical problems by drawing frame allocation tables for different reference strings and algorithms.

2. Memorize the EAT formula and practice substituting different values to understand how page fault rate affects performance.

3. Create a comparison table of FIFO, Optimal, and LRU algorithms covering advantages, disadvantages, and implementation complexity.

4. Remember that demand paging optimizes memory usage at the cost of increased initial page fault overhead during process startup.