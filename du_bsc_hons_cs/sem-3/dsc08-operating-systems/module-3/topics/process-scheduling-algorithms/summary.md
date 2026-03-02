# Process Scheduling Algorithms - Summary

## Key Definitions and Concepts

- **CPU Scheduler**: Selects which process from the ready queue gets the CPU
- **Dispatcher**: Gives control of CPU to the selected process (involves context switch)
- **Context Switching**: Saving and restoring CPU state when switching between processes
- **Preemptive Scheduling**: OS can forcibly remove CPU from running process
- **Non-Preemptive Scheduling**: Once CPU assigned, process keeps it until termination/waiting
- **Time Quantum**: Fixed time slice in Round Robin scheduling
- **Aging**: Technique to prevent starvation by gradually increasing priority of waiting processes

## Important Formulas and Theorems

- **Turnaround Time** = Completion Time - Arrival Time
- **Waiting Time** = Turnaround Time - Burst Time
- **Average Waiting Time** = Sum of all waiting times / Number of processes
- **Average Turnaround Time** = Sum of all turnaround times / Number of processes
- **SJF Theorem**: Non-preemptive SJF provides optimal minimum average waiting time (when burst times are known)

## Key Points

1. FCFS is simple but suffers from convoy effect (short processes wait behind long ones)

2. SJF minimizes average waiting time but can cause starvation of long processes

3. Round Robin is ideal for time-sharing systems with good response time

4. Priority scheduling can lead to starvation; aging prevents this

5. Preemptive algorithms cause more context switches (overhead) than non-preemptive

6. Multilevel Feedback Queue is most flexible—it adapts to process behavior

7. For same arrival time, SJF and FCFS give same results; for different arrival times, SJF is better

8. Time quantum too large → RR becomes FCFS; too small → excessive context switching

9. Response time is critical for interactive systems; throughput matters for batch systems

10. No single algorithm is best for all scenarios—choice depends on system requirements

## Common Mistakes to Avoid

1. **Forgetting arrival time**: Many students calculate turnaround time as just burst time, ignoring arrival time
2. **Not drawing Gantt chart**: Attempting to solve scheduling problems without visual representation leads to errors
3. **Confusing preemptive and non-preemptive**: Preemptive SJF is Shortest Remaining Time First (SRTF), not the same as non-preemptive SJF
4. **Ignoring context switch time**: In some exam questions, context switch time must be accounted for
5. **Wrong completion time calculation**: Always trace through timeline carefully; completion time is when process finishes completely

## Revision Tips

1. Practice at least 5 numerical problems covering all algorithms before the exam

2. Create a comparison table of all algorithms with their advantages, disadvantages, and suitable use cases

3. Remember: Waiting Time = Turnaround Time - Burst Time is the most important formula

4. For quick revision, focus on FCFS, SJF (both types), Priority, and Round Robin—these cover 80% of exam questions

5. Understand the concept of "optimal" in context—SJF is optimal for average waiting time, not for every metric