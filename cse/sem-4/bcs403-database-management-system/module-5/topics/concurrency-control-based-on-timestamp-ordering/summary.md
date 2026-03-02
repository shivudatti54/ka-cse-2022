# Concurrency Control Based on Timestamp Ordering - Summary

## Key Definitions and Concepts

- **Timestamp**: A unique identifier (typically a monotonically increasing number or system time) assigned to each transaction at the start of execution. Older timestamps have higher priority.

- **Timestamp Ordering Protocol**: A concurrency control method that ensures conflicting operations are executed in timestamp order. Uses Read_Timestamp and Write_Timestamp values for each data item.

- **Read_Timestamp(Q)**: The largest timestamp among all transactions that have successfully read data item Q.

- **Write_Timestamp(Q)**: The largest timestamp among all transactions that have successfully written data item Q.

- **Thomas' Write Rule**: An optimization allowing certain write operations to be treated as no-ops rather than causing transaction rollback.

## Important Formulas and Theorems

**Read Operation Rule:**

- If TS(T_i) ≥ Write_Timestamp(Q): Read succeeds, update Read_Timestamp(Q) = max(Read_Timestamp(Q), TS(T_i))
- If TS(T_i) < Write_Timestamp(Q): Transaction T_i is rolled back

**Write Operation Rule:**

- If TS(T_i) ≥ Read_Timestamp(Q) AND TS(T_i) ≥ Write_Timestamp(Q): Write succeeds, update Write_Timestamp(Q) = TS(T_i)
- Otherwise: Transaction T_i is rolled back

**Thomas' Write Rule:**

- If TS(T_i) < Write_Timestamp(Q): Ignore the write (no-op) instead of rolling back

## Key Points

- Timestamp ordering is an optimistic concurrency control technique that does not use locks
- Each transaction is assigned a unique timestamp at the start of execution
- Older timestamps have higher priority—transactions with smaller timestamp values execute first
- The protocol ensures conflict-serializable schedules by rejecting operations that would violate timestamp order
- Deadlock is impossible in timestamp ordering due to predetermined execution order
- Cascading rollbacks can occur in basic timestamp ordering but can be prevented in strict timestamp ordering
- Thomas' Write Rule improves throughput by converting certain rejected writes into no-ops
- Starvation is possible if a transaction repeatedly faces conflicts with younger transactions

## Common Mistakes to Avoid

- Confusing the direction of timestamp comparison—remember older timestamps (smaller values) have priority
- Believing timestamp ordering completely eliminates rollbacks—it can still cause transaction rollbacks
- Mixing up Read_Timestamp and Write_Timestamp—each serves different purposes in the protocol
- Forgetting that Thomas' Write Rule applies only to writes, not reads

## Revision Tips

1. Practice with at least 3-4 timestamp ordering examples to understand how read/write operations are validated
2. Remember the golden rule: if TS(T_i) < Write_Timestamp(Q) for a read operation, the transaction must be rolled back
3. Compare timestamp ordering with two-phase locking—both achieve conflict serializability but through different mechanisms
4. Focus on understanding when transactions get rolled back—this is the most common exam question pattern
5. Review the conditions for Thomas' Write Rule and how it optimizes the basic protocol
