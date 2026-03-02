# Scheduling Algorithms - Summary

## Key Definitions and Concepts

CPU Scheduling: The operating system function that determines which process gets the CPU when multiple processes are ready to execute.

CPU Burst: The period of time a process executes on the CPU before waiting for I/O or being preempted.

Waiting Time: Total time a process spends in the ready queue waiting for CPU allocation.

Turnaround Time: Time from process arrival to completion, equal to completion time minus arrival time.

Response Time: Time from process arrival to first CPU allocation.

Throughput: Number of processes completed per unit time.

Dispatcher: OS component that transfers CPU control to processes selected by the scheduler, performing context switches.

## Important Formulas and Theorems

Turnaround Time = Completion Time - Arrival Time

Waiting Time = Turnaround Time - Actual CPU Burst Time

Average Waiting Time = Total Waiting Time / Number of Processes

Average Turnaround Time = Total Turnaround Time / Number of Processes

SJF provides optimal average waiting time for a given set of processes (theoretically optimal but practically impossible to implement).

## Key Points

FCFS (First-Come-First-Served) is simple but can result in poor average waiting time and the convoy effect where short processes wait behind long ones.

SJF (Shortest Job First) minimizes average waiting time but requires advance knowledge of CPU burst times and can cause starvation for long processes.

Round Robin provides fair scheduling with no starvation by giving each process a fixed time quantum; performance depends heavily on time quantum size.

Priority Scheduling assigns priority numbers to processes and executes highest priority first, but can lead to starvation which aging helps mitigate.

Preemptive algorithms like RR and preemptive SJF allow process preemption, while non-preemptive algorithms like FCFS and non-preemptive SJF do not.

Multilevel Queue Scheduling partitions processes into different queues based on characteristics, each with its own scheduling algorithm.

Multilevel Feedback Queue Scheduling allows processes to move between queues, combining advantages of multiple algorithms through flexible queue management.

## Common Mistakes to Avoid

Confusing waiting time with turnaround time—waiting time only counts time in ready queue, while turnaround includes actual CPU execution time.

Forgetting to account for arrival times when calculating waiting times; only processes in the ready queue at a given time can be scheduled.

Assuming SJF can be directly implemented in practice without considering how CPU burst times are predicted in real systems.

Ignoring context switching overhead in theoretical calculations, especially in Round Robin with small time quantums.

## Revision Tips

Practice numerical problems for each algorithm type, drawing Gantt charts to visualize process execution and verify calculations.

Create comparison tables listing algorithm characteristics including type (preemptive/non-preemptive), average waiting time, starvation potential, and implementation complexity.

Focus on understanding why certain algorithms perform better under specific conditions rather than just memorizing formulas.

Review the relationship between time quantum and system performance in Round Robin scheduling as this is frequently examined.