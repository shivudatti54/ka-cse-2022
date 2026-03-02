# Demand Paging - Summary

## Key Definitions

- **Demand Paging**: A virtual memory management technique that loads pages into physical memory only when they are explicitly referenced by a running process
- **Page Fault**: A trap raised by the hardware when a process accesses a page marked as invalid in the page table
- **Valid-Invalid Bit**: A status bit in each page table entry indicating whether the corresponding page is currently resident in memory
- **Swap Device**: Secondary storage space used to hold pages that are not currently resident in physical memory
- **Effective Access Time (EAT)**: The average time to access memory in a paged system, accounting for page fault probability

## Important Formulas

- **Effective Access Time**: EAT = (1 - p) × Ma + p × Ft
- Where p = page fault rate (0 ≤ p ≤ 1)
- Ma = memory access time
- Ft = time to service a page fault

## Key Points

1. Demand paging follows a "lazy loading" approach - pages are loaded only when referenced, not all at program start
2. The valid-invalid bit in the page table determines whether a page is in memory (valid) or on disk (invalid)
3. Page fault service involves: trap handling, locating free frame, reading page from disk, updating page table, restarting instruction
4. Disk access time for page faults (milliseconds) dominates over memory access time (nanoseconds), causing significant performance overhead
5. Even a small page fault rate (e.g., 0.1%) can degrade performance by orders of magnitude
6. Copy-on-write (COW) is an extension where pages are shared until modification is attempted, leveraging demand paging principles
7. Demand paging enables execution of programs larger than physical memory through virtual memory
8. The working set concept - pages actively used by a process - determines actual memory requirements

## Common Mistakes

1. Confusing valid and invalid bits: Remember "valid" means in memory, "invalid" means not in memory or not allocated
2. Unit mismatch in EAT calculations: Always convert all times to the same unit (nanoseconds or milliseconds) before calculation
3. Forgetting that page fault service includes both disk I/O time and overhead for trap handling and instruction restart
4. Assuming page fault rate is zero: In practice, some page faults are inevitable during process initialization
5. Not considering that every instruction that spans page boundaries can potentially cause multiple page faults
