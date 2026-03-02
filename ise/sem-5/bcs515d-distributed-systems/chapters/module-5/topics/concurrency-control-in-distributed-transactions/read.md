# Concurrency Control in Distributed Transactions

## Introduction

In distributed systems, transactions often span multiple servers or databases, accessing data items stored at different locations. **Concurrency control** refers to the process of managing simultaneous operations on shared data to ensure transaction isolation and consistency while maintaining system performance. In distributed environments, this becomes significantly more complex due to the lack of shared memory, communication delays, and potential partial failures.

The primary goal of concurrency control is to provide the **illusion of serializability** – making it appear as though transactions executed one after another, even though they may be interleaved. This preserves the consistency of the database despite concurrent execution.

## Key Concepts and Challenges

### Serializability

A schedule of transactions is serializable if its outcome is equivalent to some serial schedule (one where transactions execute one after another without interleaving). This is the fundamental correctness criterion for concurrent transactions.

### ACID Properties in Distributed Context

- **Atomicity**: A transaction must be all-or-nothing across all participating sites.
- **Consistency**: Transactions must preserve database consistency constraints across all sites.
- **Isolation**: Concurrent transactions must not interfere with each other, despite distribution.
- **Durability**: Committed changes must persist across all sites despite failures.

### Unique Distributed Challenges

- **Network latency** affects coordination between sites
- **Partial failures** where some sites are unavailable while others operate
- **Heterogeneous systems** with different concurrency control mechanisms
- **Increased communication overhead** for coordination

## Concurrency Control Techniques

### 1. Distributed Two-Phase Locking (2PL)

Two-phase locking is extended to distributed environments with lock managers at each site coordinating through messages.

#### Phases:

1. **Growing Phase**: Transaction acquires all required locks (shared or exclusive)
2. **Shrinking Phase**: Transaction releases locks (but cannot acquire new ones)

In distributed 2PL, a transaction must acquire all locks at all sites before it can proceed to the shrinking phase.

```
Transaction T1:
1. Send lock requests to all sites        -> Growing Phase
2. Receive lock grants from all sites
3. Perform operations
4. Send unlock requests to all sites     -> Shrinking Phase

Site 1 LM: receives lock request -> grants lock
Site 2 LM: receives lock request -> grants lock
```

#### Variants:

- **Centralized 2PL**: Single lock manager for entire system
- **Primary Copy 2PL**: Locks for a data item managed at its primary site
- **Distributed 2PL**: Lock managers at each site coordinate

**Comparison of 2PL Approaches:**

| Approach         | Advantages                                       | Disadvantages                                         |
| ---------------- | ------------------------------------------------ | ----------------------------------------------------- |
| Centralized 2PL  | Simple implementation, deadlock detection easier | Single point of failure, potential bottleneck         |
| Primary Copy 2PL | Better load distribution, reduced communication  | Need to maintain primary copy information             |
| Distributed 2PL  | No single point of failure, good scalability     | Complex deadlock detection, higher communication cost |

### 2. Timestamp Ordering Protocols

Each transaction is assigned a unique timestamp, and operations are ordered based on these timestamps.

#### Basic Timestamp Ordering:

- Each data item has read-timestamp (largest timestamp of transaction that read it) and write-timestamp (largest timestamp of transaction that wrote it)
- If transaction T with timestamp TS(T) requests to read data item X:
  - If TS(T) < write-timestamp(X), reject and abort T
  - Otherwise, allow read and set read-timestamp(X) = max(read-timestamp(X), TS(T))
- If transaction T with timestamp TS(T) requests to write data item X:
  - If TS(T) < read-timestamp(X), reject and abort T
  - If TS(T) < write-timestamp(X), reject (Thomas Write Rule allows this write to be ignored instead of aborting)
  - Otherwise, allow write and set write-timestamp(X) = TS(T)

#### Distributed Timestamp Generation:

Timestamps must be unique and globally meaningful. Common approaches:

- **Physical timestamps**: Using synchronized clocks (challenging due to clock skew)
- **Logical timestamps**: Lamport clocks or vector clocks to maintain causal ordering

### 3. Multiversion Concurrency Control (MVCC)

Maintains multiple versions of data items to allow readers to access older consistent versions while writers create new versions.

```
Data item X:
Version X1 (timestamp 10) - value = 100
Version X2 (timestamp 20) - value = 150
Version X3 (timestamp 30) - value = 200

Transaction with timestamp 25 would read version X2
```

#### Benefits:

- Read operations rarely blocked (can read older consistent versions)
- Better support for read-intensive workloads
- Snapshot isolation capabilities

#### Challenges in Distributed Context:

- Version storage overhead across multiple sites
- Version garbage collection coordination
- Determining which versions to maintain at which sites

### 4. Optimistic Concurrency Control

Transactions proceed without locking, checking for conflicts only at commit time.

#### Three phases:

1. **Read Phase**: Transaction executes, makes tentative updates in private workspace
2. **Validation Phase**: Check if transaction's execution serializes with committed transactions
3. **Write Phase**: If validation succeeds, make changes permanent; else abort

```
Transaction T:
[Read Phase] -> Read data, compute results
[Validation Phase] -> Check for conflicts with committed transactions
[Write Phase] -> Commit changes if valid, else abort
```

#### Distributed Validation:

- Requires global validation protocol
- Needs to check conflicts across all participating sites
- Can use timestamp ordering for validation

## Distributed Deadlocks

Deadlocks can occur when transactions wait for locks held by other transactions in a cycle.

### Deadlock Detection Approaches:

#### 1. Centralized Deadlock Detection

- One site designated as deadlock detector
- All sites periodically send wait-for graphs to central detector
- Central detector combines graphs and checks for cycles

```
Site 1: T1 -> T2 (waiting)
Site 2: T2 -> T3 (waiting)
Site 3: T3 -> T1 (waiting)

Central detector combines: Cycle T1->T2->T3->T1 -> Deadlock!
```

#### 2. Distributed Deadlock Detection

- Each site maintains part of the wait-for graph
- Sites exchange information to detect global cycles
- Algorithms like Chandy-Misra-Haas or Obermarck

#### 3. Deadlock Prevention

- Assign priorities to transactions (e.g., based on timestamps)
- If lower-priority transaction holds lock needed by higher-priority transaction:
  - **Wait-die**: Older transaction waits, younger transaction dies
  - **Wound-wait**: Older transaction wounds (aborts) younger transaction, younger transaction waits

## Replication and Concurrency Control

When data is replicated across multiple sites, concurrency control must maintain consistency across copies.

### Primary Copy Approach

- One site designated as primary for each data item
- All locks managed at primary site
- Updates propagated to secondary copies

### Voting Protocols

- Transactions must acquire locks from a majority of copies
- Quorum-based approaches: Read quorum (Qr) and Write quorum (Qw) where Qr + Qw > N and 2Qw > N (N = total copies)

## Performance Considerations

### Factors Affecting Performance:

- **Communication cost**: Number of messages required for coordination
- **Response time**: Latency introduced by distributed coordination
- **Abort rate**: How often transactions must be aborted due to conflicts
- **Throughput**: Number of transactions processed per time unit

### Trade-offs:

- Locking protocols: Higher communication cost, lower abort rates
- Timestamp ordering: Lower communication cost, higher abort rates
- Optimistic protocols: Good for low conflict environments, poor for high conflict

## Example Scenario

Consider a banking system with branches in New York (Site A) and London (Site B). Account X is at Site A, Account Y is at Site B.

Transaction T1: Transfer $100 from X to Y
Transaction T2: Calculate total balance of X + Y

**With Distributed 2PL:**

```
T1: Lock X (exclusive) at Site A, Lock Y (exclusive) at Site B
T2: Lock X (shared) at Site A, Lock Y (shared) at Site B

If T1 acquires locks first, T2 must wait until T1 releases locks
This ensures T2 sees consistent state (either before or after transfer)
```

**With Timestamp Ordering:**

```
Assume TS(T1) = 100, TS(T2) = 150

T1 writes X and Y at respective sites
T2 attempts to read X and Y

If T2's read occurs after T1's write at both sites, it sees new values
If T2's read occurs before T1's write completes, it sees old values
But timestamp checking ensures serializable ordering
```

## Exam Tips

1. **Understand the trade-offs**: Be prepared to compare different concurrency control methods and explain when each is appropriate.

2. **Focus on distributed challenges**: Highlight how distribution affects concurrency control (communication costs, partial failures, etc.).

3. **Know the protocols thoroughly**: Be able to explain the steps of 2PL, timestamp ordering, and optimistic concurrency control with distributed examples.

4. **Practice with scenarios**: Work through examples showing how different protocols handle specific transaction sequences.

5. **Remember deadlock handling**: Understand the differences between detection and prevention approaches in distributed environments.

6. **Connect with other topics**: Relate concurrency control to atomic commit protocols (2PC, 3PC) and recovery techniques.

7. **Watch for terminology**: Distinguish between local and global deadlocks, centralized vs distributed approaches, and different timestamp generation methods.
