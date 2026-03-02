# Paging

## Overview

Paging is a memory management scheme that eliminates external fragmentation by dividing physical memory into fixed-size blocks called frames and logical memory into same-sized blocks called pages. The OS maintains a page table for each process to translate logical addresses to physical addresses.

## Key Points

- **Pages**: Fixed-size blocks of logical memory (typically 4KB or 8KB)
- **Frames**: Fixed-size blocks of physical memory, same size as pages
- **Page Table**: Maintained by OS for each process, maps page numbers to frame numbers
- **Address Translation**: Logical address = page number + page offset, physical address = frame number + page offset
- **No External Fragmentation**: Fixed-size allocation eliminates external fragmentation
- **Internal Fragmentation**: Last page may not use entire frame, causing internal fragmentation (average 0.5 frames per process)
- **Page Table Implementation**: Registers (fast, small tables), memory (slower, larger tables), TLB (fast cache)
- **Translation Lookaside Buffer (TLB)**: Small, fast cache of recent page-to-frame translations

## Important Concepts

- Page size is power of 2 (4KB = 2^12 bytes) simplifying address calculation
- Logical address space can be larger than physical memory (with virtual memory)
- Page table entry contains frame number and control bits (valid-invalid, protection, modified, referenced)
- TLB hit provides fast translation, TLB miss requires page table access

## Notes

- Practice calculating page numbers and offsets from logical addresses
- Understand how page size affects internal fragmentation and table size
- Know TLB speedup calculation and effective access time
- Remember paging eliminates external fragmentation but causes internal fragmentation
