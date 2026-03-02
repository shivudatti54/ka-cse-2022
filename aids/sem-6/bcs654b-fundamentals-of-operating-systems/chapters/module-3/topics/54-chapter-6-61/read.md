# **Fundamentals of Operating Systems**

## **Module 1: Introduction to Operating Systems**

### Chapter 6: Process Management

---

#### 6.1 Process Scheduling

---

## **Process Scheduling:**

Process scheduling is the discipline of selecting the next process to be executed by the CPU. It determines how the operating system allocates the CPU time to each process.

## **Types of Process Scheduling:**

- **Preemptive Scheduling:** The operating system preempts the current process to schedule another one.
- **Non-Preemptive Scheduling:** The operating system does not preempt the current process unless it is interrupted by some external event.

## **Process Scheduling Algorithms:**

- **FCFS (First-Come-First-Served):** The process that arrives first is executed first.
- **SJF (Shortest Job First):** The process with the shortest execution time is executed first.
- **HRD (Highest Response Time):** The process with the highest response time is executed first.
- **Priority Scheduling:** The process with the highest priority is executed first.

## **Process Scheduling Example:**

Consider a system with three processes: P1, P2, and P3. The execution times are as follows:

| Process | Execution Time |
| ------- | -------------- |
| P1      | 10 ms          |
| P2      | 5 ms           |
| P3      | 15 ms          |

Using SJF scheduling algorithm:

1.  P2 is executed first because it has the shortest execution time (5 ms).
2.  P1 is executed next because it has the next shortest execution time (10 ms).
3.  P3 is executed last because it has the longest execution time (15 ms).

**Key Concepts:**

- **Process Priority:** A value assigned to a process to determine its relative importance.
- **Process Scheduling Algorithm:** A set of rules that the operating system follows to select the next process to be executed.
- **Process Execution Time:** The time taken by the CPU to execute a process.

## **Real-World Applications:**

Process scheduling is used in various operating systems to manage the execution of processes. For example:

- **Windows:** Uses a priority-based scheduling algorithm to manage process execution.
- **Linux:** Uses a combination of SJF and priority-based scheduling algorithms to manage process execution.

**Key Terms:**

- **Process:** A program in execution.
- **CPU:** Central Processing Unit.
- **Operating System:** A software that manages computer hardware resources.
