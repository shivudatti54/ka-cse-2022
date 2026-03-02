# Memory Management Strategies - Summary

## Key Definitions and Concepts

- **Memory Management**: The OS function that controls and coordinates computer memory, allocating portions to processes and maintaining the mapping between logical and physical memory.

- **Internal Fragmentation**: Wasted memory within an allocated partition or page when more memory than requested is provided.

- **External Fragmentation**: Scattered free memory blocks throughout memory that cannot satisfy a large memory request despite total free memory being sufficient.

- **Paging**: A memory management scheme that eliminates external fragmentation by dividing both physical and logical memory into fixed-size blocks called pages and frames.

- **Segmentation**: A memory management technique that divides memory into logically meaningful variable-sized segments.

- **Virtual Memory**: A technique that provides the illusion of a larger address space by combining physical memory and disk storage.

- **Page Fault**: An exception that occurs when a process accesses a page that is not currently in physical memory.

## Important Formulas and Theorems

- **Page Number**: virtual_address / page_size (integer division)
- **Offset**: virtual_address mod page_size
- **Physical Address**: (frame_number × page_size) + offset
- **Belady's Anomaly**: The counter-intuitive phenomenon where increasing the number of frames can increase page faults in FIFO replacement.

## Key Points

- Contiguous memory allocation (fixed and variable partitioning) suffers from fragmentation problems—fixed partitioning has internal fragmentation, variable partitioning has external fragmentation.

- Paging eliminates external fragmentation by allowing non-contiguous allocation but introduces internal fragmentation equal to half a page on average.

- Segmentation provides logical protection and meaningful address spaces but requires hardware support for implementation.

- FIFO is simple but can suffer from Belady's anomaly; LRU approximates optimal replacement but requires special hardware; Clock provides a practical compromise.

- The Translation Lookaside Buffer (TLB) is a hardware cache that speeds up address translation by storing recent page table entries.

- Virtual memory enables execution of programs larger than physical memory through demand paging.

## Common Mistakes to Avoid

- Confusing internal and external fragmentation—internal occurs within allocated blocks, external occurs between allocated blocks.

- Forgetting that offset must be less than page size when performing address translation calculations.

- Assuming that increasing frames always reduces page faults—remember Belady's anomaly with FIFO.

- Mixing up page numbers and frame numbers—pages are logical divisions, frames are physical divisions.

## Revision Tips

- Practice address translation problems multiple times until comfortable with the calculation method.

- Trace through page replacement algorithms with sample reference strings to build intuition.

- Create a comparison table of all memory management strategies listing their advantages, disadvantages, and fragmentation type addressed.

- Remember that modern systems use combinations of these strategies (segmented paging) rather than isolated approaches.