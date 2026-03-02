# **SQL: Advanced Queries: More Complex SQL Retrieval Queries**

### Overview

- Advanced SQL queries are used to retrieve complex data from a database.
- These queries involve multiple joins, subqueries, and aggregations.

### Key Concepts

- **Joins**:
  - INNER JOIN: Returns only matching rows from both tables.
  - LEFT JOIN: Returns all rows from the left table and matching rows from the right table.
  - RIGHT JOIN: Returns all rows from the right table and matching rows from the left table.
  - FULL OUTER JOIN: Returns all rows from both tables, including non-matching rows.
- **Subqueries**:
  - Subquery: A query nested inside another query.
  - Correlated subquery: Subquery is correlated with the outer query.
  - Non-correlated subquery: Subquery is not correlated with the outer query.
- **Aggregations**:
  - GROUP BY: Groups rows based on one or more columns.
  - HAVING: Filters groups based on a condition.
  - SUM, COUNT, AVG, MAX, MIN: Aggregate functions.
- **Window Functions**:
  - ROW_NUMBER(), RANK(), DENSE_RANK(): assigns a rank to each row.
  - LAG(), LEAD(): accesses adjacent rows.

### Important Formulas and Definitions

- **SQL JOIN Formula**:

```
SELECT *
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

- **Subquery Formula**:

```
SELECT *
FROM table1
WHERE column IN (SELECT column FROM table2 WHERE condition);
```

- **Aggregation Formula**:

```
SELECT column, SUM(value)
FROM table
GROUP BY column;
```

- **Window Function Formula**:

```
SELECT *
FROM (
  SELECT *, ROW_NUMBER() OVER (ORDER BY column) AS row_num
  FROM table
) AS subquery;
```

### Important Theorems

- **Distributive Law**: `A (B + C) = AB + AC`
- **Associative Law**: `(A + B)C = AC + BC`

### Quick Revision Tips

- Practice writing complex SQL queries to improve your problem-solving skills.
- Review the different types of joins, subqueries, and aggregations.
- Familiarize yourself with window functions and their applications.
