# Allocation Of Frames - Summary

## Key Definitions

- **Frame**: A fixed-size block of physical memory in a paging system
- **Frame Allocation**: The distribution of available physical frames among competing processes
- **Page Fault**: Occurs when a process references a page not currently in memory
- **Thrashing**: Excessive paging activity due to insufficient frames, degrading performance
- **Working Set**: The set of pages referenced by a process in the most recent τ time units

## Important Formulas

- **Equal Allocation**: Frames per process = m / n (where m = total frames, n = processes)

- **Proportional Allocation**: a_i = (s_i / S) × m
- a_i = frames for process i
- s_i = size of process i
- S = total size of all processes
- m = total frames available

- **Working Set Size**: W(t, τ) = pages referenced in time interval [t-τ, t]

## Key Points

1. Frame allocation determines how physical memory is distributed among processes in a paging system

2. Equal allocation is simple but ignores process characteristics and requirements

3. Proportional allocation assigns frames based on process size, improving efficiency

4. Variable allocation allows dynamic adjustment of frames during process execution

5. Global replacement offers flexibility but can cause interference between processes

6. Local replacement provides isolation but may lead to suboptimal frame utilization

7. The working set model helps determine appropriate frame allocation dynamically

8. Insufficient frame allocation leads to thrashing and severe performance degradation

9. Higher degree of multiprogramming requires smaller frame allocation per process

10. Minimum frames per process depends on instruction set architecture and addressing modes

## Common Mistakes

1. Confusing frame allocation with page replacement - they are separate concepts

2. Forgetting that equal allocation may leave frames unused if not evenly divisible

3. Not considering that proportional allocation requires knowing process sizes at load time

4. Overlooking the impact of local vs global replacement on allocation effectiveness

5. Assuming more frames always improves performance - there's a point of diminishing returns
