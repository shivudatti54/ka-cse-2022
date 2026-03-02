# Threads and Multithreading Models - Summary

## Key Definitions and Concepts

- **Thread**: The smallest unit of CPU execution, consisting of a thread ID, program counter, register set, and stack, sharing address space with other threads in the same process.
- **Process**: A heavyweight execution unit with separate address space, requiring substantial overhead for creation and context switching.
- **User Threads**: Threads managed entirely in user space by thread libraries, without kernel awareness.
- **Kernel Threads**: Threads managed directly by the operating system kernel, providing true parallelism.
- **Thread Safety**: The property of a program ensuring correct behavior when multiple threads access shared data simultaneously.

## Important Formulas and Theorems

- **Thread Creation Overhead**: Significantly lower than process creation; typically 10-100 times faster
- **Context Switch Time**: Thread context switches are faster (1-10μs) than process switches (10-100μs) due to shared address space
- **Memory Footprint**: Thread stack typically 1-2MB vs process address space of several GB
- **Amdahl's Law for Multithreading**: Speedup limited by sequential portion; theoretical maximum speedup = 1/(S + (1-S)/N) where S = serial fraction, N = number of threads

## Key Points

- Threads share address space, global variables, files, and other process resources, enabling efficient communication but requiring careful synchronization
- User threads provide fast creation but cannot achieve true parallelism on multi-processor systems due to kernel seeing only one thread
- Kernel threads allow true parallelism but incur higher overhead for thread management operations
- Many-to-one model: Simple implementation but blocks entire process on any blocking system call
- One-to-one model: Enables parallelism but creates scalability issues with many threads
- Many-to-many model: Optimal balance, allowing many user threads to be mapped to fewer kernel threads
- Mutexes provide mutual exclusion for critical sections; semaphores manage resource counting; condition variables coordinate thread execution based on state changes
- Race conditions occur when multiple threads access shared data without synchronization, leading to unpredictable results

## Common Mistakes to Avoid

- Forgetting to initialize synchronization primitives before use, leading to undefined behavior
- Creating too many threads, exceeding available CPU cores and causing excessive context switching overhead
- Deadlocks caused by acquiring locks in different orders across threads or forgetting to release locks
- Using blocking system calls in user-level threads (many-to-one model), which stalls the entire process
- Assuming thread creation is free; excessive thread creation/destruction impacts performance significantly

## Revision Tips

1. Create comparison tables for all four threading models, listing parallelism capability, blocking behavior, and implementation complexity
2. Practice implementing the producer-consumer and readers-writers problems using POSIX threads
3. Memorize the sequence of POSIX thread lifecycle functions: create → execute → join/terminate
4. Understand why mutex is preferred over spin locks for I/O-bound operations due to CPU wastage in busy-waiting
5. Review real-world applications (web servers, database systems, GUI applications) to understand practical multithreading benefits