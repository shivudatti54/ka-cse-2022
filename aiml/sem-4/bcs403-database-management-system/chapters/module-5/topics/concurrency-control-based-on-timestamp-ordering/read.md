# Concurrency Control: Timestamp Ordering Protocol

## Introduction

In a multi-user Database Management System (DBMS), concurrency control protocols are essential to ensure that concurrent transactions execute without leading to a loss of database consistency. While locking-based protocols (like Two-Phase Locking) manage concurrency by restricting access through locks, **Timestamp Ordering (TO)** is a fundamentally different, non-lock-based approach. It relies on timestamps to serialize transactions and prevent conflicts, ensuring a conflict-serializable schedule.

## Core Concepts

### 1. The Basic Idea

The Timestamp Ordering Protocol orders transactions based on their unique timestamps. A timestamp can be a unique identifier assigned to each transaction, typically based on the system clock or a logical counter when the transaction starts (e.g., `TS(T_i)`). The protocol ensures that for any two conflicting operations (read/write, write/read, or write/write) from different transactions, the order in which they are processed is consistent with the timestamp order of the transactions.

### 2. Timestamps and Data Items

For each data item `X` in the database, the system maintains two timestamps:

*   **R-timestamp(X):** The largest (i.e., most recent) timestamp of any transaction that has successfully **read** the data item `X`.
*   **W-timestamp(X):** The largest timestamp of any transaction that has successfully **written** the data item `X`.

These timestamps are updated whenever a read or write operation is successfully executed.

### 3. The Protocol Rules

For a transaction `T_i` with timestamp `TS(T_i)` issuing an operation on data item `X`, the protocol enforces the following rules:

#### a. Read Operation: `read_i(X)`
*   If `TS(T_i) < W-timestamp(X)`, it means a younger transaction (with a larger timestamp) has already written to `X`. Therefore, `T_i`'s read operation is too late; the value it would read has already been overwritten. This violates the timestamp order.
    *   **Action:** The read operation is **rejected**, and transaction `T_i` is **rolled back (aborted)** and restarted with a new, larger timestamp.
*   Else (if `TS(T_i) >= W-timestamp(X)`):
    *   The read operation is **executed**.
    *   `R-timestamp(X)` is set to `max(R-timestamp(X), TS(T_i))`.

#### b. Write Operation: `write_i(X)`
*   If `TS(T_i) < R-timestamp(X)`, it means a younger transaction has already read the value of `X` that `T_i` is now trying to overwrite. The younger transaction read a value that, in timestamp order, should not have existed yet.
    *   **Action:** The write operation is **rejected**, and `T_i` is **rolled back (aborted)**.
*   If `TS(T_i) < W-timestamp(X)`, it means a younger transaction has already written to `X`. `T_i`'s write is too late and is obsolete.
    *   **Action:** The write operation is **rejected**, and `T_i` is **rolled back (aborted)**.
*   Else (if `TS(T_i) >= R-timestamp(X)` and `TS(T_i) >= W-timestamp(X)`):
    *   The write operation is **executed**.
    *   `W-timestamp(X)` is set to `TS(T_i)`.

## Example

Let's consider two transactions and a data item `X`. Assume initial timestamps: `W-timestamp(X) = 0`, `R-timestamp(X) = 0`.

*   `T_100` (TS=100) begins.
*   `T_200` (TS=200) begins.

**Scenario 1: Violation of Write Rule**
1.  `T_200` issues `write_200(X)`. Since 200 > W-timestamp(X)(0), it is allowed. `W-timestamp(X)` becomes 200.
2.  `T_100` now issues `write_100(X)`. The protocol checks: `TS(T_100)=100` is *less than* the current `W-timestamp(X)=200`. This violates the rule.
3.  The `write_100(X)` operation is rejected, and transaction `T_100` is aborted and restarted.

**Scenario 2: Violation of Read Rule (Thomas' Write Rule)**
A common variation, called the **Thomas' Write Rule**, optimizes the protocol for increased concurrency. It ignores an obsolete write instead of aborting the transaction.

1.  `T_200` issues `write_200(X)`. `W-timestamp(X)` becomes 200.
2.  `T_100` issues `write_100(X)`. Under the basic rule, `T_100` would be aborted. However, Thomas' Write Rule recognizes that `T_100`'s write is obsolete because a younger transaction (`T_200`) has already written the value. This write has no impact on the database state and can be safely **ignored** (treated as a "no-op") without aborting `T_100`. This prevents unnecessary aborts.

## Key Points and Summary

| Aspect | Description |
| :--- | :--- |
| **Principle** | A non-lock-based, optimistic protocol that uses timestamps to order transactions and resolve conflicts. |
| **Mechanism** | Checks the timestamp of a transaction against the read/write timestamps of the data item for every operation. |
| **Conflict Resolution** | If an operation violates timestamp order, the transaction is **aborted and restarted** (given a new, larger timestamp). |
| **Advantages** | **1. Deadlock-Free:** Since no locks are used, the protocol cannot cause deadlocks. <br> **2. Potential for High Concurrency:** No waiting for locks; transactions proceed until a conflict is detected. |
| **Disadvantages** | **1. Suffers from Cascading Rollbacks:** An aborted transaction may have already read data used by other transactions, potentially causing them to also be aborted (though recoverable schedules can avoid this). <br> **2. Starvation:** A transaction might repeatedly conflict with younger transactions and keep getting aborted. <br> **3. Timestamp Management Overhead:** Maintaining and comparing timestamps for every operation adds computational cost. |
| **Strict TO** | A variant that delays read and write operations to ensure recoverability and avoid cascading rollbacks, making it similar to Strict 2PL in its effects but different in implementation. |

In conclusion, the Timestamp Ordering Protocol offers a deadlock-free alternative to locking. It is most effective in environments where conflicts are expected to be rare, as the cost of aborting and restarting transactions can be high if conflicts are frequent.