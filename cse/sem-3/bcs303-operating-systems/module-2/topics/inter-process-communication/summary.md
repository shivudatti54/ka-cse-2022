# Inter Process Communication - Summary

## Key Definitions

- **Inter Process Communication (IPC)**: A mechanism that allows processes to communicate with each other and share data or synchronize their execution.

- **Message Passing**: An IPC mechanism where processes exchange messages through a communication channel, with the operating system handling data transfer between address spaces.

- **Shared Memory**: An IPC mechanism where processes share a common memory region that they can read and write directly, requiring explicit synchronization.

- **Pipe**: A unidirectional, anonymous communication channel created by the operating system for communication between related processes.

- **FIFO (Named Pipe)**: A pipe identified by a filesystem pathname, allowing communication between unrelated processes.

- **Socket**: A versatile IPC endpoint that supports communication between processes on the same machine or across a network.

- **Semaphore**: A synchronization primitive that controls access to shared resources through atomic increment and decrement operations.

## Important Formulas

- **Shared Memory Performance**: Communication time is independent of data size once the segment is attached (O(1) overhead).

- **Message Passing Overhead**: Communication time increases with message size due to data copying between address spaces (O(n) where n is message size).

- **Pipe Buffer Capacity**: Typically 64 KB in modern Linux systems; `PIPE_BUF` defines atomic write limit (usually 4096 bytes).

## Key Points

1. IPC is essential for process collaboration, enabling modular design, resource sharing, and concurrent operation in multi-process applications.

2. Message passing provides a clean interface with implicit synchronization but incurs copying overhead; shared memory offers superior performance but requires explicit synchronization.

3. Direct communication requires processes to know each other's identities, while indirect communication uses mailboxes that can be shared by multiple processes.

4. Shared memory requires careful synchronization using semaphores, mutexes, or monitors to prevent race conditions and ensure data consistency.

5. Pipes are unidirectional and anonymous (exist only for the lifetime of related processes), while FIFOs persist in the filesystem with pathname identifiers.

6. Sockets provide versatile communication supporting both local (UNIX domain) and network (TCP/UDP) communication with consistent programming interfaces.

7. Blocking operations cause processes to wait for completion, while non-blocking operations return immediately, affecting system behavior and deadlock prevention strategies.

8. The choice of IPC mechanism depends on data volume, required speed, process relationships, and whether processes run on the same machine.

## Common Mistakes

1. **Forgetting synchronization**: Creating shared memory segments without implementing proper synchronization, leading to race conditions and data corruption.

2. **Confusing pipe direction**: Attempting to read from the write end or write to the read end of a pipe, which causes errors.

3. **Memory attachment errors**: Failing to properly attach or detach shared memory segments, leading to memory leaks or access violations.

4. **Blocking deadlock**: Using blocking send/receive operations without timeout mechanisms can cause permanent blocking when processes fail to respond.

5. **Neglecting buffer limits**: Writing large messages to pipes or message queues without checking buffer capacity, causing blocking or failure.

6. **Improper semaphore initialization**: Failing to initialize semaphores or using incorrect initial values leads to unpredictable synchronization behavior.