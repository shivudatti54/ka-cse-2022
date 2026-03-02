# **Threading Issues**

**Definition:** Threading issues refer to problems that occur when multiple threads are executed concurrently in a multi-threaded program.

**Key Points:**

- **Deadlocks:** Two or more threads are blocked indefinitely, each waiting for the other to release a resource.
  - Example: Thread A locks resource A, then waits for resource B. Thread B locks resource B, then waits for resource A.
- **Liveness Problem:** A thread is unable to make progress due to other threads holding onto resources.
  - Formula: Liveness = (Number of threads) - (Number of threads that are blocked)
- **Starvation:** A thread is unable to access a resource due to other threads holding onto it for an extended period.
  - Example: Thread A is blocked by Thread B, which is also blocked by Thread C.
- **Priority Inversion:** A lower-priority thread is unable to access a resource due to a higher-priority thread holding onto it.
  - Formula: Priority Inversion = (Priority of higher-priority thread) - (Priority of lower-priority thread)

**Data Structures:**

- **Semaphore:** A variable that controls access to a shared resource.
- **Monitors:** A data structure that allows multiple threads to access shared resources safely.

**Synchronization Algorithms:**

- **Lock-Free Data Structures:** Data structures that do not use locks to synchronize access.
- **Busy Waiting:** A method where a thread waits for a condition to occur by continuously checking a flag.

**Important Theorems:**

- **Dekker's Token Ring Algorithm:** A protocol for resolving deadlocks in a distributed system.
- **Turnstile Algorithm:** A protocol for synchronizing access to a shared resource.

**Revision Tips:**

- Understand the basics of threading and synchronization.
- Familiarize yourself with common threading issues and data structures.
- Practice solving problems related to threading and synchronization.
