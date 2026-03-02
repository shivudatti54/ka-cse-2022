# Characterizing Schedules Based on Serializability

## Introduction

In a Database Management System (DBMS), a **schedule** represents the chronological order in which the operations (read or write) of multiple concurrent transactions are executed. The primary goal of concurrency control is to allow maximum concurrency while ensuring that the database remains consistent. **Serializability** is the fundamental criterion for correctness of concurrent schedules. It guarantees that the execution of concurrent transactions produces the same outcome as some serial (one-after-another) execution of those same transactions. This module delves into how we characterize schedules based on this crucial concept.

## Core Concepts

### 1. Serial Schedule
A **serial schedule** is one where the operations of each transaction are executed consecutively, without any interleaving of operations from other transactions. For two transactions T1 and T2, the only possible serial schedules are (all of T1 followed by all of T2) or (all of T2 followed by all of T1). While these schedules are always correct, they are inefficient as they do not allow any concurrency.

### 2. Serializable Schedule
A **serializable schedule** is a non-serial schedule (i.e., operations are interleaved) that is **equivalent** to some serial schedule. This equivalence is what makes the schedule correct despite the interleaving. There are two primary types of serializability used to define this equivalence:

#### a. Conflict Serializability
This is the most practical and commonly used form. Two operations **conflict** if they all belong to different transactions, operate on the same data item, and at least one of them is a **write** operation.

*   **Conflicting Pairs:** (Read, Write), (Write, Read), (Write, Write)
*   **Non-Conflicting Pairs:** (Read, Read)

A schedule is **conflict serializable** if it can be transformed into a serial schedule by swapping non-conflicting operations. This is tested using a **precedence graph** (or serializability graph).

*   **Precedence Graph:** A directed graph where:
    *   Vertices represent transactions.
    *   An edge `Ti -> Tj` is created if an operation in `Ti` conflicts with and appears before an operation in `Tj`.

If the precedence graph is **acyclic**, the schedule is conflict serializable. A cycle in the graph indicates a conflict that cannot be resolved, meaning the schedule is not conflict serializable.

#### b. View Serializability
This is a broader, more theoretical definition. A schedule is **view serializable** if it is **view equivalent** to some serial schedule. Two schedules are view equivalent if:
1.  The same set of transactions participates.
2.  For each data item, the **first read** operation that obtains its value is from the same transaction in both schedules.
3.  Each **write** operation is from the same transaction in both schedules.
4.  The **final write** on each data item is from the same transaction in both schedules.

Every conflict serializable schedule is view serializable, but the converse is not always true. View serializability includes schedules that involve **blind writes** (a write without a prior read), which cannot be handled by the simpler conflict test.

---

## Examples

### Example 1: Conflict Serializable Schedule
Consider two transactions:
*   **T1:** R(A), W(A)
*   **T2:** R(A), W(A)

**Schedule S1:** R1(A), R2(A), W1(A), W2(A)

1.  **Check for Conflicts:**
    *   `R1(A)` and `W2(A)` conflict? Yes (Read-Write on same item, different transactions). So `T1 -> T2`.
    *   `R2(A)` and `W1(A)` conflict? Yes (Read-Write). So `T2 -> T1`.
2.  **Build Precedence Graph:**
    *   Edges: `T1 -> T2` and `T2 -> T1`.
    *   This graph **has a cycle** (`T1->T2->T1`).
3.  **Conclusion:** Schedule S1 is **NOT conflict serializable**.

**Schedule S2:** R1(A), W1(A), R2(A), W2(A)

1.  **Check for Conflicts:**
    *   `W1(A)` and `R2(A)` conflict? Yes (Write-Read). So `T1 -> T2`.
    *   Are there any other conflicting pairs leading to `T2 -> T1`? No.
2.  **Build Precedence Graph:**
    *   Only one edge: `T1 -> T2`.
    *   The graph is **acyclic**.
3.  **Conclusion:** Schedule S2 **is conflict serializable** (equivalent to the serial schedule T1 followed by T2).

### Example 2: View Serializability vs. Conflict Serializability
Consider:
*   **T1:** W(A)
*   **T2:** W(A)
*   **T3:** W(A)

**Schedule S3:** W1(A), W2(A), W3(A)
This schedule is trivially serial (and thus both conflict and view serializable).

**Schedule S4:** W2(A), W1(A), W3(A)
*   **Conflict Test:** All operations are writes and conflict. The precedence graph will have edges (`T2->T1`, `T1->T3`, `T2->T3`), which is acyclic. Thus, it is **conflict serializable**.
*   It is equivalent to the serial schedule T2, T1, T3.

**Schedule S5:** W3(A), W2(A), W1(A) // This is a blind write schedule.
*   **Conflict Test:** The graph has edges (`T3->T2`, `T2->T1`, `T3->T1`) - acyclic. It is **conflict serializable**.
*   It is equivalent to the serial schedule T3, T2, T1.

All these schedules are also view serializable. A schedule involving a blind write that creates a cycle in the precedence graph would be view serializable but not conflict serializable.

---

## Key Points & Summary

| Feature | Conflict Serializability | View Serializability |
| :--- | :--- | :--- |
| **Basis** | Order of conflicting operations. | Initial read, final write, and update dependencies. |
| **Test Method** | Precedence Graph (must be acyclic). | More complex; involves checking view equivalence conditions. |
| **Scope** | Less inclusive. More practical for concurrency control protocols. | More inclusive. Considers a wider set of schedules. |
| **Blind Writes** | Cannot handle all schedules with blind writes. | Can handle schedules with blind writes. |
| **Practical Use** | Used by most concurrency control protocols (e.g., Two-Phase Locking). | Mainly of theoretical interest; checking for it is an NP-complete problem. |

*   **Why it matters:** Serializability is the cornerstone for ensuring database consistency in a multi-user environment. It is the benchmark that all concurrency control protocols (like Two-Phase Locking and Timestamp Ordering) strive to achieve.
*   **Conflict serializability** is the de facto standard for implementation due to its simpler, efficient checking mechanism via precedence graphs.
*   A schedule must be serializable to be considered correct. Non-serializable schedules can lead to inconsistent results and are rejected by the DBMS.