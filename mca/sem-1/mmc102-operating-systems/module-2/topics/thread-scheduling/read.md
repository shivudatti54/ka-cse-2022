# Thread Scheduling


## Table of Contents

- [Thread Scheduling](#thread-scheduling)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Thread vs Process Scheduling](#thread-vs-process-scheduling)
  - [Thread Scheduling Approaches](#thread-scheduling-approaches)
  - [Scheduling Criteria](#scheduling-criteria)
  - [Scheduling Algorithms](#scheduling-algorithms)
  - [Thread Scheduling on Multiprocessor Systems](#thread-scheduling-on-multiprocessor-systems)
  - [Real-Time Thread Scheduling](#real-time-thread-scheduling)
- [Examples](#examples)
- [Exam Tips](#exam-tips)

## Introduction

Thread scheduling is a fundamental concept in modern operating systems that deals with the allocation of CPU time to threads within a process or across multiple processes. As multi-core processors have become ubiquitous, understanding thread scheduling has become essential for developing high-performance applications. Threads, being lightweight execution units within a process, require efficient scheduling mechanisms to maximize CPU utilization and system throughput.

In contemporary computing environments, where applications demand concurrent execution of multiple tasks, thread scheduling serves as the backbone of multitasking operating systems. Whether it is a web server handling numerous client requests simultaneously or a scientific application performing parallel computations, thread scheduling determines how effectively the system manages these competing demands for CPU time. The scheduler must balance multiple objectives including fairness, throughput, latency, and energy efficiency while making split-second decisions about which thread should execute at any given moment.

The evolution from single-threaded to multi-threaded operating systems has dramatically increased the complexity of scheduling decisions. Modern schedulers must consider not only which thread to run but also on which processor core, considering cache affinity, NUMA topology, and load balancing across multiple processing elements. This complexity reflects the underlying hardware architecture and directly impacts application performance.

## Key Concepts

### Thread vs Process Scheduling

While process scheduling deals with the allocation of CPU time to different processes, thread scheduling focuses on allocating CPU time among threads within the same process or across different processes. Threads within the same process share several resources including the address space, global variables, open files, and child processes. This shared nature of threads makes their scheduling distinct from process scheduling, as the scheduler must consider thread interactions and potential contention for shared resources.

The thread scheduler operates at a finer granularity than process scheduling. In a multi-threaded process, multiple threads can be simultaneously ready for execution, and the thread scheduler determines their order of execution on available CPU cores. This becomes particularly important in multi-core systems where thread placement directly impacts cache performance and overall system efficiency.

### Thread Scheduling Approaches

Thread scheduling can be implemented through different approaches depending on the relationship between user threads and kernel threads.

**User-Level Threads**: These threads are managed entirely by the thread library at the user level without kernel involvement. The application has complete control over thread scheduling, and the kernel remains unaware of thread existence within processes. User-level threads offer fast context switching (typically 1-3 microseconds) and allow application-specific scheduling algorithms. However, if any user thread makes a blocking system call, the entire process blocks, preventing other user threads from running. Additionally, user threads cannot take advantage of multiprocessing since the kernel sees only a single thread.

**Kernel-Level Threads**: The operating system kernel manages threads directly. The scheduler operates on threads rather than processes, and the kernel can schedule threads from different processes across multiple processors. While kernel-level threads avoid the blocking problem, they suffer from slower context switching (typically 10-30 microseconds) as every thread switch requires a mode transition between user and kernel modes.

**Hybrid Approaches**: Many modern operating systems use hybrid models combining advantages of both approaches. The many-to-many model maps many user threads to an equal or lesser number of kernel threads, allowing applications to create as many user threads as needed while enabling kernel-level load balancing across processors. Some systems use the two-level model where certain user threads are bound to specific kernel threads.

### Scheduling Criteria

The effectiveness of thread scheduling algorithms is measured using several criteria that capture different aspects of system performance.

**CPU Utilization**: The percentage of time the CPU is productively executing threads. In practical systems, CPU utilization should remain high, typically above 40% for batch systems and above 90% for interactive systems.

**Throughput**: The number of threads that complete execution per unit time. Higher throughput indicates better scheduling decisions that keep the CPU busy with productive work.

**Turnaround Time**: The total time from thread arrival (or creation) to thread completion. This includes waiting time in ready queue, execution time, and any I/O or synchronization delays.

**Waiting Time**: The total time a thread spends in the ready queue waiting for CPU allocation. This is a critical metric because it represents unproductive time from the thread's perspective. Algorithms are often compared based on average waiting time.

**Response Time**: The time from thread submission to when the thread starts producing output. This is particularly important for interactive and real-time systems where users or external events expect timely responses.

### Scheduling Algorithms

**First-Come, First-Served (FCFS)**: Threads are scheduled in the order of their arrival in the ready queue. This algorithm is simple to implement but can lead to the convoy effect where short threads wait behind long CPU-bound threads, resulting in poor average waiting time for short threads.

**Shortest Job First (SJF)**: The thread with the smallest CPU burst time is selected for execution next. SJF provides optimal average waiting time when all threads are available at time zero. However, it is difficult to implement in practice because CPU burst times are not known in advance. The algorithm can lead to starvation of long threads if short threads keep arriving.

**Priority Scheduling**: Each thread is assigned a priority, and the highest priority thread is scheduled first. Priorities can be either static (fixed at creation) or dynamic (adjusted based on thread behavior). A major problem is indefinite postponement or starvation of low-priority threads. Aging is a technique where waiting threads gradually increase in priority to prevent starvation.

**Round Robin (RR)**: Designed for time-sharing systems, RR cycles through all ready threads, allocating a fixed time quantum to each. The ready queue is treated as a circular buffer. The performance of RR heavily depends on the time quantum size—too small causes excessive context switching overhead, too large degenerates to FCFS.

**Multilevel Queue Scheduling**: Multiple separate queues are maintained for different classes of threads (system, interactive, batch, etc.). Each queue may use a different scheduling algorithm. Threads are permanently assigned to queues based on some property like priority or thread type.

**Multilevel Feedback Queue Scheduling**: This sophisticated algorithm allows threads to move between queues based on their CPU burst characteristics. CPU-bound threads sink to lower-priority queues with longer time quanta, while I/O-bound threads stay in higher-priority queues. This automatically prioritizes interactive threads while efficiently handling CPU-bound work.

### Thread Scheduling on Multiprocessor Systems

Modern computing environments frequently feature multi-core processors, introducing additional considerations for thread scheduling.

**Processor Affinity**: Modern schedulers attempt to keep a thread on the same processor where it previously executed, allowing reuse of cached data. Hard affinity allows processes to specify which processors they may run on, while soft affinity permits the scheduler to prefer certain processors without strict binding.

**Load Balancing**: The scheduler must distribute threads evenly across available processors to prevent some cores from being idle while others are overloaded. This can be achieved through work stealing or migration of threads from busy to idle processors.

**NUMA Awareness**: On systems with non-uniform memory access, thread placement affects memory access latency. The scheduler should prefer running threads on processors closest to their memory regions.

### Real-Time Thread Scheduling

Real-time systems require guarantees that threads meet their timing deadlines. Thread scheduling in real-time systems must be predictable and meet hard deadlines.

**Rate Monotonic Scheduling (RMS)**: A fixed-priority algorithm where shorter period threads receive higher priorities. Under certain assumptions (all threads are periodic, threads do not share resources, context switch time is negligible), RMS is provably optimal for fixed-priority scheduling.

**Earliest Deadline First (EDF)**: A dynamic priority algorithm where the thread with the nearest deadline is scheduled first. EDF can achieve higher CPU utilization than RMS but is more complex to analyze and implement.

## Examples

**Example 1: Round Robin Time Quantum Impact**

Consider three threads with CPU burst times of 10, 5, and 8 time units arriving simultaneously, with a time quantum of 4 units.

With quantum = 4:
- T1 executes 4 units, remaining = 6
- T2 executes 4 units, remaining = 1
- T3 executes 4 units, remaining = 4
- T1 executes 4 units, remaining = 2
- T2 executes 1 unit, remaining = 0 (complete)
- T3 executes 4 units, remaining = 0 (complete)
- T1 executes 2 units, remaining = 0 (complete)

Completion times: T1=24, T2=13, T3=17
Turnaround times: T1=24, T2=13, T3=17
Average turnaround time = (24 + 13 + 17) / 3 = 18 units
Waiting times: T1=24-10=14, T2=13-5=8, T3=17-8=9
Average waiting time = (14 + 8 + 9) / 3 = 10.33 units

With quantum = 8:
- T1 executes 8 units, remaining = 2
- T2 executes 5 units, remaining = 0 (complete)
- T3 executes 8 units, remaining = 0 (complete)
- T1 executes 2 units, remaining = 0 (complete)

Completion times: T1=18, T2=5, T3=13
Turnaround times: T1=18, T2=5, T3=13
Average turnaround time = (18 + 5 + 13) / 3 = 12 units
Average waiting time = (18-10 + 5-5 + 13-8) / 3 = 4.33 units

This demonstrates how larger time quanta can improve average waiting time but may increase response time for interactive threads.

**Example 2: Priority Scheduling with Aging**

Consider four threads with the following properties:

| Thread | Priority | Burst Time | Arrival |
|--------|----------|------------|---------|
| T1 | 10 (high) | 7 | 0 |
| T2 | 5 | 4 | 0 |
| T3 | 5 | 2 | 2 |
| T4 | 1 (low) | 3 | 3 |

Initial execution order (non-preemptive priority):
- Time 0-7: T1 runs (priority 10), completes at time 7
- Time 7-11: T2 runs (priority 5), waiting time = 7, completes at time 11
- Time 11-13: T3 runs (priority 5), waiting time = 11-2 = 9, completes at time 13
- Time 13-16: T4 runs (priority 1), waiting time = 13-3 = 10, completes at time 16

Without aging: T4 waits 10 time units while lower-priority threads run. This demonstrates starvation.

With aging implemented (+1 priority per 5 time units waiting):
- T4 waits from time 3 to 13 (10 units waiting)
- After 5 units waiting: priority increases from 1 to 2
- After 10 units waiting: priority increases to 3
- Even with aging, T4 still runs last but the waiting time is bounded

This example illustrates how aging prevents indefinite postponement in priority scheduling systems.

**Example 3: Multilevel Feedback Queue Scheduling**

Consider threads with different CPU burst patterns entering a three-level queue system:

- Q0: Round Robin, quantum = 8 (highest priority)
- Q1: Round Robin, quantum = 16
- Q2: First-Come, First-Served (lowest priority)

Thread A: CPU-bound, needs 20 time units of CPU
- Enters Q0, runs for 8 units (quantum exhausted)
- Demoted to Q1, runs for 16 units (quantum exhausted)
- Demoted to Q2, completes remaining 6 units
- Total execution time longer due to lower priority queue

Thread B: I/O-bound, frequently blocks for I/O
- Enters Q0, runs for 3 units then blocks
- Returns to Q0 at higher priority
- Runs again for 4 units then blocks
- Quickly completes in Q0 due to frequent I/O

This demonstrates how MLFQ automatically prioritizes interactive I/O-bound threads while fairly handling CPU-bound work.

## Exam Tips

For the University of Delhi MCA semester examination, the following points are essential for the thread scheduling topic.

1. Memorize the five scheduling criteria: CPU utilization, throughput, turnaround time, waiting time, and response time. Understand that SJF provides optimal average waiting time but is not practical without known burst times.

2. When solving Round Robin problems, always list threads in execution order, track the remaining burst time after each quantum, and calculate waiting time as turnaround time minus burst time. The time quantum selection is crucial—a very small quantum increases context switch overhead, while a very large quantum degrades to FCFS.

3. Distinguish clearly between preemptive and non-preemptive scheduling. Preemptive versions (like preemptive SJF or round robin) allow higher-priority or newly arrived threads to interrupt currently running threads.

4. For priority scheduling problems, remember to address starvation and explain aging as a solution. A thread with lower priority gradually increases its priority the longer it waits in the ready queue.

5. Understand the differences between user-level and kernel-level threads. User-level threads are fast to create and switch but cannot exploit multiprocessing, while kernel-level threads can run on multiple processors but have higher overhead.

6. On multiprocessor systems, focus on three key concepts: processor affinity (keeping threads on the same CPU for cache efficiency), load balancing (distributing work evenly), and NUMA awareness (placing threads near their memory).

7. For real-time scheduling, remember that Rate Monotonic assigns fixed priorities based on period (shorter period equals higher priority), while Earliest Deadline First uses dynamic priorities based on absolute deadlines.

8. When comparing algorithms in numerical problems, compute average waiting time and average turnaround time for each algorithm under the given thread arrival and burst patterns to determine which performs better for specific workloads.