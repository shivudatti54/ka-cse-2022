# Memory Management Techniques - Summary

## Key Definitions and Concepts
- **Paging**: Fixed-size memory division with page tables for address translation
- **Segmentation**: Logical memory division with protection attributes
- **TLB**: Hardware cache for fast page table lookups
- **Working Set**: Pages actively used by a process within time window
- **Thrashing**: Excessive page faults due to insufficient memory allocation

## Important Formulas and Theorems
- `Physical Address = (Frame Number × Page Size) + Offset`
- `Effective Access Time = (TLB Hit Time × Hit Ratio) + (Miss Penalty × Miss Ratio)`
- **Belady's Anomaly**: FIFO may increase faults with more frames
- **Locality Principle**: Basis for caching and working set model

## Key Points
- Paging eliminates external fragmentation but causes internal fragmentation
- Multilevel page tables reduce memory overhead for large address spaces
- LRU approximation algorithms (Clock, Aging) used in practice
- Segmentation enables better memory protection and sharing
- Demand paging requires careful page replacement policy selection
- Copy-on-Write optimization used in process forking
- Memory-mapped files combine file I/O with virtual memory

## Common Mistakes to Avoid
- Confusing page table entries with segment descriptors
- Forgetting to check segment limits in address translation
- Misapplying page replacement algorithms to cache policies
- Neglecting TLB effects in access time calculations
- Assuming virtual memory eliminates need for physical RAM upgrades

## Revision Tips
- Practice at least 5 different page replacement problem sets
- Create comparison tables for memory management techniques
- Use memory visualization tools (e.g., OS simulator apps)
- Relate concepts to Linux/proc/meminfo output analysis
- Study past DU papers for numerical problem patterns