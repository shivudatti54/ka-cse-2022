# Background of Memory Management - Summary

## Key Definitions and Concepts

- Memory Management: The operating system function that controls and coordinates computer memory, allocating portions to processes and maintaining allocation state
- Virtual Memory: A technique that creates the illusion of a larger memory space than physically available by using secondary storage
- MMU (Memory Management Unit): Hardware component that translates virtual addresses to physical addresses and provides memory protection
- Internal Fragmentation: Wasted memory within an allocated partition due to fixed sizes or rounding
- External Fragmentation: Scattered free memory blocks that cannot accommodate larger processes despite sufficient total free space
- Logical Address: Memory address used by a program, which must be translated to physical address
- Physical Address: Actual address in RAM where data is stored

## Important Formulas and Theorems

- Physical Address = Base Register + Logical Address (in simple partitioning)
- Internal Fragmentation = Allocated Partition Size - Actual Process Size
- Memory Access Time = Hit Ratio × Cache Access Time + (1 - Hit Ratio) × (Cache Access Time + Main Memory Access Time)

## Key Points

- Memory hierarchy organizes storage by speed: registers, cache, main memory (RAM), secondary storage
- Early systems had no memory management; single programs used all available memory
- Fixed partitioning caused internal fragmentation while dynamic partitioning led to external fragmentation
- The MMU is essential hardware for address translation and memory protection in modern systems
- Memory management objectives include efficiency, protection, isolation, and programmer simplicity
- Base and limit registers provide basic memory protection through bounds checking
- Translation Lookaside Buffer (TLB) caches recent address translations for performance
- Virtual memory combines paging and segmentation to provide large address spaces with protection

## Common Mistakes to Avoid

- Confusing internal and external fragmentation: internal occurs within allocated blocks, external occurs between them
- Believing virtual memory eliminates the need for physical memory; it merely extends available memory using secondary storage
- Assuming memory management overhead is negligible; TLB misses and page table lookups add latency to memory access
- Overlooking hardware support: memory management is not purely a software function but requires significant hardware assistance

## Revision Tips

- Create a timeline of memory management evolution to understand why each technique was developed
- Practice calculating internal and external fragmentation with numerical examples
- Review MMU operation with simple address translation examples
- Memorize the memory hierarchy order and characteristics of each level
- Focus on understanding why virtual memory was needed rather than just memorizing its features