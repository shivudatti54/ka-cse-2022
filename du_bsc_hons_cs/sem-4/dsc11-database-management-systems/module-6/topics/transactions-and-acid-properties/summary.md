# Transactions and ACID Properties - Summary

## Key Definitions and Concepts

- **Transaction**: A logical unit of work consisting of one or more SQL statements executed as a single atomic unit that transforms the database from one consistent state to another.

- **ACID Properties**: The four fundamental properties (Atomicity, Consistency, Isolation, Durability) that ensure reliable transaction processing in database systems.

- **Commit**: A statement that permanently saves all changes made during a transaction to the database.

- **Rollback**: A statement that undoes all changes made during a transaction, restoring the database to its state before the transaction began.

- **Serializability**: A property of concurrent transaction schedules that ensures the same result as some serial execution of the same transactions.

## Important Formulas and Theorems

- **Two-Phase Locking (2PL) Protocol**: Growing phase (acquire locks only) → Shrinking phase (release locks only)
- **Conflict Serializability**: Two operations conflict if they operate on the same data item and at least one is a write operation

## Key Points

- A transaction is the fundamental unit of work in database systems, ensuring logical grouping of related operations.

- **Atomicity** ensures all-or-nothing execution—no partial results are visible to other transactions or persisted in the database.

- **Consistency** guarantees that a transaction leaves the database in a valid state, satisfying all integrity constraints.

- **Isolation** prevents concurrent transactions from interfering with each other, making each transaction appear to execute alone.

- **Durability** ensures that committed transactions survive system failures and are permanently stored.

- Transaction states: Active → Partially Committed → Committed (or Failed → Aborted)

- Common concurrency control techniques include locking protocols (2PL) and timestamp-based protocols.

- Higher isolation levels prevent more anomalies but reduce concurrency and may impact performance.

## Common Mistakes to Avoid

1. Confusing COMMIT with saving data—COMMIT makes changes permanent, while ROLLBACK undoes them completely.

2. Assuming transactions are always isolated—different isolation levels allow varying degrees of visibility into uncommitted changes.

3. Believing serializable schedules always require sequential execution—they just need to produce equivalent results to serial execution.

4. Forgetting that consistency is the responsibility of both the database system (constraints) and the application (business logic).

## Revision Tips

1. Practice writing SQL transactions with explicit BEGIN, COMMIT, and ROLLBACK statements to reinforce practical understanding.

2. Create a comparison table of isolation levels and the anomalies (dirty read, non-repeatable read, phantom read) each prevents.

3. Solve past exam questions on determining whether a schedule is serializable—this is a frequently tested concept.

4. Use real-world examples like banking transactions to remember how ACID properties work in practice.