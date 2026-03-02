# CPU Scheduling

## Overview

CPU scheduling determines which process runs on the CPU when multiple processes are ready, maximizing CPU utilization, throughput, and fairness while minimizing turnaround time, waiting time, and response time. Scheduling can be preemptive (process can be interrupted) or non-preemptive (process runs until completion or waiting state).

## Key Points

- **Scheduling Criteria**: CPU utilization (percentage of time CPU busy), throughput (processes completed per time), turnaround time (submission to completion), waiting time (time in ready queue), response time (submission to first response)
- **Scheduler Types**: Long-term (job scheduler, controls multiprogramming degree), short-term (CPU scheduler, very fast), medium-term (swapping for time-sharing)
- **Context Switch**: Save current process state to PCB, load new process state from PCB - pure overhead
- **FCFS (First-Come-First-Served)**: Non-preemptive, simple, convoy effect (short processes wait behind long ones)
- **SJF (Shortest-Job-First)**: Optimal for minimizing average waiting time, difficult to predict burst time, can cause starvation
- **Priority Scheduling**: CPU allocated to highest priority process, can cause starvation (solved by aging)
- **Round Robin**: Time quantum (10-100ms), preemptive, performance depends on quantum size (large→FCFS, small→high overhead)
- **Preemptive vs Non-Preemptive**: Preemptive can interrupt running process, non-preemptive runs until termination or waiting

## Important Concepts

- Dispatcher gives control to selected process: switch context, switch to user mode, jump to program location
- Waiting Time = Turnaround Time - Burst Time (key formula for calculations)
- SJF provably optimal but impossible to implement without prediction
- Round Robin good for time-sharing but quantum size critical (balance response time vs context switch overhead)

## Notes

- Practice calculating metrics from Gantt charts
- Draw Gantt charts for each algorithm - essential exam skill
- Know trade-offs: FCFS simple but poor, SJF optimal but impractical, RR fair but overhead
- Preemption distinction critical for SJF and Priority scheduling
