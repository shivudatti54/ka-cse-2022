# Allocation of Frames - Summary

## Key Definitions and Concepts

- **Frame**: A fixed-size block of physical memory in a paged virtual memory system
- **Frame Allocation**: The distribution of available physical memory frames among competing processes
- **Working Set**: The set of pages actively used by a process during a specific time interval
- **Thrashing**: Excessive page fault activity caused by insufficient frame allocation, leading to poor system performance

## Important Formulas and Theorems

- **Equal Allocation**: Frames per process = Total frames / Number of processes
- **Proportional Allocation**: Frames for process i = (Size of process i / Total size of all processes) × Total frames
- **Working Set Model**: Process requires at least working set size frames to avoid thrashing

## Key Points

- Frame allocation determines how physical memory is distributed among processes in a paging system
- Equal allocation is simple but ignores varying process requirements
- Proportional allocation allocates based on process size, providing better memory utilization
- Priority-based allocation gives more frames to critical processes but may cause starvation
- Global replacement allows frame stealing across processes; local replacement restricts to process's own frames
- The working set model provides a theoretical foundation for determining minimum frame requirements
- Thrashing occurs when allocated frames are less than the working set size

## Common Mistakes to Avoid

- Confusing equal allocation with proportional allocation—equal gives same frames to all, proportional gives based on size
- Forgetting that working set size changes over time as process execution progresses
- Assuming thrashing is a memory shortage problem rather than an allocation problem
- Ignoring the distinction between global and local replacement when analyzing allocation scenarios

## Revision Tips

- Practice numerical problems involving both equal and proportional allocation calculations
- Memorize the relationship: Thrashing = Allocated frames < Working set size
- Create a comparison table of all three allocation strategies with advantages and disadvantages
- Understand that frame allocation and page replacement policies work together—always consider both
- Focus on why proportional allocation is generally preferred over equal allocation in practice