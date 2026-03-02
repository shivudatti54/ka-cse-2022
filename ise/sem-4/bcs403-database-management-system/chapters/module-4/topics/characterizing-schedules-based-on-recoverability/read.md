# Characterizing Schedules Based on Recoverability

## Introduction

In a multi-user Database Management System (DBMS), a **schedule** represents the chronological order in which the operations (read, write, commit, abort) of concurrent transactions are executed. If a transaction fails, it is crucial that its effects can be properly undone without causing database inconsistencies. **Recoverability** is a fundamental property of a schedule that guarantees this. It ensures that for every pair of transactions `Ti` and `Tj`, if `Tj` reads a data item written by `Ti`, then the commit of `Ti` must precede the commit of `Tj`. This module explores how to characterize schedules based on their recoverability.

## Core Concepts

### 1. Recoverable Schedule (RC)

A schedule is **recoverable** if it ensures that a transaction only commits after all transactions whose changes it has read have also committed.

- **Why is this important?** Imagine if `Tj` reads a value written by `Ti` and then commits. If `Ti` later aborts, the value it wrote is rolled back. However, `Tj` has already committed based on that now-"non-existent" value, leading to a database state that reflects an update that never truly occurred. This is a form of inconsistency.
- **Rule:** A schedule is recoverable if, for every pair of transactions `Ti` and `Tj` such that `Tj` reads a data item written by `Ti`, the commit operation of `Ti` appears before the commit operation of `Tj`.

**Example of a Recoverable Schedule:**

| Time | Transaction T1 | Transaction T2          |
| :--- | :------------- | :---------------------- |
| t1   | `read(A)`      |                         |
| t2   | `write(A)`     |                         |
| t3   |                | `read(A)` // Dirty Read |
| t4   | **`commit`**   |                         |
| t5   |                | `write(B)`              |
| t6   |                | **`commit`**            |

This schedule is recoverable because `T2` performs a **dirty read** (it reads uncommitted data from `T1`), but it only commits _after_ `T1` has committed. If `T1` had aborted at t4, `T2` could also be aborted (cascaded rollback) before it commits, making the schedule recoverable.

---

### 2. Cascadeless Schedule (Avoids Cascaded Rollbacks)

A stricter form of recoverability is the **cascadeless schedule** (also called _Avoids Cascaded Rollbacks_). A schedule is cascadeless if transactions only read data items that have been written by committed transactions. This prevents the problem of **cascading rollbacks**, where aborting one transaction forces other transactions that read its uncommitted data to also be aborted.

- **Rule:** A schedule is cascadeless if, for every pair of transactions `Ti` and `Tj` such that `Tj` reads a data item written by `Ti`, the read operation of `Tj` is performed _after_ the commit operation of `Ti`.

**Example of a Cascadeless Schedule:**

| Time | Transaction T1 | Transaction T2          |
| :--- | :------------- | :---------------------- |
| t1   | `read(A)`      |                         |
| t2   | `write(A)`     |                         |
| t3   | **`commit`**   |                         |
| t4   |                | `read(A)` // Clean Read |
| t5   |                | `write(B)`              |
| t6   |                | **`commit`**            |

This schedule is cascadeless (and therefore also recoverable) because `T2` reads `A` only after `T1` has committed. If `T1` were to abort at any point before its commit, it would not affect `T2`.

---

### 3. Strict Schedule

The strictest category is a **strict schedule**. A schedule is strict if, for every pair of transactions `Ti` and `Tj`, a `read` or `write` operation on a data item by `Tj` is allowed only _after_ the transaction `Ti` that last wrote that data item has committed or aborted _and_ the abort has been undone.

- **Rule:** A schedule is strict if, for every pair of transactions `Ti` and `Tj`, if `Tj` performs a `read(X)` or `write(X)` after `Ti` has performed a `write(X)`, then the commit or abort of `Ti` must precede this operation by `Tj`.
- **Benefit:** This simplifies recovery procedures significantly. When a transaction aborts, the recovery manager can simply restore the before-images (the old values) of all its writes. It doesn't need to worry about other transactions that might have read or overwritten those values, because no such operations were allowed to occur.

**Example of a Strict Schedule:**

| Time | Transaction T1 | Transaction T2 |
| :--- | :------------- | :------------- |
| t1   | `read(A)`      |                |
| t2   | `write(A)`     |                |
| t3   | **`commit`**   |                |
| t4   |                | `write(A)`     |
| t5   |                | **`commit`**   |

This schedule is strict because `T2` performs its `write(A)` only after `T1` (the last writer of `A`) has committed.

## Key Points & Summary

| Property              | Rule                                                                                                | Prevents                                                                           | Hierarchy                           |
| :-------------------- | :-------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- | :---------------------------------- |
| **Recoverable (RC)**  | A transaction commits only after all transactions it read from have committed.                      | Inconsistency from committing based on uncommitted data that is later rolled back. | Least Restrictive                   |
| **Cascadeless (ACA)** | Transactions read only data written by committed transactions.                                      | Cascading rollbacks, improving system performance and simplicity.                  | More Restrictive than RC            |
| **Strict**            | Transactions read or write data items only after the last transaction to write them has terminated. | Complex recovery operations; allows simple recovery using only before-images.      | Most Restrictive (Implies ACA & RC) |

**Hierarchy:** Every **strict** schedule is **cascadeless**, and every **cascadeless** schedule is **recoverable**. The converse is not true.
The goal of a concurrency control protocol is often to produce **strict** schedules, as they offer the strongest guarantees for both correctness (serializability) and recoverability.
