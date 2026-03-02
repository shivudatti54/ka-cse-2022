# More Complex SQL Retrieval Queries

## Table of Contents

- [More Complex SQL Retrieval Queries](#more-complex-sql-retrieval-queries)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Subqueries (Nested Queries)](#1-subqueries-nested-queries)
  - [2. Set Operations](#2-set-operations)
  - [3. Aggregate Functions and Grouping](#3-aggregate-functions-and-grouping)
  - [4. Various JOIN Types](#4-various-join-types)
  - [5. EXISTS and NOT EXISTS](#5-exists-and-not-exists)
  - [6. ALL and ANY (SOME) Operators](#6-all-and-any-some-operators)
- [Examples](#examples)
  - [Example 1: Subquery in WHERE Clause](#example-1-subquery-in-where-clause)
  - [Example 2: Correlated Subquery with EXISTS](#example-2-correlated-subquery-with-exists)
  - [Example 3: Set Operations](#example-3-set-operations)
  - [Example 4: Complex JOIN with GROUP BY](#example-4-complex-join-with-group-by)
  - [Example 5: Using ALL Operator](#example-5-using-all-operator)
- [Exam Tips](#exam-tips)

## Introduction

SQL (Structured Query Language) is the standard language for managing and manipulating relational databases. While basic SQL queries allow us to retrieve simple data using SELECT statements with simple WHERE conditions, real-world database applications often require more sophisticated data retrieval techniques. Complex SQL retrieval queries enable us to perform multi-level data analysis, combine results from multiple tables in various ways, and extract meaningful insights from large datasets.

In this module, we will explore advanced SQL retrieval techniques that are essential for database developers and administrators. These include subqueries, set operations, aggregate functions with grouping, various types of joins, and advanced filtering conditions. Mastering these concepts is crucial for the university examination as well as for practical database management tasks. Complex queries form the backbone of reporting, data analysis, and business intelligence applications.

## Key Concepts

### 1. Subqueries (Nested Queries)

A subquery is a query nested inside another query, typically within the WHERE, FROM, or SELECT clause. The inner query (subquery) executes first and returns values that are used by the outer query. Subqueries can be of two types: non-correlated subqueries (independent of the outer query) and correlated subqueries (reference columns from the outer query).

Scalar subqueries return a single value and can be used anywhere a single value is expected. Table subqueries return a set of rows and are used in the FROM clause to create temporary result sets.

### 2. Set Operations

SQL provides three main set operations for combining results from multiple queries: UNION, INTERSECT, and EXCEPT (MINUS). UNION combines all distinct rows from both queries. INTERSECT returns only rows that appear in both query results. EXCEPT returns rows from the first query that are not in the second query. All set operations require that the queries have the same number of columns with compatible data types.

### 3. Aggregate Functions and Grouping

Aggregate functions perform calculations on sets of rows and return single values. Common aggregate functions include COUNT, SUM, AVG, MAX, and MIN. The GROUP BY clause divides rows into groups based on specified columns. The HAVING clause filters groups based on conditions, similar to WHERE but operates on grouped data.

### 4. Various JOIN Types

Joins combine data from multiple tables based on related columns. INNER JOIN returns only matching rows from both tables. LEFT JOIN (or LEFT OUTER JOIN) returns all rows from the left table and matching rows from the right table. RIGHT JOIN returns all rows from the right table. FULL JOIN (or FULL OUTER JOIN) returns all rows when there is a match in either table. CROSS JOIN produces the Cartesian product of two tables.

### 5. EXISTS and NOT EXISTS

The EXISTS operator tests whether a subquery returns any rows. It is commonly used with correlated subqueries to check for the existence of related records. NOT EXISTS performs the opposite function, checking that no rows satisfy the condition.

### 6. ALL and ANY (SOME) Operators

These operators are used with comparison operators (=, <, >, <=, >=, <>) and subqueries. ALL returns TRUE if the comparison is true for all values returned by the subquery. ANY (or SOME) returns TRUE if the comparison is true for at least one value in the subquery result.

## Examples

### Example 1: Subquery in WHERE Clause

**Problem:** Find all employees whose salary is greater than the average salary of all employees.

```sql
SELECT employee_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

**Step-by-step solution:**

1. First, the inner query calculates the average salary: SELECT AVG(salary) FROM employees
2. This returns a single value (e.g., 50000)
3. The outer query then finds all employees with salary > 50000
4. Result shows employees earning above average

### Example 2: Correlated Subquery with EXISTS

**Problem:** Find all departments that have at least one employee with salary > 50000.

```sql
SELECT d.department_name
FROM departments d
WHERE EXISTS (
 SELECT 1
 FROM employees e
 WHERE e.department_id = d.department_id
 AND e.salary > 50000
);
```

**Step-by-step solution:**

1. The outer query selects each department
2. For each department, the correlated subquery checks if any employee in that department earns more than 50000
3. EXISTS returns TRUE if the subquery finds at least one matching row
4. Only departments with high earners are displayed

### Example 3: Set Operations

**Problem:** Find all customer IDs who placed orders or have accounts, without duplicates.

```sql
SELECT customer_id FROM orders
UNION
SELECT customer_id FROM accounts;
```

**Step-by-step solution:**

1. First query gets all customer IDs from orders table
2. Second query gets all customer IDs from accounts table
3. UNION combines both lists and removes duplicates
4. Result contains unique customer IDs from both sources

### Example 4: Complex JOIN with GROUP BY

**Problem:** Find the total sales amount for each product category, showing only categories with total sales > 100000.

```sql
SELECT p.category_name, SUM(s.quantity * s.unit_price) AS total_sales
FROM products p
INNER JOIN sales s ON p.product_id = s.product_id
GROUP BY p.category_name
HAVING SUM(s.quantity * s.unit_price) > 100000
ORDER BY total_sales DESC;
```

**Step-by-step solution:**

1. INNER JOIN combines products and sales tables on product_id
2. GROUP BY groups results by category_name
3. SUM calculates total sales for each category
4. HAVING filters to only categories exceeding 100000 in sales
5. ORDER BY sorts results in descending order

### Example 5: Using ALL Operator

**Problem:** Find employees whose salary is greater than all salaries in the Marketing department.

```sql
SELECT employee_name, salary
FROM employees
WHERE salary > ALL (
 SELECT salary
 FROM employees
 WHERE department = 'Marketing'
);
```

**Step-by-step solution:**

1. Subquery retrieves all salaries from Marketing department
2. ALL operator ensures salary must exceed every value in that list
3. This is equivalent to salary > MAX(Marketing salaries)
4. Result shows employees earning more than the highest-paid Marketing staff

## Exam Tips

1. **Remember the execution order:** FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
2. **Difference between WHERE and HAVING:** WHERE filters rows before grouping, HAVING filters groups after aggregation
3. **Set operations remove duplicates by default:** Use UNION ALL to include duplicates
4. **Correlated vs Non-correlated:** Correlated subqueries reference outer query; non-correlated don't
5. **EXISTS efficiency:** EXISTS stops searching as soon as first match is found, making it efficient
6. **NULL handling:** Be careful with NULL values in comparisons - use IS NULL or IS NOT NULL
7. **JOIN vs Subquery:** Many JOIN operations can be written as subqueries and vice versa
8. **Column aliasing:** Always use aliases (AS) for calculated columns to make output readable
9. **Practice conversion:** Be able to convert between different query types solving the same problem
10. **Know SQL syntax:** Understand the correct placement of commas, parentheses, and keywords
