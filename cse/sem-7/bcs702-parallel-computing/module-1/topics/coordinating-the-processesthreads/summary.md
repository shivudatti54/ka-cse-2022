# Coordinating Processes and Threads

=====================================

### Overview

Coordinating processes and threads is the mechanism for managing interaction between concurrent execution entities to ensure correct, predictable, and efficient parallel program execution. Without proper coordination, shared resource access leads to race conditions, data corruption, and incorrect results.

### Key Points

- **Processes vs Threads:** Processes are heavyweight with their own memory space; threads are lightweight and share memory within a process.
- **Critical Section:** A code segment accessing shared resources that must be executed with mutual exclusion.
- **Three Requirements:** Mutual exclusion (only one entity at a time), Progress (no indefinite postponement), and Bounded Waiting (no starvation).
- **Locks/Mutexes:** Simplest mechanism; a thread must acquire the lock before entering and release it when leaving the critical section.
- **Semaphores:** Generalized synchronization tool with wait(P) and signal(V) atomic operations; invented by Dijkstra.
- **Binary vs Counting Semaphore:** Binary (0 or 1) acts as a mutex; counting semaphore controls access to resources with multiple instances.
- **Monitors:** High-level language construct encapsulating shared data and procedures; only one thread active inside at a time.
- **Shared Memory Communication:** Fast but requires explicit synchronization to avoid race conditions.
- **Message Passing Communication:** No shared state, naturally safer, used for distributed processes (e.g., MPI).

### Important Concepts

- Race condition: outcome depends on non-deterministic execution order of concurrent entities
- Semaphore wait(S): decrements S, blocks if S becomes negative; signal(S): increments S, wakes a blocked process
- Shared memory is faster but needs synchronization; message passing avoids shared state but involves data copying overhead
- Java synchronized methods/blocks implement monitor-like concepts

### Notes

- For exams, know the three conditions for solving the critical section problem (mutual exclusion, progress, bounded waiting).
- Be able to distinguish between binary and counting semaphores with use-case examples.
- Understand the trade-off: shared memory is fast but error-prone; message passing is safer but slower.
