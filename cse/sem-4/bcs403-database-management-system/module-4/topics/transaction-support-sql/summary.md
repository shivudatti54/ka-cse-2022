# Transaction Support in SQL - Summary

## Key Definitions and Concepts

- **Transaction**: A logical unit of work consisting of one or more SQL statements that execute as a single atomic unit.
- **ACID Properties**: Atomicity (all or nothing), Consistency (valid state to valid state), Isolation (concurrent appears serial), Durability (permanent results).
- **COMMIT**: SQL statement that permanently saves all changes made in the current transaction.
- **ROLLBACK**: SQL statement that undoes all uncommitted changes in the current transaction.
- **SAVEPOINT**: A named checkpoint within a transaction allowing partial rollback without affecting earlier operations.

## Important Formulas and Theorems

- **Transaction States**: Active → Partially Committed → Committed (or) Failed → Aborted
- **Isolation Level Problems**: Dirty Read → Non-repeatable Read → Phantom Read (increasing severity)
- **Isolation Levels Order**: READ UNCOMMITTED < READ COMMITTED < REPEATABLE READ < SERIALIZABLE (increasing isolation/decreasing concurrency)

## Key Points

1. Transactions ensure database remains consistent even during system failures or concurrent access.
2. COMMIT releases all locks held by the transaction; ROLLBACK restores database to pre-transaction state.
3. SAVEPOINT creates intermediate recovery points within a transaction.
4. READ UNCOMMITTED allows reading uncommitted data (dirty reads possible).
5. READ COMMITTED prevents dirty reads but allows non-repeatable reads.
6. REPEATABLE READ prevents dirty reads and non-repeatable reads but allows phantom reads.
7. SERIALIZABLE is the highest isolation level, preventing all concurrency anomalies.
8. Higher isolation levels provide better data integrity but reduce concurrent execution.
9. Most databases default to READ COMMITTED isolation level.
10. Transaction control is essential for applications involving multiple related DML operations.

## Common Mistakes to Avoid

1. Forgetting to COMMIT after successful operations leaves data uncommitted and locks held.
2. Assuming ROLLBACK affects only the last statement (it affects entire transaction unless SAVEPOINT is used).
3. Using inappropriate isolation levels that either cause data inconsistencies or unnecessarily reduce performance.
4. Not checking for errors in transactions, leading to partial commits.

## Revision Tips

1. Practice writing transactions with COMMIT and ROLLBACK for scenarios like fund transfers and inventory updates.
2. Remember the ACID mnemonic: "Always Consistency In Databases" or create your own memory aid.
3. Understand that higher isolation = more protection = less concurrency (trade-off).
4. Review SQL Server and Oracle differences in transaction syntax.
5. Solve previous university exam questions on transaction control statements and isolation levels.
