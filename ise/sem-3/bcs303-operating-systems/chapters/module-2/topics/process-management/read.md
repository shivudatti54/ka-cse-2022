# Process Management

## Introduction

Process Management is a fundamental concept in operating systems that deals with the creation, scheduling, execution, and termination of processes. In any computer system, multiple programs need to run concurrently, and the operating system must manage these programs efficiently to ensure smooth functioning. A process is essentially a program in execution, and managing these processes is one of the most critical responsibilities of the operating system.

In the context of the University of Delhi's Computer Science curriculum, understanding Process Management is essential because it forms the backbone of modern operating systems. Whether you are preparing for internal assessments or end-semester examinations, this topic carries significant weight. The concepts covered here—process states, process control blocks, scheduling queues, and context switching—appear repeatedly in operating system design and implementation questions.

This chapter explores the theoretical foundations of process management along with practical implications. We will examine how the operating system maintains information about processes, how it schedules them for CPU execution, and how it handles operations like process creation and termination. These concepts are not merely academic; they directly relate to how your computer runs multiple applications simultaneously without interference.

## Key Concepts

### What is a Process?

A process is an instance of a program in execution. It is a dynamic entity—unlike a program, which is static. When you double-click an application icon, the operating system creates a process that executes the program's instructions. A process consists of the program code, current activity (program counter, registers), stack (temporary data like function parameters, return addresses), data section (global variables), and heap (dynamically allocated memory during execution).

In technical terms, a process is a unit of work in a modern computing system. The operating system must allocate resources to processes, including CPU time, memory, I/O devices, and file storage. Each process has its own address space, which ensures isolation between processes—this is a fundamental security feature that prevents one program from corrupting another's memory.

### Process States

A process can exist in multiple states throughout its lifetime. The typical states are:

**New State**: The process is being created. The operating system is performing administrative tasks like allocating memory and initializing the process control block.

**Ready State**: The process is waiting to be assigned to the CPU. All necessary resources except the CPU are available. The ready queue contains all processes in this state.

**Running State**: The process's instructions are being executed by the CPU. Only one process can be in the running state on a single-processor system at any given time.

**Waiting State**: The process is waiting for some event to occur, such as I/O completion, availability of a resource, or a signal from another process.

**Terminated State**: The process has finished execution. The operating system performs cleanup operations and reclaims all allocated resources.

These states are not arbitrary; they represent the logical progression of a process through the system. The transition from ready to running state occurs through a mechanism called dispatching, while the transition from running to waiting state happens when the process requests I/O or waits for an event.

### Process Control Block (PCB)

The Process Control Block is the most important data structure used by the operating system to manage processes. Think of the PCB as the "identity card" of a process. Each process has its own PCB that the operating system creates and maintains throughout the process's lifetime.

The PCB contains the following critical information:

**Process State**: The current state of the process (new, ready, running, waiting, or terminated).

**Program Counter**: The address of the next instruction to be executed for this process.

**CPU Registers**: The contents of all registers, including general-purpose registers, index registers, and stack pointers. These are necessary for context switching.

**Memory Management Information**: This includes base and limit registers, page tables, or segment tables that define the process's address space.

**Accounting Information**: CPU usage, time limits, process IDs, parent process ID, and other administrative data.

**I/O Status Information**: List of open files, pending I/O requests, and device allocation information.

The operating system maintains a queue of PCBs, organized by state. The ready queue contains PCBs of all processes in the ready state, while waiting queues contain PCBs of processes waiting for specific events.

### Process Scheduling

Process scheduling is the mechanism by which the operating system decides which process should occupy the CPU at any given time. Scheduling is essential because there are typically more processes than available CPU cores, and the system must allocate CPU time fairly and efficiently.

The **scheduler** is the component of the operating system responsible for this task. There are two main types:

**Long-Term Scheduler** (Admission Scheduler): This decides which processes are admitted to the system from the pool of new processes. It controls the degree of multiprogramming—the number of processes in memory. In modern systems, particularly time-sharing systems, this scheduler may be minimal or absent.

**Short-Term Scheduler** (CPU Scheduler): This selects one process from the ready queue and dispatches it to the CPU. This scheduler must be fast because it runs frequently (every few milliseconds).

**Medium-Term Scheduler**: This is found in some systems to improve performance by temporarily removing processes from memory (swapping) and bringing them back later.

### Operations on Processes

The operating system provides system calls for creating, terminating, and managing processes:

**Process Creation**: A process can create child processes using system calls like fork() in Unix/Linux or CreateProcess() in Windows. The parent process receives the child's process ID, while the child receives a return value of 0. This creates a parent-child relationship where the child typically executes a new program using exec() system call.

**Process Termination**: A process terminates when it completes execution, when it calls exit(), or when it is killed by another process. The operating system reclaims all resources—memory, open files, I/O devices—and removes the process from all queues.

**Process Synchronization**: When processes share resources, the operating system must ensure they do not interfere with each other. This leads to concepts like mutexes, semaphores, and monitors, which are covered in detail in the interprocess communication section.

### Context Switching

When the CPU switches from one process to another, the operating system must save the state of the currently running process and load the state of the newly selected process. This operation is called a context switch.

The context switch involves:
1. Saving the values of CPU registers, program counter, and other state information into the current process's PCB
2. Updating the process state from running to ready (or waiting)
3. Moving the current process's PCB to the appropriate queue
4. Selecting the next process from the ready queue
5. Loading the new process's state from its PCB into CPU registers
6. Updating the memory management hardware with the new process's address space

Context switching is a pure overhead operation—the CPU does no useful work during this time. The time required for a context switch depends on hardware support and the amount of state that must be saved and restored. In modern systems, this can range from a few microseconds to several milliseconds.

## Examples

### Example 1: Understanding Process States Through a Text Editor

Consider the scenario of using a text editor like Microsoft Word. When you open the application, the operating system creates a new process. The process first enters the NEW state as the system allocates memory and initializes data structures.

Once initialization is complete, the process moves to the READY state and joins the ready queue. When the CPU becomes available, the scheduler dispatches this process, and it enters the RUNNING state. The text editor begins executing—loading the graphical interface, initializing default settings, and preparing to accept user input.

Now, suppose you press Ctrl+S to save your document. The text editor process must perform disk I/O to write the file. Since I/O is slow compared to CPU operations, the process cannot continue until the write operation completes. The process therefore transitions from RUNNING to WAITING state. During this time, the CPU is free to execute other processes.

When the disk I/O completes, the disk controller generates an interrupt. The operating system handles this interrupt and moves the text editor process from the WAITING state back to the READY state. Eventually, when the scheduler selects it again, it returns to the RUNNING state and continues execution.

### Example 2: Process Creation in Unix

In Unix/Linux systems, process creation uses the fork() system call. Consider this C program:

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();
    
    if (pid == 0) {
        // This code executes in child process
        printf("I am the child process\n");
        execlp("/bin/ls", "ls", "-l", NULL);
    } else if (pid > 0) {
        // This code executes in parent process
        printf("I am the parent process, child PID = %d\n", pid);
        wait(NULL);
        printf("Child process terminated\n");
    } else {
        // fork() failed
        printf("Fork failed\n");
    }
    
    return 0;
}
```

When this program runs, fork() creates a new process. The child process gets a return value of 0, while the parent receives the child's process ID (a positive number). The child then uses execlp() to replace its program with the ls command. The parent uses wait() to wait for the child to complete before printing its termination message.

### Example 3: Context Switch Analysis

Consider a single-CPU system with two processes, P1 and P2, both in the ready queue. Initially, P1 is running. After a time quantum expires (in round-robin scheduling), the scheduler performs a context switch to run P2.

The context switch involves these steps:
1. Save P1's context: program counter (say 0x00401234), registers (EAX=10, EBX=20, etc.), and stack pointer
2. Update P1's PCB: change state from RUNNING to READY
3. Move P1's PCB to the ready queue
4. Select P2 from the ready queue
5. Load P2's context from its PCB: program counter (0x00567890), registers (EAX=100, EBX=200, etc.)
6. Update memory management unit with P2's page table
7. Change P2's state from READY to RUNNING
8. Jump to P2's program counter and resume execution

If each context switch takes 2 milliseconds, and the time quantum is 100 milliseconds, then 2% of CPU time is spent on overhead. This overhead increases with more processes and more frequent switches.

## Exam Tips

Understanding process management is crucial for both internal assessment and end-semester examinations. Here are the key points to remember:

1. **Distinguish between Program and Process**: A program is a passive entity (stored on disk), while a process is an active entity (in execution). This distinction is frequently tested in DU examinations.

2. **Remember All Five Process States**: The five states—new, ready, running, waiting, and terminated—must be memorized. Be prepared to draw state transition diagrams.

3. **PCB Contents are Important**: Know all components of the Process Control Block. Questions often ask you to list or explain what's stored in a PCB.

4. **Understand Scheduler Types**: Long-term, short-term, and medium-term schedulers have distinct functions. Long-term controls multiprogramming degree, short-term allocates CPU time.

5. **Context Switching Overhead**: Remember that context switching is pure overhead—it consumes CPU time without performing useful work. Know what information is saved and restored.

6. **Parent-Child Process Relationship**: When a parent process terminates before its child, the child becomes an orphan. When a child terminates but the parent doesn't wait for it, it becomes a zombie. These concepts are important.

7. **Real-World Examples Help**: In exams, use real-world analogies (like the text editor example) to explain concepts. Examiners appreciate practical understanding.

8. **Practice Diagrams**: Draw clear, labeled diagrams for process state transitions and scheduling queues. Visual representation often earns full marks.