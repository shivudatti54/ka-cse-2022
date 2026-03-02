# Module 3: Thread Scheduling

---

## 1. Introduction

In a modern operating system, the number of active threads often far exceeds the number of available CPU cores. This creates a fundamental problem: how does the OS decide which thread to run on which core and for how long? The solution is **Thread Scheduling**—the method by which the system's kernel allocates precious CPU time to threads. Effective scheduling is crucial for ensuring system responsiveness, fairness among processes, and optimal utilization of hardware resources.

## 2. Core Concepts of Thread Scheduling

Thread scheduling builds upon process scheduling concepts but operates at a more granular level. The scheduler is a key component of the OS kernel that makes these decisions.

### The Thread Scheduler

The scheduler's primary goal is to distribute CPU time slices (or quanta) to the pool of available threads. It operates based on a **scheduling algorithm** and maintains several key data structures:

- **Ready Queue:** A queue (or multiple queues) that holds all threads that are in the "Ready" state, meaning they are prepared to execute and are waiting for CPU time.
- **Context Switch:** The process of saving the state of a currently running thread and loading the saved state of a new one. This overhead is a critical factor in scheduling efficiency.

### Scheduling Algorithms

The choice of scheduling algorithm drastically affects system performance. Two primary categories exist:

#### A. Non-Preemptive Scheduling

Once a thread is allocated the CPU, it keeps it until it terminates or voluntarily blocks (e.g., for an I/O operation).

- **Example: First-Come, First-Served (FCFS)**
- Threads are executed in the order they arrive in the ready queue.
- **Advantage:** Simple to implement.
- **Disadvantage:** Can lead to poor average waiting times. A long CPU-bound thread can block all others, causing the "convoy effect."

#### B. Preemptive Scheduling

The scheduler can interrupt a currently running thread before it completes or voluntarily blocks. This allows the OS to prioritize more important or interactive threads.

- **Example: Round-Robin (RR)**
- Each thread is assigned a fixed **time quantum** (e.g., 10-100ms). The scheduler cycles through the ready queue, allocating the CPU to each thread for one time quantum. If a thread doesn't complete, it is preempted and placed back at the end of the queue.
- **Advantage:** Excellent for time-sharing systems; ensures fairness and good response time for interactive threads.
- **Disadvantage:** High context switch overhead if the time quantum is set too low.

- **Example: Priority Scheduling**
- Each thread is assigned a priority. The highest-priority thread in the ready queue gets the CPU next.
- Preemptive version: If a high-priority thread becomes ready, it can preempt a currently running lower-priority thread.
- **Challenge: Starvation** - Low-priority threads may never get CPU time. This is often mitigated by **aging**, where a thread's priority is gradually increased the longer it waits.

### User-Level vs. Kernel-Level Threads

The OS scheduling policy interacts differently with the thread model:

- **Kernel-Level Threads (KLTs):** The OS kernel is aware of and manages the threads. The scheduler directly schedules threads onto CPU cores. This allows true parallel execution on multicore systems.
- **User-Level Threads (ULTs):** Managed by a thread library at the application level (e.g., POSIX Pthreads). The OS only sees the single process and schedules it. The process's internal thread scheduler then decides which ULT runs. The downside is that if one ULT blocks (e.g., on I/O), the entire process blocks, as the OS is unaware of the other threads.

Most modern systems (like Windows and Linux) use a hybrid model, often mapping multiple ULTs to a smaller pool of KLTs, combining the flexibility of ULTs with the scheduling efficiency of KLTs.

## 3. Example Scenario

Imagine a system using a **Preemptive Priority Round-Robin** algorithm. It has three threads:

- **Thread A (High Priority, CPU-bound):** Quantum = 30ms
- **Thread B (Low Priority, Interactive):** Quantum = 30ms
- **Thread C (Medium Priority, I/O-bound):** Quantum = 30ms

1. Thread A runs for its full 30ms quantum but isn't finished. Due to its high priority, it might go to the front of the queue instead of the back.
2. Thread B (interactive) is scheduled next. After just 5ms, it issues an I/O request and blocks. The scheduler immediately preempts it and saves its state.
3. With Thread B blocked, Thread C gets the CPU.
4. When Thread B's I/O completes, it becomes ready again. Because it's interactive and yielded the CPU quickly, its effective priority might be boosted. It could preempt the currently running medium-priority Thread C to provide a responsive user experience.

## 4. Key Points & Summary

- **Purpose:** The thread scheduler allocates CPU time to threads to maximize CPU utilization, ensure responsiveness, and enforce fairness.
- **Preemption:** Preemptive scheduling (e.g., Round-Robin) is essential for interactive systems, allowing the OS to stop one thread to run another.
- **Algorithm Choice:** The scheduling algorithm (FCFS, RR, Priority) defines the policy for ordering the ready queue and has direct impact on performance metrics like throughput, turnaround time, and waiting time.
- **Starvation:** A risk in priority-based systems where low-priority threads may never run. Aging is a common solution.
- **Model Interaction:** The OS schedules kernel threads. User-level threads are scheduled within their process, which can lead to blocking if not managed carefully. Modern OSes use a hybrid approach for efficiency.

Understanding thread scheduling is fundamental to grasping how an OS manages complexity and delivers a seamless multi-tasking experience.
