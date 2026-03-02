# Process Concept

## Introduction

The process is one of the most fundamental concepts in operating systems, forming the backbone of modern computing. In any computer system, multiple programs appear to execute simultaneously, whether they are user applications like a web browser and a word processor, or system services like printing and file management. The operating system abstracts the complexities of hardware execution and provides the illusion of concurrent execution through the process abstraction. Understanding processes is essential for comprehending how operating systems manage resources, schedule CPU time, and maintain system stability and security.

In the context of University of Delhi's Computer Science curriculum, the process concept serves as the foundation for advanced topics like process scheduling, inter-process communication, and multithreading. A thorough grasp of processes enables programmers to write efficient, responsive applications and system administrators to optimize system performance. This topic becomes particularly relevant when studying how modern operating systems like Windows, Linux, and macOS handle the complexity of executing hundreds or thousands of concurrent tasks on limited hardware resources.

## Key Concepts

### Definition of a Process

A process is a program in execution. It is a dynamic entity, unlike a program which is static. When you write code and save it as a file, it is a program. When you execute that code, the operating system creates a process that carries out the instructions specified in the program. A process encompasses the program code, current activity represented by program counter values, processor registers, stack contents, heap memory, data section, and various system resources allocated to it such as file descriptors and signal handlers.

Technically, a process is the unit of work in a modern computing system. The operating system kernel maintains data structures called Process Control Blocks (PCBs) to represent each process. These PCBs contain all the information the OS needs to manage and schedule processes, making them the most critical data structure in process management.

### Process States

As a process executes, it moves through various states. The standard process states defined in most operating systems are:

**NEW (Created):** The process is being created. The operating system has performed the initial setup but has not yet admitted it to the pool of executable processes. Memory allocation for the process control block has occurred, but the program has not been loaded into memory yet.

**READY:** The process is waiting to be assigned to the processor. All necessary resources except the CPU are available. The process sits in the ready queue, waiting for the scheduler to select it for execution. Multiple ready processes may exist simultaneously, forming the ready queue.

**RUNNING:** The process is currently being executed by the processor. At any given time, on a single-processor system, only one process can be in the running state. The CPU executes the process's instructions, and the program counter points to the next instruction to be executed.

**WAITING (Blocked):** The process is waiting for some event to occur, such as I/O completion, availability of a resource, or reception of a signal. The process cannot continue execution until the event it is waiting for occurs. While waiting, the process does not consume CPU cycles.

**TERMINATED (Exit):** The process has finished execution or has been explicitly terminated. The operating system reclaims all resources allocated to the process, including memory, open files, and other system resources. The process control block remains in memory temporarily to allow the parent process to retrieve the exit status.

These states are not merely theoretical; they directly correspond to the state transitions that occur within the operating system kernel. Understanding these transitions helps in debugging performance issues and designing efficient applications.

### Process Control Block (PCB)

The Process Control Block is a data structure maintained by the operating system for each process. It serves as the repository of information about a process and contains the following critical components:

**Process Identification:** Each process is assigned a unique identifier (PID). The PCB stores this PID along with identifiers of the parent process (PPID), user identifier (UID), and group identifier (GID) for security and resource management purposes.

**Processor State Information:** This includes the contents of CPU registers, program counter, stack pointer, status registers, and condition codes. When a process is preempted (removed from CPU), the OS saves all these values to the PCB so that execution can resume exactly where it left off.

**Process Control Information:** This encompasses scheduling information (process priority, scheduling queue pointers), accounting information (CPU time used, elapsed time), memory management information (page tables, segment tables, limits), I/O status information (open files, pending signals), and other status information.

The PCB essentially acts as a snapshot of the entire execution context of a process. This context switching capability is what enables the operating system to rapidly switch between processes, creating the illusion of concurrent execution on a limited number of processors.

### Process vs Program

A common point of confusion is distinguishing between a program and a process. A program is a passive entity—a file containing instructions and data stored on disk. It has no life until executed. A process, on the other hand, is an active entity with a current state and activity. Multiple processes can execute the same program simultaneously; each will have its own process control block, its own memory space, and its own execution context.

Consider a text editor program stored on disk. When three users simultaneously open the same text editor application, three separate processes are created, although they all execute the same program code. Each process maintains its own document state, cursor position, and user interactions. This distinction is fundamental to understanding how operating systems achieve multi-tasking and resource isolation.

### Process Creation

In Unix-like systems, process creation follows a parent-child hierarchy. The fork() system call creates a new process by duplicating the calling process. The child process receives a copy of the parent's address space, including all open file descriptors and the program code. After fork(), both processes continue execution from the same point, but they can determine their identity using the getpid() system call. Typically, the child process then calls exec() to replace its memory space with a new program, enabling it to execute a different program than its parent.

In Windows, the CreateProcess() system call handles both creation and program loading in a single operation. The parent process specifies the executable file to run, and the OS creates a new process with its own address space and initial thread. Windows processes do not automatically share the parent's address space, though they can explicitly create shared memory regions.

Process creation involves significant overhead: allocating memory for the PCB and address space, initializing the process control block, setting up the memory management structures, copying or sharing resources from the parent, and adding the process to the appropriate scheduling queues. This overhead is why operating systems implement process pooling and thread creation as lighter-weight alternatives.

### Process Termination

A process terminates normally when it completes execution and calls the exit() system call (in Unix) or when the main function returns (which implicitly calls exit). The termination status is passed to the parent process, which can retrieve it using the wait() or waitpid() system calls. This mechanism allows the parent to determine whether the child completed successfully or encountered errors.

Abnormal termination occurs when the process receives an unhandled signal (such as SIGSEGV for segmentation fault or SIGINT for interrupt), when the parent process terminates the child using the kill() system call, or when the operating system terminates the process due to resource limits or severe errors. In all cases, the OS performs cleanup: closing remaining file descriptors, releasing memory, removing the process from scheduling queues, and deallocating the PCB.

### Types of Processes

Processes can be categorized based on their characteristics and behavior:

**Interactive Processes:** These processes are started by users and run in the foreground, requiring continuous user interaction. Examples include text editors, file managers, and terminal applications. They typically have a user interface and respond immediately to user input.

**Batch Processes:** These processes are submitted to the system in batches and executed without user interaction. They process large amounts of data or perform computational tasks that run for extended periods. Operating systems often schedule batch processes during off-peak hours to optimize resource utilization.

**Daemon Processes:** These are background processes that run continuously, providing system services. They are typically started at system boot and run until system shutdown. Examples include web servers (httpd), print spoolers (cupsd), and network services (sshd). Daemon processes usually have no controlling terminal and are orphaned from login sessions.

**Real-Time Processes:** These processes have strict timing requirements and must complete execution within specified time constraints. They are used in embedded systems, industrial control, and multimedia applications where delayed execution could cause system failure or quality degradation.

## Examples

### Example 1: Process State Transitions

Consider a simple C program that reads data from a file:

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    FILE *fp = fopen("data.txt", "r");
    char buffer[100];
    
    printf("Starting to read file...\n");
    fgets(buffer, 100, fp);  // This triggers I/O wait
    printf("Read complete: %s\n", buffer);
    fclose(fp);
    
    return 0;
}
```

When this program executes, the process undergoes the following state transitions:

1. **NEW to READY:** The OS loads the program into memory, creates the PCB, and places the process in the ready queue.

2. **READY to RUNNING:** The scheduler selects this process, loads its context into the CPU registers, and sets the program counter to the beginning of main().

3. **RUNNING to WAITING:** When fgets() requests I/O from the file, the OS initiates the disk operation and changes the process state to WAITING (blocked on I/O). The CPU is immediately freed for other ready processes.

4. **WAITING to READY:** When the disk operation completes, the OS receives an interrupt, updates the process's PCB, and moves it back to the READY queue.

5. **READY to RUNNING:** The scheduler again selects this process to resume execution, restoring its context from the PCB.

6. **RUNNING to TERMINATED:** When the program exits, the OS cleans up all resources and marks the process as TERMINATED.

### Example 2: Process Control Block Operations

When the Linux kernel performs a context switch between two processes (let's call them Process A and Process B), the following PCB operations occur:

**Saving Context of Process A:**
The scheduler saves the current CPU state to Process A's PCB, including the program counter (instruction pointer), all general-purpose registers, stack pointer, status flags, and memory management registers. This saved state becomes the resume point when Process A gets CPU time again.

**Updating Process A's State:**
The PCB state field is changed from RUNNING to either READY (if it was preempted by time slice expiration) or WAITING (if it blocked on I/O or synchronization). If it was preempted, Process A remains in the ready queue; otherwise, it moves to the appropriate wait queue.

**Loading Context of Process B:**
The scheduler loads the saved state from Process B's PCB into the CPU registers. This includes restoring the program counter to where Process B last stopped, restoring its stack pointer, and reinitializing memory management structures.

**Updating Process B's State:**
The PCB state field is changed from READY to RUNNING. The process now executes on the CPU.

This entire context switch operation typically takes only a few microseconds on modern hardware, but it represents one of the most frequent and performance-critical operations in the operating system.

### Example 3: Fork Operation in Unix

The following program demonstrates the fork() system call:

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();
    
    if (pid < 0) {
        printf("Fork failed\n");
        return 1;
    }
    else if (pid == 0) {
        // This code executes in child process
        printf("Child Process: PID = %d, Parent PID = %d\n", 
               getpid(), getppid());
        printf("Child is running a new program...\n");
        // In real programs, child would call exec() here
        return 0;
    }
    else {
        // This code executes in parent process
        printf("Parent Process: PID = %d, Child PID = %d\n", 
               getpid(), pid);
        
        int status;
        waitpid(pid, &status, 0);  // Wait for child to complete
        
        if (WIFEXITED(status)) {
            printf("Child exited with status: %d\n", 
                   WEXITSTATUS(status));
        }
    }
    
    return 0;
}
```

When executed, the fork() system call creates an almost exact copy of the parent process. Both processes continue execution from the same point, but they differ in the return value of fork(): the child receives 0, while the parent receives the child's PID. This return value allows the program to distinguish between parent and child execution paths.

The parent calls waitpid() to synchronize with the child's completion, ensuring the child terminates before the parent. This prevents the child from becoming a zombie process (a terminated process whose exit status hasn't been collected by the parent).

## Exam Tips

1. **Differentiate between program and process:** THIS IS A FREQUENT EXAMINATION QUESTION. Remember: a program is static (passive), while a process is dynamic (active).

2. **Draw process state diagrams:** BE ABLE TO SKETCH AND EXPLAIN THE FIVE-STATE PROCESS MODEL including all transitions (new to ready, ready to running, running to ready, running to waiting, waiting to ready, running to terminated).

3. **PCB components are crucial:** MEMORIZE THE MAJOR COMPONENTS OF PROCESS CONTROL BLOCK: process ID, parent ID, process state, program counter, CPU registers, memory limits, list of open files, and scheduling information.

4. **Understand context switching:** KNOW THAT CONTEXT SWITCH INVOLVES SAVING THE STATE OF THE CURRENTLY RUNNING PROCESS TO ITS PCB AND LOADING THE STATE OF THE NEW PROCESS FROM ITS PCB.

5. **Compare Unix and Windows process creation:** BE PREPARED TO EXPLAIN THE DIFFERENCES between fork()/exec() in Unix and CreateProcess() in Windows.

6. **Explain process states with examples:** IN EXAMINATIONS, PROVIDE CONCRETE EXAMPLES of when a process transitions between states (e.g., process running to waiting when waiting for keyboard input).

7. **Zombie and orphan processes:** UNDERSTAND THESE SPECIAL PROCESS STATES: zombie occurs when child terminates but parent hasn't called wait(); orphan occurs when parent terminates before child.

8. **Process vs thread distinction:** WHILE THE EXAMINATION TOPIC IS PROCESS CONCEPT, YOU MUST DISTINGUISH PROCESSES FROM THREADS as this is often tested alongside process concepts.