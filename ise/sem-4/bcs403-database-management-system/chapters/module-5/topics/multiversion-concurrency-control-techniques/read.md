# Multiversion Concurrency Control (MVCC) Techniques

**Subject:** Database Management System (DBMS)
**Module:** Module 5
**Topic:** Concurrency Control Techniques

## 1. Introduction

In a multi-user Database Management System (DBMS), **Concurrency Control** is essential for managing simultaneous transactions to ensure data integrity and consistency. Traditional locking-based mechanisms can lead to performance bottlenecks and deadlocks. **Multiversion Concurrency Control (MVCC)** is a sophisticated, non-locking technique that enhances concurrency and performance by maintaining multiple versions of a data item. This allows readers to operate without blocking writers and vice versa, making it a cornerstone of modern databases like PostgreSQL, Oracle, and MySQL (InnoDB).

## 2. Core Concepts of MVCC

MVCC's fundamental principle is simple: instead of overwriting data, it creates a new version of a data item whenever it is updated. This means the database stores multiple states of the same data object at different points in time.

### How MVCC Works

1.  **Data Storage:** Each tuple (row) in a table has two additional, hidden system columns (or metadata fields):
    - **Creation Transaction ID (Xmin):** The ID of the transaction that created (inserted) this version of the tuple.
    - **Expiration Transaction ID (Xmax):** The ID of the transaction that deleted this version or updated it (which effectively marks this version as obsolete). It is initially null.

2.  **Snapshot Isolation:** When a transaction (`T_i`) begins, the DBMS takes a **snapshot** of the database. This snapshot represents a consistent view of the database state as it existed at the start of the transaction. `T_i` will only see data that was committed before it started; it is isolated from changes made by concurrent transactions that commit after it began.

3.  **Read Operation:** When a transaction requests to read a data item, the MVCC system scans the chain of versions for that item. It selects the most recent version that was committed _before_ the transaction's snapshot was taken and whose `Xmax` is either not set or set by a transaction not in the snapshot. This ensures the transaction reads a consistent, stable version of the data.

4.  **Write Operations:**
    - **UPDATE:** Does not overwrite the existing tuple. Instead, it creates a new version of the tuple with a new `Xmin` (set to the current transaction's ID). The old version's `Xmax` is set to the current transaction's ID, marking it as expired.
    - **DELETE:** Does not physically remove the tuple immediately. It sets the `Xmax` of the current version to the current transaction's ID, logically deleting it.
    - **INSERT:** Creates a new tuple with the `Xmin` set to the current transaction's ID and `Xmax` initially null.

5.  **Commit and Cleanup:** Once a transaction commits, its changes become visible to all new snapshots. Old versions of data that are no longer visible to any active transaction (as per their snapshots) are eventually removed by a separate database process often called the **vacuum** or **cleanup** process. This reclaims storage space.

### A Simple Example

Consider two transactions operating on a bank account balance (Account A = $1000).

- **T1 (Transaction 1):** A long-running read operation (e.g., generating a monthly statement) starts at time `t1`.
- **T2 (Transaction 2):** Updates Account A to $1200 and commits at time `t2`.

| Time | Action                                                                                                                                                                                                                                                             | T1's Snapshot (started at t1) sees... | T2's Snapshot (started after t2) sees... |
| :--- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------ | :--------------------------------------- |
| `t1` | **T1 begins.** Takes a snapshot of the database.                                                                                                                                                                                                                   |                                       |                                          |
|      | The database has one version of Account A: `Balance=$1000` (Xmin=TxOld, Xmax=null)                                                                                                                                                                                 |                                       |                                          |
| `t2` | **T2 updates** Account A to $1200. A new version is created: `Balance=$1200` (Xmin=T2, Xmax=null). <br> The old version is marked: `Balance=$1000` (Xmin=TxOld, Xmax=T2).                                                                                          |                                       |                                          |
| `t3` | **T2 commits.**                                                                                                                                                                                                                                                    |                                       |                                          |
| `t4` | **T1 reads** Account A. It scans the versions. It finds the latest version valid for its snapshot (which was before T2 committed). It ignores the new version ($1200) because T2 was not committed at the time of its snapshot. It reads the old version: `$1000`. | Sees $1000 (a consistent view)        |                                          |
| `t5` | A new transaction **T3 begins** _after_ T2 committed. It takes a new snapshot that includes T2's commit.                                                                                                                                                           |                                       |                                          |
| `t6` | **T3 reads** Account A. Its snapshot sees the version created by T2 as valid.                                                                                                                                                                                      |                                       | Sees $1200                               |

This example shows how MVCC allows T1 to read a consistent value without being blocked by T2's write, and T2's write was not blocked by T1's read.

## 3. Key Points & Summary

- **Core Idea:** MVCC maintains multiple physical versions of a single logical data item.
- **Key Benefit:**
  - **Reads don't block writes, writes don't block reads.** This significantly increases potential concurrency and system throughput compared to strict locking protocols.
  - Eliminates the read-write and write-write conflicts that cause deadlocks in locking schemes.
- **Mechanism:** Uses hidden metadata (Xmin, Xmax) and **snapshot isolation** to provide each transaction with a consistent view of the past.
- **Overhead:** The main trade-off is increased storage and maintenance overhead. The system must store multiple versions and periodically clean up obsolete ones (via vacuuming).
- **Prevents:** It prevents dirty reads and non-repeatable reads but requires additional mechanisms (like predicate locking) to fully prevent phantoms.
- **Ubiquity:** MVCC is the preferred concurrency control method in most modern relational and non-relational (NoSQL) database systems due to its performance advantages.
