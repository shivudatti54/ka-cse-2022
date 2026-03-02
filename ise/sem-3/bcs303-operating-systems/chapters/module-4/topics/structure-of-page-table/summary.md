# Structure of Page Table - Summary

## Key Definitions and Concepts

A page table is a data structure used by operating systems with paged virtual memory to map virtual addresses to physical addresses. Each entry in the page table is called a Page Table Entry (PTE) and contains the frame number where the corresponding virtual page resides in physical memory.

Virtual memory creates an illusion of larger memory by using secondary storage to hold pages not currently in physical memory. The page table tracks which virtual pages are in memory, their physical locations, and access permissions.

A Translation Lookaside Buffer (TLB) is a hardware cache that stores recent virtual-to-physical address translations to speed up memory access. It acts as an associative memory with extremely fast lookup.

## Important Formulas and Theorems

Address Translation: Physical Address = Frame Number × Page Size + Offset

For a logical address with p bits and page size of 2^n bytes:
- Offset bits = n
- Page number bits = p - n

Page Table Size (Single-Level): Number of Entries × Entry Size = 2^(p-n) × Entry_Size

Effective Memory Access Time (EAT):
EAT = Hit_Rate × TLB_Access_Time + (1 - Hit_Rate) × (TLB_Access_Time + Memory_Access_Time)

## Key Points

- Page table entries typically contain: frame number, valid/invalid bit, protection bits, referenced bit, and modified bit
- The valid bit indicates whether a page is currently resident in physical memory; invalid pages trigger page faults when accessed
- The modified (dirty) bit tracks whether a page has been changed and must be written back to disk before eviction
- The referenced (accessed) bit helps page replacement algorithms identify recently used pages
- Single-level page tables consume significant memory for large address spaces (4MB for 32-bit system with 4KB pages)
- Hierarchical (multi-level) page tables allocate page tables on demand, reducing memory overhead for sparse address spaces
- Inverted page tables store one entry per physical frame instead of per virtual page, dramatically reducing table size
- TLBs achieve high hit rates (typically >90%) due to temporal and spatial locality in program execution
- Protection bits in PTEs enforce read, write, and execute permissions for memory pages

## Common Mistakes to Avoid

Confusing page number with frame number is a frequent error. The page number indexes into the page table, while the frame number indicates the actual physical location in memory. These are fundamentally different values.

Forgetting to include the offset when calculating physical addresses leads to incomplete answers. The offset from the virtual address must be added to the frame number multiplied by page size.

Misunderstanding the purpose of the modified bit causes confusion. This bit indicates whether memory contents differ from disk copy, requiring a write-back operation during page replacement.

Ignoring the overhead of hierarchical page table access is another common mistake. Each level of the page table hierarchy requires an additional memory access, potentially negating space savings with time costs.

## Revision Tips

Practice numerical problems involving address translation until you can solve them quickly and accurately. This is the most scoring portion of the topic in examinations.

Create a comparison table of different page table organizations, noting their advantages, disadvantages, and ideal use cases. This helps in answering conceptual questions.

Remember that page table entries are stored in physical memory, not virtual memory. The page table base register (PTBR) points to the page table's physical address.

When studying TLBs, always remember the two-step process: first check TLB, then if miss occurs, access page table and update TLB. Both steps add to memory access latency in case of TLB miss.