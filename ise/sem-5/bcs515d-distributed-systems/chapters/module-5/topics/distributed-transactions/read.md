# Introduction to Distributed Transactions

## 1. What are Distributed Transactions?

A **distributed transaction** is a type of transaction that spans multiple networked computing resources, typically databases or services located on different servers. Unlike local transactions that operate on a single database, distributed transactions require coordination across multiple participants to ensure data consistency throughout the system.

### Key Characteristics:

- **Atomicity**: The entire transaction must succeed or fail as a unit
- **Consistency**: The transaction must bring the system from one valid state to another
- **Isolation**: Concurrent transactions shouldn't interfere with each other
- **Durability**: Once committed, changes persist even after system failures

These properties are collectively known as **ACID properties**, which are extended from single database transactions to distributed environments.

```
Example: A banking transaction transferring $100 from Account A (Bank X) to Account B (Bank Y)
1. Debit $100 from Account A at Bank X
2. Credit $100 to Account B at Bank Y
3. Both operations must succeed or both must fail
```

## 2. Why Distributed Transactions Matter

Distributed transactions are essential in modern computing environments because:

- **Microservices Architecture**: Different services manage their own databases
- **Business Process Integration**: Cross-organizational transactions (e.g., supply chain)
- **Cloud Computing**: Resources are distributed across availability zones
- **Data Partitioning**: Sharded databases for scalability

Without proper distributed transaction management, systems risk data inconsistency, which can lead to financial errors, inventory discrepancies, and other critical business problems.

## 3. Flat vs. Nested Distributed Transactions

### Flat Distributed Transactions

These involve multiple participants but follow a simple linear structure where all operations are at the same level.

```
Client
  │
  ├──→ Participant 1 (Database A)
  ├──→ Participant 2 (Database B)
  └──→ Participant 3 (Service C)
```

**Characteristics:**

- Single level of coordination
- All participants treated equally
- Simpler to implement but less flexible

### Nested Distributed Transactions

These create a hierarchy of subtransactions, where each subtransaction can itself contain other subtransactions.

```
Top-level Transaction
  │
  ├──→ Subtransaction 1
  │      ├──→ Operation A
  │      └──→ Operation B
  │
  └──→ Subtransaction 2
         ├──→ Operation C
         └──→ Subtransaction 2.1
                └──→ Operation D
```

**Characteristics:**

- Hierarchical structure
- Support for partial rollbacks
- Greater flexibility but more complex
- Better suited for long-running business processes

**Comparison Table:**

| Aspect         | Flat Transactions | Nested Transactions        |
| -------------- | ----------------- | -------------------------- |
| Structure      | Single level      | Hierarchical               |
| Complexity     | Lower             | Higher                     |
| Partial Commit | Not supported     | Supported                  |
| Recovery       | Simpler           | More complex               |
| Use Cases      | Simple operations | Complex business processes |

## 4. Atomic Commit Protocols

Atomic commit protocols ensure that a distributed transaction either commits at all participants or aborts at all participants.

### Two-Phase Commit (2PC)

The most widely used atomic commit protocol.

**Phase 1: Preparation Phase**

1. Coordinator sends "prepare" message to all participants
2. Participants perform operations but don't commit
3. Participants respond with "yes" (ready to commit) or "no" (must abort)

**Phase 2: Commit/Abort Phase** 4. If all participants voted "yes": coordinator sends "commit" 5. If any participant voted "no": coordinator sends "abort" 6. Participants acknowledge commit/abort

```
Sequence Diagram:
Coordinator    Participant 1    Participant 2
     |               |               |
     |---prepare---->|               |
     |               |---prepare---->|
     |<--yes---------|               |
     |               |<--yes---------|
     |---commit----->|               |
     |               |---commit----->|
     |<--ack---------|               |
     |               |<--ack---------|
```

**Advantages:**

- Ensures atomicity
- Widely understood and implemented

**Disadvantages:**

- Blocking protocol (participants may wait indefinitely)
- Single point of failure (coordinator)
- Multiple message rounds create latency

### Three-Phase Commit (3PC)

An extension of 2PC that reduces blocking problems.

**Phases:**

1. **CanCommit**: Coordinator queries if participants can commit
2. **PreCommit**: If all agree, coordinator sends pre-commit
3. **DoCommit**: If all acknowledge pre-commit, coordinator sends commit

**Advantages:**

- Non-blocking in certain failure scenarios
- Better fault tolerance

**Disadvantages:**

- More complex
- Additional message rounds
- Still not completely fault-tolerant

## 5. Concurrency Control in Distributed Transactions

Concurrency control mechanisms ensure that concurrent transactions don't interfere with each other while maintaining isolation.

### Lock-based Protocols

- **Distributed Two-Phase Locking (2PL)**: Extends traditional 2PL across participants
- **Primary Copy Locking**: One designated copy manages locks for all replicas
- **Centralized Lock Manager**: Single lock service for the entire system

### Timestamp-based Protocols

- Each transaction receives a unique timestamp
- Operations are ordered based on timestamps
- Conflicts are resolved by aborting the transaction with the earlier timestamp

### Optimistic Concurrency Control

- Transactions proceed without locking
- Validation phase checks for conflicts before commit
- Conflicting transactions are aborted and restarted

**Comparison of Concurrency Control Methods:**

| Method          | Advantages         | Disadvantages          | Best For                      |
| --------------- | ------------------ | ---------------------- | ----------------------------- |
| Distributed 2PL | Strong consistency | Deadlock potential     | High consistency requirements |
| Timestamp-based | No deadlocks       | Timestamp management   | Systems with global time      |
| Optimistic      | High throughput    | Abort rate may be high | Low conflict environments     |

## 6. Distributed Deadlocks

Deadlocks can occur in distributed systems when transactions wait for resources held by each other in a cycle.

### Deadlock Detection Methods:

- **Centralized**: Single deadlock detection component
- **Distributed**: Each site performs local detection, global picture emerges from cooperation
- **Hierarchical**: Sites grouped in hierarchy, detection at multiple levels

### Deadlock Prevention:

- **Wait-Die**: Older transactions wait, younger ones die
- **Wound-Wait**: Older transactions wound (abort) younger ones
- **Timeout-based**: Transactions abort after waiting too long

## 7. Transaction Recovery

Recovery mechanisms ensure that transactions can be properly completed even after failures.

### Log-based Recovery:

- **Write-Ahead Logging (WAL)**: Log entries written before actual data changes
- **Redo Logs**: Record changes to be reapplied after recovery
- **Undo Logs**: Record changes to be rolled back after failure

### Checkpointing:

- Periodic saving of system state
- Reduces recovery time by limiting the log that needs to be processed

## 8. Real-world Examples

**Banking System:**

```
Transaction: Transfer $500 from Account A (Bank X) to Account B (Bank Y)
1. Begin transaction
2. Debit $500 from Account A (participant 1)
3. Credit $500 to Account B (participant 2)
4. If both succeed → commit
5. If either fails → abort both
```

**E-commerce Order:**

```
Transaction: Create order with inventory update and payment processing
1. Begin transaction
2. Reserve inventory (Inventory service)
3. Process payment (Payment service)
4. Create order (Order service)
5. If all succeed → commit
6. If any fails → abort all operations
```

## Exam Tips

1. **Understand ACID Properties**: Be able to explain how each property is maintained in distributed environments
2. **Compare 2PC and 3PC**: Know the differences, advantages, and disadvantages of each protocol
3. **Draw Diagrams**: Practice drawing sequence diagrams for commit protocols
4. **Concurrency Control**: Understand the trade-offs between different concurrency control methods
5. **Failure Scenarios**: Be prepared to explain how systems handle various failure cases
6. **Real-world Applications**: Relate concepts to practical examples like banking or e-commerce systems
7. **Terminology**: Master key terms like coordinator, participant, prepare, commit, abort, and their roles

Remember that distributed transactions involve trade-offs between consistency, availability, and performance. The CAP theorem (which states that a distributed system can only provide two of three guarantees: Consistency, Availability, and Partition Tolerance) often influences design decisions in real-world systems.
