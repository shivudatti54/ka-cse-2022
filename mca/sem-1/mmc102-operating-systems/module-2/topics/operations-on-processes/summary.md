# Operations On Processes - Summary

## Key Definitions and Concepts

Process Creation: The operation of creating a new process in an operating system, typically involving memory allocation, PCB creation, and resource initialization.

Process Control Block (PCB): A kernel data structure containing all information about a process, including process ID, state, CPU registers, memory management information, and accounting data.

Context Switching: The procedure of saving and restoring the CPU state when switching between processes, enabling multiple processes to share a single CPU.

Zombie Process: A terminated process that remains in the process table because its parent has not yet called wait() to retrieve its exit status.

Orphan Process: A running process whose parent process has terminated; such processes are adopted by the init process.

Interprocess Communication (IPC): Mechanisms allowing processes to exchange data and synchronize their activities, including message-passing and shared-memory models.

## Important Formulas and Concepts

The fork() system call returns the child's PID to the parent and 0 to the child process. This return value distinction is fundamental for distinguishing parent and child execution paths.

The exit(status) system call terminates a process with the specified status, which can be retrieved by the parent using wait(&status).

Process states follow the five-state model: NEW → READY → RUNNING → BLOCKED → TERMINATED. State transitions occur due to specific events like I/O requests, CPU scheduling decisions, and process completion.

## Key Points

Process creation in UNIX uses fork() to create a child process and exec() to load a new program into the child process's address space.

The PCB serves as the central data structure for process management and is essential for context switching operations.

The wait() system call allows a parent process to synchronize with child termination and retrieve the child's exit status.

Context switching involves saving and restoring CPU registers, program counter, stack pointer, and memory management information.

Zombie processes can accumulate if parents repeatedly fail to call wait(), potentially exhausting the process table.

Interprocess communication can be achieved through message-passing (pipes, message queues, sockets) or shared-memory models.

The parent-child relationship in processes creates a hierarchical structure that facilitates resource inheritance and cleanup.

## Common Mistakes to Avoid

Confusing fork() with exec() is a common error. Remember that fork() creates a process, while exec() replaces the process's program.

Many students confuse zombie and orphan processes. Zombies have terminated but remain in the process table; orphans are still running but have no parent.

Forgetting that fork() returns twice in the program flow, leading to unexpected duplicate execution of code after the fork() call.

Assuming that process termination automatically cleans up all resources; parents must call wait() to reap children properly.

## Revision Tips

Draw the process state transition diagram repeatedly until you can reproduce it from memory. Label each transition with the event that causes it.

Write sample C programs using fork(), exec(), wait(), and exit() to understand their behavior in practice. Execution reveals details that pure theory cannot convey.

Create a table comparing zombie and orphan processes, including their definition, cause, and how the operating system handles each.

Review the PCB contents and understand why each field is necessary for process management. The PCB is the foundation of all process operations.