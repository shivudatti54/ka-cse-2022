# Flat and Nested Distributed Transactions - Summary

## Key Definitions and Concepts

- **Distributed Transaction**: A transaction that spans multiple independent resources (databases, services) across different nodes and requires coordination to maintain data consistency

- **Flat Transaction**: A single-level transaction where all operations execute in one linear sequence without nesting

- **Nested Transaction**: A hierarchical transaction model allowing parent transactions to spawn child sub-transactions that can execute independently

- **Two-Phase Commit (2PC)**: A coordination protocol with prepare and commit phases where the coordinator gathers votes from participants before deciding to commit or abort

- **Three-Phase Commit (3PC)**: A non-blocking commit protocol with prepare, pre-commit, and commit phases that eliminates the blocking problem of 2PC

- **Compensating Transaction**: An operation that undoes the effects of a previously committed sub-transaction in open nested transactions

## Important Formulas and Theorems

- **ACID Properties**: Atomicity, Consistency, Isolation, Durability—the fundamental guarantees required for transactions

- **Two-Phase Locking (2PL)**: Growing phase (locks acquired) followed by shrinking phase (locks released)—ensures serializability

- **Timestamp Ordering**: Transactions ordered by timestamps; operations allowed if they maintain timestamp-based serializability

## Key Points

1. Flat transactions provide simplicity but cannot partially commit—entire transaction succeeds or fails together

2. The two-phase commit protocol ensures atomicity but is blocking; if coordinator fails after prepare, participants may wait indefinitely

3. Nested transactions improve fault tolerance and concurrency by allowing sub-transactions to execute independently

4. Open nested transactions allow sub-transactions to commit early, requiring compensating transactions for potential rollback

5. Distributed concurrency control can use locking, timestamps, or optimistic approaches, each with trade-offs

6. Deadlock detection in distributed systems requires coordination across nodes—centralized, hierarchical, or distributed approaches exist

7. The choice between flat and nested transactions depends on application requirements for atomicity, performance, and fault tolerance

## Common Mistakes to Avoid

1. Confusing flat transactions with simple transactions—flat transactions can span multiple nodes but have no nesting

2. Believing 2PC is non-blocking—it can block when coordinator fails after participants vote prepare

3. Forgetting that open nested transactions require explicit compensation logic, not traditional rollback

4. Assuming distributed deadlock detection is identical to centralized deadlock detection—it requires coordination across multiple nodes

5. Overlooking the performance overhead of distributed transactions due to network latency and coordination messages

## Revision Tips

1. Draw the two-phase commit protocol flow diagram and explain each step from both coordinator and participant perspectives

2. Create a comparison table for flat vs. nested transactions covering structure, fault tolerance, concurrency, and complexity

3. Practice tracing through 2PC with a failure scenario at each possible point to understand failure handling

4. Remember that exam questions often ask for advantages/disadvantages, so prepare comparative analysis

5. Review the ACID properties for each transaction model to reinforce conceptual understanding
