# Operations On Processes - Summary

## Key Definitions

- **Process Creation**: The operation of bringing a new process into existence, involving PCB allocation, memory assignment, and parent-child relationship establishment.

- **fork()**: A Unix system call that creates an exact copy of the calling process, with the child receiving return value 0 and parent receiving child's PID.

- **exec()**: A family of functions that replace the current process image with a new program, maintaining the same process ID.

- **Process Termination**: The operation of ending a process's execution and releasing its resources to the operating system.

- **Zombie Process**: A terminated process whose exit status has not been retrieved by its parent; remains in the process table consuming minimal resources.

- **Orphan Process**: A running process whose parent has terminated; automatically adopted by the init process.

- **wait()**: A system call that causes the parent process to block until one of its child processes terminates, retrieving the exit status.

## Important Formulas

- **Process Creation Cost**: T(n) = O(PCB initialization + Memory allocation + Parent state copy)

- **Zombie Prevention**: Parent must call wait() for each child to prevent zombie formation

## Key Points

1. Process creation involves allocating a Process Control Block (PCB) with unique PID, scheduling information, and resource allocations.

2. The fork() system call creates a child process as an exact copy of the parent, using copy-on-write to optimize memory duplication.

3. The fork-exec model separates process creation (fork) from program execution (exec), providing flexibility in Unix systems.

4. Windows combines creation and program loading in CreateProcess(), handling both operations atomically.

5. Normal process termination occurs via exit() or return from main(); abnormal termination results from signals or fatal errors.

6. The exit status is stored in the PCB and retrieved by the parent using wait()/waitpid() - convention: 0 = success.

7. Zombie processes form when a child terminates but parent hasn't called wait(); they consume only PCB resources.

8. Orphan processes are adopted by init (PID 1), which performs wait operations to prevent zombie formation.

9. Process hierarchies form trees where parent-child relationships enable collective operations like process groups.

10. Daemon processes are background processes detached from any terminal, running until system shutdown.

## Common Mistakes

1. **Forgetting to call wait()**: This causes zombie processes to accumulate, potentially exhausting the process table.

2. **Using exit() instead of _exit() in child after fork()**: The exit() function performs cleanup that may interfere with proper process termination in the child.

3. **Not checking fork() return value for errors**: Fork can fail (e.g., too many processes), and this must be handled.

4. **Confusing fork() and exec()**: Fork creates a copy of the current program; exec replaces the program entirely.

5. **Not understanding the two return values**: Fork returns twice - once to parent (with child's PID) and once to child (with 0).