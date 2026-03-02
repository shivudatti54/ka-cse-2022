# Inter Process Communication (IPC) and Multi-threaded Programming: Overview

### Definitions and Concepts

- **Inter Process Communication (IPC):** Mechanism by which one process can communicate with another process or system.
- **Multi-threaded Programming:** Programming technique that allows multiple threads of execution to run concurrently within a single process.

### Key Concepts

- **Process:** Independent program execution unit with its own memory space.
- **Thread:** Lightweight process execution unit with shared memory space.
- **IPC Mechanisms:**
  - **Synchronous IPC:** Blocking communication between processes.
  - **Asynchronous IPC:** Non-blocking communication between processes.
- **Synchronization:** Techniques for coordinating access to shared resources.

### Important Formulas and Theorems

- **The Four Critical Sections Problem:** A fundamental problem in concurrent programming that deals with the access to shared resources.
- **Monitors and Semaphores:** Higher-level synchronization primitives that can be used to implement critical sections.

### Key IPC Mechanisms

- **Shared Memory:** Direct access to shared memory between processes.
- **Message Passing:** Use of messages to communicate between processes.
- **Pipe and Socket:** IPC mechanisms that provide a connection-oriented and connectionless communication respectively.

### Key Multi-threaded Programming Concepts

- **Thread Synchronization:** Techniques for coordinating access to shared resources.
- **Locks and Semaphores:** Lower-level synchronization primitives used for thread synchronization.
- **Deadlocks and Liveness:** Concepts related to thread synchronization.

### Important Theorems

- **Dektrik's Theorem:** A fundamental theorem in concurrent programming that deals with the impossibility of achieving predictable behavior in concurrent systems due to the presence of multiple threads.
- **Haberman's Theorem:** A theorem that states that if a system has the ability to synchronize multiple tasks using locks, then it will always deadlock.

### Study Tips

- Focus on understanding the basic concepts of processes, threads, and synchronization.
- Practice implementing IPC mechanisms and multi-threaded programming techniques.
- Review the important formulas and theorems to improve your understanding of concurrent systems.
