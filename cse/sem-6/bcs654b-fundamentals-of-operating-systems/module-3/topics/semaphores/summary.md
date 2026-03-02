# Semaphores

## Overview

Semaphores are synchronization tools providing atomic wait() and signal() operations to control access to shared resources. They solve critical section problems through counting semaphores (multiple resources) or binary semaphores (mutual exclusion), preventing race conditions via OS-guaranteed atomicity.

## Key Points

- **Semaphore Operations**: wait(S) decrements and blocks if negative, signal(S) increments and wakes waiting process
- **Atomicity**: wait() and signal() operations indivisible, cannot be interrupted, preventing race conditions
- **Counting Semaphore**: Unrestricted integer value, manages multiple identical resource instances (value = available resources)
- **Binary Semaphore**: Value 0 or 1, implements mutual exclusion (1=available, 0=held)
- **Spinlock**: Busy waiting in loop, efficient for short waits, wastes CPU cycles
- **Blocking Semaphore**: Process moved to waiting queue, CPU relinquished, efficient for longer waits
- **Mutual Exclusion**: Binary semaphore mutex=1, wait(mutex) for entry, signal(mutex) for exit
- **Synchronization**: Semaphore sync=0 enforces execution order between processes

## Important Concepts

- Producer-Consumer: mutex=1 (buffer access), empty=BUFFER_SIZE (empty slots), full=0 (full slots)
- Readers-Writers: mutex=1 (read_count protection), wrt=1 (writer exclusion), read_count tracks active readers
- Deadlock from incorrect semaphore ordering: always acquire locks in consistent global order
- Starvation when process indefinitely denied resource (e.g., continuous readers blocking writers)

## Notes

- Differentiate counting (multiple resources) vs binary (mutual exclusion) semaphores
- Practice Producer-Consumer and Readers-Writers pseudocode
- Pay close attention to order of wait() calls - incorrect order causes deadlock
- Always state semaphore initial values - incorrect initialization breaks logic
