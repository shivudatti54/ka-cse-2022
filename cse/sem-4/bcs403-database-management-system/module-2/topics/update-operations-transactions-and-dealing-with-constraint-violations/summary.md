# Update Operations, Transactions, and Constraint Violations - Summary

## Key Definitions

- **Transaction**: A logical unit of work consisting of one or more database operations that transforms the database from one consistent state to another.

- **Integrity Constraint**: A rule defined on database schema that must be satisfied by any valid database state.

- **Referential Integrity**: The constraint that ensures foreign key values either match primary key values in the referenced relation or are null.

- **ACID Properties**: Four properties (Atomicity, Consistency, Isolation, Durability) that guarantee reliable transaction processing.

- **Rollback**: The process of undoing the effects of a partially executed transaction.

- **Commit**: The process of permanently saving the effects of a successfully completed transaction.

## Important Formulas

- **Transaction Success Criteria**: 
  - If all operations succeed → COMMIT
  - If any operation fails → ROLLBACK (atomicity)

- **Referential Actions** (for DELETE/UPDATE on parent):
  - NO ACTION: Reject the operation
  - CASCADE: Apply same operation to child tuples
  - SET NULL: Set foreign key to NULL
  - SET DEFAULT: Set foreign key to default value

## Key Points

1. Three update operations: INSERT (adds tuples), DELETE (removes tuples), UPDATE (modifies attribute values).

2. Transactions provide atomicity—either all operations succeed or none take effect.

3. Consistency is preserved by enforcing integrity constraints during transaction execution.

4. Isolation ensures concurrent transactions don't interfere with each other.

5. Durability guarantees committed transactions survive system failures.

6. Constraint violations during INSERT are typically rejected by the DBMS.

7. DELETE operations may cascade, set null, set default, or be rejected based on referential actions.

8. UPDATE can violate key constraints if modifying primary keys to duplicate values.

9. Deferred constraint checking allows violations within a transaction but checks at commit time.

10. Transactions move through states: Active → Partially Committed → Committed (or Aborted).

## Common Mistakes

1. **Confusing COMMIT and ROLLBACK**: Remember COMMIT makes changes permanent; ROLLBACK undoes them.

2. **Ignoring referential actions**: Many students forget that foreign key constraints have defined actions beyond just rejection.

3. **Assuming immediate rollback on any error**: Some errors may be handled differently depending on constraint definition and deferred checking settings.

4. **Forgetting that transactions ensure consistency**: Not all "errors" cause rollback—only constraint violations or system failures.