# Specifying Constraints as Assertions and Action Triggers - Summary

## Key Definitions and Concepts

- **Assertion**: A declarative constraint that enforces a condition which must always be true across the entire database, involving multiple tables.
- **Trigger**: An event-driven database object that automatically executes specific actions in response to INSERT, UPDATE, or DELETE operations.
- **Row-level Trigger**: Executes once for each row affected by the triggering statement.
- **Statement-level Trigger**: Executes once for the entire triggering statement.
- **Mutating Table**: A table currently being modified by a DML operation, which cannot be queried or modified by a row-level trigger on the same table.

## Important Formulas and Trigger Components

**Assertion Syntax:**

```sql
CREATE ASSERTION assertion_name CHECK (condition);
```

**Trigger Syntax:**

```sql
CREATE TRIGGER trigger_name
{BEFORE | AFTER | INSTEAD OF}
{INSERT | UPDATE | DELETE} ON table_name
[FOR EACH ROW] [WHEN condition]
BEGIN
    -- trigger body
END;
```

## Key Points

- Assertions provide declarative enforcement of complex business rules spanning multiple tables.
- Triggers can perform automated actions before or after data modifications.
- BEFORE triggers are used for data validation and modification; AFTER triggers for auditing.
- INSTEAD OF triggers enable DML operations on complex, non-updatable views.
- :OLD references contain existing values; :NEW references contain new values.
- RAISE_APPLICATION_ERROR is used to raise custom error messages in triggers.
- The WHEN clause allows conditional trigger execution based on specific criteria.
- Commercial DBMS have limited support for assertions compared to triggers.
- Triggers maintain data integrity through automated enforcement of business rules.

## Common Mistakes to Avoid

1. **Mutating table errors**: Querying or modifying the triggering table within a row-level trigger.
2. **Incorrect timing**: Using AFTER triggers when data validation should occur before modification.
3. **Forgetting :NEW and :OLD prefixes**: In Oracle PL/SQL triggers, these must be prefixed with colons.
4. **Empty trigger body**: Triggers without proper logic may pass silently without enforcing rules.
5. **Recursive triggers**: Creating triggers that cause infinite loops by triggering themselves.

## Revision Tips

1. Practice writing triggers for common scenarios like audit logging and data validation.
2. Remember the sequence: BEFORE trigger fires → DML executes → AFTER trigger fires.
3. Use flowcharts to determine when to use assertions vs. triggers.
4. Review the differences between row-level and statement-level triggers.
5. Understand that assertions are checked after DML, and any violation causes transaction rollback.
