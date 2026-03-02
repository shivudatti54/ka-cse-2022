# Semaphores - Summary

## Key Definitions and Concepts

- **Semaphore**: A synchronization variable that is a non-negative integer with two atomic operations - wait (P) and signal (V)
- **Wait Operation (P)**: Decrements semaphore value; blocks process if value becomes negative
- **Signal Operation (V)**: Increments semaphore value; wakes waiting process if any
- **Atomic Operation**: Operation that executes without interruption - crucial for semaphore correctness
- **Critical Section**: Code segment accessing shared resources requiring mutual exclusion

## Important Formulas and Theorems

- **Binary Semaphore**: Value range {0, 1}, used for mutual exclusion, initialized to 1
- **Counting Semaphore**: Value range 0 to N, used for resource counting, initialized to N (resource count)
- **Synchronization Semaphore**: Initialized to 0 for forcing initial blocking
- **Producer-Consumer**: Requires empty (init N), full (init 0), and mutex (init 1)
- Bounded waiting satisfied when using properly implemented semaphores

## Key Points

1. Semaphores were introduced by Edsger Dijkstra in 1965
2. Binary semaphores provide mutual exclusion; counting semaphores manage multiple resources
3. Wait and signal operations must be atomic to prevent race conditions
4. Semaphores block processes instead of busy waiting (unlike spinlocks)
5. Binary semaphores differ from mutex: any process can signal a semaphore
6. Proper semaphore solutions satisfy mutual exclusion, progress, and bounded waiting
7. Deadlock can occur with incorrect semaphore implementation (e.g., circular wait)
8. Semaphores solve both mutual exclusion and synchronization problems
9. The producer-consumer problem requires three semaphores for proper solution
10. Initialization value determines semaphore behavior and purpose

## Common Mistakes to Avoid

1. Initializing binary semaphore to 0 instead of 1 for mutual exclusion
2. Forgetting to signal after wait, leading to deadlock
3. Using the same semaphore for both mutual exclusion and synchronization
4. Confusing binary semaphores with mutexes (ownership concept differs)
5. Not ensuring atomicity of wait/signal operations in implementation

## Revision Tips

1. Practice writing semaphore code for mutual exclusion and synchronization
2. Remember: wait decrements, signal increments - this is the core behavior
3. For binary semaphore in mutual exclusion, think "1 = available, 0 = in use"
4. Study the classical problems thoroughly as they frequently appear in exams
5. Draw timeline diagrams to visualize process blocking and waking
6. Memorize initial values: mutex=1, empty=N, full=0, sync=0
