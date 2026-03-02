# Concurrency Control: Timestamp Ordering Protocol

## 1. Introduction

In a multi-user Database Management System (DBMS), concurrent execution of transactions is essential for performance and throughput. However, this concurrency can lead to inconsistencies if not controlled properly. The **Timestamp Ordering Protocol** is a fundamental concurrency control technique that ensures serializability without requiring locks. Instead, it uses timestamps to dictate the order in which transactions are allowed to access data items, thereby preventing conflicts and ensuring a serializable schedule.

## 2. Core Concepts

### What is a Timestamp?
A timestamp is a unique identifier assigned to each transaction at the moment it begins. This is typically a simple, monotonically increasing value derived from the system clock or a logical counter (e.g., `TS(Ti)` for transaction `Ti`). The timestamp represents the transaction's "age"; an older transaction (with a lower timestamp) should appear to have executed before a younger one (with a higher timestamp).

### The Basic Principle
The protocol's core principle is straightforward: **If transaction Ti issues a request to read or write a data item Q, the operation is allowed only if it follows the timestamp order of the last transaction that successfully read or wrote Q.** If it violates this order, the transaction is rolled back (aborted) and restarted with a new, larger timestamp.

Two timestamps are associated with each data item `Q`:
*   **R-Timestamp(Q):** The largest timestamp of any transaction that has successfully read `Q`.
*   **W-Timestamp(Q):** The largest timestamp of any transaction that has successfully written `Q`.

### The Rules of the Protocol
For a transaction `Ti` with timestamp `TS(Ti)`:

#### 1. Read Rule
When `Ti` issues a `read(Q)` operation:
*   If `TS(Ti) < W-Timestamp(Q)`, it means a younger transaction has already written `Q`. Therefore, `Ti`'s read would be invalid as it should have read the older value. `Ti` is **aborted and restarted**.
*   Otherwise, the `read` operation is executed.
    *   `R-Timestamp(Q)` is set to `max(R-Timestamp(Q), TS(Ti))`.

#### 2. Write Rule
When `Ti` issues a `write(Q)` operation:
*   If `TS(Ti) < R-Timestamp(Q)`, it means a younger transaction has already read the current value of `Q`. Allowing `Ti` to write would make that previous read invalid. `Ti` is **aborted and restarted**.
*   If `TS(Ti) < W-Timestamp(Q)`, it means a younger transaction has already written `Q`. `Ti`'s write is essentially obsolete and is **ignored**. This is called the **Thomas Write Rule**. It allows some view-serializable schedules that are not conflict-serializable but avoids unnecessary aborts. (Without this rule, `Ti` would be aborted).
*   Otherwise, the `write` operation is executed.
    *   `W-Timestamp(Q)` is set to `TS(Ti)`.

## 3. Example

Let's consider two transactions and a data item `X`. Assume initial `R-TS(X)=0` and `W-TS(X)=0`.

*   **Transaction T1** (TS=10): Reads and then writes to `X`.
*   **Transaction T2** (TS=20): Reads and then writes to `X`.

**Scenario 1: Correct Order (T1 then T2)**
1.  `T1` issues `read(X)`. `TS(T1)=10 > W-TS(X)=0`. Read allowed.
    *   `R-TS(X) = max(0, 10) = 10`
2.  `T1` issues `write(X)`. `TS(T1)=10 > R-TS(X)=10`? No, it's equal. `10 > W-TS(X)=0`. Write allowed.
    *   `W-TS(X) = 10`
3.  `T2` issues `read(X)`. `TS(T2)=20 > W-TS(X)=10`. Read allowed.
    *   `R-TS(X) = max(10, 20) = 20`
4.  `T2` issues `write(X)`. `TS(T2)=20 > R-TS(X)=20`? No, it's equal. `20 > W-TS(X)=10`. Write allowed.
    *   `W-TS(X) = 20`
*Schedule is serializable (T1 -> T2). No aborts.*

**Scenario 2: Incorrect Order (T2 then T1) - A Conflict**
1.  `T2` (TS=20) issues `write(X)`. Allowed. `W-TS(X)=20`.
2.  `T1` (TS=10) *now* issues `read(X)`.
    *   Check: `TS(T1)=10 < W-TS(X)=20`. **VIOLATION!**
    *   `T1` is **aborted and restarted** with a new, larger timestamp.
*The protocol prevents a non-serializable schedule by aborting the older transaction that arrived late.*

## 4. Key Points & Summary

| Aspect | Description |
| :--- | :--- |
| **Goal** | To ensure conflict serializability without using locks. |
| **Mechanism** | Uses timestamps to order transactions and enforce serializability. Operations that violate the timestamp order cause the transaction to be aborted. |
| **Pros** | **No deadlocks.** Since no locks are held, the system cannot enter a deadlock state. |
| **Cons** | **Cascading Rollbacks** are possible. If `Tj` reads a value written by `Ti` and `Ti` is later aborted, `Tj` must also be aborted (though this can be mitigated). Can also lead to **starvation** for older transactions. |
| **Thomas Write Rule** | An optimization that ignores obsolete writes instead of aborting the transaction, improving efficiency. |
| **Contrast with Locking** | Lock-Based protocols (e.g., 2PL) use blocking/waiting. Timestamp ordering uses rollbacks/restarts to resolve conflicts. |
| **Summary** | The Timestamp Ordering Protocol is a non-locking, pessimistic concurrency control method that uses timestamps to serialize transaction execution. It guarantees serializability by aborting transactions that violate the timestamp order, ensuring the database remains consistent in a concurrent environment. |