# **5.4 Chapter 6: 6.1 - Process Scheduling Algorithms**

## **Introduction**

Process scheduling is a crucial component of an operating system, responsible for allocating system resources to running processes. The goal of process scheduling is to ensure that processes are executed in an efficient and timely manner. In this section, we will explore the different process scheduling algorithms, their characteristics, and examples.

## **Process Scheduling Algorithms**

### 1. First-Come-First-Served (FCFS) Scheduling Algorithm

**Definition:** FCFS scheduling algorithm is a simple and intuitive algorithm that schedules processes in the order they arrive at the ready queue.

**Characteristics:**

- First-come-first-served: processes are executed in the order they arrive at the ready queue.
- No consideration is given to process priority or burst time.
- Can lead to poor performance if processes have varying burst times.

**Example:** Suppose we have three processes: P1, P2, and P3, with arrival times 0, 2, and 4 seconds, respectively, and burst times 3, 2, and 1 second, respectively. If we apply FCFS scheduling, the order of execution will be P1, P2, P3.

### 2. Shortest Job First (SJF) Scheduling Algorithm

**Definition:** SJF scheduling algorithm is a variation of FCFS that schedules processes based on their burst times.

**Characteristics:**

- Shortest job first: processes with shorter burst times are executed first.
- No consideration is given to process priority.
- Can lead to poor performance if processes have varying burst times.

**Example:** Using the same example as above, if we apply SJF scheduling, the order of execution will be P3, P2, P1.

### 3. Priority Scheduling Algorithm

**Definition:** Priority scheduling algorithm is a scheduling algorithm that assigns a priority to each process based on its characteristics.

**Characteristics:**

- Priority-based scheduling: processes are executed based on their priority.
- Can be based on various criteria such as burst time, I/O time, or priority value.
- Can lead to better performance if processes have different priorities.

**Example:** Suppose we have three processes: P1, P2, and P3, with priority values 3, 2, and 1, respectively. If we apply priority scheduling with priority values, the order of execution will be P1, P2, P3.

### 4. Round-Robin (RR) Scheduling Algorithm

**Definition:** RR scheduling algorithm is a time-sliced scheduling algorithm that assigns a fixed time slice to each process.

**Characteristics:**

- Time-sliced scheduling: processes are executed for a fixed time slice.
- Each process gets an equal time slice.
- Can lead to better performance if processes have varying burst times.

**Example:** Suppose we have three processes: P1, P2, and P3, with burst times 3, 2, and 1 second, respectively. If we apply RR scheduling with a time slice of 2 seconds, the order of execution will be P1, P2, P3, P1, P2, P3, ...

### 5. Multi-Level Feedback Queue (MLFQ) Scheduling Algorithm

**Definition:** MLFQ scheduling algorithm is a variation of RR scheduling that uses multiple queues with different time slices.

**Characteristics:**

- Multiple queues: multiple queues with different time slices are used.
- Each queue has a different priority and time slice.
- Can lead to better performance if processes have varying burst times.

**Example:** Suppose we have three processes: P1, P2, and P3, with burst times 3, 2, and 1 second, respectively. If we apply MLFQ scheduling with three queues (high, medium, and low priority), the order of execution will be P1 (high priority), P2 (medium priority), P3 (low priority), ...

## **Comparison of Process Scheduling Algorithms**

| Algorithm | Characteristics           | Advantages                                                            | Disadvantages                                          |
| --------- | ------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------ |
| FCFS      | First-come-first-served   | Simple to implement                                                   | Poor performance if processes have varying burst times |
| SJF       | Shortest job first        | Can lead to better performance if processes have varying burst times  | Poor performance if processes have varying burst times |
| Priority  | Priority-based scheduling | Can lead to better performance if processes have different priorities | Complexity in assigning priority values                |
| RR        | Time-sliced scheduling    | Can lead to better performance if processes have varying burst times  | Complexity in assigning time slices                    |
| MLFQ      | Multiple queues           | Can lead to better performance if processes have varying burst times  | Complexity in managing multiple queues                 |

In conclusion, the choice of process scheduling algorithm depends on the specific requirements of the system, such as the type of processes, the availability of system resources, and the desired performance characteristics.
