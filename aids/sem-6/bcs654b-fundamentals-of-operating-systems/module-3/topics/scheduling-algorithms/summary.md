# CPU Scheduling Algorithms - Summary

## Key Definitions and Concepts

- **CPU Scheduling**: OS mechanism to select which ready process gets CPU time
- **Preemptive Scheduling**: Allows interrupting running processes (e.g., Round Robin)
- **Non-preemptive Scheduling**: Process runs until completion (e.g., FCFS)
- **Turnaround Time**: `Completion Time - Arrival Time`
- **Waiting Time**: `Turnaround Time - Burst Time`
- **Response Time**: Time from request submission to first response
- **Throughput**: # of processes completed per time unit
- **Starvation**: Indefinite blocking of low-priority processes

## Important Formulas and Theorems

```plaintext
1. Turnaround Time (TAT) = Completion Time - Arrival Time
2. Waiting Time (WT) = TAT - Burst Time
3. Average TAT = (Σ TAT)/n
4. Average WT = (Σ WT)/n
5. Response Time (RR) = Time of first CPU allocation - Arrival Time
```

## Key Points

- FCFS: Simple but causes convoy effect (long processes delay short ones)
- SJF: Optimal for minimum waiting time but requires burst time knowledge
- Priority Scheduling: Risk of starvation for low-priority processes
- Round Robin: Preemptive with time quantum, fair but high context switching
- Multilevel Queue: Separates processes into priority classes
- Preemptive vs Non-preemptive: Key differentiator for algorithm behavior
- Evaluation Metrics: Focus on CPU utilization, throughput, and fairness
- Real-world Use: RR in time-sharing, SJF in batch processing

## Common Mistakes to Avoid

1. Confusing preemptive SJF (SRTF) with non-preemptive SJF
2. Forgetting arrival times when calculating waiting/turnaround times
3. Applying RR time quantum to entire process instead of per CPU burst
4. Assuming all scheduling algorithms prevent starvation (Priority can cause it)

## Revision Tips

1. Practice numerical problems using different algorithms (especially SJF and RR)
2. Create comparison tables for algorithms (preemption, avg WT, use cases)
3. Use Gantt charts to visualize process execution sequences
4. Memorize formulas using mnemonics: "TAT = CAT - AAT" (Completion - Arrival)
