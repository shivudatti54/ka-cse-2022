# Process Management

## Introduction

Process Management is one of the most fundamental and critical concepts in operating systems. In any computer system, multiple programs need to execute concurrently, and the operating system must efficiently manage these executing programs while maintaining system stability, security, and performance. The process serves as the fundamental unit of work in modern operating systems, representing an instance of a program in execution.

Understanding process management is essential for several reasons. First, it forms the backbone of multiprogramming, which allows users to run multiple applications simultaneously without noticeable interference. Second, it enables CPU utilization by keeping the processor busy even when some processes are waiting for I/O operations. Third, it provides the framework for process isolation, ensuring that one process cannot accidentally or maliciously interfere with another process's execution or data. ForDU students preparing for semester examinations, a thorough grasp of process management concepts is indispensable, as this topic frequently appears in both internal assessments and end-semester examinations.

## Key Concepts

### Process Definition and Characteristics

A process is defined as a program in execution. It is not merely the program code (often called the text section) but encompasses the entire activity of the program. When a program is loaded into memory and begins execution, it becomes a process. A process possesses several key attributes that distinguish it from a static program.

The distinguishing characteristics of a process include:

1. **Program Counter (PC)**: Indicates the address of the next instruction to be executed
2. **Process Stack**: Contains temporary data such as function parameters, return addresses, and local variables
3. **Data Section**: Contains global and static variables
4. **Heap**: Dynamically allocated memory during runtime
5. **Process State**: The current state of execution (new, ready, running, waiting, or terminated)

### Process Control Block (PCB)

The Process Control Block is a data structure maintained by the operating system for each process. It serves as the repository of information about a process and is crucial for process management. The PCB contains all the necessary information that the operating system needs to manage and control a process effectively.

The PCB stores the following critical information:

- **Process Identification**: Unique process ID (PID), parent process ID (PPID), and user identification
- **Processor State Information**: Register values, program counter, stack pointer, and status flags
- **Process Control Information**: Process state, scheduling information (priority, queue pointers), accounting information (CPU time used, time limits), and I/O status information
- **Pointer Information**: Pointers to parent process, child processes, and memory management information

The PCB essentially acts as the "brain" of the process from the operating system's perspective, containing all the context needed to suspend and resume process execution seamlessly.

### Process States

A process can exist in one of several states throughout its lifetime. The classic five-state model includes:

1. **New (Created)**: The process is being created but has not yet been admitted to the ready queue
2. **Ready**: The process is waiting to be assigned to a processor
3. **Running**: Instructions are being executed on the processor
4. **Waiting (Blocked)**: The process is waiting for some event to occur (such as I/O completion or signal reception)
5. **Terminated**: The process has finished execution and is being cleaned up

State transitions occur due to various events. A running process may transition to the ready state due to time slice expiration or preemptive scheduling. A running process may transition to the waiting state when it initiates an I/O operation. A waiting process transitions to ready when the event it was waiting for completes.

### Process Scheduling

Process scheduling is the mechanism by which the operating system determines which process should occupy the CPU at any given time. The scheduling system involves three main components: schedulers, the ready queue, and the dispatch mechanism.

**Schedulers** are specialized system components that select processes from queues. The operating system typically employs three types of schedulers:

- **Long-term Scheduler**: Decides which processes are admitted to the ready queue from the new state. It controls the degree of multiprogramming and balances system load. In modern systems with abundant memory, this scheduler is often less critical or absent.

- **Short-term Scheduler (CPU Scheduler)**: Selects from the ready queue which process should be dispatched to the CPU. This scheduler must be extremely fast since it runs frequently (potentially every few milliseconds).

- **Medium-term Scheduler**: Temporarily removes processes from memory to reduce degree of multiprogramming, swapping them back when memory becomes available.

The **ready queue** contains all processes ready to execute, typically implemented as a linked list or priority queue. The **dispatcher** is the component that actually transfers control from the currently running process to the newly selected process, involving context switching.

### Operations on Processes

The operating system provides mechanisms for process creation and termination, enabling dynamic management of system resources.

**Process Creation**: A process can create child processes, forming a hierarchy. In Unix-like systems, the init process becomes the ancestor of all other processes. When a new process is created, the parent may either continue execution concurrently with its children or wait until all children terminate. The child process may be a duplicate of the parent (fork) or load a new program (exec).

**Process Termination**: A process terminates when it executes its last statement and requests the operating system to delete it using the exit() system call. The parent may wait for the child's termination using the wait() system call to retrieve the child's exit status. The operating system then reclaims all resources allocated to the terminated process, including memory, open files, and I/O buffers.

### Interprocess Communication

Processes frequently need to communicate and share data, necessitating Interprocess Communication (IPC) mechanisms. There are two primary models for IPC:

**Shared Memory Model**: Processes share a region of memory, with one process writing data that another process can read. This provides high-speed communication but requires explicit synchronization mechanisms (such as semaphores or mutexes) to prevent race conditions.

**Message Passing Model**: Processes communicate by sending and receiving messages through a communication channel. This can be implemented through direct or indirect communication, synchronous or asynchronous message passing, and automatic or explicit buffering.

Common IPC mechanisms include pipes, message queues, shared memory segments, and sockets. Each mechanism has specific use cases and performance characteristics that make it suitable for different scenarios.

## Examples

### Example 1: Understanding Process States in a Simple Scenario

Consider a user running a web browser while simultaneously compiling a large program. Initially, both processes are created and enter the "New" state. Once admitted by the long-term scheduler, they enter the "Ready" state and are placed in the ready queue. The short-term scheduler selects the browser process to run, transitioning it to the "Running" state. While the browser displays content, the compilation process remains in "Ready" state.

When the browser initiates a network request to load a webpage, it transitions to the "Waiting" state. The CPU scheduler now selects the compilation process from the ready queue, changing it to "Running." When the network operation completes, the browser transitions back to "Ready" state. The CPU continues switching between these processes based on scheduling decisions.

This example illustrates how multiple processes appear to execute simultaneously through rapid context switching, enabling effective CPU utilization and user responsiveness.

### Example 2: Process Creation Using fork() and exec()

In Unix-like systems, process creation involves two system calls: fork() creates a new process (child), and exec() replaces the child process's memory space with a new program.

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();  // Create new process
    
    if (pid < 0) {
        // Fork failed
        printf("Fork failed\n");
        return 1;
    }
    else if (pid == 0) {
        // Child process executes this
        printf("Child Process: PID = %d, Parent PID = %d\n", 
               getpid(), getppid());
        execlp("/bin/ls", "ls", "-l", NULL);  // Replace with ls command
        // If exec succeeds, this line never executes
        printf("Exec failed\n");
    }
    else {
        // Parent process executes this
        printf("Parent Process: Created child with PID = %d\n", pid);
        wait(NULL);  // Wait for child to complete
        printf("Child process completed\n");
    }
    
    return 0;
}
```

In this example, fork() returns twice: once in the parent (with the child's PID) and once in the child (with 0). The child then uses execlp() to replace its program image with the "ls" command. The parent uses wait() to synchronize with the child's completion, ensuring proper cleanup.

### Example 3: Calculating Turnaround and Waiting Time

Given three processes with the following arrival times and burst times, calculate average turnaround time and average waiting time using First-Come-First-Served (FCFS) scheduling:

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1      | 0            | 10         |
| P2      | 1            | 5          |
| P3      | 2            | 8          |

**Solution:**

**Gantt Chart:**
```
P1(0-10) | P2(10-15) | P3(15-23) |
```

**Completion Times:**
- P1: 0 + 10 = 10
- P2: 10 + 5 = 15
- P3: 15 + 8 = 23

**Turnaround Time = Completion Time - Arrival Time:**
- P1: 10 - 0 = 10
- P2: 15 - 1 = 14
- P3: 23 - 2 = 21
- Average Turnaround Time: (10 + 14 + 21) / 3 = 15

**Waiting Time = Turnaround Time - Burst Time:**
- P1: 10 - 10 = 0
- P2: 14 - 5 = 9
- P3: 21 - 8 = 13
- Average Waiting Time: (0 + 9 + 13) / 3 = 7.33

This example demonstrates how to analyze process scheduling behavior, a common examination question type.

## Exam Tips

For DU semester examinations, keep the following points in mind:

1. **Understand PCB Structure**: Know the exact contents of a Process Control Block and its role in context switching. This is frequently tested in both objective and subjective questions.

2. **State Transition Diagrams**: Be able to draw and explain process state transition diagrams. Questions asking you to identify valid or invalid state transitions are common.

3. **Scheduling Algorithms**: Master FCFS, SJF, Round Robin, and Priority scheduling algorithms. Be prepared to calculate waiting times, turnaround times, and completion times for given scenarios.

4. **fork() and exec()**: Understand the relationship between these system calls and how they work together for process creation in Unix-like systems.

5. **IPC Mechanisms**: Know the differences between shared memory and message passing models, including advantages and disadvantages of each approach.

6. **Context Switching**: Understand what happens during a context switch, including the role of the PCB and the time overhead involved.

7. **Difference Between Process and Program**: Clearly articulate that a process is a program in execution with its own resources, while a program is a passive entity stored on disk.

8. **Scheduling Criteria**: Know CPU utilization, throughput, turnaround time, waiting time, and response time as evaluation criteria for scheduling algorithms.