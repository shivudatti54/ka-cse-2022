# Thread Scheduling

## Introduction

Thread scheduling is a fundamental concept in modern operating systems that determines how CPU time is allocated among competing threads within a process or system-wide. As computing evolved from single-threaded to multi-threaded architectures, the need for efficient thread scheduling became paramount. While processes served as the primary unit of resource allocation in early operating systems, the emergence of threads as lightweight execution units demanded a more granular approach to CPU management.

Thread scheduling plays a CRITICAL ROLE in determining system performance, responsiveness, and overall efficiency. In contemporary computing environments where multi-core processors dominate, proper thread scheduling ensures optimal utilization of available CPU cores, maintains system responsiveness for interactive applications, and maximizes throughput for compute-intensive workloads. Understanding thread scheduling is essential for computer science students because it bridges the gap between theoretical operating system concepts and practical system programming.

The University of Delhi curriculum emphasizes thread scheduling as it represents the practical implementation of scheduling principles at a finer granularity than process scheduling. Modern applications ranging from web servers to mobile operating systems rely heavily on efficient thread management. This topic builds upon your understanding of process scheduling and prepares you for advanced topics in concurrent programming and distributed systems.

## Key Concepts

### Thread States and Lifecycle

Threads, like processes, traverse through various states during their lifetime. The THREE PRIMARY STATES are ready, running, and blocked. A thread in the ready state is waiting for CPU allocation, the running state indicates active execution on a processor, and the blocked state means the thread is waiting for I/O or other resources. Understanding these states is fundamental to grasping how schedulers make allocation decisions.

The thread state diagram includes additional states such as new (thread being created), terminated (completed execution), and in some systems, suspended states. The scheduler maintains ready queues for each priority level or processor affinity, organizing threads awaiting CPU time. Transitioning between these states forms the basis of all scheduling decisions.

### Scheduling Criteria

Several CRITERIA influence thread scheduling decisions. CPU utilization measures the percentage of time the CPU is productively working. Throughput refers to the number of threads completed per unit time. Turnaround time encompasses the total time from thread creation to completion, including waiting time and execution time. Waiting time is the cumulative period a thread spends in the ready queue. Response time measures the delay between a thread becoming ready and receiving CPU time for the first time.

Balancing these criteria often involves trade-offs. A system optimized for throughput might sacrifice response time for interactive applications. Real-time systems prioritize meeting deadlines over throughput. Your understanding of these criteria will help you analyze different scheduling algorithms critically.

### Types of Thread Scheduling

Thread scheduling operates at TWO LEVELS based on contention scope. Process Contention Scope (PCS) occurs when threads within the same process compete for CPU time. The process itself manages this scheduling, and threads share the process's resources. System Contention Scope (SCS) involves competition among all threads in the system, regardless of which process they belong to. The operating system kernel manages SCS scheduling, making it more complex but providing better system-wide fairness.

Many-to-one and many-to-many threading models typically use PCS for user-level threads, while one-to-one models (like Windows and Linux) use SCS for kernel threads. Understanding this distinction helps explain why certain threading implementations perform differently under various workloads.

### Thread Scheduling vs Process Scheduling

While process scheduling and thread scheduling share fundamental principles, they differ in significant ways. Thread scheduling operates at a finer granularity since threads within a process share address space and resources. Context switches between threads are faster because they require saving fewer registers and no address space switching. Threads can be scheduled independently while sharing process resources, enabling more efficient parallelism.

Process scheduling involves protecting process resources and maintaining isolation, while thread scheduling focuses purely on CPU allocation among competing execution contexts. This efficiency makes multi-threaded applications preferable to multi-process applications for most scenarios requiring concurrent execution.

## Scheduling Algorithms

### First-Come First-Served (FCFS)

FCFS represents the simplest scheduling algorithm where threads are executed in the order they arrive in the ready queue. This non-preemptive algorithm is easy to implement using a simple FIFO queue. However, FCFS suffers from the convoy effect where short threads wait behind long-running threads, leading to poor average waiting time. Consider three threads with burst times: T1 = 24ms, T2 = 3ms, T3 = 3ms. If they arrive in order T1, T2, T3, T1 completes at 24ms, T2 at 27ms, and T3 at 30ms, yielding an average turnaround time of (24+27+30)/3 = 27ms. If reordered as T2, T3, T1, average turnaround time becomes (3+6+30)/3 = 13ms, demonstrating FCFS sensitivity to arrival order.

### Shortest Job First (SJF)

SJF selects the thread with the smallest burst time for execution, minimizing average waiting time for known burst times. The non-preemptive SJF algorithm is optimal for average waiting time but requires advance knowledge of thread execution times, which is impractical in general-purpose systems. The preemptive version, Shortest Remaining Time First (SRTF), preempts running threads when a shorter thread becomes ready. SJF suffers from starvation where long threads may never execute if shorter threads keep arriving.

### Round Robin (RR)

Round Robin is a PREEMPTIVE algorithm designed for time-sharing systems. Each thread receives a fixed time quantum (slice) for execution. If a thread's burst exceeds its quantum, it is preempted and placed at the back of the ready queue. RR provides good response time and ensures fairness by giving each thread an equal opportunity to execute.

The effectiveness of RR depends heavily on time quantum selection. If quantum is too large, RR degenerates to FCFS. If quantum is too small, context switching overhead becomes significant. A common practice is to set quantum between 10ms and 100ms, with context switch time typically less than 10% of the quantum. For quantum = 4ms and threads with bursts 10ms, 8ms, and 7ms: Thread 1 executes for 4ms (remaining 6ms), Thread 2 executes for 4ms (remaining 4ms), Thread 3 executes for 4ms (remaining 3ms), continuing until completion.

### Priority Scheduling

Priority scheduling assigns a priority value to each thread, executing the highest priority thread first. Priorities can be either static (fixed at creation) or dynamic (changing based on behavior). Preemptive priority scheduling preempts a running thread if a higher priority thread becomes ready. A CRITICAL ISSUE is starvation or indefinite postponement where low-priority threads may never execute if higher priority threads keep arriving.

Aging is a technique to combat starvation by gradually increasing the priority of waiting threads. After each time unit in the ready queue, a thread's priority increases slightly, ensuring eventually it receives CPU time. Many modern operating systems implement priority inheritance protocols where a thread temporarily inherits the priority of lower-priority threads it blocks, preventing priority inversion.

### Multilevel Queue Scheduling

This algorithm maintains SEPARATE READY QUEUES for different classes of threads. System threads might use FCFS in one queue while interactive threads use RR in another. Each queue has its own scheduling algorithm, and queues themselves are scheduled using fixed priority or time slicing. This approach accommodates different thread types with appropriate scheduling strategies.

The major limitation is that threads cannot move between queues once assigned. Multilevel Feedback Queue (MLFQ) addresses this by allowing threads to move between queues based on their CPU burst characteristics. CPU-intensive threads move to lower priority queues while I/O-bound interactive threads remain in higher priority queues, improving overall system responsiveness.

### Thread Scheduling in Modern Operating Systems

Linux uses the Completely Fair Scheduler (CFS) which implements fair CPU time distribution among runnable threads. CFS uses a red-black tree to track virtual runtimes, always scheduling the thread with the smallest virtual runtime. Windows uses a priority-based scheduler with 32 priority levels, combining real-time priorities (16-31) and variable priorities (0-15). Both systems support thread affinity allowing threads to be pinned to specific processors.

## Examples

### Example 1: Calculating Average Waiting Time for FCFS and SJF

Problem: Consider four threads with the following arrival times and burst times:
- Thread A: Arrival = 0, Burst = 7
- Thread B: Arrival = 2, Burst = 4
- Thread C: Arrival = 4, Burst = 1
- Thread D: Arrival = 5, Burst = 4

Calculate average waiting time using FCFS and non-preemptive SJF.

Solution for FCFS:
- Thread A: Waiting = 0 (executes immediately at time 0)
- Thread B: Waiting = 7 - 2 = 5 (waits from time 2 to execution at 7)
- Thread C: Waiting = 11 - 4 = 7 (waits from time 4 to execution at 11)
- Thread D: Waiting = 12 - 5 = 7 (waits from time 5 to execution at 12)
- Average Waiting Time = (0 + 5 + 7 + 7) / 4 = 19/4 = 4.75 ms

Solution for SJF (prioritizing by burst time when threads arrive):
- At time 0: Only A available, executes 0-7
- At time 2: B arrives, at time 4: C arrives, at time 5: D arrives
- After A completes at 7: B (4), C (1), D (4) are waiting - C has shortest burst
- C executes 7-8
- At time 8: B (4), D (4) - either can execute first
- B executes 8-12, D executes 12-16
- Thread waiting times: A = 0, B = 7-2 = 5, C = 7-4 = 3, D = 12-5 = 7
- Average Waiting Time = (0 + 5 + 3 + 7) / 4 = 15/4 = 3.75 ms

### Example 2: Round Robin Time Quantum Calculation

Problem: Three threads arrive simultaneously with burst times T1 = 10ms, T2 = 5ms, T3 = 8ms. Using Round Robin with quantum = 3ms and zero context switch time, calculate completion time and turnaround time for each thread.

Solution:
Time 0-3: T1 executes (remaining 7ms), queue: T2, T3, T1
Time 3-6: T2 executes (remaining 2ms), queue: T3, T1, T2
Time 6-9: T3 executes (remaining 5ms), queue: T1, T2, T3
Time 9-12: T1 executes (remaining 4ms), queue: T2, T3, T1
Time 12-14: T2 executes (remaining 0ms - completes), queue: T3, T1
Time 14-17: T3 executes (remaining 2ms), queue: T1, T3
Time 17-20: T1 executes (remaining 1ms), queue: T3, T1
Time 20-22: T3 executes (remaining 0ms - completes), queue: T1
Time 22-23: T1 executes (remaining 0ms - completes)

Completion times: T1 = 23ms, T2 = 14ms, T3 = 22ms
Turnaround times: T1 = 23-0 = 23ms, T2 = 14-0 = 14ms, T3 = 22-0 = 22ms
Average Turnaround Time = (23 + 14 + 22) / 3 = 59/3 ≈ 19.67ms

### Example 3: Priority Scheduling Analysis

Problem: Four threads with priorities (higher number = higher priority) and burst times:
- P1: Priority 2, Burst 6
- P2: Priority 1, Burst 8
- P3: Priority 3, Burst 4
- P4: Priority 2, Burst 5

Calculate average turnaround time using non-preemptive priority scheduling (highest priority first). What issue might occur?

Solution:
Order of execution by priority: P3 (priority 3), then P1 (priority 2), P4 (priority 2), then P2 (priority 1)
- P3: Start 0, Complete 4, Turnaround = 4
- P1: Start 4, Complete 10, Turnaround = 10
- P4: Start 10, Complete 15, Turnaround = 15
- P2: Start 15, Complete 23, Turnaround = 23

Average Turnaround Time = (4 + 10 + 15 + 23) / 4 = 52/4 = 13ms

The ISSUE is starvation: P2 with lowest priority must wait for all other threads to complete. If high-priority threads continuously arrive, P2 might never execute - this is the starvation problem in priority scheduling.

## Exam Tips

Understanding thread scheduling is crucial for DU semester examinations. Here are ESSENTIAL points to remember:

1. DISTINGUISH between preemptive and non-preemptive scheduling: Preemptive allows thread preemption while non-preemptive runs threads to completion or until they voluntarily yield.

2. KNOW the difference between thread scheduling and process scheduling: Thread scheduling operates at finer granularity with faster context switches and shared resources within a process.

3. UNDERSTAND the trade-offs in Round Robin: Larger quantum improves throughput but increases response time; smaller quantum improves response time but increases context switch overhead.

4. REMEMBER that SJF provides optimal average waiting time but requires knowledge of burst times: In practice, burst times are estimated using exponential averaging.

5. IDENTIFY starvation scenarios: Priority scheduling can cause low-priority threads to wait indefinitely; aging is the solution to prevent starvation.

6. KNOW the scheduling criteria: CPU utilization, throughput, turnaround time, waiting time, and response time - each is appropriate for different system types.

7. UNDERSTAND the difference between Process Contention Scope and System Contention Scope: PCS manages threads within a process, SCS manages all system threads.

8. FOR numerical problems, ALWAYS draw timeline diagrams: Visual representation helps avoid errors in calculating waiting and turnaround times.

9. BE PREPARED to compare algorithms: Questions often ask to analyze which algorithm performs better under specific conditions and why.

10. KNOW real-world scheduling: Linux CFS and Windows priority-based scheduling demonstrate how theoretical concepts are implemented in practical operating systems.