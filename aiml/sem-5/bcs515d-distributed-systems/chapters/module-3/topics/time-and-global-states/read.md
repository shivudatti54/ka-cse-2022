# Distributed Systems: Module 3 - Time and Global States

## Introduction

In a centralized system, understanding the state of the system is straightforward—there's a single, global clock and a single memory state we can observe. However, in a distributed system, processes run concurrently on different machines, each with its own independent clock and local state. This raises fundamental questions: How can we order events across these systems? What does it mean to say the system was in a "global state" at a particular time? This module delves into the core concepts of logical and physical time, event ordering, and techniques for capturing a meaningful global state, which are essential for debugging, monitoring, and ensuring consistency in distributed applications.

## Core Concepts

### 1. The Problem of Physical Time

Each computer in a distributed system has its own physical hardware clock. These clocks are subject to **clock drift** (they run at slightly different speeds) and are not perfectly synchronized. Even with protocols like Network Time Protocol (NTP), achieving perfect synchronization is impossible due to network delays. This means we cannot rely on physical time to order events from different machines accurately.

### 2. Logical Time and Lamport's Logical Clocks

To overcome the limitations of physical time, Leslie Lamport introduced the concept of **logical clocks**. The key idea is to define a "happened-before" relation (denoted as `→`), also known as causal ordering.

*   **The "Happened-Before" Relation:** For two events, `a` and `b`, `a → b` if:
    1.  `a` and `b` are events in the same process, and `a` occurs before `b`.
    2.  `a` is the sending of a message and `b` is the receipt of that same message.
    3.  The relation is transitive (if `a → b` and `b → c`, then `a → c`).

If two events are not related by `→`, they are said to be **concurrent**.

*   **Lamport Timestamps:** Each process `P_i` maintains a logical clock `L_i`.
    *   Before a process executes an event, it increments its local clock: `L_i = L_i + 1`.
    *   When a process sends a message, it includes its current timestamp `t`.
    *   Upon receiving a message with timestamp `t`, the receiver sets its logical clock to `max(L_i, t) + 1`.

This ensures that if `a → b`, then the timestamp of `a` is less than the timestamp of `b`. However, the converse is not true: a lower timestamp does not necessarily mean "happened-before."

### 3. Vector Clocks

**Vector Clocks** extend Lamport's logical clocks to overcome their limitation. They can detect causal relationships (and concurrency) between events definitively.

*   Each process `P_i` maintains a vector `V_i` of `N` integers (for `N` processes).
*   `V_i[i]` is the logical time for `P_i`.
*   `V_i[j]` represents `P_i`'s knowledge of `P_j`'s logical time.

**Rules:**
1.  Initially, all counters are 0.
2.  Before executing an event, process `P_i` increments its own component: `V_i[i] = V_i[i] + 1`.
3.  When sending a message, `P_i` includes its entire vector `V_i`.
4.  On receiving a message with vector `t`, process `P_i` updates its vector: `for all j, V_i[j] = max(V_i[j], t[j])`. Then it increments its own component (`V_i[i] = V_i[i] + 1`) to count the receive event.

**Comparison:**
*   `V_a = V_b` iff `V_a[i] = V_b[i]` for all `i`.
*   `V_a <= V_b` iff `V_a[i] <= V_b[i]` for all `i`.
*   `V_a < V_b` iff `V_a <= V_b` and `V_a != V_b`.

We can now determine causality:
*   **Event `a` happened-before event `b` (`a → b`)** iff `V_a < V_b`.
*   Events `a` and `b` are **concurrent** iff `!(V_a < V_b)` and `!(V_b < V_a)`.

*Example:* Process P1 sends a message with vector `(1,0,0)`. P2 receives it and updates its vector to `max( (0,0,0), (1,0,0) ) = (1,0,0)`, then increments its own counter, resulting in `(1,1,0)`. This vector correctly reflects that P1's event (send) happened before P2's event (receive).

### 4. Global States

A **global state** of a distributed system is the set of all local process states (`S_1, S_2, ..., S_N`) and the state of the communication channels (the messages in transit).

Capturing a truly instantaneous global state is impossible due to the lack of a global clock. Instead, we record a **consistent global state** (or a **snapshot**). A recorded global state is consistent if it reflects a set of local states that could have occurred together in some real execution of the system. This means if a message's `receive` event is recorded in the snapshot, its `send` event must also be included.

The **Chandy-Lamport snapshot algorithm** is a famous algorithm for recording such a consistent global state without freezing the entire system.

## Key Points / Summary

*   **Physical Clocks** are imperfect and cannot be perfectly synchronized, making them unreliable for ordering events in distributed systems.
*   **Logical Clocks** provide a way to order events based on causality, not absolute time.
*   **Lamport Timestamps** ensure that if `a → b`, then `L(a) < L(b)`, but not vice-versa.
*   **Vector Clocks** are a more powerful mechanism that allow processes to precisely determine causal relationships (`a → b`) or concurrency between events.
*   A **Global State** is a collection of local process states and channel states. A **Consistent Global State** is one that looks like it existed at a single moment in time, even if it didn't, and is crucial for building checkpoints and monitoring systems.
*   Understanding time and state is fundamental for implementing higher-level distributed systems concepts like consistency models, distributed debugging, and checkpointing.