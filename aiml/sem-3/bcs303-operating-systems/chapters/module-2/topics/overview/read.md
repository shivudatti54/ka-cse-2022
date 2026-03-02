# Overview of Process Management

## Introduction

Process Management is one of the fundamental pillars of any modern operating system. It forms the backbone of how computers execute multiple tasks seemingly simultaneously, enabling the multi-tasking capabilities that we often take for granted in today's computing environments. Whether you are browsing the internet, writing a document, or running a complex simulation, the operating system's process management subsystem is working tirelessly behind the scenes to ensure smooth execution of all applications.

In the context of the University of Delhi's Computer Science curriculum, this module holds exceptional importance as it directly addresses how operating systems allocate CPU time, manage system resources, and maintain system stability under varying workloads. Understanding process management is not merely theoretical—it forms the practical foundation for writing efficient concurrent programs, debugging system-level issues, and designing scalable software architectures.

This overview serves as an introduction to the entire Module 2, which encompasses eight hours of intensive study. We will explore the process concept, understand how the operating system represents and controls processes, examine various scheduling algorithms, analyze inter-process communication mechanisms, and delve into the increasingly important domain of multi-threaded programming. Each of these topics builds upon the fundamental understanding of what a process truly is in the eyes of the operating system.

## Key Concepts

### What is a Process?

A process is fundamentally a program in execution. However, it is crucial to understand that a program is a passive entity—a collection of instructions stored on disk—while a process is an active entity that the operating system creates, manages, and eventually terminates. When you execute a program, the operating system creates a process that includes the program code, current activity represented by program counter values, processor register contents, stack data, heap memory, and various system resources such as file descriptors and security attributes.

The operating system maintains a process control block (PCB) for each process, which serves as the repository of all information about the process. The PCB contains process identification information (PID), process state (new, ready, running, waiting, or terminated), program counter indicating the next instruction to execute, CPU register contents, memory management information including page tables or segment tables, accounting information such as CPU time used and limits, I/O status information listing open files and devices, and scheduling information including priority and pointers to scheduling queues.

### Process States

A process can exist in one of several distinct states throughout its lifecycle. The NEW state represents a process that is being created but has not yet been admitted to the pool of executable processes. The READY state indicates that the process is waiting in the ready queue to obtain the CPU for execution. The RUNNING state means the process is currently being executed by the CPU, with its instructions being processed. The WAITING or BLOCKED state signifies that the process is waiting for some event to occur, such as I/O completion or the availability of a resource. Finally, the TERMINATED state indicates that the process has finished execution and the operating system is reclaiming its resources.

Transitions between these states occur through specific events. A running process may be preempted and moved back to the ready state if a higher-priority process becomes ready or if its time quantum expires. A running process may enter the waiting state by issuing an I/O request or waiting for another process. A waiting process returns to the ready state when the event it was waiting for occurs.

### Process Scheduling

Process scheduling is the mechanism by which the operating system decides which process should execute at any given time. The scheduler maintains various queues to organize processes according to their states. The ready queue contains all processes waiting for CPU time, while device queues contain processes waiting for I/O devices. The scheduler's job is to select processes from these queues according to specific criteria and assign them to the CPU.

Scheduling occurs at three distinct levels. Long-term scheduler, also called the admission scheduler, decides which processes are admitted to the ready queue from the pool of new processes. It controls the degree of multiprogramming—the number of processes in memory. Short-term scheduler, or CPU scheduler, decides which of the ready processes should be allocated the CPU next. This scheduler operates frequently, making decisions every few milliseconds. The medium-term scheduler, unique to systems with swapping capabilities, temporarily removes processes from memory to reduce the degree of multiprogramming, later reintroducing them to the ready state.

### Operations on Processes

The operating system provides several fundamental operations for process management. Process creation is initiated when a parent process creates child processes, establishing a parent-child relationship. UNIX systems use the fork() system call to create a new process, with the child receiving a copy of the parent's address space. The exec() family of functions then replaces the child's memory space with a new program.

Process termination occurs when a process completes its execution normally via the exit() system call or abnormally due to an unhandled exception. The parent process can wait for child termination using the wait() system call, retrieving the child's exit status. In some cases, the operating system may terminate a misbehaving process, for instance, when it exceeds its time limits or consumes excessive memory.

Process synchronization becomes essential when multiple processes access shared resources. The operating system provides mechanisms like semaphores, mutex locks, and monitors to prevent race conditions and ensure data consistency. These synchronization primitives ensure that only one process at a time can access critical sections of code or shared data structures.

### Inter-Process Communication

Processes frequently need to communicate and coordinate their activities. Inter-process communication (IPC) enables processes to exchange data and synchronize their execution. The two primary models for IPC are shared memory and message passing.

In the shared memory model, processes share a region of memory and read/write to it directly. This approach offers high-speed communication but requires explicit synchronization to prevent conflicts. The message passing model involves sending and receiving messages through communication channels established between processes. This model provides cleaner separation between processes but may incur higher overhead due to system calls for each message transmission.

Common IPC mechanisms include pipes for parent-child communication, message queues for structured message exchange, shared memory segments for direct data sharing, and sockets for network-based communication between processes on potentially different machines.

### Multi-threaded Programming

Threads represent a lightweight unit of execution within a process. Unlike separate processes that have independent address spaces, threads within the same process share the code section, data section, and other operating system resources. This shared nature makes thread creation and context switching much faster compared to process creation and switching.

Multi-threaded programming has become essential for modern application development. Server applications use threads to handle multiple client requests concurrently. Web browsers use threads to load page content, execute JavaScript, and render graphics simultaneously. Database management systems use threads to handle multiple queries in parallel.

Each thread has its own thread ID, program counter, register set, and stack, while sharing the heap and other resources with other threads in the same process. This arrangement enables efficient parallel processing while maintaining the simplicity of a single address space.

## Examples

### Example 1: Process Creation and Execution

Consider a scenario where a user double-clicks an icon to launch a text editor application. The following sequence illustrates process management in action:

First, the shell (command interpreter) receives the user's request and calls the fork() system call, creating a child process that is a copy of the shell process. The child process then calls exec() to replace its program image with the text editor program. Now the new process enters the NEW state as the operating system loads the program code and data into memory. Once loading completes, the process moves to the READY state, waiting in the ready queue for CPU allocation.

When the CPU scheduler selects this process, it transitions to the RUNNING state, and the processor begins executing the text editor's instructions. When the user types characters, the text editor may issue I/O system calls, causing the process to move to the WAITING state while the keyboard driver processes the input. After the I/O completes, the device driver generates an interrupt, the operating system moves the process back to the READY state. This cycle continues until the user closes the application, the process calls exit(), and the operating system reclaims all its resources.

### Example 2: Process Scheduling Decision

Consider a system with three processes in the ready queue: Process A with CPU burst time of 5ms and priority 5, Process B with burst time of 10ms and priority 3, and Process C with burst time of 3ms and priority 7. If the system uses priority scheduling, Process C (highest priority 7) would be selected first. However, this could cause starvation for lower-priority processes.

If the system uses Shortest Job First (SJF) scheduling, Process C with the smallest burst time (3ms) would execute first, followed by Process A (5ms), and then Process B (10ms). This approach minimizes average waiting time but requires the scheduler to know or estimate burst times in advance, which is often impractical.

In a Round Robin system with a time quantum of 4ms, all three processes would receive CPU time in rotation. Process A would execute for 4ms (1ms remaining), then Process B for 4ms (6ms remaining), then Process C for 3ms (completes), then Process A again for 4ms (completes), and finally Process B for the remaining 6ms. This ensures fairness but may result in higher average waiting time compared to SJF.

### Example 3: Thread Creation in Practice

A web server application demonstrates multi-threading effectively. The main thread listens for incoming HTTP requests on port 80. When a request arrives, the main thread creates a new worker thread to handle that specific client. This worker thread processes the request—reading files, executing server-side scripts, accessing databases—and sends the response back to the client.

Consider a scenario where 1000 clients connect simultaneously. With a single-threaded server, each client would wait for all previous requests to complete. With 1000 threads, all requests can be processed concurrently. Each thread has its own stack for function call tracking, but all threads share the same file descriptors for open connections, the same database connection pool, and the same application code.

The thread creation process involves allocating a thread control block, initializing thread-specific data like stack and program counter, and adding the thread to the system's run queue. This is significantly faster than creating a new process, which would require duplicating the entire address space and all system resources.

## Exam Tips

For DU semester examinations, understanding the following points will help you score well in process management questions.

First, always remember the distinction between a program and a process—a program is passive, while a process is active and includes execution context. The PCB is the most important data structure in process management, and you should be able to list all its components.

Second, understand all five process states and the possible transitions between them. Drawing a state diagram often helps in examinations to visualize these transitions. Pay special attention to when a running process transitions to waiting versus ready states.

Third, memorize the differences between long-term, short-term, and medium-term schedulers. Understand which scheduler operates at which level of memory hierarchy and how frequently each makes decisions. Long-term scheduler controls degree of multiprogramming, while short-term scheduler affects system responsiveness.

Fourth, for scheduling algorithms, you should be able to calculate waiting time, turnaround time, and throughput for FCFS, SJF, Priority, and Round Robin algorithms. Practice numerical problems thoroughly. Remember that SJF can be either preemptive or non-preemptive—know the difference.

Fifth, understand process creation using fork() and exec() in UNIX systems. Be clear about what happens to the parent's address space when fork() is called and how exec() replaces it. This is a frequently asked concept in examinations.

Sixth, for inter-process communication, know the differences between shared memory and message passing models. Understand which is faster and why, and recognize common IPC mechanisms like pipes, message queues, and sockets.

Seventh, in multi-threading, focus on the benefits of threads over processes, including faster creation, faster context switching, and ease of communication. Understand thread libraries and the differences between user-level and kernel-level threads.

Finally, remember that thread safety and synchronization are critical when multiple threads access shared resources. Be familiar with concepts like race conditions, critical sections, and basic synchronization primitives.