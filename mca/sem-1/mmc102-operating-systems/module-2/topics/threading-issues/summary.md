# Threading Issues - Summary

## Key Definitions and Concepts

- Critical Section: Code segment accessing shared resources where only one thread should execute at any given time.
- Race Condition: Unpredictable program behavior resulting from indeterminate thread scheduling affecting outcome.
- Deadlock: Circular waiting scenario where threads hold resources needed by others in the circular chain.
- Priority Inversion: Phenomenon where higher-priority threads wait due to lower-priority thread holding needed resource.
- Thread-Specific Data: Per-thread private storage accessible through key-based lookup mechanisms.

## Important Formulas and Theorems

- Coffman Conditions for Deadlock: Mutual exclusion + Hold and wait + No preemption + Circular wait = DEADLOCK possible.
- Bounded Waiting: If a thread enters its critical section n times, other threads can enter at most n times before it re-enters.
- Progress Property: Only threads not in remainder section can participate in deciding next critical section entrant.

## Key Points

- Synchronization primitives (mutexes, semaphores, condition variables) address the critical section problem.
- Mutexes provide exclusive access while semaphores manage resource counts with wait/signal operations.
- Deadlock prevention requires eliminating one of the four Coffman conditions, commonly hold-and-wait or circular wait.
- Priority inheritance temporarily elevates thread priority to resolve priority inversion scenarios.
- Thread cancellation must use cleanup handlers to release resources properly and maintain system consistency.
- Condition variables require mutex protection and should use while loops rather than if statements for condition checking.
- Race conditions occur at read-modify-write operations on shared data without atomic guarantees.

## Common Mistakes to Avoid

- Using if statements instead of while loops when waiting on condition variables, leading to spurious wakeup bugs.
- Forgetting to release locks in all code paths, especially during error conditions, causing deadlock.
- Attempting to acquire multiple locks in different orders across different threads, creating deadlock possibilities.
- Assuming asynchronous thread cancellation safely cleans up resources without cleanup handlers.

## Revision Tips

- Practice writing synchronization code for classic problems like producer-consumer until the patterns become automatic.
- Trace through deadlock scenarios by identifying the circular wait chain in resource allocation graphs.
- Remember that all synchronization operations must be atomic to prevent introducing new race conditions.
- Review POSIX thread API functions (pthread_create, pthread_mutex_lock, pthread_cond_wait, pthread_cancel) for exam.
- Understand why priority inheritance rather than priority ceiling or prevention is commonly used in real-time systems.