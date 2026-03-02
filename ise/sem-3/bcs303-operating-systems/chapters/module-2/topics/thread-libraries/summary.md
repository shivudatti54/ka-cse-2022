# Thread Libraries - Summary

## Key Definitions and Concepts

- THREAD LIBRARY: A programming interface providing functions to create, manage, and synchronize multiple threads within a process
- USER-LEVEL THREADS: Threads managed entirely in user space without kernel awareness; faster but vulnerable to process blocking
- KERNEL-LEVEL THREADS: Threads managed directly by the operating system kernel; better multi-processor utilization but slower operations
- MUTEX: A synchronization primitive providing mutual exclusion to protect shared resources
- CONDITION VARIABLE: A synchronization primitive allowing threads to wait for specific conditions to be signaled
- SEMAPHORE: An integer-valued counter controlling access to a finite number of resources
- THREAD POOL: A design pattern reusing a fixed number of worker threads for multiple tasks

## Important Formulas and Theorems

- DEADLOCK CONDITIONS (Coffman Conditions): Mutual exclusion, Hold and wait, No preemption, Circular wait — ALL FOUR must hold for deadlock to occur
- RACE CONDITION: Occurs when the outcome of a program depends on the relative timing of interleaved thread executions

## Key Points

- Thread libraries provide abstractions for concurrent execution within a single process
- POSIX Threads (pthreads) is the standard threading interface for Unix-like systems
- Windows Thread API provides kernel-level threading support on Windows platforms
- User-level threads offer faster creation and switching but cannot utilize multiple processors
- Kernel-level threads provide better concurrency but require system calls for thread operations
- Mutexes ensure exclusive access to shared resources, preventing data races
- Condition variables enable efficient wait-notify patterns without busy-waiting
- Thread pools reduce overhead by reusing threads instead of creating new ones for each task
- Thread scheduling is influenced by priority, processor affinity, and operating system policies

## Common Mistakes to Avoid

- FORGETTING TO INITIALIZE synchronization primitives before use
- NOT UNLOCKING mutexes after acquisition, leading to deadlock
- USING condition variables without associated mutex locks
- CREATING too many threads, causing excessive context switching overhead
- NOT JOINING or DETACHING threads, potentially causing resource leaks

## Revision Tips

- PRACTICE writing Pthreads programs covering creation, synchronization, and common patterns
- MEMORIZE key function signatures for pthread_create, pthread_join, mutex, and condition variable operations
- UNDERSTAND the difference between blocking and non-blocking synchronization
- ANALYZE sample thread programs to identify synchronization issues and race conditions
- REVIEW deadlock scenarios and understand how to prevent circular wait conditions