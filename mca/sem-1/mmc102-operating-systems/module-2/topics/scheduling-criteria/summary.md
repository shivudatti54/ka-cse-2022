# Scheduling Criteria - Summary

## Key Definitions and Concepts

- **CPU Utilization**: Percentage of time the CPU is busy executing processes; typically measured as (Busy Time / Total Time) × 100%

- **Throughput**: Number of processes completed per unit time; higher throughput indicates better system productivity

- **Turnaround Time**: Total time from process arrival to completion; includes waiting time plus execution time

- **Waiting Time**: Total time a process spends in the ready queue awaiting CPU allocation; excludes actual execution time

- **Response Time**: Time from process arrival to the start of its first CPU execution; critical for interactive systems

- **Fairness**: Ensures all processes receive CPU time without indefinite postponement or starvation

- **Priority**: Numerical ordering of processes for CPU allocation; can cause starvation of lower-priority processes

## Important Formulas and Theorems

- Turnaround Time = Completion Time - Arrival Time
- Waiting Time = Turnaround Time - Burst Time
- Response Time = First CPU Start Time - Arrival Time
- CPU Utilization = (Busy Time / Total Time) × 100%
- Throughput = Number of Completed Processes / Time Unit
- Average Metric = Sum of Individual Values / Number of Processes

## Key Points

- NO SINGLE ALGORITHM OPTIMIZES ALL CRITERIA simultaneously; trade-offs are inevitable

- FCFS maximizes CPU utilization but performs poorly on waiting time and turnaround time

- SJF minimizes average waiting time and turnaround time but cannot be practically implemented perfectly

- Round-Robin provides good response time and fairness but increases context switch overhead with small quanta

- Response time is THE MOST CRITICAL criterion for interactive and real-time systems

- Priority scheduling can cause starvation, solved through aging (increasing priority over waiting time)

- CPU utilization near 100% is achievable but may result in poor response times for interactive users

- Throughput and turnaround time are inversely related to average service time

## Common Mistakes to Avoid

- CONFUSING WAITING TIME WITH TURNAROUND TIME; waiting time excludes actual CPU execution

- FORGETTING THAT CONTEXT SWITCH OVERHEAD affects effective CPU utilization in time-slice algorithms

- ASSUMING SJF IS ALWAYS OPTIMAL; it only optimizes average waiting/turnaround time, not response time or fairness

- IGNORING ARRIVAL TIMES when calculating scheduling metrics; arrival time affects all criteria

- MISUNDERSTANDING PREEMPTION; preemptive algorithms provide better response time guarantees

## Revision Tips

- PRACTICE CALCULATING all metrics from given process tables until calculations become automatic

- MEMORIZE which algorithms excel at which criteria: SJF (waiting/turnaround), RR (response/fairness), FCFS (utilization)

- UNDERSTAND THE TRADE-OFFS in depth—know WHY optimizing one criterion hurts others in specific scenarios

- REVIEW PREVIOUS EXAM QUESTIONS on scheduling to understand the problem patterns and expected answer formats