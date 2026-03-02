# Synchronization

## Overview

Synchronization prevents race conditions when concurrent processes access shared resources using mechanisms like semaphores. The critical section problem requires mutual exclusion, progress, and bounded waiting, solved through atomic wait() and signal() operations on semaphores.

## Key Points

- **Race Condition**: Final outcome depends on particular order of accesses to shared resources
- **Critical Section**: Code segment accessing shared resource, only one process should execute at a time
- **Three Requirements**: Mutual exclusion (one process in CS), progress (no delay if no process in CS), bounded waiting (finite wait time before entry)
- **wait() Operation**: Decrements semaphore, blocks if value negative until non-negative
- **signal() Operation**: Increments semaphore, wakes one waiting process if any blocked
- **Counting Semaphore**: Manages multiple resource instances, value represents available units
- **Binary Semaphore**: Implements mutual exclusion (0 or 1 value), acts as lock
- **Producer-Consumer Solution**: mutex=1, empty=BUFFER_SIZE, full=0 semaphores

## Important Concepts

- Software solutions (Peterson's Algorithm) complex, require busy waiting, may not work on modern hardware
- OS-guaranteed atomicity of wait/signal operations essential for preventing race conditions
- Semaphores solve mutual exclusion and event-based synchronization (ordering)
- Deadlock by incorrect ordering solved by acquiring locks in consistent global order

## Notes

- Explain why software solutions insufficient before introducing semaphores
- Emphasize atomicity as key power of semaphores
- Know initialization values for classical problems (Producer-Consumer, Readers-Writers)
- Identify deadlock/starvation scenarios in pseudocode
