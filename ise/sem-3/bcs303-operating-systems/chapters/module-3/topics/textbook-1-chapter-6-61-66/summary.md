# Operating Systems

### Chapter 6: Process Management

#### 6.1 Process Concepts

- **Process**: A program in execution
- **Process Scheduling**: Allocating and executing processes
- **Process Communication**: Exchanging data between processes

#### 6.2 Process Scheduling Algorithms

- **FCFS (First-Come-First-Served)**: Scheduling process in the order they arrive
- **SJF (Shortest Job First)**: Scheduling process with the shortest execution time
- **HRD (Highest Response Time Delay)**: Scheduling process with the highest response time
- **Priority Scheduling**: Assigning priority to processes based on their urgency
- **Multilevel Feedback Queue (MLFQ)**: Using multiple queues with different priorities

#### 6.3 Process Scheduling Theorems

- **Hillier's Theorem**: Optimality of FCFS scheduling algorithm
- **Johnson's Theorem**: Optimality of SJF scheduling algorithm

#### 6.4 Deadlocks

- **Deadlock**: A situation where two or more processes are blocked indefinitely
- **Deadlock Detection**: Identifying and resolving deadlocks
- **Deadlock Prevention**: Avoiding deadlocks by using techniques such as banker's algorithm

#### 6.5 Starvation

- **Starvation**: A situation where a process is denied access to the CPU for an extended period
- **Starvation Prevention**: Preventing starvation by using techniques such as priority scheduling and context switching

#### 6.6 Process Termination

- **Process Termination**: Terminating a process when it completes its task
- **Process Synchronization**: Ensuring that multiple processes access shared resources safely

### Important Formulas and Definitions

- **CPU Utilization**: Measuring the percentage of time the CPU is busy
- **Turnaround Time**: Measuring the time a process spends from its arrival to completion
- **Wait Time**: Measuring the time a process spends waiting for the CPU
- **Response Time**: Measuring the time a process spends from its request to completion
- **Process Yield**: The amount of CPU time a process voluntarily relinquishes to other processes
- **Context Switching**: The process of switching from one process to another
- **Round Robin Scheduling**: A scheduling algorithm that allocates a fixed time slice (time quantum) to each process
