# Concurrency Control in Distributed Transactions

## Introduction

Concurrency control in distributed transactions is a critical aspect of modern database management systems that operate across multiple network nodes. In a distributed database system, data is stored across different geographical locations, and multiple transactions may access and modify this data simultaneously. Without proper concurrency control mechanisms, the fundamental properties of transactions—atomicity, consistency, isolation, and durability (ACID)—cannot be guaranteed.

The challenge in distributed environments is significantly more complex than in centralized systems due to several factors: communication delays between nodes, lack of global clock, independent failures of nodes, and the need to maintain consistency across multiple databases. This topic is essential for CSE students as it forms the backbone of modern enterprise applications, cloud databases, and distributed systems that power today's digital infrastructure.

Understanding concurrency control in distributed transactions is crucial for designing robust systems that can handle high concurrency while maintaining data integrity. The techniques discussed here are implemented in real-world systems like distributed databases (Google Spanner, Amazon Aurora), blockchain systems, and enterprise resource planning systems.

## Key Concepts

### Distributed Transactions

A distributed transaction involves multiple nodes in a distributed system, where a transaction may need to access data from several different databases located on different servers. The transaction must ensure that either all operations succeed across all nodes or none of them succeed. This is achieved through protocols like the Two-Phase Commit (2PC) and Three-Phase Commit (3PC).

### ACID Properties in Distributed Context

1. **Atomicity**: All operations across all nodes must complete successfully, or none should be applied. This requires coordination between all participating nodes.
2. **Consistency**: The transaction must transform the database from one consistent state to another.
3. **Isolation**: Concurrent transactions must appear to execute serially, even when running in parallel across different nodes.
4. **Durability**: Once a transaction commits, its effects must persist even if system failures occur.

### Lock-Based Concurrency Control

In distributed systems, locks can be managed centrally, hierarchically, or in a distributed manner:

**Centralized Lock Management**: A single lock manager handles all lock requests across the system. Simple to implement but creates a single point of failure and performance bottleneck.

**Primary Copy Locking**: One replica of each data item is designated as the primary copy, and locks are managed at the node containing the primary copy. This reduces bottlenecks but introduces delays when the primary copy is unavailable.

**Distributed Lock Management**: Lock managers exist at each node, and they coordinate to manage locks for data distributed across the system. This provides better scalability and fault tolerance but adds complexity.

### Timestamp-Based Protocols

Timestamp-based protocols use transaction timestamps to order transactions and ensure serializability:

**Thomas' Write Rule**: A variation of timestamp ordering that allows certain write operations to be skipped if they would be overwritten anyway, improving concurrency.

**Multi-Version Timestamp Ordering (MVTO)**: Maintains multiple versions of data items, allowing read operations to access older versions without blocking write operations.

### Distributed Deadlock Detection

Deadlocks occur when transactions form a circular wait dependency. In distributed systems, deadlock detection is more complex:

**Centralized Detection**: A single coordinator maintains the global wait-for graph. Simple but creates a bottleneck and single point of failure.

**Hierarchical Detection**: Nodes are organized in a hierarchy, with each level handling deadlock detection within its domain.

**Distributed Detection**: Multiple nodes participate in detecting deadlocks, exchanging information about wait-for graphs. The most commonly used approach is the **Chandy-Misra-Haas algorithm**, which uses a diffusing computation technique.

### Two-Phase Commit Protocol (2PC)

The Two-Phase Commit ensures atomic commitment of distributed transactions:

**Phase 1 (Prepare Phase)**:

- The coordinator sends a PREPARE message to all participants
- Each participant locks the resources and writes a prepare log
- Participants vote YES if ready to commit, NO otherwise

**Phase 2 (Commit Phase)**:

- If all participants vote YES, coordinator sends COMMIT
- If any votes NO, coordinator sends ROLLBACK
- Participants apply the decision and release locks

**Limitations**: Blocking problem where participants wait indefinitely if coordinator fails.

### Three-Phase Commit Protocol (3PC)

An extension of 2PC that eliminates blocking by adding an extra phase:

**Phase 1 (CanCommit)**: Coordinator checks if all participants can commit
**Phase 2 (PreCommit)**: If all can commit, coordinator sends pre-commit
**Phase 3 (DoCommit)**: Actual commit or abort

## Examples

### Example 1: Distributed Lock Acquisition

Consider a distributed system with three nodes: N1, N2, and N3. Transaction T1 running on N1 needs to read data items X (at N1) and Y (at N2).

**Step-by-step execution**:

1. T1 requests lock on X from lock manager at N1 → Granted (local lock)
2. T1 requests lock on Y from lock manager at N2 → N2's lock manager communicates with N1's manager
3. Lock on Y granted at N2
4. T1 can now read both X and Y

If Transaction T2 at N3 needs Y (at N2) and Z (at N3), and tries to acquire locks after T1:

- T2 can acquire lock on Z at N3 immediately
- T2 will be blocked at N2 waiting for Y until T1 releases it

### Example 2: Two-Phase Commit Scenario

A distributed transaction T transfers ₹5000 from Account A (Node 1) to Account B (Node 2):

**Phase 1 - Prepare**:

- Coordinator sends PREPARE to Node 1 and Node 2
- Node 1: Debits ₹5000, writes prepare log, votes YES
- Node 2: Credits ₹5000, writes prepare log, votes YES

**Phase 2 - Commit**:

- Coordinator receives YES from both nodes
- Coordinator sends COMMIT to both nodes
- Both nodes make changes permanent, release locks
- Transaction completes successfully

**Failure scenario**: If Node 2 had voted NO (insufficient balance):

- Coordinator sends ROLLBACK to both nodes
- Both nodes undo the debit/credit operations
- Transaction aborts atomically

### Example 3: Distributed Deadlock Detection

Using the Chandy-Misra-Haas algorithm:

- Transaction T1 at Node 1 holds lock on X, waits for Y (held by T2 at Node 2)
- Transaction T2 at Node 2 holds lock on Y, waits for Z (held by T3 at Node 3)
- Transaction T3 at Node 3 holds lock on Z, waits for X (held by T1 at Node 1)

**Detection process**:

1. T1 sends probe to T2 via network
2. T2 forwards probe to T3
3. T3 forwards probe back to T1
4. T1 detects it initiated the probe → deadlock detected
5. One transaction (typically the youngest) is aborted to break deadlock

## Exam Tips

1. **Remember the difference between centralized and distributed concurrency control**: Centralized has a single lock manager, while distributed distributes lock management across nodes.

2. **Two-Phase Commit is most important**: Know both phases (Prepare and Commit) and understand why it's called "two-phase."

3. **Deadlock detection in distributed systems uses wait-for graphs**: Understand how the wait-for graph is constructed and how cycles indicate deadlocks.

4. **Timestamp ordering ensures conflict serializability**: Transactions are ordered by timestamps, and older transactions have priority.

5. **ACID properties must be maintained in distributed transactions**: Be prepared to explain how each property is preserved in a distributed environment.

6. **Know the limitations of 2PC**: The blocking problem is a major limitation where participants can be blocked waiting for coordinator recovery.

7. **Isolation levels in distributed context**: Serializable isolation is often too expensive; practical systems use snapshot isolation or other weakened levels.

8. **Network partitioning challenges**: Understand CAP theorem implications—during network partitions, systems must choose between consistency and availability.

9. **Primary copy locking reduces communication**: Selecting the primary copy strategically can minimize lock acquisition overhead.

10. **Recovery in distributed transactions**: Understand the role of logs (prepare logs, commit logs) in recovering from failures during distributed transactions.
