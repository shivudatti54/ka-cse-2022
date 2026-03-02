# CPU Scheduling Criteria - Summary

## Key Definitions and Concepts

- **CPU Utilization**: Percentage of time the CPU is actively executing processes; aim for high utilization (40-90% in practice).
- **Throughput**: Number of processes completed per unit time; higher throughput indicates greater system productivity.
- **Turnaround Time**: Total time from process arrival to completion; includes waiting time plus execution time.
- **Waiting Time**: Time spent in ready queue before CPU allocation; excludes actual execution and I/O time.
- **Response Time**: Time from process arrival to first CPU allocation; critical for interactive systems.

## Important Formulas and Theorems

- Turnaround Time = Completion Time - Arrival Time
- Waiting Time = Turnaround Time - Burst Time
- Response Time = First CPU Execution Time - Arrival Time
- Throughput = Completed Processes / Time Unit

## Key Points

1. These five criteria form the basis for evaluating and comparing all CPU scheduling algorithms.

2. FCFS typically results in higher average waiting time, especially when short processes wait behind long ones.

3. SJF (Shortest Job First) minimizes average waiting time and turnaround time but may cause starvation.

4. Round Robin provides good response time for interactive systems by limiting maximum waiting time to one time quantum.

5. No single scheduling algorithm optimizes all five criteria simultaneously; trade-offs are inevitable.

6. System type determines priority: interactive systems prioritize response time, batch systems prioritize throughput.

7. Higher CPU utilization does not always mean better system performance if other criteria suffer significantly.

8. Preemptive scheduling algorithms can better balance criteria like response time but introduce additional overhead.

## Common Mistakes to Avoid

1. Confusing turnaround time with waiting time—turnaround includes execution time, waiting time does not.

2. Assuming higher CPU utilization always means better performance—it may come at the cost of poor response times.

3. Forgetting that response time measures only the FIRST CPU allocation, not process completion.

4. Ignoring context switch overhead when evaluating scheduling algorithm efficiency.

5. Claiming one algorithm is universally "best" without specifying the criterion being optimized.

## Revision Tips

1. Practice numerical problems with different process sets and burst times to master calculations.

2. Create a comparison table of scheduling algorithms with their strengths and weaknesses regarding each criterion.

3. Remember that in DU exams, questions often ask you to calculate metrics for a specific algorithm, so practice FCFS, SJF, and Round Robin calculations thoroughly.

4. Understand real-world analogies: turnaround time is like delivery time, response time is like acknowledgment receipt.