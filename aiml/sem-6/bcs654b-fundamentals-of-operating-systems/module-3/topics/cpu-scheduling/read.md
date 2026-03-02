# CPU Scheduling Concepts


## Table of Contents

- [CPU Scheduling Concepts](#cpu-scheduling-concepts)
- [Introduction to CPU Scheduling](#introduction-to-cpu-scheduling)
- [Scheduling Criteria](#scheduling-criteria)
- [Scheduling Queues](#scheduling-queues)
- [Scheduler Types](#scheduler-types)
- [Context Switch](#context-switch)
- [Preemptive vs. Non-Preemptive Scheduling](#preemptive-vs-non-preemptive-scheduling)
- [Dispatch](#dispatch)
- [Common Scheduling Algorithms](#common-scheduling-algorithms)
  - [1. First-Come, First-Served (FCFS)](#1-first-come-first-served-fcfs)
  - [2. Shortest-Job-First (SJF)](#2-shortest-job-first-sjf)
  - [3. Priority Scheduling](#3-priority-scheduling)
  - [4. Round Robin (RR)](#4-round-robin-rr)
- [Algorithm Comparison](#algorithm-comparison)
- [Thread Scheduling](#thread-scheduling)
- [Exam Tips](#exam-tips)

## Introduction to CPU Scheduling

CPU scheduling is a fundamental function of an operating system that determines which process runs on the CPU at any given time. In a multiprogramming system, multiple processes reside in memory simultaneously. However, a CPU can only execute one instruction from one process at a time. The **scheduler** is the OS component responsible for selecting the next process to run. When the CPU becomes idle, the scheduler selects a process from the **ready queue** to be executed.

The primary objectives of CPU scheduling are:

- Maximize CPU utilization
- Ensure fairness among processes
- Maximize throughput (number of processes completed per unit time)
- Minimize turnaround time (time from submission to completion)
- Minimize waiting time (time spent in the ready queue)
- Minimize response time (time from submission until first response)

## Scheduling Criteria

To evaluate and compare scheduling algorithms, we use specific performance metrics:

| Metric              | Description                                 | Formula (if applicable)                 |
| :------------------ | :------------------------------------------ | :-------------------------------------- |
| **CPU Utilization** | Percentage of time the CPU is busy          | `(Busy time / Total time) * 100%`       |
| **Throughput**      | Number of processes completed per unit time | `Number of processes / Total time`      |
| **Turnaround Time** | Total time from submission to completion    | `Completion time - Arrival time`        |
| **Waiting Time**    | Total time spent waiting in the ready queue | `Turnaround time - Burst time`          |
| **Response Time**   | Time from submission until first response   | `Time of first response - Arrival time` |

## Scheduling Queues

Processes move between various queues during their lifetime. The key queues involved in scheduling are:

1. **Job Queue**: All processes in the system.
2. **Ready Queue**: Processes residing in main memory that are ready and waiting to execute.
3. **Device Queues**: Processes waiting for a particular I/O device.

```
+----------------+ Event Occurs +---------------+
| | ------------------> | |
| Running State | | Ready Queue |
| | <------------------ | |
+----------------+ Dispatch +---------------+
 ^ |
 | | I/O Completion,
 | Scheduler Invoked | Time Slice Expired
 | (e.g., I/O Request) v
+----------------+ +---------------+
| | | |
| Wait Queue | <------------------ | I/O Device |
| (for I/O, etc.)| | |
| | ------------------> | |
+----------------+ I/O Available +---------------+
```

## Scheduler Types

The OS employs different schedulers for different purposes:

- **Long-Term Scheduler (Job Scheduler)**: Selects which processes should be brought into the ready queue from the job pool (disk). It controls the **degree of multiprogramming** (number of processes in memory) and is responsible for a good mix of I/O-bound and CPU-bound processes.
- **Short-Term Scheduler (CPU Scheduler)**: Selects which process from the ready queue should be executed next and allocates the CPU to it. This scheduler is invoked very frequently (every few milliseconds), so it must be extremely fast.
- **Medium-Term Scheduler**: Used in systems with time-sharing. It can temporarily remove (swap out) a process from memory to reduce the degree of multiprogramming and later swap it back in.

## Context Switch

When the CPU switches from executing one process to another, a **context switch** must occur. The context of the current process (its state, including the values of CPU registers, program counter, etc.) is saved into its Process Control Block (PCB). The context of the newly selected process is then loaded from its PCB into the CPU registers. This operation is pure overhead because the system does no useful work while switching. The speed of a context switch is heavily dependent on hardware support.

```
+-------------------------+ +-------------------------+
| Process A: Running | | Process B: Running |
| - Registers: R1, R2, PC | | - Registers: R1, R2, PC |
+-------------------------+ +-------------------------+
 | ^
 | Save State to PCB A | Load State from PCB B
 v |
+-------------------------+ +-------------------------+
| PCB A: Saved Context | | PCB B: Saved Context |
+-------------------------+ +-------------------------+
```

## Preemptive vs. Non-Preemptive Scheduling

CPU scheduling decisions can take place under four main circumstances:

1. When a process switches from the running state to the waiting state (e.g., I/O request).
2. When a process switches from the running state to the ready state (e.g., interrupt).
3. When a process switches from the waiting state to the ready state (e.g., I/O completion).
4. When a process terminates.

Based on when these decisions can happen, scheduling is categorized as:

- **Non-Preemptive Scheduling**: Once the CPU is allocated to a process, the process keeps it until it terminates or switches to the waiting state. Scheduling decisions only occur in circumstances 1 and 4. Algorithms like First-Come, First-Served (FCFS) and Shortest Job First (SJF) can be non-preemptive.
- **Preemptive Scheduling**: A process can be interrupted and forced to release the CPU, even if it is still running and would like to continue. Scheduling decisions can occur in all four circumstances. This is more common in modern time-sharing systems but requires careful handling of shared data to avoid race conditions. Algorithms like Round Robin (RR) and preemptive SJF are examples.

## Dispatch

The **dispatcher** is the module that gives control of the CPU to the process selected by the short-term scheduler. Its functions include:

- Switching context
- Switching to user mode
- Jumping to the proper location in the user program to restart it

The time taken by the dispatcher to stop one process and start another is called the **dispatch latency**.

## Common Scheduling Algorithms

### 1. First-Come, First-Served (FCFS)

The simplest algorithm; processes are assigned the CPU in the order they request it. It is inherently non-preemptive.

_Example:_
Processes arrive in order: P1 (burst time 24), P2 (burst time 3), P3 (burst time 3).

```
Gantt Chart:
+----+----+----+
| P1 | P2 | P3 |
+----+----+----+
0 24 27 30

Waiting Time:
P1: 0
P2: 24
P3: 27
Average Waiting Time: (0 + 24 + 27)/3 = 17
```

**Convoy Effect**: Short processes wait behind one long process, leading to high average waiting time.

### 2. Shortest-Job-First (SJF)

Associates with each process the length of its next CPU burst. The scheduler selects the process with the smallest next CPU burst. It can be preemptive (Shortest Remaining Time First - SRTF) or non-preemptive.

_Example (Non-preemptive):_
Processes: P1 (burst 6, arrival 0), P2 (burst 8, arrival 0), P3 (burst 7, arrival 0), P4 (burst 3, arrival 0).
SJF order: P4, P1, P3, P2.

```
Gantt Chart:
+----+----+----+----+
| P4 | P1 | P3 | P2 |
+----+----+----+----+
0 3 9 16 24

Waiting Time:
P1: 3
P2: 16
P3: 9
P4: 0
Average Waiting Time: (3+16+9+0)/4 = 7
```

SJF is provably optimal for minimizing average waiting time but is impossible to implement at the short-term level because the next CPU burst length is not known. It must be predicted.

### 3. Priority Scheduling

A priority number (integer) is associated with each process. The CPU is allocated to the process with the highest priority (smallest integer = highest priority is common). Can be preemptive or non-preemptive.

**Starvation (Indefinite Blocking)**: Low-priority processes may wait indefinitely. Solution: **Aging** - gradually increase the priority of processes that wait for a long time.

### 4. Round Robin (RR)

Designed specifically for time-sharing systems. Each process gets a small unit of CPU time (**time quantum** or **time slice**), typically 10-100 milliseconds. After this time has elapsed, the process is preempted and added to the end of the ready queue.

_Example:_
Processes: P1 (burst 24), P2 (burst 3), P3 (burst 3). Time Quantum = 4.

```
Gantt Chart:
+----+----+----+----+----+----+----+----+
| P1 | P2 | P3 | P1 | P1 | P1 | P1 | P1 |
+----+----+----+----+----+----+----+----+
0 4 7 10 14 18 22 26 30

Waiting Time:
P1: (0 + (10-4)) = 6 // Waits from time 4 to 10, and finishes at 30.
P2: 4 // Arrives at 0, starts at 4.
P3: 7 // Arrives at 0, starts at 7.
Average Waiting Time: (6+4+7)/3 ≈ 5.66
```

Performance depends heavily on the size of the time quantum. If the quantum is very large, RR degenerates to FCFS. If the quantum is very small, context switch overhead becomes high.

## Algorithm Comparison

| Algorithm       | Mode           | Advantages                  | Disadvantages                                                            |
| :-------------- | :------------- | :-------------------------- | :----------------------------------------------------------------------- |
| **FCFS**        | Non-Preemptive | Simple, easy to implement   | Convoy effect, high waiting time                                         |
| **SJF**         | Both           | Optimal avg. waiting time   | Difficult to predict burst time, can cause starvation                    |
| **Priority**    | Both           | Good for real-time systems  | Starvation of low-priority processes                                     |
| **Round Robin** | Preemptive     | Good for time-sharing, fair | High context switch overhead with small quantum, poor if bursts are long |

## Thread Scheduling

Thread scheduling operates on two levels:

1. **Process Contention Scope (PCS)**: Scheduling done by the thread library to decide which user-level thread to put onto an available lightweight process (LWP). This is invisible to the kernel.
2. **System Contention Scope (SCS)**: Scheduling done by the kernel to decide which kernel-level thread (or which process's LWP) to assign to a CPU.

On systems using the many-to-many or many-to-one model, the PCS scheduler and the SCS scheduler work together. On systems using the one-to-one model (e.g., Windows, Linux), thread scheduling is typically done solely by the kernel using SCS.

## Exam Tips

1. **Understand the Metrics**: Be able to calculate turnaround time, waiting time, and response time from a given Gantt chart or process list. Remember: `Waiting Time = Turnaround Time - Burst Time`.
2. **Draw Gantt Charts**: For any scheduling algorithm question, the first step is usually to draw the Gantt chart showing the order of execution. This makes calculating the performance metrics much easier.
3. **Know the Trade-offs**: No single algorithm is best for all situations. Be prepared to discuss the pros and cons of each (e.g., RR is fair but has overhead, SJF has low waiting time but is hard to implement).
4. **Preemption is Key**: Pay close attention to whether a problem specifies a preemptive or non-preemptive variant of an algorithm (especially for SJF and Priority). The results can be very different.
5. **Context Switch Overhead**: Remember that context switches take time. When evaluating RR, consider how the time quantum size affects this overhead and overall performance.
