# Process Management - Summary

## Key Definitions and Concepts

- **Process**: A program in execution, consisting of the program code, current activity (program counter, registers), stack, heap, data section, and system resources.
- **Process Control Block (PCB)**: Kernel data structure storing complete information about a process, including PID, state, CPU registers, memory management info, I/O status, and scheduling information.
- **Process Scheduling**: OS mechanism to decide which process executes on the CPU, involving long-term (admission), short-term (CPU dispatch), and medium-term (swapping) schedulers.
- **Context Switch**: The process of saving and restoring CPU state when switching between processes, representing pure overhead.
- **Interprocess Communication (IPC)**: Mechanisms allowing processes to communicate and synchronize, including pipes, message queues, shared memory, semaphores, and signals.

## Important Formulas and Theorems

- **Average Waiting Time (AWT)**: Sum of waiting times of all processes divided by number of processes
- **Turnaround Time**: Completion time minus arrival time (includes waiting time + execution time)
- **Response Time**: Time from process arrival to first time on CPU
- **Throughput**: Number of processes completed per unit time
- **CPU Utilization**: Percentage of time CPU is busy executing processes

## Key Points

- A process is a dynamic entity while a program is static; multiple processes can run the same program simultaneously.
- The five process states are: New, Ready, Running, Waiting, and Terminated.
- The PCB is the most important data structure for process management—it maintains all process information.
- Short-term scheduler runs most frequently and must be fast; long-term scheduler controls degree of multiprogramming.
- FCFS: Simple but can cause convoy effect; good for batch systems.
- SJF: Optimal for minimizing average waiting time but requires knowledge of burst times.
- Round Robin: Ideal for time-sharing with time quantum; ensures fairness.
- Priority scheduling may cause starvation of low-priority processes.
- fork() creates a child process as a copy of parent; exec() replaces child with new program.
- Processes become zombies if parent doesn't call wait() after termination.
- Shared memory provides fastest IPC but requires explicit synchronization via semaphores.

## Common Mistakes to Confuse

- Confusing program (static code) with process (dynamic execution)
- Confusing waiting state (I/O wait) with ready state (waiting for CPU)
- Believing context switch does useful work (it is pure overhead)
- Thinking higher priority always means better (causes starvation)
- Forgetting that Round Robin requires time quantum to work

## Revision Tips

1. Draw the process state diagram repeatedly until you can reproduce it from memory.

2. Practice numerical problems on waiting time calculation for FCFS, SJF, and Round Robin.

3. Memorize PCB contents by grouping them logically: identification, state, control.

4. For IPC, remember: pipes are simple, message queues are structured, shared memory is fast, semaphores are for synchronization.

5. Understand the fork-exec sequence in Unix as this is frequently tested in theory exams.