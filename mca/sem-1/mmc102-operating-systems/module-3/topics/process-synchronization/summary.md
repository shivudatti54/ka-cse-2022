# Process Synchronization - Summary

## Key Definitions and Concepts

- **Critical Section**: The portion of code where shared resources are accessed and where only one process should be allowed to execute at a time.
- **Race Condition**: A situation where the outcome of a program depends on the relative timing of concurrent processes.
- **Mutual Exclusion**: Ensuring that only one process can access a shared resource or execute in a critical section at any given time.
- **Semaphore**: An integer variable with atomic wait() and signal() operations used for process synchronization.
- **Monitor**: A high-level abstraction that combines shared data with procedures and synchronization mechanisms ensuring mutual exclusion.
- **Deadlock**: A state where two or more processes are each waiting for the other to release resources.

## Important Formulas and Theorems

- **Semaphore wait()**: Decrements the semaphore value; blocks if result is negative
- **Semaphore signal()**: Increments the semaphore value; wakes a waiting process if any
- **Critical Section Requirements**: Mutual exclusion, progress, bounded waiting (Dijkstra's criteria)
- **Coffman Conditions for Deadlock**: Mutual exclusion, hold and wait, no preemption, circular wait

## Key Points

- Process synchronization is essential for preventing race conditions when multiple processes access shared resources.
- The critical section problem requires that any valid solution satisfies mutual exclusion, progress, and bounded waiting.
- Hardware synchronization primitives like Test-and-Set provide atomic operations but may lead to busy-waiting.
- Semaphores are more flexible than hardware primitives and can solve complex synchronization problems.
- Binary semaphores implement mutual exclusion; counting semaphores manage multiple resource instances.
- Monitors provide automatic mutual exclusion with condition variables for more structured synchronization.
- The producer-consumer problem uses counting semaphores to track buffer slots; the readers-writers problem uses reader/writer counts with appropriate locking.
- Dining philosophers illustrates deadlock avoidance through careful resource acquisition ordering or central coordination.

## Common Mistakes to Avoid

- Reversing the order of wait operations in producer-consumer (waiting on mutex before empty/full causes deadlock).
- Forgetting to release semaphores in all code paths (unreleased semaphores cause deadlock or resource leaks).
- Using busy-waiting in semaphores without understanding its CPU overhead.
- Confusing monitors with semaphores—they provide different abstraction levels and synchronization semantics.
- Overlooking starvation possibilities when designing synchronization solutions.

## Revision Tips

- Practice writing semaphore-based solutions for all three classical problems (producer-consumer, readers-writers, dining philosophers).
- Always draw or trace through the execution sequence to verify mutual exclusion and absence of deadlock.
- Memorize the three requirements of the critical section problem—they form the basis for evaluating any solution.
- Understand why certain wait() orderings are required and what happens when they are violated.
- Review the difference between blocking (queue-based) and spinlock (busy-wait) semaphore implementations.