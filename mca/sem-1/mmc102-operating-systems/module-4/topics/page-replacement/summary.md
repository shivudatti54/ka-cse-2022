# Page Replacement - Summary

## Key Definitions and Concepts

- PAGE REPLACEMENT: The process of selecting a victim page to evict from physical memory when a new page must be loaded and no free frames are available

- PAGE FAULT: An exception raised when a process accesses a page not currently in physical memory, triggering the page replacement mechanism

- VICTIM PAGE: The page selected for eviction from physical memory to make room for a newly needed page

- THRASHING: Excessive page fault activity causing the system to spend more time on page I/O than productive work

- TEMPORAL LOCALITY: The principle that recently accessed memory locations are likely to be accessed again soon

## Important Formulas and Theorems

- BELADY'S ALGORITHM (OPT): Replace the page that will not be used for the longest time in the future. This produces minimum page faults but requires future knowledge.

- WORKING SET: W(t, w) = {pages referenced in time interval [t-w, t]}. The system should maintain these pages in memory.

- PAGE FAULT RATE: Number of page faults divided by total memory references. The primary metric for evaluating replacement algorithms.

## Key Points

- PAGE REPLACEMENT ENABLES VIRTUAL MEMORY by allowing pages to be swapped between disk and physical memory, creating the illusion of larger memory

- FIFO IS SIMPLE BUT FLAWED: It only considers residence time, not usage patterns, and suffers from Belady's anomaly where more frames can cause more faults

- LRU APPROXIMATES OPT: By replacing least recently used pages, LRU captures temporal locality but requires significant hardware support for exact implementation

- CLOCK ALGORITHM IS PRACTICAL: Uses a reference bit to approximate LRU with minimal overhead, making it the choice for most real operating systems

- CLEAN VS DIRTY PAGES: Clean pages can be replaced immediately; dirty pages must be written to disk first, adding significant I/O overhead

- ALGORITHM SELECTION DEPENDS ON WORKLOAD: No single algorithm performs best for all access patterns

## Common Mistakes to Avoid

- CONFUSING FIFO WITH LRU: FIFO evicts the oldest page regardless of usage; LRU evicts the least recently used page

- IGNORING THE REFERENCE BIT IN CLOCK: The reference bit is crucial for second chance functionality; forgetting to update it invalidates the algorithm

- NOT ACCOUNTING FOR DIRTY PAGES: When counting page faults, remember that dirty pages require additional disk writes

- FORGETTING INITIAL FAULTS: Loading the first few pages into empty frames also counts as page faults

## Revision Tips

- PRACTICE TRACE EXERCISES: Work through multiple page reference strings with each algorithm until you can solve them quickly

- REMEMBER THE ANOMALY: Only non-stack algorithms like FIFO exhibit Belady's anomaly; stack algorithms maintain inclusion properties

- KNOW REAL-WORLD USAGE: Linux uses a variant of the clock algorithm (accessed bit), Windows uses a working set model combined with priority-based replacement

- UNDERSTAND THE BIG PICTURE: Page replacement is part of virtual memory management, working with paging, segmentation, and TLB to provide efficient memory abstraction