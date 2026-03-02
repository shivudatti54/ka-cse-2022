# Scheduling Criteria

## Overview

Scheduling criteria are performance metrics used to evaluate and compare CPU scheduling algorithms. The five core criteria are CPU utilization, throughput, turnaround time, waiting time, and response time. Different system types prioritize different criteria based on their purpose.

## Key Points

- **CPU Utilization**: Percentage of time CPU actively executing a process (goal: maximize, 40-90% in real systems)
- **Throughput**: Number of processes completed per unit time (goal: maximize, varies from 1/hour for long processes to 1000/second for transactions)
- **Turnaround Time**: Total time from process submission to completion, includes waiting, executing, and I/O time (goal: minimize average)
- **Waiting Time**: Total time process spends in ready queue, only metric affected by scheduler (goal: minimize average)
- **Response Time**: Time from submission to first response produced, critical for interactive systems (goal: minimize average)
- **Trade-offs**: Maximizing throughput may increase waiting time, minimizing response time may lower CPU utilization
- **System Types**: Batch systems focus on throughput/turnaround time, interactive systems focus on response/waiting time, all aim for high CPU utilization

## Important Concepts

- Waiting Time = Turnaround Time - Total CPU Execution Time (key formula)
- Scheduler only affects waiting time, not execution time or I/O time
- Criteria often conflict - algorithm design requires balancing based on use case
- Performance metrics determine algorithm effectiveness for specific scenarios

## Notes

- Know which criteria to maximize (CPU utilization, throughput) vs minimize (turnaround, waiting, response)
- Understand system type priorities: batch vs interactive vs real-time
- Remember waiting time is the primary focus since scheduler can only affect this
- Practice calculating each metric from given process data
