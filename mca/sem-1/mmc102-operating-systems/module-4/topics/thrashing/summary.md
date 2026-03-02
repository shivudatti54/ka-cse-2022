# Thrashing - Summary

## Key Definitions and Concepts

- Thrashing: Excessive paging activity where the system spends more time servicing page faults than executing useful work, causing severe performance degradation

- Working Set: The set of pages a process has referenced during the most recent τ (tau) time units or memory references

- Page Fault Frequency (PFF): The rate at which a process experiences page faults, used as a metric for controlling memory allocation

- Degree of Multiprogramming: The number of processes actively competing for CPU and memory resources simultaneously

- Virtual Memory: Memory management technique that allows execution of processes that may not be completely in physical memory

## Important Formulas and Theorems

- Working Set Size: Number of unique pages referenced within the window τ

- Page Fault Rate: Page faults per unit of time or per N memory references

- Thrashing Condition: Total working set sizes of all processes > Available physical memory frames

- PFF Control Rules: Allocate frames when fault rate > upper threshold; reclaim frames when fault rate < lower threshold

## Key Points

- Thrashing occurs when processes cannot hold their working sets in physical memory, leading to continuous page evictions and fault cycles

- The working set model requires that each process receives at least enough frames to contain its working set; otherwise thrashing occurs

- Page fault frequency control dynamically adjusts frame allocation based on measured fault rates rather than estimated working sets

- Primary symptoms of thrashing include low CPU utilization, high disk I/O, long disk queues, and poor response times

- Recovery from thrashing involves reducing degree of multiprogramming by suspending or swapping out processes

- Proper memory allocation, appropriate page replacement algorithms, and workload management prevent thrashing

- Interactive processes are typically given priority to retain their working sets during memory pressure

## Common Mistakes to Avoid

- Confusing working set with physical memory allocation; working set is the pages actively used, not necessarily all pages in memory

- Assuming thrashing only affects the process causing it; thrashing is a system-wide phenomenon impacting all processes

- Setting PFF thresholds too close together causing oscillation between frame allocation and reclamation

- Ignoring that disk I/O time for page faults is orders of magnitude slower than memory access, making thrashing particularly severe

## Revision Tips

- Practice calculating working sets from reference strings with different τ values

- Review the relationship between degree of multiprogramming, CPU utilization, and thrashing

- Memorize the key differences between working set model and page fault frequency approaches

- Understand why FIFO, LRU, and other page replacement algorithms behave differently during thrashing scenarios

- Draw conceptual diagrams showing the thrashing cycle and recovery mechanisms