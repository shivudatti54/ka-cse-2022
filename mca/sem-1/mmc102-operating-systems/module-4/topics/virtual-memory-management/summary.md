# Virtual Memory Management - Summary

## Key Definitions and Concepts

- VIRTUAL MEMORY is an abstraction that provides processes with the illusion of having a large, contiguous address space larger than physical memory, managed through mapping between virtual and physical addresses.

- PAGING divides both virtual and physical memory into fixed-size blocks (pages and frames), with the page table storing translation information for each virtual page.

- A PAGE FAULT occurs when a process accesses a page not currently in physical memory, triggering the operating system to load the page from secondary storage.

- DEMAND PAGING loads pages only when they are accessed, deferring page loading until necessary and enabling execution of programs larger than physical memory.

- WORKING SET is the set of pages a process has accessed recently and must keep resident to avoid excessive page faults.

- THRASHING occurs when the system spends more time handling page faults than executing useful work due to insufficient physical memory for active processes.

## Important Formulas and Theorems

- EFFECTIVE MEMORY ACCESS TIME = (TLB Hit Rate × TLB Hit Time) + (TLB Miss Rate × TLB Miss Time)

- VIRTUAL ADDRESS = (Page Number × Page Size) + Offset

- NUMBER OF PAGES = Virtual Address Space / Page Size

- BELADY'S ANOMALY: FIFO can exhibit increased page faults with increased frames; LRU and OPTIMAL do not suffer from this anomaly.

## Key Points

- Virtual memory enables process isolation, allowing each process to believe it has exclusive access to the entire address space.

- The MMU performs hardware address translation on every memory access, using page tables and potentially TLB caches.

- Page replacement algorithms determine which page to evict when memory is full; OPTIMAL achieves minimum faults but is impractical, LRU approximates it, FIFO is simple but suffers Belady's anomaly, and CLOCK provides practical LRU approximation.

- TLB caching of page table entries is critical for performance—without it, every memory access would require additional memory accesses for translation.

- Thrashing occurs when total working set sizes exceed physical memory, causing constant page evictions and severe performance degradation.

- Modern systems combine segmentation (logical organization) with paging (physical management) to leverage benefits of both approaches.

## Common Mistakes to Confuse

- CONFUSING PAGE FAULTS WITH SEGMENTATION FAULTS: Page faults are recoverable (page needs loading), while segmentation faults indicate invalid memory access.

- IGNORING TLB OVERHEAD: When calculating effective access time, always include the TLB lookup time even on hits.

- FORGETTING THAT PAGE FAULT HANDLING INVOLVES DISK I/O: This makes page faults extremely expensive (milliseconds vs. nanoseconds for memory access).

- MISAPPLYING PAGE REPLACEMENT ALGORITHMS: The best algorithm depends on access pattern—FIFO can outperformRU for certain sequential L patterns.

## Revision Tips

- PRACTICE ADDRESS TRANSLATION: Work through multiple examples converting between virtual addresses, page numbers, and frame addresses.

- MEMORIZE ALGORITHM BEHAVIORS: Create a comparison table of FIFO, LRU, OPTIMAL, and CLOCK with their advantages, disadvantages, and best use cases.

- UNDERSTAND THE BIG PICTURE: Connect virtual memory to related concepts like process isolation, memory protection, and system performance.

- SOLVE PREVIOUS EXAM QUESTIONS: Page fault calculations and TLB effective access time problems appear frequently in DU examinations.