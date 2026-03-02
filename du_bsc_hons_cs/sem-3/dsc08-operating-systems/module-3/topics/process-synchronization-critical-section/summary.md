# Process Synchronization and Critical Section - Summary

## Key Definitions and Concepts

- **Critical Section**: A code segment that accesses shared variables and must not be executed by more than one process simultaneously
- **Race Condition**: When the final outcome depends on the relative timing of concurrent processes, leading to inconsistent results
- **Semaphore**: An integer variable with atomic wait() and signal() operations; used for synchronization
- **Mutex**: A binary semaphore (value 0 or 1) used for mutual exclusion
- **Atomic Operation**: An operation that completes entirely without interruption

## Important Formulas and Theorems

- **Peterson's Algorithm**: Uses `flag[]` array and `turn` variable for two-process mutual exclusion
- **TestAndSet**: Atomic instruction that returns old value while setting target to true
- **Swap**: Atomic instruction that exchanges values of two variables

## Key Points

1. The critical section problem requires satisfying **Mutual Exclusion**, **Progress**, and **Bounded Waiting**

2. Software solutions like Peterson's Algorithm work for only two processes and require atomic memory operations

3. Hardware solutions (TestAndSet, Swap) provide atomic operations but may cause busy waiting (spinlocks)

4. Semaphores are OS-supported synchronization primitives with atomic wait() and signal() operations

5. Producer-Consumer problem uses three semaphores: mutex, empty, and full

6. Readers-Writers problem allows multiple readers but exclusive writer access; priority can be given to either

7. Dining Philosophers problem demonstrates resource allocation and potential deadlock scenarios

8. Busy waiting wastes CPU cycles; blocking (as with semaphores) is more efficient

9. Deadlock occurs when processes wait indefinitely; starvation occurs when a process is perpetually denied resources

10. Atomicity is fundamental to all synchronization mechanisms

## Common Mistakes to Avoid

- Confusing mutual exclusion with progress conditions
- Using semaphore value incorrectly (e.g., initializing mutex to 0 instead of 1)
- Forgetting to release locks/semaphores in all code paths (leading to deadlock)
- Assuming operations are atomic without explicit synchronization
- Mixing up binary semaphores with mutexes (ownership semantics differ)

## Revision Tips

1. Draw timeline diagrams showing race conditions in simple counter increment scenarios

2. Practice writing semaphore solutions for Producer-Consumer and Readers-Writers from scratch

3. Memorize the three conditions of the critical section problem — questions often ask to verify if a solution satisfies these

4. Review hardware instructions (TestAndSet, Swap) and understand how they provide atomicity

5. Understand why Peterson's Algorithm doesn't work for more than two processes