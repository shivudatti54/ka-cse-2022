# Basic Concepts of Process Management - Summary

## Key Definitions and Concepts

- **Process**: A program in execution—a dynamic, active entity with its own execution context, memory space, and system resources.
- **Program**: A passive entity consisting of instructions and data stored in a file on disk; it becomes a process when loaded into memory and executed.
- **Process Control Block (PCB)**: A data structure maintained by the operating system that contains all information about a process, including PID, state, program counter, CPU registers, and resource information.
- **Context Switching**: The procedure by which the CPU switches from one process to another, saving the current process state and restoring another process's state.

## Important Formulas and Theorems

- **Total Execution Time with Context Switching**: Total Time = CPU Work Time + (Number of Context Switches × Context Switch Time)
- **Process State Model**: NEW → READY → RUNNING → (WAITING/TERMINATED) with various transitions back to READY

## Key Points

- A process is more than just program code—it includes the execution context, system resources, and current state.
- The five process states are NEW, READY, RUNNING, WAITING, and TERMINATED.
- The PCB is the central data structure for process management, storing all process-related information.
- Context switching enables multiprogramming but introduces overhead.
- In Unix, `fork()` creates a new process, and `exec()` replaces it with a new program.
- Each process has a unique PID assigned by the operating system.
- Parent processes can wait for child completion using `wait()` to retrieve exit status.
- Multiple processes can run the same program simultaneously as separate entities.

## Common Mistakes to Avoid

- Confusing a program (static) with a process (dynamic) in definitions.
- Forgetting that only one process per CPU core can be in RUNNING state at any instant.
- Overlooking context switching overhead in performance calculations.
- Not understanding that waiting for I/O causes a process to move from RUNNING to WAITING state.

## Revision Tips

1. Draw the process state diagram from memory and label all transitions.
2. List all components of the PCB and explain each briefly.
3. Write pseudocode demonstrating parent-child process relationships.
4. Practice calculating context switch overhead with sample problems.
5. Review previous years' DU examination questions on this topic.