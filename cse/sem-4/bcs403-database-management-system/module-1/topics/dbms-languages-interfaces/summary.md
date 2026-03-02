# Database Languages and Interfaces - Summary

## Key Definitions and Concepts

- **DDL (Data Definition Language)**: SQL commands for defining database structure—CREATE, ALTER, DROP, TRUNCATE, RENAME. Auto-committed operations.
- **DML (Data Manipulation Language)**: SQL commands for data manipulation—SELECT, INSERT, UPDATE, DELETE. Require explicit COMMIT/ROLLBACK.
- **DCL (Data Control Language)**: Commands for access control—GRANT (give privileges) and REVOKE (remove privileges).
- **TCL (Transaction Control Language)**: Commands for transaction management—COMMIT (save), ROLLBACK (undo), SAVEPOINT (checkpoint), SET TRANSACTION.

## Important Formulas and Theorems

- **ACID Properties**: Atomicity (all or nothing), Consistency (valid state), Isolation (concurrent transactions), Durability (committed data permanent).
- **Transaction States**: Active, Partially Committed, Committed, Failed, Terminated.

## Key Points

- DDL commands are auto-committed; DML requires manual commitment
- DROP deletes table structure permanently; TRUNCATE removes data only
- GRANT provides privileges; REVOKE removes them
- SELECT is the most frequently used SQL command
- TCL ensures data integrity through COMMIT/ROLLBACK operations
- Database interfaces include CLI (command-line), GUI (graphical), API (programming), and web-based
- Constraints enforce data integrity: PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, NOT NULL

## Common Mistakes to Avoid

- Forgetting to COMMIT after DML operations, leading to uncommitted changes being lost
- Confusing DROP (removes table) with DELETE (removes rows) with TRUNCATE (removes all rows)
- Not understanding that GRANT/REVOKE require appropriate privileges to execute
- Using WHERE clause with TRUNCATE (not allowed—truncates entire table)

## Revision Tips

1. Practice writing all types of SQL commands—DDL, DML, DCL, TCL—repeatedly
2. Remember the sequence: DDL → DCL → DML → TCL for database operations
3. Focus on understanding constraints and their implementations
4. Review transaction management concepts thoroughly as they're frequently tested
