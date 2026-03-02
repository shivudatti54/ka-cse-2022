# CPU Scheduling Concepts

## Why CPU Scheduling?

- Maximize CPU utilization
- Maximize throughput
- Minimize waiting time
- Minimize turnaround time
- Minimize response time

## Scheduling Criteria

| Criterion       | Description                              | Goal     |
| --------------- | ---------------------------------------- | -------- |
| CPU Utilization | % time CPU is busy                       | Maximize |
| Throughput      | Processes completed per time unit        | Maximize |
| Turnaround Time | Total time from submission to completion | Minimize |
| Waiting Time    | Time spent in ready queue                | Minimize |
| Response Time   | Time from submission to first response   | Minimize |

## Key Formulas

```
Turnaround Time = Completion Time - Arrival Time
Waiting Time = Turnaround Time - Burst Time
Response Time = First Response Time - Arrival Time
```

## Types of Scheduling

### Non-Preemptive

- Process runs until it blocks or terminates
- Simple but poor response time
- Examples: FCFS, SJF (non-preemptive)

### Preemptive

- Process can be interrupted
- Better response time
- Requires context switches
- Examples: Round Robin, SRTF, Priority (preemptive)

## Scheduling Queues

- **Job Queue**: All processes in system
- **Ready Queue**: Processes in memory, ready to run
- **Device Queues**: Processes waiting for I/O

## Dispatcher

Gives CPU control to selected process:

1. Context switch
2. Switch to user mode
3. Jump to proper location in program

**Dispatch Latency**: Time to stop one process and start another.

> **Exam Tip**: Know all formulas. Practice calculating turnaround and waiting times for different algorithms.
