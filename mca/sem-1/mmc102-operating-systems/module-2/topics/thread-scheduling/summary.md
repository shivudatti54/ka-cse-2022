# Thread Scheduling - Summary

## Key Definitions and Concepts

- **Thread Scheduling**: The process of determining which ready thread executes on the CPU at any given time, managing CPU allocation among competing threads

- **User-Level Threads**: Threads managed entirely by application software without kernel involvement; fast but cannot exploit multiprocessing

- **Kernel-Level Threads**: Threads managed directly by the operating system kernel; slower but can utilize multiple processors

- **Processor Affinity**: The tendency of a scheduler to keep a thread running on the same processor to maximize cache hit rates

- **Time Quantum**: The fixed time slice allocated to a thread in round robin scheduling before preemptive context switching occurs

- **Aging**: A technique where thread priority gradually increases with waiting time to prevent starvation of low-priority threads

## Important Formulas and Theorems

- **Turnaround Time** = Completion Time - Arrival Time

- **Waiting Time** = Turnaround Time - Actual CPU Burst Time

- **Average Waiting Time Formula** = Sum of individual waiting times divided by number of threads

- **Throughput** = Number of threads completed per unit time

- **CPU Utilization** = (Busy Time / Total Time) × 100%

- **SJF Optimality**: Shortest Job First scheduling provides optimal average waiting time when all threads are available at time zero

- **Rate Monotonic Feasibility**: For n periodic threads, RMS is feasible if Σ(Ci/Ti) ≤ n(2^(1/n) - 1), which approaches 0.69 as n increases

## Key Points

- Thread scheduling operates at finer granularity than process scheduling, managing execution within multi-threaded processes

- Round robin scheduling is universally used in time-sharing systems due to its fairness and interactive response characteristics

- The time quantum size critically affects RR performance—too small increases overhead, too large degrades to FCFS

- User-level threads offer faster context switching but cannot run on multiple processors; kernel-level threads provide multiprocessing benefits at higher overhead cost

- Multilevel feedback queue scheduling automatically categorizes threads by behavior, favoring interactive I/O-bound work

- In multiprocessor systems, schedulers must balance processor affinity (cache efficiency) against load balancing (even work distribution)

- Real-time scheduling algorithms like RMS use fixed priorities based on task frequency, while EDF uses dynamic priorities based on deadlines

- Priority inversion (high-priority thread waiting for low-priority thread) is a critical synchronization problem requiring priority inheritance protocols

## Common Mistakes to Avoid

1. Confusing waiting time with turnaround time—waiting time excludes actual execution time, turnaround time includes everything from arrival to completion

2. Forgetting that context switch time adds overhead to scheduling; smaller time quanta mean more switches and higher overhead percentage

3. Assuming SJF is always optimal—it is optimal only for average waiting time when all threads arrive simultaneously

4. Overlooking starvation in priority scheduling without considering aging or other starvation-prevention mechanisms

5. Misunderstanding that user-level threads cannot benefit from multiple processors since the kernel sees only the containing process

6. Neglecting the impact of thread creation time and termination handling in scheduling algorithm analysis

## Revision Tips

1. Practice numerical problems for each scheduling algorithm with different thread arrival sequences and burst times

2. Create comparison tables of all scheduling algorithms covering time complexity, advantages, disadvantages, and ideal use cases

3. Trace through round robin execution manually for various quantum sizes to understand the quantum-performance relationship

4. Review the trade-offs between processor affinity and load balancing in multi-core scheduling scenarios

5. Memorize the scheduling criteria definitions and be able to identify which criteria different algorithms optimize