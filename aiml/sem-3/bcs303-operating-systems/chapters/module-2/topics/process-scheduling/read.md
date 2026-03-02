# Process Scheduling

## Introduction

Process scheduling is a fundamental concept in operating systems that determines which process gets access to the CPU and for how long. In any modern computer system, multiple processes compete for a limited number of CPU cores. The process scheduler is the component of the operating system responsible for managing this competition efficiently, ensuring fair CPU allocation while optimizing system performance metrics like throughput and response time.

The importance of process scheduling cannot be overstated in today's computing environment. When you run multiple applications simultaneously—perhaps a web browser, a text editor, and a music player—the operating system must rapidly switch the CPU's attention among these processes, creating the illusion that all applications run concurrently. This is achieved through process scheduling algorithms that decide the order and duration of CPU allocation to each process. Without effective scheduling, systems would become unresponsive, and the computational resources would be severely underutilized.

This topic builds directly upon the Process concept and Process Management fundamentals covered earlier in your studies. Understanding scheduling is essential not only for theoretical knowledge but also for practical system administration and performance optimization. In DU semester examinations, process scheduling typically carries significant weightage, with questions ranging from algorithm comparisons to numerical problems calculating waiting times and turnaround times.

## Key Concepts

### Scheduling Criteria

Operating systems use several criteria to evaluate the effectiveness of scheduling algorithms. These criteria help system designers choose appropriate algorithms for different workloads and system requirements.

CPU utilization measures the percentage of time the CPU is actively executing processes. In a well-scheduled system, CPU utilization should remain high, typically between 40% and 90% depending on the workload. Throughput refers to the number of processes that complete their execution per unit time—higher throughput indicates better system efficiency. Turnaround time encompasses the total time from process arrival to completion, including waiting time and execution time. Waiting time specifically measures the total time a process spends ready in the ready queue, waiting for CPU allocation. Response time is the interval between process arrival and when the process gets CPU time for the first time—crucial for interactive systems where users expect quick feedback.

### Scheduling Algorithms

#### First-Come, First-Served (FCFS)

The FCFS algorithm is the simplest scheduling method, where the process that arrives first gets CPU priority. Processes are served in the order of their arrival in the ready queue. The main advantage of FCFS is its simplicity and fairness—every process eventually gets CPU time. However, it suffers from the convoy effect, where short processes wait behind long processes, leading to poor average waiting time. Consider three processes: P1 (burst time 24 units), P2 (burst time 3 units), and P3 (burst time 3 units arriving after P1 and P2). If they arrive in order P1, P2, P3, the average waiting time becomes (0 + 24 + 27) / 3 = 17 units—a relatively high value.

#### Shortest Job First (SJF)

SJF selects the process with the smallest burst time from the ready queue. This algorithm provides optimal average waiting time when all processes are available at time zero. However, in practice, knowing the exact burst time in advance is impossible. Systems often use exponential averaging to predict the next CPU burst based on previous bursts. SJF can be implemented in two forms: non-preemptive, where once a process starts executing, it runs to completion; and preemptive, called Shortest Remaining Time First (SRTF), where if a new process arrives with a burst time shorter than the remaining time of the currently executing process, the CPU is preempted. SRTF provides better response time for new short processes but requires more context switches.

#### Priority Scheduling

Priority scheduling assigns a priority number to each process, and the CPU is allocated to the process with the highest priority (or lowest number, depending on convention). Priorities can be either static, determined at process creation time, or dynamic, changing during execution based on factors like waiting time or resource usage. A major problem with priority scheduling is starvation or indefinite blocking, where low-priority processes may never get CPU time if high-priority processes keep arriving. Aging is a solution to starvation—gradually increasing the priority of waiting processes so that even low-priority processes eventually get scheduled.

#### Round Robin (RR)

Round Robin is designed specifically for time-sharing systems. Each process gets a fixed time slice called a quantum or time slice. Processes are arranged in a circular queue, and the scheduler gives each process one quantum of CPU time in rotation. If a process's burst is longer than the quantum, it is preempted and placed at the end of the ready queue. The performance of RR heavily depends on the quantum size: if the quantum is too small, excessive context switching occurs; if too large, response time suffers. Typically, the quantum is set between 10 to 100 milliseconds to balance responsiveness and overhead.

#### Multilevel Queue Scheduling

This algorithm partitions the ready queue into multiple separate queues, each with its own scheduling algorithm. Processes are permanently assigned to one queue based on some property like process type (system, interactive, batch) or priority. For example, a system might have a high-priority queue using RR for interactive processes and a low-priority queue using FCFS for batch processes. The challenge is scheduling between queues—typically, the higher priority queues must finish completely before lower priority queues are served, which can cause starvation.

#### Multilevel Feedback Queue Scheduling

MLFQ addresses the limitations of multilevel queue scheduling by allowing processes to move between queues. Processes that use too much CPU time are moved to lower-priority queues (punishment), while processes that wait too long are moved to higher-priority queues (reward). This dynamic movement allows the system to adapt to process behavior, providing good response for interactive processes while ensuring CPU-intensive processes eventually complete. MLFQ requires defining the number of queues, scheduling algorithm for each queue, criteria for moving processes between queues, and method to determine initial queue assignment.

### Thread Scheduling

In systems supporting threads, scheduling can occur at two levels: process scheduling and thread scheduling. Kernel-level threads are scheduled directly by the operating system, while user-level threads are managed by the thread library and must be mapped to kernel-level threads. On systems using many-to-one or many-to-many models, the thread library schedules user threads onto available kernel threads. The actual CPU dispatching happens at the kernel level, making thread scheduling platform-dependent.

### Multiple-Processor Scheduling

When multiple CPU cores are available, scheduling becomes significantly more complex. The primary challenge is load balancing—ensuring work is distributed evenly across all processors. Approaches include symmetric multiprocessing (SMP), where each processor is self-scheduling and can pick any ready thread, and asymmetric multiprocessing, where one processor handles all scheduling decisions while others execute assigned tasks. Cache affinity, the likelihood that a process benefits from running on the same processor where its data is cached, is also an important consideration in multiprocessor scheduling.

## Examples

### Example 1: Calculating Waiting Time for FCFS and SJF

Consider four processes arriving at time 0 with burst times: P1=6, P2=8, P3=7, P4=3. Calculate average waiting time for FCFS and non-preemptive SJF.

**FCFS Order: P1 → P2 → P3 → P4**

- P1: Waiting time = 0 (starts immediately)
- P2: Waiting time = 6 (P1's burst)
- P3: Waiting time = 6 + 8 = 14 (P1 + P2)
- P4: Waiting time = 6 + 8 + 7 = 21 (P1 + P2 + P3)
- Average Waiting Time = (0 + 6 + 14 + 21) / 4 = 41/4 = 10.25 units

**SJF Order: P4 → P1 → P3 → P2** (sorted by burst time: 3, 6, 7, 8)

- P4: Waiting time = 0
- P1: Waiting time = 3
- P3: Waiting time = 3 + 6 = 9
- P2: Waiting time = 3 + 6 + 7 = 16
- Average Waiting Time = (0 + 3 + 9 + 16) / 4 = 28/4 = 7 units

This demonstrates SJF's optimality in minimizing average waiting time.

### Example 2: Round Robin with Time Quantum

Consider processes with arrival times and burst times: P1(0, 10), P2(1, 5), P3(2, 8) with quantum = 4. Calculate turnaround time for each process using RR.

**Timeline:**
- Time 0-4: P1 executes (remaining: 6)
- Time 4: P2 arrives, P1 goes to queue end
- Time 4-8: P2 executes (remaining: 1)
- Time 8: P3 arrives, P2 goes to queue end
- Time 8-12: P3 executes (remaining: 4)
- Time 12: P1 (remaining 6) → P3 (remaining 4) → P2 (remaining 1)
- Time 12-16: P1 executes (remaining: 2)
- Time 16-20: P3 executes (completes)
- Time 20-21: P2 executes (completes)
- Time 21-23: P1 executes (completes)

**Turnaround Times:**
- P1: Completion 23 - Arrival 0 = 23
- P2: Completion 21 - Arrival 1 = 20
- P3: Completion 20 - Arrival 2 = 18
- Average Turnaround Time = (23 + 20 + 18) / 3 = 61/3 ≈ 20.33

### Example 3: Preemptive SJF (SRTF)

Consider processes: P1(0, 8), P2(1, 4), P3(2, 9), P4(3, 5). Calculate waiting time using preemptive SJF.

**Execution Timeline:**
- 0-1: P1 executes (remaining: 7)
- 1-2: P2 arrives, P2(4) < P1(7), so P2 executes (remaining: 3)
- 2-3: P3 arrives, P2(3) < P1(7) < P3(9), P2 continues (remaining: 2)
- 3-4: P4 arrives, P2(2) < P4(5) < P1(7) < P3(9), P2 continues (remaining: 1)
- 4-5: P2 continues (remaining: 0, completes at 5)
- 5-8: Now compare P1(7), P3(9), P4(5): P4 executes (remaining: 1)
- 8-9: P4 continues (completes at 9)
- 9-16: P1 executes (completes at 16)
- 16-25: P3 executes (completes at 25)

**Waiting Times:**
- P1: (1-0) + (9-16) = 1 + 7 = 8 (waited from 0-1 before first execution, and 9-16 before resuming)
- P2: 0 (executing from 1-5 continuously)
- P3: (2-2) + (16-25) = 0 + 9 = 9
- P4: (3-3) + (9-9) = 0 + 0 = 0
- Average Waiting Time = (8 + 0 + 9 + 0) / 4 = 17/4 = 4.25

## Exam Tips

1. **Memorize the scheduling criteria definitions thoroughly.** Questions frequently ask to define throughput, turnaround time, waiting time, and response time with precise wording.

2. **Practice numerical problems extensively.** DU exams consistently include calculation-based questions on waiting time and turnaround time for FCFS, SJF, and Round Robin algorithms.

3. **Understand the difference between preemptive and non-preemptive scheduling clearly.** Know which algorithms can be preempted (SJF can be preemptive as SRTF, Priority can be preemptive, RR is inherently preemptive) and the implications.

4. **Remember the quantum size impact on Round Robin.** Large quantum approaches FCFS behavior; small quantum increases context switching overhead but improves response time.

5. **Know how to solve starvation.** Aging is the technique where waiting processes gradually gain priority over time to prevent indefinite waiting.

6. **For SJF, always state that it's optimal for average waiting time but impractical** because burst times cannot be predicted accurately in real systems.

7. **Multilevel Feedback Queue is the most complex but most versatile algorithm.** Be prepared to explain how it combines the benefits of multiple scheduling approaches through process migration between queues.

8. **Draw Gantt charts for algorithm comparisons.** Visual representation helps in calculating waiting times accurately and demonstrates understanding clearly in answers.