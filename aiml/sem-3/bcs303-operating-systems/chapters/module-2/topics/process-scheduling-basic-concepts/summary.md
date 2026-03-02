# Process Scheduling Basic Concepts - Summary

## Key Definitions and Concepts

- PROCESS SCHEDULING is the mechanism by which the operating system decides which process executes on the CPU and for how long
- A SCHEDULER is the component of the operating system that implements the scheduling algorithm
- CONTEXT SWITCHING is the process of saving and restoring the state of a CPU so that multiple processes can share a single processor
- PREEMPTION allows the operating system to forcibly interrupt a running process, while NON-PREEMPTIVE scheduling requires processes to voluntarily yield the CPU

## Important Formulas and Theorems

- Turnaround Time = Completion Time - Arrival Time
- Waiting Time = Turnaround Time - Burst Time
- Average Turnaround Time = Sum of All Turnaround Times / Number of Processes
- Average Waiting Time = Sum of All Waiting Times / Number of Processes

## Key Points

- Operating systems implement three levels of scheduling: long-term (admission), short-term (CPU), and medium-term (swapping)
- The short-term scheduler is the most frequently invoked and operates at millisecond intervals
- CPU utilization measures productive CPU usage, while throughput measures completed processes per time unit
- Turnaround time includes waiting time plus execution time, while waiting time is only the time spent in the ready queue
- Preemptive scheduling enables better response time and system responsiveness but requires more complex implementation
- Non-preemptive scheduling is simpler but can lead to poor system responsiveness under heavy load
- Round-Robin scheduling uses a time quantum to allocate CPU time fairly among processes

## Common Mistakes to Avoid

- Confusing waiting time with turnaround time; waiting time does NOT include actual CPU execution time
- Forgetting that context switching overhead reduces effective CPU utilization
- Assuming FCFS always provides the best performance; it suffers from the convoy effect
- Choosing an inappropriately small time quantum in Round-Robin, causing excessive context switches
- Ignoring the fact that SJF requires knowledge of future CPU burst times, which is not practical in real systems

## Revision Tips

- Always draw Gantt charts when solving numerical problems to visualize process execution
- Practice calculating waiting times and turnaround times for all standard algorithms
- Memorize the five scheduling criteria and understand when each is most important
- Review the differences between preemptive and non-preemptive versions of common algorithms