# Characterizing Schedules Based on Serializability

## Table of Contents

- [Characterizing Schedules Based on Serializability](#characterizing-schedules-based-on-serializability)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Transaction and Schedule Basics](#transaction-and-schedule-basics)
  - [Conflict Serializability](#conflict-serializability)
  - [Precedence Graph (Conflict Graph)](#precedence-graph-conflict-graph)
  - [View Serializability](#view-serializability)
  - [Recoverable Schedules](#recoverable-schedules)
- [Examples](#examples)
  - [Example 1: Testing Conflict Serializability](#example-1-testing-conflict-serializability)
  - [Example 2: Non-Serializable Schedule](#example-2-non-serializable-schedule)
  - [Example 3: Recoverability Analysis](#example-3-recoverability-analysis)
- [Exam Tips](#exam-tips)

## Introduction

In a database management system, multiple transactions often execute concurrently to improve system throughput and resource utilization. However, concurrent execution can lead to problems such as lost updates, uncommitted data, and inconsistent database states. The concept of serializability provides a theoretical foundation for determining whether a concurrent schedule of transactions produces correct results equivalent to some serial execution. This topic is crucial for understanding how database systems maintain data consistency and integrity while allowing concurrent operations. Serializability theory forms the backbone of concurrency control mechanisms used in modern database systems, including locking, timestamp-based, and optimistic protocols.

The study of serializability helps database administrators and system designers ensure that the interleaved execution of transactions does not violate the ACID properties, particularly Atomicity, Consistency, and Isolation. By characterizing schedules based on their serializability properties, we can identify which concurrent executions are safe and which may lead to erroneous results. This understanding is essential for implementing robust concurrency control mechanisms and for analyzing transaction schedules in real-world database applications.

## Key Concepts

### Transaction and Schedule Basics

A **transaction** is a logical unit of work that transforms the database from one consistent state to another. Each transaction consists of a sequence of read and write operations on database items. A **schedule** (or history) is a chronological sequence of operations from all participating transactions, showing the interleaved execution order.

A **serial schedule** is one where transactions execute one after another without any interleaving—either all operations of T1 complete before T2 starts, or vice versa. Serial schedules always maintain database consistency because each transaction sees a consistent state. However, they offer poor performance due to limited concurrency.

A **non-serial schedule** allows interleaving of operations from different transactions, which improves throughput but requires careful management to prevent inconsistencies.

### Conflict Serializability

Two operations are said to **conflict** if they operate on the same data item and at least one of them is a write operation. There are three types of conflicts:

1. **Read-Write Conflict (RW)**: One transaction reads a data item while another writes it
2. **Write-Read Conflict (WR)**: One transaction writes a data item while another reads it
3. **Write-Write Conflict (WW)**: Both transactions write to the same data item

A schedule is **conflict serializable** if it can be transformed into a serial schedule by swapping pairs of non-conflicting operations. The key insight is that swapping non-conflicting operations does not change the final outcome of any transaction.

### Precedence Graph (Conflict Graph)

The **precedence graph** (also called conflict graph or serializability graph) is a directed graph used to test conflict serializability. For a schedule S, the precedence graph contains:

- A node for each transaction that has operations in the schedule
- A directed edge from Ti to Tj (Ti → Tj) if Ti performs an operation that conflicts with an operation of Tj, and Ti's operation appears before Tj's operation in the schedule

A schedule is conflict serializable if and only if its precedence graph is **acyclic** (contains no cycles). If the graph is acyclic, a topological ordering of the nodes gives an equivalent serial schedule.

### View Serializability

**View serializability** is a broader notion than conflict serializability. A schedule is view-serializable if it is view-equivalent to some serial schedule. Two schedules are view-equivalent if:

1. Each transaction reads the same initial values in both schedules
2. Each transaction writes the same final values in both schedules
3. Each transaction performs the final write to each data item

Every conflict serializable schedule is view-serializable, but the converse is not true. Some view-serializable schedules are not conflict serializable (containing blind writes). Testing for view serializability is NP-complete in general, making it impractical for most database systems.

### Recoverable Schedules

A schedule is **recoverable** if a transaction commits only after all transactions whose changes it has read have committed. In other words, if Tj reads a value written by Ti, then Ti must commit before Tj commits. Recoverable schedules ensure that database can be recovered to a consistent state after a failure.

A schedule is **cascadeless** (or avoid cascading aborts) if a transaction reads only values written by committed transactions. Cascadeless schedules are a subset of recoverable schedules and prevent cascading rollbacks.

## Examples

### Example 1: Testing Conflict Serializability

Consider the schedule S1:

```
T1: R(X) W(X)
 T2: R(Y) W(Y)
```

**Step 1: Identify conflicting operations**

- T1 reads X, T2 writes X - No conflict (T2 doesn't access X)
- T1 reads Y - No conflict (T1 doesn't access Y)
- T1 writes X, T2 reads Y - No conflict (different items)
- T1 writes X, T2 writes Y - No conflict

Actually, let me reconsider with a better schedule:

S1: T1:R(X) W(X) T2:R(X) W(X)

Conflicting pairs:

- T1:W(X) and T2:R(X) - RW conflict
- T1:W(X) and T2:W(X) - WW conflict

**Step 2: Construct precedence graph**

- Edge from T1 to T2 (T1 writes X before T2 reads X)
- Edge from T1 to T2 (T1 writes X before T2 writes X)

**Step 3: Check for cycles**
The graph has nodes {T1, T2} with edge T1→T2. No cycle exists.

**Conclusion**: S1 is conflict serializable. An equivalent serial schedule could be T1, T2.

### Example 2: Non-Serializable Schedule

Consider the schedule S2:

```
T1: R(X) W(Y)
T2: R(Y) W(X)
```

**Conflicting operations:**

- T1:R(X) and T2:W(X) - WR conflict
- T1:W(Y) and T2:R(Y) - WR conflict

**Precedence graph:**

- Edge T1→T2 (T1 reads X before T2 writes X)
- Edge T2→T1 (T2 reads Y before T1 writes Y)

This creates a cycle: T1→T2→T1

**Conclusion**: S2 is NOT conflict serializable. The interleaving can lead to inconsistent results.

### Example 3: Recoverability Analysis

Schedule S3:

```
T1: R(X) W(X) Abort
T2: R(X) Commit
```

This schedule is NOT recoverable because T2 reads X written by T1, and T2 commits before T1 commits (T1 eventually aborts). If T1 rolls back, T2 has already committed a transaction based on uncommitted data.

A recoverable version would require T2 to wait until T1 commits or aborts before committing.

## Exam Tips

1. **Remember the precedence graph test**: A schedule is conflict serializable if and only if its precedence graph is acyclic—this is the most frequently tested concept.

2. **Know the conflict types**: RW, WR, and WW conflicts—practice identifying conflicting operations in schedules.

3. **Distinguish conflict vs. view serializability**: Conflict serializability is easier to test (polynomial time) while view serializability is NP-complete.

4. **Cascadeless implies recoverable**: Remember that cascadeless schedules are always recoverable, but not vice versa.

5. **Serial schedules are always serializable**: A serial schedule with n transactions has n! possible orderings, all of which are serializable.

6. **Blind writes**: Transactions that write without reading first (blind writes) may create view-serializable but not conflict-serializable schedules.

7. **Drawing precedence graphs**: Practice drawing precedence graphs from schedules—label nodes with transactions and edges with the conflicting operations.

8. **Recovery terminology**: Memorize definitions of recoverable, cascadeless, and strict schedules for exam questions.
