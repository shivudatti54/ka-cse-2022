# Allocation of Frames - Summary

## Key Definitions and Concepts

- FRAME: A fixed-size block of physical memory in a paging system, typically 4KB in modern systems.
- PAGE: A logical block of a process's virtual address space that maps to a frame.
- PAGE TABLE: Data structure that maps virtual pages to physical frames.
- FRAME ALLOCATION: The strategy used by the operating system to distribute available physical memory frames among competing processes.
- THRASHING: Excessive page fault activity that occurs when processes do not have enough frames, causing the system to spend more time paging than executing.
- WORKING SET: The set of pages a process has referenced during a recent time window.

## Important Formulas and Theorems

- Equal Allocation: Frames per process = Total frames / Number of processes

- Proportional Allocation: Frames for process i = (Size of process i / Total virtual size of all processes) × Total available frames

- Minimum Frames: Must be at least equal to the maximum number of different pages that can be referenced by any single machine instruction (typically equals the number of memory operands an instruction can access)

## Key Points

1. Frames are the physical unit of memory allocation in paging systems, while pages are the logical unit.

2. The minimum frames per process prevents immediate thrashing and is determined by CPU architecture.

3. Equal allocation is simple but ignores process-specific needs, leading to potential inefficiency.

4. Proportional allocation provides better utilization by distributing frames based on process size or other factors.

5. Priority-based allocation ensures critical processes receive more frames but may cause starvation of low-priority processes.

6. The working set model allocates frames dynamically based on actual page usage patterns.

7. Local replacement maintains consistent frame allocation per process, while global replacement allows redistribution.

8. Modern operating systems typically combine multiple strategies (proportional with priority adjustments).

9. Proper frame allocation directly impacts system throughput and prevents thrashing.

10. The choice of allocation strategy affects both individual process performance and overall system efficiency.

## Common Mistakes to Avoid

1. Confusing pages with frames—pages are logical, frames are physical.

2. Forgetting that total allocated frames cannot exceed available frames in the system.

3. Assuming equal allocation is always inefficient—it works well when process sizes are similar.

4. Ignoring the minimum frames requirement when calculating allocations.

5. Confusing frame allocation with page replacement—these are related but distinct concepts.

## Revision Tips

1. Practice numerical problems on proportional allocation until comfortable with the calculations.

2. Create a comparison table of all allocation strategies with pros and cons.

3. Memorize the relationship between frame allocation, page faults, and thrashing.

4. Review how modern operating systems implement these concepts in practice.

5. Solve previous year DU examination questions on this topic to understand the question patterns.