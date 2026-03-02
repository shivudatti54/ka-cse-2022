# Basic Concepts in Process Management - Summary

## Key Definitions

- **Process**: A program in execution - a dynamic entity that includes the program code, current activity, execution context, and allocated resources
- **Process Control Block (PCB)**: A kernel data structure that stores all information about a process, including process state, program counter, CPU registers, memory management information, and scheduling data
- **Context Switching**: The process of saving the state of one process and restoring the state of another when switching CPU execution between processes
- **Process Scheduling**: The mechanism by which the OS selects which process to execute on the CPU at any given time
- **Ready Queue**: A data structure holding all processes that are ready to execute and waiting for CPU allocation

## Important Formulas

- **Context Switch Time**: T_cs = T_save + T_load + T_flush, where T_save is time to save current process state, T_load is time to load new process state, and T_flush is time to flush CPU caches/TLB
- **CPU Utilization**: The percentage of time the CPU is actively executing processes (typically expressed as: Utilization = (Busy Time / Total Time) × 100%)
- **Throughput**: Number of processes completed per time unit (Throughput = Total Completed Processes / Total Time)

## Key Points

1. A process is more than just a program - it encompasses the complete execution context including code, stack, heap, data section, and PCB
2. The Process Control Block (PCB) is the fundamental data structure for process management, containing all process-related information
3. Processes exist in one of five states: New, Ready, Running, Waiting, and Terminated
4. State transitions are triggered by specific events: scheduler dispatch (Ready→Running), I/O request (Running→Waiting), I/O completion (Waiting→Ready), and time slice expiration (Running→Ready)
5. Context switching involves saving the complete CPU state of the current process and loading the saved state of the selected process
6. The OS maintains multiple queues (job queue, ready queue, device queues) to manage processes at different stages of execution
7. Long-term scheduler controls the degree of multiprogramming, short-term scheduler selects the next process to run, and medium-term scheduler handles swapping
8. Each process has a unique Process ID (PID) assigned by the operating system for identification
9. Processes are independent entities - each has its own address space and cannot directly access another process's memory
10. Context switching overhead is pure system overhead with no productive work being accomplished during the switch

## Common Mistakes

1. **Confusing Program and Process**: A common error is treating a program and process as identical. Remember: a program is static code, while a process is dynamic and in execution.

2. **Assuming Only One Running Process**: Students sometimes forget that in a single-processor system, only one process can be in Running state at any instant, though multiple processes can be in Ready or Waiting states.

3. **Overlooking Context Switching Overhead**: Many students focus only on the benefits of scheduling without recognizing that context switching introduces significant overhead.

4. **Mixing Up Scheduler Types**: Confusing the roles of long-term, short-term, and medium-term schedulers is a frequent error. Long-term controls admission, short-term controls CPU allocation, and medium-term handles swapping.