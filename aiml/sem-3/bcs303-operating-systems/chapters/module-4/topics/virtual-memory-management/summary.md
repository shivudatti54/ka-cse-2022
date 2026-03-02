# Virtual Memory Management - Summary

## Key Definitions and Concepts

- **Virtual Memory**: A memory management technique that creates an abstraction layer between logical (virtual) addresses used by programs and physical addresses in RAM, allowing programs to use more memory than physically available.

- **Virtual Address Space**: The range of virtual addresses available to a process, typically much larger than physical memory. In 32-bit systems, this is 4 GB; in 64-bit systems, it is practically unlimited.

- **Page Table**: A data structure maintained by the OS that maps virtual page numbers to physical frame numbers. Each entry (PTE) contains frame number, valid bit, protection bits, dirty bit, and reference bit.

- **TLB (Translation Lookaside Buffer)**: A hardware cache that stores recent virtual-to-physical address translations for fast lookup, avoiding expensive page table walks.

- **Page Fault**: An exception that occurs when a process accesses a page not currently in physical memory, triggering the OS to load the page from disk.

- **Copy-on-Write (COW)**: An optimization where pages are shared between processes until modification is required, at which point private copies are created.

## Important Formulas and Theorems

- **Physical Address Calculation**: Physical Address = (Frame Number × Page Size) + Offset

- **Virtual Page Number**: Virtual Page Number = Virtual Address / Page Size (integer division)

- **Effective Access Time**: EAT = (Hit Rate × TLB Access Time) + (Miss Rate × Page Table Access Time)

- **Number of Pages**: Number of Pages = Virtual Address Space / Page Size

- **Number of Frames**: Number of Frames = Physical Memory / Page Size

## Key Points

- Virtual memory enables execution of programs larger than physical RAM by using disk as temporary storage for inactive pages.

- Address translation is performed by the MMU using page tables, with TLB providing fast caching of recent translations.

- Page replacement algorithms (FIFO, LRU, Optimal) determine which page to evict when physical memory is full and a new page must be loaded.

- Virtual memory provides memory protection through separate address spaces for each process and hardware-enforced access rights.

- Belady's Anomaly (FIFO Anomaly) demonstrates that adding more frames can sometimes increase page faults with FIFO algorithm.

- Demand paging loads pages only when referenced, improving startup time and reducing memory usage.

- Hierarchical page tables and inverted page tables are used to manage page tables efficiently for large address spaces.

## Common Mistakes to Avoid

1. Confusing virtual memory with physical memory—virtual addresses do not exist physically; they are logical constructs translated by the MMU.

2. Forgetting that page offset remains unchanged during address translation—only the page number is mapped to a different frame.

3. Miscalculating page table sizes—remember to account for the number of entries and the size of each entry.

4. Overlooking the TLB when calculating effective memory access time—its presence significantly reduces average access time.

5. Assuming more frames always improves performance—FIFO can exhibit worse performance with more frames due to Belady's anomaly.

## Revision Tips

1. Practice numerical problems on address translation until you can solve them quickly and accurately.

2. Draw the page table and TLB for sample sequences to visualize how page faults occur and how replacement works.

3. Memorize the sequence of operations during page fault handling: trap → save state → determine virtual address → locate page → allocate frame → load page → update table → restart instruction.

4. Compare the three major page replacement algorithms (FIFO, LRU, Optimal) with respect to implementation complexity and performance characteristics.

5. Review past DU examination questions on virtual memory to understand the pattern and difficulty level of problems typically asked.