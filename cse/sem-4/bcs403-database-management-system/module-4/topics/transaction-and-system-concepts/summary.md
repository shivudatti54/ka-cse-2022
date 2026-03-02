# Transaction and System Concepts - Summary

## Key Definitions and Concepts

- **Transaction**: A logical unit of work consisting of one or more database operations that transforms the database from one consistent state to another.

- **Schedule**: A sequence of operations from multiple concurrent transactions executed in a specific time order.

- **Serializability**: A property of a schedule where the concurrent execution produces the same result as some serial execution of the same transactions.

- **Conflict Serializability**: A schedule can be transformed into a serial schedule by swapping non-conflicting operations.

- **Deadlock**: A situation where two or more transactions are waiting indefinitely for locks held by each other.

## Important Formulas and Theorems

- **Precedence Graph**: Used to test conflict serializability. A schedule is conflict serializable if and only if its precedence graph is acyclic.

- **Two-Phase Locking (2PL)**: Growing phase (acquire locks) → Shrinking phase (release locks). Ensures conflict serializability but may cause deadlocks.

- **Conflict Operations**: Two operations conflict if: (i) they belong to different transactions, (ii) at least one is a write, and (iii) they access the same data item.

## Key Points

- ACID properties (Atomicity, Consistency, Isolation, Durability) are fundamental to transaction processing.

- Transaction states: Active → Partially Committed → Committed (or) Active → Failed → Aborted.

- Serial schedules are always correct but inefficient; serializable schedules balance correctness and efficiency.

- 2PL is the most widely used concurrency control protocol in commercial database systems.

- Log-based recovery uses undo (for uncommitted transactions) and redo (for committed transactions) operations.

- Checkpoints reduce recovery time by limiting the log processing to transactions after the last checkpoint.

## Common Mistakes to Avoid

1. Confusing serializability with serial schedules—serializable schedules can be concurrent but produce equivalent results to serial execution.

2. Forgetting that isolation allows intermediate results to be hidden from other transactions until commit.

3. Assuming that conflict serializability and view serializability are the same—they are related but different concepts.

4. Overlooking the fact that deadlock is a possibility in lock-based concurrency control, requiring detection and recovery mechanisms.

## Revision Tips

1. Draw the transaction state diagram from memory and label all transitions.

2. Practice constructing precedence graphs for at least 5 different schedules to master conflict serializability testing.

3. Remember: All serial schedules are serializable, but not all serializable schedules are serial.

4. For exams, focus on ACID properties with examples, 2PL protocol phases, and simple serializability tests.
