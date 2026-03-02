# Interprocess Communication (IPC)

## Introduction to IPC
Interprocess Communication (IPC) refers to the mechanisms and techniques that allow processes to exchange data and coordinate their activities. In modern operating systems, multiple processes often need to work together to accomplish complex tasks, making IPC a fundamental aspect of process management.

Processes can be either:
- **Independent processes** - Cannot affect or be affected by other processes
- **Cooperating processes** - Can affect or be affected by other processes

IPC enables process cooperation, which provides several benefits:
- Information sharing between applications
- Computational speedup through parallel processing
- Modularity in system design
- Convenience for users performing multiple tasks

## Fundamental IPC Models

### Shared Memory Model
In the shared memory model, processes communicate by reading and writing to a common region of memory that multiple processes can access.

```
Process A          Shared Memory          Process B
   |                    |                    |
   |-- Write Data ----->|                    |
   |                    |                    |
   |                    |<--- Read Data -----|
   |                    |                    |
```

**Characteristics:**
- Faster than message passing as it avoids system calls after setup
- Requires synchronization mechanisms to prevent race conditions
- Typically used for high-performance applications

### Message Passing Model
In the message passing model, processes communicate by sending and receiving messages through the operating system.

```
Process A          OS/Kernel          Process B
   |                 |                 |
   |--- Send Msg --->|                 |
   |                 |--- Deliver ----->|
   |                 |                 |
   |<-- Reply -------|<--- Send -------|
   |                 |                 |
```

**Characteristics:**
- Slower than shared memory due to system call overhead
- Easier to implement correctly
- Built-in synchronization through blocking operations
- Better for distributed systems

## IPC Techniques and Mechanisms

### Pipes
Pipes provide a unidirectional communication channel between processes. They are typically used for communication between parent and child processes.

**Types of Pipes:**
1. **Ordinary Pipes** - Unidirectional, cannot be accessed from outside the process that created it
2. **Named Pipes (FIFOs)** - Bidirectional, can be accessed by unrelated processes

```
$ ls | grep ".txt" | wc -l
```
In this command line example, three processes communicate through pipes.

### Message Queues
Message queues allow processes to exchange messages through a linked list stored in kernel memory.

**Characteristics:**
- Messages are stored as linked lists
- Each message has a type field for selective receiving
- Persistent until read and explicitly deleted
- Synchronization through blocking operations

### Shared Memory
Shared memory allows multiple processes to map the same memory segment into their address space.

**Implementation Steps:**
1. Create shared memory segment
2. Attach segment to process address space
3. Access the shared memory
4. Detach when done
5. Destroy segment (optional)

### Sockets
Sockets provide communication between processes that may be on different machines. They use a standard interface for network communication.

**Types:**
- Stream sockets (TCP) - Connection-oriented, reliable
- Datagram sockets (UDP) - Connectionless, unreliable

### Signals
Signals are software interrupts used to notify processes of events. They provide a basic form of IPC for simple notifications.

**Common signals:**
- SIGINT (Interrupt)
- SIGKILL (Kill process)
- SIGUSR1/2 (User-defined)

## Synchronization in IPC

Proper synchronization is crucial for IPC to prevent race conditions and ensure data consistency.

### Critical Section Problem
The critical section is a code segment that accesses shared resources and must not be executed by more than one process simultaneously.

**Requirements:**
1. Mutual Exclusion - Only one process in critical section at a time
2. Progress - Processes not in critical section shouldn't block others
3. Bounded Waiting - No process should wait indefinitely

### Semaphores
Semaphores are synchronization tools that use atomic operations to control access to shared resources.

```c
// Pseudo-code for semaphore operations
wait(S) {
    while (S <= 0); // Busy wait
    S--;
}

signal(S) {
    S++;
}
```

**Types:**
- Counting semaphores - Can have any integer value
- Binary semaphores - Can only be 0 or 1 (mutex locks)

### Mutex Locks
Mutex (Mutual Exclusion) locks provide a simple synchronization mechanism where a process must acquire the lock before entering its critical section and release it afterward.

## Classical IPC Problems

### Producer-Consumer Problem
The producer produces data that the consumer uses. They share a bounded buffer.

```
Producer Process --> [Bounded Buffer] --> Consumer Process
```

**Solution approaches:**
- Using semaphores for empty and full counts
- Implementing circular buffer

### Reader-Writer Problem
Multiple readers can read simultaneously, but writers need exclusive access.

**Variations:**
- First reader-writers problem - No reader kept waiting unless writer has permission
- Second reader-writers problem - Once writer is ready, no new readers may start

### Dining Philosophers Problem
Five philosophers sit around a table with five chopsticks. Each needs two chopsticks to eat.

```
    P0
   /   \
 C5     C1
  |     |
 P4     P1
   \   /
 C4     C2
    P3
```

## IPC in Modern Systems

### Remote Procedure Call (RPC)
RPC allows a process to execute procedures on remote systems as if they were local.

**Stages:**
1. Client stub marshals parameters
2. Message sent to server
3. Server stub unmarshals parameters
4. Procedure executed
5. Result returned to client

### Distributed Shared Memory (DSM)
DSM creates an illusion of shared memory across networked computers.

## Performance Comparison

| IPC Mechanism     | Speed     | Complexity | Synchronization | Use Case                      |
|-------------------|-----------|------------|-----------------|-------------------------------|
| Shared Memory     | Very Fast | High       | Manual          | High-performance applications |
| Message Queues    | Medium    | Medium     | Built-in        | Structured communication      |
| Pipes            | Medium    | Low        | Built-in        | Command-line tools            |
| Sockets          | Slow      | High       | Manual          | Network communication         |
| Signals          | Fast      | Low        | Limited         | Simple notifications          |

## Implementation Examples

### POSIX Shared Memory
```c
// Creating shared memory
int shm_fd = shm_open("/my_shm", O_CREAT | O_RDWR, 0666);
ftruncate(shm_fd, SIZE);
void *ptr = mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
```

### POSIX Message Queue
```c
// Creating message queue
mqd_t mq = mq_open("/my_queue", O_CREAT | O_RDWR, 0666, NULL);
mq_send(mq, "Hello", 6, 0);
mq_receive(mq, buffer, MAX_MSG_SIZE, NULL);
```

## Exam Tips
1. **Understand the trade-offs** between shared memory and message passing - shared memory is faster but requires explicit synchronization
2. **Remember the three requirements** for solving the critical section problem: mutual exclusion, progress, and bounded waiting
3. **Practice solving classical problems** like producer-consumer and dining philosophers using semaphores
4. **Know the differences** between various IPC mechanisms and when to use each
5. **Understand synchronization primitives** thoroughly, especially semaphores and mutex locks
6. **Be prepared to draw diagrams** illustrating how processes communicate using different IPC methods