# Thrashing - Summary

## Key Definitions and Concepts

- Thrashing: A severe performance degradation in virtual memory systems where the CPU spends most of its time handling page faults rather than executing processes, caused by excessive paging activity.

- Working Set: The set of pages that a process has referenced within a time window T (working set window), representing the pages that must remain resident for efficient execution.

- Degree of Multiprogramming: The number of processes simultaneously resident in physical memory; must be balanced to avoid thrashing while maximizing CPU utilization.

- Page Fault Frequency: The rate at which a process experiences page faults, used as a metric for controlling memory allocation and detecting thrashing.

## Important Formulas and Theorems

- Total Working Set Demand = Sum of working set sizes of all processes in memory

- Thrashing Condition: Total Working Set Demand > Available Physical Memory Frames

- Page Fault Rate Relationship: More allocated frames generally produce fewer page faults, following a curve with diminishing returns

## Key Points

- Thrashing occurs when physical memory cannot accommodate the combined working sets of all running processes.

- The thrashing cycle is self-reinforcing: page faults cause evictions, which cause more page faults.

- CPU utilization drops dramatically during thrashing because the system becomes I/O bound.

- Working set model provides theoretical foundation for preventing thrashing through proper memory allocation.

- Page fault frequency monitoring automatically adjusts frame allocation to prevent thrashing.

- Common causes include excessive multiprogramming, insufficient memory, and poor application locality.

- Resolution strategies include reducing workload, adding memory, or optimizing applications.

## Common Mistakes to Avoid

- Confusing high memory usage with thrashing: thrashing specifically requires HIGH PAGE FAULT RATES, not just high memory consumption.

- Believing that adding more processes always improves performance: beyond a certain point, additional processes cause thrashing and reduce overall throughput.

- Assuming linear relationship between frames and page faults: the relationship follows diminishing returns.

- Ignoring the cost of disk I/O: page faults are orders of magnitude slower than memory accesses.

## Revision Tips

1. Memorize the thrashing condition: Total Working Set Demand > Physical Memory = Thrashing.

2. Remember the key indicator: LOW CPU + HIGH DISK I/O = THRASHING.

3. Practice calculating whether given working set sizes will cause thrashing with available memory.

4. Review how degree of multiprogramming affects both CPU utilization and thrashing.

5. Understand that the working set window size T affects working set accuracy and thrashing prediction.