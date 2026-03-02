# Process Scheduling Basic Concepts

## Introduction

Process scheduling is one of the most fundamental concepts in operating system design, serving as the backbone of modern computing systems. In any computer system, multiple processes compete for limited CPU resources, and the operating system must decide which process gets access to the CPU and for how long. This decision-making mechanism is precisely what process scheduling entails. Without an efficient scheduler, a computer system would be unable to handle multiple tasks simultaneously, leading unresponsive systems, and wasted to poor performance, computational resources.

The importance of process scheduling becomes evident when we consider the sheer number of processes running on any given computer system at any moment. From the moment you turn on your computer, dozens of background processes begin executing, managing system resources, handling network connections, and providing user interface elements. Meanwhile, you might be running applications like a web browser, a word processor, and a media player simultaneously. The process scheduler ensures that all these processes receive appropriate CPU time, creating the illusion of parallel execution on a single processor or optimizing performance on multi-core systems.

This topic explores the fundamental concepts underlying process scheduling, including the role of different types of schedulers, the criteria used to evaluate scheduling algorithms, and the distinction between preemptive and non-preemptive scheduling approaches. Understanding these concepts is essential for comprehending how operating systems achieve efficiency, fairness, and responsiveness in managing computational resources.

## Key Concepts

### The Scheduling Problem

The fundamental problem that process scheduling addresses is this: given a set of processes that are ready to execute, which process should be selected to run on the CPU at any given time? This decision must be made repeatedly throughout the life of each process, and the choices made by the scheduler have profound implications for system performance. A well-designed scheduler balances multiple objectives, including maximizing CPU utilization, ensuring fairness among processes, minimizing waiting time, and providing responsive system behavior.

Modern operating systems support multitasking, which allows multiple processes to appear to execute simultaneously. On single-processor systems, this is achieved through rapid switching between processes, giving each process a small slice of CPU time. On multi-processor systems, scheduling becomes even more complex, as the scheduler must decide not only which process to run but also on which processor to run it. The scheduling algorithm chosen by system designers reflects the intended use case of the system, with different algorithms optimized for different performance goals.

### Types of Schedulers

Operating systems typically implement three levels of scheduling, each operating at a different timescale and serving a distinct purpose. Understanding these levels helps clarify how the operating system manages processes from creation to completion.

The long-term scheduler, also known as the admission scheduler, controls which processes are admitted to the system for processing. It decides which jobs from the job pool are loaded into the ready queue for processing. On systems where this scheduler is present, it attempts to maintain a good mix of CPU-bound and I/O-bound processes. A CPU-bound process spends most of its time performing computations, while an I/O-bound process spends most of its time waiting for I/O operations to complete. Maintaining a balanced mix ensures that the CPU remains busy while also keeping I/O devices utilized. Desktop and server operating systems often omit the long-term scheduler, admitting all new processes directly to memory, while batch systems and some mainframe operating systems make extensive use of it.

The short-term scheduler, also called the CPU scheduler, is the most critical component of the scheduling system. It selects from among the processes that are ready to execute and allocates the CPU to one of them. This decision is made frequently, perhaps every few milliseconds, and the algorithm used must be fast and efficient to minimize scheduling overhead. The short-term scheduler is responsible for determining which process runs next and for how long, making it the primary determinant of system responsiveness and throughput.

The medium-term scheduler introduces the concept of swapping, where processes can be temporarily moved out of main memory and stored on disk. This allows the operating system to manage memory more efficiently by removing inactive processes from memory, thereby freeing up space for other processes. When the swapped-out process needs to execute again, it is swapped back into memory. Swapping is particularly useful in systems with limited memory or when the system is under heavy load, and it represents an intermediate form of scheduling between the long-term and short-term schedulers.

### Scheduling Queue Structure

The operating system maintains several queues to track processes as they move through the system, and the scheduler operates by manipulating these queues. When a process enters the system, it is placed in the job queue, which contains all processes in the system. Processes that are in main memory and ready to execute are placed in the ready queue, which is typically implemented as a linked list or a priority queue. Processes that are waiting for I/O completion or other events are placed in device queues, with each device having its own queue.

A process typically moves between these queues throughout its lifetime. A newly created process enters the ready queue. When it is selected by the short-term scheduler, it transitions to the running state. While running, if the process initiates an I/O operation or waits for an event, it leaves the running state and enters an appropriate device queue. When the I/O operation completes, the process moves back to the ready queue, waiting for another turn on the CPU. This continuous movement between queues is what enables the operating system to manage multiple processes concurrently on a limited number of processors.

### Scheduling Criteria

Evaluating the effectiveness of a scheduling algorithm requires quantitative measures, and operating system designers use several criteria to compare different scheduling approaches. Understanding these criteria helps explain why different algorithms are suitable for different scenarios.

CPU utilization measures the percentage of time that the CPU is productively working. In a well-utilized system, the CPU should be busy most of the time, as idle CPU time represents wasted computational resources. Most operating systems aim for CPU utilization in the range of 40% to 90%, with higher utilization generally considered better. However, achieving very high CPU utilization sometimes comes at the cost of other desirable properties.

Throughput refers to the number of processes that the system completes per unit of time. A system with high throughput can execute more processes in a given period, making more efficient use of system resources. Throughput is particularly important in batch processing environments where the goal is to process as many jobs as possible.

Turnaround time is the total time from the moment a process arrives in the ready queue until it completes execution. This includes waiting time in the ready queue, execution time on the CPU, and time spent waiting for I/O operations. Minimizing turnaround time is desirable for interactive systems where users expect quick responses to their requests.

Waiting time is the total amount of time a process spends in the ready queue, waiting for CPU time. It does not include the time the process actually spends executing or waiting for I/O. The scheduling algorithm directly affects waiting time, and minimizing waiting time is a common goal of schedulers.

Response time is the time from when a process first enters the ready queue until it gets CPU time for the first time. This is particularly critical for interactive systems, where users perceive the system as slow if there is a long delay before the system begins responding to their commands. Minimizing response time is often more important than minimizing turnaround time for interactive applications.

### Preemptive vs Non-Preemptive Scheduling

A fundamental distinction in scheduling algorithms is whether they allow preemption, which is the ability to forcibly remove a process from the CPU before it completes its CPU burst. This distinction has significant implications for system behavior and the type of algorithms that can be used.

In non-preemptive scheduling, once a process begins executing, it continues to run until it voluntarily yields the CPU, either by terminating or by waiting for an I/O operation. Non-preemptive scheduling is simpler to implement because the scheduler does not need to interrupt a running process, and it ensures that a process will not be interrupted mid-execution. However, non-preemptive scheduling can lead to poor response times for interactive processes, as a long-running CPU-bound process could monopolize the CPU.

In preemptive scheduling, the operating system can forcibly suspend a running process and allocate the CPU to another process. This requires the scheduler to implement mechanisms for saving and restoring process state, known as context switching. Preemptive scheduling enables the system to respond quickly to events and ensures that no single process can monopolize the CPU. However, preemptive scheduling introduces additional overhead due to context switches and can create issues such as race conditions in multi-process programs.

The choice between preemptive and non-preemptive scheduling affects many aspects of system design, including the need for synchronization primitives, the complexity of kernel design, and the responsiveness of the system to user input. Most modern general-purpose operating systems use preemptive scheduling for user processes, while some real-time systems may use non-preemptive scheduling for certain types of tasks.

## Examples

Consider a system with three processes arriving at time zero with the following CPU burst requirements: Process P1 requires 24 milliseconds, Process P2 requires 3 milliseconds, and Process P3 requires 3 milliseconds. Let us examine how different scheduling algorithms would handle this set of processes.

Using First-Come-First-Served (FCFS), a non-preemptive scheduling algorithm, the processes would execute in the order of their arrival. Process P1 would execute first, completing at time 24. Then P2 would execute from time 24 to 27, and P3 would execute from time 27 to 30. The average turnaround time would be (24 + 3 + 6) divided by 3, which equals 11 milliseconds. The waiting times would be 0 milliseconds for P1, 21 milliseconds for P2, and 24 milliseconds for P3.

Using Shortest-Job-First (SJF), which selects the process with the smallest CPU burst, P2 and P3 would execute first. If both arrive simultaneously, either could go first. Let us assume P2 goes first, completing at time 3. Then P3 executes from time 3 to 6, and finally P1 executes from time 6 to 30. The average turnaround time would be (30 + 3 + 6) divided by 3, which equals 13 milliseconds. The waiting times would be 6 milliseconds for P1, 0 milliseconds for P2, and 3 milliseconds for P3. While SJF has higher average turnaround time in this specific case, it minimizes waiting time for the short processes.

Using Round-Robin scheduling with a time quantum of 4 milliseconds, a preemptive algorithm, the CPU cycles through all processes in the ready queue. P1 executes from 0 to 4, then P2 from 4 to 7, then P3 from 7 to 10. Then P1 executes again from 10 to 14, from 14 to 18, from 18 to 22, and finally from 22 to 24. The average turnaround time would be (24 + 7 + 10) divided by 3, which equals approximately 13.67 milliseconds. Round-Robin ensures that no process waits longer than (n-1)q time units, where n is the number of processes and q is the time quantum, providing better response time for interactive systems.

## Exam Tips

For DU semester examinations, focus on understanding the differences between the three types of schedulers and their roles in process management. Questions frequently ask about the specific functions of long-term, short-term, and medium-term schedulers.

Memorize the five scheduling criteria: CPU utilization, throughput, turnaround time, waiting time, and response time. Be able to explain each criterion and identify scenarios where maximizing or minimizing each criterion is important.

Understand the distinction between preemptive and non-preemptive scheduling thoroughly. Know the advantages and disadvantages of each type, and be able to identify which scheduling algorithms fall into each category.

When solving numerical problems involving scheduling algorithms, always draw a timeline or Gantt chart to visualize the execution order. This helps avoid errors and makes it easier to calculate waiting times and turnaround times accurately.

Remember that waiting time is the time spent in the ready queue, NOT the total time from process creation. Many students confuse waiting time with turnaround time, which is a common mistake.

For First-Come-First-Served, note that it suffers from the convoy effect, where short processes wait behind long processes. Be prepared to explain this phenomenon and its impact on system performance.

In Round-Robin scheduling, the choice of time quantum is critical. If the quantum is too large, the algorithm degenerates to FCFS; if too small, excessive context switching overhead degrades performance. The ideal quantum should be chosen such that most processes complete their CPU burst within one quantum.