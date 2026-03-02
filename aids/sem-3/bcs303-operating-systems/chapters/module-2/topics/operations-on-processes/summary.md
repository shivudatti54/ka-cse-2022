# Operations on Processes

## Revision Notes

### Key Definitions

- **Process**: A task or program that is currently being executed by the CPU.
- **Process Table**: A data structure that stores information about all running processes.
- **Process Scheduling**: The art of allocating CPU time to processes.

### Process Creation and Termination

- **Process Creation**: A new process is created by the operating system using a system call (e.g., `fork()`).
- **Process Termination**: A process is terminated when it completes its execution or is killed by the operating system.
- **Wait**: A process can call `wait()` to suspend its execution and wait for the termination of another process.
- **Signal**: A signal is a message sent by the operating system to a process to terminate or suspend its execution.

### Process Communication

- **Inter-Process Communication (IPC)**: Techniques used by processes to exchange data with each other.
- **Synchronization**: Techniques used to coordinate access to shared resources between processes.
- **Semaphores**: A variable that controls the access to a shared resource.
- **Monitors**: A higher-level synchronization construct that can be used to implement semaphores.

### Process Scheduling Algorithms

- **First-Come-First-Served (FCFS)**: The operating system schedules processes in the order they arrived.
- **Shortest Job First (SJF)**: The operating system schedules processes based on their execution time.
- **Round-Robin (RR)**: The operating system allocates equal time slices to each process.

### Process States

- **Ready**: A process is ready to be executed by the CPU.
- **Running**: A process is currently being executed by the CPU.
- **Waiting**: A process is waiting for input/output operations to complete.
- **Sleeping**: A process is waiting for a specific event to occur.
- **Zombie**: A process that has terminated but still exists in the process table.
- **Dead**: A process that has terminated and is no longer in the process table.

### Important Formulas

- **CPU Time**: The amount of time a process spends executing in the CPU.
- **Turnaround Time**: The time a process spends waiting for CPU time.
- **Response Time**: The time a process spends waiting for input/output operations to complete.

### Important Theorems

- **Theorem of Scheduling**: The schedule of a process can be optimized to minimize CPU time and maximize throughput.
- **Theorem of Condition**: The condition for a process to be scheduled is that it must be ready and have a non-negative priority.

### Key Concepts

- **Process Priority**: The priority assigned to a process to determine its order of execution.
- **Process Scheduling Heuristics**: Techniques used to optimize process scheduling.
- **Process Context Switching**: The process of switching from one process to another.
- **Process Swapping**: The process of loading a new program into memory.
