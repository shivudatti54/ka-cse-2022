# Thread Scheduling

## Overview

Thread scheduling determines which thread runs on which CPU core and for how long, allocating CPU time slices to threads. Schedulers use algorithms like FCFS (non-preemptive) and Round-Robin (preemptive) to distribute CPU time while maintaining fairness, responsiveness, and CPU utilization.

## Key Points

- **Ready Queue**: Holds all threads in "Ready" state waiting for CPU time
- **Context Switch**: Save current thread state, load new thread state - critical overhead factor
- **Non-Preemptive Scheduling**: Thread keeps CPU until termination or voluntary block (FCFS - simple but convoy effect)
- **Preemptive Scheduling**: Scheduler can interrupt running thread (Round-Robin with time quantum, Priority scheduling)
- **Priority Scheduling**: Highest-priority thread gets CPU, can cause starvation (solved by aging)
- **User-Level Threads (ULTs)**: Managed by thread library, OS unaware, if one blocks all block
- **Kernel-Level Threads (KLTs)**: OS manages threads, true parallel execution on multicore, directly scheduled onto CPU cores
- **Hybrid Model**: Multiple ULTs mapped to smaller pool of KLTs - flexibility + efficiency

## Important Concepts

- Time quantum in Round-Robin critical: too low causes high context switch overhead, ensures fairness
- Aging gradually increases priority of waiting threads to prevent starvation
- Modern systems (Windows, Linux) use hybrid model combining ULT flexibility with KLT efficiency
- Preemptive scheduling essential for interactive systems providing responsive user experience

## Notes

- Understand trade-off between FCFS (simple, poor performance) and Round-Robin (fair, overhead)
- Know difference between user-level and kernel-level thread scheduling
- Starvation in priority scheduling solved by aging mechanism
- Practice scenarios showing context switching and scheduler decisions
