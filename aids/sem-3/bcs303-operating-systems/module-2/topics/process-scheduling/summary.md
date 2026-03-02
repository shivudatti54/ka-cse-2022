# Process Scheduling - Summary

## Key Definitions

- **Process Scheduling:** The OS function that decides which process gets the CPU, for how long, and in what order when multiple processes compete for CPU resources.

- **Scheduler:** The component of the operating system that selects the next process to receive CPU time. Three types exist: long-term, short-term, and medium-term.

- **Context Switch:** The process of saving the state of one process and loading the state of another, enabling the CPU to switch between processes.

- **Dispatcher:** The module that gives control of the CPU to the process selected by the CPU scheduler, performing context switch, mode switch, and control transfer.

- **Multiprogramming:** The technique of keeping multiple processes in memory simultaneously, allowing CPU to work on one process while another waits for I/O.

- **Starvation:** A condition where a process never gets CPU time because other processes continually receive priority, typically in priority scheduling.

## Important Formulas

- **Turnaround Time** = Completion Time - Arrival Time

- **Waiting Time** = Turnaround Time - Burst Time

- **Response Time** = First Response Time - Arrival Time

- **CPU Utilization** = (Busy Time / Total Time) × 100%

- **Throughput** = Number of Processes Completed / Unit Time

## Key Points

1. Process scheduling is essential for maximizing CPU utilization and system throughput in multiprogrammed systems.

2. The short-term scheduler (CPU scheduler) operates most frequently and must be extremely fast, typically running every few milliseconds.

3. Long-term scheduler controls the degree of multiprogramming by admitting processes to the ready queue, balancing I/O-bound and CPU-bound processes.

4. Preemptive scheduling allows the OS to forcibly take CPU away from running processes, enabling better responsiveness for interactive systems.

5. FCFS is simple but can cause the "convoy effect" where short processes wait behind long ones; SJF minimizes average waiting time but may cause starvation.

6. Round Robin provides good response time and fairness but performance heavily depends on the time quantum chosen.

7. Context switch time is pure overhead and varies from 1 to 1000 microseconds depending on hardware and OS design.

8. Priority scheduling can lead to starvation; aging (increasing priority over time) is used to combat this problem.

9. No single scheduling algorithm is optimal for all scenarios; the choice depends on system type (batch, interactive, real-time) and workload characteristics.

10. The dispatcher latency—the time to stop one process and start another—is a critical performance metric affecting system responsiveness.

## Common Mistakes

1. **Confusing turnaround time with waiting time:** Turnaround time includes both waiting time and execution time, while waiting time is only the time spent in the ready queue.

2. **Incorrectly calculating completion time:** Students often forget to add the current time to the burst time when determining when a process finishes.

3. **Forgetting arrival time in calculations:** Many problems assume all processes arrive at time 0, but when arrival times differ, timing calculations must account for process availability.

4. **Assuming preemptive SJF works the same as non-preemptive:** In preemptive SJF (Shortest Remaining Time First), a newly arrived process with shorter burst can preempt the currently running process.