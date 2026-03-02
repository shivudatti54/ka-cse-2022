# Process Synchronization

## Overview

Process synchronization solves the critical section problem using semaphores - integer variables accessed through atomic wait() and signal() operations. Semaphores prevent race conditions and enable mutual exclusion and event-based synchronization between concurrent processes.

## Key Points

- **Critical Section Problem Requirements**: Mutual exclusion (only one process in CS), progress (no indefinite postponement), bounded waiting (finite wait time)
- **Semaphore**: Integer variable accessed only through atomic wait() (P, decrement) and signal() (V, increment) operations
- **Counting Semaphore**: Value over unrestricted domain, manages multiple resource instances (e.g., 3 printers)
- **Binary Semaphore**: Value 0 or 1, implements mutual exclusion like a lock (1=available, 0=held)
- **Spinlock**: Busy waiting in loop, efficient for short waits, wastes CPU cycles
- **Blocking Semaphore**: Process moved to waiting queue, CPU relinquished, efficient for longer waits
- **Producer-Consumer**: Uses mutex (mutual exclusion), empty (empty slots), full (full slots) semaphores
- **Readers-Writers**: Multiple readers allowed, writer needs exclusive access, uses mutex and wrt semaphores

## Important Concepts

- Atomicity of wait() and signal() guaranteed by OS prevents race conditions on semaphore itself
- Order of wait() calls crucial - incorrect order causes deadlock
- Initialization matters: incorrect initial value breaks synchronization logic
- Deadlock occurs when processes wait indefinitely for events only other waiting processes can cause

## Notes

- Practice writing pseudocode for Producer-Consumer and Readers-Writers problems
- Always state semaphore initial values in solutions
- Watch for deadlock scenarios - acquire locks in consistent global order
- Understand starvation in Readers-Writers when readers prevent writers from accessing resource
