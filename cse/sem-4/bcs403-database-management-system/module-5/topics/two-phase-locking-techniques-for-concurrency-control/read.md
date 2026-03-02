# Two-Phase Locking Techniques for Concurrency Control

## Table of Contents

- [Two-Phase Locking Techniques for Concurrency Control](#two-phase-locking-techniques-for-concurrency-control)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Two-Phase Locking (2PL)](#basic-two-phase-locking-2pl)
  - [Strict Two-Phase Locking (Strict 2PL)](#strict-two-phase-locking-strict-2pl)
  - [Rigorous Two-Phase Locking (Rigorous 2PL)](#rigorous-two-phase-locking-rigorous-2pl)
  - [Lock Compatibility Matrix](#lock-compatibility-matrix)
  - [Deadlock Handling](#deadlock-handling)
  - [Timestamp-Based Protocols (Alternative to 2PL)](#timestamp-based-protocols-alternative-to-2pl)
- [Examples](#examples)
  - [Example 1: Basic Two-Phase Locking](#example-1-basic-two-phase-locking)
  - [Example 2: Strict 2PL Preventing Cascading Abort](#example-2-strict-2pl-preventing-cascading-abort)
  - [Example 3: Lock Compatibility](#example-3-lock-compatibility)
- [Exam Tips](#exam-tips)

## Introduction

Concurrency control is a critical aspect of database management systems that ensures multiple transactions can execute simultaneously without violating data consistency. When multiple users access and modify the database concurrently, problems such as lost updates, uncommitted data, and inconsistent retrievals can arise. Two-Phase Locking (2PL) is one of the most widely used concurrency control techniques that ensures serializability of transactions by imposing a strict ordering on the lock acquisition and release operations.

The fundamental principle behind Two-Phase Locking is that a transaction must acquire all necessary locks before releasing any lock. This approach guarantees that the execution of concurrent transactions can be equivalent to some serial execution, thereby maintaining database consistency. The importance of 2PL in modern database systems cannot be overstated, as it forms the foundation for many commercial database management systems including Oracle, SQL Server, and MySQL.

In the context of the university's Database Management System course, understanding Two-Phase Locking techniques is essential for both theoretical knowledge and practical database design. This topic builds upon the concepts of transaction management, serializability, and concurrency problems covered in earlier modules. The techniques discussed here are directly applicable in real-world database development and are frequently tested in university examinations.

## Key Concepts

### Basic Two-Phase Locking (2PL)

Two-Phase Locking divides the execution of a transaction into two distinct phases:

1. **Growing Phase (Expanding Phase)**: In this phase, a transaction can acquire new locks but cannot release any lock. The transaction progressively acquires locks as needed for the resources it accesses. The number of locks held by the transaction continuously increases during this phase.

2. **Shrinking Phase**: Once a transaction releases its first lock, it enters the shrinking phase. During this phase, the transaction can only release locks but cannot acquire any new locks. The number of locks held continuously decreases.

The fundamental rule of 2PL states that the growing phase must be followed by the shrinking phase, with the point where the transaction acquires its final lock called the **lock point**. The serializability of transactions is guaranteed when they follow the Two-Phase Locking protocol.

**Example**: Consider Transaction T1 with operations: Read(A), Read(B), Write(A), Write(B)

- Growing phase: Acquire lock on A, Read A → Acquire lock on B, Read B
- Lock point reached after acquiring lock on B
- Shrinking phase: Release lock on A after writing A → Release lock on B after writing B

### Strict Two-Phase Locking (Strict 2PL)

Basic 2PL ensures serializability but does not prevent cascading rollbacks. In Strict 2PL, a transaction holds all exclusive (write) locks until the transaction commits or aborts. This modification prevents other transactions from reading uncommitted data modified by the transaction, thereby eliminating cascading aborts.

The key difference from basic 2PL is that the shrinking phase for write locks is delayed until the transaction completes (commits or aborts). Read locks can be released normally in the shrinking phase, but write locks are retained until the end.

**Advantage**: Ensures strict serializability and prevents cascading rollbacks, making recovery simpler.

### Rigorous Two-Phase Locking (Rigorous 2PL)

Rigorous 2PL is an even stricter variant where a transaction holds all locks (both read and write) until it commits or aborts. This approach completely eliminates the possibility of cascading rollbacks and simplifies transaction recovery significantly.

In Rigorous 2PL, the shrinking phase for all locks begins only after the transaction reaches its commit point. This means that throughout its execution, a transaction holds all locks it has acquired, and all locks are released together at the end.

**Advantage**: Simplifies recovery and ensures no cascading rollbacks. Most commercial databases implement some form of Rigorous 2PL.

### Lock Compatibility Matrix

The lock compatibility matrix determines whether a transaction can acquire a lock based on locks already held by other transactions:

|                | Shared Lock | Exclusive Lock |
| -------------- | ----------- | -------------- |
| Shared Lock    | Yes         | No             |
| Exclusive Lock | No          | No             |

- **Shared Lock (S Lock)**: Granted when a transaction only needs to read data. Multiple transactions can hold shared locks simultaneously on the same resource.
- **Exclusive Lock (X Lock)**: Granted when a transaction needs to modify data. Only one transaction can hold an exclusive lock on a resource at any time.

### Deadlock Handling

A deadlock occurs when two or more transactions are waiting indefinitely for locks held by each other. Two-Phase Locking, while ensuring serializability, can lead to deadlocks. There are two primary approaches to handle deadlocks:

1. **Deadlock Prevention**: The system ensures that deadlocks cannot occur by imposing a total ordering of lock requests. Techniques include:

- **Wait-Die Scheme**: Older transactions wait for younger ones; younger transactions die (abort)
- **Wound-Wait Scheme**: Older transactions wound (abort) younger ones; younger transactions wait

2. **Deadlock Detection**: The system periodically checks for cycles in the wait-for graph. When a deadlock is detected, one or more transactions are selected as victims and aborted to break the cycle.

### Timestamp-Based Protocols (Alternative to 2PL)

Timestamp-based concurrency control protocols provide an alternative to locking-based approaches:

1. **Basic Timestamp Ordering (TO)**: Each transaction receives a timestamp at startup. Operations are executed only if the timestamp is valid; otherwise, the transaction is rejected and restarted.

2. **Thomas's Write Rule**: A modified version of timestamp ordering that allows certain write operations to proceed even if they would normally be rejected, improving concurrency.

Timestamp protocols avoid deadlocks but may suffer from starvation and may not always ensure serializability.

## Examples

### Example 1: Basic Two-Phase Locking

Consider two transactions T1 and T2 executing concurrently on data items A and B:

```
T1: Read(A), Write(A), Read(B), Write(B)
T2: Read(B), Write(B), Read(A), Write(A)
```

**Solution using Basic 2PL**:

**Step 1**: T1 acquires X lock on A, reads and writes A
**Step 2**: T1 tries to acquire X lock on B, but T2 already holds X lock on B (waiting)
**Step 3**: T2 acquires X lock on B, reads and writes B
**Step 4**: T2 tries to acquire X lock on A, but T1 already holds X lock on A (waiting)

This creates a deadlock. The system must detect this and abort one transaction. After aborting and restarting T2 with a new timestamp, the schedule becomes serializable.

**Serial execution equivalent**: Either T1 completely followed by T2, or T2 completely followed by T1.

### Example 2: Strict 2PL Preventing Cascading Abort

```
T1: Read(A), Write(A), Read(B), Write(B), Commit
T2: Read(A), Read(B), Commit
```

**Step-by-step with Strict 2PL**:

1. T1 acquires X lock on A, reads A=10, writes A=20
2. T1 acquires X lock on B, reads B=30, writes B=40
3. T2 requests S lock on A - **DENIED** (T1 holds X lock)
4. T2 waits for T1 to release locks
5. T1 commits and releases X locks on A and B
6. T2 acquires S locks on A and B, reads values
7. T2 commits

**Key Point**: T2 cannot read uncommitted values of A and B from T1 because T1 holds exclusive locks until commit. This prevents cascading aborts.

### Example 3: Lock Compatibility

Consider the following schedule with three transactions:

```
T1: Read(A), Write(A)
T2: Read(A)
T3: Read(A)
```

**Execution with Lock Compatibility**:

1. T1 acquires X lock on A, reads A
2. T1 writes A (still holding X lock)
3. T2 requests S lock on A - **DENIED** (X lock held by T1)
4. T3 requests S lock on A - **DENIED** (X lock held by T1)
5. T1 commits and releases X lock
6. T2 and T3 can now both acquire S locks on A simultaneously
7. Both read the updated value

**Result**: The write operation of T1 is serialized before reads of T2 and T3, ensuring consistency.

## Exam Tips

1. **Remember the two phases**: The growing phase (lock acquisition) must always precede the shrinking phase (lock release). This is the fundamental rule of 2PL.

2. **Differentiate between 2PL variants**: Basic 2PL allows early lock release causing cascading aborts; Strict 2PL releases write locks only at commit; Rigorous 2PL releases all locks only at commit.

3. **Lock compatibility is crucial**: Shared locks are compatible with shared locks but not with exclusive locks. Exclusive locks are not compatible with any other lock type.

4. **Deadlock vs. Starvation**: Deadlock involves circular waiting, while starvation involves indefinite waiting due to priority issues. Know the prevention and detection techniques for each.

5. **Serializability guarantee**: The primary advantage of 2PL is that it guarantees conflict serializability for any schedule of transactions.

6. **Draw wait-for graphs**: For deadlock detection questions, practice drawing wait-for graphs where vertices are transactions and edges represent waiting relationships.

7. **Thomas's Write Rule**: Remember this is a modification to basic timestamp ordering that allows certain out-of-order writes to be treated as blind writes, improving concurrency.

8. **Commercial implementation**: Most real-world databases use Rigorous 2PL or a variation because it simplifies recovery and prevents cascading rollbacks completely.
