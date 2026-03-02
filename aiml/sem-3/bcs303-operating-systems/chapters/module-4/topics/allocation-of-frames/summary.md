# Allocation of Frames - Summary

## Key Definitions and Concepts

- **Frame**: A fixed-size block of physical memory in a paging system, typically ranging from 512 bytes to 8 KB.
- **Page**: A fixed-size block of logical (virtual) memory that maps to a frame when loaded in physical memory.
- **Frame Allocation**: The process of distributing available physical memory frames among competing processes.
- **Working Set**: The set of pages a process is currently actively using; processes perform efficiently when their working set fits in allocated frames.

## Important Formulas and Theorems

- **Equal Allocation**: Frames per process = Total frames / Number of processes
- **Proportional Allocation**: Frames for process i = (Size of process i / Total size of all processes) × Total available frames
- **Working Set Model**: A process should be allocated enough frames to hold its current working set to avoid thrashing.

## Key Points

1. Frame allocation determines how physical memory is distributed among processes in a paging system.

2. Equal allocation provides simplicity and fairness but wastes memory when process sizes differ significantly.

3. Proportional allocation matches frame distribution to actual process size, generally improving memory utilization.

4. Priority-based allocation gives preferential treatment to critical processes but requires careful management to prevent starvation.

5. Global allocation allows processes to steal frames from other processes, maximizing throughput but reducing individual process predictability.

6. Local allocation restricts each process to its allocated frames, providing predictable performance but potentially poor system-wide utilization.

7. The working set model helps identify when processes have sufficient frames and when thrashing may occur.

8. Free frame list management is essential for handling page faults when no unallocated frames exist.

## Common Mistakes to Remember

1. Confusing frames (physical) with pages (logical) - frames exist in RAM, pages exist in virtual address space.

2. Using local replacement when global is specified, or vice versa, in calculation problems.

3. Forgetting that proportional allocation must account for all processes in the system.

4. Assuming equal allocation is always bad - it works well when all processes have similar memory requirements.

5. Overlooking the fact that total allocated frames cannot exceed available frames in the system.

## Revision Tips

1. Practice calculating both equal and proportional allocations with different numbers of processes and frames.

2. Create a comparison table of all allocation strategies with advantages, disadvantages, and suitable use cases.

3. Understand that frame allocation and page replacement are related but distinct concepts—allocation decides how many frames a process gets, replacement decides which page to evict when needed.

4. Review the relationship between frame allocation and thrashing, as this connects to the broader memory management module.