# Process Scheduling


## Table of Contents

- [Process Scheduling](#process-scheduling)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Types of Schedulers](#types-of-schedulers)
  - [Scheduling Queues](#scheduling-queues)
  - [Context Switch](#context-switch)
  - [The Dispatcher](#the-dispatcher)
  - [Scheduling Criteria](#scheduling-criteria)
  - [Preemptive vs. Non-Preemptive Scheduling](#preemptive-vs-non-preemptive-scheduling)
- [Examples](#examples)
- [Exam Tips](#exam-tips)

## Introduction

Process scheduling is a fundamental function of any operating system that manages the execution of multiple processes on the CPU. In a modern computing environment, hundreds or thousands of processes compete for limited CPU resources. The operating system must decide which process gets the CPU, for how long, and in what order. This decision-making process is known as process scheduling, and it directly impacts system performance, throughput, and user responsiveness.

The need for process scheduling arises from the fundamental mismatch between the number of processes and the limited number of CPU cores. When a process initiates an I/O operation, the CPU remains idle. Rather than wasting this idle CPU time, the scheduler can dispatch another ready process to utilize the CPU effectively. This multiplexing of CPU time among processes enables multiprogramming, which maximizes CPU utilization and system throughput.

Process scheduling operates at different levels within the operating system. The long-term scheduler controls the degree of multiprogramming by deciding which processes enter the ready queue from the job pool. The short-term scheduler (also called the CPU scheduler) selects which process from the ready queue gets the CPU next. The medium-term scheduler temporarily removes processes from memory to manage the degree of multiprogramming and improve system efficiency.

## Key Concepts

### Types of Schedulers

**Long-term Scheduler (Job Scheduler):** This scheduler controls the number of processes admitted to the system from the pool of new processes. It selects processes from the job pool and loads them into memory for execution. The long-term scheduler aims to maintain a balance between I/O-bound and CPU-bound processes to optimize system throughput. In modern systems, particularly time-sharing systems, the long-term scheduler may be minimal or absent, as processes are often admitted directly to the ready queue.

**Short-term Scheduler (CPU Scheduler):** This is the most critical scheduler that selects a process from the ready queue and allocates the CPU to it. The short-term scheduler must be extremely fast since it is invoked frequently (every few milliseconds). It uses various scheduling algorithms to make its decision based on criteria such as priority, burst time, or arrival time.

**Medium-term Scheduler:** This scheduler performs swapping operations—moving processes between main memory and secondary storage. It removes processes from memory when system load is high and brings them back when load decreases. This technique, called swapping, helps manage the degree of multiprogramming and improves system responsiveness.

### Scheduling Queues

The operating system maintains several queues to manage process states:

**Job Queue:** Contains all processes submitted to the system but not yet admitted to memory.

**Ready Queue:** Contains all processes that are in main memory and ready to execute. The ready queue is typically implemented as a linked list or priority queue, with each PCB (Process Control Block) containing a pointer to the next process in the queue.

**Device Queues:** Each I/O device has its own queue containing processes waiting for that particular device. When a process requests I/O, it is moved from the ready queue to the appropriate device queue.

### Context Switch

When the CPU switches from one process to another, the operating system must save the state of the old process and load the saved state of the new process. This mechanism is called a context switch. The context of a process is stored in its PCB and includes the value of CPU registers, program counter, memory management information, and I/O status information.

The time required for a context switch is pure overhead because the CPU performs no useful work during this transition. Context switch time varies depending on the operating system and hardware, typically ranging from 1 to 1000 microseconds. Modern systems employ various techniques to minimize context switch overhead, including optimized data structures and hardware support for fast state saving.

### The Dispatcher

The dispatcher is the component that gives control of the CPU to the process selected by the short-term scheduler. It performs the following functions:

1. **Context switch:** Switching context from the old process to the new process
2. **Switch to user mode:** Restoring the program counter to the proper location
3. **Jump to the proper location:** Transferring control to the selected process

The dispatcher latency is the time required for the dispatcher to stop one process and start another. Minimizing dispatcher latency is crucial for system responsiveness.

### Scheduling Criteria

Different scheduling algorithms aim to optimize various system properties:

**CPU Utilization:** The percentage of time the CPU is actively executing processes. In a well-utilized system, CPU utilization should remain as close to 100% as possible.

**Throughput:** The number of processes completed per unit time. Higher throughput indicates better system efficiency.

**Turnaround Time:** The total time from process submission to process completion, including waiting time in the ready queue, execution time, and I/O time.

**Waiting Time:** The total time a process spends waiting in the ready queue. This is a critical metric as it represents non-productive time.

**Response Time:** The time from process submission to the first response (not completion). This metric is particularly important for interactive systems.

### Preemptive vs. Non-Preemptive Scheduling

In **non-preemptive scheduling**, once a process gets the CPU, it keeps the CPU until it voluntarily releases it (through termination or I/O request). This approach is simple but may lead to poor response times for interactive processes.

In **preemptive scheduling**, the operating system can forcibly take the CPU away from a running process. This enables better response times and ensures that high-priority processes can interrupt lower-priority ones. However, preemptive scheduling introduces additional complexity and potential race conditions.

## Examples

**Example 1: Calculating Turnaround Time and Waiting Time**

Consider three processes P1, P2, and P3 with the following burst times (in milliseconds):

- P1: Burst time = 24, Arrival time = 0
- P2: Burst time = 3, Arrival time = 0
- P3: Burst time = 3, Arrival time = 0

Using FCFS (First-Come-First-Served) scheduling:

**Execution Order:** P1 → P2 → P3

- **P1:** Completion time = 24, Turnaround time = 24 - 0 = 24 ms, Waiting time = 0 ms
- **P2:** Completion time = 24 + 3 = 27, Turnaround time = 27 - 0 = 27 ms, Waiting time = 24 ms
- **P3:** Completion time = 27 + 3 = 30, Turnaround time = 30 - 0 = 30 ms, Waiting time = 27 ms

**Average Turnaround Time:** (24 + 27 + 30) / 3 = 27 ms
**Average Waiting Time:** (0 + 24 + 27) / 3 = 17 ms

This example demonstrates the "convoy effect" where short processes wait behind long processes, leading to increased waiting times.

**Example 2: SJF Scheduling Analysis**

Consider four processes with arrival times:

- P1: Arrival = 0, Burst = 7
- P2: Arrival = 1, Burst = 4
- P3: Arrival = 2, Burst = 1
- P4: Arrival = 3, Burst = 4

Using non-preemptive SJF:

At time 0, only P1 is available → Execute P1 (0-7)
At time 7, P2, P3, P4 are all available → Select shortest: P3 (burst = 1) → Execute P3 (7-8)
At time 8, P2 and P4 available → Select P2 (burst = 4) → Execute P2 (8-12)
At time 12, P4 remaining → Execute P4 (12-16)

**Turnaround Times:**

- P1: 7 - 0 = 7
- P2: 12 - 1 = 11
- P3: 8 - 2 = 6
- P4: 16 - 3 = 13

**Average Turnaround Time:** (7 + 11 + 6 + 13) / 4 = 9.25 ms

**Average Waiting Time:**

- P1: 7 - 7 = 0
- P2: 11 - 4 = 7
- P3: 6 - 1 = 5
- P4: 13 - 4 = 9

**Average Waiting Time:** (0 + 7 + 5 + 9) / 4 = 5.25 ms

**Example 3: Round Robin Time Quantum Analysis**

Consider three processes with burst times: P1 = 10, P2 = 5, P3 = 8, all arriving at time 0. Using Round Robin with time quantum q = 4:

**Execution Timeline:**

- Time 0-4: P1 executes (remaining: 6)
- Time 4-5: P2 executes (remaining: 1)
- Time 5-8: P3 executes (remaining: 4)
- Time 8-10: P1 executes (remaining: 2)
- Time 10-11: P2 executes (remaining: 0) → P2 completes
- Time 11-14: P3 executes (remaining: 0) → P3 completes
- Time 14-16: P1 executes (remaining: 0) → P1 completes

**Completion Times:** P1 = 16, P2 = 11, P3 = 14
**Turnaround Times:** P1 = 16, P2 = 11, P3 = 14
**Waiting Times:** P1 = 6, P2 = 6, P3 = 6

All processes have equal waiting time (6 ms), demonstrating Round Robin's fairness. Note that with smaller time quantum, context switches increase but response time improves.

## Exam Tips

1. **Understand the difference between scheduling levels:** Remember that long-term scheduler controls degree of multiprogramming, short-term scheduler decides which process runs, and medium-term scheduler handles swapping.

2. **Know scheduling criteria trade-offs:** No single algorithm optimizes all criteria. For instance, SJF minimizes average waiting time but may cause starvation, while Round Robin provides fair allocation but may increase average turnaround time.

3. **Remember the difference between preemptive and non-preemptive:** Preemptive scheduling allows process preemption and is suitable for time-sharing systems, while non-preemptive is simpler and used in batch systems.

4. **Practice numerical problems:** Most exam questions involve calculating turnaround time, waiting time, and completion time for different scheduling algorithms like FCFS, SJF, and Round Robin.

5. **Understand context switch overhead:** Remember that context switch time is pure overhead and affects scheduling efficiency. Consider this when comparing algorithms.

6. **Starvation vs. Aging:** Starvation occurs when a low-priority process never gets CPU time. Aging is the technique of increasing process priority over time to prevent starvation.

7. **Time quantum selection in Round Robin:** A very small time quantum increases context switches and overhead, while a very large time quantum degenerates to FCFS. The optimal quantum balances responsiveness with efficiency.

8. **Real-time scheduling considerations:** In real-time systems, schedulability analysis becomes crucial. Rate Monotonic and Earliest Deadline First are commonly analyzed approaches.

9. **Remember key formulas:**

- Turnaround Time = Completion Time - Arrival Time
- Waiting Time = Turnaround Time - Burst Time
- Response Time = First Response Time - Arrival Time

10. **Understand dispatcher functions:** The dispatcher handles context switching, mode switching, and transferring control to the selected process. Dispatcher latency is a critical performance metric.
