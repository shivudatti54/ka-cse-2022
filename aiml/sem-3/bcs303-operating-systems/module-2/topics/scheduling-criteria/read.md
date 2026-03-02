# Scheduling Criteria


## Table of Contents

- [Scheduling Criteria](#scheduling-criteria)
- [Introduction](#introduction)
- [Core Scheduling Criteria](#core-scheduling-criteria)
  - [1. CPU Utilization](#1-cpu-utilization)
  - [2. Throughput](#2-throughput)
  - [3. Turnaround Time](#3-turnaround-time)
  - [4. Waiting Time](#4-waiting-time)
  - [5. Response Time](#5-response-time)
  - [6. Fairness](#6-fairness)
- [Key Points & Summary](#key-points--summary)

## Introduction

In a multiprogramming system, the CPU is often faced with a choice: which process to run next from the ready queue? The part of the operating system that makes this decision is the **CPU scheduler**, and the algorithm it uses is the **scheduling algorithm**. But how do we decide which algorithm is "good"? We evaluate them based on a set of **scheduling criteria**. These criteria are the metrics that define the performance and behavior of a scheduling algorithm, allowing us to compare different policies and choose the one best suited for a specific environment (e.g., batch, interactive, real-time).

## Core Scheduling Criteria

The choice of a scheduling algorithm depends on which of the following criteria we wish to optimize. Different systems prioritize different criteria.

### 1. CPU Utilization

- **Concept:** The primary goal of any OS is to keep the CPU as busy as possible. CPU utilization is the fraction of time the CPU is actively executing a process. It ranges from 0% to 100%. In real systems, it is desirable to keep it high (e.g., 40% for a lightly loaded system, up to 90% for a heavily used one).
- **Analogy:** This is like ensuring a expensive machine in a factory is never idle.

### 2. Throughput

- **Concept:** If the CPU is busy, the work is getting done. Throughput measures the amount of work completed in a unit of time. It is defined as the **number of processes that are completed per time unit**.
- **Example:** If Scheduling Algorithm A completes 10 processes in one hour, and Algorithm B completes 12, then Algorithm B has a higher throughput. This is a crucial measure for batch systems.

### 3. Turnaround Time

- **Concept:** This is a critical measure from the perspective of a single process. It is the total time taken from when a process **submits** itself for execution to when it **completes** (including waiting time in the ready queue, I/O time, and execution time).
- **Formula:** `Turnaround Time = Time of Completion - Time of Submission`
- **Example:** If a process P1 submits at time `t=0` and finishes at time `t=15`, its turnaround time is `15 units`. A good scheduling algorithm minimizes the _average_ turnaround time.

### 4. Waiting Time

- **Concept:** The CPU scheduling algorithm does not affect the amount of time a process spends running or doing I/O; it only affects the time a process spends waiting in the ready queue. **Waiting time** is the sum of all periods a process spends waiting in the ready queue.
- **Key Point:** To minimize waiting time, we need to minimize the time processes spend waiting for the CPU. This is often the primary focus of many scheduling algorithms.

### 5. Response Time

- **Concept:** This is the most important criterion in **time-sharing** and **interactive** systems. It is the time from the submission of a request (e.g., a user pressing 'Enter') to the **first response** produced by the process (not the time to output the entire result).
- **Why it matters:** In an interactive system, a user expects a quick response, even if the total job takes a long time to complete. A process might produce its first output quickly but take a long time to fully complete (good response time, but maybe poor turnaround time).
- **Example:** When you type a command in the terminal, the time until you see the first line of output is the response time.

### 6. Fairness

- **Concept:** A scheduling algorithm must be fair. This means every process should get a fair share of the CPU time. No process should suffer from **starvation**—a situation where a process is indefinitely denied access to the CPU because other processes are always preferred.
- **Example:** A First-Come-First-Serve (FCFS) algorithm is inherently fair. A poorly designed priority-based algorithm might starve low-priority processes if high-priority processes keep arriving.

---

## Key Points & Summary

| Criterion           | Description                                                           | Primary Goal |
| :------------------ | :-------------------------------------------------------------------- | :----------- |
| **CPU Utilization** | Keep the CPU as busy as possible.                                     | Maximize     |
| **Throughput**      | Number of processes completed per time unit.                          | Maximize     |
| **Turnaround Time** | Total time from submission to completion of a process.                | Minimize     |
| **Waiting Time**    | Total time a process spends waiting in the ready queue.               | Minimize     |
| **Response Time**   | Time from submission to the first response (for interactive systems). | Minimize     |
| **Fairness**        | Ensure each process gets a fair share of the CPU; prevent starvation. | Ensure       |

It is impossible to optimize all these criteria simultaneously. For instance, maximizing throughput might sometimes lead to higher response times. The art of designing a scheduling algorithm involves finding the right **trade-off** based on the system's purpose:

- **Batch Systems (e.g., payroll processing):** Focus on throughput and turnaround time.
- **Interactive Systems (e.g., desktops, servers):** Focus on response time and fairness.
- **Real-Time Systems (e.g., robotics, flight control):** Focus on meeting deadlines, often at the expense of other criteria.

Understanding these criteria is the first step to analyzing and comparing specific scheduling algorithms like FCFS, SJF, Priority Scheduling, and Round Robin.
