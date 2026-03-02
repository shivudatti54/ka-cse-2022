# Scheduling Criteria

## Introduction

CPU scheduling is one of the fundamental concepts in operating system design, forming the backbone of multiprogramming and time-sharing systems. When multiple processes compete for CPU time, the operating system must make critical decisions about which process to execute and for how long. The effectiveness of these decisions directly impacts system performance, user satisfaction, and overall resource utilization.

Scheduling criteria are the metrics and standards used to evaluate and compare different CPU scheduling algorithms. Understanding these criteria is essential for system designers, administrators, and developers who need to optimize operating system performance. In real-world scenarios, different computing environments demand different scheduling priorities. A server handling web requests requires different optimization goals than a real-time system controlling industrial machinery. This diversity makes the study of scheduling criteria particularly relevant for modern computing applications.

In the context of the University of Delhi's Computer Science curriculum, scheduling criteria form a critical component of operating system theory. These concepts appear frequently in semester examinations and provide foundational knowledge for understanding more advanced topics like real-time scheduling, multiprocessor scheduling, and cloud resource management.

## Key Concepts

### Primary Scheduling Criteria

**1. CPU Utilization**

CPU utilization measures the percentage of time the CPU is actively executing processes. In a well-designed system, CPU utilization should remain high, ideally close to 100% for dedicated systems, though 40% to 90% is typical for general-purpose systems. High CPU utilization indicates efficient use of expensive computational resources. System administrators monitor CPU utilization to identify bottlenecks and plan capacity upgrades. The formula for CPU utilization is:

CPU Utilization = (Busy Time / Total Time) × 100%

In practice, achieving maximum CPU utilization requires balancing between keeping the CPU busy and minimizing context switching overhead, which consumes CPU cycles without performing useful work.

**2. Throughput**

Throughput represents the number of processes that a computer system completes per unit of time. It is a measure of system productivity and is particularly important in batch processing environments where large volumes of similar tasks must be completed. Throughput is calculated as:

Throughput = Number of Processes Completed / Time Unit

For example, if a system completes 50 processes in 10 seconds, the throughput is 5 processes per second. Higher throughput generally indicates better scheduling performance, though it must be balanced against other criteria like turnaround time.

**3. Turnaround Time**

Turnaround time encompasses the entire duration from when a process is submitted to when it completes execution. This includes waiting time in the ready queue, execution time on the CPU, and time spent in I/O operations. Turnaround time is calculated as:

Turnaround Time = Completion Time - Arrival Time

Turnaround time is particularly important for batch jobs and interactive systems where users expect reasonable response times. Minimizing average turnaround time is often a primary goal of scheduling algorithms, though it must be balanced against fairness and other criteria.

**4. Waiting Time**

Waiting time specifically measures the total time a process spends in the ready queue, waiting for CPU allocation. It does not include the actual execution time or I/O wait time. This criterion is crucial because unnecessary waiting represents inefficiency from the user's perspective. Waiting time is calculated as:

Waiting Time = Turnaround Time - Burst Time - I/O Time

Different scheduling algorithms produce dramatically different waiting times. Shortest Job First (SJF) and Shortest Remaining Time First (SRTF) algorithms aim to minimize waiting time, while FCFS may result in longer waiting times for processes with longer CPU bursts.

**5. Response Time**

Response time is the interval from when a process first requests CPU time until it receives CPU attention for the first time. This criterion is critically important for interactive systems where users expect immediate feedback. The formula is:

Response Time = First CPU Allocation Time - Arrival Time

Real-time systems and interactive applications demand minimal response times. A terminal session feels responsive only if the response time is less than the human perception threshold (typically 100-200 milliseconds).

### Secondary Scheduling Criteria

**Fairness**

Fairness ensures that each process receives a fair share of CPU time without starvation. A scheduling algorithm is considered fair if no process waits indefinitely for CPU time. However, achieving perfect fairness often requires sacrificing optimal performance on other criteria like throughput or turnaround time.

**Priority**

Many systems incorporate process priorities into scheduling decisions. Higher-priority processes receive CPU preference over lower-priority ones. Priority scheduling can lead to starvation of low-priority processes, requiring additional mechanisms like aging (gradually increasing priority of waiting processes) to ensure fairness.

**Predictability**

Predictable scheduling ensures that similar processes receive similar treatment regardless of system load. This is important in real-time systems where timing constraints must be guaranteed. Predictability involves consistent response times and adherence to deadlines.

## Examples

### Example 1: Comparing FCFS and SJF Scheduling

Consider three processes arriving at time 0 with the following CPU burst times:

- Process P1: 24 milliseconds
- Process P2: 3 milliseconds  
- Process P3: 3 milliseconds

**FCFS Scheduling (P1 → P2 → P3):**

- P1 waiting time: 0 ms, turnaround: 24 ms
- P2 waiting time: 24 ms, turnaround: 27 ms
- P3 waiting time: 27 ms, turnaround: 30 ms

Average waiting time: (0 + 24 + 27) / 3 = 17 ms
Average turnaround time: (24 + 27 + 30) / 3 = 27 ms

**SJF Scheduling (P2 → P3 → P1):**

- P2 waiting time: 0 ms, turnaround: 3 ms
- P3 waiting time: 3 ms, turnaround: 6 ms
- P1 waiting time: 6 ms, turnaround: 30 ms

Average waiting time: (0 + 3 + 6) / 3 = 3 ms
Average turnaround time: (3 + 6 + 30) / 3 = 13 ms

This example demonstrates that SJF significantly reduces average waiting time compared to FCFS. However, SJF requires advance knowledge of CPU burst times, which is not always available in practice.

### Example 2: Response Time Calculation in Round Robin

Consider four processes arriving simultaneously with the following CPU bursts and a time quantum of 10 ms:

- P1: 20 ms
- P2: 5 ms
- P3: 15 ms
- P4: 10 ms

Using Round Robin (time quantum = 10 ms):

- Cycle 1: P1 executes 10 ms (remaining: 10), P2 executes 5 ms (completes), P3 executes 10 ms (remaining: 5), P4 executes 10 ms (completes)
- Cycle 2: P1 executes 10 ms (completes), P3 executes 5 ms (completes)

Response times:
- P1: First response at 10 ms
- P2: First response at 10 ms
- P3: First response at 20 ms
- P4: First response at 30 ms

Average response time: (10 + 10 + 20 + 30) / 4 = 17.5 ms

Round Robin provides good response time for short processes but may have longer response times for processes with longer CPU bursts.

### Example 3: Real-World Application - Web Server Scheduling

Consider a web server handling three types of requests:

1. Static content requests (short, I/O bound): 5 ms CPU, 20 ms I/O
2. Database queries (medium, CPU+I/O): 30 ms CPU, 50 ms I/O  
3. Video processing requests (long, CPU intensive): 200 ms CPU

For a web server prioritizing user experience, the scheduling criteria priorities would be:
- Response time (most important): Users expect web pages within 2-3 seconds
- Throughput (important): Server must handle many concurrent requests
- Fairness (important): All types of requests should be served

A weighted fair queuing or multilevel queue scheduling would be appropriate, giving priority to short interactive requests while still ensuring longer tasks eventually complete.

## Exam Tips

1. **Memorize the five primary scheduling criteria**: CPU utilization, throughput, turnaround time, waiting time, and response time. These form the foundation of any scheduling-related question.

2. **Know the formulas**: Understand how to calculate each criterion from process execution data. Exam questions frequently ask for numerical calculations.

3. **Differentiate waiting time from turnaround time**: Waiting time is only the time spent in the ready queue, while turnaround time includes execution time and I/O wait.

4. **Understand the trade-offs**: No scheduling algorithm optimizes all criteria simultaneously. Be prepared to explain why certain algorithms sacrifice one criterion to improve another.

5. **Real-world context matters**: When answering questions, relate criteria to practical scenarios (batch systems vs. interactive systems vs. real-time systems).

6. **Remember SJF limitations**: While SJF minimizes average waiting time, it can cause starvation and requires knowledge of burst times.

7. **Round Robin considerations**: RR provides good response time but may have high context switching overhead with small time quantum.

8. **Concept of aging**: Understand how aging prevents starvation in priority scheduling by gradually increasing the priority of waiting processes.

9. **Distinguish preemptive vs non-preemptive**: Preemptive scheduling (like SRTF, RR) can better minimize response time but adds complexity.

10. **Practice numerical problems**: DU exams frequently include numerical questions requiring calculation of average waiting time, turnaround time, and throughput for different scheduling algorithms.