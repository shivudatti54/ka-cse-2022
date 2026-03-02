# Time and Global States in Distributed Systems

## Introduction

In a centralized system, there is a single, global clock that provides a consistent notion of time and a single, well-defined state for the entire system. Distributed systems, however, lack this shared global memory and a common physical clock. This fundamental characteristic introduces significant challenges: How do we order events that happen on different machines? How can we know the global state of the entire system at a particular time? Understanding "Time and Global States" is crucial for designing and reasoning about distributed algorithms for coordination, consistency, and failure recovery.

## Core Concepts

### The Need for Logical Ordering

Since it is often impossible to synchronize physical clocks across a network with perfect accuracy (due to network delays and clock drift), we rely on **logical time** to capture the *causal ordering* of events. The key idea is that if event A causally affects event B (e.g., a message is sent before it is received), then A must be considered as happening before B, regardless of their physical timestamps.

### Lamport's Logical Clocks

Leslie Lamport proposed a mechanism to order events logically without a global clock.

*   **Logical Clock:** Each process `P_i` maintains a simple counter, `C_i`, which it increments according to two rules:
    1.  **Before executing an event (e.g., send, receive, internal event), a process increments its counter:** `C_i = C_i + 1`.
    2.  **When a process sends a message, it includes its current logical timestamp.** When a process receives a message with timestamp `T`, it updates its own clock: `C_i = max(C_i, T) + 1`.

This scheme ensures that if event `a` happens before event `b` (denoted `a -> b`), then the logical clock of `a` is less than the clock of `b` (`L(a) < L(b)`). However, the converse is not true: `L(a) < L(b)` does not imply `a -> b`. This is a **partial ordering** of events.

### Vector Clocks

To capture causality completely, we need a system where `L(a) < L(b)` *if and only if* `a -> b`. **Vector Clocks** achieve this.

*   **Vector Clock:** Each process `P_i` maintains a vector `V_i` of `N` integers (where `N` is the total number of processes). `V_i[i]` is the logical time of `P_i`, and `V_i[j]` represents the latest logical time of `P_j` known to `P_i`.
*   **Rules:**
    1.  Before executing an event, a process increments its own component: `V_i[i] = V_i[i] + 1`.
    2.  When sending a message, a process includes its entire current vector clock.
    3.  On receiving a message with vector clock `T`, the receiver updates its vector: for each `j`, set `V_i[j] = max(V_i[j], T[j])`. Then, it increments its own component (`V_i[i] = V_i[i] + 1`) to account for the receive event itself.

*   **Comparing Vectors:**
    *   `V = V'` iff `V[i] = V'[i]` for all `i`.
    *   `V <= V'` iff `V[i] <= V'[i]` for all `i`.
    *   `V < V'` iff `V <= V'` and `V != V'`.

We can now say that event `a` causally precedes event `b` (`a -> b`) **if and only if** the vector clock of `a` is less than the vector clock of `b` (`V(a) < V(b)`).

**Example:** Imagine three processes, P0, P1, and P2.
*   P0 sends a message `m1` with its vector `(1,0,0)`.
*   P1 receives `m1`, updates its vector to `max((0,0,0), (1,0,0)) = (1,0,0)`, increments its own component: `(1,1,0)`, and then sends a message `m2` with `(1,1,0)`.
*   P2 receives `m2` first, its vector becomes `(1,1,1)`.
*   P0 then sends another message `m3` with an updated clock `(2,0,0)`.
*   When P2 receives `m3`, it compares `(2,0,0)` with its current `(1,1,1)`. It updates: `(max(2,1), max(0,1), max(0,1)) = (2,1,1)` and increments its own component for the receive event: `(2,1,2)`.

The vector `(2,0,0)` from `m3` is *not less than* the vector `(1,1,1)` from `m2`. This correctly indicates that `m2` and `m3` are **concurrent events**; neither causally affects the other.

### Global States and Consistent Snapshots

A **global state** is the set of all individual process states and the state of the communication channels. A **consistent global snapshot** is a captured global state that could have occurred during the execution of the system. It must not contain inconsistencies, such as recording the receipt of a message without recording its send.

The **Chandy-Lamport snapshot algorithm** is a famous algorithm for recording a consistent global snapshot without stopping the system. It works by having an initiator process inject a special **marker** message into the network. The rules for processes upon receiving a marker message ensure that the state they record for their incoming channels is consistent with the states recorded by other processes.

## Key Points / Summary

*   **Physical Clock Limitations:** Perfect synchronization is impossible, necessitating logical concepts of time.
*   **Logical Clocks (Lamport):** Provide a partial ordering of events based on causality. If `a -> b` then `L(a) < L(b)`, but not vice-versa. Useful for total ordering where a consistent order is needed (e.g., log entries).
*   **Vector Clocks:** Capture causality completely. `V(a) < V(b)` if and only if `a -> b`. They are essential for applications that need true causal ordering, like causal consistency in databases or debugging distributed systems.
*   **Global State:** The collective state of all processes and channels.
*   **Consistent Snapshot:** A recorded global state that is meaningful and could have existed. The Chandy-Lamport algorithm is a key method for obtaining one without freezing the entire system.
*   **Fundamental Challenge:** The lack of a global clock or memory means time and state are inherently relative concepts in a distributed system, and we must use clever algorithms to reason about them.