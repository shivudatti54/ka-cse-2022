# Threads, Multicore Systems, and Multithreading - Summary

## Key Definitions and Concepts

- **Thread**: The smallest unit of CPU execution within a process; consists of thread ID, program counter, register set, and stack while sharing code, data, and OS resources with other threads in the same process
- **Process**: A heavyweight execution entity with separate memory space, requiring significant overhead for creation and context switching
- **User-Level Threads (ULT)**: Threads managed entirely by user-space libraries; kernel unaware of their existence; faster but cannot utilize multiple CPU cores
- **Kernel-Level Threads (KLT)**: Threads managed directly by the OS kernel; provide true parallelism but require kernel mode transitions
- **Multicore Processor**: A single chip containing multiple processing cores that can execute instructions independently and simultaneously

## Important Formulas and Theorems

- **Amdahl's Law**: Speedup = 1 / (S + (1-S)/N), where S = sequential fraction of program, N = number of processors
- **Thread Creation Time**: Typically 10-100 times faster than process creation
- **Thread Context Switch**: Much faster than process context switch due to shared memory space

## Key Points

- Threads share code section, data section, and OS resources with other threads in the same process, making them lightweight
- User-level threads provide better performance but suffer from blocking issues; kernel-level threads provide better reliability but with overhead
- The one-to-one model (used by Windows and Linux) is the most common modern implementation
- Multicore systems require careful synchronization to prevent data races and maintain cache coherence
- Race conditions occur when multiple threads access shared data without proper synchronization
- Deadlock requires four conditions: mutual exclusion, hold and wait, no preemption, and circular wait
- Mutex provides exclusive access (ownership), while semaphores are signaling mechanisms with counters
- Condition variables enable threads to wait for specific conditions, essential for producer-consumer problems

## Common Mistakes to Avoid

1. **Forgetting to initialize synchronization primitives** before use
2. **Not releasing locks** in all code paths (causing deadlock)
3. **Using while loops instead of if statements** for condition variables (prevents spurious wakeups)
4. **Confusing semaphores with mutexes**—semaphores can allow multiple simultaneous accesses
5. **Assuming thread execution order**—thread scheduling is non-deterministic

## Revision Tips

1. Practice writing pthread programs to understand thread creation, joining, and synchronization
2. Draw diagrams comparing multithreading models for visual retention
3. Memorize Amdahl's Law formula and practice speedup calculations
4. Review the four Coffman conditions for deadlock—they frequently appear in exams
5. Understand the difference between busy-waiting and blocking synchronization primitives
6. Review previous year DU question papers on this topic for pattern understanding
7. Implement classic problems (producer-consumer, readers-writers, dining philosophers) to solidify understanding