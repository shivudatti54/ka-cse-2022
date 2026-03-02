# Exec Functions and IPC Methods - Summary

## Key Definitions and Concepts

- **exec family:** Functions that replace the current process image with a new program without creating a new process; the PID remains unchanged
- **IPC (Inter-Process Communication):** Mechanisms allowing processes to exchange data and synchronize operations
- **Pipe:** Unidirectional communication channel created using `pipe()` system call
- **Named Pipe (FIFO):** Special file allowing unrelated processes to communicate
- **Shared Memory:** IPC mechanism where multiple processes share the same memory segment directly
- **Semaphore:** Integer-valued counter used for process synchronization and resource management
- **Signal:** Asynchronous notification mechanism for inter-process event handling

## Important Formulas and Theorems

- **exec() return value:** Returns -1 on failure; on success, control never returns to calling program
- **Pipe creation:** `int pipe(int pipefd[2])` returns 0 on success, -1 on failure
- **Shared memory:** `shmget(key, size, flags)` creates/gets segment; `shmat()` attaches; `shmdt()` detaches
- **Semaphore operations:** `semop(semid, sembuf *, nsops)` performs atomic operations

## Key Points

1. The exec functions (execl, execlp, execle, execv, execvp, execve) replace the program being executed without creating a new process
2. Variants with 'p' search PATH for executable; variants with 'e' allow environment specification
3. Arguments to exec can be passed as a list (execl series) or as an array (execv series)
4. Unnamed pipes work only between parent-child processes; named pipes (FIFOs) work between any processes
5. Shared memory provides fastest IPC but requires synchronization via semaphores
6. Message queues support asynchronous communication with message typing
7. Semaphores provide atomic operations for process synchronization
8. Sockets are the most versatile IPC, supporting both local and network communication
9. Signals provide asynchronous notification but cannot carry substantial data

## Common Mistakes to Avoid

1. Forgetting to check exec() return value - it only returns on failure
2. Not closing unused pipe ends, leading to deadlocks or unexpected behavior
3. Failing to synchronize shared memory access, causing race conditions
4. Using unnamed pipes for unrelated processes (should use named pipes/FIFOs)
5. Confusing fork() with exec() - fork creates new process, exec replaces program
6. Not providing NULL as last argument in execl/execlp variants
7. Forgetting to detach from shared memory after use

## Revision Tips

1. Practice writing programs using each exec variant to understand argument passing
2. Draw diagrams showing data flow in pipe communication
3. Compare IPC methods based on speed, complexity, and use cases
4. Remember the memory layout changes when exec() is called (code, data, heap, stack replaced)
5. Review semaphore operations and understand why they must be atomic
6. Focus on the differences between various IPC mechanisms for exam questions
