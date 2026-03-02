# Semaphores - Summary

## Key Definitions

- **Semaphore:** An integer variable with two atomic operations wait() and signal(), used for process synchronization.
- **wait(S):** An operation that decrements semaphore S; blocks the process if S ≤ 0.
- **signal(S):** An operation that increments semaphore S; wakes a waiting process if any.
- **Binary Semaphore:** A semaphore taking only values 0 and 1; used for mutual exclusion.
- **Counting Semaphore:** A semaphore with non-negative integer values; used for resource management.

## Important Formulas

- Initial value for binary semaphore (mutual exclusion): S = 1
- Initial value for counting semaphore: S = number of available resources
- wait(S): S = S - 1 (after atomic check that S > 0)
- signal(S): S = S + 1

## Key Points

1. Semaphores were introduced by Edsger Dijkstra in 1965 as a general-purpose synchronization mechanism.

2. The wait and signal operations must be atomic to prevent race conditions; OS ensures atomicity through hardware support.

3. Binary semaphores (mutex) are used for mutual exclusion, ensuring only one process enters a critical section.

4. Counting semaphores manage multiple identical resources; the value represents available resource count.

5. In the producer-consumer problem, "empty" tracks buffer space, "full" tracks filled slots, and "mutex" ensures exclusive buffer access.

6. Queue-based semaphore implementation (vs. busy-waiting) prevents CPU waste and is more efficient.

7. Semaphores can solve the critical section problem, producer-consumer, readers-writers, and dining philosophers problems.

8. Improper semaphore usage can lead to deadlock (e.g., acquiring semaphores in different orders) or starvation.

## Common Mistakes

1. Confusing wait and signal operations—remember wait decrements (acquires) and signal increments (releases).

2. Forgetting to initialize semaphores; the initial value determines the semaphore's behavior.

3. Not using mutex along with counting semaphores in producer-consumer, leading to race conditions on the buffer.

4. Assuming semaphores solve all synchronization problems—incorrect ordering can still cause deadlock.

5. Using busy-waiting (spinlocks) in exam answers when queue-based implementation is preferred.