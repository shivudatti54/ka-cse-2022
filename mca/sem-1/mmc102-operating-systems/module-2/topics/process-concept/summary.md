# Process Concept - Summary

## Key Definitions and Concepts

- **Process**: An instance of a program in execution, consisting of the program code, current activity (program counter, registers), stack, data section, and allocated system resources. It is an active entity that the operating system creates, schedules, and terminates.

- **Process Control Block (PCB)**: A data structure maintained by the operating system for each process, containing process identification (PID, PPID), process state, program counter, CPU registers, memory management information, accounting information, and I/O status information.

- **Context Switching**: The mechanism of saving the state of one process and restoring the state of another process when the CPU switches between processes. It involves saving all CPU registers, program counter, and other state information to the PCB.

- **Process State**: The current condition of a process—NEW (being created), READY (waiting for CPU), RUNNING (executing on CPU), WAITING (waiting for I/O/event), or TERMINATED (finished execution).

## Important Formulas and Theorems

- **Context Switching Overhead Calculation**: Time spent on context switching = (Number of context switches per second) × (Time per context switch). Percentage of CPU overhead = (Context switching time / Total CPU time) × 100.

- **Degree of Multiprogramming**: Controlled by the long-term scheduler. Higher degrees increase CPU utilization but may increase average turnaround time for individual processes.

## Key Points

- A process is fundamentally different from a program: a program is passive code stored on disk, while a process is an active execution instance with allocated resources.

- The PCB serves as the process's identity and state repository; without the PCB, the operating system cannot manage or resume a process after context switching.

- The five-state model (New, Ready, Running, Waiting, Terminated) describes the lifecycle of a process from creation to termination.

- Context switching is pure overhead—it consumes CPU cycles without performing user computation. Minimizing context switch frequency and time is important for system performance.

- CPU-bound processes perform computations and use full time quantums; I/O-bound processes frequently block for I/O, giving up CPU time before their quantum expires.

- The scheduler decides which ready process to run next. Short-term schedulers run frequently (milliseconds), while long-term schedulers run less frequently.

- Each process has a unique PID; parent processes create child processes using system calls like fork() and exec().

## Common Mistakes to Avoid

- Confusing a process with a program—they are fundamentally different entities (active vs passive).

- Forgetting that context switching saves complete CPU state, not just the program counter.

- Assuming only one process can be in the ready or waiting states—queues can hold many processes in each state.

- Overlooking the overhead of context switching when evaluating system performance.

- Believing that the running process always completes its time quantum—processes can voluntarily give up the CPU by requesting I/O.

## Revision Tips

- Draw the process state transition diagram from memory and label all possible transitions with the events causing them.

- Create a table listing all PCB components and their purposes for quick recall.

- Practice calculating context switching overhead with sample problems to reinforce understanding.

- Remember that the waiting state always involves some external event (I/O completion, signal, resource availability) that the process cannot control.

- Review how process concepts apply to modern systems by considering how Linux or Windows manages processes during typical operations.