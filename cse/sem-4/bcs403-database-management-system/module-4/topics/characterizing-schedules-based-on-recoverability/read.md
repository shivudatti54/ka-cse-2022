# Characterizing Schedules Based on Recoverability

## Table of Contents

- [Characterizing Schedules Based on Recoverability](#characterizing-schedules-based-on-recoverability)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Transaction Schedule](#transaction-schedule)
  - [Recoverability Issues](#recoverability-issues)
  - [Types of Schedules Based on Recoverability](#types-of-schedules-based-on-recoverability)
  - [Hierarchy of Recoverability](#hierarchy-of-recoverability)
  - [Testing for Recoverability](#testing-for-recoverability)
- [Examples](#examples)
  - [Example 1: Classifying a Schedule](#example-1-classifying-a-schedule)
  - [Example 2: Cascadeless Schedule Verification](#example-2-cascadeless-schedule-verification)
  - [Example 3: Constructing a Strict Schedule](#example-3-constructing-a-strict-schedule)
- [Exam Tips](#exam-tips)

## Introduction

In database management systems, multiple transactions often execute concurrently to improve system throughput and resource utilization. However, concurrent execution introduces critical challenges related to data consistency and the ability to recover from failures. When a transaction fails, it becomes essential to ensure that the database can be restored to a consistent state without leaving behind partial effects of failed transactions on other concurrent transactions. This leads to the fundamental concept of **recoverability** in transaction schedules.

Recoverability is a crucial property of schedules that ensures the database remains consistent even when transactions fail during execution. A schedule is recoverable if it guarantees that committed transactions do not need to be rolled back when a later transaction aborts. This topic is essential for understanding how database management systems maintain data integrity in concurrent environments. In this module, we will explore the classification of schedules based on recoverability, including recoverable schedules, cascadeless schedules, and strict schedules, along with their practical implications in DBMS implementation.

## Key Concepts

### Transaction Schedule

A **schedule** is a chronological sequence of operations from multiple transactions executing concurrently. Each schedule represents the order in which operations (read and write) are performed across all transactions. Schedules can be classified as serial or non-serial, with serial schedules executing transactions one after another, while non-serial schedules allow interleaving of operations from different transactions.

### Recoverability Issues

When transactions execute concurrently, a critical problem arises: if transaction T2 reads values written by transaction T1, and T1 aborts later, T2 has already used invalid data. This creates a situation where rolling back T1 becomes complicated because T2 may have already committed based on incorrect data. Recoverability addresses this fundamental issue by ensuring that such scenarios are prevented or handled properly.

### Types of Schedules Based on Recoverability

#### 1. Recoverable Schedules (RC)

A schedule is said to be **recoverable** if it satisfies the following condition: for every pair of transactions T_i and T_j, if T_j reads a data item previously written by T_i, then the commit operation of T_i must occur before the commit operation of T_j.

In simpler terms, a transaction should only commit after all transactions whose data it has read have committed. This ensures that if any transaction aborts, we can roll back all transactions that depended on it.

**Example of Recoverable Schedule:**

```
T1: Read(A)
T1: Write(A)
T1: Commit
T2: Read(A)
T2: Commit
```

This schedule is recoverable because T2 reads A after T1 has written it, and T1 commits before T2 commits.

**Example of Non-Recoverable Schedule:**

```
T1: Read(A)
T1: Write(A)
T1: Abort
T2: Read(A)
T2: Commit
```

This is non-recoverable because T2 reads A (written by T1) and commits, but T1 later aborts. T2 has committed using invalid data and cannot be rolled back.

#### 2. Cascadeless Schedules (ACA) - Avoid Cascading Aborts

A schedule is **cascadeless** (or ensures no cascading aborts) if every transaction reads only the committed values of data items from previous transactions. In other words, a transaction T_j should not read values written by transaction T_i unless T_i has already committed.

Cascadeless schedules are a stricter form of recoverable schedules. They prevent the phenomenon where the abort of one transaction forces the abort of multiple other transactions.

**Example of Cascadeless Schedule:**

```
T1: Read(A)
T1: Write(A)
T1: Commit
T2: Read(A)
T2: Write(B)
T2: Commit
```

This is cascadeless because T2 reads the committed value of A written by T1.

**Example of Cascading Schedule (Not Cascadeless):**

```
T1: Read(A)
T1: Write(A)
T2: Read(A)
T2: Write(B)
T1: Abort
```

This schedule is not cascadeless because T2 reads the uncommitted value of A written by T1. If T1 aborts, T2 must also abort (cascading abort).

#### 3. Strict Schedules (ST)

A schedule is **strict** if for every pair of transactions T_i and T_j, if T_j writes a data item that was previously written by T_i, then the commit or abort operation of T_i must occur before T_j performs any operation (read or write) on that data item.

Strict schedules provide the highest level of recoverability and ensure that uncommitted data is never read or overwritten by other transactions. This makes rollback operations simpler and more efficient.

**Example of Strict Schedule:**

```
T1: Read(A)
T1: Write(A)
T1: Commit
T2: Read(A)
T2: Write(B)
T2: Commit
```

This is strict because T2 reads A only after T1 has committed.

**Example of Non-Strict Schedule:**

```
T1: Read(A)
T1: Write(A)
T2: Read(A)
T2: Write(B)
T1: Commit
```

This is not strict because T2 reads A before T1 commits.

### Hierarchy of Recoverability

The three types of recoverable schedules follow a strict hierarchy in terms of restrictiveness:

```
Strict Schedule (ST) ⊂ Cascadeless Schedule (ACA) ⊂ Recoverable Schedule (RC)
```

A strict schedule is always cascadeless, and a cascadeless schedule is always recoverable. However, the converse is not true.

### Testing for Recoverability

To determine if a schedule is recoverable:

1. Identify all read-write conflicts in the schedule
2. For each read operation, check if the transaction that wrote the data has committed before the reading transaction commits
3. If any transaction reads uncommitted data and commits, the schedule is not recoverable

## Examples

### Example 1: Classifying a Schedule

Consider the following schedule:

```
S1: R1(X), W1(X), R2(X), W2(Y), R3(Y), W3(Z), C1, C2, C3
```

**Step-by-step Analysis:**

1. **Check for Recoverability (RC):**

- T2 reads X written by T1 (R2(X) after W1(X))
- T2 must commit after T1 commits for recoverability
- In S1, C1 occurs before C2, so this condition is satisfied
- T3 reads Y written by T2 (R3(Y) after W2(Y))
- C2 occurs before C3, so this condition is satisfied
- **Conclusion: Schedule is Recoverable**

2. **Check for Cascadeless (ACA):**

- T2 reads X after W1(X), but is C1 before R2(X)? No, R2(X) comes before C1
- This means T2 reads an uncommitted value
- **Conclusion: Schedule is NOT Cascadeless**

3. **Check for Strict (ST):**

- T2 reads X before T1 commits (violates strict condition)
- **Conclusion: Schedule is NOT Strict**

**Final Classification:** The schedule is Recoverable but neither Cascadeless nor Strict.

### Example 2: Cascadeless Schedule Verification

Consider:

```
S2: R1(A), W1(A), R2(B), W2(B), C2, R3(A), C3, C1
```

**Analysis:**

- T2 reads B (written by T2 itself) - no issue
- T3 reads A written by T1 - check: when does R3(A) occur? After C2 but before C1
- Wait, R3(A) occurs before C1 (commit of T1)
- For cascadeless: T3 should read only committed values from T1
- Since C1 occurs after R3(A), T3 reads uncommitted value of A
- **Not cascadeless**

For recoverability:

- T3 reads A (written by T1) and commits at C3
- T1 commits at C1, which is after C3
- This violates recoverability condition!
- **Not recoverable**

**Final Classification:** Neither Recoverable, Cascadeless, nor Strict.

### Example 3: Constructing a Strict Schedule

Given T1: R(A), W(A), C and T2: R(B), W(B), C

A strict schedule:

```
S3: R1(A), W1(A), C1, R2(B), W2(B), C2
```

This is strict because T2 operations on B occur entirely after C1 (T1's commit), and there are no conflicts between T1 and T2 on the same data items.

Another strict schedule with conflicts:

```
S4: R1(A), W1(A), C1, R2(A), W2(A), C2
```

Here T2 reads and writes A only after T1 commits, making it strict.

## Exam Tips

1. **Remember the Hierarchy:** Strict ⊂ Cascadeless ⊂ Recoverable. Always check in this order during exams.

2. **Quick Test for Recoverability:** If any transaction reads uncommitted data and then commits, the schedule is NOT recoverable.

3. **Quick Test for Cascadeless:** If any transaction reads uncommitted data (regardless of commit), the schedule is NOT cascadeless.

4. **Quick Test for Strict:** If any transaction reads OR writes a data item written by an uncommitted transaction, the schedule is NOT strict.

5. **Understanding "Read":** Remember that a transaction reading its own written values is always acceptable. The concern is always about reading values written by OTHER transactions.

6. **Dependency Graph:** For complex schedules, draw a dependency graph to trace data flow between transactions.

7. **Notation Practice:** Be comfortable with the notation R_i(X) meaning Transaction i reads X, W_i(X) meaning Transaction i writes X, and C_i meaning Transaction i commits.

8. **university Exam Focus:** Questions typically ask you to classify a given schedule as RC/ACA/ST or to determine whether a schedule is recoverable. Practice several examples.
