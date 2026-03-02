# Process Scheduling

## Introduction

Process scheduling is one of the most fundamental concepts in operating systems, forming the backbone of how modern computers achieve efficient and equitable CPU allocation. When multiple processes reside in memory ready to execute, the operating system must decide which process receives the CPU's attention and for how long. This decision-making mechanism is precisely what we call process scheduling.

The importance of process scheduling cannot be overstated in today's computing environment. Consider a typical desktop system running dozens of applications simultaneously—a web browser, a text editor, a music player, and background processes like system services. Without proper scheduling, the user experience would be chaotic: the music player might stutter, the text editor would become unresponsive, and the entire system would appear frozen. Process scheduling ensures that each process gets fair CPU time, maintaining system responsiveness and maximizing overall throughput.

In the context of University of Delhi's Computer Science curriculum, process scheduling bridges theoretical concepts with practical system design. Understanding scheduling algorithms is essential not only for written examinations but also for comprehending how operating systems optimize resource utilization—a skill directly applicable in system programming and software development careers.

## Key Concepts

### The Scheduler

An operating system contains a component called the scheduler that selects which process from the ready queue should be allocated the CPU next. The scheduler operates at three distinct levels:

**Long-term Scheduler**: Also known as the job scheduler, this component decides which processes are admitted to the ready queue from the pool of new processes. It controls the degree of multiprogramming—the number of processes in memory. In modern desktop systems, this function is often minimal or absent, as the operating system tends to keep most processes in memory once launched.

**Short-term Scheduler**: Also called the CPU scheduler, this component makes the critical decision of which ready process to execute next. It operates frequently, making decisions every few milliseconds. This is the primary focus of process scheduling discussions.

**Medium-term Scheduler**: This scheduler handles process swapping—moving processes in and out of main memory to manage memory pressure. It can temporarily remove processes from memory to free up space for other processes.

### Scheduling Criteria

Evaluating scheduling algorithms requires standardized criteria that measure effectiveness from different perspectives:

**CPU Utilization**: The percentage of time the CPU is productively working. In an ideal system, CPU utilization approaches 100%, though in practice, 40-90% is considered good depending on system load.

**Throughput**: The number of processes that complete their execution per unit time. Higher throughput indicates better system efficiency.

**Turnaround Time**: The total time from process arrival in the ready queue to process completion. This includes waiting time, execution time, and I/O time.

**Waiting Time**: The total time a process spends in the ready queue waiting for CPU allocation. This is a critical metric because it represents pure inefficiency from the process's perspective.

**Response Time**: The time from process arrival to the first CPU allocation. This metric is particularly crucial for interactive systems where users expect quick feedback.

### Scheduling Algorithms

**First-Come-First-Served (FCFS)**: The simplest scheduling algorithm where the process that arrives first gets CPU time first. FCFS is easy to implement using a FIFO queue. However, it suffers from the convoy effect—short processes wait behind long processes, leading to poor average waiting time. For processes arriving in order P1 (24 units), P2 (3 units), P3 (3 units), the average waiting time is (0 + 24 + 27) / 3 = 17 units.

**Shortest Job First (SJF)**: This algorithm selects the process with the smallest burst time. SJF provides optimal average waiting time but requires knowledge of CPU burst lengths in advance, which is impractical. The preemptive version, Shortest Remaining Time First (SRTF), preempts the running process if a new process arrives with a shorter burst time. For processes with arrival times, SJF scheduling can significantly reduce waiting time compared to FCFS.

**Priority Scheduling**: Each process is assigned a priority, and the CPU is allocated to the highest priority process. Priorities can be internal (based on factors like memory requirements, I/O ratio) or external (based on user-assigned importance). A major drawback is starvation—low-priority processes may never execute if high-priority processes keep arriving.

**Round Robin (RR)**: Designed for time-sharing systems, RR allocates a fixed time quantum to each process in a cyclic manner. If a process completes within the quantum, it terminates; otherwise, it goes to the back of the ready queue. The choice of time quantum is critical: too small causes excessive context switches, too large degrades to FCFS. With quantum q=4 and processes P1 (10), P2 (5), P3 (8), the execution follows a cyclic pattern until all complete.

**Multilevel Queue Scheduling**: This algorithm partitions the ready queue into multiple separate queues, each with its own scheduling algorithm. For example, system processes might use FCFS while interactive processes use RR. Processes are permanently assigned to one queue based on some property like process type or priority.

**Multilevel Feedback Queue Scheduling**: A sophisticated variant that allows processes to move between queues. A process starting in the highest queue moves to lower queues if it consumes its full time quantum, and to higher queues if it relinquishes the CPU early (indicating I/O-bound behavior). This approach automatically separates CPU-bound and I/O-bound processes.

### Thread Scheduling

In modern operating systems, scheduling often occurs at the thread level rather than the process level. Thread scheduling follows similar principles but operates within a process's thread pool. On systems supporting many-to-many or two-level models, the thread library can influence which user-level threads receive CPU time by mapping them to kernel-level threads.

### Multiple-Processor Scheduling

When multiple CPUs are available, scheduling becomes significantly more complex. Key considerations include:

**Processor Affinity**: The tendency of a process to run on the same processor where it previously executed, taking advantage of cached data. Soft affinity allows movement between processors, while hard affinity binds a process to specific processors.

**Load Balancing**: Distributing work evenly across processors to prevent some from being idle while others are overloaded. This can be achieved through push migration (periodically checking load) or pull migration (idle processors pull work from busy ones).

**Symmetric vs Asymmetric Multiprocessing**: In SMP, all processors are equal and can execute any task. In AMP, one processor serves as the master handling all scheduling decisions while others execute assigned work.

## Examples

### Example 1: Calculating Turnaround Time for FCFS

Consider four processes arriving at time 0 in the order P1, P2, P3, P4 with burst times 7, 4, 1, and 3 units respectively.

**Solution:**
- P1 executes from time 0 to 7 → Completion time = 7, Turnaround time = 7 - 0 = 7
- P2 executes from time 7 to 11 → Completion time = 11, Turnaround time = 11 - 0 = 11
- P3 executes from time 11 to 12 → Completion time = 12, Turnaround time = 12 - 0 = 12
- P4 executes from time 12 to 15 → Completion time = 15, Turnaround time = 15 - 0 = 15

Average Turnaround Time = (7 + 11 + 12 + 15) / 4 = 45 / 4 = 11.25 units

Waiting times: P1=0, P2=7, P3=11, P4=12. Average Waiting Time = 30/4 = 7.5 units

### Example 2: Shortest Job First with Arrival Times

Consider processes arriving at different times:

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1      | 0            | 8          |
| P2      | 1            | 4          |
| P3      | 2            | 2          |
| P4      | 3            | 4          |

**Solution:**
- Time 0-1: Only P1 in queue, P1 executes [0,1)
- Time 1: P2 arrives, queue has P1(7), P2(4). Select P2
- Time 1-5: P2 executes for 4 units [1,5)
- Time 5: P3(2), P4(4), P1(7) in queue. Select P3 (shortest)
- Time 5-7: P3 executes [5,7)
- Time 7: P4(4), P1(7) in queue. Select P4
- Time 7-11: P4 executes [7,11)
- Time 11: P1 executes [11,19)

Turnaround times: P1=19-0=19, P2=5-1=4, P3=7-2=5, P4=11-3=8. Average = 36/4 = 9

### Example 3: Round Robin with Time Quantum

Consider processes P1(10), P2(5), P3(8) arriving at time 0 with quantum=4.

**Solution:**
- Cycle 1: P1 executes [0,4), goes to queue end
- Cycle 1: P2 executes [4,8), completes (needed only 5, used 4)
- Cycle 1: P3 executes [8,12), goes to queue end
- Cycle 2: P1 executes [12,16), remaining=6
- Cycle 2: P3 executes [16,20), remaining=4
- Cycle 3: P1 executes [20,24), remaining=2
- Cycle 3: P3 executes [24,28), completes
- Cycle 4: P1 executes [28,30), completes

Completion times: P1=30, P2=8, P3=28
Turnaround: P1=30, P2=8, P3=28. Average = 66/3 = 22

## Exam Tips

1. **Understand the difference between preemptive and non-preemptive scheduling**: Non-preemptive algorithms (like FCFS, non-preemptive SJF) once started cannot be interrupted, while preemptive (RR, SRTF, preemptive priority) can be interrupted by higher-priority processes.

2. **Remember that SJF provides optimal average waiting time** only when all processes arrive at time 0. With different arrival times, the optimal solution becomes more complex.

3. **For time quantum decisions**: A good quantum should be large enough to amortate context switch overhead but small enough to provide good response time. Typically 10-100 milliseconds.

4. **Starvation vs Deadlock**: Remember that priority scheduling can cause starvation (low priority processes never execute) but deadlock is a completely different concept involving circular waiting.

5. **Context switch overhead**: Higher priority processes or more frequent preemptions increase context switches, which is pure overhead. This trade-off is important in algorithm selection.

6. **Real-world example for RR**: Modern operating systems use RR for time-sharing because it provides good response time for interactive processes while ensuring fair CPU distribution.

7. **Know when each algorithm is best**: FCFS for simple systems, SJF when burst times are predictable, RR for time-sharing, Priority for real-time systems.

8. **Formula recall**: Average Waiting Time = (Sum of Waiting Times) / (Number of Processes); Turnaround Time = Burst Time + Waiting Time

9. **Thread scheduling distinction**: User-level threads are managed by thread library without kernel involvement, while kernel-level threads are directly scheduled by OS.