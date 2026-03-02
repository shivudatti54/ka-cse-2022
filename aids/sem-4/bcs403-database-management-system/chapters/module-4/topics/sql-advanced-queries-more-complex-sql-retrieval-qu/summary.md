# **SQL: Advanced Queries: More complex SQL retrieval queries**

### Overview

This module covers advanced SQL retrieval queries, including more complex queries and techniques.

### Key Points

- **Subqueries**
  - Definition: A query nested inside another query
  - Types: correlated subqueries, non-correlated subqueries
  - Formula: `(SELECT ... FROM ... WHERE ...)` used inside `FROM` or `WHERE` clauses
- **Joins**
  - Definition: Combining rows from two or more tables based on a related column
  - Types: inner join, left join, right join, full outer join
  - Formula: `JOIN table_name ON table1.column = table2.column`
- **Grouping and Aggregation**
  - Definition: Grouping rows and performing calculations on grouped rows
  - Formula: `GROUP BY column`, `HAVING condition`, `SUM`, `AVG`, `MAX`, `MIN`, etc.
- **Window Functions**
  - Definition: Calculating values over a set of rows that are related to the current row
  - Formula: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `NTILE()`, etc.
- **Common Table Expressions (CTEs)**
  - Definition: Temporary result sets that can be referenced within a query
  - Formula: `WITH cte AS (SELECT ... FROM ...) SELECT * FROM cte`
- **Indexing and Optimization**
  - Definition: Improving query performance by using indexes and optimizing query plans
  - Formula: `CREATE INDEX index_name ON table_name (column)`, `EXPLAIN` statement

### Important Formulas, Definitions, and Theorems

- **IN operator**: `SELECT * FROM table_name WHERE column IN (SELECT column FROM table_name)`

### Revision Tips

- Practice writing complex queries to improve understanding and speed.
- Use online tools and databases to test query performance.
- Review indexing and optimization techniques to improve query performance.
