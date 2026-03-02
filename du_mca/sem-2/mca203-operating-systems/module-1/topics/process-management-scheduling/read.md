# Process Management and Scheduling

## Introduction
Process management is the fundamental mechanism through which operating systems manage program execution and resource allocation. In modern computing environments where multitasking is essential, efficient process management ensures optimal utilization of CPU resources while maintaining system responsiveness.

The scheduler acts as the brain of process management, making critical decisions about which process gets CPU time and when. With the increasing complexity of applications and the rise of multi-core processors, sophisticated scheduling algorithms have become vital for balancing fairness, throughput, and latency requirements in systems ranging from real-time embedded devices to cloud servers.

For MCA students, understanding process scheduling is crucial for system programming, performance optimization, and designing distributed systems. The concepts directly apply to thread management in modern programming frameworks and container orchestration in cloud environments.

## Key Concepts
1. **Process vs Program**: 
   - Program: Passive entity stored on disk
   - Process: Active instance of program with associated resources (memory, registers, I/O status)

2. **Process States**:
   - New: Being created
   - Ready: Waiting for CPU allocation
   - Running: Executing on CPU
   - Waiting: Blocked for I/O/event
   - Terminated: Finished execution

3. **Process Control Block (PCB)**:
   - OS data structure containing:
   - Process ID, State, Priority
   - CPU registers, Memory limits
   - I/O status information
   - Accounting information

4. **Scheduling Queues**:
   - Job Queue: All processes in system
   - Ready Queue: Processes ready to execute
   - Device Queues: Processes waiting for I/O

5. **Scheduler Types**:
   - Long-term (Job scheduler): Controls degree of multiprogramming
   - Short-term (CPU scheduler): Selects next process for CPU
   - Medium-term: Handles swapping

6. **Scheduling Algorithms**:
   - First-Come-First-Served (FCFS)
   - Shortest Job First (SJF)
   - Priority Scheduling
   - Round Robin (RR)
   - Multilevel Queue Scheduling
   - Multilevel Feedback Queue

7. **Context Switch**:
   - Mechanism to save/restore process state
   - Involves PCB transfer between memory and CPU registers
   - Typical cost: 1-100 μs in modern systems

8. **Dispatcher**:
   - Special module giving control of CPU to selected process
   - Functions: Context switching, user mode switching, jumping to proper location

## Examples

**Example 1: FCFS Scheduling**
```
Process | Arrival Time | Burst Time
P1      | 0            | 24
P2      | 0            | 3
P3      | 0            | 3

Calculate average waiting time
```
Solution:
1. Execution order: P1 → P2 → P3
2. Waiting times:
   - P1: 0
   - P2: 24
   - P3: 27
3. Average = (0 + 24 + 27)/3 = 17 ms

**Example 2: Round Robin (Time Quantum=4)**
```
Process | Burst Time
P1      | 24
P2      | 3
P3      | 3

Calculate completion times
```
Solution:
1. Execution sequence:
   P1(4) → P2(3) → P3(3) → P1(20)
2. Completion times:
   - P2: 7
   - P3: 10
   - P1: 30
3. Throughput = 3 processes/30 ms = 0.1 processes/ms

**Example 3: Priority Scheduling (Lower number=higher priority)**
```
Process | Burst Time | Priority
P1      | 10         | 3
P2      | 1          | 1
P3      | 2          | 4
P4      | 1          | 5
P5      | 5          | 2

Determine execution order
```
Solution:
1. Priority order: P2(1) → P5(2) → P1(3) → P3(4) → P4(5)
2. Execution sequence: P2 → P5 → P1 → P3 → P4

## Exam Tips
1. Always draw Gantt charts for scheduling problems - mandatory for full marks
2. Remember formulas:
   - Waiting Time = Start Time - Arrival Time
   - Turnaround Time = Completion Time - Arrival Time
3. For preemptive scheduling, track remaining burst time after each interrupt
4. Priority scheduling can lead to starvation - mention solutions like aging
5. Understand the Convoy Effect in FCFS through mathematical proof
6. Compare algorithms using metrics: CPU utilization, throughput, waiting time
7. Multilevel Feedback Queue is favorite question area - prepare real OS examples (Windows, Linux)