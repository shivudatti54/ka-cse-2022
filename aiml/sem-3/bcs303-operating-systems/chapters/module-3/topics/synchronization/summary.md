# Synchronization - Summary

## Key Definitions and Concepts

- **Synchronization**: Mechanism for managing concurrent access to shared resources to prevent race conditions and maintain data consistency
- **Critical Section**: Code segment that accesses shared variables or resources and must not be concurrently executed by more than one process
- **Race Condition**: Unpredictable behavior resulting from interleaved execution of processes accessing shared data
- **Semaphore**: Integer variable with two atomic operations wait() and signal(), used for synchronization
- **Binary Semaphore**: Semaphore taking only values 0 and 1, used for mutual exclusion
- **Counting Semaphore**: Semaphore with values >1, used for resource counting
- **Monitor**: High-level synchronization construct combining mutual exclusion with condition variables
- **Atomic Operation**: Operation that completes without interruption

## Important Formulas and Theorems

- **Peterson's Solution**: Uses `turn` variable and `flag[2]` array to achieve mutual exclusion for two processes
- **Test-and-Set**: Atomic instruction that reads and sets a boolean in one operation: `boolean test_and_set(boolean *target)`
- **Compare-and-Swap**: Atomic instruction: `CAS(*ptr, oldVal, newVal)` returns true if swap succeeded
- **Semaphore Operations**:
  - `wait(S)`: If S>0, decrement S; otherwise block process
  - `signal(S)`: Increment S; wake one waiting process if any

## Key Points

1. Synchronization is essential for preventing race conditions in concurrent systems
2. The critical section problem requires three properties: mutual exclusion, progress, and bounded waiting
3. Peterson's solution works only for two processes and has limitations on modern hardware
4. Hardware atomic instructions (test-and-set, CAS) provide building blocks for synchronization primitives
5. Semaphores abstract away hardware details and offer cleaner synchronization mechanisms
6. Binary semaphores (mutex) enforce mutual exclusion; counting semaphores manage multiple resources
7. Classical problems (producer-consumer, readers-writers, dining philosophers) illustrate common synchronization patterns
8. Monitors provide higher-level abstraction combining data and synchronization
9. Deadlock (circular waiting) and starvation (indefinite postponement) are two key problems in synchronization design
10. Choice of synchronization technique depends on system requirements, hardware support, and complexity tolerance

## Common Mistakes to Avoid

1. Forgetting that wait() and signal() must be atomic operations
2. Confusing binary semaphores with counting semaphores and using them inappropriately
3. Not initializing semaphores to correct values (mutex=1, empty=N, full=0 for producer-consumer)
4. Placing signal() before wait() in producer-consumer, causing deadlock
5. Overlooking the bounded waiting requirement when designing synchronization solutions

## Revision Tips

1. Practice implementing semaphore solutions for all three classical problems
2. Trace through Peterson's algorithm step-by-step with two processes
3. Understand how test-and-set provides atomicity on single and multi-processor systems
4. Review the difference between deadlock and starvation with examples
5. Memorize the standard semaphore patterns for producer-consumer (two semaphores + mutex)
6. Know why hardware-based atomic operations are preferred over pure software solutions