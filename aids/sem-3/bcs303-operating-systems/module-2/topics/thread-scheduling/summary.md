# Thread Scheduling - Summary

## Key Definitions

- **Thread Scheduling**: The process of allocating CPU time to threads, determining which thread runs at any given time.
- **User-Level Threads**: Threads managed entirely by a thread library in user space without kernel awareness.
- **Kernel-Level Threads**: Threads managed directly by the operating system kernel.
- **Time Quantum**: The fixed time slice allocated to each thread in Round Robin scheduling.
- **Thread Affinity**: The ability to bind a thread to a specific CPU core to maintain cache locality.
- **Starvation**: A condition where a thread perpetually waits for CPU time due to being continuously bypassed by higher-priority threads.
- **Convoy Effect**: A phenomenon where short threads wait behind long CPU-bound threads, degrading performance.

## Important Formulas

- **Average Turnaround Time** = (Sum of completion times - arrival times) / Number of threads
- **Average Waiting Time** = (Sum of turnaround times - Sum of burst times) / Number of threads
- **RMS Feasibility Condition**: U ≤ n(2^(1/n) - 1), where U is total utilization and n is number of threads

## Key Points

1. Thread scheduling operates at finer granularity than process scheduling, enabling better CPU utilization in multithreaded applications.

2. User-level threads offer fast context switching but suffer from blocking issues; kernel-level threads provide better preemptive scheduling but with higher overhead.

3. Round Robin scheduling provides fairness and good response time, with the time quantum being a critical parameter affecting performance.

4. Multilevel Feedback Queue is the most sophisticated algorithm as it dynamically adjusts thread priorities based on observed behavior.

5. Priority scheduling can lead to starvation, which is typically mitigated through aging mechanisms that gradually increase the priority of waiting threads.

6. In modern multi-core systems, thread affinity scheduling considers cache locality and NUMA topology for optimal performance.

7. Real-time scheduling requires deterministic behavior; RMS uses fixed priorities based on periods, while EDF uses dynamic priorities based on deadlines.

## Common Mistakes

1. **Confusing thread scheduling with process scheduling**: Remember that threads within the same process share many resources, making thread context switches faster than process switches.

2. **Ignoring the impact of time quantum in Round Robin**: Selecting an inappropriate quantum (too small or too large) can severely degrade system performance.

3. **Misunderstanding starvation**: Starvation is not the same as deadlock—a starved thread could eventually run if priorities change, whereas a deadlocked thread waits indefinitely.

4. **Forgetting about kernel involvement**: Even with user-level threads, the kernel ultimately controls CPU allocation and can preempt the entire process.

5. **Overlooking cache effects**: In multi-core systems, poorly designed thread scheduling can cause excessive cache misses, negating the benefits of multithreading.