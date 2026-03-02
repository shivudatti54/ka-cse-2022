# SQL: Advanced Queries: More Complex SQL Retrieval Queries

**Table of Contents**

1. [Introduction](#introduction)
2. [Historical Context](#historical-context)
3. [Modern Developments](#modern-developments)
4. [Subqueries](#subqueries)
   - [Single-Column Subqueries](#single-column-subqueries)
   - [Multi-Column Subqueries](#multi-column-subqueries)
   - [Subquery with Join](#subquery-with-join)
5. [Correlated Subqueries](#correlated-subqueries)
   - [Using Correlated Subqueries](#using-correlated-subqueries)
   - [Benefits of Correlated Subqueries](#benefits-of-correlated-subqueries)
6. [Window Functions](#window-functions)
   - [ROW_NUMBER() Function](#row-number-function)
   - [RANK() Function](#rank-function)
   - [DENSE_RANK() Function](#dense_rank-function)
   - [NTILE() Function](#ntile-function)
   - [LAG() Function](#lag-function)
   - [LEAD() Function](#lead-function)
7. [Common Table Expressions (CTEs)](#common-table-expressions-ctes)
   - [Defining CTEs](#defining-ctes)
   - [Using CTEs in Queries](#using-ctes-in-queries)
8. [Full Outer Joins](#full-outer-joins)
9. [Left Outer Joins](#left-outer-joins)
10. [Right Outer Joins](#right-outer-joins)
11. [Full Outer Joins](#full-outer-joins)
12. [Indexing and Optimization](#indexing-and-optimization)
13. [Conclusion](#conclusion)
14. [Further Reading](#further-reading)

## **Introduction**

SQL (Structured Query Language) is a programming language designed for managing and manipulating data in relational database management systems (RDBMS). While SQL is a powerful language, it has limitations when it comes to retrieving complex data. Advanced queries are used to retrieve data from multiple tables, handle missing values, and optimize query performance.

In this module, we will explore more complex SQL retrieval queries, including subqueries, correlated subqueries, window functions, CTEs, full outer joins, and indexing and optimization.

## **Historical Context**

The first version of SQL, SQL/DS (Structured Query Language Data Server), was developed in 1979 by Donald Chamberlin and Raymond Boyce at the University of Utah. SQL/DS was designed to manage and manipulate data in relational databases, and it introduced many of the concepts that are still used in modern SQL.

In the 1980s, SQL/PSM (Structured Query Language Procedural Syntax Markup) was developed, which introduced procedural syntax and the ability to create stored procedures.

In the 1990s, SQL/92 (Structured Query Language, Second Edition) was developed, which introduced the standard syntax and structure for SQL.

Today, SQL is a widely used language for managing and manipulating data in RDBMS, and it continues to evolve with new features and technologies.

## **Modern Developments**

In recent years, there have been many advances in SQL, including:

- **SQL Server 2012**: Introduced the Generalized Aggregate Function (GAF) and the Analytic Functions.
- **PostgreSQL**: Introduced the Window Functions and the Common Table Expressions (CTEs).
- **MySQL**: Introduced the Window Functions and the Common Table Expressions (CTEs).
- **Oracle**: Introduced the JSON data type and the XML data type.
- **Microsoft Azure SQL Database**: Introduced the JSON data type and the XML data type.

## **Subqueries**

A subquery is a query that is nested inside another query. Subqueries are used to retrieve data from multiple tables or to perform complex calculations.

### Single-Column Subqueries

A single-column subquery is a subquery that returns only one column. Here is an example:

```sql
SELECT *
FROM customers
WHERE country IN (SELECT country FROM orders);
```

In this example, the subquery returns the `country` column from the `orders` table, which is then used in the main query to filter the `customers` table.

### Multi-Column Subqueries

A multi-column subquery is a subquery that returns multiple columns. Here is an example:

```sql
SELECT *
FROM customers
WHERE country IN (SELECT country, city FROM orders);
```

In this example, the subquery returns both the `country` and `city` columns from the `orders` table, which is then used in the main query to filter the `customers` table.

### Subquery with Join

A subquery with join is a subquery that is used with a join clause. Here is an example:

```sql
SELECT *
FROM customers
JOIN orders ON customers.country = orders.country
WHERE orders.total > 1000;
```

In this example, the subquery returns the `total` column from the `orders` table, which is then used in the main query to filter the `customers` table.

## **Correlated Subqueries**

A correlated subquery is a subquery that is used with a condition that references the outer query. Correlated subqueries are used to retrieve data from multiple tables or to perform complex calculations.

### Using Correlated Subqueries

A correlated subquery is used by adding the `WHERE` clause in the subquery to reference the outer query. Here is an example:

```sql
SELECT *
FROM customers
WHERE country IN (SELECT country FROM orders WHERE total > 1000);
```

In this example, the subquery returns the `country` column from the `orders` table, which is then used in the main query to filter the `customers` table based on the `total` column.

### Benefits of Correlated Subqueries

Correlated subqueries are used in many situations, including:

- **Retrieving data from multiple tables**: Correlated subqueries are used to retrieve data from multiple tables based on complex conditions.
- **Performing complex calculations**: Correlated subqueries are used to perform complex calculations that involve the outer query.

## **Window Functions**

A window function is a function that is used to retrieve data from a table while also referencing other rows in the table. Window functions are used to perform calculations across an entire row or a set of rows.

### ROW_NUMBER() Function

The `ROW_NUMBER()` function is used to assign a unique number to each row in the table. Here is an example:

```sql
SELECT *
FROM (SELECT *, ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
      FROM employees) AS subquery
WHERE row_num = 1;
```

In this example, the `ROW_NUMBER()` function is used to assign a unique number to each row in the `employees` table, and the main query then selects the row with the highest `salary`.

### RANK() Function

The `RANK()` function is used to rank rows in the table based on a specific column. Here is an example:

```sql
SELECT *
FROM (SELECT *, RANK() OVER (ORDER BY salary DESC) AS rank
      FROM employees) AS subquery
WHERE rank = 1;
```

In this example, the `RANK()` function is used to rank rows in the `employees` table based on the `salary` column, and the main query then selects the row with the highest `salary`.

### DENSE_RANK() Function

The `DENSE_RANK()` function is used to rank rows in the table based on a specific column, and to assign the same rank to rows with the same value. Here is an example:

```sql
SELECT *
FROM (SELECT *, DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
      FROM employees) AS subquery
WHERE dense_rank = 1;
```

In this example, the `DENSE_RANK()` function is used to rank rows in the `employees` table based on the `salary` column, and the main query then selects the row with the highest `salary`.

### NTILE() Function

The `NTILE()` function is used to partition rows in the table into a specified number of groups based on a specific column. Here is an example:

```sql
SELECT *
FROM (SELECT *, NTILE(4) OVER (ORDER BY salary DESC) AS ntile
      FROM employees) AS subquery
WHERE ntile = 1;
```

In this example, the `NTILE()` function is used to partition rows in the `employees` table into four groups based on the `salary` column, and the main query then selects the first group.

### LAG() Function

The `LAG()` function is used to reference a value from a previous row in the table. Here is an example:

```sql
SELECT *
FROM (SELECT *, LAG(salary) OVER (ORDER BY salary DESC) AS prev_salary
      FROM employees) AS subquery
WHERE salary = (SELECT MAX(salary) FROM employees);
```

In this example, the `LAG()` function is used to reference the `salary` value from the previous row in the `employees` table, and the main query then selects the row with the highest `salary`.

### LEAD() Function

The `LEAD()` function is used to reference a value from a next row in the table. Here is an example:

```sql
SELECT *
FROM (SELECT *, LEAD(salary) OVER (ORDER BY salary DESC) AS next_salary
      FROM employees) AS subquery
WHERE salary = (SELECT MAX(salary) FROM employees);
```

In this example, the `LEAD()` function is used to reference the `salary` value from the next row in the `employees` table, and the main query then selects the row with the highest `salary`.

## **Common Table Expressions (CTEs)**

A CTE is a temporary result set that is defined within the execution of a single SQL statement. CTEs are used to simplify complex queries and to improve readability.

### Defining CTEs

A CTE is defined using the `WITH` clause. Here is an example:

```sql
WITH employees AS (
  SELECT *
  FROM employees
  WHERE salary > 50000
)
SELECT *
FROM employees;
```

In this example, the CTE `employees` is defined to select rows from the `employees` table where `salary` is greater than 50000, and the main query then selects all rows from the CTE.

### Using CTEs in Queries

CTEs can be used in a variety of ways, including:

- **Simplifying complex queries**: CTEs can be used to simplify complex queries by breaking them down into smaller, more manageable pieces.
- **Improving readability**: CTEs can be used to improve readability by giving a clear and concise name to a complex query.
- **Reducing repetition**: CTEs can be used to reduce repetition by avoiding the need to repeat complex queries.

## **Full Outer Joins**

A full outer join is a type of join that returns all rows from both tables, including rows that do not have a match in the other table. Here is an example:

```sql
SELECT *
FROM customers
FULL OUTER JOIN orders ON customers.country = orders.country;
```

In this example, the full outer join is used to combine the `customers` and `orders` tables based on the `country` column, and the resulting table includes all rows from both tables.

## **Left Outer Joins**

A left outer join is a type of join that returns all rows from the left table, and the matching rows from the right table. If there is no match, the result is NULL on the right side. Here is an example:

```sql
SELECT *
FROM customers
LEFT OUTER JOIN orders ON customers.country = orders.country;
```

In this example, the left outer join is used to combine the `customers` and `orders` tables based on the `country` column, and the resulting table includes all rows from the `customers` table.

## **Right Outer Joins**

A right outer join is a type of join that returns all rows from the right table, and the matching rows from the left table. If there is no match, the result is NULL on the left side. Here is an example:

```sql
SELECT *
FROM customers
RIGHT OUTER JOIN orders ON customers.country = orders.country;
```

In this example, the right outer join is used to combine the `customers` and `orders` tables based on the `country` column, and the resulting table includes all rows from the `orders` table.

## **Indexing and Optimization**

Indexing and optimization are used to improve the performance of SQL queries by reducing the amount of data that needs to be scanned and by reducing the amount of computation required.

### Indexing

Indexing involves creating a data structure that allows the database to quickly locate specific data. Indexes can be created on individual columns or on multiple columns.

### Optimization

Optimization involves modifying the query to improve its performance. This can involve optimizing the query plan, rewriting the query, or using caching.

## **Conclusion**

In this module, we have explored more complex SQL retrieval queries, including subqueries, correlated subqueries, window functions, CTEs, full outer joins, and indexing and optimization.

These advanced queries are used to retrieve data from multiple tables, handle missing values, and optimize query performance.

We hope that this module has provided you with a comprehensive understanding of advanced SQL retrieval queries and has helped you to improve your skills in using these complex queries to retrieve data from relational database management systems.

## **Further Reading**

- **SQL Tutorial by W3Schools**: A comprehensive tutorial on SQL, including topics such as data types, indexing, and optimization.
- **SQL Tutorial by Tutorials Point**: A comprehensive tutorial on SQL, including topics such as data types, indexing, and optimization.
- **SQL Course by edX**: A comprehensive course on SQL, including topics such as data types, indexing, and optimization.
- **SQL Book by O'Reilly Media**: A comprehensive book on SQL, including topics such as data types, indexing, and optimization.
