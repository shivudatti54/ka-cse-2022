# Additional Features of SQL - Summary

## Key Definitions and Concepts

- **View:** A virtual table defined by a SQL query that does not store data physically but provides a customized representation of data from one or more tables
- **Sequence:** A database object that generates a sequence of unique numbers, commonly used for auto-incrementing primary key values
- **Index:** A database object that improves the speed of data retrieval operations by creating a quick access path to table data
- **Integrity Constraint:** Rules enforced on table data to maintain accuracy, consistency, and validity
- **Subquery:** A query nested inside another query, used for retrieving data based on unknown values
- **Transaction:** A logical unit of work consisting of one or more SQL statements executed as a single unit

## Important Formulas and Theorems

- **CREATE VIEW:** `CREATE VIEW view_name AS SELECT ... FROM ... WHERE ...`
- **CREATE SEQUENCE:** `CREATE SEQUENCE seq_name START WITH n INCREMENT BY n MAXVALUE n CYCLE/NOCYCLE`
- **CREATE INDEX:** `CREATE INDEX idx_name ON table(column)` or `CREATE UNIQUE INDEX idx_name ON table(column)`
- **Set Operations:** UNION, UNION ALL, INTERSECT, EXCEPT - combine results from multiple SELECT statements

## Key Points

1. Views provide data security, logical independence, and simplify complex queries
2. Sequences generate unique numbers independently and can be shared across multiple tables
3. Indexes significantly improve SELECT query performance but slow down DML operations
4. PRIMARY KEY combines NOT NULL and UNIQUE constraints; FOREIGN KEY maintains referential integrity
5. CHECK constraint ensures values satisfy specified conditions; DEFAULT provides fallback values
6. UNION removes duplicates while UNION ALL retains all rows including duplicates
7. WHERE filters before grouping; HAVING filters groups after GROUP BY
8. Correlated subqueries reference the outer query and are executed for each row
9. TCL commands (COMMIT, ROLLBACK, SAVEPOINT) ensure atomicity of database operations

## Common Mistakes to Avoid

1. Confusing WHERE and HAVING - using WHERE with aggregate functions is incorrect
2. Creating too many indexes, which slows down DML operations unnecessarily
3. Forgetting that views are virtual and do not store actual data
4. Using UNION when UNION ALL would be more efficient (when duplicates don't matter)
5. Not understanding that complex views (with joins, aggregates) cannot be updated via DML

## Revision Tips

1. Practice creating views with different SELECT statements and query them
2. Write queries using sequences to understand NEXTVAL and CURRVAL usage
3. Compare query performance with and without indexes using EXPLAIN PLAN
4. Solve practice problems involving nested subqueries and correlated subqueries
5. Remember the order: SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY
6. Practice transaction control with COMMIT and ROLLBACK to understand atomicity
