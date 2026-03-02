# CPU Scheduling: Revision Notes

### Basic Concepts

- **CPU Scheduling**: The process of allocating the CPU to a process for execution.
- **Process**: A program in execution.
- **Thread**: A lightweight process that shares the same memory space.
- **Time Quanta**: The minimum time interval for which the CPU is allocated to a process.

### Scheduling Criteria

- **Priority Scheduling**: Assigns higher priority to processes with higher priorities.
- **Round Robin Scheduling**: Allocates the CPU to each process for a fixed time quanta.
- **Shortest Job First (SJF)**: Schedules processes based on their execution time.
- **Highest Response Time (HRT)**: Schedules processes based on their response time.

### Scheduling Algorithms

- **FCFS (First Come First Served)**: Schedules processes in the order they arrive.
- **SJF (Shortest Job First)**: Schedules processes based on their execution time.
- **Round Robin (RR)**: Allocates the CPU to each process for a fixed time quanta.
- **Priority Scheduling**: Assigns higher priority to processes with higher priorities.

### Thread Scheduling

- **Thread Scheduling**: Schedules threads within a process.
- **Thread Priority**: Sets the priority of a thread.
- **Thread Synchronization**: Ensures that threads access shared resources safely.

### Process Synchronization

- **Synchronization**: Ensures that multiple processes access shared resources safely.
- **Semaphores**: Used to control access to shared resources.
- **Monitors**: Used to protect shared resources from concurrent access.
- **Mutual Exclusion**: Ensures that only one process can access a shared resource at a time.

### Important Formulas and Definitions

- **CPU Utilization**: (Total CPU time / Total time) x 100
- **Average Response Time**: Average time taken by a process to complete.
- **Average Turnaround Time**: Average time taken by a process to complete, including waiting time.
- **Turnaround Time**: Time taken by a process to complete, including waiting time.
- **Waiting Time**: Time a process spends waiting in the ready queue.

### Theorems

- **Holt's Theorem**: Sum of waiting time and turnaround time is equal to the total execution time.
- **Jackson's Theorem**: Maximum throughput of a multi-server queue is achieved when the servers are served in the order of their service rates.
