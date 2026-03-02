# CPU Scheduling Algorithms

## Introduction to CPU Scheduling

CPU scheduling is a fundamental function of an operating system that determines which process runs on the CPU when multiple processes are ready to execute. The CPU scheduler selects from among the processes in memory that are ready to execute and allocates the CPU to one of them.

**Why is Scheduling Needed?**

- Multiprogramming: Maximize CPU utilization by switching between processes
- Time-sharing: Allow multiple users to interact with the system simultaneously
- Fairness: Ensure all processes get fair share of CPU time
- Efficiency: Minimize overhead and maximize throughput

## Scheduling Criteria

Several criteria are used to evaluate scheduling algorithms:

| Criterion           | Description                                 | Ideal Value   |
| ------------------- | ------------------------------------------- | ------------- |
| **CPU Utilization** | Percentage of time CPU is busy              | High (40-90%) |
| **Throughput**      | Number of processes completed per time unit | High          |
| **Turnaround Time** | Time from submission to completion          | Low           |
| **Waiting Time**    | Time process spends waiting in ready queue  | Low           |
| **Response Time**   | Time from submission until first response   | Low           |

## Scheduling Algorithms

### 1. First-Come, First-Served (FCFS)

The simplest scheduling algorithm that processes requests in the order they arrive.

**Characteristics:**

- Non-preemptive: Once CPU allocated, process keeps it until termination
- Implemented using FIFO queue
- Can lead to convoy effect: short processes wait behind long ones

**Example:**

```
Process    Burst Time (ms)
P1         24
P2         3
P3         3

Gantt Chart:
|   P1   | P2 | P3 |
0       24   27   30

Waiting Time: P1=0, P2=24, P3=27
Average Waiting Time: (0+24+27)/3 = 17ms
```

### 2. Shortest-Job-First (SJF)

Selects the process with the smallest next CPU burst. Can be preemptive (Shortest-Remaining-Time-First) or non-preemptive.

**Characteristics:**

- Optimal for minimizing average waiting time
- Difficult to implement (need to know next CPU burst)
- Can lead to starvation of longer processes

**Example (Non-preemptive):**

```
Process    Arrival Time    Burst Time
P1         0               8
P2         1               4
P3         2               9
P4         3               5

Execution Order: P1, P2, P4, P3
Gantt Chart:
| P1 | P2 | P4  | P3     |
0    8   12   17      26

Waiting Time: P1=0, P2=7, P3=15, P4=9
Average Waiting Time: (0+7+15+9)/4 = 7.75ms
```

### 3. Priority Scheduling

Each process is assigned a priority, and the CPU is allocated to the process with the highest priority.

**Characteristics:**

- Can be preemptive or non-preemptive
- Priorities can be internal (based on time limits, memory requirements) or external (user-defined)
- Can lead to starvation (indefinite blocking) of low-priority processes
- Aging technique can be used: gradually increase priority of waiting processes

### 4. Round Robin (RR)

Designed for time-sharing systems. Each process gets a small unit of CPU time (time quantum), typically 10-100ms.

**Characteristics:**

- Preemptive: Process is interrupted if not completed within time quantum
- Performance depends heavily on time quantum size
- Large quantum → FCFS behavior
- Small quantum → high context switch overhead

**Example (Time Quantum = 4ms):**

```
Process    Burst Time
P1         24
P2         3
P3         3

Gantt Chart:
| P1 | P2 | P3 | P1 | P1 | P1 | P1 | P1 |
0   4   7   10  14  18  22  26  30

Waiting Time: P1=6, P2=4, P3=7
Average Waiting Time: (6+4+7)/3 = 5.67ms
```

### 5. Multilevel Queue Scheduling

Ready queue is partitioned into separate queues based on process characteristics (system processes, interactive processes, batch processes, etc.).

**Characteristics:**

- Each queue can have its own scheduling algorithm
- Scheduling between queues: fixed priority or time slice

### 6. Multilevel Feedback Queue Scheduling

Allows processes to move between queues based on their behavior and CPU burst characteristics.

**Characteristics:**

- More flexible than multilevel queue scheduling
- Parameters: number of queues, scheduling algorithms for each queue, method to determine when to upgrade/demote process

## Thread Scheduling

Thread scheduling can occur at two levels:

1. **Process-contention scope (PCS)**: User-level threads scheduled by thread library
2. **System-contention scope (SCS)**: Kernel-level threads scheduled by OS

## Algorithm Comparison

| Algorithm               | Preemptive? | Advantages                                 | Disadvantages                        |
| ----------------------- | ----------- | ------------------------------------------ | ------------------------------------ |
| **FCFS**                | No          | Simple, fair                               | Convoy effect, poor for time-sharing |
| **SJF**                 | Optional    | Minimal waiting time                       | Difficult to predict burst time      |
| **Priority**            | Optional    | Priority-based service                     | Starvation of low-priority processes |
| **Round Robin**         | Yes         | Good for time-sharing                      | Performance depends on quantum size  |
| **Multilevel Queue**    | Varies      | Different policies for different processes | Complex implementation               |
| **Multilevel Feedback** | Yes         | Adaptive, flexible                         | Most complex to implement            |

## Real-World Considerations

Modern operating systems use hybrid approaches:

- **Windows**: Priority-based with dynamic priority adjustment
- **Linux**: Completely Fair Scheduler (CFS) based on virtual runtime
- **macOS**: Multilevel feedback queue with priority classes

## Exam Tips

1. **Gantt Charts**: Practice drawing Gantt charts for different algorithms with various process sequences
2. **Waiting Time Calculation**: Remember that waiting time = turnaround time - burst time
3. **SJF Optimality**: SJF gives minimum average waiting time but is difficult to implement
4. **Quantum Size**: For Round Robin, understand the trade-off between response time and context switch overhead
5. **Starvation**: Identify which algorithms can cause starvation and how to prevent it
6. **Real Systems**: Be prepared to discuss how real operating systems implement scheduling
