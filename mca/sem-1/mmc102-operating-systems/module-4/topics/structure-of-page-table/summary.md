# Structure Of Page Table - Summary

## Key Definitions and Concepts

- **Page Table**: A data structure maintained by the operating system that maps virtual page numbers to physical frame numbers, enabling virtual memory address translation.

- **Page Table Entry (PTE)**: Contains the physical frame number, valid/invalid bit, protection bits (read/write/execute), dirty bit, and reference bit.

- **PTBR (Page Table Base Register)**: A CPU register that holds the starting physical address of the current process's page table.

- **Translation Lookaside Buffer (TLB)**: A hardware cache that stores recently used page table entries to accelerate address translation.

- **Hierarchical Page Table**: A multi-level page table structure where higher-level tables point to lower-level tables, allowing selective allocation of only needed page table pages.

- **Inverted Page Table**: A page table structure containing one entry per physical frame rather than per virtual page, indexed by physical frame number.

- **Hashed Page Table**: Uses a hash function to map virtual page numbers to hash table buckets, efficiently handling sparse address spaces.

## Important Formulas and Theorems

- **Virtual Address Division**: For n-level paging, virtual address is divided into n page number fields + 1 offset field
- **Page Table Size**: Single-level = (Number of virtual pages) × (PTE size)
- **Multi-level Space Savings**: Only allocated second-level tables contribute to memory overhead; unallocated virtual pages consume no page table space
- **Physical Address**: Physical Address = (Frame Number × Page Size) + Offset

## Key Points

- Page tables are essential for virtual memory, providing address translation and memory protection between processes.

- Single-level page tables are simple but wasteful for large address spaces (4MB overhead for 32-bit address space with 4KB pages).

- Multi-level (hierarchical) page tables like two-level or four-level structures allocate page table pages on demand, significantly reducing memory overhead.

- The x86-64 architecture implements 4-level paging (PML4 → PDPT → PD → PT) to support large virtual address spaces.

- Inverted page tables store one entry per physical frame, dramatically reducing memory overhead but requiring hash-based lookup.

- TLB caches are essential for performance because every memory access requires at least one page table lookup in main memory.

- Frame tables complement page tables by tracking the status and ownership of each physical memory frame.

## Common Mistakes to Confuse

- Confusing inverted page tables with traditional page tables: inverted tables are indexed by physical frame number, not virtual page number.

- Forgetting that hierarchical page tables require multiple memory accesses for translation—one per level plus one for the actual data access.

- Assuming all levels of a hierarchical page table must be resident; only the top-level (page directory) must always be in memory.

- Mixing up page tables with TLBs: TLBs are hardware caches, while page tables are software-managed data structures in memory.

## Revision Tips

1. Practice numerical problems involving address translation through multi-level page tables, identifying each component of the virtual address.

2. Create a comparison table of all page table structures, listing advantages, disadvantages, and typical use cases.

3. Draw the hierarchical page table structure and trace through an example address translation step by step.

4. Memorize the standard page table entry bits and their purposes—valid, protection, dirty, referenced are most frequently tested.

5. Understand whyTLB hit rate is critical: with a TLB miss, address translation requires 2+ memory accesses versus 1 with a TLB hit.