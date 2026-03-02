Of course. Here is a comprehensive educational note on "Scheduling Criteria" for  Engineering students, structured as requested.

***

# Module 3: CPU Scheduling - Scheduling Criteria

## 1. Introduction

In a multiprogramming operating system, the CPU is constantly switching between processes. The **scheduler** is the OS component responsible for making this decision. But how does it decide which process to run next? The goal is never arbitrary; it is designed to achieve certain system objectives.

**Scheduling Criteria** are the set of metrics or performance indicators used to evaluate and compare the effectiveness of different CPU scheduling algorithms. They define *what* we want to optimize for in our system. Understanding these criteria is fundamental to analyzing why one scheduling algorithm might be chosen over another for a specific environment (e.g., batch processing, interactive systems, real-time systems).

## 2. Core Concepts of Scheduling Criteria

The criteria can be broadly categorized into two types: those that are user-centric (perceived by the user) and those that are system-centric (focused on efficient resource utilization).

### A. User-Oriented Criteria

These metrics are directly experienced by the user of the system.

1.  **CPU Utilization:** The fraction of time the CPU is busy executing a process. It is the primary measure from the system's perspective. Ideally, we want to keep the CPU as busy as possible (maximize utilization, e.g., 90%+). A scheduling algorithm should avoid leaving the CPU idle when processes are ready to run.

2.  **Throughput:** The number of processes completed per unit time. It measures the overall work done by the system. A high throughput indicates an efficient scheduler. For example, a scheduler that completes 50 processes in a minute has a higher throughput than one that completes only 30.

3.  **Turnaround Time:** The total time taken from when a process *submits* itself for execution until it *completes*. This is a crucial metric for the user. It includes:
    *   Time spent waiting in the ready queue
    *   Time spent executing on the CPU
    *   Time performing I/O operations
    A good scheduling algorithm minimizes the average turnaround time.

4.  **Waiting Time:** The total time a process spends waiting in the **ready queue**. This is the specific time a process is ready to run but is not allocated the CPU. *It is the time spent waiting, not running.* A key goal of scheduling is to minimize the average waiting time.

5.  **Response Time:** Particularly important in **time-sharing** and interactive systems. It is the time from the submission of a request (e.g., a user typing a command) until the first response is produced (e.g., the first output is shown). It does not require the process to complete. Minimizing response time leads to a more responsive, user-friendly system.

### B. System-Oriented Criteria

These are internal metrics important for the system's health and efficiency.

1.  **Fairness:** The scheduler should allocate CPU time to all processes in a fair and non-discriminatory manner. No process should suffer from **starvation**—a situation where a process is denied CPU time indefinitely because other processes are always preferred. A good algorithm ensures every process gets a chance to make progress.

## 3. Examples and Trade-offs

The importance of these criteria varies based on the system environment.

*   **Batch Systems (e.g., processing payroll):** The main goal is to **maximize throughput** and **minimize turnaround time**. Users submitting jobs care about how long the entire job takes, not immediate response.
*   **Interactive Systems (e.g., your laptop):** The most critical metric is **minimizing response time**. A user expects the system to react immediately to clicks or keystrokes. High throughput is still desired but is secondary to responsiveness.
*   **Real-Time Systems (e.g., flight control):** The criteria shift to **meeting deadlines**. The scheduler must guarantee that critical processes get the CPU by their required deadlines, even if it means lower overall throughput or fairness for non-critical tasks.

> **Note:** There is often a **trade-off** between these criteria. For instance, optimizing for minimal average waiting time (like Shortest Job First does) might seem unfair to longer processes, potentially leading to starvation. A scheduler cannot maximize all criteria simultaneously.

## 4. Summary of Key Points

| Criteria | Description | Goal |
| :--- | :--- | :--- |
| **CPU Utilization** | % of time the CPU is busy | Maximize |
| **Throughput** | # of processes completed per unit time | Maximize |
| **Turnaround Time** | Submission to completion time | Minimize |
| **Waiting Time** | Time spent waiting in the ready queue | Minimize |
| **Response Time** | Time from request to first response | Minimize |
| **Fairness** | Equitable CPU allocation | Prevent starvation |

**In essence, scheduling criteria provide the "rules of the game."** They are the measurable goals that a CPU scheduling algorithm is designed to achieve. The choice of which criteria to prioritize directly influences the selection of the scheduling algorithm (e.g., FCFS, SJF, Priority, Round Robin) for a given operating system.