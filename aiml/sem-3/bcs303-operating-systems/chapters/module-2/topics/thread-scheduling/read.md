# Thread Scheduling

## Introduction

Thread scheduling is a fundamental concept in operating systems that determines how CPU time is allocated among competing threads within a multithreaded process or across multiple processes. As modern operating systems increasingly adopt multithreading as a primary paradigm for achieving concurrency and parallelism, understanding thread scheduling becomes essential for developing efficient and responsive applications. Unlike process scheduling, which deals with entire processes, thread scheduling operates at a finer granularity, managing individual threads within processes. This distinction is crucial because threads within the same process share many resources, including the address space, open files, and global variables, making thread switching less expensive than process context switches while introducing unique scheduling challenges.

The importance of thread scheduling extends across various computing domains. In real-time systems, proper thread scheduling ensures that time-critical tasks meet their deadlines. In server environments, effective thread pooling and scheduling directly impact throughput and responsiveness. For interactive applications, scheduling decisions determine whether the system feels responsive or sluggish to users. University of Delhi's Computer Science curriculum recognizes this significance, and thread scheduling forms a critical component of operating system studies, frequently appearing in semester examinations with both theoretical and practical questions.

## Key Concepts

### Thread Scheduling vs Process Scheduling

While process scheduling and thread scheduling share similar goals—efficient CPU allocation—they differ in significant ways. Process scheduling decides which process gets the CPU when, considering entire processes as scheduling entities. Thread scheduling, on the other hand, works within the framework established by process scheduling. When the operating system schedules a process to run, the thread scheduler within that process (or the OS thread scheduler) determines which thread within the process should execute. Threads within the same process can often run in parallel on multi-core systems, whereas processes are typically isolated scheduling entities.

The shared nature of process resources among threads creates unique scheduling considerations. When a thread blocks on I/O, other threads in the same process can continue executing. When a thread enters a critical section, the scheduler must ensure other threads don't cause race conditions. These considerations distinguish thread scheduling from its process-level counterpart and require careful algorithm design.

### Thread Scheduling Models

Operating systems implement thread scheduling through two primary models based on contention scope: Process Contention Scope (PCS) and System Contention Scope (SCS).

**Process Contention Scope (PCS)** occurs when threads compete for execution resources within the same process. The scheduling decision is made among threads belonging to the same process, typically managed by a thread library at user level. This model is common in many-to-one and many-to-many threading models where the thread library handles scheduling of user-level threads onto available lightweight processes or kernel threads. In PCS, the operating system is not directly aware of individual thread priorities or states; it only sees the process as a single scheduling entity.

**System Contention Scope (SCS)** involves competition among all threads in the system, regardless of which process they belong to. The operating system's kernel directly manages these threads, making scheduling decisions based on system-wide criteria. One-to-one threading models (where each user thread maps to a kernel thread) typically use SCS, giving the OS full control over thread prioritization and scheduling. This provides better control over system resources but may require more kernel overhead.

### Scheduling Criteria

The effectiveness of thread scheduling algorithms is evaluated using several standard criteria, each measuring a different aspect of system performance:

**CPU Utilization** measures the percentage of time the CPU is actively executing useful work. In a well-scheduled system, CPU utilization should remain high, minimizing idle time. For thread scheduling, this means keeping the CPU busy with productive threads rather than having it wait for I/O or context switches.

**Throughput** refers to the number of threads (or processes) completed per unit time. Higher throughput indicates the system is completing more work efficiently. For thread scheduling, this involves minimizing overhead from excessive context switches while ensuring all threads get fair CPU time.

**Turnaround Time** is the total time from thread creation (or ready state) to thread completion. This includes waiting time in ready queue, execution time, and any I/O time. Minimizing turnaround time is particularly important for batch processing scenarios.

**Waiting Time** specifically measures the time a thread spends in the ready queue waiting for CPU allocation. Different algorithms impact waiting time differently, and minimizing waiting time generally improves system responsiveness.

**Response Time** is crucial for interactive systems—the time from thread request to first CPU allocation. For user-facing applications, minimizing response time ensures the system feels responsive to users.

### Thread Scheduling Algorithms

#### First-Come, First-Served (FCFS)

The simplest scheduling algorithm, FCFS (also known as First-In-First-Out) schedules threads in the order they arrive in the ready queue. While easy to implement, FCFS can lead to poor average waiting times and the "convoy effect" where short threads wait behind long ones. Consider three threads with burst times (execution times) of 24, 3, and 3 units arriving in order:

With FCFS, if thread T1 arrives first followed by T2 and T3, the waiting times are: T1 = 0, T2 = 24, T3 = 27. Average waiting time = (0 + 24 + 27)/3 = 17 units. However, if they arrived in order T2, T3, T1, average waiting time would be (0 + 3 + 6)/3 = 3 units, demonstrating FCFS's sensitivity to arrival order.

#### Shortest Job First (SJF)

SJF selects the thread with the smallest burst time from the ready queue. This optimal algorithm minimizes average waiting time for a known set of threads. In the previous example, with burst times 24, 3, 3, SJF would schedule the two 3-unit threads first, achieving optimal average waiting time. However, SJF requires advance knowledge of thread execution times, which is rarely available in practice. A preemptive version called Shortest Remaining Time First (SRTF) can address this limitation by preempting when a shorter thread arrives.

#### Round Robin (RR)

Round Robin allocates CPU time in fixed time slices (quantum) to each thread in a cyclic manner. This approach ensures no thread starves and provides fair distribution of CPU time. The time quantum size critically impacts performance: too small causes excessive context switching overhead, too large degrades to FCFS. The average waiting time under RR depends on the quantum size and thread characteristics. For threads with similar burst times, RR performs well; for long-running threads, waiting time increases proportionally to burst time.

#### Priority Scheduling

Priority scheduling assigns priority levels to threads and schedules the highest-priority ready thread. Priority can be static (fixed) or dynamic (changing based on behavior). A major concern is starvation—low-priority threads may wait indefinitely if higher-priority threads continuously arrive. Aging (gradually increasing priority of waiting threads) addresses this issue. Priority can be based on various factors including user importance, thread type, or computational requirements.

#### Multilevel Queue Scheduling

This algorithm organizes ready threads into multiple separate queues, each with its own scheduling algorithm. Common implementations include a system process queue (using FCFS), an interactive process queue (using RR), and a batch process queue (using FCFS). Threads are permanently assigned to one queue based on their characteristics. The scheduler first attempts to schedule from the highest-priority non-empty queue, ensuring critical work gets priority while maintaining fairness within each queue.

#### Multilevel Feedback Queue (MLFQ)

MLFQ addresses the limitations of multilevel queue by allowing threads to move between queues based on their behavior. CPU-intensive threads that use complete time quanta move to lower-priority queues, while interactive threads that frequently block (for I/O) remain in higher-priority queues. This approach automatically adapts to thread behavior, favoring interactive work while ensuring CPU-intensive tasks eventually complete. The ability to change priority provides dynamic responsiveness that static priority systems lack.

### Real-Time Thread Scheduling

Real-time systems require deterministic scheduling behavior where tasks must complete within specified time constraints. Two primary real-time scheduling algorithms are commonly used:

**Rate Monotonic Scheduling (RMS)** assigns fixed priorities based on task frequency—higher frequency tasks receive higher priorities. Under certain conditions (bounded CPU utilization), RMS can guarantee all deadlines are met. The feasibility bound is approximately 69% for n tasks, meaning CPU utilization must stay below this threshold for guaranteed schedulability.

**Earliest Deadline First (EDF)** dynamically schedules tasks based on their upcoming deadlines. The task with the earliest deadline always runs next. EDF is optimal and can achieve up to 100% CPU utilization while meeting deadlines, making it more efficient than RMS. However, EDF requires runtime deadline tracking and may have more overhead.

### Multiple-Processor Scheduling

Thread scheduling becomes significantly more complex on multi-processor and multi-core systems. Key considerations include:

**Processor Affinity** refers to the tendency of a thread to prefer running on the same processor where it previously executed. Maintaining affinity improves performance by avoiding cache reload costs. Soft affinity allows movement between processors when beneficial, while hard affinity restricts threads to specific processors.

**Load Balancing** ensures work is evenly distributed across processors. This can be push-based (periodic checks moving work from busy to idle processors) or pull-based (idle processors actively take work). The goal is maximizing parallelism while minimizing migration overhead.

**Cache Coherency** issues arise when threads on different processors access shared data. Proper scheduling can minimize false sharing and cache invalidations by grouping related threads on the same processor cluster.

## Examples

### Example 1: Calculating Waiting Time for FCFS and SJF

Consider four threads with the following burst times (in milliseconds): T1 = 8, T2 = 4, T3 = 2, T4 = 6. Arrival order is T1, T2, T3, T4 at time 0.

**FCFS Scheduling:**
- T1 executes from 0 to 8 → Waiting time = 0
- T2 executes from 8 to 12 → Waiting time = 8
- T3 executes from 12 to 14 → Waiting time = 12
- T4 executes from 14 to 20 → Waiting time = 14
- Average waiting time = (0 + 8 + 12 + 14) / 4 = 34/4 = 8.5 ms

**SJF Scheduling:**
- Sort by burst time: T3 (2), T2 (4), T4 (6), T1 (8)
- T3 executes from 0 to 2 → Waiting time = 0
- T2 executes from 2 to 6 → Waiting time = 2
- T4 executes from 6 to 12 → Waiting time = 6
- T1 executes from 12 to 20 → Waiting time = 12
- Average waiting time = (0 + 2 + 6 + 12) / 4 = 20/4 = 5 ms

This example demonstrates SJF's optimality in minimizing average waiting time when burst times are known.

### Example 2: Round Robin Time Quantum Analysis

Consider three threads with burst times: T1 = 10, T2 = 5, T3 = 8. Time quantum = 4 ms.

**Execution Timeline:**
- Time 0-4: T1 executes (remaining: 6)
- Time 4-8: T2 executes (remaining: 1)
- Time 8-12: T3 executes (remaining: 4)
- Time 12-16: T1 executes (remaining: 2)
- Time 16-17: T2 executes (completes)
- Time 17-21: T3 executes (completes)
- Time 21-23: T1 executes (completes)

**Completion times:**
- T2: 17 ms, T3: 21 ms, T1: 23 ms

**Waiting times:**
- T1: (0-12) + (16-21) = 12 + 5 = 17 ms
- T2: (4-16) = 12 ms
- T3: (8-17) = 9 ms

Average waiting time = (17 + 12 + 9) / 3 = 38/3 ≈ 12.67 ms

If we change quantum to 8 ms:
- T1 runs 0-8 (remaining: 2)
- T2 runs 8-13 (completes)
- T3 runs 13-21 (completes)
- T1 runs 21-23 (completes)

Average waiting time becomes (12 + 4 + 0) / 3 = 16/3 ≈ 5.33 ms

This illustrates how larger quantum sizes reduce context switching overhead and improve average waiting time for this workload.

### Example 3: Priority Scheduling with Aging

Consider threads with initial priorities (lower number = higher priority):
- T1: Priority 3, Burst 6
- T2: Priority 1, Burst 3
- T3: Priority 2, Burst 5
- T4: Priority 4, Burst 2

Without aging, execution order is T2, T3, T1, T4. T4 with lowest priority may starve.

With aging (priority increases by 1 for every 2 time units waited), after T2 and T3 complete:
- T1 has waited 8 units → Priority increases to 2
- T4 has waited 8 units → Priority increases to 3

New execution order becomes T1 (now priority 2), T4 (now priority 3). This ensures all threads eventually complete, preventing starvation while maintaining preference for higher-priority work.

## Exam Tips

1. **Differentiate between thread and process scheduling**: Remember that thread scheduling operates at a finer granularity and threads within the same process share resources, unlike independent processes.

2. **Remember scheduling criteria**: CPU utilization, throughput, turnaround time, waiting time, and response time are the five standard criteria for evaluating scheduling algorithms.

3. **Know algorithm trade-offs**: FCFS is simple but suffers from convoy effect; SJF is optimal for average waiting time but impractical without advance knowledge; Round Robin provides fairness but overhead depends on quantum size; Priority can cause starvation.

4. **Understand contention scope**: Process Contention Scope (PCS) manages threads within one process, while System Contention Scope (SCS) involves system-wide competition.

5. **Real-time scheduling key points**: Rate Monotonic Scheduling uses fixed priorities based on frequency with ~69% utilization bound; Earliest Deadline First is dynamic and optimal with 100% utilization potential.

6. **Multi-processor considerations**: Processor affinity reduces cache misses, load balancing distributes work, and cache coherency impacts performance on shared-memory systems.

7. **Aging prevents starvation**: When discussing priority scheduling, always mention aging as the solution to starvation of low-priority threads.

8. **Quantum size matters for Round Robin**: Too small causes excessive context switches; too large degrades to FCFS. Consider the trade-off in algorithm selection.