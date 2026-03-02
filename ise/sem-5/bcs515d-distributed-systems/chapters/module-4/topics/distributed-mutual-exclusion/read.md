# Distributed Mutual Exclusion

## Introduction

In distributed systems, **mutual exclusion** is a fundamental coordination problem where multiple processes must coordinate their access to shared resources to ensure that only one process can execute a critical section at any given time. Unlike in centralized systems where solutions like semaphores or mutex locks are straightforward, distributed mutual exclusion presents unique challenges due to the absence of shared memory and the inherent delays and uncertainties of message passing.

The need for distributed mutual exclusion arises in various scenarios, such as:

- Controlling access to a shared printer or storage device
- Managing updates to a distributed database
- Implementing a distributed lock service
- Coordinating access to network resources

## Key Properties of Distributed Mutual Exclusion Algorithms

A correct mutual exclusion algorithm in distributed systems must satisfy these properties:

1. **Safety**: At most one process may execute in the critical section (CS) at any time.
2. **Liveness**: Every request to enter the CS is eventually granted (no deadlock).
3. **Fairness**: Requests are granted in the order they were made (no starvation).

Additional desirable properties include:

- **Fault tolerance**: The algorithm should withstand process failures and network partitions.
- **Efficiency**: Minimize the number of messages and the time delay for entering the CS.

## Classification of Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion algorithms can be broadly classified into two categories:

1. **Token-based algorithms**: A unique token circulates in the system, and a process can enter the CS only when it possesses the token.
2. **Permission-based algorithms**: A process must obtain permission from other processes before entering the CS.

Permission-based algorithms can be further divided into:

- **Centralized algorithms**: A single coordinator grants permissions
- **Distributed algorithms**: Permissions are obtained from multiple processes

Let's examine the most important algorithms in detail.

## Centralized Algorithm

The centralized algorithm simulates a single-server solution in a distributed environment.

### How it works:

1. One process is designated as the coordinator (can be elected using an election algorithm)
2. When a process wants to enter the CS, it sends a REQUEST message to the coordinator
3. The coordinator maintains a queue of requests
4. If no process is in the CS, the coordinator sends a GRANT message
5. After exiting the CS, the process sends a RELEASE message to the coordinator
6. The coordinator then grants the next request in the queue

```
Processes: P1, P2, P3
Coordinator: C

P1 wants to enter CS:
P1 -> C: REQUEST
C -> P1: GRANT (if CS available)
P1 enters CS
P1 exits CS
P1 -> C: RELEASE
C grants next request
```

### Advantages:

- Simple to implement
- Guarantees fairness (FIFO ordering)
- Requires only 3 messages per CS entry (REQUEST, GRANT, RELEASE)

### Disadvantages:

- Single point of failure - if coordinator crashes, the system is blocked
- Performance bottleneck at the coordinator
- Not truly distributed

## Distributed Algorithm (Lamport's Algorithm)

Leslie Lamport proposed a fully distributed algorithm that uses logical clocks to timestamp requests and maintain ordering.

### How it works:

1. When a process wants to enter the CS, it sends a timestamped REQUEST message to all other processes
2. Each process maintains a queue of requests
3. Upon receiving a REQUEST, a process:
   - If it's not interested in the CS, sends a REPLY immediately
   - If it's interested but has a higher timestamp, sends a REPLY immediately
   - If it's interested and has a lower timestamp, defers the REPLY
4. A process enters the CS when it has received REPLY from all other processes
5. After exiting the CS, it sends a RELEASE message to all deferred processes

```
Processes: P1, P2, P3

P1 wants to enter CS (timestamp = 10):
P1 -> P2, P3: REQUEST(10)

P2 receives REQUEST(10):
If P2 not interested -> sends REPLY to P1
If P2 interested with timestamp=15 -> sends REPLY to P1
If P2 interested with timestamp=5 -> defers REPLY

P1 collects all REPLIES -> enters CS
P1 exits CS -> sends RELEASE to deferred processes
```

### Advantages:

- Fully distributed - no single point of failure
- Fairness guaranteed through timestamp ordering

### Disadvantages:

- Requires 3(n-1) messages per CS entry (where n is number of processes)
- All processes must participate in every decision
- Poor scalability as n increases

## Token Ring Algorithm

This algorithm uses a logical ring topology and a circulating token.

### How it works:

1. Processes are arranged in a logical ring: P1 → P2 → P3 → ... → Pn → P1
2. A token circulates around the ring
3. When a process receives the token:
   - If it wants to enter the CS, it keeps the token, enters the CS, and exits
   - After exiting, it passes the token to the next process
   - If it doesn't want to enter the CS, it immediately passes the token

```
Logical ring: P1 -> P2 -> P3 -> P1
Token circulates: P1 -> P2 -> P3 -> P1 -> ...

P2 has token but doesn't want CS -> passes to P3
P3 has token and wants CS -> keeps token, enters CS
P3 exits CS -> passes token to P1
```

### Advantages:

- Simple concept and implementation
- No starvation - every process gets the token eventually
- Only 1 message per CS entry in low contention

### Disadvantages:

- Token loss can halt the system (needs token regeneration)
- Delay in CS entry if token is far away in the ring
- Not fair in terms of request order - processes get access in ring order

## Maekawa's Voting Algorithm

Maekawa improved on the message complexity by having each process request permission only from a subset of processes (a "voting set" or "quorum").

### How it works:

1. Each process has a voting set (subset of processes)
2. Voting sets are constructed such that any two sets have non-empty intersection
3. To enter CS, a process sends REQUEST messages to all processes in its voting set
4. A process replies with a REPLY only if it hasn't already promised its vote to another process
5. After receiving all REPLY messages, the process enters the CS
6. After exiting, it sends RELEASE messages to all processes in its voting set

### Advantages:

- Reduces message complexity to O(√n) instead of O(n)
- More scalable than Lamport's algorithm

### Disadvantages:

- More complex to implement
- Potential for deadlock if not carefully designed

## Comparison of Algorithms

| Algorithm   | Message Complexity | Delay before CS entry | Problems                   |
| ----------- | ------------------ | --------------------- | -------------------------- |
| Centralized | 3                  | 2 message times       | Single point of failure    |
| Lamport's   | 3(n-1)             | 2 message times       | High message count         |
| Token Ring  | 1 to ∞             | 0 to n-1 steps        | Token loss, unfair         |
| Maekawa's   | O(√n)              | 2 message times       | Complex, deadlock possible |

## Performance Metrics

When evaluating mutual exclusion algorithms, we consider:

1. **Number of messages**: Total messages required per CS entry
2. **Synchronization delay**: Time between one process exiting the CS and the next entering
3. **Response time**: Time from when a process requests entry until it enters
4. **System throughput**: Rate at which processes can enter the CS

## Practical Considerations in Real Systems

In real-world distributed systems, mutual exclusion is often implemented using:

1. **Distributed lock services**: Like Apache ZooKeeper or Chubby
2. **Database locking mechanisms**: Pessimistic or optimistic locking
3. **Lease mechanisms**: Time-bound permissions for resource access
4. **Quorum systems**: As in distributed databases

## Exam Tips

1. **Understand the trade-offs**: Each algorithm makes different trade-offs between message complexity, fault tolerance, and fairness. Be prepared to justify why you would choose one algorithm over another for a specific scenario.

2. **Draw clear diagrams**: For Lamport's algorithm and Token Ring, practice drawing the message sequence charts. Label timestamps and message types clearly.

3. **Calculate message counts**: Be able to calculate the number of messages required for each algorithm given a specific number of processes.

4. **Compare and contrast**: Expect questions that ask you to compare two or more algorithms. Create a mental comparison table with key characteristics.

5. **Real-world applications**: Be prepared to discuss how these concepts apply to real systems like distributed databases or cloud services.

6. **Watch for trick questions**: Some questions might present scenarios where certain algorithms would fail (e.g., coordinator failure in centralized algorithm) - read carefully!
