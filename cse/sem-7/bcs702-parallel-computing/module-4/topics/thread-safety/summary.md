# Thread Safety in Parallel Computing

=====================================

### Overview

Thread safety refers to the property of code that functions correctly when accessed by multiple threads simultaneously. A thread-safe function or data structure can be called from multiple threads without causing race conditions, data corruption, or undefined behavior. Ensuring thread safety is fundamental to writing correct shared-memory parallel programs.

### Key Points

- **Race Condition:** Occurs when multiple threads access shared data simultaneously and at least one thread writes
- **Critical Section:** A code segment that accesses shared resources and must be executed by only one thread at a time
- **Mutex (Mutual Exclusion):** A lock mechanism ensuring only one thread enters a critical section at a time
- **Atomic Operations:** Hardware-supported indivisible operations (e.g., `#pragma omp atomic` for read-modify-write)
- **Thread-Safe Functions:** Functions that use only local variables or properly synchronize access to shared data
- **Reentrant Functions:** Functions that do not use static or global data; can be safely called by multiple threads
- **Deadlock:** When two or more threads wait indefinitely for each other to release locks

### Important Concepts

- The `count++` operation is NOT atomic: it involves read, modify, and write steps that can interleave
- OpenMP synchronization: `#pragma omp critical`, `#pragma omp atomic`, `#pragma omp barrier`
- Reduction clauses provide thread-safe accumulation without explicit locking
- Thread-local storage eliminates sharing entirely, avoiding race conditions

### Notes

- Identify the critical section in code by finding shared variables that are both read and written
- Prefer reduction clauses over critical sections for accumulation patterns
- Minimize the scope of critical sections to reduce serialization and improve performance
- Be able to identify non-thread-safe code and propose fixes using OpenMP synchronization directives