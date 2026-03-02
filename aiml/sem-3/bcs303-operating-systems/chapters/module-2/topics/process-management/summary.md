# Process Management - Summary

## Key Definitions and Concepts

- **Process**: A program in execution, representing an active instance of a program with its own program counter, stack, data, and memory space
- **Process Control Block (PCB)**: A data structure maintained by the OS containing process identification, processor state information, and process control information
- **Process State**: The current condition of a process (New, Ready, Running, Waiting, Terminated)
- **Context Switch**: The process of saving and restoring CPU state when switching between processes
- **Interprocess Communication (IPC)**: Mechanisms enabling processes to communicate and share data

## Important Formulas and Theorems

- **Turnaround Time**: Completion Time - Arrival Time
- **Waiting Time**: Turnaround Time - Burst Time
- **Throughput**: Number of processes completed per unit time
- **CPU Utilization**: Percentage of time the CPU is busy

## Key Points

- A process is not merely a program but includes the execution context (registers, PC, stack, memory)
- The PCB is central to process management and is essential for context switching
- Process states follow a deterministic transition model (New → Ready → Running → Waiting/Terminated)
- Three levels of scheduling control degree of multiprogramming and process selection
- fork() creates a child process by duplicating the parent; exec() replaces the process image
- IPC can use shared memory (fast, requires synchronization) or message passing (safer, slower)
- Scheduling algorithms balance competing objectives: CPU utilization, throughput, turnaround time

## Common Mistakes to Avoid

- Confusing program and process: A program is passive; a process is active
- Forgetting that context switching involves saving complete CPU state to PCB
- Assuming higher priority always means better scheduling (starvation is possible)
- Neglecting synchronization in shared memory IPC (leads to race conditions)
- Confusing waiting time with turnaround time in calculations

## Revision Tips

1. Draw the complete process state diagram from memory and label all transitions
2. Practice numerical problems on scheduling algorithms until comfortable with calculations
3. Memorize the exact contents of PCB and understand why each component is necessary
4. Create comparison tables for IPC mechanisms and scheduling algorithms
5. Write sample code demonstrating fork() and exec() usage to reinforce concepts