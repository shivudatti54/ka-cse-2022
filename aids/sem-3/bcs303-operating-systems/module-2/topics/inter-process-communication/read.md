# Inter-Process Communication (IPC)


## Table of Contents

- [Inter-Process Communication (IPC)](#inter-process-communication-ipc)
- [Introduction](#introduction)
- [Independent vs Cooperating Processes](#independent-vs-cooperating-processes)
- [Reasons for Process Cooperation](#reasons-for-process-cooperation)
  - [1. Information Sharing](#1-information-sharing)
  - [2. Computation Speedup](#2-computation-speedup)
  - [3. Modularity](#3-modularity)
  - [4. Convenience](#4-convenience)
- [IPC Models](#ipc-models)
- [Shared Memory Model](#shared-memory-model)
  - [Producer-Consumer Problem](#producer-consumer-problem)
  - [Bounded Buffer vs Unbounded Buffer](#bounded-buffer-vs-unbounded-buffer)
  - [Bounded Buffer Implementation](#bounded-buffer-implementation)
- [Message Passing Model](#message-passing-model)
  - [Direct Communication](#direct-communication)
  - [Indirect Communication](#indirect-communication)
  - [Synchronization](#synchronization)
  - [Buffering](#buffering)
- [Comparison: Shared Memory vs Message Passing](#comparison-shared-memory-vs-message-passing)
- [Summary Table](#summary-table)
- [Exam Tips](#exam-tips)

## Introduction

Processes executing concurrently in the operating system may be either **independent** or **cooperating** processes. A process is independent if it cannot affect or be affected by other processes executing in the system. A process is cooperating if it can affect or be affected by other processes.

Any process that shares data with other processes is a cooperating process. There are several reasons for providing an environment that allows process cooperation.

## Independent vs Cooperating Processes

| Feature          | Independent Process                        | Cooperating Process                             |
| ---------------- | ------------------------------------------ | ----------------------------------------------- |
| Data sharing     | Does not share data with other processes   | Shares data with other processes                |
| Effect on others | Cannot affect or be affected by others     | Can affect or be affected by others             |
| Execution        | Deterministic -- depends only on input     | Non-deterministic -- depends on execution order |
| Reproducibility  | Always produces same result for same input | May produce different results                   |
| Synchronization  | Not required                               | Required                                        |

## Reasons for Process Cooperation

There are several reasons why processes need to cooperate:

### 1. Information Sharing

Since several users may be interested in the same piece of information (e.g., a shared file), we must provide an environment to allow concurrent access to such information.

### 2. Computation Speedup

If we want a particular task to run faster, we must break it into subtasks, each of which will be executing in parallel with the others. Such a speedup can be achieved only if the computer has multiple processing cores.

### 3. Modularity

We may want to construct the system in a modular fashion, dividing the system functions into separate processes or threads (e.g., microkernel architecture).

### 4. Convenience

Even an individual user may work on many tasks at the same time. For example, a user may be editing, listening to music, and compiling in parallel.

**Mnemonic: "I Can Manage Conveniently" -- Information sharing, Computation speedup, Modularity, Convenience**

## IPC Models

Cooperating processes require an **inter-process communication (IPC)** mechanism that will allow them to exchange data and information. There are two fundamental models of IPC:

1. **Shared Memory**
2. **Message Passing**

```
+------------------------------------------------------------------+
| IPC Models Comparison |
| |
| SHARED MEMORY MODEL MESSAGE PASSING MODEL |
| |
| +---------+ +---------+ +---------+ +---------+ |
| |Process A| |Process B| |Process A| |Process B| |
| | | | | | | | | |
| +----+----+ +----+----+ +----+----+ +----+----+ |
| | | | | |
| v v | | |
| +------------------+ v v |
| | Shared Memory | +------------------------+ |
| | Region | | Message Queue / | |
| | +------+ +-----+ | | Kernel Mailbox | |
| | |Buffer| |Data | | | | |
| | +------+ +-----+ | | send() receive() | |
| +------------------+ +------------------------+ |
| |
| Kernel Kernel |
| (sets up shared region) (manages messages) |
+------------------------------------------------------------------+
```

## Shared Memory Model

In the shared-memory model, a region of memory that is shared by cooperating processes is established. Processes can then exchange information by reading and writing data to the shared region.

**Key characteristics:**

- A shared-memory region resides in the address space of the process creating it
- Other processes must attach this shared-memory segment to their address space
- Normally, the OS prevents one process from accessing another's memory -- shared memory requires processes to agree to remove this restriction
- The processes are responsible for ensuring they are not writing to the same location simultaneously

### Producer-Consumer Problem

The producer-consumer problem is the classic paradigm for cooperating processes. A **producer** process produces information that is consumed by a **consumer** process.

```
Producer-Consumer Model:

 +----------+ +----------+
 | | write +---------+ read | |
 | Producer |----------->| Buffer |------>| Consumer |
 | | +---------+ | |
 +----------+ +----------+

 Producer produces items, places them in buffer.
 Consumer removes items from buffer and consumes them.
```

**Examples:**

- A compiler (producer) produces assembly code that is consumed by an assembler (consumer)
- A web server (producer) produces HTML content consumed by a browser (consumer)

### Bounded Buffer vs Unbounded Buffer

| Feature       | Unbounded Buffer                | Bounded Buffer               |
| ------------- | ------------------------------- | ---------------------------- |
| Size          | No practical limit on size      | Fixed size (N items)         |
| Producer      | Can always produce; never waits | Must wait if buffer is full  |
| Consumer      | Must wait if buffer is empty    | Must wait if buffer is empty |
| Practical use | Theoretical model               | Used in real implementations |

### Bounded Buffer Implementation

The bounded buffer can be implemented using a shared circular array with two pointers:

```
Bounded Buffer (size N = 5):

 +-----+-----+-----+-----+-----+
 | A | B | C | | |
 +-----+-----+-----+-----+-----+
 ^ ^
 | |
 out in
 (consumer (producer
 reads here) writes here)

 Buffer FULL when: (in + 1) % N == out
 Buffer EMPTY when: in == out
 Usable slots: N - 1 (one slot is always kept empty
 to distinguish full from empty)
```

**Shared variables:**

```
#define BUFFER_SIZE 10

typedef struct {
 . . .
} item;

item buffer[BUFFER_SIZE];
int in = 0; // next free position
int out = 0; // first full position
```

**Producer code:**

```
while (true) {
 /* produce an item in next_produced */
 while (((in + 1) % BUFFER_SIZE) == out)
 ; /* do nothing -- buffer is full */
 buffer[in] = next_produced;
 in = (in + 1) % BUFFER_SIZE;
}
```

**Consumer code:**

```
while (true) {
 while (in == out)
 ; /* do nothing -- buffer is empty */
 next_consumed = buffer[out];
 out = (out + 1) % BUFFER_SIZE;
 /* consume the item in next_consumed */
}
```

**Limitation:** This solution allows at most BUFFER_SIZE - 1 items in the buffer at the same time. One slot is wasted to distinguish between a full and an empty buffer.

## Message Passing Model

Message passing provides a mechanism for processes to communicate and synchronize their actions **without sharing the same address space**. It is particularly useful in a distributed environment where communicating processes may reside on different computers connected by a network.

A message-passing facility provides at least two operations:

- **send(message)**
- **receive(message)**

```
Message Passing Operations:

 Process P Process Q
 +--------+ +--------+
 | | send(msg) | |
 | P |------------------>| Q |
 | | | |
 | | receive(msg) | |
 | |<------------------| |
 +--------+ +--------+
```

### Direct Communication

Each process must explicitly name the recipient or sender:

- **send(P, message)** -- send a message to process P
- **receive(Q, message)** -- receive a message from process Q

**Properties of direct communication:**

- A link is established automatically between every pair of processes that want to communicate
- A link is associated with exactly two processes
- Between each pair of processes, there exists exactly one link

**Disadvantage:** Hard-coding process identifiers. If the identifier of a process changes, all references to it must be found and modified (limited modularity).

### Indirect Communication

Messages are sent to and received from **mailboxes** (also called ports). Each mailbox has a unique identification.

- **send(A, message)** -- send a message to mailbox A
- **receive(A, message)** -- receive a message from mailbox A

```
Indirect Communication via Mailbox:

 Process P1 ---+ +--- Process P3
 | +-----------+ |
 +--->| Mailbox A |---+
 +--->| |---+
 Process P2 ---+ +-----------+ +--- Process P4
```

**Properties of indirect communication:**

- A link is established between processes only if they share a mailbox
- A link may be associated with more than two processes
- Between each pair of processes, several different links may exist (via different mailboxes)

| Feature        | Direct Communication            | Indirect Communication                  |
| -------------- | ------------------------------- | --------------------------------------- |
| Addressing     | Explicit process naming         | Via mailboxes/ports                     |
| Link creation  | Automatic between process pairs | Only if processes share a mailbox       |
| Processes/link | Exactly two                     | Two or more                             |
| Links/pair     | Exactly one                     | Multiple possible (different mailboxes) |
| Modularity     | Low (hard-coded process names)  | High (processes only know mailbox IDs)  |

### Synchronization

Message passing may be either **blocking** or **non-blocking** (also known as synchronous and asynchronous):

| Type                     | Behavior                                                   |
| ------------------------ | ---------------------------------------------------------- |
| **Blocking send**        | Sender blocks until the message is received                |
| **Non-blocking send**    | Sender sends the message and continues (resumes operation) |
| **Blocking receive**     | Receiver blocks until a message is available               |
| **Non-blocking receive** | Receiver retrieves either a valid message or a null        |

**Rendezvous**: When both send and receive are blocking, we have a rendezvous between the sender and the receiver. The solution to the producer-consumer problem becomes trivial with rendezvous.

```
Synchronization Types:

 Blocking (Synchronous):
 P: send(msg) ----BLOCKED----> Q: receive(msg)
 (waits) (waits until message arrives)

 Non-blocking (Asynchronous):
 P: send(msg) ---> continues Q: receive(msg)
 (does not wait) (returns null if no msg)
```

### Buffering

Messages exchanged by communicating processes reside in a temporary queue. Such queues can be implemented in three ways:

| Buffer Capacity        | Behavior                                                                            |
| ---------------------- | ----------------------------------------------------------------------------------- |
| **Zero capacity**      | Queue has maximum length 0. Sender must block until receiver receives (rendezvous). |
| **Bounded capacity**   | Queue has finite length n. Sender blocks only when queue is full.                   |
| **Unbounded capacity** | Queue has potentially infinite length. Sender never blocks.                         |

## Comparison: Shared Memory vs Message Passing

| Aspect              | Shared Memory                    | Message Passing                          |
| ------------------- | -------------------------------- | ---------------------------------------- |
| Speed               | Faster (memory access speeds)    | Slower (system calls for each message)   |
| System calls        | Only to establish shared region  | Required for every message exchange      |
| Synchronization     | Must be handled by programmer    | Handled by OS (implicit in send/receive) |
| Ease of programming | More difficult (race conditions) | Easier (no conflict management needed)   |
| Distributed systems | Difficult to implement           | Well-suited                              |
| Data volume         | Better for large amounts of data | Better for small amounts of data         |
| Kernel involvement  | Minimal after setup              | Active for every communication           |
| Example             | POSIX shared memory              | Pipes, sockets, message queues           |

```
Performance Comparison:

 Shared Memory:
 Setup: [Kernel call to create region] (one-time cost)
 Transfer: [Direct memory read/write] (very fast, no kernel)

 Message Passing:
 Setup: [Minimal]
 Transfer: [Kernel call] --> [Copy to kernel] --> [Kernel call]
 --> [Copy to receiver] (slower per message)
```

## Summary Table

| Concept                | Key Points                                                        |
| ---------------------- | ----------------------------------------------------------------- |
| Independent process    | Cannot affect or be affected by others                            |
| Cooperating process    | Can affect or be affected by other processes                      |
| Cooperation reasons    | Information sharing, computation speedup, modularity, convenience |
| Shared memory          | Processes read/write a common memory region                       |
| Message passing        | Processes use send/receive operations                             |
| Producer-consumer      | Classic IPC paradigm; bounded and unbounded buffer variants       |
| Direct communication   | Processes name each other explicitly                              |
| Indirect communication | Messages sent/received via mailboxes                              |
| Blocking (synchronous) | Sender/receiver waits until operation completes                   |
| Non-blocking (async)   | Sender/receiver continues without waiting                         |

## Exam Tips

1. **Diagram questions are very common**: Be ready to draw shared memory and message passing models with labeled processes, kernel, and communication paths
2. **Producer-consumer bounded buffer code** is frequently asked -- memorize the shared variables (in, out, buffer) and the while-loop conditions
3. **Know the buffer full/empty conditions**: Full = (in + 1) % N == out; Empty = in == out
4. **Direct vs Indirect communication** comparison is a common 5-mark question -- know properties of links for each
5. **Four reasons for cooperation** (ICMC): Information sharing, Computation speedup, Modularity, Convenience
6. **Blocking vs Non-blocking**: Memorize all four combinations; know that both-blocking = rendezvous
7. **Shared memory vs Message passing** comparison table is a guaranteed exam question -- memorize at least 5 differences
8. **Buffer capacity** (zero, bounded, unbounded) -- know when the sender blocks for each type
9. **N-1 limitation**: Bounded buffer with array of size N can hold at most N-1 items (one slot wasted to distinguish full from empty)
10. **Remember**: Shared memory is faster for large data; message passing is better for distributed systems
