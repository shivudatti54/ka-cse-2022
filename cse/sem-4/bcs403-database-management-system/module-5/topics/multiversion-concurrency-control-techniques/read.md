# Multiversion Concurrency Control Techniques

## Introduction

Multiversion Concurrency Control (MVCC) is an advanced database concurrency control technique that allows multiple versions of data items to exist simultaneously, enabling read operations to proceed without blocking write operations and vice versa. Unlike traditional locking-based approaches, MVCC maintains historical versions of data, ensuring that transactions always see a consistent snapshot of the database while other transactions modify the data concurrently.

The importance of MVCC in modern database systems cannot be overstated. It addresses the fundamental conflict between read and write operations in high-concurrency environments. In traditional Two-Phase Locking (2PL), read operations must acquire shared locks, which can be blocked by exclusive locks held by other transactions. This blocking leads to reduced throughput and potential deadlocks. MVCC eliminates this problem by allowing readers to access previous versions of data while writers create new versions, fundamentally improving database performance in multi-user environments.

Major database management systems like PostgreSQL, MySQL (InnoDB), Oracle, and SQL Server extensively use MVCC to provide high concurrency without sacrificing data consistency. Understanding MVCC is essential for database administrators and software engineers who design systems requiring reliable concurrent access to shared data.

## Key Concepts

### Fundamentals of Multiversioning

MVCC works on the principle of maintaining multiple physical versions of each data item. When a transaction modifies a tuple, instead of overwriting the existing data, the database creates a new version while retaining the old version. Each version contains additional metadata such as creation transaction ID and expiration transaction ID, which help determine which transactions can access which versions.

The core idea is simple yet powerful: write operations create new versions while read operations access the appropriate version based on isolation level and transaction timestamp. This approach ensures that long-running read queries are never blocked by concurrent updates, and write operations never wait for readers to complete.

Each version stores metadata including:

- **Transaction ID (XID)**: Unique identifier of the transaction that created the version
- **Begin/End Timestamps**: Valid time interval for each version
- **Pointer**: Links to previous and next versions for chain traversal

### Timestamp-Based Concurrency Control

Timestamp-Based Concurrency Control (TBC) assigns a unique timestamp to each transaction when it begins. The timestamp determines the serialization order of transactions. Unlike lock-based approaches that use mutual exclusion, TBC uses timestamps to order operations and ensure serializability.

**Thomas's Write Rule** is an important optimization in timestamp-based systems: if a transaction T wants to write a data item Q, but T's timestamp is older than the timestamp of the transaction that last wrote Q, then the write can be ignored because the previous write would have overwritten it in any serializable schedule.

The basic timestamp ordering rules are:

1. **Read Rule**: A transaction T can read data item Q only if the last write timestamp on Q is less than T's timestamp
2. **Write Rule**: A transaction T can write data item Q only if the last read and write timestamps on Q are both less than T's timestamp

When these rules are violated, the transaction is aborted and restarted with a new timestamp.

### Snapshot Isolation

Snapshot Isolation is a widely implemented isolation level based on MVCC principles. Under Snapshot Isolation, each transaction sees a snapshot of the database as it existed at the start of the transaction. This snapshot contains all committed updates made before the transaction started and excludes all uncommitted or subsequent updates.

**First-Committer-Wins** is the standard rule for write-write conflicts in Snapshot Isolation. If two transactions attempt to modify the same tuple, the first transaction to commit succeeds, and the second transaction is aborted due to a write-write conflict. This prevents the "Lost Update" problem that occurs in Read Uncommitted isolation.

Snapshot Isolation provides the following guarantees:

- **Consistent Reads**: Each transaction sees a stable view throughout its execution
- **No Non-Repeatable Reads**: Multiple reads within a transaction return the same data
- **No Phantoms**: Inserted or deleted records by other transactions are not visible

### Multi-Version Timestamp Ordering (MVTO)

Multi-Version Timestamp Ordering combines the benefits of timestamp ordering with version maintenance. MVTO maintains multiple versions of data items, and each version stores the timestamp of the transaction that created it.

In MVTO:

- Read operations never block and never abort; they simply read the appropriate version
- Write operations create new versions if the timestamp ordering rule is satisfied
- If a transaction attempts to write a version that was already read by another transaction with a later timestamp, the write is rejected

This approach ensures that read-heavy workloads experience no interference from concurrent writes.

### Serializable Snapshot Isolation (SSI)

Serializable Snapshot Isolation is an enhancement to Snapshot Isolation that provides true serializability while maintaining the performance benefits of MVCC. SSI detects potential serialization anomalies (like write skew) that Snapshot Isolation allows and resolves them by aborting one of the conflicting transactions.

SSI uses two key pieces of information stored with each tuple:

- **Tmin**: Lower bound of transactions that have read the tuple
- **Tmax**: Upper bound of transactions that have read the tuple without conflicts

When a transaction commits, SSI checks whether its write set conflicts with the read sets of concurrent transactions. If a dangerous structure is detected, one of the transactions is aborted to ensure serializability.

## Examples

### Example 1: Timestamp-Based Concurrency Control

Consider a banking database with an account balance of $1000. Transaction T1 (timestamp 10) wants to read the balance, and Transaction T2 (timestamp 20) wants to withdraw $200.

```
Initial: Balance = $1000, LastWriteTimestamp = 5

T1 (TS=10) Read Operation:
- Check: LastWriteTimestamp (5) < T1's timestamp (10) ✓
- T1 reads Balance = $1000

T2 (TS=20) Write Operation:
- Check: LastReadTimestamp (10) < T2's timestamp (20) ✓
- Check: LastWriteTimestamp (5) < T2's timestamp (20) ✓
- T2 writes Balance = $800 (1000 - 200)
- Update LastWriteTimestamp to 20
```

Both operations succeed because T1 (reading old value) and T2 (writing new value) are properly ordered by timestamps.

### Example 2: Snapshot Isolation - Write-Write Conflict

Consider two transactions T1 and T2 both starting simultaneously, attempting to update the same inventory item:

```
Inventory Table: Product_A, Quantity = 50

T1: UPDATE Inventory SET Quantity = 40 WHERE Product = 'Product_A'
T2: UPDATE Inventory SET Quantity = 30 WHERE Product = 'Product_A'

Scenario: T1 commits first
- T1 sees Quantity = 50 (snapshot at start)
- T1 writes Quantity = 40, commits successfully
- T2 tries to commit; system detects conflict with T1's write
- T2 is aborted (First-Committer-Wins rule)

Result: Only T1's update is visible, Quantity = 40
```

### Example 3: Read Operations Never Block

Demonstrating how MVCC allows concurrent reads without blocking:

```
Table: Employee (id, salary)

Initial: Employee 'John' has salary = 50000
Version 1: Created by Transaction 100

Transaction T1 (Long-running report):
- Starts at timestamp 100
- Reads John's salary = 50000
- Takes 10 minutes to complete
- Never blocked by any concurrent operations

Transaction T2 (Update):
- Starts at timestamp 150
- Updates John's salary to 55000
- Creates Version 2
- Commits successfully

Transaction T3 (Short read):
- Starts at timestamp 200
- Reads John's salary = 55000 (sees committed update)
```

Even though T1 started before T2's update, T1 completes successfully reading the old version, demonstrating MVCC's ability to provide consistent snapshots without blocking readers.

## Exam Tips

1. **Remember the key advantage**: MVCC allows readers to not block writers and writers to not block readers, unlike traditional locking.

2. **Snapshot Isolation vs Serializable Snapshot Isolation**: Snapshot Isolation may allow anomalies like Write Skew, while SSI provides true serializability by detecting and resolving these anomalies.

3. **First-Committer-Wins vs First-Winner-Writes**: In Snapshot Isolation, the first transaction to commit wins; the second is aborted. This is crucial for understanding write-write conflicts.

4. **Version Chain**: Understand that each tuple may have multiple versions linked through pointers, and the database selects the appropriate version based on transaction timestamp.

5. **Garbage Collection**: Know that old versions must eventually be cleaned up to reclaim storage space—this is called garbage collection or vacuuming in PostgreSQL.

6. **Thomas's Write Rule**: Remember this optimization allows ignoring certain obsolete writes in timestamp-based concurrency control, improving system throughput.

7. **MVCC in Real Systems**: PostgreSQL uses SSI, Oracle uses MVCC with rollback segments, and MySQL InnoDB uses MVCC—be familiar with how these systems implement MVCC.

8. **Trade-offs**: While MVCC improves concurrency, it increases storage requirements (multiple versions) and adds complexity to transaction management.

9. **Isolation Levels**: MVCC naturally provides Snapshot Isolation and can be extended to achieve Serializability (SSI) by detecting dangerous structures in the dependency graph.
