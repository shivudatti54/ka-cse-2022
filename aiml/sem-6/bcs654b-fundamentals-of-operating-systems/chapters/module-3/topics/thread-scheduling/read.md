# Thread Scheduling: Module 3 - Fundamentals of Operating Systems

## Introduction

In a multi-threaded environment, a single process can have multiple threads of execution. These threads, often called lightweight processes, share the process's code section, data section, and other OS resources but have their own registers, stack, and program counter. The CPU can only execute one thread at a time per core. **Thread Scheduling** is the fundamental mechanism used by the operating system to decide which of these many ready threads should run next on the available CPU cores. It is the core function that enables concurrency and parallelism, maximizing CPU utilization and improving application responsiveness.

## Core Concepts of Thread Scheduling

### 1. Contention Scope

Thread scheduling can occur at two levels, defining the "competition pool" for the CPU:

*   **Process-Contention Scope (PCS):** Scheduling is local to the process. The thread library (e.g., in user space) schedules user-level threads onto available Light Weight Processes (LWPs). The OS kernel is unaware of these user-level threads and only sees the single kernel-level thread it has assigned to the process. The choice of which user-level thread runs next is decided by a library function, not the OS scheduler.
*   **System-Contention Scope (SCS):** Scheduling is global. The OS kernel schedules all kernel-level threads across all processes. This is the classic and most common scheduling scenario. The kernel scheduler decides which kernel-level thread (which may be part of any process) runs on which CPU core.

### 2. The Role of the Thread Scheduler

The OS thread scheduler performs three primary tasks:

1.  **Scheduling:** It selects a thread from the **ready queue** based on a specific scheduling algorithm (e.g., Round Robin, Priority Scheduling).
2.  **Dispatching:** It performs the context switch, which involves:
    *   Switching the memory map (if needed).
    *   Saving the state (registers, PC, stack pointer) of the current thread.
    *   Loading the state of the new thread.
    *   Jumping to the location of the new thread's program counter.
3.  **Non-preemptive vs. Preemptive:** A key distinction in scheduling is when it occurs.
    *   **Non-preemptive:** A thread voluntarily yields the CPU, either by terminating or blocking (e.g., for I/O).
    *   **Preemptive:** The scheduler can forcibly interrupt a currently running thread after its time quantum expires or a higher-priority thread becomes ready. This is essential for ensuring fairness and system responsiveness.

### 3. Common Scheduling Algorithms

Several algorithms are used to decide the order of thread execution. Here are two prevalent ones:

*   **Round Robin (RR):** Each thread is assigned a fixed time unit called a **time quantum** or **time slice** (e.g., 10-100ms). The scheduler assigns the CPU to the first thread in the ready queue for only one time quantum. When the time expires, the thread is preempted and placed at the back of the ready queue.
    *   **Example:** Imagine three threads, T1, T2, and T3, in the ready queue. The scheduler gives T1 a 20ms quantum. If T1 doesn't block or finish, it's preempted after 20ms and moved to the back of the queue. T2 then gets 20ms, followed by T3. This cycle repeats, ensuring no thread is starved of CPU time.

*   **Priority Scheduling:** Each thread is assigned a priority. The scheduler always chooses the thread with the highest priority from the ready queue. To prevent starvation of lower-priority threads, **aging** is often used, where a thread's priority is gradually increased the longer it waits in the ready queue.

## Interaction with Thread Models

The scheduling behavior is heavily influenced by the thread model employed:

*   **Many-to-One Model (User Threads):** The OS schedules the single kernel thread (the LWP). The user-level thread library then decides which user thread runs within that scheduled kernel thread. This is **PCS**. If one user thread blocks, the entire process blocks.
*   **One-to-One Model (Kernel Threads):** Each user thread is mapped to a separate kernel thread. The OS scheduler directly handles each thread. This is **SCS**. It provides better concurrency (one thread blocking doesn't stop others) but creates more overhead for the OS.
*   **Many-to-Many Model:** Multiplexes many user threads onto a smaller or equal number of kernel threads. The OS scheduler manages the kernel threads (**SCS**), while the thread library schedules user threads onto them (**PCS**). This offers a balance between concurrency and efficiency.

## Key Points / Summary

| Key Point | Description |
| :--- | :--- |
| **Goal** | To maximize CPU utilization, ensure fairness, and minimize response time by deciding the order of thread execution. |
| **Contention Scope** | **PCS:** Scheduling among user-level threads (done by library). **SCS:** Scheduling among kernel-level threads (done by OS). |
| **Scheduler Operations** | Involves **scheduling** (selecting a thread), **dispatching** (context switching), and **preemption** (interrupting a running thread). |
| **Common Algorithms** | **Round Robin** uses time slices for fairness. **Priority Scheduling** uses thread priority, often with aging to prevent starvation. |
| **Dependency on Model** | The thread implementation model (Many-to-One, One-to-One, Many-to-Many) dictates whether scheduling occurs at the user level (PCS), kernel level (SCS), or both. |
| **Preemption** | Essential for a responsive multi-tasking system, allowing the OS to interrupt a thread that has exceeded its time quantum or to service a higher-priority task. |