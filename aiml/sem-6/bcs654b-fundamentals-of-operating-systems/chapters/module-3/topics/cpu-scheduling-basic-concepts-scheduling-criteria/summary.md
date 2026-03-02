# **CPU Scheduling: Basic Concepts, Scheduling Criteria, Scheduling Algorithms, Thread Scheduling, Process Synchronization**

## **Basic Concepts**

- **CPU Scheduling**: The process of allocating the CPU to a process for execution.
- **Process**: A program in execution.
- **Thread**: A lightweight process that can be executed concurrently.
- **Context Switching**: The process of switching from one process to another.

## **Scheduling Criteria**

- **Response Time**: The time it takes for a process to complete its execution.
- **Throughput**: The number of processes that can be executed per unit time.
- **Turnaround Time**: The time it takes for a process to complete its execution, including waiting time.
- **Wait Time**: The time a process waits for the CPU to be available.

## **Scheduling Algorithms**

- **First-Come-First-Served (FCFS)**: The process with the earliest arrival time gets the CPU first.
- **Shortest Job First (SJF)**: The process with the shortest execution time gets the CPU first.
- **Priority Scheduling**: The process with the highest priority gets the CPU first.
- **Round Robin (RR)**: Each process gets a fixed time slice (called a time quantum) before being preempted.

## **Thread Scheduling**

- **Thread Scheduling**: The process of allocating the CPU to a thread for execution.
- **Thread Priority**: The priority of a thread, which determines its scheduling order.

## **Process Synchronization**

- **Synchronization**: The process of coordinating the actions of multiple processes to avoid conflicts.
- **Mutual Exclusion**: A condition where only one process can access a shared resource at a time.
- **Mutual Exclusion Test**: A test to determine if a process can access a shared resource.

## **Important Formulas and Definitions**

- **Waiting Time**: `WT = T - CT`, where `WT` is the waiting time, `T` is the total execution time, and `CT` is the context switching time.
- **Turnaround Time**: `TT = T + WT`, where `TT` is the turnaround time, `T` is the total execution time, and `WT` is the waiting time.
- **CPU Utilization**: `CPU Utilization = (Total CPU Time)/(Total Time)`, where `Total CPU Time` is the total time spent executing processes, and `Total Time` is the total time spent executing all processes.
- **Theorem**: **"The waiting time of a process is less than or equal to its average response time."**

This summary should provide a comprehensive overview of the key concepts, criteria, algorithms, and formulas related to CPU scheduling and process synchronization.
