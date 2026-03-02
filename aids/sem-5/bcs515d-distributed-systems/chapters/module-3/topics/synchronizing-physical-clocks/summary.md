# Synchronizing Physical Clocks

================================

## Introduction

---

- Distributed systems require synchronization of physical clocks to ensure consistency in global states.
- Synchronization ensures that all nodes in the system have the same notion of time.

## Definitions

---

- **Clock Skew**: The difference in time between two clocks.
- **Clock Synchronization**: The process of adjusting clocks to have the same time.
- **Synchronization Protocol**: A set of rules for synchronizing clocks in a distributed system.

## Theorems

---

- **Pitts' Theorem**: If two processes are synchronized, then if one process is delayed, the other process will also be delayed by the amount of the delay.
- **Lamport's Theorem**: If two processes are synchronized, then if one process is delayed by a certain amount, the other process will also be delayed by the same amount.

## Formulas

---

- **Clock Skew Formula**: Δt = |t1 - t2|, where Δt is the clock skew and t1 and t2 are the times on two clocks.
- **Synchronization Formula**: tsync = (t1 + t2) / 2, where tsync is the synchronized time and t1 and t2 are the times on two clocks.

## Key Points

---

- **NTP (Network Time Protocol)**: A widely used synchronization protocol for distributed systems.
- **Synchronization Methods**:
  - **Peer-to-Peer Synchronization**: Two or more nodes synchronize with each other.
  - **Master-Slave Synchronization**: One node acts as the master and synchronizes with one or more slave nodes.
- **Clock Synchronization Algorithms**:
  - **Round-Robin Algorithm**: Each node synchronizes with the next node in a circular list.
  - **Leader-Follower Algorithm**: One node acts as the leader and synchronizes with follower nodes.

## Important Concepts

---

- **Clock Drift**: The gradual change in the time kept by a clock over time.
- **Clock Jitter**: The variation in the time difference between two clocks.
- **Synchronization Accuracy**: The degree of accuracy of a synchronization protocol.
