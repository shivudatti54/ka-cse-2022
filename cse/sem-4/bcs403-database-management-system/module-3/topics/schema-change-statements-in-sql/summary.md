# Schema Change Statements in SQL - Summary

## Key Definitions and Concepts

- **DDL (Data Definition Language)**: SQL commands that define database structure including CREATE, ALTER, and DROP statements. These automatically commit and cannot be rolled back in most database systems.

- **Schema Change Statements**: DDL commands that modify the structure of existing database objects after their initial creation.

- **ALTER TABLE**: Primary command for modifying table structure by adding, modifying, or dropping columns and constraints.

- **Constraint**: A rule enforced on table columns to maintain data integrity, including PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, and CHECK.

## Important Formulas and Syntax

```sql
-- Add column
ALTER TABLE table_name ADD COLUMN column_name datatype;

-- Modify column
ALTER TABLE table_name MODIFY COLUMN column_name new_datatype;

-- Drop column
ALTER TABLE table_name DROP COLUMN column_name;

-- Drop table completely
DROP TABLE table_name;

-- Remove all data (keep structure)
TRUNCATE TABLE table_name;

-- Create index
CREATE INDEX index_name ON table_name(column_name);

-- Drop index
DROP INDEX index_name ON table_name;
```

## Key Points

1. ALTER TABLE modifies existing table structure without losing existing data, while DROP TABLE removes the entire table definition.

2. TRUNCATE is faster than DELETE for removing all rows because it deallocates pages rather than deleting rows individually.

3. When adding a column with a default value, existing rows automatically receive the default value.

4. Dropping a column permanently removes data and cannot be undone without restoration from backup.

5. Indexes improve query performance but add overhead for INSERT, UPDATE, and DELETE operations.

6. Views are virtual tables defined by queries; dropping a view does not affect underlying table data.

7. Schema changes should be performed during maintenance windows to minimize impact on users.

## Common Mistakes to Avoid

1. Trying to reduce column size when data exists that would exceed the new size limit.

2. Dropping columns that are part of foreign key constraints without first dropping the constraint.

3. Using DELETE instead of TRUNCATE for large tables when performance is critical.

4. Forgetting to use IF EXISTS clauses, causing scripts to fail when run multiple times.

5. Not considering the impact of schema changes on dependent views, stored procedures, and application code.

## Revision Tips

1. Practice writing ALTER TABLE commands for adding, modifying, and dropping multiple columns in a single statement.

2. Memorize the differences between DROP, TRUNCATE, and DELETE with respect to transaction handling and performance.

3. Remember that most database systems require committing before DDL changes become visible to other sessions.

4. Review index creation syntax for different database systems (MySQL, Oracle, PostgreSQL, SQL Server) as syntax varies.

5. Understand that some schema changes like changing data types may require table recreation if incompatible.
