# **SQL: Advanced Queries: More Complex SQL Retrieval Queries**

## **Module Overview**

- Duration: 8 hours
- Topic: Advanced SQL queries for complex retrieval

## **Key Concepts**

### 1. Subqueries

- Definition: A subquery is a query nested inside another query.
- Types:
  - Single-column subquery
  - Multiple-column subquery
- Syntax: `SELECT * FROM table_name WHERE column_name = (SELECT column_name FROM another_table_name)`

### 2. Joins

- Definition: A join is a way to combine rows from two or more tables based on a related column.
- Types:
  - Inner join
  - Left join (or left outer join)
  - Right join (or right outer join)
  - Full outer join
- Syntax:
  - Inner join: `SELECT * FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name`
  - Left join: `SELECT * FROM table1 LEFT JOIN table2 ON table1.column_name = table2.column_name`

### 3. Grouping and Aggregation

- Definition: Grouping and aggregation involve grouping rows by one or more columns and applying aggregate functions.
- Syntax:
  - `GROUP BY` clause: `SELECT column_name, aggregate_function(column_name) FROM table_name GROUP BY column_name`
  - Aggregate functions:
    - `SUM`: calculates the sum of a column
    - `AVG`: calculates the average of a column
    - `COUNT`: counts the number of rows in a group
    - `MAX` and `MIN`: returns the maximum and minimum values in a group, respectively

### 4. Window Functions

- Definition: Window functions are used to perform calculations across a set of rows that are related to the current row.
- Syntax:
  - `ROW_NUMBER()`: assigns a unique row number to each row within a partition
  - `RANK()`: assigns a rank to each row within a partition based on the value
  - `LAG()` and `LEAD()`: returns the value of a column from a previous or next row, respectively

### 5. Common Table Expressions (CTEs)

- Definition: A CTE is a temporary result set that is defined within a SQL statement.
- Syntax:
  - `WITH` clause: `WITH cte AS (SELECT column_name FROM table_name)`
