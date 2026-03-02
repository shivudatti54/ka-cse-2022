# Basic Concepts of Processes and Threads - Summary

## Key Definitions and Concepts

- **Process**: A program in execution, representing an instance of a program with its own address space, containing program code, data, stack, heap, and process control block
- **Process Control Block (PCB)**: The data structure maintained by the operating system that contains process state, program counter, CPU registers, memory management information, accounting data, and I/O status
- **Thread**: The smallest unit of CPU execution within a process; a lightweight entity that shares process resources while maintaining individual execution context
- **User-level Threads**: Threads managed entirely by user-level thread libraries without kernel involvement, offering fast creation but lacking multiprocessor support
- **Kernel-level Threads**: Threads managed directly by the operating system, enabling true parallelism but with higher overhead
- **Context Switching**: The process of saving the state of one process or thread and restoring the state of another

## Important Formulas and Theorems

- Process creation involves fork() system call returning twice (once in parent with child PID, once in child with 0)
- Thread creation uses pthread_create() with entry function, arguments, and attributes parameters
- Thread synchronization requires pthread_join() for waiting and pthread_mutex for mutual exclusion

## Key Points

- A process exists in one of five states: NEW, READY, RUNNING, WAITING, or TERMINATED
- Processes provide strong isolation through separate address spaces while threads share process resources
- PCB serves as the central repository for all process information and enables context switching
- User-level threads cannot achieve true parallelism on multi-core systems without kernel support
- Thread context switching is faster than process context switching due to shared resources
- The fork-exec model is fundamental to Unix process creation and management
- Processes are hierarchical with parent-child relationships, while threads are typically peer entities

## Common Mistakes to Avoid

- Confusing process state with process status; state refers to current execution phase while status refers to general condition
- Assuming threads always provide better performance; inappropriate thread usage can introduce synchronization overhead and race conditions
- Forgetting that threads share global variables and open files, leading to unintended data corruption
- Misunderstanding that user-level threads can block the entire process if any thread makes a blocking system call

## Revision Tips

- Draw and label the process state diagram repeatedly until transitions become automatic
- Create comparison tables between processes and threads covering creation time, resource sharing, communication, and switching overhead
- Write sample fork-exec and pthread programs to understand the practical implementation of these concepts
- Practice explaining each concept in one sentence to develop concise conceptual understanding for exam answers