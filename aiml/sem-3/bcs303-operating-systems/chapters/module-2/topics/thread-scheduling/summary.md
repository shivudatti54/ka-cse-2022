# Thread Scheduling - Summary

## Key Definitions and Concepts

- **Thread Scheduling**: The OS mechanism that determines which thread gets CPU time when multiple threads compete for execution resources.
- **Process Contention Scope (PCS)**: Scheduling where threads compete only with other threads in the same process.
- **System Contention Scope (SCS)**: Scheduling where all system threads compete regardless of process boundaries.
- **Time Quantum**: The fixed time slice allocated to each thread in Round Robin scheduling.
- **Starvation**: A condition where low-priority threads wait indefinitely due to continuous arrival of higher-priority threads.
- **Aging**: A technique where thread priority gradually increases based on waiting time to prevent starvation.
- **Processor Affinity**: The tendency of a thread to prefer execution on the same processor to optimize cache performance.

## Important Formulas and Theorems

- **Average Waiting Time**: (Sum of waiting times for all threads) / (Number of threads)
- **Turnaround Time**: Completion time - Arrival time = Waiting time + Burst time
- **Response Time**: First CPU allocation time - Arrival time
- **Rate Monotonic Utilization Bound**: For n tasks, feasibility is guaranteed if CPU utilization ≤ n(2^(1/n) - 1), approximately 69% for large n

## Key Points

1. Thread scheduling operates at finer granularity than process scheduling, with threads within a process sharing memory and resources.

2. The five scheduling criteria are: CPU utilization, throughput, turnaround time, waiting time, and response time—each prioritized differently based on system type.

3. FCFS is simple but can cause poor average waiting times due to convoy effect; SJF is optimal for average waiting time but requires advance knowledge of execution times.

4. Round Robin provides fairness through time-slicing but performance depends critically on time quantum selection—too small increases overhead, too large degrades to FCFS.

5. Priority scheduling can cause starvation of low-priority threads, addressed through aging mechanisms that gradually increase waiting thread priorities.

6. Real-time scheduling requires deterministic behavior: RMS uses fixed priorities based on task rate, EDF uses dynamic deadlines and achieves better utilization.

7. Multi-processor scheduling introduces complexity with processor affinity (cache benefits), load balancing (work distribution), and cache coherency considerations.

8. Multilevel Feedback Queue combines multiple queues with dynamic priority adjustment based on thread behavior, adapting to both interactive and CPU-intensive work.

## Common Mistakes to Avoid

1. Confusing thread scheduling with process scheduling—remember threads are lighter-weight entities within processes.

2. Forgetting that SJF requires advance knowledge of burst times, which is often impractical in real systems.

3. Not considering the overhead of context switching when evaluating scheduling algorithm efficiency.

4. Ignoring the relationship between time quantum size and context switch overhead in Round Robin.

5. Overlooking that priority inversion can occur in priority scheduling when high-priority threads wait for low-priority threads holding shared resources.

## Revision Tips

1. Practice numerical problems: Calculate waiting times and turnaround times for all algorithms with different arrival orders and burst times.

2. Create comparison tables: List each algorithm with its advantages, disadvantages, and best-use scenarios.

3. Remember real-world associations: Interactive systems prioritize response time, batch systems prioritize throughput, real-time systems require deterministic behavior.

4. Understand the "why" behind each algorithm's design—knowing the problem each algorithm solves helps in selection during exams.