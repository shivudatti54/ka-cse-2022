# Process Concept, States, and Process Control Block (PCB) - Summary

## Key Definitions and Concepts

- **Process**: A program in execution — an active entity with its own execution context, memory, registers, and system resources. Composed of program code, stack, heap, data section, and PCB.
- **Program**: A passive file containing instructions stored on disk; becomes a process when loaded into memory and executed.
- **Process Control Block (PCB)**: Kernel data structure that stores all information about a process — its identity, state, registers, scheduling info, memory management details, and I/O status.
- **Context Switch**: The mechanism of saving the state of one running process and restoring the state of another, enabling CPU to execute different processes.
- **Turnaround Time**: Total time from process arrival to completion (Completion Time - Arrival Time).
- **Waiting Time**: Time process spends in ready queue (Turnaround Time - Burst Time).

## Important Formulas and Theorems

- **Average Turnaround Time** = Σ(Turnaround Time of all processes) / Number of processes
- **Average Waiting Time** = Σ(Waiting Time of all processes) / Number of processes
- **Turnaround Time** = Completion Time - Arrival Time
- **Waiting Time** = Turnaround Time - Burst Time (CPU burst)
- **Throughput** = Number of processes completed per unit time

## Key Points

1. A process is more than a program — it includes execution context, resources, and the PCB.
2. Five process states: New (Created), Ready, Running, Blocked (Waiting), Terminated.
3. The PCB is the OS's "identity card" for each process, storing all metadata needed for management.
4. Context switching saves complete CPU state (PC, registers, flags) into the running process's PCB.
5. The ready queue contains processes waiting only for CPU; blocked queues contain processes waiting for I/O or events.
6. Preemptive scheduling allows the OS to forcibly take CPU from a running process; non-preemptive does not.
7. A process moves from Running to Blocked when it initiates I/O or waits for an event.
8. I/O completion or event occurrence causes a Blocked → Ready transition.
9. Multiple processes can exist simultaneously; each has a unique PID.
10. The OS maintains a Process Table — an array of pointers to all PCBs in the system.

## Common Mistakes to Avoid

1. **Confusing program and process**: A program is static code; a process is dynamic execution.
2. **Assuming all processes run simultaneously**: On a single-core CPU, only one process runs at a time; others wait in ready queue.
3. **Forgetting that context switching is overhead**: It consumes CPU time without doing useful work.
4. **Incorrectly calculating turnaround time**: Remember it's from arrival to completion, not from start of execution.
5. **Confusing waiting time with turnaround time**: Waiting time excludes the actual CPU burst time.

## Revision Tips

1. Draw the process state diagram repeatedly until you can do it from memory.
2. Memorize PCB components by understanding why each is necessary (e.g., PC needed to resume execution).
3. Practice numerical problems — draw Gantt charts for different scheduling algorithms.
4. Relate concepts to real examples: word processor waiting for keyboard input (blocked), browser loading multiple tabs (multiple processes).
5. Review previous years' DU question papers — process states and PCB are frequently asked.
6. Understand context switching as the mechanism that enables "apparent" simultaneity on single-CPU systems.