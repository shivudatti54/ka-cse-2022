# Process Management - Summary

## Key Definitions and Concepts

- PROCESS: A program in execution — an active entity that includes program code, current execution state (program counter, CPU registers), stack, heap, and data section.
- PROCESS CONTROL BLOCK (PCB): A kernel data structure that stores all information about a process including state, program counter, CPU registers, memory management info, process ID, accounting info, and I/O status.
- CONTEXT SWITCH: The process of saving and restoring CPU state when switching between processes, involving saving the running process's state to its PCB and loading another process's state.
- SCHEDULING QUEUE: Data structures (ready queue, wait queues) that organize processes based on their current state and waiting requirements.
- INTERPROCESS COMMUNICATION (IPC): Mechanisms enabling processes to communicate and share data, including shared memory and message passing.

## Important Formulas and Theorems

- TURNAROUND TIME = Completion Time - Arrival Time
- WAITING TIME = Turnaround Time - Burst Time (or CPU Time)
- CPU UTILIZATION = (Busy Time / Total Time) × 100%
- THROUGHPUT = Number of Processes Completed / Unit Time
- AVERAGE WAITING TIME = Total Waiting Time / Number of Processes
- SJF (Non-preemptive) provides MINIMUM AVERAGE WAITING TIME among non-preemptive algorithms.
- ROUND ROBIN with time quantum q approximates FCFS when q is large and approximates processor-sharing when q is small.

## Key Points

- The operating system manages processes through the PCB, which is created when a process is admitted and destroyed when it terminates.
- Process state transitions occur due to scheduler decisions, system calls, interrupts, and I/O operations.
- Long-term scheduler controls degree of multiprogramming; short-term scheduler allocates CPU; medium-term scheduler performs swapping.
- FCFS suffers from convoy effect; SJF provides optimal average waiting time but requires burst prediction; Round Robin is ideal for time-sharing.
- Context switching has overhead — excessive switching reduces effective CPU time available for actual computation.
- Unix process creation uses fork() to create a child process and exec() to replace its program image.
- Zombie processes exist when terminated but parent hasn't called wait(); orphans are adopted by init when parent terminates.
- Shared memory provides fastest IPC but requires explicit synchronization; message passing provides natural synchronization but involves kernel overhead.

## Common Mistakes to Avoid

- Confusing program (passive) with process (active) — they are fundamentally different entities.
- Treating all scheduling algorithms as equivalent — each has specific use cases and performance characteristics.
- Forgetting that context switch involves saving COMPLETE CPU state, not just the program counter.
- Confusing preemptive and non-preemptive SJF — the preemptive version (Shortest Remaining Time First) can interrupt running processes.
- Assuming process state changes are always initiated by the running process — interrupts from hardware can also trigger state changes.

## Revision Tips

- Practice numerical problems from all scheduling algorithms multiple times — these carry significant weight in DU exams.
- Draw and label process state diagrams repeatedly until you can reproduce them from memory.
- Memorize the fields of PCB and understand WHY each field is necessary.
- Compare scheduling algorithms side-by-side using a comparison table covering criteria like starvation, convoy effect, and response time.
- Understand Unix-specific concepts (fork, exec, zombie, orphan) as they frequently appear in DU examinations.