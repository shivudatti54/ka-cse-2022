# Process Management and Scheduling - Summary

## Key Definitions and Concepts
- **Process**: Instance of program in execution with associated resources
- **Thread**: Lightweight process sharing memory space
- **Context Switch**: Saving/restoring process state during scheduler decisions
- **Throughput**: Number of processes completed per time unit
- **Quantum**: Time slice allocated in Round Robin scheduling

## Important Formulas and Theorems
- **CPU Utilization** = (Busy Time)/(Total Time) × 100%
- **Average Waiting Time** = Σ(Waiting Times)/n
- **Turnaround Time** = Completion Time - Arrival Time
- **Response Time** = First Response Time - Arrival Time
- **Little's Law**: L = λW (System processes = Arrival rate × Avg. time in system)

## Key Points
- FCFS suffers from Convoy Effect with long processes
- SJF gives minimum average waiting time but needs exact burst times
- Round Robin performance depends heavily on time quantum size
- Priority scheduling requires aging to prevent starvation
- Multilevel Feedback Queues combine multiple scheduling strategies
- Real-time systems use Rate Monotonic scheduling
- Linux uses Completely Fair Scheduler (CFS) with virtual runtime

## Common Mistakes to Avoid
- Confusing preemptive vs non-preemptive SJF
- Forgetting to account for arrival times in calculations
- Missing context switch overhead in performance analysis
- Assuming all scheduling algorithms are suitable for real-time systems

## Revision Tips
1. Practice drawing Gantt charts for different algorithms
2. Create comparison tables for scheduling algorithms
3. Use Python simulations to verify manual calculations
4. Study Linux's CFS and Windows' scheduler for real-world implementations
5. Focus on trade-offs: fairness vs throughput vs response time