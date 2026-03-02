# CPU Scheduling Algorithms


## Table of Contents

- [CPU Scheduling Algorithms](#cpu-scheduling-algorithms)
- [Introduction](#introduction)
- [Key Scheduling Criteria](#key-scheduling-criteria)
- [Scheduling Algorithms](#scheduling-algorithms)
  - [1. First-Come, First-Served (FCFS)](#1-first-come-first-served-fcfs)
  - [2. Shortest Job First (SJF)](#2-shortest-job-first-sjf)
  - [3. Priority Scheduling](#3-priority-scheduling)
  - [4. Round Robin (RR)](#4-round-robin-rr)
- [Comparative Analysis](#comparative-analysis)
- [Real-World Implementations](#real-world-implementations)
- [Examples](#examples)
  - [Example 1: SJF vs FCFS](#example-1-sjf-vs-fcfs)
  - [Example 2: Round Robin (q=2)](#example-2-round-robin-q2)
- [Exam Tips](#exam-tips)

## Introduction

CPU scheduling is the core mechanism that enables efficient resource utilization in operating systems. When multiple processes compete for CPU time, the scheduler determines the order of execution based on specific algorithms. These algorithms directly impact system performance metrics like throughput, latency, and fairness.

In modern computing environments ranging from embedded systems to cloud servers, effective scheduling ensures:

- Optimal response times for interactive applications
- High throughput for batch processing
- Fair allocation in multi-user systems
- Real-time guarantees for time-sensitive operations

The choice of scheduling algorithm depends on system objectives - time-sharing systems prioritize response time, batch systems emphasize throughput, while real-time systems focus on meeting deadlines.

## Key Scheduling Criteria

Before examining algorithms, understand these evaluation metrics:

| Metric          | Formula                        | Importance                        |
| --------------- | ------------------------------ | --------------------------------- |
| Waiting Time    | Σ(Start Time - Arrival Time)   | Measures queue delay              |
| Turnaround Time | Completion Time - Arrival Time | Total system interaction time     |
| Response Time   | First Response - Arrival Time  | Interactive system responsiveness |
| Throughput      | Processes Completed/Time Unit  | System productivity measure       |
| CPU Utilization | (Busy Time/Total Time) × 100%  | Resource efficiency metric        |

## Scheduling Algorithms

### 1. First-Come, First-Served (FCFS)

**Characteristics:**

- Non-preemptive
- Simple FIFO queue
- No priority considerations

**Algorithm:**

```python
1. Maintain ready queue in arrival order
2. Allocate CPU to first process
3. Process runs to completion
4. Select next process from queue
```

**Example Calculation:**
Process | Arrival Time | Burst Time
-------|-------------|-----------
P1 | 0 | 5
P2 | 1 | 3
P3 | 2 | 8

Gantt Chart: |P1(0-5)|P2(5-8)|P3(8-16)|

Waiting Times:

- P1: 0
- P2: 5-1 = 4
- P3: 8-2 = 6
  Average Waiting Time = (0+4+6)/3 = 3.33

**Advantages:**

- Simple implementation
- No starvation

**Disadvantages:**

- Convoy effect (long processes delay short ones)
- Poor for time-sharing systems

**Application:** Batch processing systems

### 2. Shortest Job First (SJF)

**Variants:**

- Non-preemptive: Once started, runs to completion
- Preemptive (SRTF): Can interrupt current process

**Algorithm (Preemptive):**

```python
1. At each time unit:
 a. Check if new process arrived
 b. Compare remaining time of current process with new processes
 c. Preempt if shorter job exists
```

**Example (Non-preemptive):**
Process | Arrival Time | Burst Time
-------|-------------|-----------
P1 | 0 | 6
P2 | 2 | 3
P3 | 4 | 4

Execution Order: P1 (0-6), P2 (6-9), P3 (9-13)
Average Waiting Time = (0 + (6-2) + (9-4))/3 = (0+4+5)/3 = 3

**Real-World Use:** Embedded systems with known task durations

### 3. Priority Scheduling

**Key Aspects:**

- Can be preemptive or non-preemptive
- Priorities assigned internally (memory needs, I/O) or externally (user-defined)
- Starvation possible (solution: aging)

**Algorithm:**

```python
1. Assign priority to each process
2. Select process with highest priority
3. For preemptive version:
 a. Interrupt running process if higher priority arrives
```

**Example:**
Process | Priority | Burst Time
-------|---------|-----------
P1 | 3 | 5
P2 | 1 | 3
P3 | 2 | 4

Execution Order: P2 (highest priority) → P3 → P1
Average Waiting Time = (8-0) + (0) + (3-0) = (8+0+3)/3 = 3.67

**Application:** Real-time operating systems

### 4. Round Robin (RR)

**Characteristics:**

- Preemptive
- Uses time quantum (q)
- Fair allocation but high context switching

**Algorithm:**

```python
1. Maintain circular ready queue
2. Allocate CPU for q time units
3. After q expires:
 a. Preempt process
 b. Add to queue end
4. Repeat until all processes complete
```

**Example (q=4):**
Process | Burst Time
-------|-----------
P1 | 6
P2 | 3
P3 | 1

Gantt Chart: |P1(0-4)|P2(4-7)|P3(7-8)|P1(8-10)|

Waiting Times:

- P1: (8-4) = 4
- P2: 4-0 = 4
- P3: 7-0 = 7
  Average Waiting Time = (4+4+7)/3 = 5

**Optimization Tip:** Quantum size should be 80% of average CPU burst

**Application:** Time-sharing systems, web servers

## Comparative Analysis

| Algorithm   | Preemptive | Avg Wait Time | Throughput | Starvation | Context Switches |
| ----------- | ---------- | ------------- | ---------- | ---------- | ---------------- |
| FCFS        | No         | High          | Medium     | No         | Low              |
| SJF         | Optional   | Lowest        | High       | Possible   | Medium           |
| Priority    | Optional   | Depends       | Medium     | Yes        | Medium           |
| Round Robin | Yes        | Medium        | Medium     | No         | High             |

## Real-World Implementations

- Linux CFS (Completely Fair Scheduler): Uses weighted round-robin
- Windows: Priority-based preemptive with quantum
- Real-time OS: Priority inheritance protocols
- Cloud Schedulers: Hybrid approaches with dynamic priorities

## Examples

### Example 1: SJF vs FCFS

**Process Set:**
Process | Arrival | Burst
-------|--------|-----
A | 0 | 3
B | 2 | 6
C | 4 | 4

**FCFS Solution:**
Gantt: A(0-3) → B(3-9) → C(9-13)
Wait Times: A=0, B=3-2=1, C=9-4=5
Average Wait = (0+1+5)/3 = 2

**SJF Solution:**
A runs first (only process at 0). At t=3:
Available processes: B(6), C(4) → Choose C
Gantt: A(0-3) → C(3-7) → B(7-13)
Wait Times: A=0, B=7-2=5, C=3-4= -1 → 0 (can't be negative)
Average Wait = (0+5+0)/3 ≈ 1.67

### Example 2: Round Robin (q=2)

**Processes:**
Process | Burst
-------|-----
P1 | 5
P2 | 3
P3 | 1

**Execution:**
Cycle 1: P1(0-2), P2(2-4), P3(4-5)
Remaining: P1(3), P2(1)
Cycle 2: P1(5-7), P2(7-8)
Total Wait:
P1: (2-0) + (5-4) = 2+1=3
P2: (4-2) + (7-5) = 2+2=4
P3: 0
Average = (3+4+0)/3 ≈ 2.33

## Exam Tips

1. **Calculation Priority:** Always compute waiting time as (start time - arrival time), not just queue time
2. **Preemption Points:** For RR/SRTF, create timeline tables showing each time unit
3. **Gantt Charts:** Draw even if not asked - helps visualize process order
4. **Starvation Solutions:** Mention aging when discussing priority scheduling
5. **Quantum Effects:** Understand that large quantum makes RR behave like FCFS
6. **Convoy Effect:** Always cite in FCFS disadvantages
7. **SJF Optimality:** Remember it gives minimum average waiting time but requires exact burst times
