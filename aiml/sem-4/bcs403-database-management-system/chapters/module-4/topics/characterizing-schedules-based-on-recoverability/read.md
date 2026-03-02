# Characterizing Schedules Based on Recoverability (DBMS)

## Introduction

In a multi-user Database Management System (DBMS), multiple transactions are executed concurrently to improve system throughput and resource utilization. However, this concurrency can lead to inconsistencies if not properly controlled. A **schedule** is a sequence of operations (read, write, commit, abort) from multiple transactions. A critical property of any schedule is its **recoverability**—the ability to recover the database to a consistent state after a transaction fails. This module explores how to characterize schedules based on their recoverability properties.

## Core Concepts

### 1. Recoverable Schedule (RC)

A schedule is **recoverable** if, for every pair of transactions `T_i` and `T_j`, if `T_j` reads a data item previously written by `T_i`, then the commit of `T_i` must appear *before* the commit of `T_j`.

*   **Why?** If `T_j` commits first and `T_i` subsequently fails and aborts, `T_j` would have read a value that was never truly committed to the database (a "dirty read"). This makes recovery impossible because we cannot reverse the commit of `T_j`.

**Example of a Recoverable Schedule:**

| T1        | T2        |
| :-------- | :-------- |
| `read(A)` |           |
| `write(A)`|           |
|           | `read(A)` |
| **`commit`** |           |
|           | `write(B)`|
|           | **`commit`** |

This schedule is recoverable because `T2` reads `A` from `T1`, and `T1` commits *before* `T2` commits.

---

### 2. Cascadeless Schedule (Avoiding Cascaded Rollbacks)

A recoverable schedule is **cascadeless** (also called *avoiding cascaded rollbacks*) if, for every pair of transactions `T_i` and `T_j`, if `T_j` reads a data item written by `T_i`, then the commit of `T_i` must appear *before* that read operation of `T_j`.

*   **Why?** This stricter property prevents a **cascading rollback**. If `T_i` writes a value and `T_j` reads it, and then `T_i` aborts, `T_j` must also be aborted because it used uncommitted (and now invalid) data. If `T_j` was already committed or had other dependent transactions, the rollback would "cascade," causing significant performance overhead and complexity.

**Example of a Cascadeless Schedule:**

| T1        | T2        |
| :-------- | :-------- |
| `read(A)` |           |
| `write(A)`|           |
| **`commit`** |           |
|           | `read(A)` |
|           | `write(B)`|
|           | **`commit`** |

This schedule is cascadeless. `T2` reads `A` only *after* `T1` has committed. If `T1` were to abort at any point before its commit, it would not affect `T2`.

**Counter-Example (Recoverable but NOT Cascadeless):**

| T1        | T2        |
| :-------- | :-------- |
| `read(A)` |           |
| `write(A)`|           |
|           | `read(A)` |  // T2 reads uncommitted data from T1
| **`commit`** |           |
|           | **`commit`** |

This schedule is recoverable (`T1` commits before `T2`). However, it is **not** cascadeless. If `T1` had aborted *after* `T2` performed the `read(A)`, `T2` would have to be rolled back as well, causing a cascade.

---

### 3. Strict Schedule

A schedule is **strict** if, for every pair of transactions `T_i` and `T_j`, if `T_j` reads *or writes* a data item previously written by `T_i`, then the commit *or abort* of `T_i` must appear *before* that read or write operation of `T_j`.

*   **Why?** This is the most restrictive and safest property. It ensures that no transaction can read or overwrite the uncommitted data of another transaction. This greatly simplifies recovery. When a transaction aborts, we can simply restore the values of all data items it wrote to their **before images** (the value they held before `T_i` started), without worrying about other transactions having seen or modified those values.

**Example of a Strict Schedule:**

| T1        | T2        |
| :-------- | :-------- |
| `read(A)` |           |
| `write(A)`|           |
| **`commit`** |           |
|           | `read(A)` | // Both read and write are
|           | `write(A)`| // performed only after T1 commits

This schedule is strict. `T2` does not interact with any data item touched by `T1` until after `T1` has committed.

## Summary and Key Points

| Property          | Rule                                                                                                | Prevents                                    | Strictness Level |
| :---------------- | :-------------------------------------------------------------------------------------------------- | :------------------------------------------ | :--------------- |
| **Recoverable (RC)**  | If `T_j` reads `T_i`'s write, `T_i` must commit **before `T_j` commits**.                          | Irrecoverable states after commit.          | Least Strict     |
| **Cascadeless**   | If `T_j` reads `T_i`'s write, `T_i` must commit **before `T_j` reads**.                            | Cascading rollbacks.                        | More Strict      |
| **Strict**        | If `T_j` reads **or writes** `T_i`'s write, `T_i` must commit/abort **before `T_j`'s operation**. | Complex recovery; allows simple undo.       | Most Strict      |

**Hierarchy:** Every **strict** schedule is **cascadeless**, and every **cascadeless** schedule is **recoverable**. The converse is not true.

**Practical Implication:** Database systems aim to generate **strict** schedules (often via **strict two-phase locking**) as they offer the simplest and most efficient recovery mechanism, which is crucial for practical system design.