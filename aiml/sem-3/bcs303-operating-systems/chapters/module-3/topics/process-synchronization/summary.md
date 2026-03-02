# Process Synchronization - Summary

## Key Definitions and Concepts

- **Process Synchronization**: Mechanism to coordinate execution of multiple processes accessing shared resources to prevent inconsistencies
- **Race Condition**: Undesirable situation where final outcome depends on the order of interleaving operations between processes
- **Critical Section**: Portion of code where shared variables are accessed; requires controlled access
- **Mutual Exclusion**: Property ensuring no two processes can simultaneously occupy their critical sections
- **Progress**: Requirement that only processes not in remainder section can participate in deciding the next entrant
- **Bounded Waiting**: Guarantee that a process requesting entry will eventually enter within a limited time
- **Semaphore**: Integer variable with atomic wait() and signal() operations; binary for mutual exclusion, counting for resource management

## Important Formulas and Theorems

- **Peterson's Solution**: Uses `flag[i]` and `turn` variables; satisfies all three critical section requirements for two processes
- **Test-and-Set**: Atomic operation that returns old value while setting location to true: `boolean testAndSet(boolean *target)`
- **Semaphore Operations**:
  - `wait(S)`: While S ≤ 0, spin; otherwise S--
  - `signal(S)`: S++
- **Producer-Consumer**: Requires `empty`, `full`, and `mutex` semaphores; empty = n, full = 0 initially

## Key Points

- Race conditions arise from concurrent access to shared data without proper synchronization
- The critical section problem requires satisfying mutual exclusion, progress, and bounded waiting simultaneously
- Peterson's solution provides software-based mutual exclusion for exactly two processes
- Hardware atomic instructions (test-and-set, swap) enable implementation of synchronization primitives
- Semaphores abstract the complexity of busy-waiting and provide cleaner synchronization mechanisms
- Binary semaphores provide mutual exclusion; counting semaphores manage multiple identical resources
- Deadlock occurs when circular wait exists; starvation occurs from indefinite postponement

## Common Mistakes to Avoid

- Confusing bounded waiting with progress: progress is about who enters next, bounded waiting limits total entries after a request
- Using busy-wait (spinlock) semaphores without considering CPU waste in production systems
- Forgetting that semaphore operations must be atomic to prevent race conditions within the synchronization mechanism itself
- Not distinguishing between deadlock (permanent blocking) and starvation (unfair but possibly temporary)

## Revision Tips

- Practice drawing execution interleavings for Peterson's solution to verify mutual exclusion
- Memorize the standard semaphore pattern for producer-consumer: empty (n), full (0), mutex (1)
- Review why hardware atomic operations are necessary on multi-processor systems
- Understand that bounded waiting prevents starvation of any single process
- Focus on the three requirements of critical section problem as most exam questions test these concepts