# Clocks, Events and Process States in Distributed Systems

## Introduction to Time and Global States

In distributed systems, processes execute concurrently on different computers connected by networks. Unlike in centralized systems, there is no shared memory or a single global clock to synchronize events across these processes. This lack of a global time reference makes it challenging to determine the order of events, reason about the system's state, and ensure consistency. The study of time, events, and process states provides the foundational concepts needed to overcome these challenges. It allows us to define causality, track system evolution, and capture meaningful global states for tasks like distributed debugging, checkpointing, and recovery.

## Fundamental Concepts: Events, Process States, and Clocks

### Events

An **event** is an action that occurs at a process. It represents a change in the state of the system. Events are the fundamental units of computation in a distributed system.

**Types of Events:**

- **Internal Event:** An action that occurs within a single process and does not involve communication with any other process (e.g., a local variable update).
- **Send Event:** The action of sending a message from one process to another.
- **Receive Event:** The action of receiving a message by a process from another process.

Every event is assumed to occur at an instantaneous point in time.

### Process States

The **state** of a process is the set of values of all variables within that process, including its program counter. A process's state changes only when an event occurs. The sequence of events within a single process forms a **process history**.

### Clocks

A **clock** is a mechanism to measure the passage of time. In distributed systems, we deal with two main types:

1.  **Physical Clocks:** These attempt to track real-time (e.g., UTC). Each computer has its own hardware clock (e.g., a quartz crystal).
2.  **Logical Clocks:** These assign sequence numbers to events to capture the _logical ordering_ or _causality_ between them, without necessarily corresponding to real-time.

## The Happened-Before Relation (→)

Leslie Lamport introduced the **happened-before relation** (denoted by `→`) to define a partial ordering of events in a distributed system without a global clock. This relation is also known as **causal ordering**.

**Rules for the Happened-Before Relation:**

1.  **Local Ordering:** If events `e1` and `e2` occur in the same process and `e1` occurs before `e2`, then `e1 → e2`.
2.  **Message Passing:** If event `e1` is the sending of a message by one process and event `e2` is the receipt of that same message by another process, then `e1 → e2`.
3.  **Transitivity:** If `e1 → e2` and `e2 → e3`, then `e1 → e3`.

If two events, `e1` and `e2`, are not related by the happened-before relation (i.e., `e1 ↛ e2` and `e2 ↛ e1`), they are said to be **concurrent** (denoted by `e1 || e2`). Concurrent events are not causally related.

**Example:**
Consider three processes, P1, P2, and P3.

```
P1: e1₁ ---s---→ e1₂
P2:          e2₁ ---r---> e2₂
P3:                e3₁
```

- `e1₁ → e1₂` (Rule 1: same process)
- `e1₁ → e2₂` (Because `e1₁ → s`, `s → r` (Rule 2), `r → e2₂` (Rule 1), therefore `e1₁ → e2₂` by transitivity (Rule 3))
- `e1₂ || e3₁` (They are not related by any chain of `→`; they are concurrent)

## Logical Clocks

Logical clocks are used to implement the happened-before relation by assigning a timestamp (a number) to each event.

### Lamport's Logical Clock

Lamport's algorithm assigns a simple integer counter, `C_i`, to each process `P_i`.

**Algorithm Rules:**

1.  **Local Event:** Before executing an event, a process increments its local counter: `C_i = C_i + 1`. The event is assigned this new value.
2.  **Send Event:** When sending a message `m`, the process includes its current timestamp, `t = C_i`.
3.  **Receive Event:** When receiving a message `m` with timestamp `t_sent`, the process sets its local counter to the maximum of its own value and the received timestamp plus one: `C_i = max(C_i, t_sent) + 1`. The receive event is then assigned this new value.

**Property:** If event `e → f`, then the timestamp of `e` is less than the timestamp of `f` (`L(e) < L(f)`). **However, the converse is not true.** `L(e) < L(f)` does not imply `e → f`; the events could be concurrent.

**Example of Lamport Timestamps:**

```
P1: 0 (A) --m1:1--> 2 (B)
P2:    1 (C) <-m1:1-- 3 (D) --m2:3--> 4 (E)
P3:    0 (F) ------------------m2:3-> 4 (G)
```

Events: A, B, C, D, E, F, G.

- `A → C` (via m1) and `L(A)=0 < L(C)=1`
- `C → D` (same process) and `L(C)=1 < L(D)=3`
- `D → G` (via m2) and `L(D)=3 < L(G)=4`
- `B || F` (concurrent). `L(B)=2`, `L(F)=0`. `L(F) < L(B)` but `F ↛ B`.

### Vector Clocks

Vector clocks overcome the limitation of Lamport clocks by ensuring that if the timestamp of event `e` is less than the timestamp of event `f` in every component, then `e` causally precedes `f`. Each process `P_i` maintains a vector `V_i` of length `N` (number of processes).

**Algorithm Rules:**

1.  **Initialize:** Initially, `V_i[j] = 0` for all `i, j`.
2.  **Local Event:** Before executing an event, process `P_i` increments its own component of the vector: `V_i[i] = V_i[i] + 1`.
3.  **Send Event:** When sending a message `m`, `P_i` includes its current vector `V_i`.
4.  **Receive Event:** When receiving a message `m` with vector `V_m`, process `P_j` updates its vector: `∀k: V_j[k] = max(V_j[k], V_m[k])`. It then increments its own component: `V_j[j] = V_j[j] + 1`. The receive event is assigned this new vector.

**Comparing Vector Timestamps:**
Let `V(e)` be the vector timestamp of event `e`.

- **Causally Precedes (`→`):** `V(e) < V(f)` iff `∀k: V(e)[k] <= V(f)[k]` and `∃k: V(e)[k] < V(f)[k]`.
- **Concurrent (`||`):** `V(e) || V(f)` iff `!(V(e) < V(f))` and `!(V(f) < V(e))`. This means some components of `V(e)` are greater and some are less than corresponding components in `V(f)`.

**Example of Vector Clocks:**
Assume 3 processes: P1, P2, P3.

```
P1: [1,0,0] (A) --m1:[1,0,0]--> [2,0,0] (B)
P2:      [1,1,0] (C) <--m1:[1,0,0]-- [max(1,1),max(0,0)+1,max(0,0)] = [1,1,0] -> [1,2,0] (D)
P3: [0,0,1] (E) ---------------------------------------m2:[1,2,0]--> [max(0,1),max(0,2),max(1,0)+1] = [1,2,1] (F)
```

- Is `A → C`? `V(A)=[1,0,0]`, `V(C)=[1,1,0]`. `[1,0,0] < [1,1,0]`? Yes, because for all k, `V(A)[k] <= V(C)[k]` and for k=2, `0 < 1`. So, YES.
- Is `E || D`? `V(E)=[0,0,1]`, `V(D)=[1,2,0]`. `[0,0,1] < [1,2,0]`? No, because `V(E)[3]=1` is not `<= V(D)[3]=0`. `[1,2,0] < [0,0,1]`? No. Therefore, `E || D`.

**Comparison of Lamport and Vector Clocks**

| Feature              | Lamport Clock                                                                   | Vector Clock                                                                                           |
| :------------------- | :------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------- |
| **Purpose**          | Capture total ordering consistent with causality.                               | Capture causal (happened-before) ordering precisely.                                                   |
| **Space Complexity** | O(1) per process (single integer).                                              | O(N) per process (vector of length N).                                                                 |
| **Inference**        | `e → f` ⇒ `L(e) < L(f)`                                                         | `e → f` ⇔ `V(e) < V(f)`                                                                                |
|                      | `L(e) < L(f)` ⇏ `e → f`                                                         |                                                                                                        |
| **Use Case**         | Simple event ordering where causality is not strictly required (e.g., logging). | Applications requiring precise knowledge of causality (e.g., causal broadcast, distributed snapshots). |

## Global States

A **global state** of a distributed system is the union of the local states of all processes and the state of the communication channels (messages in transit). Capturing a consistent global state is crucial for distributed debugging, checkpointing for recovery, and detecting stable properties (e.g., deadlock).

**The Challenge:** Because processes and channels are independent, collecting local states at different times can lead to an **inconsistent global state**. For example, a state where a process has recorded the receipt of a message, but the sending process has not recorded sending it.

**Consistent Global State:** A global state `S` is **consistent** if it respects causality. Specifically, if a receive event has been recorded in the state of the receiving process, then the corresponding send event must have been recorded in the state of the sending process. A consistent global state is one that could have occurred during the execution of the system.

**Inconsistent Global State:** A global state where a receive event is recorded but the corresponding send event is not recorded. This state could never have occurred in a real execution.

## Exam Tips

1.  **Understand Happened-Before:** This is the core concept. Be able to apply the three rules (local order, message passing, transitivity) to any diagram of events to determine the `→` relation and identify concurrent events.
2.  **Practice Timestamping:** Draw process timelines and practice assigning both Lamport timestamps and Vector clocks to events. This is a common exam question.
3.  **Key Difference:** Remember the critical difference between Lamport and Vector clocks: Lamport's `L(e) < L(f)` does not guarantee `e → f`, but Vector's `V(e) < V(f)` does.
4.  **Global State Consistency:** When asked about global states, focus on the channel state. An inconsistent state arises from "recording the message receipt but not the send." Think about the messages in transit.
5.  **Interpret Notation:** Be comfortable with the notation (`→`, `||`, `V_i[i]`, etc.) as it will be used in questions.
