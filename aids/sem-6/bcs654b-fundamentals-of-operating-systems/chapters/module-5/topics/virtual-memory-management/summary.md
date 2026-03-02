# Virtual Memory Management - Summary

## Key Definitions and Concepts

- VIRTUAL MEMORY: A memory management technique that allows execution of processes that may not be completely in physical memory, creating an illusion of larger address space
- VIRTUAL ADDRESS SPACE: The range of memory addresses that a process can use, typically much larger than physical memory
- PHYSICAL ADDRESS SPACE: The actual RAM installed in the system, where data is stored
- MMU (Memory Management Unit): Hardware component that translates virtual addresses to physical addresses
- PAGE TABLE: Data structure maintained by OS that maps virtual pages to physical frames
- TLB (Translation Lookaside Buffer): Hardware cache storing recent address translations for fast lookup
- PAGE FAULT: Exception raised when a process accesses a page not currently in physical memory

## Important Formulas and Theorems

- Effective Access Time (EAT) = Hit Rate × (TLB Time + Memory Time) + Miss Rate × (TLB Time + 2 × Memory Time)
- Number of offset bits = log₂(Page Size)
- Number of VPN bits = log₂(Virtual Address Space / Page Size)
- Physical Address = Frame Number × Page Size + Offset

## Key Points

- Virtual memory enables programs larger than physical RAM to execute by swapping pages between RAM and disk
- Each process has its own isolated virtual address space, preventing unauthorized access to other processes' memory
- Address translation performed by MMU uses page tables to map virtual pages to physical frames
- Page tables use hierarchical structure (multi-level) to efficiently handle large virtual address spaces
- TLB provides fast translation caching, achieving hit rates above 99% due to locality of reference
- Demand paging loads pages only when referenced, reducing startup time and memory usage
- Page fault handling involves OS selecting victim page, possibly writing to disk, loading new page, and updating page tables

## Common Mistakes to Avoid

- Confusing virtual memory with physical memory; remember virtual addresses require translation
- Forgetting that page fault handling includes disk I/O, which causes significant delay (milliseconds vs nanoseconds for memory)
- In page replacement questions, always check the dirty bit before evicting a page; modified pages must be written back
- When calculating physical addresses, ensure you correctly separate the page number from the offset bits

## Revision Tips

- Practice at least 5 numerical problems on address translation to become comfortable with binary and hexadecimal conversions
- Create a comparison table of all page replacement algorithms with their advantages and disadvantages
- Memorize the sequence of events during page fault handling as this is frequently asked in exams
- Understand the concept of locality (spatial and temporal) as it explains why virtual memory works efficiently in practice