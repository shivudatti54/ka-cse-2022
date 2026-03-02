# **SQL: Advanced Queries: More Complex SQL Retrieval Queries**

## **Table of Contents**

1. [Introduction](#introduction)
2. [Historical Context](#historical-context)
3. [Modern Developments](#modern-developments)
4. [Joining Tables](#joining-tables)
   - [Inner Join](#inner-join)
   - [Left Outer Join](#left-outer-join)
   - [Right Outer Join](#right-outer-join)
   - [Full Outer Join](#full-outer-join)
5. [Subqueries](#subqueries)
   - [Single-Row Subquery](#single-row-subquery)
   - [Multi-Row Subquery](#multi-row-subquery)
6. [Window Functions](#window-functions)
   - [ROW_NUMBER()](#row-number)
   - [RANK()](#rank)
   - [DENSE_RANK()](#dense_rank)
   - [NTILE()](#ntile)
7. [Common Table Expressions (CTEs)](#common-table-expressions-ctes)
   - [Defining CTEs](#defining-ctes)
   - [Using CTEs](#using-ctes)
8. [Grouping and Aggregating](#grouping-and-aggregating)
   - [GROUP BY](#group-by)
   - [HAVING](#having)
   - [Aggregate Functions](#aggregate-functions)
9. [Sorting and Limiting](#sorting-and-limiting)
   - [ORDER BY](#order-by)
   - [LIMIT](#limit)
10. [Case Studies and Applications](#case-studies-and-applications)
11. [Further Reading](#further-reading)

## **Introduction**

SQL (Structured Query Language) is a standard programming language designed for managing relational databases. In this module, we will explore advanced SQL queries for retrieving data from databases. These queries will help you extract complex data from multiple tables, perform operations on grouped data, and manipulate data using window functions and CTEs.

## **Historical Context**

SQL was first developed in the 1970s by a team at IBM led by Donald Chamberlin and Raymond Boyce. The first version of SQL, known as SQL/DS, was released in 1974. Over time, SQL evolved and was refined through various versions, including SQL/2 and SQL/88. The modern version of SQL, known as SQL:1999, was released in 1999. Since then, SQL has continued to evolve, with new features and standards being added regularly.

## **Modern Developments**

In recent years, there has been a significant increase in the use of big data and NoSQL databases. However, relational databases like MySQL, PostgreSQL, and SQL Server continue to be widely used and supported. Modern developments include:

- **SQL:2016**: This version of SQL introduced several new features, including window functions, CTEs, and a new syntax for subqueries.
- **JSON and XML Support**: Many modern databases now support JSON and XML data types, allowing you to store and query data in these formats.
- **Cloud-Based Databases**: Cloud-based databases like Google Cloud SQL, Amazon RDS, and Azure SQL Database provide scalable and secure database solutions.

## **Joining Tables**

Joining tables is a fundamental concept in SQL, allowing you to combine data from multiple tables. There are several types of joins, including:

### Inner Join

An inner join returns only the rows that have a match in both tables.

```sql
SELECT *
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id;
```

### Left Outer Join

A left outer join returns all the rows from the left table and the matching rows from the right table. If there is no match, the result will contain NULL values for the right table columns.

```sql
SELECT *
FROM orders
LEFT OUTER JOIN customers
ON orders.customer_id = customers.customer_id;
```

### Right Outer Join

A right outer join is similar to a left outer join, but it returns all the rows from the right table and the matching rows from the left table.

```sql
SELECT *
FROM orders
RIGHT OUTER JOIN customers
ON orders.customer_id = customers.customer_id;
```

### Full Outer Join

A full outer join returns all the rows from both tables, including rows that do not have a match.

```sql
SELECT *
FROM orders
FULL OUTER JOIN customers
ON orders.customer_id = customers.customer_id;
```

## **Subqueries**

Subqueries are queries nested inside another query. There are two types of subqueries:

### Single-Row Subquery

A single-row subquery returns only one row.

```sql
SELECT *
FROM orders
WHERE customer_id = (SELECT customer_id FROM customers WHERE country='USA');
```

### Multi-Row Subquery

A multi-row subquery returns multiple rows.

```sql
SELECT *
FROM orders
WHERE total_amount > (SELECT AVG(total_amount) FROM orders);
```

## **Window Functions**

Window functions are used to perform calculations across a set of rows that are related to the current row. There are several types of window functions, including:

### ROW_NUMBER()

The ROW_NUMBER() function assigns a unique number to each row within a result set.

```sql
SELECT *
FROM (
  SELECT *, ROW_NUMBER() OVER (ORDER BY total_amount DESC) AS row_num
  FROM orders
) AS subquery;
```

### RANK()

The RANK() function assigns a rank to each row within a result set, based on a specific column.

```sql
SELECT *
FROM (
  SELECT *, RANK() OVER (ORDER BY total_amount DESC) AS rank
  FROM orders
) AS subquery;
```

### DENSE_RANK()

The DENSE_RANK() function assigns a rank to each row within a result set, based on a specific column, without gaps.

```sql
SELECT *
FROM (
  SELECT *, DENSE_RANK() OVER (ORDER BY total_amount DESC) AS rank
  FROM orders
) AS subquery;
```

### NTILE()

The NTILE() function divides a result set into a specified number of groups.

```sql
SELECT *
FROM (
  SELECT *, NTILE(4) OVER (ORDER BY total_amount DESC) AS quartile
  FROM orders
) AS subquery;
```

## **Common Table Expressions (CTEs)**

CTEs are temporary result sets that are defined within a query. They can be used to simplify complex queries and improve performance.

### Defining CTEs

CTEs are defined using the WITH keyword.

```sql
WITH sales AS (
  SELECT *
  FROM orders
  WHERE total_amount > 1000
)
SELECT *
FROM sales;
```

### Using CTEs

CTEs can be used to reference the result set of another query.

```sql
WITH sales AS (
  SELECT *
  FROM orders
  WHERE total_amount > 1000
)
SELECT *
FROM sales
WHERE region = 'North America';
```

## **Grouping and Aggregating**

Grouping and aggregating data is used to summarize and analyze data.

### GROUP BY

The GROUP BY clause groups rows based on one or more columns.

```sql
SELECT country, AVG(total_amount) AS average_order_value
FROM orders
GROUP BY country;
```

### HAVING

The HAVING clause filters groups based on aggregate values.

```sql
SELECT country, AVG(total_amount) AS average_order_value
FROM orders
GROUP BY country
HAVING AVG(total_amount) > 1000;
```

### Aggregate Functions

Aggregate functions are used to perform calculations on groups of rows.

```sql
SELECT country, SUM(total_amount) AS total_revenue
FROM orders
GROUP BY country;
```

## **Sorting and Limiting**

Sorting and limiting data is used to present data in a specific order and to limit the amount of data returned.

### ORDER BY

The ORDER BY clause sorts rows based on one or more columns.

```sql
SELECT *
FROM orders
ORDER BY total_amount DESC;
```

### LIMIT

The LIMIT clause limits the number of rows returned.

```sql
SELECT *
FROM orders
LIMIT 10;
```

## **Case Studies and Applications**

Here are a few examples of how SQL queries can be used in real-world scenarios:

- **E-commerce Website**: A company's e-commerce website uses SQL to manage customer information, track orders, and analyze sales data.
- **Social Media Platform**: A social media platform uses SQL to store and query user data, track engagement metrics, and analyze user behavior.
- **Financial Institution**: A financial institution uses SQL to manage customer accounts, track transactions, and analyze financial data.

## **Further Reading**

- **SQL Tutorial**: W3Schools SQL Tutorial
- **SQL Reference**: Oracle SQL Reference
- **SQL Syntax**: Microsoft SQL Server SQL Syntax

Note: This is a comprehensive guide to SQL advanced queries. However, it is not an exhaustive guide. There are many more advanced topics in SQL that are not covered here.
