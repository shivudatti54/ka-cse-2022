# Concurrency Control in Distributed Transactions - Summary

## Key Definitions and Concepts

- **Distributed Transaction**: A transaction that operates across multiple database nodes, requiring coordination to ensure atomicity.
- **Concurrency Control**: Mechanisms to ensure correct execution of multiple concurrent transactions while maintaining database consistency.
- **Two-Phase Commit (2PC)**: A protocol ensuring atomic commitment of distributed transactions through prepare and commit phases.
- **Lock Manager**: A system component that manages locks on data items to control concurrent access.
- **Wait-for Graph**: A directed graph representing transaction dependencies, where cycles indicate deadlocks.
- **Timestamp**: A unique identifier assigned to transactions to determine their ordering for serializability.

## Important Formulas and Theorems

- **Serializability Condition**: A schedule is serializable if it is conflict-equivalent to some serial schedule.
- **Thomas' Write Rule**: If TS(T) < write_TS(X), the write can be ignored if a newer version already exists.
- **2PC Blocking Condition**: Participants may block indefinitely if coordinator fails before sending commit/abort.

## Key Points

- Distributed concurrency control is more complex due to communication delays, independent failures, and lack of global clock.

- Lock-based approaches can be centralized (single point of failure), primary-copy (designated primary node), or fully distributed.

- Two-Phase Commit ensures atomicity but suffers from blocking problem during coordinator failure.

- Three-Phase Commit eliminates blocking but adds complexity and communication overhead.

- Timestamp-based protocols ensure serializability without locks but may cause transaction restarts.

- Distributed deadlock detection uses wait-for graphs across multiple nodes; the Chandy-Misra-Haas algorithm is the standard approach.

- CAP theorem states that during network partitioning, systems must choose between consistency and availability.

## Common Mistakes to Avoid

- Confusing Two-Phase Commit with Two-Phase Locking—they are different concepts (commit protocol vs. locking protocol).

- Assuming global timestamps exist—they must be generated using logical clocks or hybrid approaches.

- Ignoring the blocking problem in 2PC—it can cause system-wide hangs during coordinator failures.

- Believing distributed deadlocks are detected instantly—they require communication and computation across nodes.

## Revision Tips

1. Focus on understanding 2PC thoroughly—it's the most frequently examined protocol.

2. Practice drawing and analyzing wait-for graphs for deadlock detection problems.

3. Remember the key difference between centralized and distributed lock management approaches.

4. Know the CAP theorem trade-offs in the context of distributed databases.

5. Review the ACID properties and how they are preserved (or relaxed) in distributed systems.
