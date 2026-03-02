# Process Management in Operating Systems


## Table of Contents

- [Process Management in Operating Systems](#process-management-in-operating-systems)
- [1. Introduction and Fundamental Concepts](#1-introduction-and-fundamental-concepts)
  - [1.1 Formal Definition](#11-formal-definition)
  - [1.2 Process Memory Layout](#12-process-memory-layout)
- [2. Process States](#2-process-states)
  - [2.1 State Definitions](#21-state-definitions)
  - [2.2 State Transition Diagram](#22-state-transition-diagram)
  - [2.3 Additional Process States](#23-additional-process-states)
- [3. Process Control Block (PCB)](#3-process-control-block-pcb)
  - [3.1 PCB Structure](#31-pcb-structure)
  - [3.2 Context Switching](#32-context-switching)
- [4. Process Scheduling](#4-process-scheduling)
  - [4.1 Scheduling Queues](#41-scheduling-queues)
  - [4.2 Types of Schedulers](#42-types-of-schedulers)
  - [4.3 Scheduling Criteria](#43-scheduling-criteria)
  - [4.4 Scheduling Algorithms](#44-scheduling-algorithms)
- [5. Process Operations](#5-process-operations)
  - [5.1 Process Creation](#51-process-creation)
  - [5.2 Process Termination](#52-process-termination)
  - [5.3 Inter-Process Communication (IPC)](#53-inter-process-communication-ipc)
- [6. Conclusion](#6-conclusion)

## 1. Introduction and Fundamental Concepts

Process management constitutes one of the most critical functions of any modern operating system. It encompasses the creation, scheduling, termination, and synchronization of processes—the fundamental units of work within a computing system. The efficiency of process management directly determines CPU utilization, system throughput, and overall system responsiveness.

An **operating system process** represents a program in execution. The distinction between a program and a process is fundamental: a program constitutes a passive entity stored on disk as an executable file, while a process is an active entity with its own execution context, including a program counter, CPU registers, and allocated resources.

### 1.1 Formal Definition

A process can be formally defined as:

> "A process is a program in execution, consisting of the program code, current activity represented by the program counter, contents of processor registers, stack containing temporary data, heap for dynamic memory allocation, data section containing global variables, and various system resources it has acquired."

### 1.2 Process Memory Layout

A process in memory is organized into distinct segments:

```
Address Space:
+-------------------------+ High Address (0xFFFFFFFF)
| Stack | ← Function parameters, return addresses,
| ↓ | local variables, automatic variables
+-------------------------+
| |
| (Unused/Gap) |
| |
+-------------------------+
| ↑ |
| Heap | ← Dynamically allocated memory (malloc, new)
+-------------------------+
| Data | ← Initialized and uninitialized global/static
| (BSS + Data) | variables
+-------------------------+
| Text | ← Program code (instructions), read-only
+-------------------------+ Low Address (0x00000000)
```

The **text segment** contains the compiled machine code instructions and is typically read-only to prevent accidental modification. The **data segment** stores initialized global and static variables, while the **BSS segment** (Block Started by Symbol) holds uninitialized global and static variables initialized to zero. The **heap** grows upward during dynamic memory allocation, and the **stack** grows downward for function calls, storing return addresses, parameters, and local variables.

## 2. Process States

A process transitions through various states throughout its lifetime. The operating system maintains the current state of each process to manage execution and resource allocation effectively.

### 2.1 State Definitions

| State          | Description                                                                                                    |
| :------------- | :------------------------------------------------------------------------------------------------------------- |
| **New**        | The process is being created. The OS is loading program code and initializing the PCB.                         |
| **Ready**      | The process is loaded in main memory and waiting for CPU allocation. It resides in the ready queue.            |
| **Running**    | Instructions are actively executing on the CPU. The process has control of the processor.                      |
| **Waiting**    | The process cannot continue execution until some event occurs (I/O completion, signal, resource availability). |
| **Terminated** | The process has completed execution or has been explicitly terminated. The OS reclaims its resources.          |

### 2.2 State Transition Diagram

```
 +-------+
 | New | (Process creation)
 +---+---+
 | admit
 v
 +----------+ dispatch +-----------+
 | Ready |<------------| Running |
 +----+-----+ +-----+-----+
 ^ |
 | I/O or event | timeout / preempt
 | complete v
 | +-----------+
 +--------------------| Waiting |
 +-----------+

 Running ---> exit ---> Terminated
```

**Critical Note:** On a single-processor system, exactly one process can occupy the **Running** state at any instant. Multiple processes may simultaneously occupy the **Ready** and **Waiting** states, managed through various queue structures.

### 2.3 Additional Process States

Modern operating systems often include intermediate states:

- **Suspended**: Process swapped out to secondary storage (not in memory)
- **Zombie**: Process terminated but parent has not yet read its exit status
- **Stopped**: Process halted by a signal (debugging)

## 3. Process Control Block (PCB)

The operating system represents each process using a data structure called the **Process Control Block (PCB)** or **Task Control Block**. The PCB serves as the repository of all information necessary for the OS to manage process execution.

### 3.1 PCB Structure

| Component                  | Description                                                            |
| :------------------------- | :--------------------------------------------------------------------- |
| **Process State**          | Current state (new, ready, running, waiting, terminated)               |
| **Process ID (PID)**       | Unique positive integer identifier                                     |
| **Program Counter (PC)**   | Address of the next instruction to execute                             |
| **CPU Registers**          | Accumulator, index registers, stack pointer, general-purpose registers |
| **CPU Scheduling Info**    | Process priority, pointer to scheduling queue, scheduling parameters   |
| **Memory Management Info** | Base register, limit register, page tables, segment tables             |
| **Accounting Info**        | CPU time used, time limits, process number, parent process ID          |
| **I/O Status Info**        | List of open files, allocated I/O devices, pending signals             |

### 3.2 Context Switching

When the CPU switches from one process to another, the OS must save the complete execution state of the current process into its PCB and restore the state of the newly scheduled process. This operation is called a **context switch**.

**Context Switch Steps:**

1. Save the current process's context (registers, PC, state) into its PCB
2. Update the PCB state from Running to Ready or Waiting
3. Select the next process from the ready queue
4. Load the selected process's context from its PCB
5. Update memory management registers (MMU)
6. Resume execution from the saved program counter

The time required for a context switch represents pure overhead—the CPU performs no useful work during this period. Context switch times typically range from 1 to 1000 microseconds, depending on the architecture and OS design.

## 4. Process Scheduling

Process scheduling is fundamental to achieving **multiprogramming** (maximizing CPU utilization by keeping it busy) and **time sharing** (enabling user interaction with multiple processes).

### 4.1 Scheduling Queues

The OS maintains several scheduling queues:

- **Job Queue**: Contains all processes in the system, including those not yet in memory
- **Ready Queue**: Processes residing in main memory, ready to execute, typically implemented as a linked list with PCB pointers
- **Device Queues**: Processes waiting for specific I/O devices, each device has its own queue

### 4.2 Types of Schedulers

| Scheduler            | Execution Frequency     | Function                                                                                              |
| :------------------- | :---------------------- | :---------------------------------------------------------------------------------------------------- |
| **Long-term (Job)**  | Infrequent (seconds)    | Selects processes from job pool and loads them into ready queue. Controls degree of multiprogramming. |
| **Short-term (CPU)** | Frequent (milliseconds) | Selects from ready queue and dispatches to CPU. Must be fast to minimize dispatch latency.            |
| **Medium-term**      | Intermittent            | Temporarily removes processes from memory to reduce degree of multiprogramming (swapping).            |

### 4.3 Scheduling Criteria

Various criteria evaluate scheduling algorithm effectiveness:

- **CPU Utilization**: Percentage of time the CPU is actively executing processes (target: 40-90%)
- **Throughput**: Number of processes completed per unit time
- **Turnaround Time**: Time from process submission to completion (waiting + execution + I/O)
- **Waiting Time**: Total time spent in the ready queue
- **Response Time**: Time from request submission to first response (crucial for interactive systems)

**Mathematical Relationships:**

```
Turnaround Time = Waiting Time + Burst Time + I/O Time
Response Time ≤ Turnaround Time (by definition)
```

### 4.4 Scheduling Algorithms

#### First-Come-First-Served (FCFS)

Processes are served in order of arrival. Simple to implement using FIFO queue. Suffers from convoy effect where short processes wait behind long processes.

#### Shortest Job First (SJF)

Selects process with smallest burst time. Provides optimal average waiting time but requires knowledge of future CPU bursts (impractical). Variants include Shortest Remaining Time First (preemptive SJF).

#### Priority Scheduling

Processes are assigned priorities; highest priority process runs first. May suffer from **starvation** (low-priority processes may never execute). Aging technique can mitigate starvation by gradually increasing priority of waiting processes.

#### Round Robin (RR)

Each process receives a fixed time quantum (slice). Processes are cycled through in FCFS order. Performance depends critically on quantum size:

- **Large quantum**: Approaches FCFS, poor response time
- **Small quantum**: High context switch overhead, good response time

**Optimal quantum**: Should be large enough that 80% of CPU bursts are shorter than the quantum.

#### Multilevel Queue Scheduling

Multiple ready queues with different priorities. Processes are permanently assigned to one queue. Each queue may use different scheduling algorithms (e.g., system processes use FCFS, interactive processes use RR).

#### Multilevel Feedback Queue

Similar to multilevel queue but allows process migration between queues. Processes that use too much CPU are moved to lower-priority queues, while I/O-bound processes remain in higher-priority queues. This approach approximates Shortest Job First adaptively.

## 5. Process Operations

### 5.1 Process Creation

A process (parent) can create new processes (children) using system calls:

```
PID = fork() // Creates new process
if (PID == 0) {
 exec(program) // Replace current process image
}
```

**UNIX/Linux system calls:**

- `fork()`: Creates a new process with copied address space
- `exec()`: Replaces the current process image with a new program
- `wait()`: Parent waits for child to terminate
- `exit()`: Process terminates and returns status

### 5.2 Process Termination

A process terminates when:

1. It reaches its final statement
2. It calls `exit()` system call
3. It receives a termination signal
4. An error occurs (division by zero, illegal memory access)

The parent may retrieve the child's exit status using `wait()`. If the parent does not call `wait()`, the child becomes a **zombie** process.

### 5.3 Inter-Process Communication (IPC)

Processes often require communication and synchronization:

- **Shared Memory**: Multiple processes access common memory region
- **Message Passing**: Processes exchange messages through OS kernel
- **Pipes**: Unidirectional byte stream between related processes
- **Sockets**: Network-based communication
- **Signals**: Asynchronous notifications

## 6. Conclusion

Process management forms the backbone of operating system functionality, enabling multiprogramming, time sharing, and efficient resource utilization. Understanding process states, the PCB structure, scheduling algorithms, and process creation/termination mechanisms is fundamental to comprehending how operating systems manage concurrent execution and provide the illusion of parallelism on single and multi-processor systems.
