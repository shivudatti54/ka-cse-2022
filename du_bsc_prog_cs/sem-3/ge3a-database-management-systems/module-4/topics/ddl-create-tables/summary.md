# DDL: CREATE TABLE Statement - Summary

## Key Definitions and Concepts

- **DDL (Data Definition Language):** SQL commands that define database structure (CREATE, ALTER, DROP)
- **CREATE TABLE:** Fundamental DDL command to define table structure with columns, data types, and constraints
- **Constraint:** Rule enforced on table columns to maintain data integrity
- **Primary Key:** Unique identifier for each row; cannot be NULL
- **Foreign Key:** Column that references primary key in another table, establishing relationships

## Important Formulas and Theorems

**Basic CREATE TABLE Syntax:**
```sql
CREATE TABLE table_name (
    column_name data_type [constraint],
    ...
);
```

**Constraint Types:**
- `column_name TYPE NOT NULL` - Mandatory field
- `column_name TYPE UNIQUE` - No duplicates
- `column_name TYPE PRIMARY KEY` - Unique identifier
- `column_name TYPE REFERENCES other_table(pk_column)` - Foreign key
- `column_name TYPE CHECK (condition)` - Value validation
- `column_name TYPE DEFAULT value` - Default value

## Key Points

1. Every table needs at least one column with a data type specified
2. PRIMARY KEY can be single column (column-level) or composite (table-level)
3. FOREIGN KEY establishes referential integrity between tables
4. CHECK constraint validates data against specified conditions
5. AUTO_INCREMENT generates sequential unique IDs (syntax varies by DB)
6. VARCHAR is preferred over CHAR for variable-length text
7. DEFAULT provides fallback values when no value is inserted
8. UNIQUE allows one NULL value in most database systems

## Common Mistakes to Avoid

1. Forgetting to specify column names before data types
2. Using table-level syntax for single-column primary keys unnecessarily
3. Confusing FOREIGN KEY syntax - missing REFERENCES keyword
4. Placing CHECK constraint at column level for multi-column conditions
5. Using CHAR for variable-length data (wastes space)
6. Forgetting that a table can have only ONE primary key
7. Not understanding that PRIMARY KEY columns are automatically NOT NULL

## Revision Tips

1. Practice writing CREATE TABLE statements for at least 5 different scenarios
2. Memorize the exact syntax for each constraint type
3. Understand the difference between column-level and table-level constraints
4. Know how to create composite primary keys using PRIMARY KEY (col1, col2)
5. Remember foreign key syntax: FOREIGN KEY (col) REFERENCES table(col)
6. Review sample exam questions from previous DU papers on this topic