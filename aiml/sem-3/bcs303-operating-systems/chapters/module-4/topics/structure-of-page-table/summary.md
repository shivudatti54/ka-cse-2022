# Structure of Page Table - Summary

## Key Definitions and Concepts

- **Page Table**: A data structure maintained by the operating system that maps virtual page numbers to physical frame numbers, enabling virtual memory implementation.

- **Page Table Entry (PTE)**: A single entry in the page table containing the physical frame number and control bits for one virtual page.

- **Hierarchical Page Table**: A multi-level page table structure where upper-level tables index into lower-level tables, created only for valid virtual memory regions.

- **Inverted Page Table**: A page table structure with one entry per physical frame rather than per virtual page, reducing memory overhead significantly.

- **Translation Lookaside Buffer (TLB)**: A hardware cache that stores recent virtual-to-physical address translations for fast access.

## Important Formulas and Theorems

- Number of virtual pages = 2^(virtual address bits - page offset bits)
- Flat page table size = Number of virtual pages × PTE size
- Physical address = Frame number × Page size + Offset
- Two-level page table addressing: Virtual address = PD_index | PT_index | Offset

## Key Points

- Page table entries contain the frame number plus control bits: valid/invalid, protection, dirty, and reference bits.

- Flat page tables are simple but waste memory for sparse address spaces—requiring 4MB for a 32-bit address space per process.

- Hierarchical page tables (two-level, three-level, four-level) reduce memory overhead by allocating only needed second-level tables.

- Inverted page tables have O(1) memory overhead but slower O(n) translation requiring hash table acceleration.

- TLB is critical for performance—a typical hit rate above 95% makes virtual memory nearly as fast as physical memory access.

- Protection bits in PTEs enforce read/write/execute permissions and prevent unauthorized memory access.

- The dirty bit tracks modifications for proper page eviction; the reference bit supports LRU-based page replacement.

## Common Mistakes to Avoid

- Confusing page number with frame number—page number indexes the page table, frame number indicates physical location.

- Forgetting that hierarchical page table access requires multiple memory lookups, increasing latency compared to flat tables.

- Assuming larger page sizes always improve performance—while reducing page table size, they cause internal fragmentation.

- Overlooking that TLB entries must be invalidated or tagged with ASIDs when processes switch contexts.

## Revision Tips

1. Draw the structure of a PTE and label all fields from memory to reinforce understanding.

2. Practice numerical problems on page table size calculation and address translation through multi-level tables.

3. Create a comparison table of page table types with advantages, disadvantages, and use cases.

4. Remember that modern 64-bit systems use four-level page tables (PGD → PUD → PMD → PTE) to handle the vast address space efficiently.