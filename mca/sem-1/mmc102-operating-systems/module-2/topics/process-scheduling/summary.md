# Process Scheduling - Summary

## Key Definitions and Concepts

Process scheduling is the operating system mechanism that determines which process executes on the CPU at any given time. The ready queue holds all processes waiting for CPU allocation, while device queues hold processes waiting for I/O operations. A context switch occurs when the CPU switches from executing one process to another, saving and restoring process state.

## Important Formulas and Theorems

Average Waiting Time = Total Waiting Time / Number of Processes

Turnaround Time = Completion Time - Arrival Time

Turnaround Time = Waiting Time + Burst Time (Execution Time)

For Round Robin: Number of CPU visits = ceil(Burst Time / Quantum)

SJF with exponential averaging: τ(n+1) = α × t(n) + (1-α) × τ(n), where τ is estimated burst, t is actual burst, and α is the weighting factor (typically 0.5)

## Key Points

- Long-term scheduler controls multiprogramming degree; short-term scheduler selects the next process to run; medium-term scheduler handles swapping

- FCFS is simple but suffers from convoy effect; average waiting time is poor with varying burst times

- SJF provides optimal average waiting time but requires knowledge of burst times; prediction uses exponential averaging

- Round Robin is ideal for time-sharing with quantum typically 10-100 milliseconds; too small quantum causes excessive overhead

- Priority scheduling can cause starvation; aging progressively increases priority of waiting processes

- Multilevel feedback queues dynamically adjust process priorities based on behavior, combining advantages of multiple algorithms

- No single algorithm optimizes all criteria simultaneously; system requirements determine algorithm choice

## Common Mistakes to Avoid

Confusing long-term and short-term scheduler functions is a frequent error; remember that long-term controls job admission while short-term makes actual CPU allocation decisions. In preemptive SJF (SRTF), always check if newly arriving processes have shorter remaining time than the current running process.

For Round Robin problems, many students forget that the first process starts at time zero and incorrectly calculate waiting time. Ensure you account for the fact that a process arriving at time zero begins immediately without waiting.

Ignoring arrival times when calculating waiting time leads to incorrect answers. Waiting time only counts time spent in the ready queue, not time spent in other queues or before system entry.

## Revision Tips

Practice numerical problems by drawing Gantt charts for all scheduling algorithms; visualization clarifies the execution sequence and helps identify context switch points. Memorize the key characteristics of each algorithm: FCFS (no preemption, FIFO), SJF (optimal waiting, requires burst prediction), RR (time quantum based, preemptive), Priority (priority-based, starvation possible).

Focus on understanding when each algorithm is appropriate: FCFS for batch systems, RR for time-sharing, SJF for minimizing waiting in controlled environments. Remember the aging technique as the solution to starvation in priority scheduling.