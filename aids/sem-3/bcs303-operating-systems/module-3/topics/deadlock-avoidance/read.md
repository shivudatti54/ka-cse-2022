# Deadlock Avoidance


## Table of Contents

- [Deadlock Avoidance](#deadlock-avoidance)
- [Introduction](#introduction)
- [Safe State vs Unsafe State](#safe-state-vs-unsafe-state)
  - [Safe State](#safe-state)
  - [Unsafe State](#unsafe-state)
  - [Example: Safe vs Unsafe](#example-safe-vs-unsafe)
- [Resource Allocation Graph Algorithm](#resource-allocation-graph-algorithm)
  - [Edge Types](#edge-types)
  - [Algorithm](#algorithm)
- [Banker's Algorithm](#bankers-algorithm)
  - [Data Structures](#data-structures)
  - [Safety Algorithm](#safety-algorithm)
  - [Resource-Request Algorithm](#resource-request-algorithm)
  - [Worked Example](#worked-example)
- [Prevention vs Avoidance](#prevention-vs-avoidance)
- [Summary](#summary)
- [Exam Tips](#exam-tips)

## Introduction

**Deadlock avoidance** is a strategy where the OS dynamically examines the resource-allocation state before granting each request, ensuring the system never enters an **unsafe state**. Unlike prevention (which restricts how requests are made), avoidance allows all four necessary conditions to potentially hold but makes smart allocation decisions at runtime to avoid deadlock.

The key requirement: each process must declare in advance the **maximum number** of resources of each type it may need. The OS uses this information to ensure that the system always remains in a **safe state**.

## Safe State vs Unsafe State

### Safe State

A state is **safe** if the system can allocate resources to each process (up to its maximum) in some order and still avoid deadlock. Formally, a safe state has a **safe sequence**.

**Safe sequence:** A sequence of processes <P1, P2, ..., Pn> is safe if for each Pi, the resources Pi still needs can be satisfied by the currently available resources plus the resources held by all Pj where j < i (processes that finish before Pi in the sequence).

### Unsafe State

A state is **unsafe** if **no safe sequence exists**. An unsafe state **may** lead to deadlock (but doesn't necessarily mean deadlock has occurred yet).

```
 +-------------+
 | All States |
 +------+------+
 |
 +------------+------------+
 | |
 +-----+-----+ +-----+-----+
 | Safe | | Unsafe |
 | States | | States |
 | | | +------+ |
 | | | |Dead- | |
 | | | |lock | |
 | | | +------+ |
 +-----------+ +-----------+

 Safe state → Deadlock is impossible
 Unsafe state → Deadlock is possible (but not certain)
 Deadlock → Always an unsafe state
```

**Key relationships:**

- Safe state → **No deadlock** (guaranteed)
- Unsafe state → Deadlock is **possible** (not guaranteed)
- Deadlock state → Always **within** the set of unsafe states

### Example: Safe vs Unsafe

System has 12 tape drives. Three processes:

| Process | Maximum Need | Currently Holding |
| :------ | :----------- | :---------------- |
| P0      | 10           | 5                 |
| P1      | 4            | 2                 |
| P2      | 9            | 2                 |

Available = 12 - (5 + 2 + 2) = **3**

**Is this safe?** Find a safe sequence:

- P1 needs at most 4 - 2 = 2 more. Available = 3 >= 2. Allocate to P1.
- P1 finishes, releases 4. Available = 3 + 4 = **5** (wait: 3 - 2 + 4 = 5)

Actually let's recalculate: Give P1 its remaining 2 from Available(3). Available becomes 1. P1 finishes, releases all 4. Available = 1 + 4 = **5**.

- P0 needs 10 - 5 = 5 more. Available = 5 >= 5. Allocate to P0.
- P0 finishes, releases 10. Available = 5 + 10 = **15** (more than enough).
- P2 needs 9 - 2 = 7 more. Available = 15 (actually recalculated: after P0 releases, plenty available).

Safe sequence: **<P1, P0, P2>**. The system is in a safe state.

## Resource Allocation Graph Algorithm

For systems where each resource type has **exactly one instance**, deadlock avoidance can be implemented using a modified **Resource Allocation Graph (RAG)** with a new type of edge called a **claim edge**.

### Edge Types

| Edge            | Notation | Meaning                             | Drawing      |
| :-------------- | :------- | :---------------------------------- | :----------- |
| Request edge    | Pi → Rj  | Pi is requesting Rj                 | Solid arrow  |
| Assignment edge | Rj → Pi  | Rj is allocated to Pi               | Solid arrow  |
| Claim edge      | Pi ⇢ Rj  | Pi **may** request Rj in the future | Dashed arrow |

### Algorithm

1. Before execution, each process declares all resources it **may** request — these are added as **claim edges** (dashed)
2. When Pi actually requests Rj, the claim edge Pi ⇢ Rj is converted to a **request edge** Pi → Rj
3. Before granting the request (converting request edge to assignment edge), the system checks:

- **Would this create a cycle** (considering both solid and dashed edges)?
- If **no cycle** → grant the request (safe)
- If **cycle** → deny the request (Pi must wait)

4. When Pi releases Rj, the assignment edge reverts to a claim edge

```
Before request: After granting (if safe):
 Pi - - -> Rj Rj ------> Pi
 (claim) (assignment)

Check: Does converting claim→assignment create a cycle?
 No cycle → Safe → Grant
 Cycle → Unsafe → Deny (Pi waits)
```

**Limitation:** This algorithm only works when each resource type has a **single instance**.

## Banker's Algorithm

For systems with **multiple instances** of each resource type, we use the **Banker's Algorithm**, proposed by Edsger Dijkstra. It is named after the way a banker manages loans — never lending more than can be safely recovered.

### Data Structures

Let **n** = number of processes, **m** = number of resource types.

| Data Structure | Size               | Description                                                      |
| :------------- | :----------------- | :--------------------------------------------------------------- |
| **Available**  | Vector of length m | Available[j] = number of available instances of resource type Rj |
| **Max**        | n × m matrix       | Max[i][j] = maximum demand of process Pi for resource Rj         |
| **Allocation** | n × m matrix       | Allocation[i][j] = instances of Rj currently allocated to Pi     |
| **Need**       | n × m matrix       | Need[i][j] = remaining demand = Max[i][j] - Allocation[i][j]     |

### Safety Algorithm

Determines if the current state is safe by trying to find a safe sequence.

```
1. Let Work = Available (copy of available resources)
 Let Finish[i] = false for all i (no process has finished yet)

2. Find an index i such that BOTH:
 a. Finish[i] == false (process hasn't finished)
 b. Need[i] <= Work (process can be satisfied)

3. If such i exists:
 Work = Work + Allocation[i] (process finishes, releases resources)
 Finish[i] = true
 Go to step 2

4. If Finish[i] == true for ALL i:
 → System is in a SAFE state
 Otherwise:
 → System is in an UNSAFE state
```

### Resource-Request Algorithm

When process Pi makes a request Request[i]:

```
1. If Request[i] > Need[i]:
 → ERROR (process exceeded its maximum claim)

2. If Request[i] > Available:
 → Pi must WAIT (resources not available)

3. Pretend to allocate (tentative):
 Available = Available - Request[i]
 Allocation[i] = Allocation[i] + Request[i]
 Need[i] = Need[i] - Request[i]

4. Run the Safety Algorithm:
 If SAFE → Actually grant the request
 If UNSAFE → Deny the request, restore old state, Pi waits
```

### Worked Example

**System:** 5 processes (P0-P4), 3 resource types: A(10), B(5), C(7)

**Snapshot at time T0:**

| Process | Allocation (A B C) | Max (A B C) | Need (A B C) |
| :------ | :----------------- | :---------- | :----------- |
| P0      | 0 1 0              | 7 5 3       | 7 4 3        |
| P1      | 2 0 0              | 3 2 2       | 1 2 2        |
| P2      | 3 0 2              | 9 0 2       | 6 0 0        |
| P3      | 2 1 1              | 2 2 2       | 0 1 1        |
| P4      | 0 0 2              | 4 3 3       | 4 3 1        |

**Available = (10-7, 5-2, 7-5) = (3, 3, 2)**

Wait — let me recalculate: Total allocated = (0+2+3+2+0, 1+0+0+1+0, 0+0+2+1+2) = (7, 2, 5). Available = (10-7, 5-2, 7-5) = **(3, 3, 2)**.

**Finding a safe sequence:**

| Step | Process | Need    | Work (before) | Can run?               | Work (after)              |
| :--- | :------ | :------ | :------------ | :--------------------- | :------------------------ |
| 1    | P1      | (1,2,2) | (3,3,2)       | Yes (1<=3, 2<=3, 2<=2) | (3,3,2)+(2,0,0)=(5,3,2)   |
| 2    | P3      | (0,1,1) | (5,3,2)       | Yes                    | (5,3,2)+(2,1,1)=(7,4,3)   |
| 3    | P4      | (4,3,1) | (7,4,3)       | Yes                    | (7,4,3)+(0,0,2)=(7,4,5)   |
| 4    | P2      | (6,0,0) | (7,4,5)       | Yes                    | (7,4,5)+(3,0,2)=(10,4,7)  |
| 5    | P0      | (7,4,3) | (10,4,7)      | Yes                    | (10,4,7)+(0,1,0)=(10,5,7) |

**Safe sequence: <P1, P3, P4, P2, P0>**

**Now suppose P1 requests (1, 0, 2):**

1. Request(1,0,2) <= Need(1,2,2)? Yes
2. Request(1,0,2) <= Available(3,3,2)? Yes
3. Tentatively allocate:

- Available = (3,3,2) - (1,0,2) = (2,3,0)
- Allocation[P1] = (2,0,0) + (1,0,2) = (3,0,2)
- Need[P1] = (1,2,2) - (1,0,2) = (0,2,0)

4. Run safety algorithm with new state → If safe, grant; if unsafe, deny.

## Prevention vs Avoidance

| Aspect                   | Prevention                                    | Avoidance                                 |
| :----------------------- | :-------------------------------------------- | :---------------------------------------- |
| **Approach**             | Restrict how requests are made (static rules) | Make dynamic decisions at each request    |
| **Information needed**   | None beyond resource types                    | Maximum resource needs of each process    |
| **Restricts**            | How processes request resources               | Which requests are granted                |
| **Resource utilization** | Lower (conservative restrictions)             | Higher (more flexible)                    |
| **Overhead**             | Low (simple rules)                            | Higher (safety algorithm at each request) |
| **Deadlock possible?**   | No (structurally impossible)                  | No (dynamically avoided)                  |

## Summary

| Concept            | Key Point                                                  |
| :----------------- | :--------------------------------------------------------- |
| Safe state         | A safe sequence exists — all processes can finish          |
| Unsafe state       | No safe sequence — deadlock is possible but not certain    |
| Claim edge         | Dashed edge in RAG showing future possible request         |
| RAG algorithm      | For single-instance resources — check for cycles           |
| Banker's algorithm | For multi-instance resources — check for safe state        |
| Available          | Resources currently free                                   |
| Need               | Max - Allocation (what each process still needs)           |
| Safety algorithm   | Simulate: can all processes finish with current resources? |

## Exam Tips

1. **Banker's Algorithm numerical problems** — This is one of the most frequently asked questions in exams (10 marks). Practice computing Need matrix, running the safety algorithm, and finding safe sequences.
2. **Safe vs unsafe vs deadlock** — Know the relationship: deadlock ⊂ unsafe ⊂ all states. An unsafe state does NOT mean deadlock has occurred.
3. **Resource-Request Algorithm steps** — Know all 4 steps: check against Need, check against Available, tentatively allocate, run safety check.
4. **RAG with claim edges** — Be able to draw the modified RAG and explain how claim edges work.
5. **Prevention vs avoidance** — This is a common comparison question. Key difference: prevention uses static rules, avoidance uses dynamic runtime checks with maximum need information.
6. **Time complexity** — The safety algorithm is O(m x n^2) where m = resource types and n = processes.
