# Paging - Summary

## Key Definitions and Concepts

- PAGING: A memory management technique that divides both logical and physical memory into fixed-size blocks called pages and frames respectively

- PAGE: A fixed-size block of logical memory belonging to a process's address space

- FRAME: A fixed-size block of physical memory where pages are stored

- PAGE TABLE: A data structure maintaining the mapping between virtual pages and physical frames

- TRANSLATION LOOKASIDE BUFFER (TLB): A hardware cache storing recent page table entries for fast address translation

- PAGE FAULT: An exception raised when a process accesses a page not currently in physical memory

## Important Formulas and Theorems

- Number of bits for offset = log2(page size)
- Number of pages = 2^(logical address bits - offset bits)
- Physical address = (frame number × page size) + offset
- Effective Access Time = (hit rate × hit time) + (miss rate × miss time)
- Belady's Anomaly: In FIFO, increasing frames can increase page faults

## Key Points

- Paging eliminates external fragmentation by allowing non-contiguous physical memory allocation

- Page size trade-off: larger pages reduce page table overhead but increase internal fragmentation

- TLB provides fast address translation through associative lookup, typically achieving 95%+ hit rates

- Multi-level page tables reduce memory overhead for sparse address spaces

- Demand paging loads pages only when referenced, enabling over-commitment of memory

- Page replacement algorithms include FIFO, LRU, Optimal, and Clock (Second Chance)

- Each PTE contains frame number, valid bit, protection bits, and dirty bit

## Common Mistakes to Avoid

- Confusing page number with frame number in address calculations

- Forgetting that page offset remains unchanged during address translation

- Overlooking the cost of TLB misses in performance calculations

- Applying FIFO replacement to non-existent pages (checking valid bits)

- Confusing internal fragmentation (unused space within allocated units) with external fragmentation (unavailable contiguous space)

## Revision Tips

- Practice address translation problems until the process becomes automatic

- Memorize the steps for tracing each page replacement algorithm with example reference strings

- Remember that offset bits are always the lower-order bits in logical addressing

- Review TLB calculations as they frequently appear in numerical problems

- Understand the relationship between page size, address bits, and number of entries in page tables