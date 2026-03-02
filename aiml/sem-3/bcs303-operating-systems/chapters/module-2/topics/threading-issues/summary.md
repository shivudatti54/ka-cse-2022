# Threading Issues

### Overview

- Threading is a technique used in operating systems to improve system efficiency
- Issues with threading can lead to performance degradation and system crashes

### Types of Threading Issues

- **Deadlock**: A situation where two or more threads are blocked indefinitely, each waiting for the other to release a resource
- **Livelock**: A situation where two or more threads are constantly taking turns, but never make progress
- **Starvation**: A situation where one or more threads are unable to access a shared resource due to other threads holding onto it for an extended period
- **Priority Inversion**: A situation where a lower-priority thread is able to bypass higher-priority threads due to the operating system's scheduling algorithm

### Thread Synchronization Issues

- **Monitors**: Data structures that allow multiple threads to access and modify shared resources in a thread-safe manner
- **Semaphores**: Variables that control the access to a shared resource, allowing threads to wait until the resource is available
- **Monitors and Semaphores**: Theorems:
  - **Monotonic Property**: A monitor's state is consistent with its previous state
  - **Safety Property**: A monitor's state is consistent with the state of all other monitors
- **Atomicity**: A sequence of operations that are performed as a single, indivisible unit

### Thread Communication Issues

- **Synchronization**: Ensuring that multiple threads access shared resources in a thread-safe manner
- **Deadlock Avoidance Techniques**: Using techniques such as:
  - **Avoiding Nested Locks**
  - **Using Timers**
  - **Using Lock Ordering**
- **Deadlock Detection and Prevention Techniques**: Using techniques such as:
  - **Deadlock Detection Algorithms**
  - **Deadlock Prevention Algorithms**

### Important Formulas and Definitions

- **Lamport's Bakery Algorithm**: A synchronization algorithm for distributing tickets to threads
- **The Busy Wait**: A technique where a thread waits for a resource to become available without using locks or other synchronization primitives
- **Condition Variables**: Variables that allow threads to wait for a specific condition to occur before proceeding

### Key Theorems and Lemmas

- **Hartmanis' Theorem**: A theorem that states that a synchronization algorithm is correct if and only if it is based on a correct synchronization algorithm
- **Lamport's Theorem**: A theorem that states that a synchronization algorithm is correct if and only if it is based on a correct synchronization algorithm and is deadlock-free
