# Thread Scheduling - Summary

## Key Definitions and Concepts

- THREAD SCHEDULING: The process of determining which thread gets CPU time and for how long, operating at a finer granularity than process scheduling.
- THREAD STATES: Ready (waiting for CPU), Running (actively executing), Blocked (waiting for I/O or resources).
- SCHEDULING CRITERIA: CPU utilization (percentage busy), Throughput (threads completed per unit), Turnaround time (creation to completion), Waiting time (time in ready queue), Response time (first CPU allocation).
- PROCESS CONTENTION SCOPE (PCS): Scheduling among threads within the same process sharing process resources.
- SYSTEM CONTENTION SCOPE (SCS): System-wide scheduling among all threads, managed by the kernel.

## Important Formulas and Theorems

- Average Waiting Time = Sum of (Completion Time - Arrival Time - Burst Time) / Number of Threads
- Average Turnaround Time = Sum of (Completion Time - Arrival Time) / Number of Threads
- Context Switch Overhead in RR = (Context Switch Time / Time Quantum) × 100%
- SJF is OPTIMAL for minimum average waiting time when burst times are known in advance.
- Turnaround time = Waiting time + Burst time

## Key Points

1. Thread scheduling is more efficient than process scheduling due to shared address space and faster context switches.
2. ROUND ROBIN provides the best response time for interactive systems but performance depends heavily on time quantum selection.
3. FCFS suffers from the convoy effect where short threads wait behind long threads.
4. PRIORITY scheduling can cause starvation for low-priority threads; aging is the solution.
5. SJF minimizes average waiting time but cannot predict burst times in practice.
6. Preemptive scheduling allows thread preemption during execution; non-preemptive runs threads to completion.
7. Modern OS use multilevel feedback queues combining advantages of multiple algorithms.
8. Linux CFS ensures fair CPU distribution using virtual runtime tracking.
9. Windows uses 32-level priority scheduling combining real-time and variable priorities.

## Common Mistakes to Avoid

- Confusing turnaround time with waiting time: Turnaround includes execution time, waiting time does not.
- Forgetting that SJF requires knowledge of burst times which is impractical in real systems.
- Assuming FCFS always performs poorly: It performs well when burst times are similar.
- Overlooking context switch overhead in Round Robin calculations.
- Mixing up Process Contention Scope and System Contention Scope in multi-threaded models.

## Revision Tips

1. Practice numerical problems for each algorithm: Draw timeline diagrams to visualize thread execution sequence.
2. Create comparison tables for all algorithms listing advantages, disadvantages, and suitable applications.
3. Memorize the formula relationships: Turnaround = Waiting + Burst.
4. Understand why modern OS use hybrid approaches rather than pure algorithms.
5. Review thread scheduling in context of multi-core processors where thread affinity becomes relevant.
6. Solve previous year DU examination questions on process and thread scheduling.