# Memory Management Strategies - Summary

## Key Definitions and Concepts

- **Swapping**: Moving entire processes between main memory and secondary storage to manage memory scarcity.
- **Contiguous Memory Allocation**: Assigning each process a single continuous block of memory using allocation algorithms (First-Fit, Best-Fit, Worst-Fit).
- **Paging**: Memory management scheme dividing both physical and virtual memory into fixed-size blocks (frames and pages) to eliminate external fragmentation.
- **Segmentation**: Dividing memory into logical segments (code, data, stack, heap) based on program structure with base and limit registers.
- **Virtual Memory**: Technique extending physical memory using disk space, allowing programs larger than RAM to execute.
- **Demand Paging**: Loading pages into memory only when referenced, reducing initial load time and memory consumption.
- **Thrashing**: Excessive paging activity causing degraded system performance when processes lack sufficient memory frames.

## Important Formulas and Theorems

- **Effective Access Time (EAT)** = (1 - p) × Memory Access Time + p × Page Fault Service Time
  - Where p = page fault rate

- **Hit Ratio** = Number of memory hits / Total memory references

- **Belady's Anomaly**: Increasing frames in FIFO can increase page faults (counter-intuitive phenomenon)

- **Working Set**: Set of pages a process has referenced in the last τ references

## Key Points

- Memory management strategies evolved from simple swapping to complex virtual memory systems
- Contiguous allocation suffers from external fragmentation; paging eliminates it but introduces internal fragmentation
- Page replacement algorithms (FIFO, LRU, Optimal, Clock) determine which pages to evict when memory is full
- Virtual memory provides process isolation and enables execution of programs larger than physical RAM
- The MMU (Memory Management Unit) translates virtual addresses to physical addresses using page tables
- Multi-level page tables reduce memory overhead for large address spaces
- Thrashing occurs when excessive paging degrades performance; working set model helps prevent it
- Copy-on-write optimizes process creation by deferring page copies until modification

## Common Mistakes to Confuse

- Confusing internal fragmentation (paging) with external fragmentation (contiguous allocation)
- Believing Optimal replacement can be implemented (it requires future knowledge)
- Confusing page fault rate with hit ratio (they sum to 1)
- Forgetting that segmentation is programmer-visible while paging is transparent

## Revision Tips

1. Practice numerical problems on page replacement algorithms with different reference strings until you can solve them quickly and accurately.

2. Create comparison tables for all memory management strategies, noting advantages, disadvantages, and typical use cases.

3. Memorize the key formulas for effective access time and be comfortable substituting values and interpreting results.

4. Review past DU examination papers to understand the question patterns and important topics that recur frequently.

5. When studying page tables, draw diagrams showing address translation to reinforce conceptual understanding.