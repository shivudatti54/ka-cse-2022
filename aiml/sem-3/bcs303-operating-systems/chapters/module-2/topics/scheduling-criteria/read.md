# CPU Scheduling Criteria

## Introduction

CPU Scheduling is one of the fundamental concepts in Operating System design, determining how the central processing unit allocates its time among various competing processes. When multiple processes reside in the ready queue waiting to execute, the operating system must make critical decisions about which process should receive the CPU next. This decision-making process relies heavily on scheduling criteria—specific metrics and parameters that evaluate the effectiveness and efficiency of a scheduling algorithm.

Understanding scheduling criteria is essential for analyzing and comparing different scheduling algorithms. In real-world operating systems like Windows, Linux, and macOS, these criteria influence system performance, user experience, and overall productivity. For instance, a system designed for interactive users requires quick response times, while a batch processing system might prioritize throughput. The criteria help system designers choose appropriate algorithms based on system requirements and usage patterns.

In the context of the University of Delhi's Computer Science curriculum, scheduling criteria form the theoretical foundation for understanding how operating systems manage process execution. This knowledge is tested extensively in semester examinations, where students must not only memorize the criteria but also apply them to analyze and compare various scheduling algorithms.

## Key Concepts

### CPU Utilization

CPU Utilization refers to the percentage of time that the CPU is actively executing a process, as opposed to being idle or waiting for I/O operations. In a well-designed system, CPU utilization should be kept as high as possible to maximize the return on investment in hardware resources. Modern operating systems typically aim for CPU utilization between 40% and 90% depending on the system type and workload.

The theoretical maximum CPU utilization is 100%, but in practice, this is rarely achieved due to periodic I/O operations, context switches, and system overhead. A higher CPU utilization indicates efficient use of processing power, but it must be balanced against other criteria. For example, a system running at 100% CPU utilization with extremely poor response time would not provide a good user experience.

### Throughput

Throughput measures the number of processes that a system completes per unit of time, typically expressed as processes per minute or processes per second. It is a direct indicator of the system's productivity and efficiency in processing work. Higher throughput means the system can accomplish more tasks in less time.

In batch processing systems, throughput is often the primary scheduling criterion because the goal is to process large volumes of data efficiently. For example, a mainframe system processing financial transactions might need to handle thousands of transactions per second. Throughput is calculated as:

Throughput = Number of Completed Processes / Time Unit

The value of throughput depends on the average service time of processes and the scheduling algorithm used. Shortest Job First (SJF) and Shortest Remaining Time First (SRTF) algorithms typically achieve higher throughput compared to First Come First Serve (FCFS) because they complete more short processes quickly.

### Turnaround Time

Turnaround time is defined as the total time elapsed from the moment a process enters the ready queue (or is submitted) until the moment it completes execution. This includes waiting time in the ready queue, execution time on the CPU, and time spent in I/O operations. It is a comprehensive measure of how long a process must wait before its work is finished.

Turnaround Time = Completion Time - Arrival Time

From a user's perspective, turnaround time is often the most visible performance metric. Users care about how quickly their tasks are completed. A process with a long turnaround time appears sluggish and unresponsive. Operating systems that serve interactive users must minimize average turnaround time to provide good user experience.

Different scheduling algorithms have varying impacts on turnaround time. FCFS tends to produce variable turnaround times, especially when short processes wait behind long ones. SJF minimizes average turnaround time for short processes but may cause starvation for long processes.

### Waiting Time

Waiting time specifically measures the total time a process spends waiting in the ready queue before receiving the CPU for execution. It excludes the actual execution time and I/O periods. Optimizing waiting time is crucial because processes in the ready queue consume memory resources and contribute to system overhead without making progress.

Waiting Time = Turnaround Time - Burst Time - I/O Time

The waiting time is directly influenced by the scheduling algorithm. A good scheduling algorithm should minimize the total waiting time across all processes. However, different algorithms optimize waiting time differently. While FCFS provides predictable waiting patterns, it may result in high waiting times for short processes. Priority scheduling can cause indefinite waiting (starvation) for low-priority processes.

From a system perspective, reducing waiting time improves overall system responsiveness and allows more processes to complete within given time constraints. This is particularly important in time-sharing systems where multiple users expect fair and timely service.

### Response Time

Response time is the interval between the time a process submits a request (or arrives in the ready queue) and the time the system provides the first response to that request. For interactive systems, response time is often more critical than turnaround time because users perceive responsiveness based on how quickly the system acknowledges their input.

Response Time = First CPU Execution Time - Arrival Time

In interactive applications like web browsers, word processors, and graphical user interfaces, users expect immediate feedback. A delay of more than 100 milliseconds is often noticeable and can create a perception of system slowness. Real-time systems have strict response time requirements where missing deadlines can have catastrophic consequences.

Different scheduling algorithms exhibit different response time characteristics. Round Robin scheduling typically provides good average response time because it gives every process regular CPU access. However, if the time quantum is too small, context switch overhead increases, actually worsening response times.

### Relationships Between Criteria

The five scheduling criteria are interconnected, and optimizing one criterion may negatively impact others. This creates trade-offs that system designers must carefully balance:

- High CPU utilization may increase waiting times for some processes
- Maximum throughput might require longer turnaround times for individual processes
- Minimizing response time could reduce overall CPU efficiency

The appropriate balance depends on the system type and user requirements. A university computer lab running interactive sessions prioritizes response time, while a data processing center emphasizes throughput.

## Examples

### Example 1: Calculating Scheduling Metrics

Consider three processes arriving at time 0 in the ready queue with the following burst times:

Process P1: 10 ms
Process P2: 5 ms
Process P3: 8 ms

Calculate the average waiting time, turnaround time, and throughput using FCFS scheduling.

**Solution using FCFS:**

Execution order: P1 → P2 → P3

**For P1:**
Completion Time = 10 ms
Turnaround Time = 10 - 0 = 10 ms
Waiting Time = Turnaround Time - Burst Time = 10 - 10 = 0 ms

**For P2:**
Completion Time = 10 + 5 = 15 ms
Turnaround Time = 15 - 0 = 15 ms
Waiting Time = 15 - 5 = 10 ms

**For P3:**
Completion Time = 15 + 8 = 23 ms
Turnaround Time = 23 - 0 = 23 ms
Waiting Time = 23 - 8 = 15 ms

**Average Waiting Time** = (0 + 10 + 15) / 3 = 25/3 ≈ 8.33 ms
**Average Turnaround Time** = (10 + 15 + 23) / 3 = 48/3 = 16 ms

If we complete these processes in 23 ms time unit:
**Throughput** = 3 processes / 23 ms ≈ 0.13 processes/ms ≈ 130 processes/second

### Example 2: Comparing SJF vs FCFS

Using the same processes, calculate metrics using SJF (non-preemptive):

**Solution using SJF (Shortest Job First):**

Execution order by burst time: P2 (5ms) → P3 (8ms) → P1 (10ms)

**For P2:**
Completion Time = 5 ms
Turnaround Time = 5 - 0 = 5 ms
Waiting Time = 5 - 5 = 0 ms

**For P3:**
Completion Time = 5 + 8 = 13 ms
Turnaround Time = 13 - 0 = 13 ms
Waiting Time = 13 - 8 = 5 ms

**For P1:**
Completion Time = 13 + 10 = 23 ms
Turnaround Time = 23 - 0 = 23 ms
Waiting Time = 23 - 10 = 13 ms

**Average Waiting Time** = (0 + 5 + 13) / 3 = 18/3 = 6 ms
**Average Turnaround Time** = (5 + 13 + 23) / 3 = 41/3 ≈ 13.67 ms

**Comparison with FCFS:**
- FCFS Average Waiting Time: 8.33 ms → SJF: 6 ms (IMPROVED)
- FCFS Average Turnaround Time: 16 ms → SJF: 13.67 ms (IMPROVED)

This demonstrates that SJF reduces both waiting time and turnaround time when shorter processes are executed first.

### Example 3: Response Time in Round Robin

Consider four processes arriving at time 0 with burst times: P1=6, P2=4, P3=2, P4=8 (all in ms). Using Round Robin with time quantum = 2 ms, calculate response time for each process.

**Solution:**

The execution proceeds in rounds, with each process getting 2 ms per turn:

**Timeline:**
Time 0-2: P1 (P1's first response: 0 ms)
Time 2-4: P2 (P2's first response: 2 ms)
Time 4-6: P3 (P3's first response: 4 ms)
Time 6-8: P4 (P4's first response: 6 ms)
Time 8-10: P1 (P1's second response: 8 ms)
Time 10-12: P2 completes
Time 12-14: P3 completes
Time 14-16: P1 completes
Time 16-20: P4 completes

**Response Times:**
- P1: 0 ms (immediate)
- P2: 2 ms
- P3: 4 ms
- P4: 6 ms

**Average Response Time** = (0 + 2 + 4 + 6) / 4 = 12/4 = 3 ms

Round Robin ensures no process waits longer than one time quantum for its first response, making it excellent for interactive systems where response time is critical.

## Exam Tips

1. Memorize the five primary scheduling criteria: CPU Utilization, Throughput, Turnaround Time, Waiting Time, and Response Time. Know exact definitions and formulas for each.

2. Understand the trade-offs between criteria. examiners frequently ask why optimizing one criterion might harm another. Example: maximizing CPU utilization might increase waiting time.

3. Practice numerical problems extensively. DU exams include calculation-based questions where you must compute waiting time, turnaround time, and throughput for FCFS, SJF, and Round Robin algorithms.

4. Remember that turnaround time ALWAYS includes waiting time plus execution time. Never confuse the two or use them interchangeably in answers.

5. Response time is specifically the time until FIRST CPU allocation, not completion time. This distinction is crucial for Round Robin analysis.

6. For comparative questions between scheduling algorithms, use specific criteria. For example, SJF gives minimum average waiting time but may cause starvation; FCFS is simple but can have high average waiting time.

7. Time quantum selection in Round Robin is important: too small increases context switch overhead (reducing CPU utilization), too large degrades to FCFS (increasing response time).

8. When answering "which algorithm is best" questions, always state "depends on the criteria" first, then justify based on the specific criterion mentioned in the question.