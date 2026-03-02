# Two-Phase Locking (2PL) for Concurrency Control

## Introduction

In a multi-user Database Management System (DBMS), multiple transactions may execute concurrently to improve system performance and resource utilization. However, this concurrent execution can lead to several problems, such as **Lost Updates**, **Dirty Reads**, and **Inconsistent Retrievals**, if not controlled properly. Concurrency Control protocols are mechanisms to ensure that such anomalies are prevented, and the isolation property of transactions (the 'I' in ACID) is maintained. **Two-Phase Locking (2PL)** is one of the most fundamental and widely used _protocols_ for achieving serializability, which is the correct criterion for concurrency execution.

## Core Concepts of Two-Phase Locking

Two-Phase Locking is a protocol that governs how locks are acquired and released by transactions. A lock is a mechanism used to control access to a data item (e.g., a database row). There are two main types of locks:

- **Shared Lock (S-Lock):** Used for read operations. Multiple transactions can hold a shared lock on the same data item simultaneously, allowing concurrent reads.
- **Exclusive Lock (X-Lock):** Used for write operations. Only one transaction can hold an exclusive lock on a data item at any given time. It is exclusive of all other locks.

The fundamental rule of 2PL is that every transaction must acquire and release its locks in two distinct, non-overlapping phases:

### 1. The Growing Phase (First Phase)

In this phase, the transaction is allowed to **acquire** new locks on data items as needed (either S-locks for reading or X-locks for writing), but it **cannot release any lock**. The transaction can only grow its set of locks.

### 2. The Shrinking Phase (Second Phase)

In this phase, the transaction is allowed to **release** locks it has already acquired, but it **cannot acquire any new locks**. The transaction's set of locks can only shrink.

Once a transaction releases its first lock, it enters the shrinking phase and is barred from obtaining any further locks. This strict separation ensures that the transaction's actions are isolated in a way that guarantees serializability.

## How 2PL Works: An Example

Consider two transactions, T1 and T2, that want to access two data items, A and B.

- **Transaction T1:** `Read(A); A = A + 100; Write(A); Read(B); B = B + 100; Write(B);`
- **Transaction T2:** `Read(A); Read(B); Print(A+B);`

**Scenario without 2PL (Uncontrolled):** T2 might read A after T1 has updated it but before T1 updates B, leading to an inconsistent sum (a dirty read or incorrect summary).

**Scenario with 2PL (Controlled):**

1.  **T1 starts:** Acquires an X-lock on A (for writing).
2.  **T2 starts:** Tries to acquire an S-lock on A. Since T1 holds an X-lock, T2's request is denied, and it is forced to wait. This prevents a dirty read.
3.  **T1 continues:** Reads A, updates A, writes A. It then acquires an X-lock on B (it's still in its growing phase). It reads B, updates B, writes B.
4.  **T1's Shrinking Phase:** T1 has finished its operations. It now releases its locks, say first the lock on A and then on B. The moment it releases its first lock (on A), it enters the shrinking phase.
5.  **T2 Resumes:** Once T1 releases the X-lock on A, T2's previously queued request for an S-lock on A is granted. It reads A. It then requests an S-lock on B. Since T1 has already released the X-lock on B, T2 acquires it, reads B, and prints the consistent sum (A+B).

This locking and unlocking schedule, dictated by the 2PL protocol, ensures a serializable schedule equivalent to T1 executing completely before T2.

## Variations of 2PL

- **Strict Two-Phase Locking:** A crucial variation where a transaction **holds all its exclusive (X) locks until it commits or aborts**. This prevents other transactions from reading uncommitted data (dirty reads) and simplifies transaction recovery.
- **Rigorous Two-Phase Locking:** A stricter version where a transaction **holds all locks (both shared and exclusive) until it commits or aborts**. This generates schedules that are _strict_ and _serializable_.

## Key Points and Summary

| Key Point        | Description                                                                                                                     |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| **Purpose**      | To ensure serializability and isolation of concurrent transactions in a DBMS.                                                   |
| **Mechanism**    | Uses Shared (S) and Exclusive (X) locks on data items.                                                                          |
| **Two Phases**   | **Growing Phase:** Only acquire locks. **Shrinking Phase:** Only release locks.                                                 |
| **Guarantee**    | If all transactions follow 2PL, the schedule is guaranteed to be serializable.                                                  |
| **Drawbacks**    | **Can lead to deadlocks.** Transactions can wait cyclically for locks, requiring a deadlock detection and resolution mechanism. |
| **Strict 2PL**   | Holds all X-locks until commit/abort. Prevents dirty reads and cascading rollbacks. Commonly used in practice.                  |
| **Rigorous 2PL** | Holds all locks until commit/abort. Easiest to implement for recovery.                                                          |

**Summary:** Two-Phase Locking is a foundational concurrency control protocol that ensures correct execution of concurrent transactions by regulating lock acquisition and release into two distinct phases. While it guarantees serializability, it is not deadlock-free. Its practical variants, especially **Strict 2PL**, are extensively implemented in modern database systems due to their robustness and simplicity.
