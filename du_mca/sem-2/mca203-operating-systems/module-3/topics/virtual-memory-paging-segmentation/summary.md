# Virtual Memory: Paging and Segmentation - Summary

## Key Definitions and Concepts

- **Virtual Memory**: An abstraction that provides processes with the illusion of having a contiguous, large address space, independent of physical memory availability
- **Page**: Fixed-size block in virtual memory address space
- **Frame**: Fixed-size block in physical memory corresponding to page size
- **Page Table**: Data structure mapping virtual page numbers to physical frame numbers
- **TLB (Translation Lookaside Buffer)**: Hardware cache for storing recent virtual-to-physical address translations
- **Page Fault**: Exception raised when a process accesses a page not currently in physical memory
- **Segment**: Variable-sized logical division of a program (code, data, stack, etc.)
- **Segmentation Fault**: Memory access violation when offset exceeds segment limit

## Important Formulas and Theorems

- **Virtual Address Format**: Virtual Address = (Page Number × Page Size) + Offset
- **Offset Bits**: log₂(Page Size) — e.g., 4KB page = 12 bits
- **Effective Access Time (EAT)**: Hit_Ratio × (TLB + Memory) + (1 - Hit_Ratio) × (TLB + 2 × Memory)
- **Number of Virtual Pages**: 2^(Address_Bits - Offset_Bits)
- **Page Table Size**: Number of Virtual Pages × PTE_Size
- **Belady's Anomaly**: FIFO can exhibit increased page faults with more physical frames

## Key Points

1. Virtual memory enables execution of programs larger than physical RAM by using secondary storage as backing store
2. Paging eliminates external fragmentation but introduces internal fragmentation; page size is a critical design parameter
3. The TLB is essential for performance—systems typically achieve 90%+ hit ratios; low TLB hit rates severely degrade performance
4. Segmentation reflects logical program structure (functions, arrays, stacks) and provides natural protection boundaries
5. Combined paged-segmentation systems leverage advantages of both approaches
6. Page replacement algorithms are evaluated based on page fault rate; LRU approximates Optimal but is harder to implement efficiently
7. Thrashing occurs when processes lack sufficient frames, causing excessive page fault activity and degraded system performance

## Common Mistakes to Avoid

1. **Confusing page and segment numbers**: Pages are fixed-size, indexed by page number; segments are variable-sized, indexed by segment number
2. **Forgetting to check offset validity**: In segmentation, always verify offset < limit before calculating physical address
3. **Ignoring dirty bit in replacement**: Modified pages require write-back to disk, adding significant overhead
4. **Assuming more frames always helps**: Remember Belady's Anomaly with FIFO algorithm
5. **Overlooking TLB miss penalty**: Each TLB miss requires additional memory access to page table

## Revision Tips

1. Practice drawing the virtual-to-physical address translation process for both paging and segmentation
2. Memorize the page fault service routine steps—they frequently appear in exams
3. Solve numerical problems on EAT calculation and address translation—they are high-weightage topics
4. Create comparison tables between paging and segmentation covering fragmentation, protection, and sharing
5. Review the trade-offs between different page replacement algorithms and their implementation complexities
6. Understand the relationship between working set, frame allocation, and thrashing