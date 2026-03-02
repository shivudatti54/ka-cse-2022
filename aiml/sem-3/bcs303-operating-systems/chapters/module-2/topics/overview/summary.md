# Overview of Process Management - Summary

## Key Definitions and Concepts

- **Process**: A program in execution—an active entity with its own execution context, including program counter, registers, stack, and memory space
- **Process Control Block (PCB)**: The kernel data structure that stores all information about a process, including PID, state, program counter, CPU registers, memory management info, I/O status, and scheduling information
- **Process States**: Five distinct states—NEW, READY, RUNNING, WAITING, and TERMINATED
- **Scheduler**: System software that decides which process executes at any given time
- **Long-term Scheduler**: Controls admission of new processes to the ready queue, determining degree of multiprogramming
- **Short-term Scheduler**: Selects the next process from ready queue for CPU execution
- **Medium-term Scheduler**: Handles swapping of processes in and out of memory
- **IPC (Inter-Process Communication)**: Mechanisms for processes to exchange data—shared memory and message passing are the two primary models
- **Thread**: A lightweight unit of execution within a process; threads share code, data, and system resources but have individual execution contexts

## Important Formulas and Theorems

- **Waiting Time**: Turnaround Time - Burst Time
- **Turnaround Time**: Completion Time - Arrival Time
- **Throughput**: Number of processes completed per unit time
- **CPU Utilization**: Percentage of time the CPU is actively executing processes

For Round Robin scheduling:
- If time quantum is too small: excessive context switching overhead
- If time quantum is too large: degrades to FCFS behavior

## Key Points

- A program is passive (stored on disk) while a process is active (in memory and executing)
- The PCB is the most critical data structure for process management—exam questions frequently ask about its components
- The operating system maintains multiple queues: ready queue for CPU-bound processes and device queues for I/O-bound processes
- Scheduling algorithms balance competing objectives: CPU utilization, throughput, turnaround time, waiting time, and fairness
- FCFS is simple but can cause convoy effect; SJF is optimal for average waiting time but impossible to implement in practice
- Round Robin provides good response time for time-sharing systems with appropriate time quantum selection
- Process creation involves fork() (creating a copy of parent) and exec() (replacing with new program) in UNIX systems
- Threads offer faster creation, faster context switching, and easier communication compared to processes

## Common Mistakes to Avoid

- Confusing program and process—remember program is code, process is execution
- Mixing up long-term and short-term scheduler functions—long-term controls which processes enter memory, short-term controls CPU allocation
- Forgetting that preemptive scheduling allows the OS to forcibly remove a running process, while non-preemptive allows processes to run to completion
- Assuming SJF is always non-preemptive—preemptive SJF (Shortest Remaining Time First) exists and is optimal for average response time
- Overlooking that threads share resources within a process—this requires synchronization but is also what makes them efficient

## Revision Tips

1. Draw the process state diagram repeatedly until transitions become automatic—this is frequently tested in examinations

2. Practice numerical problems on scheduling algorithms with different arrival times and burst times to master waiting time and turnaround time calculations

3. Create comparison tables for scheduling algorithms (FCFS vs SJF vs Priority vs Round Robin) noting advantages, disadvantages, and suitable applications

4. Understand UNIX system calls fork() and exec() thoroughly—these are fundamental to process creation and are commonly asked in theory questions

5. Review thread versus process differences multiple times, as this comparison frequently appears in examination questions