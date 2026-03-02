# Operations On Processes


## Table of Contents

- [Operations On Processes](#operations-on-processes)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Process Creation](#process-creation)
  - [Process Termination](#process-termination)
  - [Process Control Block (PCB)](#process-control-block-pcb)
  - [Process States and State Transitions](#process-states-and-state-transitions)
  - [Context Switching](#context-switching)
  - [Interprocess Communication](#interprocess-communication)
- [Examples](#examples)
  - [Example 1: Analyzing fork() Behavior](#example-1-analyzing-fork-behavior)
  - [Example 2: Process Termination and wait()](#example-2-process-termination-and-wait)
  - [Example 3: Zombie Process Creation](#example-3-zombie-process-creation)
- [Exam Tips](#exam-tips)

## Introduction

In modern computing systems, processes form the fundamental unit of execution. An operating system must not only create and manage processes but also provide mechanisms for processes to interact, synchronize, and terminate gracefully. Understanding operations on processes is crucial for any computer science student because these operations underpin the entire functioning of multitasking operating systems.

The study of process operations becomes particularly significant when we consider that modern operating systems handle hundreds or thousands of processes simultaneously. From the moment a user double-clicks an application icon to the moment the application closes, numerous process operations are silently performed by the operating system. These operations include creating new processes, terminating existing ones, suspending and resuming process execution, and managing the communication between related processes. Without these operations, the concept of multitasking would be impossible to implement.

This topic examines the various operations that operating systems perform on processes, including process creation, process termination, process synchronization, and interprocess communication. Each of these operations involves specific system calls, data structures, and algorithmic approaches that we will explore in detail. Understanding these operations provides the foundation for comprehending more advanced topics such as process scheduling, deadlock handling, and concurrent programming.

## Key Concepts

### Process Creation

Process creation is one of the most fundamental operations in an operating system. When a new process is created, the operating system must allocate memory for the process's code, data, stack, and other resources. Additionally, the OS must create and initialize a Process Control Block (PCB) that contains all the necessary information about the process.

In UNIX and Linux systems, process creation typically involves two system calls: fork() and exec(). The fork() system call creates a new process by duplicating the calling process. The new process is called the child process, while the original process is called the parent process. After fork(), both processes continue execution from the same point, but they have separate address spaces. The only difference is that the return value of fork() differs: it returns the child's PID (Process ID) to the parent process and returns 0 to the child process.

The exec() system call replaces the current process's address space with a new program. When a parent wants to run a different program in the child process, it first calls fork() to create a child process, and then the child process calls exec() to load the desired program. This combination provides flexibility in process creation and program execution.

In Windows systems, the CreateProcess() system call performs both creation and program loading in a single operation. It takes parameters such as the path to the executable file, command-line arguments, process attributes, and thread attributes.

Process creation follows a hierarchical model in most operating systems. In UNIX, processes form a tree structure with the init process (PID 1) as the root. Each process has a parent process, and this relationship is maintained through the Parent Process ID (PPID) field in the PCB. This hierarchical structure facilitates process management and allows for proper cleanup when parent processes terminate before their children.

### Process Termination

Process termination is the inverse operation of process creation. When a process completes its execution or is forced to terminate, the operating system must reclaim all resources allocated to that process. These resources include memory pages, file descriptors, I/O buffers, and any other system resources that the process was using.

Normal termination occurs when a process calls the exit() system call (in UNIX) or when the main function returns. The exit() system call takes an exit status as a parameter, which is typically returned to the parent process via the wait() system call. This allows the parent process to determine whether the child completed successfully or encountered errors.

Abnormal termination can occur due to various reasons such as receiving unhandled signals, accessing invalid memory addresses (segmentation fault), or being explicitly killed by another process or the user. In these cases, the operating system performs emergency cleanup and may generate core dump files for debugging purposes.

The wait() system call is crucial for process termination. When a parent process calls wait(), it blocks until one of its child processes terminates. The wait() system call returns the PID of the terminated child and stores the child's exit status. This mechanism ensures that the parent process can properly reap (clean up) its terminated children, preventing the creation of zombie processes.

A zombie process occurs when a child process terminates but its entry remains in the process table because the parent has not yet called wait(). The zombie state is temporary in normal operation. However, if the parent process terminates without calling wait() for all its children, the orphaned children become adopted by the init process, which periodically calls wait() to reap them.

### Process Control Block (PCB)

The Process Control Block is the kernel data structure that contains all the information about a process. The PCB serves as the process's identity in the operating system and is crucial for process management operations. When the CPU switches between processes, the operating system saves and restores the process's state using information stored in the PCB.

The PCB typically contains several categories of information. Process identification information includes the unique Process ID (PID), Parent Process ID (PPID), and user identification. Process state information stores the current state of the process (new, ready, running, blocked, or terminated). CPU scheduling information includes process priority, scheduling queue pointers, and other scheduling-related data.

Process control information encompasses various flags and counters, such as the program's counters pointing to the next instruction to be executed, CPU registers, memory management information including base and limit registers, page tables, or segment tables, and accounting information tracking CPU time used, time limits, and process IDs.

Resource information and status maintain lists of open files, I/O devices allocated to the process, and signals pending or blocked. The PCB may also include pointers to other PCBs for implementing various scheduling queues.

### Process States and State Transitions

A process can exist in one of several states during its lifetime. The five-state model includes new, ready, running, blocked, and terminated states. The new state represents a process that is being created but has not yet been admitted to the pool of executable processes. The ready state represents a process that is waiting in the ready queue to be assigned to the CPU. The running state means the process's instructions are currently being executed by the CPU. The blocked state indicates that the process is waiting for some event such as I/O completion or the availability of a resource. The terminated state represents a process that has finished execution but has not yet been cleaned up.

State transitions occur due to various events. A transition from new to ready occurs when the OS admits the process. The transition from ready to running happens when the scheduler selects the process for execution. Running to ready occurs when the process is preempted by the scheduler, typically due to time slice expiration. Running to blocked occurs when the process initiates an I/O request or waits for a resource. Blocked to ready occurs when the I/O operation completes or the resource becomes available. Running to terminated occurs when the process completes or aborts.

### Context Switching

Context switching is the operation of saving and restoring the state of a CPU so that processes can share the CPU. When the operating system switches from one process to another, it must save the entire context of the running process and restore the context of the next process to be executed.

The context of a process includes CPU registers, program counter, stack pointer, and other processor state information. Additionally, it may include memory management information such as page tables and base and limit registers. The context switching operation is purely overhead because the CPU does no useful work while performing the switch. Therefore, the efficiency of context switching directly impacts system performance.

Modern processors provide hardware support for context switching through features like multiple register sets. Some operating systems reduce context switching overhead by using lightweight processes or threads, which share significant portions of their context with their parent process.

### Interprocess Communication

Processes often need to communicate and cooperate to accomplish complex tasks. Interprocess Communication (IPC) provides mechanisms for processes to exchange data and synchronize their activities. There are two fundamental models of IPC: the message-passing model and the shared-memory model.

In the message-passing model, processes communicate by sending and receiving messages through communication channels provided by the operating system. System calls like send() and receive() are used for this purpose. Message passing is particularly useful for distributed systems where processes might run on different machines.

In the shared-memory model, processes share a region of memory and read/write to this shared space directly. Processes must synchronize their access to shared memory to avoid race conditions. The operating system provides shared memory primitives but typically leaves synchronization to the processes themselves.

Common IPC mechanisms include pipes, message queues, semaphores, shared memory segments, and sockets. Pipes provide unidirectional communication between related processes. Message queues allow processes to send and receive structured messages. Semaphores are synchronization primitives that help prevent race conditions. Shared memory segments enable fast data exchange between processes. Sockets support communication between processes on possibly different machines.

## Examples

### Example 1: Analyzing fork() Behavior

Consider the following C program:

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    fork();
    printf("Hello World\n");
    return 0;
}
```

When this program executes, the fork() system call creates a child process. After fork(), both parent and child execute the printf statement independently. Therefore, "Hello World" is printed twice: once by the parent process and once by the child process.

The output would be:
```
Hello World
Hello World
```

The order of output depends on the scheduler and is not deterministic. If we want to distinguish between parent and child, we can examine the return value of fork():

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();
    if (pid == 0) {
        printf("Child process: My PID is %d\n", getpid());
    } else {
        printf("Parent process: Child PID is %d\n", pid);
    }
    return 0;
}
```

This program prints different messages for parent and child processes based on the return value of fork().

### Example 2: Process Termination and wait()

Consider a parent process that creates a child to perform some task:

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();
    
    if (pid == 0) {
        // Child process
        printf("Child executing...\n");
        sleep(2);
        printf("Child finished\n");
        exit(5);  // Exit with status 5
    } else {
        // Parent process
        int status;
        wait(&status);
        printf("Parent: Child exited with status %d\n", WEXITSTATUS(status));
    }
    
    return 0;
}
```

In this example, the parent process calls wait() to wait for the child to terminate. When the child exits with status 5, the parent retrieves this status using the WEXITSTATUS macro. This demonstrates proper process termination handling and resource cleanup through wait().

### Example 3: Zombie Process Creation

A zombie process is created when a child terminates but the parent does not call wait():

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid = fork();
    
    if (pid == 0) {
        // Child exits immediately
        printf("Child exiting, becoming zombie\n");
        exit(0);
    } else {
        // Parent sleeps without calling wait()
        printf("Parent sleeping without calling wait()\n");
        sleep(10);
        printf("Parent waking up\n");
    }
    
    return 0;
}
```

During the 10-second sleep period, the child process exists as a zombie. Its entry remains in the process table, and it holds minimal resources. Once the parent calls wait() (which it doesn't in this example before exiting) or terminates, the init process will adopt and reap the zombie.

## Exam Tips

Understanding process operations is essential for the DU semester examination. The following points highlight frequently tested concepts and common pitfalls to avoid.

First, clearly distinguish between fork() and exec() system calls. Fork() creates a new process by duplicating the parent, while exec() replaces the current process's image with a new program. Remember that fork() returns twice (once to parent with child's PID, once to child with 0), while exec() never returns on success.

Second, remember the process lifecycle and state transitions thoroughly. The five-state model (new, ready, running, blocked, terminated) and the events causing transitions between states are commonly asked in examinations. Be prepared to draw state transition diagrams and explain each transition.

Third, understand the purpose and contents of the Process Control Block. The PCB is the kernel data structure that stores all process information, and it is essential for context switching. Memorize the main components: process ID, parent ID, process state, CPU registers, memory management information, and accounting information.

Fourth, be clear on the difference between zombie and orphan processes. A zombie process has terminated but its parent has not yet called wait(). An orphan process is still running but its parent has terminated. Orphans are adopted by init (PID 1), which reaps them when they terminate.

Fifth, for interprocess communication, understand both message-passing and shared-memory models, their advantages, and trade-offs. Shared memory provides faster communication but requires explicit synchronization. Message passing is safer but involves more overhead.

Sixth, remember that context switching involves saving and restoring the entire CPU context including registers, program counter, and stack pointer. It is pure overhead that does not contribute to useful computation. The time taken for context switching affects system performance.

Seventh, be familiar with practical examples of process operations in UNIX systems. Commands like ps, top, and kill demonstrate process operations in action. Understanding how these commands work helps reinforce theoretical concepts.