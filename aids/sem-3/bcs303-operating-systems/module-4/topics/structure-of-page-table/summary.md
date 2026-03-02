# Structure of Page Table - Summary

## Key Definitions

- **Page Table**: A data structure maintained by the operating system that maps virtual page numbers to physical frame numbers
- **Page Table Entry (PTE)**: A single entry in the page table containing the frame number and control bits for a virtual page
- **Hierarchical Page Table**: A multi-level tree structure where the page table is divided into multiple levels to reduce memory overhead
- **Inverted Page Table**: A page table structure that maintains one entry per physical frame rather than per virtual page
- **Translation Lookaside Buffer (TLB)**: A hardware cache that stores recent page table translations for faster access

## Important Formulas

- **Number of pages** = 2^(logical address bits - page offset bits)
- **Page table size** = Number of pages × Size of each PTE
- **Two-level address format**: [PD bits][PT bits][Offset bits] where PD + PT + Offset = address bits

## Key Points

1. Page tables provide the mapping between virtual addresses and physical addresses in a paged memory management system
2. Each PTE contains the frame number, valid bit, protection bits, dirty bit, and reference bit
3. Single-level page tables are simple but consume excessive memory for large address spaces
4. Hierarchical page tables reduce memory overhead by allocating only needed second-level tables
5. Inverted page tables dramatically reduce memory requirements but require hash-based lookup
6. The page size trade-off: smaller pages reduce internal fragmentation but increase page table size
7. TLB caching improves performance for hierarchical page tables by avoiding multiple memory accesses

## Common Mistakes

1. Confusing virtual page numbers with physical frame numbers - they serve different purposes in address translation
2. Forgetting that the page offset remains unchanged during address translation
3. Assuming larger page sizes always improve performance - they increase internal fragmentation
4. Neglecting the valid bit check, which can lead to page fault handling errors
5. Not considering that inverted page tables require searching, making them slower than hierarchical tables for certain workloads