# Process Scheduling - Summary

## Key Definitions and Concepts

- **Scheduler**: OS component that selects which process gets the CPU. Three types: long-term (job admission), short-term (CPU allocation), and medium-term (process swapping).
- **Ready Queue**: A data structure holding all processes waiting for CPU execution.
- **Context Switch**: Saving and restoring CPU state when switching between processes; represents pure overhead.
- **Multiprogramming**: Having multiple processes in memory to increase CPU utilization.

## Important Formulas and Theorems

- **Average Waiting Time** = Total Waiting Time / Number of Processes
- **Turnaround Time** = Completion Time - Arrival Time
- **Turnaround Time** = Waiting Time + Burst Time
- **Response Time** = First CPU Allocation Time - Arrival Time
- **SJF provides optimal average waiting time** for non-preemptive scheduling when all processes arrive simultaneously.

## Key Points

1. FCFS is simple but suffers from convoy effect—long processes delay short ones.
2. SJF minimizes average waiting time but requires advance knowledge of burst times.
3. Round Robin is ideal for time-sharing with a properly chosen time quantum (10-100ms).
4. Priority scheduling can cause starvation—low-priority processes may never execute.
5. Preemptive algorithms allow process interruption; non-preemptive do not.
6. Time quantum too small causes excessive context switches; too large degrades to FCFS.
7. Multilevel feedback queue automatically distinguishes CPU-bound and I/O-bound processes.
8. Processor affinity improves performance by utilizing cached data on the same processor.
9. Load balancing ensures even work distribution across multiple processors.

## Common Mistakes to Avoid

1. Confusing turnaround time with waiting time—turnaround includes execution time.
2. Forgetting that context switching is overhead, not useful work.
3. Assuming SJF is always optimal—it only works when arrival times are identical.
4. Selecting inappropriate time quantum for Round Robin in exam questions.
5. Confusing starvation (gradual denial) with deadlock (circular waiting).

## Revision Tips

1. Practice numerical problems for each algorithm type—examiners frequently ask for calculations.
2. Create a comparison table of all algorithms with pros, cons, and suitable scenarios.
3. Remember the convoy effect example for FCFS and starvation example for priority scheduling.
4. Focus on understanding the trade-offs rather than memorizing—application-based questions are common.
5. Review previous year DU question papers to understand the exam pattern and frequently asked concepts.