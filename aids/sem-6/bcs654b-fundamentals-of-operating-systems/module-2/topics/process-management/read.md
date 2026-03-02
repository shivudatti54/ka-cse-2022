# Process Management in Operating Systems


## Table of Contents

- [Process Management in Operating Systems](#process-management-in-operating-systems)
- [Introduction](#introduction)
- [Process Fundamentals](#process-fundamentals)
  - [Process Definition](#process-definition)
  - [Process vs Program](#process-vs-program)
- [Process States and Transitions](#process-states-and-transitions)
  - [State Transition Diagram](#state-transition-diagram)
  - [Detailed State Descriptions](#detailed-state-descriptions)
- [Process Control Block (PCB)](#process-control-block-pcb)
- [Process Scheduling](#process-scheduling)
  - [Key Scheduling Criteria](#key-scheduling-criteria)
  - [Scheduling Algorithms](#scheduling-algorithms)
  - [Scheduling Example (FCFS vs SJF)](#scheduling-example-fcfs-vs-sjf)
- [Process Operations](#process-operations)
  - [1. Process Creation](#1-process-creation)
  - [2. Process Termination](#2-process-termination)
  - [3. Inter-Process Communication (IPC)](#3-inter-process-communication-ipc)
- [Multithreading Models](#multithreading-models)
  - [Thread vs Process](#thread-vs-process)
  - [Threading Models](#threading-models)
  - [Thread Libraries](#thread-libraries)
- [Real-World Applications](#real-world-applications)
- [Exam Tips](#exam-tips)

## Introduction

Process Management forms the core of modern operating systems, enabling efficient resource utilization and concurrent program execution. A process represents an executing instance of a program that requires various system resources including CPU time, memory, and I/O devices. The operating system's process manager handles process creation, scheduling, synchronization, and termination.

Effective process management is crucial for:

- Achieving **multiprogramming** through CPU sharing
- Maintaining **system stability** through process isolation
- Ensuring **fair resource allocation** via scheduling algorithms
- Enabling **inter-process communication** for collaborative tasks

Modern operating systems handle complex process management scenarios like:

- Real-time process prioritization in embedded systems
- Load balancing in cloud computing environments
- Context switching in multi-core processors

## Process Fundamentals

### Process Definition

A process is formally defined as:
**"An active entity representing a program in execution, comprising:"**

- Executable code (text section)
- Current activity (program counter, stack pointer)
- Data section (global variables)
- Heap (dynamically allocated memory)
- Stack (temporary function data)

```c
struct process {
 int pid;
 int state;
 int priority;
 struct page_table *mem_map;
 // ... other PCB components
};
```

### Process vs Program

| Aspect       | Program              | Process                |
| ------------ | -------------------- | ---------------------- |
| State        | Passive (on storage) | Active (in memory)     |
| Lifetime     | Permanent            | Temporary              |
| Resources    | None allocated       | System resources used  |
| Concurrency  | Single instance      | Multiple instances     |
| Dependencies | Independent          | Parent/child relations |

## Process States and Transitions

### State Transition Diagram

```
 +---------+ +---------+
 | New |------->| Ready |
 +---------+ +---------+
 ↑ ↓
 +---------+ +---------+
 | Terminated |<-----| Running |
 +---------+ +---------+
 ↑ |
 | ↓
 +---------+
 | Waiting |
 +---------+
```

### Detailed State Descriptions

1. **New**: Initial creation state (PCB allocated)
2. **Ready**: Process waiting in memory for CPU allocation
3. **Running**: Instructions being executed on CPU
4. **Waiting**: Process blocked for I/O or event completion
5. **Terminated**: Process finished (resources being released)

**State Transitions:**

- Admit (New → Ready)
- Schedule (Ready → Running)
- I/O Request (Running → Waiting)
- I/O Completion (Waiting → Ready)
- Exit (Running → Terminated)

## Process Control Block (PCB)

The PCB is the OS's data structure for process management:

**PCB Components:**

1. Process ID (PID)
2. Process State (Running/Waiting/etc.)
3. CPU Registers (Program Counter, Stack Pointer)
4. Memory Management Information
5. Accounting Data (CPU time used, limits)
6. I/O Status (Open files, devices in use)
7. Scheduling Information (Priority, queue pointers)

**Memory Layout:**

```
+-------------------+
| Stack | ← Dynamic growth
+-------------------+
| ↓ |
| |
| ↑ |
+-------------------+
| Heap | ← Dynamic allocation
+-------------------+
| Global/Static Data|
+-------------------+
| Program Code |
+-------------------+
```

## Process Scheduling

The OS uses scheduling algorithms to maximize CPU utilization and minimize wait time.

### Key Scheduling Criteria

- **CPU Utilization**: Percentage of time CPU is busy
- **Throughput**: Number of processes completed/time unit
- **Turnaround Time**: Completion time - Arrival time
- **Waiting Time**: Total time spent in ready queue
- **Response Time**: Time from request to first response

### Scheduling Algorithms

#### 1. First-Come, First-Served (FCFS)

- Non-preemptive
- Simple but causes convoy effect
- Example: Processes arriving in order P1(24ms), P2(3ms), P3(3ms)

#### 2. Shortest Job First (SJF)

- Optimal for minimum waiting time
- Can be preemptive (SRTF) or non-preemptive
- Example: Processes with burst times 6, 8, 7, 3

#### 3. Round Robin (RR)

- Preemptive with time quantum
- Fair allocation but high context switching
- Example: Quantum=4ms, Processes with bursts 24, 3, 3

#### 4. Priority Scheduling

- Can lead to starvation
- Aging technique used to prevent indefinite blocking

### Scheduling Example (FCFS vs SJF)

**Problem:**
Process | Arrival Time | Burst Time
--------|-------------|-----------
P1 | 0 | 6
P2 | 1 | 8
P3 | 2 | 7
P4 | 3 | 3

**FCFS Solution:**

```
Gantt Chart: |P1|6| → |P2|14| → |P3|21| → |P4|24|
Waiting Times:
P1: 0
P2: 6-1 = 5
P3: 14-2 = 12
P4: 21-3 = 18
Average Wait Time = (0+5+12+18)/4 = 8.75ms
```

**SJF Solution:**

```
Execution Order: P1(6), P4(3), P3(7), P2(8)
Gantt Chart: |P1|6| → |P4|9| → |P3|16| → |P2|24|
Waiting Times:
P1: 0
P4: 6-3 = 3
P3: 9-2 = 7
P2: 16-1 = 15
Average Wait Time = (0+3+7+15)/4 = 6.25ms
```

## Process Operations

### 1. Process Creation

- Methods: fork() (Unix), CreateProcess() (Windows)
- Parent-child relationships form process trees
- Copy-on-write optimization for efficient forking

### 2. Process Termination

- Normal exit vs abort (due to error)
- Zombie processes: Terminated but PCB remains
- Orphan processes: Parent dies before child

### 3. Inter-Process Communication (IPC)

- Shared Memory: Fast but requires synchronization
- Message Passing: Slower but better for distributed systems
- Pipes: | command in Unix shells

## Multithreading Models

### Thread vs Process

| Feature       | Process          | Thread              |
| ------------- | ---------------- | ------------------- |
| Resource      | Heavyweight      | Lightweight         |
| Memory        | Separate address | Shared address      |
| Creation      | Slow             | Fast                |
| Communication | Complex (IPC)    | Simple (shared mem) |

### Threading Models

1. **Many-to-One** (User-level Threads)

- Multiple user threads to single kernel thread
- Pros: Fast, portable
- Cons: Blocking system calls affect all threads

2. **One-to-One** (Kernel-level Threads)

- Each user thread maps to kernel thread
- Pros: Better concurrency
- Cons: Higher overhead

3. **Many-to-Many** (Hybrid Model)

- Multiplexes user threads to kernel threads
- Balances concurrency and efficiency

### Thread Libraries

1. **POSIX Pthreads** (Linux/Unix)

```c
pthread_create(&thread_id, NULL, func, arg);
```

2. **Windows Thread API**

```c
CreateThread(NULL, 0, func, param, 0, &id);
```

3. **Java Threads**

```java
Thread t = new Thread(RunnableObject);
t.start();
```

## Real-World Applications

- **Web Servers**: Thread pools handle concurrent requests
- **Database Systems**: Process isolation for transaction safety
- **Game Engines**: Separate threads for physics, rendering, AI
- **Scientific Computing**: Process-based parallelism with MPI

## Exam Tips

1. **PCB Components**: Always list 5+ elements with brief descriptions
2. **Scheduling Algorithms**: Practice Gantt charts for FCFS, SJF, RR
3. **Thread Advantages**: Focus on responsiveness, resource sharing
4. **State Transitions**: Draw diagram and explain each transition
5. **IPC Methods**: Compare shared memory vs message passing
6. **Zombie vs Orphan**: Define and explain handling mechanisms
7. **Multicore Scheduling**: Mention load balancing challenges

**Common Questions:**

- Compare process and thread (4 marks)
- Calculate waiting/turnaround time for SJF (6 marks)
- Explain PCB with diagram (5 marks)
- Difference between user and kernel threads (3 marks)
- Round Robin scheduling with time quantum (8 marks)
