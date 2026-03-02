# Multithreaded Programming Overview - Summary

## Key Definitions

- **Thread**: The smallest unit of CPU execution within a process, consisting of a thread ID, program counter, register set, and stack, while sharing code, data, and OS resources with other threads in the same process.

- **Multithreading**: A programming paradigm enabling concurrent execution of multiple threads within a single process, maximizing CPU utilization and application responsiveness.

- **Thread Safety**: The property of a function ensuring correct behavior when called from multiple threads simultaneously, requiring synchronization when accessing shared resources.

- **Race Condition**: A situation where the behavior of a program depends on the relative timing of interleaved operations by multiple threads accessing shared data.

- **Deadlock**: A state where two or more threads are each waiting for resources held by the others, resulting in all threads being unable to proceed.

## Important Formulas

- **Thread Creation Overhead**: Approximately 10× faster than process creation
- **Thread Context Switch**: Typically 1/10th the cost of process context switch
- **Speedup Ratio** (with n cores, perfect parallelization): S = n
- **Amdahl's Law** (with parallel fraction p): S ≤ 1 / (1 - p)

## Key Points

1. Threads are lightweight processes that share most resources (address space, files, signals) with other threads in the same process while maintaining individual stacks and registers.

2. Multithreading improves responsiveness in interactive applications by allowing background operations without blocking user input handling.

3. User-level threads are managed by a thread library in user space (fast but cannot achieve true parallelism), while kernel-level threads are managed by the OS (true parallelism but higher overhead).

4. The many-to-many threading model offers the best balance by multiplexing many user threads onto fewer kernel threads.

5. Synchronization primitives (mutexes, semaphores, condition variables) are essential to coordinate access to shared resources and prevent data corruption.

6. Deadlock requires four conditions simultaneously: mutual exclusion, hold and wait, no preemption, and circular wait.

7. Proper thread synchronization must balance between over-synchronization (performance degradation) and under-synchronization (data corruption).

8. Thread pooling and thread reuse can reduce the overhead of frequent thread creation and destruction in high-throughput applications.

## Common Mistakes

1. **Forgetting to join threads**: Not calling pthread_join (or equivalent) can cause the main thread to terminate before child threads complete, leading to undefined behavior.

2. **Neglecting mutex initialization**: Using a mutex without proper initialization results in undefined behavior; always initialize mutexes before use and destroy them when finished.

3. **Deadlock from incorrect lock ordering**: Acquiring multiple locks in different orders by different threads is a common cause of deadlock; establish a consistent global lock ordering.

4. **Not checking return values**: Thread API functions return error codes; ignoring them can mask synchronization failures and resource exhaustion issues.

5. **Assuming atomic operations**: Simple statements like "counter++" are not atomic in C and require explicit synchronization; they involve read, increment, and write operations.