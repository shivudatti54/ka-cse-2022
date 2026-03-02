# Scheduling Criteria - Summary

## Key Definitions

- **CPU Utilization**: The percentage of time the CPU is actively executing processes, measuring system efficiency.
- **Throughput**: The number of processes completed per unit time, indicating the system's overall work rate.
- **Turnaround Time**: Total time from process submission to completion, including all waiting and execution periods.
- **Waiting Time**: Total time a process spends in the ready queue waiting for CPU allocation.
- **Response Time**: The interval between process arrival and the start of its first CPU execution.

## Important Formulas

- **CPU Utilization** = (Busy Time / Total Time) × 100%
- **Throughput** = Number of Completed Processes / Time Interval
- **Turnaround Time** = Completion Time - Arrival Time
- **Waiting Time** = Turnaround Time - Burst Time
- **Response Time** = First CPU Allocation Time - Arrival Time

## Key Points

1. CPU scheduling criteria provide objective measures for comparing and evaluating different scheduling algorithms.

2. Maximizing CPU utilization ensures expensive hardware resources are efficiently employed, particularly important in batch processing systems.

3. Throughput measures the aggregate rate of process completion, independent of individual process characteristics.

4. Turnaround time encompasses the complete process lifecycle and directly affects user-perceived performance.

5. Waiting time is the component of turnaround time that the operating system can directly control through scheduling decisions.

6. Response time is critical for interactive systems where immediate feedback to user actions determines system responsiveness.

7. Different system types prioritize different criteria: interactive systems favor response time, while batch systems emphasize throughput and CPU utilization.

8. No single scheduling algorithm optimizes all criteria simultaneously—trade-offs are inherent and unavoidable.

9. The relationship between criteria depends on process characteristics such as burst time distribution and arrival patterns.

10. Understanding these criteria is fundamental to designing and implementing effective CPU scheduling solutions.

## Common Mistakes

1. **Confusing Waiting Time with Turnaround Time**: Waiting time excludes actual CPU execution time, while turnaround time includes it. Always subtract burst time from turnaround time to verify waiting time calculations.

2. **Ignoring Process Arrival Times**: Many students assume all processes arrive at time 0, but arrival times significantly affect calculations and must be incorporated into analysis.

3. **Forgetting Response Time vs Completion**: Response time measures only until first CPU allocation, not until process termination—conflating these produces incorrect results.

4. **Overlooking Context Switch Overhead**: In real systems, context switching consumes CPU time and affects actual utilization and throughput, though theoretical problems often ignore this overhead.

5. **Assuming All Processes Have Single Bursts**: Real processes have multiple CPU and I/O bursts; single-burst analysis is a simplification that may not reflect actual system behavior.