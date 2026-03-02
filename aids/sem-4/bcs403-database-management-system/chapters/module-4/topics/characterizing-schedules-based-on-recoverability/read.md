# Module 4: Transaction Management - Characterizing Schedules Based on Recoverability

## Introduction

In a multi-user Database Management System (DBMS), a **schedule** represents the chronological order in which the operations (read/write) of multiple transactions are executed. Not all schedules are created equal. Some schedules, while yielding a correct final state, can lead to inconsistencies if a transaction fails and must be aborted. **Recoverability** is a fundamental property of a schedule that ensures we can recover the database to a consistent state after a transaction failure, without causing a **cascading rollback**. This module delves into the different classes of schedules based on their recoverability properties.

## Core Concepts

### 1. Recoverable Schedule (RC)

A schedule is **recoverable** if, for every pair of transactions `T_i` and `T_j`, where `T_j` reads a data item previously written by `T_i` (i.e., a **read-after-write** dependency), `T_i` commits *before* `T_j` commits.

*   **Why is this important?** If `T_j` reads a value written by `T_i` and then commits, but later `T_i` is aborted, we have a problem. The value read by `T_j` (and potentially used in its calculations) was never officially part of the database. If we simply abort `T_i`, `T_j` has become dependent on an uncommitted, now-rolled-back change, making `T_j`'s commit invalid. To fix this, we would have to abort `T_j` as well, leading to a cascading rollback. A recoverable schedule prevents this by ensuring the writer (`T_i`) commits first.

**Example of a Recoverable Schedule:**
| T1          | T2          |
| :---------- | :---------- |
| `read(A)`   |             |
| `write(A)`  |             |
|             | `read(A)`   | // T2 reads value written by T1
| `commit`    |             | // T1 commits *first*
|             | `commit`    | // Then T2 commits. This is safe.

### 2. Cascadeless Schedule (Avoids Cascading Rollbacks)

A stricter, more desirable form is a **cascadeless schedule** (also called an **ACA** - Avoids Cascading Aborts schedule). A schedule is cascadeless if, for every pair of transactions `T_i` and `T_j`, where `T_j` reads a data item written by `T_i`, `T_j`'s read operation occurs *after* `T_i` has committed.

*   **Why is this important?** It completely eliminates the possibility of a cascading rollback. A transaction only ever reads committed data. Therefore, if a transaction aborts, no other transaction that has already read its values will need to be rolled back. This simplifies recovery and improves system performance.

**Example of a Cascadeless Schedule:**
| T1          | T2          |
| :---------- | :---------- |
| `read(A)`   |             |
| `write(A)`  |             |
| `commit`    |             | // T1 commits first
|             | `read(A)`   | // T2 reads *only after* T1 commits
|             | `commit`    |

**Contrast with a Non-Cascadeless (but Recoverable) Schedule:**
The previous Recoverable Schedule example is actually *not* cascadeless because T2 read an uncommitted value from T1. It was recoverable only because T1 committed successfully. If T1 had failed after T2's read, T2 would also need to be aborted (a cascading rollback).

### 3. Strict Schedule

The strictest form of recoverability is a **strict schedule**. A schedule is strict if, for every pair of transactions `T_i` and `T_j`, where `T_j` writes to a data item previously written by `T_i` (a **write-after-write** dependency), `T_i` commits or aborts *before* `T_j`'s write operation.

*   **Why is this important?** It simplifies recovery even further. It ensures that an uncommitted transaction's writes are not overwritten by another transaction. If `T_i` is aborted, the recovery manager can simply restore the before-image of the data items `T_i` wrote. It doesn't have to worry about a subsequent transaction `T_j` having already overwritten that value, which would make the simple restoration incorrect.

**Example of a Strict Schedule:**
| T1          | T2          |
| :---------- | :---------- |
| `read(A)`   |             |
| `write(A)`  |             | // T1 writes A
|             | `write(A)`  | // **This is NOT allowed until T1 commits/aborts**
| `commit`    |             |
|             | `write(A)`  | // Now T2 can write A
|             | `commit`    |

## Key Points & Summary

| Property           | Definition & Requirement                                                                                                | Prevents Cascading Rollback? | Simplifies Recovery? |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------- | :--------------------------: | :------------------: |
| **Recoverable (RC)**  | `T_j` reads value written by `T_i` ⇒ `commit(T_i)` < `commit(T_j)`                                                          |             ❌              |          ✅          |
| **Cascadeless (ACA)** | `T_j` reads value written by `T_i` ⇒ `commit(T_i)` < `read(T_j)`                                                            |             ✅              |          ✅          |
| **Strict**         | `T_j` writes value written by `T_i` ⇒ `commit/abort(T_i)` < `write(T_j)`                                                    |             ✅              |          ✅✅         |

*   **Hierarchy:** Strict ⊂ Cascadeless ⊂ Recoverable. Every strict schedule is cascadeless, and every cascadeless schedule is recoverable. The reverse is not true.
*   **Importance:** These properties are crucial for designing concurrency control protocols and recovery algorithms. A DBMS aims for at least recoverable schedules, but preferably strict schedules, to ensure database consistency and simplify the recovery process after a system failure.
*   The **recovery manager** of a DBMS relies on these properties to determine the correct undo and redo actions during a restart from failure.