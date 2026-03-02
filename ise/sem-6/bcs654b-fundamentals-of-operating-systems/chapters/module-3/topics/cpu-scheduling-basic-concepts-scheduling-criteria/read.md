# **CPU Scheduling: Basic Concepts, Scheduling Criteria, Scheduling Algorithms, Thread Scheduling, Process Synchronization: Synchronization - The Critical**

## **Introduction**

CPU scheduling is a critical component of an operating system that determines the order in which processes are executed by the CPU. It ensures that the system's resources are utilized efficiently and that each process gets a fair share of the CPU time. In this module, we will explore the basic concepts, scheduling criteria, scheduling algorithms, thread scheduling, and process synchronization.

## **Basic Concepts**

- **Process**: A process is a program in execution, which consists of a set of instructions (program) and data.
- **CPU**: The Central Processing Unit (CPU) is the brain of the computer, responsible for executing instructions.
- **Time Slice**: Also known as time quantum, it is the time allocated to a process before the CPU switches to another process.
- **Ready Queue**: A data structure that stores processes waiting to be executed by the CPU.

## **Scheduling Criteria**

- **FCFS (First-Come-First-Served)**: The process that arrives first in the ready queue is executed first.
- **SJF (Shortest-Job-First)**: The process with the shortest execution time is executed first.
- **Priority Scheduling**: Processes are assigned priorities, and the process with the highest priority is executed first.
- **Round Robin**: Each process gets a fixed time slice (time quantum) before the CPU switches to another process.
- **Shortest Remaining Time First (SRTF)**: The process with the shortest remaining execution time is executed first.

## **Scheduling Algorithms**

### FCFS Scheduling Algorithm

- **Working:**
  - The process that arrives first in the ready queue is executed first.
  - The CPU executes the process until it completes its execution or reaches a time slice.
- **Example:**
  - Suppose we have three processes: P1, P2, and P3, with execution times 10, 5, and 7 units respectively.
  - P1 arrives first and is executed until it completes its execution (10 units).
  - Then, P2 arrives and is executed until it completes its execution (5 units).
  - Finally, P3 arrives and is executed until it completes its execution (7 units).

### SJF Scheduling Algorithm

- **Working:**
  - The process with the shortest execution time is executed first.
  - The CPU executes the process until it completes its execution or reaches a time slice.
- **Example:**
  - Suppose we have three processes: P1, P2, and P3, with execution times 10, 5, and 7 units respectively.
  - P2 has the shortest execution time and is executed first.
  - Then, P1 is executed until it completes its execution (10 units).
  - Finally, P3 is executed until it completes its execution (7 units).

### Priority Scheduling Algorithm

- **Working:**
  - Processes are assigned priorities, and the process with the highest priority is executed first.
  - The CPU executes the process until it completes its execution or reaches a time slice.
- **Example:**
  - Suppose we have three processes: P1, P2, and P3, with priorities 3, 2, and 1 respectively.
  - P1 has the highest priority and is executed first.
  - Then, P2 is executed until it completes its execution (5 units).
  - Finally, P3 is executed until it completes its execution (7 units).

### Round Robin Scheduling Algorithm

- **Working:**
  - Each process gets a fixed time slice (time quantum) before the CPU switches to another process.
  - The CPU executes the process until it completes its execution or reaches the time slice.
- **Example:**
  - Suppose we have three processes: P1, P2, and P3, with time slices 10, 8, and 12 units respectively.
  - P1 is executed for 10 units and then switched to P2.
  - P2 is executed for 8 units and then switched to P3.
  - P3 is executed for 12 units and then switched back to P1.

### SRTF Scheduling Algorithm

- **Working:**
  - The process with the shortest remaining execution time is executed first.
  - The CPU executes the process until it completes its execution or reaches a time slice.
- **Example:**
  - Suppose we have three processes: P1, P2, and P3, with execution times 10, 5, and 7 units respectively.
  - P2 has the shortest remaining execution time and is executed first.
  - Then, P1 is executed until it completes its execution (10 units).
  - Finally, P3 is executed until it completes its execution (7 units).

## **Thread Scheduling**

Thread scheduling is similar to process scheduling, but with some key differences:

- **Thread**: A thread is a lightweight process that shares the same memory space as the parent process.
- **Thread Scheduling Algorithm**: The thread scheduling algorithm is similar to the process scheduling algorithm, but with a few modifications.
- **Thread Priority**: Each thread has its own priority, which determines the order in which it is executed.

## **Process Synchronization**

Process synchronization is the process of coordinating the actions of multiple processes in a system. It ensures that the system's resources are utilized efficiently and that each process gets a fair share of the CPU time.

- **Mutual Exclusion**: A process can only access a shared resource at a time.
- **Mutual Exclusion Protocols**: There are several protocols that can be used to implement mutual exclusion, including semaphores and monitors.
- **Semaphores**: A semaphore is a variable that controls the access to a shared resource.
- **Monitors**: A monitor is a more complex synchronization construct that can be used to implement mutual exclusion.

## **Conclusion**

CPU scheduling is a critical component of an operating system that determines the order in which processes are executed by the CPU. Understanding the basic concepts, scheduling criteria, scheduling algorithms, thread scheduling, and process synchronization is essential for designing efficient and effective operating systems.
