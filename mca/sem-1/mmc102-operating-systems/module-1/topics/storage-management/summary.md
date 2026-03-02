# Storage Management - Summary

## Key Definitions and Concepts

- **Primary Memory (RAM)**: Fast, volatile memory where currently executing programs reside; managed directly by the operating system for process execution.
- **Secondary Storage**: Non-volatile storage (disks, SSDs) used for permanent data; accessed through file systems and serving as backing store for virtual memory.
- **External Fragmentation**: Scattered free memory blocks that cannot satisfy large requests despite sufficient total free space; occurs in contiguous allocation.
- **Internal Fragmentation**: Wasted memory within allocated blocks due to fixed allocation units; difference between allocated and requested size.
- **Paging**: Memory management scheme dividing logical and physical memory into fixed-size pages and frames; eliminates external fragmentation.
- **Page Table**: Data structure mapping virtual page numbers to physical frame numbers; maintained by operating system for address translation.
- **TLB (Translation Lookaside Buffer)**: Hardware cache storing recent page table entries for fast virtual-to-physical address translation.
- **Virtual Memory**: Technique extending logical address space beyond physical memory using secondary storage as backing store.
- **Page Fault**: Exception occurring when accessed page is not in physical memory; triggers page loading from secondary storage.
- **Thrashing**: Excessive paging activity degrading system performance when physical memory is overcommitted.

## Important Formulas and Theorems

- **EMAT = Hit_Rate × (TLB_Time + Mem_Time) + Miss_Rate × (TLB_Time + 2 × Mem_Time)**: Effective memory access time accounting for TLB and page table lookup.
- **Virtual Address = Page_Number × Page_Size + Offset**: Composition of logical address in paging systems.
- **Belady's Anomaly**: Increasing physical frames can increase page faults with FIFO algorithm.
- **Working Set Model**: Set of pages a process has referenced within the past τ time units; defines minimum frames needed to avoid thrashing.

## Key Points

- Memory hierarchy ranges from fast, expensive, small capacity (registers, cache) to slow, cheap, large capacity (disk storage).
- Contiguous allocation suffers from external fragmentation; paging solves this but introduces internal fragmentation.
- Multi-level page tables reduce memory overhead for sparse address spaces by allocating second-level tables on-demand.
- Segmentation provides logical memory view matching program structure; paging provides physical memory efficiency; combined systems use both.
- LRU approximates optimal page replacement but is difficult to implement in hardware; clock algorithm provides practical approximation.
- Demand paging loads pages only when referenced, allowing execution of programs larger than physical memory.
- TLB significantly reduces address translation overhead by caching frequently used page table entries.
- Thrashing is diagnosed by low CPU utilization despite high paging I/O; solutions include adding memory or reducing multiprogramming.

## Common Mistakes to Avoid

- Confusing internal and external fragmentation—internal occurs within allocated blocks due to fixed sizes; external occurs between allocated blocks.
- Treating segmentation and paging as mutually exclusive—modern systems combine both (segmented paging or paging segments).
- Assuming increasing frames always improves performance—FIFO exhibits Belady's anomaly where more frames cause more faults.
- Forgetting that page fault handling requires disk I/O (milliseconds), making it vastly slower than memory access (nanoseconds).

## Revision Tips

1. Draw the memory hierarchy diagram and explain trade-offs at each level before exam.

2. Practice calculating fragmentation for different allocation scenarios to solidify understanding.

3. Trace through page replacement algorithms with sample reference strings—hand-tracing builds intuition.

4. Remember that virtual memory enables programs to use more memory than physically available but at performance cost during page faults.