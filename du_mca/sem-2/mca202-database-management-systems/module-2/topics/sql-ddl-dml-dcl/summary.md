# SQL DDL, DML, DCL - Summary

## Key Definitions and Concepts
- **DDL**: Schema definition commands (CREATE, ALTER, DROP)
- **DML**: Data manipulation commands (SELECT, INSERT, UPDATE, DELETE)
- **DCL**: Access control commands (GRANT, REVOKE)
- **Transaction**: Logical unit of work with ACID properties

## Important Formulas and Theorems
- **Referential Integrity**: FOREIGN KEY REFERENCES parent_table(col)
- **Aggregation**: `SUM()/COUNT() + GROUP BY + HAVING`
- **Privilege Syntax**: `GRANT privilege_list ON object TO user/role`

## Key Points
- DDL is auto-committed in most DBMS; DML requires explicit COMMIT
- Always use WHERE clause in UPDATE/DELETE to prevent mass data changes
- INNER JOIN vs LEFT JOIN changes result set cardinality
- Column-level privileges require precise DCL statements
- CASCADE in DROP TABLE removes dependent objects
- CHECK constraints validate data before insertion
- Indexes (created via DDL) dramatically improve SELECT performance

## Common Mistakes to Avoid
- Confusing TRUNCATE (DDL) with DELETE (DML)
- Omitting JOIN conditions leading to Cartesian products
- Granting excessive privileges violating least-privilege principle
- Forgetting to COMMIT after DML in manual transaction mode

## Revision Tips
1. Create cheat sheets for DDL/DML/DCL syntax patterns
2. Practice writing nested queries with EXISTS/NOT EXISTS
3. Use Oracle LiveSQL or MySQL Workbench for hands-on testing
4. Study error messages: ORA-00942 (missing privileges) vs ORA-02291 (FK violation)