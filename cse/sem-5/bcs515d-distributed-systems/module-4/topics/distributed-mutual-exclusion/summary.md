# Distributed Mutual Exclusion - Summary

## Key Definitions and Concepts

- **Critical Section (CS)**: A portion of code that accesses shared resources and must be executed by only one process at a time.

- **Distributed Mutual Exclusion**: Ensuring that only one process can enter the critical section in a distributed system where processes run on different machines.

- **Token**: A special message that circulates among processes; only the holder can enter the critical section.

- **Logical Clock**: A counter used to order events in distributed systems without relying on physical clocks.

## Important Formulas and Theorems

- **Lamport's Algorithm Message Complexity**: 3(N-1) messages per CS entry
- **Ricart-Agrawala Algorithm Message Complexity**: 2(N-1) messages per CS entry
- **Maekawa's Algorithm Message Complexity**: O(√N) messages per CS entry
- **Token Ring Message Complexity**: 0 to N-1 messages (variable based on token position)

## Key Points

1. Distributed mutual exclusion differs from centralized due to absence of shared memory, no global clock, and unpredictable network delays.

2. Three essential properties: Safety (mutual exclusion), Liveness (no deadlock), and Fairness (no starvation).

3. Token-based algorithms use circulating tokens while tokenless algorithms use message passing with timestamps.

4. Lamport's algorithm uses logical clocks for total event ordering and requires explicit RELEASE messages.

5. Ricart-Agrawala improves on Lamport by eliminating RELEASE messages and using deferred replies.

6. Lower message complexity often comes with increased algorithm complexity or other trade-offs.

7. Token loss or process crashes can cause significant issues in token-based algorithms.

## Common Mistakes to Avoid

1. Confusing physical clocks with logical clocks - distributed systems use logical clocks, not physical time.

2. Forgetting that Ricart-Agrawala requires N-1 REPLY messages before entering CS, not N messages.

3. Thinking token-based algorithms are always better - they can suffer from token loss and require token regeneration.

4. Ignoring the synchronization delay in algorithms - it affects real-time performance.

## Revision Tips

1. Practice drawing timelines for Ricart-Agrawala to understand message flow.

2. Memorize the message complexity formulas for all major algorithms.

3. Understand why timestamps are used instead of actual time for ordering requests.

4. Compare algorithms on properties: message complexity, delay, fault tolerance, and implementation complexity.
