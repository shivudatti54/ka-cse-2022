# Scheduling Algorithms


## Table of Contents

- [Scheduling Algorithms](#scheduling-algorithms)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Terminology](#basic-terminology)
  - [Types of Schedulers](#types-of-schedulers)
  - [The Dispatcher](#the-dispatcher)
- [Scheduling Algorithms](#scheduling-algorithms)
  - [First-Come-First-Served (FCFS) Scheduling](#first-come-first-served-fcfs-scheduling)
  - [Shortest Job First (SJF) Scheduling](#shortest-job-first-sjf-scheduling)
  - [Priority Scheduling](#priority-scheduling)
  - [Round Robin (RR) Scheduling](#round-robin-rr-scheduling)
  - [Multilevel Queue Scheduling](#multilevel-queue-scheduling)
  - [Multilevel Feedback Queue Scheduling](#multilevel-feedback-queue-scheduling)
- [Examples](#examples)
  - [Example 1: FCFS Scheduling](#example-1-fcfs-scheduling)
  - [Example 2: SJF Scheduling (Non-preemptive)](#example-2-sjf-scheduling-non-preemptive)
  - [Example 3: Round Robin Scheduling](#example-3-round-robin-scheduling)
- [Exam Tips](#exam-tips)

## Introduction

CPU scheduling is one of the fundamental functions of any operating system. In a computer system, multiple processes compete for the limited CPU time available. The operating system must decide which process gets access to the CPU, for how long, and in what order. This decision-making process is governed by scheduling algorithms. Understanding these algorithms is crucial for any computer science professional because they directly impact system performance, responsiveness, and overall efficiency.

In modern computing environments, from personal computers to massive data centers, scheduling algorithms determine how efficiently hardware resources are utilized. A well-designed scheduling algorithm can significantly improve system throughput, reduce waiting time for users, and ensure fair distribution of CPU time among competing processes. This topic explores the various scheduling algorithms used in operating systems, their implementation details, performance characteristics, and practical applications in real-world systems.

The study of scheduling algorithms involves understanding both theoretical foundations and practical considerations. We will examine algorithms ranging from simple first-come-first-served approaches to more sophisticated multilevel queue scheduling schemes. Each algorithm has its strengths and weaknesses, and operating system designers must carefully choose based on system requirements and workload characteristics.

## Key Concepts

### Basic Terminology

CPU Burst and I/O Burst: A process execution consists of alternating periods of CPU activity (CPU burst) and I/O activity (I/O burst). When a process is executing on the CPU, it is in a CPU burst. When it waits for I/O operations to complete, it is in an I/O burst. Understanding the CPU-I/O burst cycle is essential for effective scheduling.

CPU Burst Time: The total time a process spends executing on the CPU. This is a critical parameter used by many scheduling algorithms to make scheduling decisions.

Arrival Time: The time at which a process enters the ready queue and becomes eligible for CPU execution.

Completion Time: The time at which a process finishes its execution completely.

Turnaround Time: The total time from process arrival to completion, calculated as Completion Time minus Arrival Time. This includes actual CPU time, waiting time, and I/O time.

Waiting Time: The total time a process spends in the ready queue waiting for CPU allocation. This is calculated as Turnaround Time minus Actual CPU Burst Time.

Response Time: The time from process arrival to the first time it gets CPU allocation. This is particularly important for interactive systems.

Throughput: The number of processes completed per unit time. Higher throughput indicates better system efficiency.

CPU Utilization: The percentage of time the CPU is busy executing processes. Ideally, this should be as close to 100 percent as possible.

### Types of Schedulers

Long-term Scheduler: Also known as the admission scheduler, it controls the degree of multiprogramming by deciding which processes are admitted to the system from the job pool. It selects processes from the mass storage device (where they are stored) and loads them into memory for execution. In modern desktop systems, this scheduler may be less prominent as most processes are started directly by users.

Short-term Scheduler: Also called the CPU scheduler, it decides which of the ready processes should get CPU allocation next. This scheduler operates frequently and must be very fast since it makes decisions every few milliseconds.

Medium-term Scheduler: This scheduler can temporarily remove processes from memory, store them on secondary storage, and bring them back later. This technique, called swapping, helps manage memory more efficiently and is particularly useful when memory is overcommitted.

### The Dispatcher

The dispatcher is the component that gives control of the CPU to the process selected by the short-term scheduler. It performs the following functions:

Context Switch: Switching the CPU to the new process involves saving the state of the previously running process and loading the state of the selected process.

Switching to User Mode: Returning control to the user program by switching the program counter to the appropriate location in the user program.

The dispatcher should be as fast as possible because it is invoked during every context switch. Dispatch latency is an important consideration in real-time and interactive systems.

## Scheduling Algorithms

### First-Come-First-Served (FCFS) Scheduling

FCFS is the simplest scheduling algorithm. Processes are served in the order they arrive in the ready queue. The first process to arrive gets CPU allocation first, and other processes wait until it completes.

Characteristics: FCFS is non-preemptive, meaning once a process gets the CPU, it continues executing until it completes its CPU burst or voluntarily yields for I/O. This can lead to the convoy effect where short processes wait behind long processes.

Advantages: Simple to implement using a FIFO (First In First Out) queue. No starvation as every process eventually gets CPU time.

Disadvantages: Poor performance in terms of average waiting time. Short processes may have to wait for long processes to complete.

### Shortest Job First (SJF) Scheduling

SJF selects the process with the smallest CPU burst time for next execution. When multiple processes have the same burst time, FCFS is used as a tie-breaker.

Characteristics: SJF can be either preemptive or non-preemptive. The preemptive version, called Shortest Remaining Time First (SRTF), preempts the currently running process if a new process arrives with a CPU burst shorter than the remaining time of the running process.

Advantages: SJF provides optimal average waiting time for a given set of processes. It minimizes the average turnaround time.

Disadvantages: Cannot be implemented in practice because CPU burst times are not known in advance. Starvation can occur for long processes if short processes keep arriving.

### Priority Scheduling

In priority scheduling, each process is assigned a priority number. The CPU is allocated to the ready process with the highest priority (or lowest number, depending on convention). When multiple processes have the same priority, FCFS is used.

Characteristics: Can be either preemptive or non-preemptive. In preemptive priority scheduling, if a higher priority process arrives, it immediately preempts the currently running process.

Advantages: Important processes can be given higher priority to ensure timely execution.

Disadvantages: Starvation is a major issue—low priority processes may never get CPU time if higher priority processes keep arriving. Aging is a technique used to combat starvation, where the priority of a waiting process gradually increases over time.

### Round Robin (RR) Scheduling

Round Robin is designed specifically for time-sharing systems. Each process gets a fixed time slice called a time quantum. Processes are cycled through in a circular manner.

Characteristics: RR is preemptive. After a process uses its time quantum, it is moved to the back of the ready queue, and the next process gets the CPU. The time quantum is typically between 10 to 100 milliseconds.

Advantages: No starvation. Provides fair CPU time distribution among all processes. Good response time for interactive systems.

Disadvantages: Higher average waiting time than SJF for light workloads. Performance depends heavily on the time quantum size. If the quantum is too small, excessive context switching occurs. If too large, response time suffers.

### Multilevel Queue Scheduling

This algorithm partitions the ready queue into multiple separate queues based on process characteristics. Each queue may have its own scheduling algorithm. Common partitions include:

System Processes Queue: For system-level processes, typically using FCFS.
Interactive Processes Queue: For interactive programs, using RR.
Batch Processes Queue: For batch jobs, using FCFS or SJF.

The scheduler first decides which queue to serve, then selects a process from that queue. Queues typically have fixed priorities, meaning processes in higher-priority queues are served first.

Advantages: Different scheduling needs for different process types can be addressed separately.
Disadvantages: Inflexible. Processes cannot move between queues once assigned.

### Multilevel Feedback Queue Scheduling

This is the most sophisticated CPU scheduling algorithm. It extends multilevel queue scheduling by allowing processes to move between queues. Processes that use too much CPU time are moved to lower-priority queues, while processes that wait too long in lower-priority queues can be promoted to higher-priority queues.

Characteristics: The algorithm attempts to balance throughput and response time. New processes enter the highest-priority queue. If a process uses its entire time quantum, it moves down. If a process voluntarily yields before the time quantum expires, it stays in the same queue.

Advantages: Flexible and adaptable. Combines the advantages of many scheduling approaches. Can be tuned to match specific system requirements.

Disadvantages: Complex to implement. Requires careful parameter tuning for optimal performance.

## Examples

### Example 1: FCFS Scheduling

Consider four processes with the following arrival times and CPU burst times:

Process P1: Arrival = 0, Burst = 10
Process P2: Arrival = 1, Burst = 5
Process P3: Arrival = 2, Burst = 8
Process P4: Arrival = 3, Burst = 6

Calculate average waiting time and turnaround time using FCFS.

Solution:
Execution order: P1 → P2 → P3 → P4

P1: Waiting Time = 0, Turnaround Time = 10 - 0 = 10
P2: Waiting Time = 10 - 1 = 9, Turnaround Time = 9 + 5 = 14
P3: Waiting Time = 15 - 2 = 13, Turnaround Time = 13 + 8 = 21
P4: Waiting Time = 23 - 3 = 20, Turnaround Time = 20 + 6 = 26

Average Waiting Time = (0 + 9 + 13 + 20) / 4 = 42 / 4 = 10.5
Average Turnaround Time = (10 + 14 + 21 + 26) / 4 = 71 / 4 = 17.75

### Example 2: SJF Scheduling (Non-preemptive)

Using the same processes, calculate using SJF (non-preemptive):

Process P1: Arrival = 0, Burst = 10
Process P2: Arrival = 1, Burst = 5
Process P3: Arrival = 2, Burst = 8
Process P4: Arrival = 3, Burst = 6

Solution:
At time 0: Only P1 is available → Execute P1
At time 10: P2, P3, P4 are available → Select shortest burst = P4 (6)
At time 16: P2 and P3 are available → Select shortest burst = P2 (5)
At time 21: P3 is available → Execute P3

Execution order: P1 → P4 → P2 → P3

P1: Waiting Time = 0, Turnaround = 10 - 0 = 10
P4: Waiting Time = 10 - 3 = 7, Turnaround = 7 + 6 = 13
P2: Waiting Time = 16 - 1 = 15, Turnaround = 15 + 5 = 20
P3: Waiting Time = 21 - 2 = 19, Turnaround = 19 + 8 = 27

Average Waiting Time = (0 + 7 + 15 + 19) / 4 = 41 / 4 = 10.25
Average Turnaround Time = (10 + 13 + 20 + 27) / 4 = 70 / 4 = 17.5

Notice the improvement in average waiting time and turnaround time compared to FCFS.

### Example 3: Round Robin Scheduling

Consider the same processes with Time Quantum = 4:

Process P1: Arrival = 0, Burst = 10
Process P2: Arrival = 1, Burst = 5
Process P3: Arrival = 2, Burst = 8
Process P4: Arrival = 3, Burst = 6

Solution:
Time 0-4: P1 executes (remaining burst = 6)
Time 4: P2 arrives, P1 moved to queue end
Time 4-8: P2 executes (remaining burst = 1)
Time 8: P3 and P4 have arrived, P2 has completed
Time 8-12: P3 executes (remaining burst = 4)
Time 12: P4 waits, P1 resumes
Time 12-16: P1 executes (remaining burst = 2)
Time 16: P4 executes
Time 16-20: P4 executes (remaining burst = 2)
Time 20: P3 executes
Time 20-24: P3 executes (completed)
Time 24: P1 executes
Time 24-26: P1 executes (completed)
Time 26: P4 executes
Time 26-28: P4 executes (completed)

Now calculate waiting times:
P1: 4 + (12-8) = 8
Wait, let me recalculate systematically:

P1: Waits from 4-8, then 16-20, then 24-26 = 4 + 4 + 2 = 10
P2: Waits from 8-12 = 4
P3: Waits from 12-16, then 20-24 = 4 + 4 = 8
P4: Waits from 8-12, then 20-24, then 26-28 = 4 + 4 + 2 = 10

Average Waiting Time = (10 + 4 + 8 + 10) / 4 = 32 / 4 = 8

Average Turnaround Time:
P1: 10 + 8 = 18
P2: 5 + 4 = 9
P3: 8 + 8 = 16
P4: 6 + 10 = 16
Average = (18 + 9 + 16 + 16) / 4 = 59 / 4 = 14.75

This example demonstrates how RR provides better average waiting time than FCFS for this particular set of processes.

## Exam Tips

Understanding scheduling algorithms requires both theoretical knowledge and problem-solving skills. Here are essential points for exam preparation:

First, memorize the definitions of all timing metrics: turnaround time, waiting time, response time, and throughput. Questions frequently ask for calculations involving these metrics, and understanding their formulas is essential. Remember that turnaround time equals completion time minus arrival time, while waiting time equals turnaround time minus actual CPU burst time.

Second, be able to distinguish between preemptive and non-preemptive scheduling. FCFS and non-preemptive SJF are non-preemptive, while RR and preemptive priority scheduling are preemptive. The type of algorithm affects how waiting times are calculated when new processes arrive.

Third, always calculate waiting times carefully in preemptive algorithms. Keep track of when processes enter the ready queue and when they actually get CPU time. Drawing a timeline or Gantt chart is highly recommended for solving scheduling problems.

Fourth, remember that SJF provides optimal average waiting time but cannot be implemented in practice because CPU burst times cannot be known in advance. This is a commonly tested concept in exams.

Fifth, for Round Robin, understand that the time quantum significantly affects performance. A very small quantum increases context switching overhead, while a very large quantum degenerates to FCFS.

Sixth, understand the concept of starvation and how aging helps overcome it. Priority scheduling can cause starvation for low-priority processes, and aging gradually increases priority of waiting processes.

Seventh, for multilevel feedback queue scheduling, remember that processes moving between queues is the key feature. Processes using more CPU time move to lower-priority queues, while processes waiting too long move to higher-priority queues.

Eighth, practice numerical problems from previous years. Scheduling algorithm problems are frequently asked in exams, and practice is essential for速度和accuracy in calculations.