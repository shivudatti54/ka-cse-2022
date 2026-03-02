# **Thread Libraries Textbook 1: Chapter 3**

## **3.1: Process Concept**

### Definition:

A process is an independent unit of execution that runs in its own memory space, sharing the same address space as the parent process. Each process has its own program counter, stack, and local variables.

### Characteristics:

- **Autonomy**: Each process has its own program execution, and it can run independently of other processes.
- **Resource allocation**: Processes can share or allocate resources such as memory, I/O devices, and files.
- **Communication**: Processes can exchange data with each other through inter-process communication (IPC) mechanisms.

### Key Concepts:

- **Process creation**: Creating a new process by duplicating an existing process.
- **Process synchronization**: Coordinating access to shared resources among multiple processes.
- **Process termination**: Stopping a process from executing.

### Example:

Suppose we have two processes, P1 and P2, running on the same CPU. P1 is a web server, and P2 is a database server. Both processes can run concurrently, and they can share resources like memory and I/O devices.

## **3.2: Process Scheduling**

### Definition:

Process scheduling is the discipline of allocating a shared resource (CPU) to a set of processes, optimizing their execution over time.

### Types of Process Scheduling:

- **Preemptive Scheduling**: The operating system interrupts a process and switches to another process.
- **Non-Preemptive Scheduling**: The operating system does not interrupt a process, and it continues executing until completion.

### Algorithms:

- **First-Come-First-Served (FCFS)**: The process that arrives first is executed first.
- **Shortest Job First (SJF)**: The process with the shortest execution time is executed first.
- **Prioritized Scheduling**: The operating system assigns a priority to each process, and the highest-priority process is executed first.

### Key Concepts:

- **Context switching**: The process of switching from one process to another.
- **CPU utilization**: The percentage of CPU time spent by a process or processes.

## **3.3: Operations on Processes**

### Definition:

Operations on processes refer to the actions performed on a process, such as creating, deleting, renaming, and terminating.

### Operations:

- **Process creation**: Creating a new process by duplicating an existing process.
- **Process deletion**: Removing a process from the system.
- **Process renaming**: Renaming a process with a new name.
- **Process termination**: Stopping a process from executing.

### Key Concepts:

- **Process ID (PID)**: A unique identifier assigned to a process.
- **Parent process**: The parent process that spawned a child process.

## **3.4: Thread Libraries**

### Definition:

A thread library is a collection of functions and data structures that provide a way to create, manage, and execute threads.

### Types of Thread Libraries:

- **POSIX Threads (pthreads)**: A thread library for POSIX systems.
- **Windows Threads (Win32)**: A thread library for Windows systems.

### Key Concepts:

- **Thread creation**: Creating a new thread using a thread library.
- **Thread synchronization**: Coordinating access to shared resources among multiple threads.
- **Thread termination**: Stopping a thread from executing.

### Example:

Suppose we want to create a web server that can handle multiple requests concurrently. We can use a thread library to create multiple threads, each responsible for handling a single request.
