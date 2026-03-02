# Overview of Process Management


## Table of Contents

- [Overview of Process Management](#overview-of-process-management)
- [What is a Process?](#what-is-a-process)
- [Process States](#process-states)
- [Process Control Block (PCB)](#process-control-block-pcb)
- [Process Scheduling](#process-scheduling)
  - [Context Switch](#context-switch)
- [Operations on Processes](#operations-on-processes)
  - [Process Creation](#process-creation)
  - [Process Termination](#process-termination)
- [Inter-Process Communication (IPC)](#inter-process-communication-ipc)
  - [Shared Memory](#shared-memory)
  - [Message Passing](#message-passing)
- [Exam Tips](#exam-tips)

## What is a Process?

A **process** is a program in execution. It is the fundamental unit of work in an operating system. While a program is a passive entity (an executable file stored on disk), a process is an active entity with a program counter specifying the next instruction to execute, along with a set of associated resources.

A process includes:

- **Text section**: The program code
- **Data section**: Global variables
- **Stack**: Temporary data (function parameters, return addresses, local variables)
- **Heap**: Dynamically allocated memory during process runtime
- **Program counter**: Address of the next instruction
- **CPU registers**: Current register values

## Process States

A process passes through several states during its lifetime:

```
 +-------+
 | New |
 +-------+
 | admitted
 v
 +-------+ scheduler dispatch +--------+
 +--->| Ready |------------------------->| Running|
 | +-------+ +--------+
 | ^ | | |
 | | interrupt (preemption) | | |
 | +-------------------------------+ | |
 | | |
 | I/O or event completion | | exit
 | +-------+ I/O or event wait | |
 +----| Wait |<-----------------------------+ |
 +-------+ v
 +-----------+
 | Terminated|
 +-----------+
```

1. **New**: The process is being created
2. **Ready**: The process is in memory, waiting to be assigned to the CPU
3. **Running**: Instructions are being executed on the CPU
4. **Waiting (Blocked)**: The process is waiting for some event (I/O completion, signal)
5. **Terminated**: The process has finished execution

## Process Control Block (PCB)

The PCB is the data structure that represents a process in the operating system. Each process has exactly one PCB. It contains:

| Field                      | Description                                       |
| -------------------------- | ------------------------------------------------- |
| **Process State**          | New, ready, running, waiting, or terminated       |
| **Program Counter**        | Address of next instruction to execute            |
| **CPU Registers**          | Contents of all process-centric registers         |
| **CPU Scheduling Info**    | Priority, scheduling queue pointers               |
| **Memory Management Info** | Page tables, segment tables, base/limit registers |
| **Accounting Info**        | CPU time used, time limits, process numbers       |
| **I/O Status Info**        | List of open files, I/O devices allocated         |

## Process Scheduling

The objective of multiprogramming is to keep the CPU busy at all times. The OS maintains several scheduling queues:

- **Job Queue**: Set of all processes in the system
- **Ready Queue**: Set of processes in main memory, ready and waiting to execute (linked list of PCBs)
- **Device Queues**: Set of processes waiting for an I/O device (each device has its own queue)

### Context Switch

When the CPU switches from one process to another:

1. Save the state of the old process in its PCB
2. Load the saved state for the new process from its PCB
3. This is **pure overhead** -- the system does no useful work during a context switch

Context-switch time depends on hardware support. Some processors provide multiple sets of registers, reducing the time required.

## Operations on Processes

### Process Creation

A process (the **parent**) creates new processes (the **children**), forming a tree of processes.

**In Unix/Linux:**

```c
pid_t pid = fork(); // Create child process

if (pid == 0) {
 // Child process
 execlp("/bin/ls", "ls", NULL); // Replace with new program
} else if (pid > 0) {
 // Parent process
 wait(NULL); // Wait for child to finish
}
```

- `fork()` returns 0 to the child, child's PID to the parent
- Child is a copy of parent's address space
- `exec()` replaces the process memory with a new program
- Parent may `wait()` for child to terminate

### Process Termination

A process terminates when it finishes executing its last statement and calls `exit()`:

- Output data from child to parent via `wait()`
- Process resources are deallocated by the OS
- **Zombie process**: Terminated child whose parent has not called `wait()` -- PCB entry remains
- **Orphan process**: Child whose parent terminated -- adopted by `init` (PID 1)

A parent may abort a child process using `kill()` if the child has exceeded resources or is no longer needed.

## Inter-Process Communication (IPC)

Processes may be **independent** (cannot affect or be affected by other processes) or **cooperating** (can affect or be affected by other processes).

### Shared Memory

- Processes share a region of memory
- Faster since no system calls needed for data access after setup
- Requires synchronization (e.g., semaphores) to prevent race conditions

### Message Passing

- Processes communicate through `send()` and `receive()` operations
- Easier to implement in distributed systems
- Slower due to system call overhead for each message
- Can be **direct** (name the recipient) or **indirect** (use mailboxes)
- Can be **synchronous** (blocking) or **asynchronous** (non-blocking)

## Exam Tips

1. **Know the process state diagram** -- draw it and label all transitions with their causes
2. **PCB contents** -- memorize all seven fields and what each stores
3. **fork() return values** -- 0 to child, child PID to parent; this is a very common exam question
4. **Context switch** -- understand it is pure overhead and what information is saved/loaded
5. **Zombie vs Orphan** -- know the precise definitions and how each is handled
6. **IPC comparison** -- shared memory (fast, needs sync) vs message passing (slower, OS-managed)
7. **Process vs Program** -- be clear: program = passive, process = active entity in execution
