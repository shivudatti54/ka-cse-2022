# Multiversion Concurrency Control (MVCC) Techniques

**Subject:** Database Management System (DBMS)  
**Module:** Module 5

## 1. Introduction

In a multi-user Database Management System, concurrency control is crucial for ensuring that simultaneous transactions do not interfere with each other, thereby preserving data consistency and integrity. Traditional locking mechanisms can lead to performance bottlenecks, deadlocks, and hinder read operations. **Multiversion Concurrency Control (MVCC)** is an advanced, elegant technique that addresses these issues by creating multiple versions of a data item. This allows read operations to access a consistent snapshot of the database without waiting for write operations to complete, significantly increasing throughput in environments with many readers.

## 2. Core Concepts of MVCC

MVCC's fundamental idea is to avoid assigning exclusive locks on data items for read operations. Instead, it maintains several versions of a data item. When a transaction needs to read data, it is presented with the most recent version that was committed when the transaction began, ensuring a consistent view.

### How MVCC Works: The Mechanics

1.  **Data Storage with Versions:** For each row (or data item) that is updated, the DBMS does not overwrite the old value. Instead, it creates a new version of that row. The old version is retained. This means the database stores a history of changes.

2.  **Timestamps/Snapshots:** Each transaction is assigned a unique start timestamp (e.g., `T_start`). This timestamp defines the transaction's view of the database.

3.  **Read Operation:** When a transaction `T_i` with start time `S_i` requests to read a data item, the concurrency control manager does not simply return the latest value. Instead, it searches through the list of versions for that item and selects the most recent version that was committed **before** `T_i` started (`commit_ts < S_i`). This provides `T_i` with a consistent snapshot from time `S_i`, isolated from any subsequent changes made by other transactions.

4.  **Write Operation:** When a transaction `T_j` wants to update a data item, it creates a new version of that item. This new version is stamped with the transaction's id and is initially in an "uncommitted" state. It becomes visible to other transactions only after `T_j` commits. The system also records a timestamp for when the version was created and when it was committed.

5.  **Garbage Collection:** Since storing every version forever is impractical, the DBMS employs a garbage collector to remove "old" versions that are no longer needed by any active or future transactions.

### Key Components for Version Tracking

Different systems implement MVCC slightly differently, but common elements include:
*   **Transaction ID (XID):** A unique identifier for each transaction.
*   **Creation XID (xmin):** The ID of the transaction that created this version.
*   **Deletion XID (xmax):** The ID of the transaction that deleted this version (or marked it for deletion). If null, the version is still valid.

## 3. Example Scenario

Let's consider a simple data item: `Balance = 1000` (Version V1, committed by an old transaction).

*   **Time t1:** Transaction `T1` (Start Timestamp = 100) begins. It wants to read the `Balance`.
    *   *Result:* It is served the latest committed version, V1. `Balance = 1000`.

*   **Time t2:** Transaction `T2` (Start Timestamp = 101) begins and updates the `Balance` to `1100`. A new version, V2, is created. It is marked as being created by `T2` and is uncommitted.

*   **Time t3:** While `T2` is still active, `T1` reads the `Balance` again.
    *   *Result:* The MVCC system looks for the most recent version committed *before T1's start time (100)*. V2 was created by `T2` (timestamp 101) which started *after* `T1` and is still uncommitted. Therefore, `T1` is again served the older, committed version V1 (`Balance = 1000`). This is a **consistent read**; `T1` sees the same data throughout its lifetime, unaffected by `T2`.

*   **Time t4:** `T2` commits. Version V2 is now marked as committed.

*   **Time t5:** A new transaction `T3` (Start Timestamp = 200) begins and reads the `Balance`.
    *   *Result:* The MVCC system finds the most recent committed version, which is now V2. `T3` reads `Balance = 1100`.

This example shows how MVCC provides **snapshot isolation**. `T1` had a consistent snapshot from time 100, while `T3` had a newer snapshot from time 200.

## 4. Advantages and Disadvantages

### Advantages:
*   **High Read Concurrency:** Read operations never block write operations and vice-versa. This is its biggest strength.
*   **No Read Locks:** Eliminates the need for read locks, reducing overhead.
*   **Avoids Deadlocks:** Since readers don't take locks, many common deadlock scenarios are eliminated.
*   **Consistent Snapshots:** Provides each transaction with a consistent view of the database for the duration of its execution.

### Disadvantages:
*   **Overhead of Version Storage:** Maintaining multiple versions consumes more storage space.
*   **Garbage Collection Overhead:** The need to clean up old versions adds computational overhead.
*   **Potential for "Write Skew":** A phenomenon that can occur under snapshot isolation where two concurrent transactions make decisions based on the same snapshot, leading to a state that might not have been serializable. Advanced MVCC implementations (like in PostgreSQL) have techniques to detect and prevent this.

## 5. Key Points / Summary

*   **MVCC** is a concurrency control method that maintains multiple physical versions of a single logical data item.
*   Its primary goal is to allow **high-concurrency reads** without blocking writes by providing **snapshot isolation**.
*   Each transaction sees a **consistent snapshot** of the database as it existed at the transaction's start time.
*   **Read operations** find the latest version committed before they began. **Write operations** create new versions.
*   **Advantages:** Increased concurrency, no read locks, avoidance of many deadlocks.
*   **Disadvantages:** Increased storage and maintenance overhead due to versioning and garbage collection.
*   MVCC is a foundational technology for modern databases like **PostgreSQL, Oracle, and MySQL (InnoDB)**.