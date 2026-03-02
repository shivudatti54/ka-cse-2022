# Process Scheduling Basic Concepts

## Introduction

Process scheduling is one of the most fundamental concepts in operating systems, forming the backbone of how modern computing systems manage resource allocation and system performance. In any computer system, multiple processes compete for limited CPU time, and the operating system must make critical decisions about which process to execute at any given moment. This decision-making process is governed by algorithms collectively known as process scheduling algorithms.

The importance of process scheduling cannot be overstated in the context of modern computing. Consider a typical desktop computer running dozens of applications simultaneously—email clients, web browsers, text editors, music players, and system background services. Without effective scheduling, the CPU would be overwhelmed, system responsiveness would degrade, and user experience would suffer dramatically. Similarly, in server environments handling thousands of concurrent requests, efficient scheduling determines whether the system can meet performance targets and service level agreements.

This topic explores the foundational concepts of process scheduling, including the criteria used to evaluate scheduling algorithms, the major scheduling algorithms employed by operating systems, and the challenges faced in multi-processor and real-time environments. Understanding these concepts is essential for any computer science student, as they represent the core mechanisms through which operating systems achieve concurrency, maximize CPU utilization, and ensure fair resource allocation among competing processes.

## Key Concepts

### What is Process Scheduling?

Process scheduling is the mechanism by which an operating system decides the order in which processes access the CPU. The operating system maintains one or more queues of processes that are ready to execute, and the scheduler selects from these queues based on specific criteria. This selection process occurs at multiple levels, leading to the concept of scheduling levels.

The scheduling subsystem consists of three main components: the long-term scheduler, the short-term scheduler, and the medium-term scheduler. The long-term scheduler, also called the admission scheduler, decides which processes are admitted to the system from the pool of new processes. It controls the degree of multiprogramming—the number of processes in memory at any given time. The short-term scheduler, or CPU scheduler, decides which of the ready processes should be allocated the CPU next. This scheduler operates very frequently, making decisions every few milliseconds. The medium-term scheduler handles process swapping, moving processes in and out of main memory to manage memory utilization and improve system performance.

### The Role of the CPU Scheduler

The CPU scheduler is responsible for selecting a process from the ready queue and allocating the CPU to it. When the currently running process voluntarily yields the CPU, or when its time quantum expires, the scheduler must choose the next process to run. This decision must be made quickly because the CPU sits idle while the scheduler makes its choice, and every cycle spent idling represents lost productivity.

The scheduler operates based on scheduling criteria that define what constitutes a "good" scheduling decision. These criteria include CPU utilization (keeping the CPU as busy as possible), throughput (completing as many processes as possible per unit time), turnaround time (minimizing the time from process submission to completion), waiting time (minimizing the time processes spend in the ready queue), and response time (minimizing the time from request submission to first response).

Different operating systems weight these criteria differently based on their intended use. A batch system might prioritize throughput and CPU utilization, while an interactive system prioritizes response time. A real-time system must guarantee that critical tasks complete within strict deadlines.

### Scheduling Criteria

Understanding scheduling criteria is essential for analyzing and comparing different scheduling algorithms. Each criterion represents a different aspect of system performance, and no single algorithm can optimize all criteria simultaneously.

CPU Utilization measures the percentage of time the CPU is actively executing processes. In a well-scheduled system, CPU utilization should remain high, typically above 90 percent for heavily loaded systems. Low CPU utilization often indicates that processes are spending too much time waiting for I/O or that the system is underutilized.

Throughput refers to the number of processes the system completes per unit time. A high-throughput system can execute more work in the same period, making efficient use of available resources. Throughput is particularly important in batch processing environments where the goal is to process as many jobs as possible.

Turnaround Time encompasses the entire lifespan of a process from the moment it enters the system to the moment it completes. This includes waiting time in the ready queue, time spent executing on the CPU, and time spent waiting for I/O operations. Minimizing turnaround time requires balancing between short and long processes.

Waiting Time specifically measures the cumulative time a process spends in the ready queue, waiting for CPU access. Unlike turnaround time, waiting time does not include the actual execution time or I/O wait time. Most scheduling algorithms aim to minimize average waiting time.

Response Time is crucial for interactive systems and measures the time from when a process makes a request to when it produces the first output. Users perceive systems with low response time as more responsive and efficient, even if throughput is not maximized.

### Scheduling Algorithms

The operating system employs various scheduling algorithms, each with distinct characteristics, advantages, and disadvantages. The choice of algorithm significantly impacts system performance and user experience.

First-Come-First-Served (FCFS) is the simplest scheduling algorithm, where the process that arrives first gets CPU time first. Processes are served in order of their arrival in the ready queue. FCFS is easy to implement but can lead to the convoy effect, where short processes wait behind long processes, resulting in poor average waiting time. Consider three processes: P1 with burst time 24, P2 with burst time 3, and P3 with burst time 3. If they arrive in order P1, P2, P3, the waiting time for P2 is 24, for P3 is 27, and for P1 is 30. The average waiting time is 27 milliseconds, which is quite high.

Shortest Job First (SJF) scheduling selects the process with the smallest burst time from the ready queue. This algorithm minimizes average waiting time when all processes are available simultaneously. However, SJF requires knowledge of process burst times, which is not always available in advance. The major challenge with SJF is the possibility of starvation for long processes if short processes keep arriving.

Priority Scheduling assigns a priority value to each process, and the CPU is allocated to the process with the highest priority. Processes with equal priority are scheduled using FCFS. Priority scheduling can lead to starvation of low-priority processes, which can be mitigated using aging techniques that gradually increase the priority of waiting processes.

Round Robin (RR) scheduling is designed specifically for time-sharing systems. Each process receives a fixed time quantum, typically between 10 to 100 milliseconds. When a process uses its entire time quantum, it is preempted and moved to the end of the ready queue. RR ensures fair CPU allocation among all processes and provides good response time. However, if the time quantum is too large, RR degenerates to FCFS; if too small, excessive context switching overhead degrades performance.

Multilevel Queue Scheduling partitions the ready queue into multiple separate queues, each with its own scheduling algorithm. For example, a system might have a system queue, an interactive queue, and a batch queue. Processes are permanently assigned to one queue based on their characteristics. This approach allows different types of processes to be scheduled according to their needs.

### Thread Scheduling

In modern operating systems, scheduling often occurs at the thread level rather than the process level. Threads within the same process share many resources, including memory and open files, but each thread maintains its own program counter, stack, and register state. The operating system can schedule threads from different processes, or multiple threads from the same process.

Thread scheduling introduces additional considerations. In a many-to-one or many-to-many model, the thread library or the operating system kernel may handle thread scheduling. Kernel-level thread scheduling provides better performance on multi-processor systems because the kernel can schedule threads on different processors simultaneously.

### Multiple-Processor Scheduling

Scheduling becomes significantly more complex in multi-processor systems. The fundamental question is whether processes should be restricted to a single processor or allowed to migrate between processors. Processor affinity refers to the tendency of a process to remain on the same processor, which improves cache performance by keeping cache warm with the process's data.

Load balancing attempts to distribute workloads evenly across all processors. This can be achieved through push migration (periodically checking load and moving processes) or pull migration (idle processors pull work from busy processors). However, load balancing must be balanced against the benefits of processor affinity.

Symmetric multi-processing (SMP) allows all processors to be equal, with each processor maintaining its own ready queue. This approach is more scalable but requires careful synchronization of the ready queues. Asymmetric multi-processing assigns specific roles to processors, with one master processor controlling the system and other processors following its directives.

## Examples

### Example 1: Calculating Waiting Time for FCFS

Consider three processes arriving at time 0 in the order P1, P2, P3 with burst times 10, 5, and 8 milliseconds respectively.

Using FCFS scheduling, P1 executes first from time 0 to 10, so its waiting time is 0 milliseconds. P2 waits from time 10 to 15, giving it a waiting time of 10 milliseconds. P3 waits from time 15 to 23, giving it a waiting time of 10 + 8 = 18 milliseconds.

The average waiting time is (0 + 10 + 18) / 3 = 9.33 milliseconds. The turnaround times are: P1 = 10 ms, P2 = 15 ms, P3 = 23 ms. The average turnaround time is (10 + 15 + 23) / 3 = 16 milliseconds.

### Example 2: Shortest Job First Scheduling

Using the same processes but applying SJF scheduling, the scheduler selects P2 (burst time 5) first, then P3 (burst time 8), then P1 (burst time 10).

P2 executes from 0 to 5 with waiting time 0. P3 executes from 5 to 13 with waiting time 5. P1 executes from 13 to 23 with waiting time 5 + 8 = 13. The average waiting time is (0 + 5 + 13) / 3 = 6 milliseconds, which is significantly better than FCFS.

The turnaround times are: P2 = 5 ms, P3 = 13 ms, P1 = 23 ms. Average turnaround time is (5 + 13 + 23) / 3 = 13.67 milliseconds.

### Example 3: Round Robin with Time Quantum

Consider three processes with burst times 10, 5, and 8 milliseconds, arriving at time 0, with a time quantum of 4 milliseconds.

At time 0, P1 executes for 4 milliseconds (remaining: 6). At time 4, P2 executes for 4 milliseconds (remaining: 1). At time 8, P3 executes for 4 milliseconds (remaining: 4). At time 12, P1 executes for 4 more milliseconds (remaining: 2). At time 16, P2 executes its remaining 1 millisecond and completes. At time 17, P3 executes for 4 milliseconds (remaining: 0) and completes. At time 21, P1 executes its final 2 milliseconds and completes.

The waiting times are: P1 = 0 + 8 + 4 = 12, P2 = 4 + 0 = 4, P3 = 8 + 0 = 8. Average waiting time = (12 + 4 + 8) / 3 = 8 milliseconds.

## Exam Tips

For DU semester examinations, several key points deserve special attention. First, clearly understand the difference between scheduling levels—long-term, short-term, and medium-term—and their roles in process management. Examiners frequently ask about these distinctions.

Second, memorize the five scheduling criteria: CPU utilization, throughput, turnaround time, waiting time, and response time. Be prepared to explain how different algorithms optimize for different criteria. FCFS maximizes CPU utilization but has poor turnaround time for short processes.

Third, practice numerical problems involving waiting time and turnaround time calculations for FCFS, SJF, and Round Robin algorithms. These calculations appear frequently in examination papers and carry significant weight.

Fourth, understand the convoy effect in FCFS and starvation in priority scheduling. Be able to explain why these problems occur and how they can be mitigated.

Fifth, remember that Round Robin is best suited for time-sharing systems due to its fairness and good response time. Know how to calculate waiting times when processes arrive at different times.

Sixth, for thread scheduling, understand the relationship between process scheduling and thread scheduling, and recognize that thread-level scheduling provides finer granularity control.

Seventh, in multiple-processor scheduling questions, be familiar with processor affinity and load balancing concepts, and understand the challenges of maintaining cache coherence.