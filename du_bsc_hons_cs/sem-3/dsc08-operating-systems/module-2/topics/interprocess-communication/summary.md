# Interprocess Communication (IPC)

## Introduction
Interprocess Communication (IPC) is a mechanism that allows processes to communicate, share data, and synchronize their execution. In modern operating systems, processes run in isolated address spaces, making IPC essential for building cooperative systems and enabling parallelism.

## Need for IPC
- **Resource Sharing**: Processes need to share resources like files, memory, and devices
- **Data Exchange**: Applications require exchange of data between cooperating processes
- **Process Synchronization**: Coordination between concurrent processes
- **Modular Design**: Enables distributed and client-server architectures

## Types of IPC Mechanisms

### 1. Shared Memory
- Fastest form of IPC
- Multiple processes access a common memory region
- **Types**: Producer-Consumer problem, Bounded Buffer
- Requires synchronization (semaphores/mutexes)

### 2. Message Passing
- Processes communicate via messages through a communication channel
- **Direct Communication**: Specific sender-receiver (e.g., `send(P, message)`)
- **Indirect Communication**: Through mailboxes/ports
- Implemented in Unix (pipes, message queues) and Windows (mailslots)

### 3. Pipes
- **Unnamed Pipes**: Parent-child communication, unidirectional
- **Named Pipes (FIFOs)**: Unrelated processes can communicate, bidirectional
- Example: `pipe()` system call in Unix

### 4. Signals
- Asynchronous notifications sent to processes
- Used for exception handling and process control
- Examples: `SIGKILL`, `SIGTERM`, `SIGALRM` in Unix

### 5. Semaphores
- Integer-based synchronization primitive
- **Operations**: `wait()` (P) and `signal()` (V)
- Solves critical section and race condition problems

### 6. Mutex (Mutual Exclusion)
- Lock-based synchronization for shared resources
- Provides exclusive access to critical sections

### 7. Message Queues
- Linked list of messages stored in kernel memory
- Supports priority-based messaging
- Example: POSIX message queues

### 8. Sockets
- Used for inter-process communication across network
- Supports both local and network communication

## Comparison Table

| Mechanism | Communication Type | Synchronization | Speed |
|-----------|-------------------|------------------|-------|
| Shared Memory | Bidirectional | Required | Fastest |
| Message Passing | Unidirectional/Bidirectional | Built-in | Moderate |
| Pipes | Unidirectional | Required | Fast |
| Sockets | Bidirectional | Required | Moderate |

## Synchronization Issues
- **Race Conditions**: When multiple processes access shared data concurrently
- **Deadlock**: Circular waiting for resources
- **Starvation**: Process never gets required resources

## Conclusion
IPC is fundamental to modern operating systems, enabling process cooperation and resource sharing. Understanding IPC mechanisms—shared memory, message passing, pipes, semaphores—is crucial for designing efficient concurrent applications. The choice of IPC method depends on data volume, synchronization needs, and communication scope (local vs. network).

*Reference: Delhi University BSc (H) CS, NEP 2024 UGCF Syllabus – Operating Systems Unit III*