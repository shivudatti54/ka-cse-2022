# Virtual Memory Management - Summary

## Key Definitions and Concepts

- VIRTUAL MEMORY: A memory management technique that provides the illusion of a larger memory space by using disk storage to supplement RAM
- DEMAND PAGING: A paging scheme where pages are loaded into memory only when explicitly referenced by a running process
- PAGE FAULT: An interrupt that occurs when a process accesses a page that is not currently in physical memory
- PAGE REPLACEMENT ALGORITHM: A strategy used to select which page to evict when memory is full and a new page must be loaded
- WORKING SET: The set of pages that a process has referenced within a specific time window
- THRASHING: Excessive paging activity that degrades system performance when the system spends more time swapping pages than executing processes
- COPY-ON-WRITE: An optimization technique that delays page copying until a process attempts to modify a shared page

## Important Formulas and Theorems

- EFFECTIVE ACCESS TIME = (1 - p) × memory_access_time + p × page_fault_time
- WHERE p is the page fault rate, typically very small (< 0.001)
- Page fault time includes: service page fault interrupt, read page from disk, restart instruction
- Working Set Size (WSS) = number of distinct pages referenced in time interval T

## Key Points

- Virtual memory enables execution of programs larger than physical memory through demand paging and swapping
- The Memory Management Unit (MMU) translates virtual addresses to physical addresses using page tables
- Page faults are expensive; reducing them improves system performance significantly
- FIFO is simple but performs poorly; LRU approximates optimal but requires complex implementation
- The optimal algorithm produces minimum page faults but cannot be practically implemented
- Thrashing occurs when processes lack sufficient frames to maintain their working sets
- Copy-on-write dramatically reduces fork overhead by deferring page copying
- Frame allocation policies include equal allocation, proportional allocation, and priority-based allocation

## Common Mistakes to Avoid

- Confusing virtual addresses with physical addresses; they are different address spaces
- Forgetting that page fault handling requires the interrupted instruction to be restarted after the page is loaded
- Believing that increasing physical memory always improves performance; improper usage can lead to thrashing
- Mixing up the reference bit and dirty bit; reference bit tracks usage, dirty bit tracks modification

## Revision Tips

- Practice tracing page replacement algorithms with multiple reference strings to build speed and accuracy
- Memorize the page fault handling sequence: validate reference, locate page on disk, find free frame, read page, update table, restart instruction
- Create comparison tables for all page replacement algorithms highlighting advantages, disadvantages, and use cases
- Understand the relationship between page size, page table size, and internal fragmentation through worked examples