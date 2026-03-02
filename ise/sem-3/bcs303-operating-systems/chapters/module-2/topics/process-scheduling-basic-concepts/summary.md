# Process Scheduling Basic Concepts - Summary

## Key Definitions and Concepts

Process scheduling is the OS mechanism that determines the order in which processes access the CPU. The three scheduler types are: long-term scheduler (controls degree of multiprogramming), short-term scheduler (selects ready process for CPU), and medium-term scheduler (handles process swapping).

## Important Formulas and Techniques

Average Waiting Time = Sum of waiting times for all processes divided by number of processes. Turnaround Time = Burst Time + Waiting Time. Throughput = Number of processes completed per unit time. CPU Utilization = (Busy Time / Total Time) × 100.

## Key Points

- FCFS is simple but can cause the convoy effect where short processes wait behind long ones.

- Shortest Job First provides optimal average waiting time when all processes are available simultaneously.

- Round Robin uses time quantum and is ideal for time-sharing systems with fair CPU distribution.

- Priority scheduling can lead to starvation of low-priority processes; aging can prevent this.

- Thread scheduling provides finer granularity than process scheduling in modern systems.

- Multiple-processor scheduling faces challenges of processor affinity, load balancing, and cache coherence.

## Common Mistakes to Avoid

Confusing turnaround time with waiting time—turnaround includes execution time. Forgetting that SJF requires knowledge of burst times in advance. Using FCFS calculation methods for RR or vice versa. Neglecting context switch overhead in Round Robin performance analysis.

## Revision Tips

Practice numerical problems for all four major algorithms until you can solve them quickly. Draw Gantt charts to visualize process execution order and verify your calculations. Memorize which algorithm optimizes which criterion—this helps in selection-based questions.