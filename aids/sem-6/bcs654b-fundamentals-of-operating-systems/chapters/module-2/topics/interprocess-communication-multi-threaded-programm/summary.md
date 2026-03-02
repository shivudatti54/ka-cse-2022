# Interprocess Communication and Multi-Threaded Programming: Overview

### Key Concepts

- **Interprocess Communication (IPC)**: Communication between two or more processes
- **Multi-threaded Programming**: Programming that uses multiple threads within a single process

### Definitions

- **Process**: A program in execution
- **Thread**: A lightweight process that runs concurrently with other threads within a process
- **Synchronization**: Coordinating access to shared resources among multiple threads

### Important Formulas and Theorems

- **Linux IPC Mechanisms**:
  - Messages (e.g., pipes, sockets)
  - Shared memory (e.g., semaphores, mutexes)
  - Inter-process queues (e.g., queues, locks)
- **Thread Synchronization**:
  - Monitors (e.g., deadlock, livelock)
  - Atomic operations (e.g., locking, unlocking)
- **Threading Theory**:
  - Thread creation and management
  - Thread communication (e.g., send, receive)

### Key IPC Mechanisms

- **Pipes**: Unidirectional data transfer between two processes
- **Sockets**: Bidirectional data transfer between two processes
- **Shared Memory**: Direct access to shared data between processes
- **Queues**: First-in, first-out data transfer between processes

### Key Multi-threaded Programming Concepts

- **Thread States**: Running, sleeping, waiting, dead
- **Thread Synchronization Primitives**: Locks, semaphores, monitors
- **Thread Communication**: Send, receive, shared variables

### Revision Tips

- Understand the differences between processes and threads
- Familiarize yourself with key IPC mechanisms (pipes, sockets, shared memory, queues)
- Know the importance of thread synchronization and its various techniques (locks, semaphores, monitors)
- Practice creating and managing threads, as well as synchronizing access to shared resources.
