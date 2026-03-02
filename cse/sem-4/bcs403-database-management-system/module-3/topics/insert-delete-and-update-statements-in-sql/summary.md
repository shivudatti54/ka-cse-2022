# Insert, Delete, and Update Statements in SQL - Summary

## Key Definitions and Concepts

- **INSERT**: DML statement used to add new rows of data into a table
- **UPDATE**: DML statement used to modify existing values in one or more columns
- **DELETE**: DML statement used to remove rows from a table based on conditions
- **Transaction**: A sequence of SQL operations treated as a single unit of work
- **COMMIT**: Makes all changes in a transaction permanent
- **ROLLBACK**: Undoes all changes in the current transaction
- **DEFAULT**: Keyword to insert default value defined during table creation

## Important Formulas and Syntax

**INSERT Syntax:**

```sql
INSERT INTO table (col1, col2) VALUES (val1, val2);
INSERT INTO table SELECT ... FROM other_table;
```

**UPDATE Syntax:**

```sql
UPDATE table SET col1 = val1, col2 = val2 WHERE condition;
```

**DELETE Syntax:**

```sql
DELETE FROM table WHERE condition;
```

## Key Points

- INSERT requires specifying values for NOT NULL columns; DEFAULT can be used for columns with default values
- UPDATE without WHERE clause affects all rows in the table
- DELETE without WHERE clause removes all rows but maintains table structure
- DELETE is DML (can be rolled back), TRUNCATE is DDL (cannot be rolled back in most databases)
- Multiple rows can be inserted in a single INSERT statement
- UPDATE can modify multiple columns in one statement using comma separation
- Transactions ensure atomicity - either all operations succeed or none do
- Subqueries can be used in INSERT, UPDATE, and DELETE for advanced operations
- String and date values require single quotes; numeric values do not
- WHERE clause is critical for UPDATE and DELETE to prevent unintended modifications

## Common Mistakes to Avoid

1. **Forgetting WHERE clause**: This causes UPDATE/DELETE to affect all rows, often resulting in data loss
2. **Incorrect quote usage**: Using double quotes or no quotes for string/date values
3. **Column-value mismatch**: Not matching the order of columns with values when column list is omitted
4. **Confusing DELETE with DROP**: DELETE removes data only, DROP removes the entire table structure

## Revision Tips

1. Practice writing all three statements with various WHERE conditions
2. Remember the sequence: INSERT adds new data, UPDATE modifies existing, DELETE removes
3. Always test UPDATE and DELETE queries with SELECT first to verify affected rows
4. Understand transaction control - COMMIT saves changes, ROLLBACK reverts them
5. Review the difference between DELETE (row-by-row, can rollback) and TRUNCATE (deallocates space, faster, may not rollback)
