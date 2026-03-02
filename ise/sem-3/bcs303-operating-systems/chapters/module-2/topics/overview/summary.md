# Process Management - Overview

## Key Definitions and Concepts

- **Process**: A program in execution—an active entity with its own memory space, execution context, system resources, and unique Process Identifier (PID)
- **Program**: A passive collection of instructions stored on disk; becomes a process when loaded into memory and executed
- **Process Control Block (PCB)**: Kernel data structure containing all information about a process including PID, state, program counter, CPU registers, memory information, and scheduling data
- **Process State**: The current condition of a process—New, Ready, Running, Waiting, or Terminated
- **Scheduler**: OS component that decides which process runs on the CPU; categorized as long-term (job scheduler), short-term (CPU scheduler), and medium-term (swapper)
- **Inter-Process Communication (IPC)**: Mechanisms allowing processes to communicate and share data, including pipes, message queues, shared memory, and sockets
- **Thread**: The smallest unit of CPU execution within a process; multiple threads share process resources while maintaining individual execution contexts

## Important Formulas and Theorems

- **Degree of Multiprogramming**: Controlled by long-term scheduler; represents the number of processes in memory simultaneously
- **CPU Burst Time**: Duration a process executes on the CPU before encountering an I/O request or being preempted
- **Context Switch Time**: Time required for the OS to save one process state and restore another; significantly lower for threads than processes
- **Throughput**: Number of processes completed per time unit; maximized by efficient scheduling
- **Turnaround Time**: Total time from process creation to completion—waiting time + execution time

## Key Points

- A process is more than just code—it encompasses the complete execution environment including memory, registers, stack, and system resources
- The Process Control Block serves as the central data structure for process management and is created when a process is created
- The five process states (New, Ready, Running, Waiting, Terminated) form the basis of process lifecycle management
- Process scheduling enables multiprogramming and gives the illusion of concurrent execution on limited CPU resources
- Parent-child process relationships are established through fork() operations, creating hierarchical process structures
- Multiple threads within a process share code, data, and system resources but maintain separate program counters and stacks
- User-level threads provide fast switching but cannot utilize multiple CPUs; kernel-level threads can but involve higher overhead
- Inter-process communication requires kernel involvement except when using shared memory, which offers the fastest communication

## Common Mistakes to Avoid

- Confusing processes with programs—every program can generate multiple processes, but not every process represents a unique program
- Forgetting that threads within a process share resources—leading to overlooked synchronization requirements
- Assuming only one process can be in ready or running state—the ready queue holds multiple processes; single-CPU systems have one running process
- Neglecting the difference between user-level and kernel-level threads when analyzing multithreading performance
- Overlooking the need for process synchronization when multiple processes access shared resources

## Revision Tips

1. Draw the complete process state diagram and practice explaining each transition with real-world examples
2. Create a table comparing IPC mechanisms based on communication type, performance, and complexity
3. Memorize PCB components by relating each to what the OS needs to resume a process after a context switch
4. Practice writing pseudocode for process creation and observe how parent and child processes differ
5. Review scheduling algorithms (FCFS, SJF, Round Robin) to understand how schedulers make allocation decisions