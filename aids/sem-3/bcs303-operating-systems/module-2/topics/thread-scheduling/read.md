# Thread Scheduling


## Table of Contents

- [Thread Scheduling](#thread-scheduling)
- [Introduction](#introduction)
- [Core Concepts of Thread Scheduling](#core-concepts-of-thread-scheduling)
  - [1. Scheduling Queues](#1-scheduling-queues)
  - [2. The Scheduler & Dispatcher](#2-the-scheduler--dispatcher)
  - [3. Scheduling Criteria](#3-scheduling-criteria)
  - [4. Preemptive vs. Non-Preemptive Scheduling](#4-preemptive-vs-non-preemptive-scheduling)
- [Common Scheduling Algorithms](#common-scheduling-algorithms)
  - [First-Come, First-Served (FCFS)](#first-come-first-served-fcfs)
  - [Shortest-Job-First (SJF) / Shortest-Remaining-Time-First (SRTF)](#shortest-job-first-sjf--shortest-remaining-time-first-srtf)
  - [Priority Scheduling](#priority-scheduling)
  - [Round-Robin (RR) Scheduling](#round-robin-rr-scheduling)
- [Key Points & Summary](#key-points--summary)

## Introduction

In a modern operating system, the CPU is a valuable resource that must be shared among multiple threads (the fundamental units of CPU utilization). Thread Scheduling is the core function of the OS that decides which of the many ready-to-run threads gets to use the CPU core(s) next. Effective scheduling is crucial for ensuring fairness, responsiveness, and optimal system performance, especially in multi-threaded and multi-core environments.

## Core Concepts of Thread Scheduling

### 1. Scheduling Queues

The OS maintains several queues to manage threads throughout their lifecycle:

- **Ready Queue:** A list of all threads that are resident in memory, ready, and waiting to execute on a CPU core.
- **Wait Queue(s):** A set of queues (e.g., for I/O devices) where threads reside when they are waiting for a specific event (like I/O completion) before they can continue.

The act of scheduling involves selecting a thread from the **ready queue** and allocating the CPU to it.

### 2. The Scheduler & Dispatcher

- **Scheduler (Long-Term & Short-Term):** The module of the OS that selects the next thread to be executed. The **short-term scheduler** (or CPU scheduler) is invoked very frequently (every few milliseconds) and makes the immediate decision on thread switching.
- **Dispatcher:** The module that gives control of the CPU to the thread selected by the short-term scheduler. Its functions include:
  _ Context switching (switching from one thread to another).
  _ Switching to user mode. \* Jumping to the proper location in the user program to resume execution.
  The time it takes for the dispatcher to stop one thread and start another is called the **dispatch latency**.

### 3. Scheduling Criteria

A good scheduling algorithm is chosen based on the following criteria:

- **CPU Utilization:** Keep the CPU as busy as possible (maximize % usage).
- **Throughput:** Maximize the number of threads completed per unit time.
- **Turnaround Time:** Minimize the total time taken from a thread's submission to its completion (finish time - arrival time).
- **Waiting Time:** Minimize the total time a thread spends waiting in the ready queue.
- **Response Time:** Minimize the time from the submission of a request until the first response is produced (critical for interactive systems).

### 4. Preemptive vs. Non-Preemptive Scheduling

- **Non-Preemptive Scheduling:** Once a thread is allocated the CPU, it keeps it until it terminates, voluntarily blocks (e.g., for I/O), or yields the CPU. The scheduler cannot force it to give up the CPU.
- **Preemptive Scheduling:** The OS can interrupt a currently running thread, save its context, and switch the CPU to another thread. This is essential for modern time-sharing systems to prevent a single thread from monopolizing the CPU. It requires careful handling of shared data to avoid race conditions.

## Common Scheduling Algorithms

### First-Come, First-Served (FCFS)

- **Concept:** The simplest algorithm; threads are executed in the order they arrive in the ready queue (like a FIFO queue).
- **Example:** If threads P1 (burst time 24ms), P2 (burst time 3ms), and P3 (burst time 3ms) arrive in that order, P1 runs first for 24ms. The waiting time for P2 is 24ms and for P3 is 27ms. This leads to the **Convoy Effect**, where short threads get stuck behind a long one, increasing average waiting time.
- **Nature:** Non-preemptive.

### Shortest-Job-First (SJF) / Shortest-Remaining-Time-First (SRTF)

- **Concept:** SJF associates each thread with the length of its next CPU burst. The scheduler picks the thread with the smallest next CPU burst.
- **SJF** is the non-preemptive version.
- **SRTF** is the preemptive version. If a new thread arrives with a CPU burst length shorter than the remaining time of the currently executing thread, the new thread preempts the current one.
- **Example:** SRTF minimizes average waiting time but requires knowledge of the next CPU burst length, which is often predicted.
- **Challenge:** It can lead to **starvation** for longer threads.

### Priority Scheduling

- **Concept:** Each thread is assigned a priority (could be internal or external). The CPU is allocated to the thread with the highest priority (e.g., smallest integer = highest priority).
- **Preemptive:** A new higher-priority thread can preempt a lower-priority one.
- **Non-preemptive:** The running thread finishes its burst even if a higher-priority one arrives.
- **Problem:** Can lead to **indefinite blocking** or starvation of low-priority threads. A common solution is **aging**—gradually increasing the priority of threads that wait for a long time.

### Round-Robin (RR) Scheduling

- **Concept:** Designed specifically for time-sharing systems. Each thread gets a small unit of CPU time, called a **time quantum** or time slice (typically 10-100ms). After the time slice expires, the thread is preempted and added to the tail of the ready queue.
- **Example:** With a time quantum of 20ms, a thread with a 100ms burst time will need 5 cycles and complete after roughly 100ms (plus context switch overhead). This provides excellent response time for interactive threads.
- **Performance:** Heavily depends on the size of the time quantum. Too large, and it becomes FCFS; too small, and context switch overhead becomes too high.

## Key Points & Summary

- **Purpose:** Thread scheduling is the OS mechanism for allocating CPU time to threads, aiming to maximize CPU use, throughput, and system responsiveness while minimizing waiting, turnaround, and response times.
- **The Scheduler** selects the next thread, and the **Dispatcher** performs the actual context switch.
- **Preemption** allows the OS to take the CPU away from a running thread, which is vital for interactive systems.
- **Common Algorithms:**
- **FCFS:** Simple but can cause high waiting times (Convoy Effect).
- **SJF/SRTF:** Theoretically optimal for minimizing waiting time but impractical without accurate burst time prediction; can cause starvation.
- **Priority Scheduling:** Flexible but requires a mechanism (aging) to prevent starvation of low-priority threads.
- **Round-Robin:** Excellent for interactive systems; performance depends on choosing a good time quantum.
- The choice of algorithm represents a trade-off between the different scheduling criteria, and no single algorithm is optimal for all scenarios. Modern OSs often use complex, multi-level feedback queue schedulers that combine these basic algorithms.
