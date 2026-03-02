# Semaphores - Summary

## Key Definitions and Concepts

- **Semaphore**: An integer-valued synchronization variable with two atomic operations: wait (P/Proberen) and signal (V/Verhogen), introduced by Edsger Dijkstra in 1965.
- **Binary Semaphore**: Takes only values 0 and 1; used for mutual exclusion (mutex locks).
- **Counting Semaphores**: Non-negative integer values representing available identical resources.
- **Atomic Operation**: An operation that executes without interruption, preventing race conditions.
- **Spinlock**: Busy-waiting implementation where processes continuously check semaphore value.
- **Block-Wakeup**: Implementation where blocked processes are added to a queue and awakened by signal operations.

## Important Formulas and Theorems

- **wait(S) operation**: Decrements S; blocks process if S <= 0 after decrement
- **signal(S) operation**: Increments S; wakes one waiting process if any in queue
- **Critical Section Solution**: Binary semaphore initialized to 1 ensures mutual exclusion
- **Producer-Consumer**: Uses three semaphores—empty (initialized to buffer size), full (initialized to 0), and mutex (initialized to 1)

## Key Points

1. Semaphores solve the critical section problem by providing atomic operations for resource allocation
2. Binary semaphores provide mutual exclusion but do not guarantee bounded waiting or progress
3. Counting semaphores manage multiple identical resources efficiently
4. The wait operation must block (not busy-wait) on modern systems to conserve CPU resources
5. Signal operations should wake exactly one waiting process to maintain correctness
6. Semaphores can be used to solve producer-consumer, readers-writer, and dining philosophers problems
7. Deadlock occurs with semaphores when circular wait exists: P1 holds S1 waits for S2, P2 holds S2 waits for S1
8. Resource ordering prevents circular wait by enforcing a fixed acquisition sequence
9. FIFO queues in semaphore implementations ensure fairness among waiting processes
10. Hardware support like Test-and-Set enables atomic semaphore operations

## Common Mistakes to Avoid

1. Forgetting to initialize semaphores—solutions depend critically on initial values
2. Placing signal operations outside critical sections, leading to race conditions
3. Using the same semaphore for different synchronization purposes, causing interference
4. Not checking for deadlock potential in solutions involving multiple semaphores
5. Confusing binary semaphores with mutex locks—they have subtle behavioral differences regarding signal ownership

## Revision Tips

1. Practice writing semaphore solutions for producer-consumer and readers-writer problems until they become automatic
2. Trace through execution sequences step-by-step to verify mutual exclusion
3. Always identify circular wait conditions when analyzing multi-semaphore solutions
4. Memorize the standard initial values: mutex=1, empty=buffer_size, full=0
5. Review Dijkstra's terminology: P for wait (Proberen), V for signal (Verhogen)