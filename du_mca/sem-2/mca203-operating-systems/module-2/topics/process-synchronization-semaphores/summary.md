# Process Synchronization - Semaphores - Summary

## Key Definitions and Concepts

- **Critical Section**: Code segment accessing shared resources requiring mutual exclusion
- **Semaphore**: Synchronization variable with integer value and two atomic operations—wait() and signal()
- **Binary Semaphore**: Takes only 0 and 1 values; implements mutual exclusion like a mutex lock
- **Counting Semaphore**: Integer value >1; controls access to multiple instances of a resource
- **Atomic Operation**: Operation that executes completely without interruption from other processes
- **Race Condition**: Unpredictable behavior due to timing-dependent access to shared resources
- **Deadlock**: Circular wait where each process holds resources needed by others

## Important Formulas and Theorems

- **wait(S)**: If S > 0, decrement S and proceed; otherwise, block the process
- **signal(S)**: Increment S and wake one waiting process if any exists
- Semaphore value formula: S = number of available resources + number of waiting processes (when S < 0, |S| equals waiting processes)

## Key Points

- Semaphores were introduced by Edsger Dijkstra in 1965 as a fundamental synchronization primitive
- Binary semaphores provide mutual exclusion while counting semaphores manage multiple resource instances
- The wait() operation must execute atomically to prevent race conditions
- In producer-consumer, always wait on empty/full before mutex to avoid deadlock
- Readers-writers problem: first reader locks resource, last reader releases it
- Semaphores support queue-based waiting, unlike spinlocks that busy-wait
- Signal operations never block; they either wake a process or increment the count
- Three requirements of critical section: mutual exclusion, progress, bounded waiting

## Common Mistakes to Avoid

- Acquiring semaphores in inconsistent orders causing deadlock
- Forgetting to signal after wait, leading to resource leaks and blocked processes
- Confusing binary semaphores with counting semaphores in solutions
- Not ensuring atomicity of wait/signal operations in implementation
- Performing wait on mutex before counting semaphores in producer-consumer
- Assuming signal immediately wakes waiting process (depends on scheduler)

## Revision Tips

1. Practice writing semaphore solutions for the three classical problems until automatic
2. Draw process timelines showing semaphore values through each operation
3. Memorize the correct order: wait counting semaphores before mutex in producer-consumer
4. Focus on understanding why certain semaphore operations prevent specific race conditions
5. Review past DU exam questions on semaphores to understand the expected answer format