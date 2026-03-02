# Paging - Summary

## Key Definitions

- **Page**: A fixed-size block of logical memory, typically 4KB, 8KB, or power of 2 bytes.
- **Frame**: A fixed-size block of physical memory of the same size as a page.
- **Page Table**: A data structure that maps logical page numbers to physical frame numbers.
- **Translation Lookaside Buffer (TLB)**: A hardware cache that stores recently used page table entries for faster address translation.
- **Page Fault**: An exception that occurs when a referenced page is not present in physical memory.

## Important Formulas

- **Page Number**: Logical Address ÷ Page Size
- **Offset**: Logical Address mod Page Size
- **Physical Address**: (Frame Number × Page Size) + Offset
- **Number of Pages**: Logical Address Space / Page Size
- **Number of Frames**: Physical Memory / Page Size

## Key Points

1. Paging eliminates external fragmentation by allowing non-contiguous allocation of physical memory.

2. The Memory Management Unit (MMU) performs hardware-based address translation using the page table.

3. Each process has its own private page table, stored in kernel memory.

4. Page size is a design decision - larger critical pages reduce page table size fragmentation.

5. but increase internal Multi-level page tables reduce address spaces.

6. The TLB provides memory overhead for sparse fast translation for address accessed pages with typical frequently hit rates of 80-99%.

7. Paging enables virtual memory, allowing processes to use more memory than physically available.

8. Protection bits in page table entries prevent unauthorized access to pages.

## Common Mistakes

1. Confusing page number with frame number - they serve different purposes in address Forgetting that translation.

2. the offset remains unchanged translation since during address pages and frames are equal-sized accounting for internal.

3. Not fragmentation when calculating actual memory usage with paging.

4. page sizes Assuming larger always improve performance - they increase memory waste from internal fragmentation.

5. Ignoring TLB performance impact on overall system performance despite its critical role in address translation.