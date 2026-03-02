# Module 5: Validation Concurrency Control Techniques (Optimistic Methods)

## Introduction

In a multi-user Database Management System (DBMS), concurrency control is essential to ensure that concurrent transactions execute without interfering with each other, thereby preserving data consistency. While locking-based protocols (like Two-Phase Locking) are pessimistic—assuming conflicts are likely and preventing them upfront—**Validation Concurrency Control**, also known as **Optimistic Concurrency Control (OCC)**, takes a different, optimistic approach. It assumes that transactions are unlikely to conflict and checks for conflicts only at the very end, just before a transaction commits.

This technique is highly effective in environments where the rate of data contention is low, such as in read-heavy databases or systems with distributed data.

## Core Concepts of Validation Techniques

The optimistic method does not require locks during the transaction execution. Instead, it validates a transaction's changes *after* it has finished its work but *before* its results are permanently written to the database. A transaction is allowed to commit only if it passes this validation phase; otherwise, it is rolled back and restarted.

The execution of a transaction under OCC is divided into three phases:

1.  **Read Phase:** The transaction executes, reading values from the database and performing computations. All write operations are performed on a temporary local copy of the data, not on the actual database. This ensures that other transactions cannot see its uncommitted changes.
2.  **Validation Phase:** When the transaction requests to commit, the DBMS checks if its execution has conflicted with any other concurrently executing transaction. This involves verifying that the data it read is still consistent.
3.  **Write Phase:** If the validation is successful, the transaction's temporary local writes are applied to the permanent database. If the validation fails, the transaction is aborted and must be restarted later.

### The Validation Test (Timestamp-Based)

A common implementation uses timestamps to track the order of transactions. Each transaction `T_i` is assigned a unique timestamp `TS(T_i)` at the beginning of its validation phase.

The validation test for a transaction `T_i` checks its activities against every other transaction `T_j` that has already successfully committed *after* `T_i` started its read phase. The validation for `T_i` succeeds if, for every such `T_j`, ONE of the following conditions is true:

1.  `T_j` completes its write phase before `T_i` starts its read phase. (They didn't overlap at all).
2.  The set of data items written by `T_j` does not intersect with the set of data items read by `T_i`, **AND** `T_j` completes its write phase before `T_i` starts its validation phase.

Condition 2 is the most critical. It states that if a later transaction `T_j` (which committed) wrote a data item that `T_i` read, then `T_i`'s read is no longer valid, and `T_i` must be aborted.

## Example Scenario

Let's consider two transactions:
*   **T₁:** Reads `A` and `B`, computes `C = A + B`, and writes `C`.
*   **T₂:** Reads `B`, increments it by 10, and writes `B` back.

Their execution might be interleaved as follows:

| Time | Transaction T₁                     | Transaction T₂                     | DB State (A, B, C) |
| :--- | :---------------------------------- | :--------------------------------- | :----------------- |
| t1   | **Start**                           |                                    | (10, 20, 0)        |
| t2   | Read A (=10) → private copy        |                                    |                    |
| t3   | Read B (=20) → private copy        |                                    |                    |
| t4   |                                     | **Start**                          |                    |
| t5   |                                     | Read B (=20) → private copy        |                    |
| t6   |                                     | Write B' = 20 + 10 = 30 (local)   |                    |
| t7   |                                     | **Validation & Commit (success)**  |                    |
| t8   |                                     | **Write Phase:** Write B=30        | (10, **30**, 0)    |
| t9   | Compute C = 10 + 20 = 30 (local)   |                                    |                    |
| t10  | Write C=30 (local)                  |                                    |                    |
| t11  | **Begin Validation for T₁**         |                                    |                    |

Now, during T₁'s validation phase (t11), the DBMS checks:
*   T₂ committed after T₁ started (t4 > t1).
*   T₂ wrote to data item `B`.
*   T₁ read data item `B`.
*   Therefore, the write set of T₂ `{B}` intersects with the read set of T₁ `{A, B}`.

This violates validation condition 2. **T₁'s validation fails**, and it is aborted and rolled back. This prevents the "incorrect" sum of `10 + 30 = 40` from being written to the database, maintaining consistency. T₁ must be restarted to read the new correct value of `B (30)`.

## Key Points & Summary

| Aspect | Description |
| :--- | :--- |
| **Philosophy** | Optimistic; assumes conflicts are rare. Checks for conflicts at the end (validation). |
| **Phases** | 1. **Read:** Execute and make local copies. <br> 2. **Validation:** Check for serializability conflicts. <br> 3. **Write:** Apply changes if validation succeeds. |
| **Advantages** | - No locking overhead during execution, leading to higher throughput in low-contention environments. <br> - Avoids deadlocks, as no locks are held. |
| **Disadvantages** | - costly rollbacks if validation frequently fails. <br> - Requires maintaining private workspaces for each transaction, increasing memory overhead. |
| **Suitable For** | Read-intensive databases, systems with low conflict rates (e.g., query-dominant workloads). |
| **Comparison with Locking** | **Pessimistic (Locking):** Prevents conflicts. **Optimistic (Validation):** Detects and resolves conflicts after they occur. |

**In summary,** Validation Concurrency Control is a non-locking technique that optimistically executes transactions and only checks for serializability violations at commit time. It is a powerful alternative to locking protocols in specific database environments.