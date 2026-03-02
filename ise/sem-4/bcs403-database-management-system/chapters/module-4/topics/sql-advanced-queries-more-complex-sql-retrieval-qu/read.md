# **SQL: Advanced Queries: More Complex SQL Retrieval Queries**

## **Module: DATABASE MANAGEMENT SYSTEM**

## **Topic: SQL: Advanced Queries: More Complex SQL Retrieval Queries**

### Introduction

In this module, we will explore advanced SQL retrieval queries that can be used to extract complex data from a database. These queries are used to retrieve data that involves multiple joins, subqueries, and other advanced techniques.

### Subqueries

A subquery is a query nested inside another query. It is used to retrieve data from a table based on the results of another query.

**Types of Subqueries:**

- **Single-Row Subquery:** Returns a single row of data.
- **Multi-Row Subquery:** Returns multiple rows of data.

**Example:**

```sql
SELECT *
FROM customers
WHERE country IN (SELECT country FROM orders);
```

In this example, the subquery `(SELECT country FROM orders)` returns a list of countries. The main query then selects all columns from the `customers` table where the country is in the list returned by the subquery.

### Joining Tables

Joining tables allows us to combine data from multiple tables based on a common column.

**Types of Joins:**

- **Inner Join:** Returns only the rows that have matching values in both tables.
- **Left Join:** Returns all the rows from the left table and the matching rows from the right table. If there is no match, the result is NULL on the right side.
- **Right Join:** Similar to left join, but returns all the rows from the right table and the matching rows from the left table.
- **Full Outer Join:** Returns all the rows from both tables, with NULL values where there is no match.

**Example:**

```sql
SELECT *
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id;
```

In this example, the inner join combines the `customers` table with the `orders` table based on the `customer_id` column.

### Correlated Subqueries

A correlated subquery is a subquery that is referenced within the outer query. It is used to retrieve data that depends on the values of the outer query.

**Example:**

```sql
SELECT *
FROM customers
WHERE country IN (SELECT country FROM orders WHERE order_total > 100);
```

In this example, the correlated subquery `(SELECT country FROM orders WHERE order_total > 100)` returns a list of countries where the total order value is greater than 100. The main query then selects all columns from the `customers` table where the country is in the list returned by the subquery.

### Window Functions

Window functions are used to perform calculations across rows in a result set.

**Example:**

```sql
SELECT *, ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employees;
```

In this example, the window function `ROW_NUMBER()` assigns a unique number to each row in the result set based on the `salary` column in descending order.

### Common Table Expressions (CTEs)

CTEs are temporary result sets that can be referenced within a query.

**Example:**

```sql
WITH sales AS (
  SELECT product_name, SUM(quantity) AS total_quantity
  FROM orders
  GROUP BY product_name
)
SELECT *
FROM sales;
```

In this example, the CTE `sales` calculates the total quantity of each product. The main query then selects all columns from the `sales` CTE.

### Aggregate Functions

Aggregate functions are used to perform calculations on groups of rows.

**Example:**

```sql
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;
```

In this example, the aggregate function `AVG()` calculates the average salary for each department.

### Grouping and Sorting

Grouping and sorting are used to organize data into groups and sort the data within each group.

**Example:**

```sql
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
ORDER BY average_salary DESC;
```

In this example, the grouping and sorting functions are used to organize the data by department and sort the data in descending order by average salary.

### Indexing and Optimization

Indexing and optimization are used to improve the performance of queries.

**Example:**

```sql
CREATE INDEX idx_country ON orders (country);
```

In this example, an index is created on the `country` column in the `orders` table to improve query performance.

### Best Practices

- Use indexes to improve query performance.
- Avoid using correlated subqueries when possible.
- Use CTEs to simplify complex queries.
- Use aggregate functions to perform calculations on groups of rows.
- Use grouping and sorting to organize data into groups and sort the data within each group.

By mastering these advanced SQL retrieval queries, you can extract complex data from your database and perform calculations on groups of rows. Remember to use indexing and optimization techniques to improve query performance.
