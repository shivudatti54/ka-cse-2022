# Process Scheduling


## Table of Contents

- [Process Scheduling](#process-scheduling)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [The Scheduling Queue Model](#the-scheduling-queue-model)
  - [Types of Schedulers](#types-of-schedulers)
  - [Scheduling Criteria](#scheduling-criteria)
  - [Scheduling Algorithms](#scheduling-algorithms)
- [Examples](#examples)
- [Exam Tips](#exam-tips)

## Introduction

Process scheduling is a fundamental concept in operating systems that determines how the central processing unit (CPU) is allocated among competing processes. In any modern computer system, multiple processes reside in memory simultaneously, each requiring CPU time to execute. The operating system must make critical decisions about which process to run at any given moment, how long to allow it to run, and when to preempt it in favor of another process. This decision-making mechanism is precisely what process scheduling encompasses.

The importance of process scheduling cannot be overstated in contemporary computing environments. Consider a scenario where you are streaming a video while downloading a file and running an antivirus scan in the background. Without effective scheduling, the video playback would stutter, downloads would pause inexplicably, and system responsiveness would deteriorate dramatically. Process scheduling ensures that all these tasks appear to execute concurrently, providing users with a seamless computing experience. From a system performance perspective, scheduling directly impacts key metrics such as CPU utilization, system throughput, and overall responsiveness. In enterprise environments running server applications that serve thousands of users simultaneously, the choice of scheduling algorithm can mean the difference between a system that handles the load efficiently and one that becomes unresponsive under pressure.

This topic examines the theoretical foundations of process scheduling, the various scheduling algorithms employed by operating systems, their comparative analysis, and practical considerations for different computing scenarios. Understanding these concepts is essential for any computer science professional, as they form the backbone of operating system design and influence application performance at every level.

## Key Concepts

### The Scheduling Queue Model

When a process enters the system, it is placed in a job queue containing all processes in the system. Processes that are ready to execute reside in the ready queue, typically implemented as a linked list or priority queue data structure. The ready queue contains all processes waiting for CPU time, organized according to the system's scheduling policy. Each process in the ready queue has associated attributes including process state, process control block, priority level, and execution history.

Processes waiting for I/O devices are placed in device queues corresponding to the specific hardware they require. A process may move between various queues throughout its lifecycle. When a process requests I/O, it leaves the ready queue and enters the appropriate device queue. Upon I/O completion, the process returns to the ready queue. This queuing model allows the operating system to manage diverse process requirements efficiently and ensures that CPU time is allocated to processes that can actually execute.

### Types of Schedulers

An operating system employs three distinct types of schedulers, each operating at different levels of the system and serving specific purposes in the overall scheduling hierarchy.

The long-term scheduler, also known as the job scheduler, controls the degree of multiprogramming by determining which processes are admitted to the system from the job pool. This scheduler decides whether to admit a new process into the ready queue or keep it waiting in the job queue. In systems with heavy computational workloads, the long-term scheduler carefully balances I/O-bound and CPU-bound processes to maximize system efficiency. Desktop operating systems typically have less aggressive long-term scheduling since they aim for quick response times.

The short-term scheduler, or CPU scheduler, is responsible for selecting one process from the ready queue and allocating the CPU to it. This scheduler executes frequently, making decisions every few milliseconds. The short-term scheduler must be extremely efficient because the overhead of scheduling itself consumes valuable CPU time. It implements the actual policy that determines which ready process gets CPU time next.

The medium-term scheduler introduces the concept of swapping, moving processes between main memory and secondary storage. When system memory becomes constrained, the medium-term scheduler may remove partially executed processes from memory, store them on disk (swapping out), and later bring them back into memory (swapping in). This technique, called swapping, helps manage the degree of multiprogramming dynamically and is particularly useful in systems with limited physical memory.

### Scheduling Criteria

Evaluating the effectiveness of a scheduling algorithm requires quantifiable criteria that capture different aspects of system performance. These criteria often conflict with each other, meaning no single algorithm can optimize all of them simultaneously.

CPU utilization measures the percentage of time the CPU is actively executing processes. In production systems, high CPU utilization is desirable as it indicates efficient use of expensive hardware resources. Modern operating systems typically aim for CPU utilization between 40 and 90 percent, with the variation depending on system load and configuration.

Throughput refers to the number of processes the system completes per unit of time. A system with high throughput can accomplish more work in less time. Throughput becomes particularly critical in batch processing environments where large volumes of jobs must be processed efficiently.

Turnaround time encompasses the entire period from process submission to process completion, including waiting time in the ready queue, execution time, and I/O time. Minimizing turnaround time is crucial for interactive systems where users expect quick responses to their commands.

Waiting time specifically measures the total time a process spends in the ready queue, excluding the actual execution time. Since the operating system cannot control I/O time or execution duration, minimizing waiting time is a primary focus for most scheduling algorithms.

Response time is the interval between submitting a request and receiving the first response. For interactive systems such as desktop computers and online transaction processing systems, minimizing response time is often the most critical requirement.

### Scheduling Algorithms

The First-Come-First-Served algorithm represents the simplest scheduling approach where the process that arrives first gets CPU time first. This algorithm is easy to implement using a FIFO queue and provides fair treatment to all processes. However, FCFS suffers from the convoy effect, where short processes wait behind long processes, leading to poor average waiting time. If a CPU-bound process executes first while I/O-bound processes wait, overall system throughput decreases significantly.

The Shortest Job First algorithm selects the process with the smallest burst time from the ready queue. SJF theoretically provides minimum average waiting time and is optimal under certain conditions. The primary challenge with SJF is accurately predicting the next CPU burst duration. Operating systems typically estimate this value using exponential averaging based on previous execution history. Additionally, SJF can cause starvation for long processes if short processes continuously arrive.

Priority scheduling assigns a priority value to each process, and the CPU is allocated to the highest priority process. Priorities can be defined internally (based on system criteria like memory requirements, file count, or time limits) or externally (based on process importance to users). A significant drawback of basic priority scheduling is indefinite blocking or starvation, where low-priority processes may never execute if higher-priority processes continuously arrive. The aging technique addresses this problem by gradually increasing the priority of waiting processes over time.

The Round Robin algorithm is designed specifically for time-sharing systems. Each process receives a fixed time slice called a quantum; when the quantum expires, the process is preempted and moved to the end of the ready queue. RR provides good response time for interactive systems and ensures no process monopolizes the CPU. The choice of quantum size critically affects system performance: too small causes excessive context switches, while too large degenerates into FCFS behavior. The optimal quantum typically falls between 10 and 100 milliseconds.

Multilevel Queue scheduling organizes the ready queue into multiple separate queues, each with its own scheduling algorithm. Processes are permanently assigned to one queue based on some property like process type, priority, or memory size. For example, a system might have a system queue running RR with a small quantum, an interactive queue using RR with a larger quantum, and a batch queue using FCFS. This approach allows the system to optimize for different process characteristics but can cause starvation for lower-priority queues.

Multilevel Feedback Queue is the most sophisticated algorithm, allowing processes to move between queues based on their behavior and CPU burst characteristics. CPU-bound processes start in lower-priority queues with longer quantums, while I/O-bound processes quickly move to higher-priority queues. This dynamic movement adapts to process behavior, providing excellent overall performance and preventing starvation through aging between queues.

## Examples

Consider three processes arriving at time zero with the following CPU burst times: P1 requires 24 milliseconds, P2 requires 3 milliseconds, and P3 requires 3 milliseconds. Under FCFS scheduling, the execution order is P1, P2, P3. P1 completes at time 24, P2 at time 27, and P3 at time 30. The waiting time for P1 is 0, P2 is 24, and P3 is 27, giving an average waiting time of 17 milliseconds. The turnaround times are 24, 27, and 30 milliseconds respectively.

Under SJF (non-preemptive), the scheduler selects P2 first (burst time 3), then P3 (burst time 3), and finally P1 (burst time 24). P2 completes at time 3, P3 at time 6, and P1 at time 30. Waiting times are 0 for P2 and P3, and 6 for P1, resulting in an average waiting time of just 2 milliseconds. This demonstrates why SJF provides significantly better average waiting time when burst times are known.

For Round Robin with quantum = 4 milliseconds, the execution proceeds as follows: P1 executes from 0-4, P2 from 4-7, P3 from 7-10, then P1 again from 10-14, P1 again from 14-18, P1 again from 18-22, and finally P1 from 22-24. The completion times are P1 at 24, P2 at 7, and P3 at 10. Waiting times are 6 for P1, 4 for P2, and 7 for P3, with an average waiting time of approximately 5.67 milliseconds. This example illustrates how RR provides better waiting time than FCFS while maintaining fairness.

## Exam Tips

For DU semester examinations, remember that long-term scheduler controls the degree of multiprogramming while short-term scheduler makes CPU allocation decisions. The most critical distinction between different scheduling algorithms lies in their handling of the trade-off between waiting time, turnaround time, and response time.

In SJF scheduling problems, always calculate waiting time as completion time minus arrival time minus burst time. Non-preemptive SJF means a running process cannot be interrupted, while preemptive SJF (also called Shortest Remaining Time First) allows preemption when a shorter process arrives.

For Round Robin problems, carefully track the quantum expiration points and remember that context switch time is often negligible but should be considered when explicitly mentioned. The number of times a process visits the CPU equals the ceiling of burst time divided by quantum, except when evenly divisible.

Priority scheduling questions frequently test the concept of starvation and its solution through aging. Remember that lower priority numbers typically indicate higher priority unless the question specifies otherwise.

The convoy effect in FCFS specifically refers to the phenomenon where short processes wait for one long CPU-bound process, degrading overall system performance. This is particularly problematic in systems where I/O-bound processes must wait for CPU-bound processes.

When comparing algorithms, FCFS provides no preemption and suffers from convoy effect, SJF provides optimal average waiting but causes starvation, RR provides good response time but poor turnaround, and priority scheduling may cause indefinite waiting. Multilevel feedback queues combine advantages of multiple approaches.

In numerical problems, always construct a timeline or Gantt chart to visualize process execution. For preemptive algorithms, clearly mark each context switch point. Verify your answers by ensuring all waiting times plus burst times equal turnaround times for each process.