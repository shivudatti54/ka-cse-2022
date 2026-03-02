# **SQL: Advanced Queries: More Complex SQL Retrieval Queries**

**Module:** DATABASE MANAGEMENT SYSTEM
**No. of Hours:** 8
**Topic:** SQL: Advanced Queries: More Complex SQL Retrieval Queries

## **Introduction**

In this module, we will cover advanced SQL queries for retrieving data from a database. These queries will help you extract complex data from your database and perform analysis. This module will cover subqueries, joins, grouping, and aggregations.

## **Subqueries**

A subquery is a query nested inside another query. It can be used to retrieve data from another table or to filter data.

**Types of Subqueries:**

- **Single-Row Subquery:** Returns a single row of data.
- **Multiple-Row Subquery:** Returns multiple rows of data.

**Example:**

Suppose we have a table called `employees` with columns `name`, `age`, and `salary`. We want to find the employee with the highest salary in a specific department.

```sql
SELECT *
FROM employees
WHERE department = 'Sales'
AND salary = (SELECT MAX(salary)
              FROM employees
              WHERE department = 'Sales');
```

## **Joins**

A join is used to combine rows from two or more tables based on a common column.

**Types of Joins:**

- **Inner Join:** Returns only the rows that have a match in both tables.
- **Left Join:** Returns all rows from the left table and the matching rows from the right table. If there is no match, the result is NULL.
- **Right Join:** Returns all rows from the right table and the matching rows from the left table. If there is no match, the result is NULL.
- **Full Outer Join:** Returns all rows from both tables. If there is no match, the result is NULL.

**Example:**

Suppose we have two tables: `orders` and `customers`. We want to find the customers who have placed an order.

```sql
SELECT c.*
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;
```

## **Grouping**

Grouping is used to group rows based on a common column.

**Types of Grouping:**

- **Aggregation Functions:** Used to perform calculations on groups of rows.
- **Grouping Sets:** Used to group rows based on multiple columns.

**Example:**

Suppose we have a table called `sales` with columns `product`, `region`, and `sales`. We want to find the total sales for each region.

```sql
SELECT region, SUM(sales) AS total_sales
FROM sales
GROUP BY region;
```

## **Aggregations**

Aggregations are used to perform calculations on groups of rows.

**Types of Aggregations:**

- **Sum:** Used to calculate the total of a group of rows.
- **Average:** Used to calculate the average of a group of rows.
- **Max:** Used to find the maximum value in a group of rows.
- **Min:** Used to find the minimum value in a group of rows.
- **Count:** Used to count the number of rows in a group.

**Example:**

Suppose we have a table called `employees` with columns `name`, `age`, and `salary`. We want to find the average salary for each department.

```sql
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;
```

## **Conclusion**

In this module, we covered advanced SQL queries for retrieving data from a database. We learned about subqueries, joins, grouping, and aggregations. These queries will help you extract complex data from your database and perform analysis. Practice these queries to improve your skills and become a proficient SQL programmer.
