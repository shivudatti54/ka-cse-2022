# Process Scheduling - Summary

## Key Definitions and Concepts

- **Process Scheduling**: The OS function that determines which process runs on the CPU at any given time, managing the ready queue to allocate CPU resources among competing processes.

- **CPU Utilization**: The percentage of time the CPU is productively executing processes; higher utilization indicates better resource usage.

- **Throughput**: Number of processes completed per unit time; measures system efficiency.

- **Turnaround Time**: Total time from process arrival to completion = Waiting time + Burst time + I/O time.

- **Waiting Time**: Total time a process spends in the ready queue waiting for CPU allocation; the key metric for scheduling algorithm performance.

- **Response Time**: Time from process arrival to first CPU execution; critical for interactive systems.

- **Time Quantum**: The fixed time slice allocated to each process in Round Robin scheduling, typically 10-100 milliseconds.

## Important Formulas and Theorems

- **Average Waiting Time (AWT)**: Sum of waiting times of all processes divided by number of processes.

- **Turnaround Time**: Completion time - Arrival time.

- ** SJF Optimality**: Non-preemptive SJF provides minimum average waiting time among all scheduling algorithms when all processes are available at time zero.

- **RR Performance**: As quantum size increases, RR approaches FCFS; as quantum approaches zero, RR becomes processor-sharing but with infinite context switching.

## Key Points

- FCFS is simple but suffers from convoy effect; good for long CPU-bound processes but terrible for interactive tasks.

- SJF minimizes average waiting time but requires advance knowledge of burst times, which is solved by using exponential averaging for prediction.

- Priority scheduling can cause starvation; aging solves this by gradually increasing priority of waiting processes.

- Round Robin is ideal for time-sharing systems, providing good response time with fairness through time slicing.

- Multilevel Feedback Queue combines multiple scheduling algorithms through dynamic process migration between queues.

- Preemptive scheduling (SRTF, preemptive priority, RR) allows processes to be interrupted for better response to new arrivals.

- Context switching has overhead; too many switches waste CPU time on kernel operations rather than user processes.

## Common Mistakes to Avoid

1. Confusing turnaround time with waiting time—turnaround includes both waiting and execution time.

2. Forgetting that SJF can be either preemptive (SRTF) or non-preemptive; the algorithm behavior differs significantly.

3. In Round Robin, not moving processes to queue end after their quantum expires—this is essential for algorithm correctness.

4. Assuming smaller quantum always improves performance—too small increases context switch overhead dramatically.

5. Ignoring arrival times when calculating waiting time—processes that arrive later should not be charged waiting time before their arrival.

## Revision Tips

1. Practice at least 3-5 numerical problems from each algorithm type before the exam.

2. Draw Gantt charts for all scheduling problems—they help visualize execution order and calculate times accurately.

3. Create a comparison table of all algorithms listing CPU utilization, throughput, waiting time, response time, and problems like starvation or convoy effect.

4. Memorize that SJF gives optimal average waiting time but FCFS is easiest to implement; RR balances fairness and responsiveness.

5. Remember that no single scheduling algorithm is best for all scenarios—the choice depends on whether the system is batch, interactive, or real-time.