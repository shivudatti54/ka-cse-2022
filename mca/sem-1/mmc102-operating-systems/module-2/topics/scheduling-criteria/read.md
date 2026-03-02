# Scheduling Criteria


## Table of Contents

- [Scheduling Criteria](#scheduling-criteria)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [CPU Utilization](#cpu-utilization)
  - [Throughput](#throughput)
  - [Turnaround Time](#turnaround-time)
  - [Waiting Time](#waiting-time)
  - [Response Time](#response-time)
  - [Fairness](#fairness)
  - [Priority](#priority)
  - [Deadline Compliance](#deadline-compliance)
- [Examples](#examples)
  - [Example 1: Comparing FCFS and SJF Scheduling](#example-1-comparing-fcfs-and-sjf-scheduling)
  - [Example 2: Round-Robin Time Quantum Impact](#example-2-round-robin-time-quantum-impact)
  - [Example 3: Response Time Calculation in Interactive System](#example-3-response-time-calculation-in-interactive-system)
- [Exam Tips](#exam-tips)

## Introduction

Scheduling criteria form the foundation upon which CPU scheduling algorithms are evaluated and compared. In modern operating systems, the CPU scheduler must make critical decisions about which process to execute when multiple processes compete for processor time. Understanding scheduling criteria is essential because different systems prioritize different performance metrics based on their intended use. A real-time system demands different optimization goals compared to a batch processing system or an interactive desktop system.

The study of scheduling criteria becomes particularly important in multi-programming environments where the operating system must maximize resource utilization while maintaining fairness among competing processes. The CPU represents one of the most valuable resources in any computing system, and efficient scheduling directly impacts system responsiveness, throughput, and overall user satisfaction. Operating system designers carefully balance multiple competing objectives, as improving one criterion often comes at the expense of another. For instance, optimizing for turnaround time might result in poorer response time for interactive users.

## Key Concepts

### CPU Utilization

CPU utilization measures the percentage of time the CPU is actively executing processes. In a well-designed system, CPU utilization should remain consistently high, as idle CPU time represents wasted computational resources. Modern operating systems typically aim for CPU utilization between 40% and 90% depending on the workload characteristics. Higher CPU utilization indicates better exploitation of expensive hardware resources.

The formula for CPU utilization is: CPU Utilization = (Busy Time / Total Time) × 100%. In practice, achieving 100% CPU utilization is neither possible nor desirable due to the need for idle periods during I/O operations and process transitions. Systems with higher CPU utilization generally demonstrate better throughput but may require more sophisticated scheduling to maintain acceptable response times.

### Throughput

Throughput refers to the number of processes that a system completes per unit of time. This metric is particularly crucial in batch processing environments where maximizing the number of jobs completed is the primary objective. Higher throughput means the system processes more work in the same timeframe, representing greater productivity.

Throughput can be calculated as: Throughput = Number of Completed Processes / Time Unit. For example, if a system completes 50 processes in 10 seconds, the throughput is 5 processes per second. Throughput is inversely related to the average service time per process; algorithms that minimize average turnaround time typically achieve higher throughput.

### Turnaround Time

Turnaround time encompasses the entire duration from process submission (or arrival in the ready queue) to process completion. This metric includes all phases of process execution: waiting in the ready queue, execution time on the CPU, and time spent in I/O operations. Turnaround time is critical in batch systems where jobs must complete within predictable timeframes.

The calculation is: Turnaround Time = Completion Time - Arrival Time. Consider a process that arrives at time 0, begins execution at time 5, finishes at time 20. The turnaround time equals 20 time units. Minimizing average turnaround time requires careful attention to both waiting time and execution time, making it a comprehensive measure of system performance.

### Waiting Time

Waiting time specifically measures the total time a process spends in the ready queue, awaiting CPU allocation. Unlike turnaround time, waiting time excludes the actual execution time and I/O periods. This criterion is particularly important because excessive waiting degrades user perception of system responsiveness, even when the CPU utilization remains high.

Average waiting time is calculated as: Sum of (Start Time - Arrival Time) for all processes / Number of processes. Scheduling algorithms like Shortest Job First (SJF) and Priority Scheduling directly aim to minimize average waiting time. However, optimal waiting time does not always translate to optimal turnaround time, creating interesting trade-offs in algorithm design.

### Response Time

Response time measures the interval between process arrival and the start of its first CPU execution. This criterion is paramount in interactive systems where users expect immediate feedback from their commands. A longer response time creates the perception of a sluggish, unresponsive system, regardless of eventual throughput.

The formula is: Response Time = First CPU Start Time - Arrival Time. For interactive applications like text editors or web browsers, response time values below 100 milliseconds are typically imperceptible to users. Real-time systems impose strict response time constraints where missing deadlines can result in system failure or data loss.

### Fairness

Fairness ensures that all processes eventually receive CPU time without indefinite postponement or starvation. A fair scheduling algorithm prevents scenarios where low-priority processes wait indefinitely while high-priority processes continuously consume CPU resources. Round-robin scheduling exemplifies a fairness-oriented approach by giving each process an equal time quantum.

Fairness can be measured by the variance in waiting times across processes or by examining whether the system guarantees progress for every process. However, absolute fairness often conflicts with optimal throughput or turnaround time, requiring system designers to balance these competing concerns based on system requirements.

### Priority

Priority-based scheduling assigns numerical priority values to processes, with the scheduler selecting higher-priority processes for execution. Priority can be either static (assigned at process creation and remains constant) or dynamic (adjusted during execution based on behavior or waiting time). Higher priority processes may experience shorter waiting times but can cause starvation of lower-priority processes.

Priority inversion occurs when a high-priority process waits for a low-priority process holding a required resource. This phenomenon is particularly problematic in real-time systems and requires special handling through priority inheritance protocols.

### Deadline Compliance

In real-time systems, meeting task deadlines is more critical than traditional performance metrics. Scheduling algorithms for real-time systems must guarantee that tasks complete before their specified deadlines. This criterion includes hard real-time systems (where missing a deadline causes system failure) and soft real-time systems (where deadline misses degrade performance but do not cause catastrophic failure).

## Examples

### Example 1: Comparing FCFS and SJF Scheduling

Consider three processes arriving at time 0 with the following burst times:

Process P1: 10 units
Process P2: 5 units  
Process P3: 8 units

**FCFS Scheduling:**
Execution order: P1 → P2 → P3
- P1 completes at time 10
- P2 completes at time 15
- P3 completes at time 23

Average Turnaround Time = (10 + 15 + 23) / 3 = 16 units
Average Waiting Time = (0 + 10 + 15) / 3 = 8.33 units

**SJF Scheduling:**
Execution order: P2 → P3 → P1
- P2 completes at time 5
- P3 completes at time 13
- P1 completes at time 23

Average Turnaround Time = (5 + 13 + 23) / 3 = 13.67 units
Average Waiting Time = (0 + 5 + 13) / 3 = 6 units

SJF demonstrates superior performance in both metrics, illustrating how burst time knowledge enables better scheduling decisions.

### Example 2: Round-Robin Time Quantum Impact

Four processes arrive simultaneously with burst times:
P1: 15, P2: 10, P3: 5, P4: 8

Using Time Quantum Q = 4:
- P1 executes 4 units, remaining: 11
- P2 executes 4 units, remaining: 6
- P3 executes 4 units, remaining: 1
- P4 executes 4 units, remaining: 4

Second round:
- P1 executes 4 units, remaining: 7
- P2 executes 4 units, remaining: 2
- P3 executes 1 unit, completes
- P4 executes 4 units, completes

Complete scheduling shows how smaller time quanta improve response time but increase context switch overhead. If context switch takes 1 unit, excessive quanta waste CPU time on overhead.

### Example 3: Response Time Calculation in Interactive System

Three processes arrive at different times in an interactive editor:
- P1 arrives at t=0, needs 3 CPU units
- P2 arrives at t=1, needs 5 CPU units
- P3 arrives at t=2, needs 2 CPU units

Using FCFS with arrivals:
- P1 starts at t=0, response time = 0
- P2 starts at t=3, response time = 2
- P3 starts at t=8, response time = 6

Average Response Time = (0 + 2 + 6) / 3 = 2.67 units

If SJF were used, P3 would execute before P2, reducing response time for P3 but potentially causing starvation for longer processes.

## Exam Tips

Understanding scheduling criteria requires knowing not just definitions but the trade-offs between different metrics. Examiners frequently ask students to compare algorithms based on specific criteria.

PRIORITIZE UNDERSTANDING OF THE RELATIONSHIPS between different criteria. Throughput and CPU utilization generally increase together, but maximizing one does not necessarily minimize others. The trade-off between throughput and response time is particularly important.

KNOW THE ALGORITHM-CRITERATION MATCHINGS: SJF optimizes turnaround time and waiting time, Round-Robin optimizes response time and fairness, and FCFS maximizes CPU utilization but performs poorly on waiting time.

MEMORIZE THE FORMULAS for each criterion. Questions frequently require calculating turnaround time, waiting time, throughput, or response time from given process data.

PRACTICE PROBLEMS WITH VARIOUS SCHEDULING SCENARIOS. Most exam questions involve numerical calculations where you must simulate scheduling algorithms and compute metrics.

UNDERSTAND THE IMPACT OF PROCESS BURST TIME VARIATIONS. For processes with similar burst times, most algorithms perform similarly. Large variations expose algorithmic differences more clearly.

BE AWARE OF LIMITATIONS AND EDGE CASES. SJF cannot be implemented perfectly in practice because burst times cannot be predicted accurately. Consider how this limitation affects real-world performance.

KNOW THE DIFFERENCE BETWEEN PREEMPTIVE AND NON-PREEMPTIVE ALGORITHMS. Preemptive algorithms like Round-Robin and Shortest Remaining Time First can interrupt running processes, affecting response time characteristics.

REMEMBER THAT NO SINGLE ALGORITHM OPTIMIZES ALL CRITERIA SIMULTANEOUSLY. This fundamental principle appears frequently in exam questions asking for algorithm selection given specific requirements.