# Scheduling Criteria - Summary

## Key Definitions and Concepts

- **CPU Scheduling Criteria**: Metrics used to evaluate and compare CPU scheduling algorithms
- **CPU Utilization**: Percentage of time the CPU is busy executing processes (target: 40-90% for general systems)
- **Throughput**: Number of processes completed per unit time (higher is better)
- **Turnaround Time**: Total time from process arrival to completion (lower is better)
- **Waiting Time**: Total time process spends in ready queue (lower is better)
- **Response Time**: Time from request to first CPU response (critical for interactive systems)

## Important Formulas

- CPU Utilization = (Busy Time / Total Time) × 100%
- Throughput = Number of Processes Completed / Time Unit
- Turnaround Time = Completion Time - Arrival Time
- Waiting Time = Turnaround Time - Burst Time - I/O Time
- Response Time = First CPU Allocation Time - Arrival Time

## Key Points

1. Five primary scheduling criteria: CPU utilization, throughput, turnaround time, waiting time, and response time

2. Different computing environments prioritize different criteria (batch systems care about throughput, interactive systems care about response time)

3. SJF minimizes average waiting time but requires advance knowledge of burst times and may cause starvation

4. Round Robin provides good response time but overhead increases with smaller time quantum

5. No scheduling algorithm optimizes all criteria simultaneously - trade-offs are inevitable

6. Fairness ensures no process starves; aging mechanisms gradually increase priority of waiting processes

7. Preemptive scheduling better minimizes response time but adds system complexity

8. Priority scheduling can lead to starvation of low-priority processes

9. Turnaround time includes waiting time plus actual execution time plus I/O time

10. Response time is most critical for interactive and real-time systems

## Common Mistakes to Avoid

1. Confusing waiting time with turnaround time - waiting time excludes execution and I/O time

2. Assuming higher throughput always means better performance - must consider other criteria

3. Thinking one scheduling algorithm is universally best - context matters

4. Ignoring context switching overhead when evaluating scheduling algorithms

5. Forgetting that response time is measured to first CPU allocation, not completion

## Revision Tips

1. Practice numerical calculations with different process combinations

2. Create a comparison table showing how each algorithm affects each criterion

3. Memorize formulas and practice applying them to exam-style questions

4. Understand real-world examples: web servers prioritize response time, batch systems prioritize throughput

5. Review the relationship between time quantum in Round Robin and system performance metrics