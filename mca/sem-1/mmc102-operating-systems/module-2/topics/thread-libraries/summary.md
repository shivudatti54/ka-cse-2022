# Thread Libraries - Summary

## Key Definitions and Concepts

- **Thread Library**: An API providing functions for creating, managing, and synchronizing multiple threads of execution within a single process
- **User-Level Threads**: Threads managed entirely in user space without kernel support; portable but cannot utilize multiple processors
- **Kernel-Level Threads**: Threads managed by the operating system kernel; can leverage multi-processor systems but have higher creation overhead
- **Thread Safety**: Property of code that ensures correct behavior when accessed by multiple threads simultaneously
- **Reentrant Code**: Code that can be safely called again while a previous call is still executing; inherently thread-safe

## Important Formulas and Theorems

- Thread creation overhead: pthread_create() vs CreateThread() have different system call costs
- Thread pool sizing: Optimal pool size typically equals the number of available processors for CPU-bound tasks
- Amdahl's Law: Theoretical speedup limitation based on the proportion of sequential code in parallel programs

## Key Points

- POSIX Threads (Pthreads) is the standardized portable API for UNIX/POSIX systems with approximately 100 functions
- Windows Threading API provides kernel-level thread management with primitives like critical sections and fibers
- Java threads map directly to kernel threads, providing true parallel execution on multi-core systems
- Mutexes provide mutual exclusion while semaphores allow counting access to resources
- Condition variables enable thread coordination based on state changes in shared data
- Thread pools reuse worker threads to minimize creation/destruction overhead
- Thread-local storage (TLS) provides thread-private global variables
- The Runnable interface is preferred over extending Thread class due to Java's single inheritance limitation

## Common Mistakes to Avoid

- Forgetting to join or wait for threads, leading to premature program termination before thread completion
- Failing to release acquired mutexes, causing deadlock scenarios
- Creating new threads for every task instead of using thread pools, resulting in excessive resource consumption
- Assuming thread execution order, which is non-deterministic due to OS scheduling
- Neglecting thread safety when accessing shared resources, resulting in race conditions

## Revision Tips

- Practice writing Pthreads code for common scenarios: thread creation, mutex usage, condition variables
- Create comparison charts differentiating Pthreads, Windows API, and Java threading mechanisms
- Memorize the sequence: lock → access shared data → unlock for proper synchronization
- Review Java ExecutorService patterns for thread pool implementation
- Understand deadlock conditions: mutual exclusion, hold and wait, no preemption, circular wait