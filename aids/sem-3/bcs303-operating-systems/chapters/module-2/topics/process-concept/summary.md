# Process Concept - Summary

## Key Definitions and Concepts

- **Process**: An instance of a program in execution; a dynamic entity with its own execution context, memory space, and system resources

- **Process Control Block (PCB)**: A data structure maintained by the OS kernel that contains all information about a process, including PID, state, program counter, CPU registers, memory management information, and I/O status

- **Process State**: The current condition of a process - new, ready, running, waiting, or terminated

- **Context Switch**: The process of saving and restoring the state of a CPU so that multiple processes can share a single CPU

- **Zombie Process**: A terminated process whose exit status has not yet been collected by its parent

- **Orphan Process**: A process whose parent has terminated before the child

## Important Formulas and Theorems

- The **Five-State Process Model**: New → Ready → Running → Waiting → Terminated (with transitions between these states)

- The **fork()** system call creates an identical copy of the calling process; returns 0 to child and child's PID to parent

- The **exec()** family of functions replaces the current process image with a new program

## Key Points

1. A process is an active entity (program in execution), while a program is a passive entity (instructions stored on disk)

2. The PCB is the most critical data structure for process management and contains process identification, state, CPU registers, program counter, memory information, and accounting data

3. Only one process can be in the running state per CPU at any instant in a uniprocessor system

4. fork() followed by exec() is the standard mechanism for process creation in Unix-like systems

5. A parent process must call wait() to collect its child's exit status and prevent zombie processes

6. Context switching involves saving the entire execution context of one process and restoring another's, which incurs CPU overhead

7. Processes can be classified as foreground (interactive) or background (daemon/services), and as CPU-bound or I/O-bound

8. When a process makes a system call for I/O, it moves from running to waiting state until the I/O completes

## Common Mistakes to Avoid

- Confusing process with program: Remember that one program can generate multiple processes

- Forgetting that fork() creates an identical copy of the process (not a new program) - only after exec() does the child run different code

- Overlooking that terminated processes remain in the process table until the parent collects their exit status via wait()

- Not understanding that context switching involves saving complete CPU state, not just the program counter

## Revision Tips

1. Draw the five-state process model diagram and practice writing transitions between states

2. Create a table comparing process vs program with clear examples

3. Write a small C program using fork() and trace its execution step-by-step

4. Memorize the components of PCB and their purposes

5. For exam questions, always define key terms first before explaining concepts