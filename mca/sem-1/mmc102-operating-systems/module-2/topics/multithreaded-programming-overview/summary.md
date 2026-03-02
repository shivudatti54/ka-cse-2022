# Multithreaded Programming Overview - Summary

## Key Definitions and Concepts

- THREAD: The smallest unit of CPU execution, representing a single sequential flow of control within a process. Each thread maintains its own program counter, register set, and stack, while sharing the process's code, data, and system resources.

- PROCESS: A heavyweight unit of resource allocation and protection that provides the execution environment for threads. Each process has its own virtual address space containing code, data, heap, and stack segments.

- USER-LEVEL THREADS: Threads managed entirely by a thread library in user space without kernel involvement, offering fast operations but suffering from the blocking problem.

- KERNEL-LEVEL THREADS: Threads directly managed by the operating system kernel, enabling true parallelism and proper handling of blocking operations but with higher overhead.

- RACE CONDITION: A situation where the final outcome of a computation depends on the relative timing of concurrent thread operations, producing nondeterministic and typically incorrect results.

- CRITICAL SECTION: A portion of code that accesses shared resources and must be executed atomically, protected by synchronization mechanisms to prevent concurrent access.

## Important Formulas and Characteristics

Thread creation overhead is significantly lower than process creation due to shared resources: process creation requires allocating separate address space and system resources, while thread creation reuses existing process resources.

Context switching between threads within the same process is faster than process context switches because thread switching avoids changing memory management information (page tables, TLB).

Maximum thread count depends on available memory: each thread requires stack space (typically 1-8 MB), so a process with 2GB user space might support hundreds to thousands of threads before exhausting addressable memory.

## Key Points

- THREADS ENABLE CONCURRENCY within a single process, allowing multiple operations to appear to execute simultaneously while sharing process resources.

- USER-LEVEL THREADS FAIL TO UTILIZE MULTIPLE PROCESSORS because the kernel schedules only the process, not individual user threads.

- KERNEL-LEVEL THREADS PROVIDE TRUE PARALLELISM but incur overhead for every thread operation requiring system calls.

- THE MANY-TO-MANY MODEL offers the best flexibility by mapping many user threads to fewer kernel threads, combining performance benefits of user-level threads with multiprocessor support.

- MUTEXES ENSURE MUTUAL EXCLUSION by allowing only one thread to access a protected resource at any given time.

- SEMAPHORES GENERALIZE MUTEXES by maintaining counts for managing finite pools of multiple identical resources.

- CONDITION VARIABLES ENABLE THREADS TO WAIT for application-specific conditions while releasing associated mutexes to allow other threads to proceed.

## Common Mistakes to Avoid

- CONFUSING THREADS WITH PROCESSES: Remember that threads share process resources while processes maintain separate address spaces. This distinction is fundamental and frequently tested.

- FORGETTING TO JOIN DETACHED THREADS: Detached threads release resources automatically, but joining allows retrieval of return values and ensures cleanup completion before process termination.

- CREATING DEADLOCKS through incorrect lock ordering or forgetting to release acquired locks. Always acquire locks in consistent order and ensure every acquire has a corresponding release.

- NEGLECTING SYNCHRONIZATION when accessing shared data. Even simple operations like counter increment involve multiple machine instructions and can cause race conditions when executed concurrently.

## Revision Tips

- PRACTICE DRAWING THREAD MODEL DIAGRAMS showing relationships between user-level threads, kernel threads, and the CPU to reinforce conceptual understanding.

- MEMORIZE THE KEY DIFFERENCES between user-level and kernel-level threads using comparison tables covering performance, blocking behavior, portability, and multiprocessor support.

- WORK THROUGH SYNCHRONIZATION PROBLEMS like producer-consumer and readers-writers to understand how primitives combine to solve complex coordination challenges.

- REVIEW OPERATING SYSTEM LECTURE NOTES on process scheduling to understand how threads become the scheduling entities when the kernel manages thread execution.