# Revision Notes: Distributed Systems - Coordination and Agreement (Ch 15.1-15.5)

## Introduction

- Definition: Distributed systems are collections of independent computers that work together as a single system.
- Key characteristics: autonomy, heterogeneity, and distribution.

## Distributed Mutual Exclusion

- Problem: Multiple processes want to access a shared resource simultaneously.
- Solution: Use a lock or semaphore to ensure exclusive access.
- Theorem: If a process is holding a lock, no other process can acquire it until it releases it.

### Petri Nets

- Definition: A graphical model for describing the interactions between processes.
- Key components: Places, transitions, arcs, and tokens.

### Token Ring Protocol

- Definition: A protocol for achieving mutual exclusion in a distributed system.
- Key components: Token, ring, and buffer.

## Concurrency Control

- Definition: Mechanisms for managing concurrent access to shared resources.
- Key concepts: Synchronization, deadlock detection, and recovery.

### Locks and Semaphores

- Definition: Synchronization primitives for controlling access to shared resources.
- Key concepts: Types of locks (mutual exclusion, shared, and read-write), semaphore values, and operations.

### Mutual Exclusion

- Definition: A process can access a shared resource only if it holds the lock.
- Theorem: If a process is holding a lock, no other process can acquire it until it releases it.

### Starvation and Livelocks

- Definition: Starvation: a process is unable to access a shared resource due to other processes holding locks indefinitely.
- Definition: Livelock: a process is unable to make progress due to repeated attempts to acquire a lock.

## Consensus Algorithms

- Definition: Algorithms for achieving agreement among processes on a value.
- Key concepts: Leader election, proposals, and votes.

### Paxos Algorithm

- Definition: A consensus algorithm that ensures all processes agree on a value.
- Key concepts: Proposals, votes, and acceptances.

### Raft Algorithm

- Definition: A consensus algorithm that ensures all processes agree on a value.
- Key concepts: Leaders, followers, and log entries.

## References

- [Insert relevant textbook or resource]
