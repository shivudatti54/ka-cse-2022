# Scheduling Criteria in Operating Systems

## Introduction

In a multiprogramming system, the CPU is switched between multiple processes, making the system appear to run many programs simultaneously. The **CPU scheduler** is the component of the operating system responsible for this task. However, the scheduler cannot make decisions arbitrarily. It needs to evaluate and select the next process based on specific measures of system performance. These measures are known as **scheduling criteria**. They are the metrics used to compare and determine the effectiveness of different CPU scheduling algorithms.

## Core Scheduling Criteria

The goal of a good scheduling algorithm is to maximize some criteria at the expense of others, depending on the system's purpose (e.g., batch, interactive, real-time). The most important criteria are:

### 1. CPU Utilization

- **Concept:** This is a measure of how busy the CPU is. It is the percentage of time the CPU is actively executing a process. In a real system, it should range from 40% to 90%. The ultimate goal is to **maximize CPU utilization**.
- **Example:** If the CPU is busy executing processes for 850 ms out of a 1000 ms period, the utilization is 85%.

### 2. Throughput

- **Concept:** Throughput is the number of processes that are completed per unit of time. It is a measure of the total work done by the CPU. For long processes, throughput might be 1 process per hour; for short transactions, it might be 1000 processes per second. The goal is to **maximize throughput**.
- **Example:** If a scheduler completes 50 processes in one minute, its throughput is 50 processes/minute.

### 3. Turnaround Time

- **Concept:** This is a crucial metric from the perspective of a single process. It is the total time taken from when a process **submits** its request to when it **completes** its execution. Turnaround time includes the time spent waiting in the ready queue, executing on the CPU, and performing I/O operations. The goal is to **minimize the average turnaround time**.
- **Example:** A process enters the system at time `t=0`, finishes execution at `t=15` seconds. Its turnaround time is 15 seconds.

### 4. Waiting Time

- **Concept:** Waiting time is a component of turnaround time. It is the total amount of time a process spends waiting in the **ready queue**. A scheduler does not affect the time a process spends running or doing I/O; it only affects the waiting time. Therefore, **minimizing the average waiting time** is a primary focus of most scheduling algorithms.
- **Example:** A process with a total CPU burst of 10 seconds might have a turnaround time of 25 seconds. This means it spent 15 seconds waiting in the ready queue.

### 5. Response Time

- **Concept:** This is particularly important in **time-sharing** and **interactive systems**. It is the time from the submission of a request (e.g., a user pressing 'Enter') to the **first response** produced by the process (not the final output). For an interactive user, a low response time is essential for a good user experience. The goal is to **minimize the average response time**.
- **Example:** In a text editor, the time between a user typing a character and the editor displaying it on the screen must be minimal. This is response time.

## The Trade-off

These criteria often conflict with one another. An algorithm designed to maximize throughput might lead to a high waiting time for short processes. An algorithm minimizing response time might lower CPU utilization. The art of designing a scheduling algorithm lies in striking the right balance for the intended use case.

- **Batch Systems:** Focus on **throughput** and **turnaround time**.
- **Interactive Systems:** Focus on **response time** and **waiting time**.
- **All Systems:** Aim for high **CPU utilization**.

## Key Points & Summary

| **Criterion**       | **Definition**                                             | **Goal** |
| :------------------ | :--------------------------------------------------------- | :------- |
| **CPU Utilization** | Percentage of time the CPU is busy.                        | Maximize |
| **Throughput**      | Number of processes completed per unit time.               | Maximize |
| **Turnaround Time** | Total time from submission to completion of a process.     | Minimize |
| **Waiting Time**    | Total time a process spends waiting in the ready queue.    | Minimize |
| **Response Time**   | Time from submission until the first response is produced. | Minimize |

- Scheduling criteria are the **performance metrics** used to evaluate CPU scheduling algorithms.
- The choice of which criterion to optimize defines the behavior of the scheduler and is dependent on the **type of operating system** (batch, interactive, real-time).
- There is always a **trade-off** between different criteria; improving one often leads to the degradation of another.
- `Waiting Time = Turnaround Time - Total CPU Execution Time`
