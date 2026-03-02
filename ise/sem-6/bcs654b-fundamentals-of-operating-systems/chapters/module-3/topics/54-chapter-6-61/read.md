# **FUNDAMENTALS OF OPERATING SYSTEMS**

## **Module: @#@10012025**

## **Topic: 5.4 Chapter 6: 6.1**

### 6.1 Process Scheduling

Process scheduling is the discipline of allocating a set of processes to various time slices, known as time quanta or time slices, within a given time period. The goal of process scheduling is to optimize the performance of the system by allocating sufficient CPU time to each process, minimizing context switching overhead, and maximizing overall system throughput.

#### Types of Process Scheduling Algorithms

There are two primary types of process scheduling algorithms:

- **Shortest Job First (SJF) scheduling algorithm**: This algorithm schedules the process with the shortest execution time first. The SJF algorithm is a non-preemptive algorithm, meaning that once a process is scheduled, it will run until it completes.
- **Round Robin (RR) scheduling algorithm**: This algorithm schedules each process for a fixed time slice (time quantum) before moving on to the next process. The RR algorithm is a preemptive algorithm, meaning that a process can be interrupted and another process can be scheduled at any time.

#### Characteristics of Process Scheduling Algorithms

Here are some key characteristics of process scheduling algorithms:

- **Preemption**: The ability of a process to be interrupted and another process scheduled at any time.
- **Context switching**: The process of switching from one process to another.
- **CPU burst**: The actual time spent by a process executing on the CPU.
- **Turnaround time**: The total time a process spends from its arrival to its completion.
- **Waiting time**: The time a process spends waiting in the system before it is scheduled.

#### Advantages and Disadvantages of Process Scheduling Algorithms

Here are some advantages and disadvantages of process scheduling algorithms:

| Algorithm | Advantages                       | Disadvantages                                              |
| --------- | -------------------------------- | ---------------------------------------------------------- |
| SJF       | 1. Minimizes waiting time        | 1. Can result in starvation (a process is never scheduled) |
| RR        | 1. Can result in fair scheduling | 1. Can result in overhead due to context switching         |

#### Example of Process Scheduling

Suppose we have three processes: P1, P2, and P3, with execution times of 10, 5, and 8 units, respectively. We will schedule these processes using both SJF and RR algorithms.

**SJF Scheduling**

1.  P1 (10 units) is scheduled first.
2.  P2 (5 units) is scheduled next.
3.  P3 (8 units) is scheduled last.

**RR Scheduling**

1.  P1 (10 units) is scheduled first with a time quantum of 5 units.
2.  P1 executes for 5 units and is preempted.
3.  P2 (5 units) is scheduled next with a time quantum of 5 units.
4.  P2 executes for 5 units and is preempted.
5.  P3 (8 units) is scheduled next with a time quantum of 5 units.
6.  P3 executes for 5 units and is preempted.
7.  P3 executes for the remaining 3 units.

The SJF algorithm results in a shorter turnaround time for P3, while the RR algorithm results in a fairer scheduling.

### Key Concepts

- **Process scheduling**: The discipline of allocating a set of processes to various time slices within a given time period.
- **SJF scheduling algorithm**: A non-preemptive algorithm that schedules the process with the shortest execution time first.
- **RR scheduling algorithm**: A preemptive algorithm that schedules each process for a fixed time slice (time quantum) before moving on to the next process.
- **Preemption**: The ability of a process to be interrupted and another process scheduled at any time.
- **Context switching**: The process of switching from one process to another.
- **CPU burst**: The actual time spent by a process executing on the CPU.
- **Turnaround time**: The total time a process spends from its arrival to its completion.
- **Waiting time**: The time a process spends waiting in the system before it is scheduled.

### Practice Questions

1.  What is the primary goal of process scheduling?
2.  What is the difference between SJF and RR scheduling algorithms?
3.  What is the advantage of using the RR scheduling algorithm?
4.  What is the disadvantage of using the SJF scheduling algorithm?
5.  What is context switching, and why is it an important consideration in process scheduling?

### References

- "Operating System Concepts" by Abraham Silberschatz, Peter Baer Galvin, and Greg Gagne
- "Operating System Design and Implementation" by Andrew S. Tanenbaum and Maarten van Steen
