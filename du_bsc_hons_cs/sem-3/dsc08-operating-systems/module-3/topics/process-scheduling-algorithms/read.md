# Process Scheduling Algorithms

## Introduction

Process scheduling is a fundamental concept in operating systems that determines which process runs on the CPU at any given time. In a modern computer system, multiple processes compete for limited CPU resources, and the operating system must manage this competition efficiently to maximize system performance. The scheduling algorithm chosen by a system administrator or embedded in the OS design directly impacts critical performance metrics such as throughput, turnaround time, and CPU utilization.

Understanding process scheduling algorithms is essential for computer science students because it bridges the gap between theoretical operating system concepts and practical system performance. In real-world scenarios, different operating systems employ different scheduling strategies. For instance, Linux uses the Completely Fair Scheduler (CFS), Windows employs a multilevel feedback queue approach, and real-time operating systems often use rate-monotonic or earliest deadline first scheduling. The study of classical algorithms like FCFS, SJF, Priority, and Round Robin provides the foundation needed to understand these modern implementations.

This topic carries significant weight in DU semester examinations, typically accounting for 15-20% of the total marks in Operating Systems papers. Students must not only understand the working of each algorithm but also be able to calculate and compare their performance using various scheduling criteria.

## Key Concepts

### CPU Scheduler and Dispatcher

The **CPU scheduler** is a component of the operating system that selects from among the processes in the ready queue and allocates the CPU to one of them. The **dispatcher** is the module that gives control of the CPU to the process selected by the CPU scheduler. This involves context switching, switching to user mode, and jumping to the proper location in the user program. The dispatcher latency—the time it takes for the dispatcher to stop one process and start another—is a critical factor in system performance.

### Scheduling Criteria

Evaluating scheduling algorithms requires understanding several key criteria:

- **CPU Utilization**: The percentage of time the CPU is busy. In a real system, CPU utilization ranges from 40% (lightly loaded) to 90% ( heavily loaded).
- **Throughput**: The number of processes that complete their execution per unit time. Higher throughput indicates better system efficiency.
- **Turnaround Time**: The total time from process arrival to process completion, including waiting time in ready queue, CPU execution time, and I/O time.
- **Waiting Time**: The total time a process spends waiting in the ready queue. This is the key metric that scheduling algorithms aim to minimize.
- **Response Time**: The time from process arrival to the first time the process gets CPU service. This is crucial for interactive systems.

### Types of Scheduling

**Preemptive scheduling** allows the operating system to interrupt a currently running process and reassign the CPU to another process. This introduces the concept of *context switching* and is essential for time-sharing systems. **Non-preemptive scheduling** once the CPU is assigned to a process, it keeps the CPU until it terminates or switches to waiting state. This simpler approach was used in early operating systems but can lead to poor response times.

## Scheduling Algorithms

### 1. First Come First Served (FCFS)

FCFS is the simplest scheduling algorithm where the process that arrives first gets CPU time first. Implementation uses a FIFO (First In First Out) queue. The ready queue is managed as a linked list where processes are appended in arrival order.

**Advantages**: Simple to implement, fair in terms of arrival order, no starvation.
**Disadvantages**: Convoy effect where short processes wait behind long processes, poor average waiting time, not suitable for time-sharing systems.

### 2. Shortest Job First (SJF)

SJF selects the process with the smallest burst time from the ready queue. It exists in two variants: **non-preemptive SJF** where once CPU is assigned, it cannot be taken away, and **preemptive SJF** (also known as Shortest Remaining Time First) where if a new process arrives with burst time less than the remaining time of current process, preemption occurs.

**Advantages**: Optimal for minimizing average waiting time (provably optimal for non-preemptive with known burst times).
**Disadvantages**: Can cause starvation of long processes, requires accurate burst time estimation.

### 3. Priority Scheduling

Each process is assigned a priority, and the CPU is allocated to the process with highest priority. Both preemptive and non-preemptive variants exist. Priorities can be assigned internally (based on memory requirements, file count, time limits) or externally (based on importance of process to user).

**Advantages**: Important processes get immediate attention.
**Disadvantages**: Can lead to starvation of low-priority processes (solution: aging—gradually increasing priority of waiting processes).

### 4. Round Robin (RR)

RR is designed specifically for time-sharing systems. A small unit of time called *time quantum* or *time slice* is defined (typically 10-100 milliseconds). The ready queue is treated as a circular queue. The CPU scheduler gives each process one time quantum in circular order.

**Advantages**: No starvation, good response time for interactive systems, fair allocation of CPU.
**Disadvantages**: Higher context switching overhead, if time quantum is too large it degrades to FCFS, if too small the overhead becomes significant.

### 5. Multilevel Queue Scheduling

This algorithm partitions the ready queue into multiple separate queues. Processes are permanently assigned to one queue based on some property (process type, priority, memory size). Each queue has its own scheduling algorithm. For example, system processes in high-priority queue might use FCFS while user processes in lower queue use RR.

**Advantages**: Combines advantages of different scheduling approaches.
**Disadvantages**: Inflexible—processes don't move between queues.

### 6. Multilevel Feedback Queue Scheduling

This is the most sophisticated classical CPU scheduling algorithm. It allows processes to move between queues based on their CPU burst characteristics. If a process uses too much CPU time, it is moved to a lower-priority queue. Processes waiting too long in lower queues can be moved to higher-priority queues (aging).

**Advantages**: Highly flexible, adapts to process behavior, minimizes turnaround time, prevents starvation.
**Disadvantages**: Complex to implement, requires parameters to be tuned properly.

## Examples

### Example 1: FCFS Scheduling Calculation

Consider four processes with the following arrival times and burst times:

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1      | 0            | 10         |
| P2      | 1            | 5          |
| P3      | 2            | 8          |
| P4      | 3            | 6          |

**Solution:**

Gantt Chart:
```
P1(0-10) | P2(10-15) | P3(15-23) | P4(23-29) |
```

Completion Times: P1=10, P2=15, P3=23, P4=29

Turnaround Time = Completion Time - Arrival Time:
- P1: 10 - 0 = 10
- P2: 15 - 1 = 14
- P3: 23 - 2 = 21
- P4: 29 - 3 = 26

Waiting Time = Turnaround Time - Burst Time:
- P1: 10 - 10 = 0
- P2: 14 - 5 = 9
- P3: 21 - 8 = 13
- P4: 26 - 6 = 20

Average Waiting Time = (0 + 9 + 13 + 20) / 4 = 42/4 = 10.5 units
Average Turnaround Time = (10 + 14 + 21 + 26) / 4 = 71/4 = 17.75 units

### Example 2: Non-Preemptive SJF

Using the same process data:

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1      | 0            | 10         |
| P2      | 1            | 5          |
| P3      | 2            | 8          |
| P4      | 3            | 6          |

**Solution:**

At time 0: Only P1 in queue, select P1
At time 10: P2(5), P3(8), P4(6) are waiting. Select P2 (shortest)
At time 15: P3(8), P4(6) waiting. Select P4
At time 21: P3(8) only

Gantt Chart:
```
P1(0-10) | P2(10-15) | P4(15-21) | P3(21-29) |
```

Completion Times: P1=10, P2=15, P4=21, P3=29

Turnaround Time:
- P1: 10 - 0 = 10
- P2: 15 - 1 = 14
- P4: 21 - 3 = 18
- P3: 29 - 2 = 27

Waiting Time:
- P1: 10 - 10 = 0
- P2: 14 - 5 = 9
- P4: 18 - 6 = 12
- P3: 27 - 8 = 19

Average Waiting Time = (0 + 9 + 12 + 19) / 4 = 40/4 = 10 units

### Example 3: Round Robin with Time Quantum = 4

Using the same data with time quantum = 4:

**Solution:**

Time 0: P1 arrives, executes 4 units (remaining: 6)
Time 4: P2 arrives, P1 moved to end, P2 executes 4 units (remaining: 1)
Time 8: P3 arrives, P2 moved to end, P3 executes 4 units (remaining: 4)
Time 12: P4 arrives, P3 moved to end, P4 executes 4 units (remaining: 2)
Time 16: P1 executes 4 units (remaining: 2)
Time 20: P2 executes 1 unit (completes)
Time 21: P3 executes 4 units (completes)
Time 25: P4 executes 2 units (completes)
Time 27: P1 executes 2 units (completes)

Gantt Chart:
```
P1(0-4) | P2(4-8) | P3(8-12) | P4(12-16) | P1(16-20) | P2(20-21) | P3(21-25) | P4(25-27) | P1(27-29)
```

Completion Times: P1=29, P2=21, P3=25, P4=27

Turnaround Time:
- P1: 29 - 0 = 29
- P2: 21 - 1 = 20
- P3: 25 - 2 = 23
- P4: 27 - 3 = 24

Waiting Time:
- P1: 29 - 10 = 19
- P2: 20 - 5 = 15
- P3: 23 - 8 = 15
- P4: 24 - 6 = 18

Average Waiting Time = (19 + 15 + 15 + 18) / 4 = 67/4 = 16.75 units

## Exam Tips

1. **Understand the difference between preemptive and non-preemptive**: This is frequently tested in DU exams. Remember that SJF can be both, Round Robin is inherently preemptive.

2. **Master waiting time calculations**: Most numerical problems ask for average waiting time. Always draw the Gantt chart first—it helps avoid mistakes.

3. **Know which algorithm gives optimal results**: SJF gives minimum average waiting time (for non-preemptive with known burst times), but FCFS gives minimum average waiting time for arrival time = 0 scenarios.

4. **Time quantum considerations**: Remember that if time quantum is too large, RR behaves like FCFS; if too small, context switching overhead increases significantly.

5. **Starvation vs Aging**: Starvation occurs when a process never gets CPU time due to low priority. Aging is the solution—gradually increasing priority of waiting processes.

6. **Context switching**: Preemptive algorithms cause more context switches than non-preemptive ones. This is an overhead that affects system performance.

7. **Real-world connection**: Be prepared to explain which algorithm would be suitable for which type of system (batch, interactive, real-time).

8. **Practice numerical problems**: DU exam always has a 10-15 mark numerical section on scheduling. Practice with at least 3-4 different sets of processes.

9. **Multilevel feedback queue**: This is the most complex but most flexible algorithm. Understand how processes move between queues.

10. **Remember scheduling criteria**: CPU utilization, throughput, turnaround time, waiting time, and response time. Each algorithm optimizes for different criteria.