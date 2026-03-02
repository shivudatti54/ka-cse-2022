# **Inter Process Communication and Multi-Threaded Programming: Overview**

### Key Concepts

- **Inter-Process Communication (IPC)**:
  - Process-to-Process Communication
  - Synchronization and Coordination
  - Types of IPC:
    - Synchronous IPC (e.g., Pipes, Sockets)
    - Asynchronous IPC (e.g., Messages, Shared Memory)
- **Multi-Threaded Programming**:
  - Multiple threads within a single process
  - Shared resources and synchronization
  - Types of threads:
    - User-level threads
    - Kernel-level threads
- **Synchronization**:
  - Ensures threads access shared resources safely
  - Types of synchronization:
    - Mutual Exclusion (Mutex)
    - Semaphores
    - Monitors

### Important Formulas and Definitions

- **Semaphore**:
  - A variable that controls the access to a common resource
  - Formula: `S = (current count - operation) % max count`
- **Monitor**:
  - A data structure that manages access to shared resources
  - Definition: A monitor is a synchronization mechanism that allows threads to access shared data safely
- **Atomic Operations**:
  - A sequence of operations that can be performed as a single, uninterruptible unit
  - Formula: `A XOR B XOR C = A`

### Important Theorems

- **Lamport's Bakery Algorithm**:
  - A synchronization algorithm for concurrent access to shared resources
  - Theorem: If `P` and `Q` are two threads that request to access the same resource, then `P` will be granted access before `Q` if `P` requests the resource earlier.

### Revision Tips

- Understand the different types of IPC and their use cases
- Familiarize yourself with synchronization mechanisms such as semaphores, monitors, and mutexes
- Learn atomic operations and their applications in multi-threaded programming
- Practice solving synchronization problems using Lamport's Bakery Algorithm
