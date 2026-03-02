# Memory Management - Summary

## Key Definitions and Concepts

- MEMORY MANAGEMENT: The OS function of controlling and coordinating computer memory, allocating portions to various running programs.
- VIRTUAL MEMORY: An abstraction that gives each process the illusion of having exclusive access to a large address space, regardless of physical memory.
- PAGE: Fixed-size block in virtual memory; FRAME: Corresponding block in physical memory.
- PAGE FAULT: Exception occurs when a process accesses a page not currently in physical memory.
- THRASHING: Excessive paging activity where system spends more time swapping pages than executing processes.
- MMU (Memory Management Unit): Hardware component translating virtual addresses to physical addresses.

## Important Formulas and Theorems

- NUMBER OF VIRTUAL PAGES = Virtual Address Space / Page Size
- PAGE TABLE SIZE = Number of Virtual Pages × Page Table Entry Size
- FRAME NUMBER = Physical Address / Frame Size
- BELADY'S ANOMALY: In FIFO, increasing frames can increase page faults (counterintuitive)

## Key Points

- Memory management enables multiple processes to share limited RAM efficiently.
- Paging eliminates external fragmentation but introduces internal fragmentation.
- Segmentation provides logical division matching programmer's view but can fragment.
- Virtual memory combines demand loading with paging to run programs larger than RAM.
- LRU approximates optimal page replacement more closely than FIFO but is costlier to implement.
- Working set model helps prevent thrashing by maintaining adequate pages per process.
- Multi-level page tables reduce memory overhead for large address spaces.
- The TLB (Translation Lookaside Buffer) speeds up address translation through caching.

## Common Mistakes to Avoid

- Confusing internal fragmentation (paging) with external fragmentation (contiguous allocation).
- Believing that more physical memory always reduces page faults—algorithms matter.
- Forgetting that page tables themselves consume memory, which must be accounted for.
- Mixing up virtual addresses with physical addresses—they are different address spaces.

## Revision Tips

- Practice numerical problems on page fault calculation for all major algorithms.
- Draw diagrams showing address translation in paging systems.
- Create comparison tables for different memory management techniques.
- Memorize why certain algorithms perform better under specific memory access patterns.
- Review previous years' DU question papers on this topic for pattern understanding.