# Multithreading Models

## Overview

Multithreading allows a single process to execute multiple threads concurrently, each representing an independent flow of execution sharing process resources. The relationship between user threads and kernel threads is defined by multithreading models: Many-to-One, One-to-One, Many-to-Many, and Two-Level models.

## Key Points

- **Thread Benefits**: Responsiveness (remains responsive when part blocked), resource sharing (efficient sharing), economy (faster/cheaper than processes), scalability (utilizes multiprocessors)
- **User Threads**: Managed by user-level library without kernel support, fast creation/context switch, entire process blocks if one thread blocks
- **Kernel Threads**: Managed by OS kernel, slower creation/context switch, other threads can run if one blocks
- **Many-to-One Model**: Many user threads mapped to single kernel thread, efficient but entire process blocks on blocking call, cannot use multiprocessing
- **One-to-One Model**: Each user thread maps to kernel thread, better concurrency, can leverage multiple processors, overhead of creating kernel threads
- **Many-to-Many Model**: Multiple user threads multiplexed to smaller/equal number of kernel threads, best of both approaches
- **Two-Level Model**: Hybrid allowing some threads bound to specific kernel threads (one-to-one) while others multiplexed (many-to-many)

## Important Concepts

- User threads are invisible to kernel, kernel threads are scheduled by OS
- Many-to-One: efficient but blocks entire process and runs on single CPU
- One-to-One: true concurrency but kernel thread creation overhead
- Many-to-Many: flexibility with optimal kernel thread count, developer can create many user threads
- Examples: Many-to-One (green threads), One-to-One (Windows, Linux, modern Java), Many-to-Many (Solaris, IRIX)

## Notes

- Remember mapping patterns for each model (many user to one kernel, etc.)
- Compare advantages/disadvantages focusing on blocking behavior and multiprocessor utilization
- Know which model each OS uses (Windows/Linux use One-to-One, Solaris uses Many-to-Many)
- Understand practical implications for application performance and design
