# Memory Management - Summary

## Key Definitions

- **Memory Management**: OS function controlling allocation and deallocation of physical memory to processes
- **Internal Fragmentation**: Wasted memory within allocated blocks due to fixed-size allocation units
- **External Fragmentation**: Scattered free memory blocks unable to satisfy large requests despite sufficient total free space
- **Page**: Fixed-size block of logical memory in paging systems
- **Frame**: Fixed-size block of physical memory in paging systems
- **Page Table**: Data structure mapping virtual page numbers to physical frame numbers
- **Page Fault**: Exception occurring when accessed page is not in physical memory
- **Virtual Memory**: Memory abstraction providing illusion of larger addressable space than physical memory
- **TLB (Translation Lookaside Buffer)**: Hardware cache storing recent address translations
- **Segmentation**: Memory management scheme dividing programs into logical segments of variable size

## Important Formulas

- **Physical Address Calculation (Paging)**: `Physical Address = (Frame Number × Page Size) + Offset`
- **Virtual Page Number**: `VPN = Virtual Address / Page Size`
- **Offset**: `Offset = Virtual Address mod Page Size`
- **Effective Access Time (with TLB)**: `EAT = Hit Ratio × (TLB + Memory) + (1 - Hit Ratio) × (TLB + 2 × Memory)`
- **Page Fault Rate**: `PFF = Number of Page Faults / Total Memory References`

## Key Points

1. Memory management must balance efficiency, protection, and flexibility while maximizing utilization of physical memory resources.

2. Contiguous allocation suffers from external fragmentation; paging eliminates external fragmentation but introduces internal fragmentation.

3. Paging uses fixed-size pages/frames enabling any free frame to satisfy any page request, simplifying memory allocation significantly.

4. Segmentation reflects logical program structure (code, data, stack) with variable-sized segments, enabling natural protection and sharing.

5. Virtual memory extends available memory using disk storage, allowing execution of programs larger than physical RAM through demand paging.

6. Page replacement algorithms determine which pages to evict when memory is full; LRU approximates optimal but Clock is more practical to implement.

7. TLB significantly improves address translation speed by caching recent virtual-to-physical mappings, reducing page table lookup frequency.

8. Modern operating systems combine multiple techniques—most use paged virtual memory with demand loading as the foundation.

## Common Mistakes

1. **Confusing page and frame**: Pages are virtual memory units; frames are physical memory units. A page maps to exactly one frame.

2. **Forgetting offset bounds**: When translating addresses, always verify that offset is less than page size; otherwise, the address is invalid.

3. **Belady's anomaly misconception**: Many assume more frames always reduce page faults; FIFO can exhibit more faults with more frames.

4. **Ignoring page fault overhead**: Page faults require disk I/O (milliseconds) vs. memory access (nanoseconds), making them extremely expensive.

5. **Mixing segmentation and paging**: They are distinct concepts—segmentation provides logical organization, paging provides physical allocation; systems can use one or both.