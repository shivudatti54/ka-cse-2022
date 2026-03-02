# Process Management

## Introduction

Process management is one of the most fundamental and critical components of any modern operating system. It forms the backbone of how computers execute multiple programs simultaneously, enabling the illusion of concurrency even on single-processor systems. In the context of operating systems, a process represents a program in execution — it is an active entity that contains all the information necessary for the CPU to execute the program's instructions. Without effective process management, operating systems would be unable to handle multiple users, run multiple applications, or provide the responsive computing experience that users expect today.

The importance of process management extends beyond mere program execution. It encompasses the creation, scheduling, and termination of processes, ensuring optimal utilization of the CPU while maintaining system stability and security. In modern computing environments, from personal computers to enterprise servers, process management enables time-sharing, multitasking, and efficient resource allocation. For students studying at Delhi University, understanding process management is essential because it forms the foundation for comprehending how operating systems achieve efficiency, responsiveness, and fairness in resource allocation.

This topic becomes particularly significant when considering the variety of processes running on any typical computer system at any given moment — from system daemons managing hardware to user applications executing user commands. The operating system must manage these processes intelligently, allocating CPU time, memory, and I/O resources in a manner that maximizes throughput while minimizing turnaround time and response time. The concepts learned in this topic will also serve as prerequisites for understanding advanced topics such as multithreading, distributed systems, and real-time operating systems.

## Key Concepts

### Process Definition and Components

A process is formally defined as a program in execution. It is not merely the program code (often called the text section) but encompasses the entire execution context. A process consists of three main components: the program code, the current activity represented by program counters and CPU registers, and the process stack containing temporary data such as function parameters, return addresses, and local variables. Additionally, a process has a data section that contains global variables and a heap section for dynamically allocated memory during execution.

The distinction between a program and a process is crucial. A program is a passive entity — a file containing instructions and data stored on disk — while a process is an active entity that the operating system creates when it loads the program into memory and begins execution. Multiple processes can execute the same program simultaneously, each having its own independent execution context. For example, opening multiple instances of a text editor results in multiple processes running the same program but maintaining separate states.

### Process Control Block (PCB)

The Process Control Block is the most important data structure used by the operating system to represent processes. It is a kernel-level data structure that contains all the information necessary for the operating system to manage a specific process. The PCB serves as the repository of process-related information and is created when the process is created, existing until the process terminates.

The PCB contains several critical fields. The process state field indicates the current state of the process (new, ready, running, waiting, or terminated). The program counter stores the address of the next instruction to be executed for this process. CPU registers hold the current values of registers when the process is interrupted. Memory management information includes page tables, segment tables, or base and limit registers that define the process address space. Process identification information includes a unique process identifier (PID) along with parent process identifier (PPID). Accounting information tracks CPU usage, elapsed time, and resource limits. I/O status information maintains the list of I/O devices allocated to the process and the list of open files.

The operating system maintains a collection of PCBs organized in various queues — a ready queue for processes waiting for CPU allocation, and one or more wait queues for processes waiting for I/O or other events. The transitions between these queues are governed by the process state changes.

### Process States

A process can exist in one of several states during its lifetime. The fundamental process states include NEW, representing a process being created; READY, indicating the process is waiting in the queue to be assigned to the CPU; RUNNING, meaning the process instructions are currently being executed by the CPU; WAITING (or BLOCKED), indicating the process is waiting for some event such as I/O completion or a signal; and TERMINATED, representing a process that has finished execution.

State transitions occur based on specific events. A NEW process moves to READY when the operating system admits it to the ready queue. A READY process moves to RUNNING when the scheduler dispatches it to the CPU. A RUNNING process can move to READY if a time slice expires or if it is preempted by a higher-priority process. A RUNNING process moves to WAITING when it initiates an I/O operation or waits for an event. A WAITING process moves to READY when the I/O operation completes or the awaited event occurs. Finally, a RUNNING or WAITING process moves to TERMINATED when execution completes or the operating system terminates it.

### Process Scheduling

Process scheduling is the mechanism by which the operating system decides which process should occupy the CPU at any given time. The scheduler is responsible for maximizing CPU utilization, ensuring fairness, minimizing turnaround time, reducing waiting time, and maximizing throughput. There are three types of schedulers working together in most operating systems.

The long-term scheduler, also called the admission scheduler, decides which processes are admitted to the system from the pool of new processes. It controls the degree of multiprogramming — the number of processes in memory. The short-term scheduler, or CPU scheduler, decides which of the ready processes should be allocated to the CPU. It is invoked frequently (every few milliseconds) and must be extremely fast. The medium-term scheduler performs swapping — moving processes between main memory and secondary storage — to manage the degree of multiprogramming and improve memory utilization.

### Process Scheduling Algorithms

Several algorithms exist for CPU scheduling, each with distinct characteristics and trade-offs. The First-Come-First-Served (FCFS) algorithm schedules processes in the order of their arrival time. While simple to implement, it suffers from the convoy effect where short processes wait behind long processes, leading to poor average turnaround time.

The Shortest Job First (SJF) algorithm selects the process with the smallest burst time. It provides optimal average waiting time but requires accurate prediction of CPU burst lengths, which is challenging in practice. The priority scheduling algorithm assigns a priority to each process and schedules the highest-priority process first. It can lead to starvation of low-priority processes, which can be mitigated using aging — gradually increasing the priority of waiting processes.

The Round Robin (RR) algorithm is designed for time-sharing systems. It allocates a fixed time slice (quantum) to each process in a cyclic manner. This ensures that no process monopolizes the CPU and provides good response time. The time quantum size is critical — too small causes excessive context switches, while too large degenerates to FCFS.

Multilevel Queue scheduling maintains separate queues for different process types (system, interactive, batch) with different scheduling algorithms for each queue. Multilevel Feedback Queue scheduling allows processes to move between queues based on their CPU burst characteristics, combining the advantages of multiple algorithms.

### Process Creation and Termination

Process creation occurs when a running process explicitly requests the creation of a new process (using system calls like fork in Unix or CreateProcess in Windows) or when the operating system initializes the system. The parent process may execute concurrently with its child processes, and they may share certain resources. The child process may be a duplicate of the parent (having the same program and data) or load a new program.

In Unix-like systems, the fork system call creates a new process by duplicating the parent process. The child receives a copy of the parent's address space. The exec system call is typically used after fork to replace the child's memory space with a new program. This two-step process (fork followed by exec) is fundamental to how Unix systems create and manage processes.

Process termination occurs when a process finishes its execution normally (reaches its natural end), calls the exit system call, or is terminated by the operating system due to an error or being killed by another process. Upon termination, the operating system reclaims all resources allocated to the process, updates process tables, and notifies the parent process through the wait system call. A terminated process whose parent has not yet called wait remains in the zombie state. An orphaned process (whose parent terminated without calling wait) is adopted by the init process.

### Interprocess Communication

Processes frequently need to communicate and cooperate to accomplish tasks. The operating system provides mechanisms for Interprocess Communication (IPC) to enable this cooperation. These mechanisms allow processes to share data, synchronize their activities, and coordinate their actions.

Shared memory is the fastest IPC mechanism. The operating system establishes a shared memory region that multiple processes can access. Processes read from and write to this shared memory directly, without kernel intervention after the initial setup. However, synchronization must be implemented by the processes themselves using mechanisms like semaphores or mutexes.

Message passing involves the operating system providing communication channels (pipes, message queues) through which processes send and receive messages. This mechanism provides natural synchronization because a send operation blocks until a receive occurs, but it can be slower than shared memory due to the involvement of the kernel in every message transfer.

Other IPC mechanisms include signals (asynchronous notifications), sockets (for network communication), and files (though with performance limitations). The choice between these mechanisms depends on the specific requirements of the application, including data volume, synchronization needs, and performance constraints.

## Examples

### Example 1: Process State Transitions

Consider a process executing a program that reads data from a file. Initially, the process is in the READY state, waiting in the ready queue. The CPU scheduler dispatches it, and the process moves to the RUNNING state. While executing, it issues a read system call for file input. Since I/O operations are slower than CPU processing, the operating system cannot keep the process running. The process moves from RUNNING to WAITING (or BLOCKED) state, and the CPU scheduler selects another ready process.

When the I/O operation completes (after hundreds of thousands of CPU cycles), the disk controller generates an interrupt. The operating system handles this interrupt and moves the waiting process from the WAITING state to the READY state, placing it back in the ready queue. Eventually, the scheduler dispatches this process again, and it returns to the RUNNING state to process the input data.

### Example 2: Round Robin Scheduling

Assume three processes arrive at time 0 with the following CPU burst times: P1 = 10 units, P2 = 5 units, and P3 = 8 units. Using Round Robin with a time quantum of 4 units, the execution proceeds as follows:

At time 0, P1 runs for 4 units (remaining: 6). At time 4, P2 runs for 4 units (remaining: 1). At time 8, P3 runs for 4 units (remaining: 4). At time 12, P1 runs again for 4 units (remaining: 2). At time 16, P2 runs for its final 1 unit and terminates. At time 17, P3 runs for 4 units (remaining: 0) and terminates. At time 21, P1 runs for its final 2 units and terminates.

The completion times are: P1 at 23, P2 at 17, P3 at 21. Average turnaround time = (23 + 17 + 21) / 3 = 20.33 units. Average waiting time = (13 + 12 + 13) / 3 = 12.67 units.

### Example 3: Fork and Exec System Calls

In Unix systems, creating a new process to run a different program involves two steps:

```
pid = fork();  // Create a new process

if (pid == 0) {
    // This is the child process
    execlp("/bin/ls", "ls", "-l", NULL);
    // If execlp succeeds, this code is never reached
    // If it fails, handle the error
} else if (pid > 0) {
    // This is the parent process
    wait(NULL);  // Wait for child to complete
    printf("Child completed\n");
} else {
    // fork failed
    perror("fork failed");
}
```

The fork call creates a child process that is a copy of the parent. In the child process (where pid == 0), the execlp call replaces the child's program with the "ls -l" command. The parent calls wait to wait for the child to complete before continuing. This pattern is fundamental to how Unix systems execute external programs.

## Exam Tips

For Delhi University semester examinations, several key points about process management require special attention. First, thoroughly understand the difference between program and process — this is a frequently tested concept in objective and short-answer questions. The examiner often asks candidates to distinguish between these two terms.

Second, memorize the five fundamental process states and understand exactly what causes transitions between them. Questions frequently ask students to draw state transition diagrams or explain why a specific transition occurs. Pay special attention to what happens during system calls and interrupts, as these trigger most state changes.

Third, the Process Control Block is another favorite topic for examination questions. Be prepared to draw and explain the PCB structure, listing all its components. Understanding the PCB is essential because it is the operating system's primary mechanism for process management.

Fourth, for scheduling algorithms, practice numerical problems thoroughly. DU exams typically include numerical questions requiring calculation of average waiting time, turnaround time, and completion time for FCFS, SJF, and Round Robin algorithms. Remember that SJF can be either preemptive or non-preemptive — both versions have appeared in previous examinations.

Fifth, understand the concept of context switching — what it is, what information is saved and restored, and why it incurs overhead. This concept connects process management with CPU architecture and is often tested in conjunction with scheduling.

Sixth, be clear about the differences between long-term, short-term, and medium-term schedulers. Know which type of scheduling each performs and how they relate to each other. Understand how the degree of multiprogramming affects system performance.

Seventh, for interprocess communication, understand both shared memory and message passing mechanisms, including their advantages and disadvantages. Questions may ask you to compare these mechanisms or explain scenarios where each would be appropriate.