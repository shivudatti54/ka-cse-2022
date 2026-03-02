# Inter Process Communication - Summary

## Key Definitions and Concepts

Inter Process Communication (IPC) is the mechanism by which processes exchange data and synchronize their actions. Processes have separate address spaces, requiring OS-provided mechanisms for communication. The fundamental models are shared memory (direct access to common memory region) and message passing (kernel-mediated data transfer through communication channels).

## Important Formulas and Techniques

Semaphore operations follow atomic protocols: wait(S) decrements S and blocks if S becomes negative; signal(S) increments S and wakes a waiting process if any exists. The producer-consumer solution uses two semaphores (empty and full) plus a mutex for buffer access. The readers-writers problem uses readcount and corresponding semaphores to allow multiple readers or exclusive writers.

## Key Points

- SHARED MEMORY provides fastest communication but requires explicit synchronization through semaphores or mutexes to prevent race conditions.

- MESSAGE PASSING involves kernel copying data between address spaces, providing better isolation but slower performance for large data transfers.

- PIPES are unidirectional byte streams created using pipe() system call; FIFOs (named pipes) allow unrelated processes to communicate.

- SOCKETS provide versatile endpoint communication supporting both local (UNIX domain) and network communication with TCP (reliable) and UDP (fast) protocols.

- SIGNALS are asynchronous notifications sent to processes for event notification; handlers must be async-signal-safe.

- SEMAPHORES are integer-valued synchronization primitives with atomic wait() and signal() operations; binary semaphores (mutexes) enforce mutual exclusion.

- The CRITICAL SECTION problem requires mutual exclusion, progress, and bounded waiting solutions achieved through hardware instructions or software algorithms.

- DEADLOCK occurs when processes hold resources while waiting for additional resources held by others; prevention requires eliminating one of four necessary conditions.

## Common Mistakes to Avoid

Failing to close unused pipe ends causes blocking issues because the kernel only sends EOF when all write ends are closed. Not initializing semaphores before use leads to undefined behavior; always use sem_init() with proper initial values.

Ignoring the atomic nature of operations results in race conditions. Operations that appear simple may not be atomic at the hardware level, requiring explicit synchronization primitives.

Confusing blocking and non-blocking I/O operations is a common error. Always verify the blocking characteristics of pipes, sockets, and message queues when designing concurrent systems.

## Revision Tips

Practice writing code for all major IPC mechanisms to reinforce understanding. Memorize the sequence of system calls for each mechanism (pipe-fork-read-write, shmget-shmat-shmdt, socket-bind-listen-accept).

Solve classical synchronization problems like producer-consumer, readers-writers, and dining philosophers. Understand why certain solutions work and what problems they prevent.

Draw timing diagrams and state diagrams for concurrent processes to visualize the sequence of operations and identify potential race conditions or deadlocks.