# Scheduling Algorithms - Summary

## Key Definitions

- **CPU Scheduling**: The process of deciding which process in the ready queue should be allocated the CPU next.
- **Dispatcher**: The module that gives control of the CPU to the process selected by the short-term scheduler.
- **Context Switch**: The process of saving and restoring the state of a CPU when switching between processes.
- **Time Quantum**: The fixed time slice allocated to a process in Round Robin scheduling.
- **Aging**: A technique to gradually increase the priority of processes that wait too long to prevent starvation.

## Important Formulas

- **Turnaround Time** = Completion Time - Arrival Time
- **Waiting Time** = Turnaround Time - Burst Time
- **Throughput** = Number of Processes Completed / Total Time
- **Average Waiting Time (FCFS)**: Can be calculated from Gantt chart by summing idle periods before each process starts
- **Average Waiting Time (SJF)**: Optimal when all processes arrive at time 0; formula applies to sorted burst times

## Key Points

1. FCFS is simple but suffers from the convoy effect where short processes wait behind long ones.

2. SJF provides optimal average waiting time but requires advance knowledge of burst times, which is impractical.

3. Round Robin is ideal for time-sharing systems as it ensures fair CPU allocation with time slicing.

4. The choice of time quantum in RR is critical—too small increases overhead, too large degrades to FCFS.

5. Priority scheduling can lead to starvation, which aging helps mitigate by gradually increasing process priorities.

6. Multilevel Feedback Queue combines advantages of multiple algorithms by allowing process migration between queues.

7. Preemptive algorithms like preemptive SJF and RR can cause starvation for longer processes but provide better response time.

8. No single scheduling algorithm is optimal for all scenarios—selection depends on system requirements.

## Common Mistakes

1. **Confusing turnaround time with waiting time**— remember turnaround includes both waiting and execution time.

2. **Forgetting arrival times** when calculating SJF— the algorithm must consider only available processes at each scheduling decision point.

3. **Incorrect time quantum behavior**— many students assume RR always performs worse than SJF in all metrics.

4. **Ignoring context switch overhead** when comparing theoretical algorithms— preemptive algorithms have more context switches.

5. **Not considering whether the algorithm is preemptive or non-preemptive**— this fundamentally changes the scheduling decisions when new processes arrive.