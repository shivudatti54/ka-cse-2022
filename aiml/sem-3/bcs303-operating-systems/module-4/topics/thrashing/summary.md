# Thrashing - Summary

## Key Definitions
- **Thrashing**: A severe degradation in system performance caused by excessive paging activity, where the CPU spends more time servicing page faults than executing user processes.
- **Working Set**: The set of pages actively used by a process during a specific time interval (t - τ, t), where τ is the working set window.
- **Working Set Size (WSS)**: The number of frames required by a process to minimize page faults within its working set window.
- **Page Fault Frequency (PFF)**: The rate at which a process experiences page faults, used as a metric for memory allocation decisions.

## Important Formulas
- **Total Working Set Demand**: Σ(WSSi) for all active processes i
- **Thrashing Condition**: Total Working Set Demand > Available Physical Memory Frames
- **Optimal Degree of Multiprogramming**: Point of maximum CPU utilization on the multiprogramming curve

## Key Points
1. Thrashing occurs when processes lack sufficient frames, leading to constant page evictions and faults.
2. The CPU utilization vs. degree of multiprogramming curve shows an optimal point beyond which thrashing reduces performance.
3. The working set model uses historical page reference patterns to determine memory requirements.
4. Page fault frequency control dynamically adjusts frame allocation based on observed fault rates.
5. Upper and lower thresholds for PFF guide allocation decisions: increase frames when above upper threshold, reclaim when below lower threshold.
6. Symptoms of thrashing include high disk I/O activity, low CPU utilization, and long disk queues.
7. Recovery strategies include reducing multiprogramming degree, swapping out processes, and adaptive memory management.
8. Modern OSes implement automatic thrashing control through continuous performance monitoring.

## Common Mistakes
1. Confusing thrashing with normal paging—thrashing involves constant page faults that prevent meaningful execution.
2. Assuming adding more memory always eliminates thrashing—if working set demand consistently exceeds physical memory, thrashing persists.
3. Misunderstanding that thrashing affects only the thrashing process—it impacts the entire system due to shared disk resources.
4. Overlooking that proper working set window selection is critical; too small windows cause excessive memory allocation, too large windows increase thrashing risk.