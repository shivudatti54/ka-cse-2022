# Distributed Mutual Exclusion

## Introduction

In distributed systems, multiple processes run on different machines connected through a network. These processes often need to access shared resources such as files, printers, databases, or memory segments. When multiple processes attempt to simultaneously access and modify a shared resource, it can lead to data inconsistency and corruption. Mutual exclusion (mutex) is a fundamental concept that ensures only one process can access the critical section (the portion of code that accesses shared resources) at any given time.

While mutual exclusion is straightforward in centralized systems using techniques like semaphores, monitors, or locks, implementing mutual exclusion in distributed systems presents unique challenges. There is no shared memory, no global clock, and communication between processes is unreliable and subject to unpredictable delays. Distributed mutual exclusion algorithms must coordinate among multiple nodes that are geographically separated, making the problem significantly more complex than its centralized counterpart.

The study of distributed mutual exclusion is crucial for modern computing applications including distributed databases, cloud computing platforms, distributed file systems, and blockchain technologies. Understanding these algorithms helps engineers design systems that maintain data consistency while maximizing concurrency and performance.

## Key Concepts

### Requirements of Distributed Mutual Exclusion

A correct distributed mutual exclusion algorithm must satisfy three fundamental properties:

1. **Safety (Mutual Exclusion)**: At most one process can execute in the critical section at any time. This is the primary requirement that prevents race conditions and data corruption.

2. **Liveness (No Deadlock)**: Every request for critical section entry must eventually be granted, provided the system is stable. Processes should not wait indefinitely if the system is functioning correctly.

3. **Fairness (No Starvation)**: Requests are served in the order they were made (FIFO order). Every process gets a fair chance to enter the critical section, preventing indefinite postponement.

Additional properties considered in practice include:

- **Message Complexity**: The number of messages exchanged per critical section entry
- **Synchronization Delay**: The time between a process requesting entry and actually entering the critical section
- **Fault Tolerance**: The algorithm's ability to handle process or network failures

### Classification of Algorithms

Distributed mutual exclusion algorithms can be broadly classified into two categories:

**Token-Based Algorithms**: A special message called a "token" circulates among processes. Only the process holding the token can enter the critical section. Examples include Token Ring and Token Passing algorithms. These algorithms have deterministic message complexity but can suffer from token loss or duplication problems.

**Tokenless (Non-Token-Based) Algorithms**: These algorithms use message passing without a special token. Each process communicates with others to determine who should enter the critical section next. Examples include Lamport's Algorithm and Ricart-Agrawala Algorithm. These are generally more complex but avoid token-related issues.

### Lamport's Distributed Mutual Exclusion Algorithm

Leslie Lamport devised a groundbreaking algorithm that uses a logical clock to establish a total ordering of events in a distributed system. The algorithm works as follows:

1. When a process wants to enter the critical section, it creates a timestamp using its logical clock and sends a REQUEST message to all other processes.

2. Each process maintains a queue of requests ordered by timestamps. Upon receiving a REQUEST message, a process sends a REPLY message to the requester and adds the request to its queue.

3. A process can enter the critical section when it has received REPLY messages from all other processes AND its request is at the front of its queue.

4. When exiting the critical section, the process sends a RELEASE message to all other processes, which then remove the request from their queues.

This algorithm requires (N-1) messages for request and (N-1) messages for reply, plus RELEASE messages, resulting in 3(N-1) messages per critical section entry.

### Ricart-Agrawala Algorithm

The Ricart-Agrawala algorithm is an improvement over Lamport's algorithm that eliminates the need for RELEASE messages. It works as follows:

1. When a process wants to enter the critical section, it sends a REQUEST message with its timestamp to all other processes.

2. Upon receiving a REQUEST message, a process immediately sends a REPLY message if it is not interested in the critical section or if its request timestamp is later than the incoming request. Otherwise, it defers the REPLY message (puts it in a queue).

3. A process enters the critical section when it has received REPLY messages from all other processes.

4. When a process exits the critical section, it sends REPLY messages to all deferred requests in its queue.

This algorithm requires 2(N-1) messages per critical section entry - (N-1) REQUEST messages and (N-1) REPLY messages.

### Maekawa's Voting Algorithm

Maekawa's algorithm reduces message complexity by using a voting mechanism. Each process has a quota of votes from other processes and needs only a majority of votes to enter the critical section. This reduces message complexity to approximately √N messages per critical section entry. However, the algorithm is more complex and requires careful management of vote quotas to avoid deadlock.

### Token Ring Algorithm

In the Token Ring approach, processes are arranged in a logical ring. A special token circulates around the ring. A process can enter the critical section only when it possesses the token. After exiting, it passes the token to the next process in the ring. This algorithm is simple but has variable message complexity depending on token position.

## Examples

### Example 1: Ricart-Agrawala Algorithm Execution

Consider three processes P1, P2, and P3 in a distributed system. The logical clock values are shown in parentheses.

**Scenario**: P2 requests critical section at time T=10, while P1 requests at T=15.

**Step-by-step execution**:

1. P2 wants to enter critical section. It sends REQUEST(10) to P1 and P3.
2. P1 wants to enter critical section. It sends REQUEST(15) to P2 and P3.
3. P3 receives REQUEST(10) from P2 first. Since P3 is not interested, it immediately sends REPLY to P2.
4. P3 receives REQUEST(15) from P1. Since 15 > 10, P3 sends REPLY to P1.
5. P2 receives REQUEST(15) from P1. Since 10 < 15, P2 defers the REPLY to P1 (queues it).
6. P1 receives REQUEST(10) from P2. Since 15 > 10, P1 sends REPLY to P2.
7. P2 has received REPLY from P1 and P3. P2 enters critical section.
8. After exiting, P2 sends REPLY to the deferred request from P1.
9. P1 receives REPLY from P2 and P3. P1 enters critical section.

**Result**: The algorithm ensures P2 enters before P1 based on timestamps, satisfying mutual exclusion and FIFO ordering.

### Example 2: Token Ring Scenario

Consider four processes arranged in a ring: P1 → P2 → P3 → P4 → P1.

**Scenario**: Token is currently at P1. P3 and P4 both want to enter critical section.

**Execution**:

1. Token arrives at P1. P1 doesn't need critical section, passes to P2.
2. Token arrives at P2. P2 doesn't need it, passes to P3.
3. Token arrives at P3. P3 wants to enter, captures token, enters critical section.
4. After exiting, P3 passes token to P4.
5. Token arrives at P4. P4 wants to enter, captures token, enters critical section.
6. After exiting, P4 passes token to P1, completing the cycle.

**Message count**: Token passes through at most N-1 processes before reaching the requester.

### Example 3: Message Complexity Comparison

For a system with N=10 processes, compare message complexity:

**Lamport's Algorithm**: 3(N-1) = 3 × 9 = 27 messages per CS entry

**Ricart-Agrawala Algorithm**: 2(N-1) = 2 × 9 = 18 messages per CS entry

**Maekawa's Algorithm**: Approximately 3√N ≈ 3 × 3.16 ≈ 9.5 messages per CS entry

**Token Ring**: 0 to N-1 messages (variable)

This example demonstrates the trade-off between complexity and message overhead in choosing an algorithm.

## Exam Tips

1. **Remember the three properties**: Safety, Liveness, and Fairness are essential for any distributed mutual exclusion algorithm. Know them thoroughly.

2. **Key difference between token-based and tokenless**: Token-based algorithms use circulating tokens while tokenless algorithms rely on message passing and timestamps.

3. **Ricart-Agrawala message count**: Always remember it requires exactly 2(N-1) messages - this is a frequently asked question in exams.

4. **Lamport vs Ricart-Agrawala**: Lamport needs RELEASE messages (3(N-1) messages) while Ricart-Agrawala doesn't (2(N-1) messages).

5. **Logical Clocks**: Understand that Lamport's algorithm uses logical clocks to create total ordering of events, which is crucial for determining request priority.

6. **Deadlock prevention**: In Ricart-Agrawala, deadlock is prevented by comparing timestamps - the process with the earlier timestamp has priority.

7. **Maekawa's advantage**: It reduces message complexity to O(√N) but requires a majority quorum for entry, making it more complex to implement.

8. **Token Ring drawback**: If the token is lost (due to network issues) or the process holding it crashes, the system can become deadlocked - this is a significant limitation.

9. **Synchronization delay**: This is the time between a process requesting entry and entering the critical section. In Ricart-Agrawala, this is 2T (where T is the maximum message delay).

10. **Practical considerations**: In real-world systems, factors like network latency, process failures, and message loss significantly impact algorithm selection.
