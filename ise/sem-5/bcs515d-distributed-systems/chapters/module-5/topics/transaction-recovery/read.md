# Transaction Recovery in Distributed Systems

## Introduction to Transaction Recovery

Transaction recovery is a critical mechanism in distributed database systems that ensures **atomicity** and **durability** even when failures occur. In a distributed environment, where a transaction may involve multiple servers across a network, recovery becomes significantly more complex than in centralized systems. The primary goal is to maintain the **ACID properties** (Atomicity, Consistency, Isolation, Durability) across all participating sites, ensuring that either all operations of a transaction are permanently recorded, or none are, despite any partial failures.

When a failure occurs (e.g., site crash, network partition, disk failure), the system must be able to restore itself to a consistent state. Recovery procedures involve techniques to **undo** the effects of incomplete transactions and **redo** the effects of committed transactions that may not have been fully written to persistent storage.

## Key Concepts in Transaction Recovery

### 1. Log-Based Recovery

The most common technique for recovery is maintaining a **log** – a sequential, append-only file that records all significant actions performed by transactions. Each server in the distributed system maintains its own **local log**.

**Types of Log Records:**

- **`<T_i, start>`**: Transaction T_i has started.
- **`<T_i, commit>`**: Transaction T_i has committed.
- **`<T_i, abort>`**: Transaction T_i has been aborted.
- **`<T_i, X, old_value, new_value>`**: Transaction T_i has updated data item X from `old_value` to `new_value`. This is a **write-ahead log (WAL)** record.

**The Write-Ahead Log (WAL) Protocol:**
Before any data page is written to the database on disk, the log records corresponding to the changes on that page _must_ be written to stable storage (the log). This ensures that if a crash occurs, we have a record of the change to either redo it or undo it.

```
[Transaction T1 updates X from 10 to 20]
1. Log Record Written: <T1, X, 10, 20>  --> Written to stable storage log
2. Database Updated: X = 20 in the database  --> Can be written to disk (may be cached)
```

### 2. Checkpointing

Periodically taking a **checkpoint** reduces the amount of log that must be processed during recovery. A checkpoint is a point at which the system forces all dirty data pages (modified in memory but not on disk) to be written to the database. The log records the checkpoint.

```
[Checkpoint Process]
1. System halts temporarily.
2. Writes a <checkpoint> record to the log, followed by a list of all active transactions.
3. Forces all modified buffer pages and the log to stable storage.
4. Resumes normal operation.
```

During recovery, the system only needs to consider transactions that were active _at the time of the last checkpoint_ or that started _after_ the checkpoint.

### 3. Recovery Algorithms: Undo and Redo

The recovery process consists of two main phases:

- **Redo Phase:** Repeating all actions that were completed (committed) but whose effects might not have been saved to the durable database. We redo from the last checkpoint or from the earliest log record of an uncommitted transaction.
- **Undo Phase:** Reversing the actions of any transactions that had not committed at the time of the failure. We use the `old_value` from the log records to restore data items.

## Recovery in a Distributed Context: The Two-Phase Commit Protocol (2PC)

The recovery of a distributed transaction is intrinsically linked to its commit protocol. The **Two-Phase Commit (2PC) protocol** is fundamental and ensures atomicity, meaning all participants either commit or all abort. Recovery procedures must handle the failure of participants and the coordinator.

### Role of the Log in 2PC

Each participant and the coordinator must write log records to stable storage to enable recovery from failures.

**Coordinator Logs:**

- **`<prepare T>`**: Decision to initiate the commit process for T.
- **`<commit T>`** or **`<abort T>`**: The final decision.

**Participant Logs:**

- **`<ready T>`**: Participant is prepared to commit and has locked resources.
- **`<commit T>`** or **`<abort T>`**: Records the final outcome.

These logs are crucial. If a participant crashes after voting "yes" (`<ready T>`), upon recovery, it must contact the coordinator or other participants to discover the outcome and act accordingly. It cannot unilaterally decide to abort.

### State Transitions and Recovery

The table below shows the states a participant can be in during 2PC and the recovery action required if a crash occurs in that state.

| Participant State    | Log Record Written | Meaning                                              | Recovery Action after Crash                                                                                              |
| -------------------- | ------------------ | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Initial**          | None               | Working on transaction                               | Simply abort the transaction. No `ready` record means no commitment.                                                     |
| **Ready** (Prepared) | `<ready T>`        | Has voted "yes", is prepared to commit, holds locks. | Must become **blocked**. It contacts the coordinator (or other participants) to **discover the outcome** (commit/abort). |
| **Committed**        | `<commit T>`       | Has received and executed the commit command.        | **Redo** the transaction's effects. The commit is durable.                                                               |
| **Aborted**          | `<abort T>`        | Has received or unilaterally decided to abort.       | **Undo** the transaction's effects.                                                                                      |

**Recovery Scenario Example:**

1.  Participant P1 votes "yes" and writes `<ready T>` to its log.
2.  Coordinator collects all votes, decides to commit, and writes `<commit T>`.
3.  Coordinator sends `commit` message to all participants.
4.  Participant P2 receives the message, commits, and writes `<commit T>`.
5.  **Participant P1 crashes** _after_ writing `<ready T>` but _before_ receiving the `commit` message.
6.  Upon recovery, P1 examines its log and finds the `<ready T>` record. It knows it voted "yes" but doesn't know the outcome.
7.  P1 must now **block** and initiate a recovery procedure. It will contact the coordinator or other participants to ask, "What was the decision for T?"
8.  Once it discovers the decision was `commit`, it will write `<commit T>` to its log and perform the commit操作.

This blocking state is a disadvantage of 2PC. A participant remains blocked, holding locks on data items, until it can discover the transaction's outcome.

### Three-Phase Commit (3PC) and Non-Blocking Recovery

3PC is designed to avoid the blocking problem of 2PC. It introduces an extra phase between voting and commit/abort to ensure that if the coordinator fails, participants can communicate among themselves to reach a decision without being blocked indefinitely. While more resilient, 3PC involves more message overhead and is less commonly used in practice.

## Comparison of Recovery Protocols

| Feature                 | Two-Phase Commit (2PC)                       | Three-Phase Commit (3PC)                               |
| ----------------------- | -------------------------------------------- | ------------------------------------------------------ |
| **Message Rounds**      | 2 ( voting + decision)                       | 3 ( voting + pre-commit + decision)                    |
| **Blocking**            | Yes, if coordinator fails after `prepare`    | Non-blocking                                           |
| **Recovery Complexity** | Medium (participants must query for outcome) | High (requires more complex participant communication) |
| **Practical Use**       | Very common, the de facto standard           | Rare, due to overhead and complexity                   |

## Implementation: Shadow Copies vs. Logging

While logging is the industry standard, another historical approach is **shadow copies** (or shadow paging).

- **Logging:** Changes are recorded in a log. The database is updated in place. Recovery uses the log to redo/undo.
- **Shadow Copies:** A transaction creates a shadow (copy) of the pages it modifies. The original pages are untouched. On commit, the shadow pages become the new current pages via a single atomic update of a master pointer.

```
        Master Pointer
             |
        [Current Database Pages]
             |
    T1 creates shadow copies and modifies them.
             |
        [Current Database Pages]   [Shadow Pages (T1's changes)]
             |
    On commit, atomically update Master Pointer to point to shadow pages.
             |
        [Old Pages (now free)]      [Shadow Pages (now current)]
```

This method avoids the need for a redo phase but has high overhead for large transactions and is inefficient for distributed systems. Logging is more versatile and performant.

## Conclusion

Transaction recovery is the safety net of distributed transactions. It relies on persistent logging and well-defined protocols like 2PC to ensure the system can always return to a consistent state. Understanding the interplay between the commit protocol and the recovery process is essential for designing and managing robust distributed systems.

---

## Exam Tips

- **Focus on Logging:** Always remember the cardinal rule: **Log before you change the database** (Write-Ahead Logging).
- **Link 2PC and Recovery:** You cannot discuss recovery of distributed transactions without mentioning 2PC. The log records (`ready`, `commit`, `abort`) are the key to the entire process.
- **Understand Blocking:** Be able to explain _why_ a participant in 2PC becomes blocked after a crash and what it must do to recover. This is a classic exam question.
- **Compare and Contrast:** Be prepared to discuss the trade-offs between 2PC and 3PC, especially regarding blocking and message complexity.
- **Use the Terminology Correctly:** Precisely use terms like `redo`, `undo`, `checkpoint`, `stable storage`, `blocked state`, and `atomic commit`.
