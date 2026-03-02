# Process Management: Basic Concepts - Summary

## Key Definitions and Concepts

A PROCESS is a program in execution—a dynamic entity that includes the program code, current execution state (program counter, registers), stack, heap, and data section. A PROGRAM is a passive collection of instructions stored on disk, while a PROCESS is an active entity with its own memory space and execution context.

The PROCESS CONTROL BLOCK (PCB) is a data structure maintained by the operating system to represent each process. It contains the process identifier, state, program counter, CPU registers, memory management information, accounting data, and I/O status information.

CONTEXT SWITCHING is the process of saving the state of one running process and restoring the state of another, enabling CPU time-sharing between multiple processes.

## Important Formulas and Theorems

CPU UTILIZATION with context switching overhead can be calculated as: ((Total CPU Time - Context Switch Overhead) / Total Time) × 100. For example, with 10ms average burst and 1ms context switch, utilization equals (10-1)/10 × 100 = 90%.

## Key Points

- A process is more than just program code—it includes execution context, stack, heap, and system resources
- The five fundamental process states are: New, Ready, Running, Waiting, and Terminated
- The PCB serves as the complete representation of a process within the operating system kernel
- Context switching involves saving and restoring process state, consuming CPU time that could otherwise execute user processes
- Long-term scheduling controls the degree of multiprogramming; short-term scheduling selects the next running process
- Multiple instances of the same program create distinct processes with independent execution contexts
- The ready queue contains processes waiting for CPU time; device queues contain processes waiting for I/O operations

## Common Mistakes to Avoid

Students often confuse process states with each other, particularly confusing the READY and RUNNING states. Remember that only ONE process can be RUNNING on a single-processor system at any instant, while multiple processes can be READY.

Another common error involves misunderstanding what gets saved during a context switch. It is not just the program counter—all CPU registers, stack pointers, and memory management state must be saved and restored.

Many students incorrectly assume that a process and its program are identical. Always remember that the program is static code while the process is dynamic execution.

## Revision Tips

Draw the process state diagram from memory repeatedly until you can reproduce it perfectly with all transition arrows labeled. Practice explaining each component of the PCB in your own words. Calculate context switching overhead for different scenarios to reinforce the practical impact of scheduling decisions. Compare how different operating systems (Windows versus Linux) implement these fundamental concepts to build deeper understanding.