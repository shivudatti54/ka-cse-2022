# Process Synchronization - Summary

## Key Definitions and Concepts

- **Critical Section**: The portion of code where a process accesses shared resources or shared data. Only one process should be allowed to execute in its critical section at any given time.

- **Mutual Exclusion**: A synchronization requirement stating that no two processes can simultaneously be in their critical sections.

- **Progress**: A synchronization requirement stating that if no process is in its critical section and processes wish to enter, only those not in remainder sections can participate in the decision.

- **Bounded Waiting**: A synchronization requirement stating that there exists a limit on the number of times other processes can enter their critical sections before a waiting process gets its turn.

- **Semaphore**: An integer variable with two atomic operations wait() and signal() used for process synchronization. The wait operation decrements the value, blocking if negative; signal increments and wakes a waiting process if any.

- **Atomic Operation**: An operation that completes entirely without interruption, ensuring that no other process can observe the operation in a partially completed state.

## Important Formulas and Theorems

- **Peterson's Solution**: Uses two shared variables—`turn` (indicates whose turn it is) and `flag[2]` (indicates readiness)—to achieve mutual exclusion for two processes.

- **TestAndSet Instruction**: Atomically returns the old value of a boolean while setting it to true. Used to implement mutual exclusion: `while (TestAndSet(&lock)) ;`

- **Swap Instruction**: Atomically exchanges values of two variables. Used for mutual exclusion by exchanging a process's local key with a shared lock.

- **Semaphore Operations**:
  - wait(S): if S > 0 then S = S - 1 else block the process
  - signal(S): S = S + 1; wake a waiting process if any

## Key Points

- The critical section problem is fundamental to all process synchronization, requiring mutual exclusion, progress, and bounded waiting.

- Peterson's solution provides a software-based approach for two processes using only shared memory variables.

- Hardware atomic instructions (TestAndSet, Swap) simplify synchronization but may cause busy waiting.

- Semaphores are OS-provided synchronization primitives that support blocking and waking of processes, avoiding busy waiting.

- Binary semaphores (mutex) are used for mutual exclusion; counting semaphores manage multiple identical resources.

- The producer-consumer problem uses semaphores to track empty and full buffer slots.

- The readers-writers problem requires allowing multiple readers while ensuring exclusive writer access.

- The dining philosophers problem illustrates deadlock and the need for careful resource allocation strategies.

## Common Mistakes to Avoid

- Forgetting to initialize semaphores with correct values—this leads to immediate blocking or loss of synchronization.

- Neglecting to make wait() and signal() atomic—this breaks the synchronization mechanism entirely.

- Confusing binary semaphores with counting semaphores and using them in wrong contexts.

- Creating deadlock in solutions like dining philosophers by allowing circular wait without proper prevention.

- Implementing busy-wait loops incorrectly, such as using non-atomic check-and-set operations.

## Revision Tips

- Practice writing complete pseudocode for semaphore solutions to producer-consumer and readers-writers problems.

- Memorize the three requirements of the critical section problem and be able to explain how each synchronization mechanism satisfies them.

- Review the conditions that lead to deadlock in the dining philosophers problem and understand prevention techniques.

- Solve previous year DU question papers to understand the exam pattern and important topics.