# **Thread Libraries Textbook 1: Chapter 3: 3.1-3.4**

## **3.1: Process vs Thread**

### Definition

- A **process** is an independent unit of execution that runs in its own memory space.
- A **thread** is a lightweight process that shares the same memory space as other threads in the same process.

### Key Characteristics of Process

- **Resource-intensive**: Each process has its own memory space, files, and resources.
- **Independent execution**: Processes can run concurrently and independently of each other.
- **Preemption**: Processes can be preempted by the operating system to allocate resources to other processes.

### Key Characteristics of Thread

- **Lightweight**: Threads have a smaller memory footprint compared to processes.
- **Shared resources**: Threads share the same memory space, files, and resources as other threads in the same process.
- **Cooperative scheduling**: Threads yield control to other threads voluntarily.

## **3.2: Process Scheduling**

### Definition

- **Process scheduling** is the allocation of time slices (called time quanta) to each process.
- **Process scheduling algorithms** determine which process should be executed next.

### Process Scheduling Algorithms

- **FCFS (First-Come-First-Served)**: The first process to arrive in the ready queue is executed first.
- **SJF (Shortest Job First)**: The process with the shortest execution time is executed first.
- **Priority Scheduling**: Processes are assigned a priority, and the highest-priority process is executed first.
- **Round Robin**: Each process is assigned a time slice, and the process is executed for a fixed time slice.

### Scheduling Parameters

- **Time Quanta**: The time slice allocated to each process.
- **Context Switching**: The time and resources required to switch from one process to another.
- **Process Yield**: The voluntary relinquishment of control to another process.

## **3.3: Operations on Processes**

### Process Creation

- **Process Creation**: The creation of a new process involves allocating memory, files, and resources.
- **Process Creation Algorithms**: Typically involve the following steps:
  - Allocate memory for the new process.
  - Copy the parent process's code and data into the new process.
  - Initialize the new process's registers.
  - Assign a process ID (PID) to the new process.

### Process Termination

- **Process Termination**: The termination of a process involves releasing its allocated resources.
- **Process Termination Algorithms**: Typically involve the following steps:
  - Release the process's memory space.
  - Release the process's files and resources.
  - Update the process table to reflect the process's termination.

### Process Synchronization

- **Process Synchronization**: The coordination of multiple processes to ensure they access shared resources safely.
- **Synchronization Algorithms**: Typically involve the use of semaphores, monitors, or locks to synchronize processes.

### Process Communication

- **Process Communication**: The exchange of data between processes.
- **Communication Algorithms**: Typically involve the use of pipes, sockets, or shared memory to facilitate communication between processes.

## **3.4: Thread Management**

### Thread Creation

- **Thread Creation**: The creation of a new thread involves allocating a thread ID (TID) and initializing the thread's registers.
- **Thread Creation Algorithms**: Typically involve the following steps:
  - Allocate a thread ID (TID).
  - Initialize the thread's registers.
  - Assign the parent process's code and data to the new thread.

### Thread Termination

- **Thread Termination**: The termination of a thread involves releasing its allocated resources.
- **Thread Termination Algorithms**: Typically involve the following steps:
  - Release the thread's memory space.
  - Release the thread's files and resources.
  - Update the thread table to reflect the thread's termination.

### Thread Synchronization

- **Thread Synchronization**: The coordination of multiple threads to ensure they access shared resources safely.
- **Synchronization Algorithms**: Typically involve the use of locks, semaphores, or monitors to synchronize threads.

### Thread Communication

- **Thread Communication**: The exchange of data between threads.
- **Communication Algorithms**: Typically involve the use of shared memory, pipes, or sockets to facilitate communication between threads.
