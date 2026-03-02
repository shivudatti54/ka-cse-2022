# **CPU Scheduling: Basic Concepts, Scheduling Criteria, Scheduling Algorithms, Thread Scheduling, Process Synchronization**

### Basic Concepts

- **CPU Scheduling**: The process of allocating the CPU to a process or thread.
- **Process**: A program in execution.
- **Thread**: A stream of execution within a process.
- **Time Quantum**: The amount of time allocated to a process or thread before the CPU is switched to another process or thread.

### Scheduling Criteria

- **Priority Scheduling**: Allocates CPU time based on process priority.
- **Round Robin Scheduling**: Allocates CPU time for each process for a fixed time period.
- **Multilevel Feedback Queue Scheduling**: A combination of priority and round robin scheduling.
- **First-Come-First-Served (FCFS) Scheduling**: Allocates CPU time to the process that arrived first.

### Scheduling Algorithms

- **Shortest Job First (SJF) Scheduling**: Allocates CPU time to the process with the shortest execution time.
- **Priority Scheduling (PS) Scheduling**: Allocates CPU time based on process priority.
- **Rate Monotonic Scheduling (RMS) Scheduling**: Allocates CPU time based on process priority and execution time.
- **Earliest Deadline First (EDF) Scheduling**: Allocates CPU time to the process with the earliest deadline.

### Thread Scheduling

- **Thread-Level Scheduling**: Scheduling of threads within a process.
- **Preemption**: The process of forcing a process to yield the CPU to another process.

### Process Synchronization

- **Synchronization**: The process of coordinating access to shared resources.
- **Monitors**: A data structure that allows only one process to access shared resources at a time.
- **Semaphores**: A variable that controls the access to shared resources.

### Important Formulas, Definitions, and Theorems

- **CPU Utilization Formula**: CPU utilization = (Total CPU time / Total time) x 100
- **Turnaround Time Formula**: Turnaround time = Total execution time + Waiting time
- **Thermal Voltage Scaling (TVS)**: A technique to reduce power consumption by reducing CPU voltage.
- **Amdahl's Law**: A law that states the maximum theoretical speedup of a parallel program is limited by the fraction of the program that cannot be parallelized.
