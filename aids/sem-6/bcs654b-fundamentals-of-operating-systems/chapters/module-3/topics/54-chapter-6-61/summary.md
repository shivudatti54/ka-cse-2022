# **5.4 Chapter 6: 6.1 Fundamentals of Operating Systems Revision Notes**

### Overview

- Operating System (OS) is a software that manages computer hardware and software resources
- OS provides a platform for running applications and services

### Key Concepts

- **Process**: A program in execution
- **Thread**: A lightweight process that shares resources with other threads in the same process
- **Thread Scheduling Algorithm**:
  - First-Come-First-Served (FCFS)
  - Shortest Job First (SJF)
  - Priority Scheduling
- **Process Scheduling Algorithm**:
  - FCFS
  - SJF
  - Round Robin (RR)
  - Priority Scheduling
- **Memory Management**:
  - Virtual Memory
  - Page Replacement Algorithms (LRU, FIFO, Optimal)

### Important Formulas and Definitions

- **CPU Utilization**: (Number of processes executing / Total number of processes)
- **Turnaround Time**: Time taken to complete a job
- **Waiting Time**: Time spent waiting for a process to be executed
- **Burst Time**: Time taken by a process to complete its execution
- **Priority Inversion**: A situation where a lower-priority process is executing while a higher-priority process is waiting

### Theorems

- **Job Scheduling Theorem**: The optimal scheduling algorithm depends on the nature of the jobs (e.g., burst time, priority)
- **Resource Allocation Theorem**: The optimal allocation of resources depends on the availability of resources and the number of processes

### Quick Revision Tips

- Understand the difference between process and thread
- Familiarize yourself with common thread scheduling and process scheduling algorithms
- Review memory management concepts, including virtual memory and page replacement algorithms
- Practice calculating CPU utilization, turnaround time, waiting time, and burst time
