# Chapter 4: 4.1

### Process Management

- A process is a program in execution, having its own memory space.
- A process can be thought of as an independent program that runs on the operating system.
- A process can communicate with other processes using inter-process communication (IPC) methods.

### Process Scheduling

- **Scheduling**: The process of assigning a set of processes to a CPU for execution.
- **Time slicing**: Each process gets a fixed time slot to execute, known as Time Quanta.
- **Priorities**: Processes are assigned different priorities to determine the order in which they should be executed.

### Process Creation and Termination

- **Process Creation**: A process is created by the operating system using a process scheduler.
- **Process Termination**: A process can terminate either by completion or by termination.

### Process Synchronization

- **Mutual Exclusion**: One process at a time can access a shared resource.
- **Deadlock**: When two or more processes are blocked indefinitely, waiting for each other to release resources.

### Formulas and Definitions

- **Process ID (PID)**: Unique identifier for a process.
- **Thread ID (TID)**: Unique identifier for a thread.
- **CPU Time**: Time spent by a process in CPU.
- **Wait Time**: Time spent by a process waiting for other processes or I/O operations.

### Important Theorems

- **Hillard's Theorem**: If two processes P1 and P2 are mutually exclusive, P1 can run until completion before P2 starts.
- **Lamport's Bakery Algorithm**: A deadlock prevention algorithm that assigns a time slice to each process and ensures that no process will hold onto a resource indefinitely.
