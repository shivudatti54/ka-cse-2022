# Thrashing - Summary

## Key Definitions and Concepts

- **Thrashing**: A severe performance degradation in virtual memory systems where the CPU spends more time paging than executing user instructions, caused by excessive page fault rates when physical memory is insufficient
- **Working Set**: The set of pages a process has referenced within a specific time window (τ), representing the pages that must remain in memory for efficient execution
- **Page Fault Frequency**: The rate at which a process generates page faults, measured as page faults per memory reference or per time unit
- **Degree of Multiprogramming**: The number of processes currently resident in physical memory

## Important Formulas and Theorems

- **Total Working Set Demand**: ΣWSS_i (sum of working set sizes of all processes). Thrashing occurs when this exceeds available physical memory.
- **Effective Access Time**: EAT = (1 - p) × Ma + p × Mt, where p = page fault probability, Ma = memory access time, Mt = page fault service time
- **Page Fault Rate**: Number of page faults / Total memory references
- **Working Set Size**: Number of distinct pages referenced in the last τ time units

## Key Points

- Thrashing occurs when the total demand for pages exceeds the available physical memory, causing constant page evictions and reloads
- CPU utilization initially increases with degree of multiprogramming but drops sharply when thrashing begins
- The working set model prevents thrashing by ensuring each process has its working set in memory
- The page fault frequency model uses upper and lower thresholds to allocate or reclaim frames
- During thrashing, effective access time can increase by 1000x or more compared to normal operation
- Thrashing creates a feedback loop: more page faults lead to more paging, which causes more page faults
- Solutions include controlling multiprogramming degree, using working set or PFF algorithms, and providing adequate memory to processes

## Common Mistakes to Avoid

- Confusing thrashing with normal page faults: thrashing is characterized by a sustained high rate of page faults, not occasional faults during program startup
- Forgetting to convert time units when calculating effective access time (nanoseconds vs. milliseconds)
- Assuming that adding more processes always improves CPU utilization—beyond a certain point, it causes thrashing and reduces utilization
- Misunderstanding that global replacement can accelerate thrashing by allowing processes to steal frames from already memory-stressed processes

## Revision Tips

- Practice drawing the CPU utilization vs. degree of multiprogramming curve and labeling the thrashing region
- Memorize the effective access time formula and practice numerical problems with different page fault rates
- Understand the working set concept by considering how program locality affects memory requirements
- Review the differences between working set model and page fault frequency model as approaches to thrashing control
- Solve previous year DU question papers to familiarize yourself with examination patterns and important topics