# Retrieval Queries in SQL

## Table of Contents

- [Retrieval Queries in SQL](#retrieval-queries-in-sql)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Basic SELECT Statement](#1-basic-select-statement)
  - [2. Column Aliases](#2-column-aliases)
  - [3. DISTINCT Keyword](#3-distinct-keyword)
  - [4. WHERE Clause](#4-where-clause)
  - [5. Logical Operators](#5-logical-operators)
  - [6. LIKE Operator](#6-like-operator)
  - [7. IN Operator](#7-in-operator)
  - [8. BETWEEN Operator](#8-between-operator)
  - [9. NULL Values](#9-null-values)
  - [10. ORDER BY Clause](#10-order-by-clause)
  - [11. Aggregate Functions](#11-aggregate-functions)
  - [12. GROUP BY Clause](#12-group-by-clause)
  - [13. HAVING Clause](#13-having-clause)
  - [14. LIMIT / TOP Clause](#14-limit--top-clause)
  - [15. Pattern Matching with REGEXP (Advanced)](#15-pattern-matching-with-regexp-advanced)
- [Examples](#examples)
  - [Example 1: Basic Retrieval with Filtering](#example-1-basic-retrieval-with-filtering)
  - [Example 2: Grouping with Aggregate Functions](#example-2-grouping-with-aggregate-functions)
  - [Example 3: Complex Query with Multiple Conditions](#example-3-complex-query-with-multiple-conditions)
- [Exam Tips](#exam-tips)

## Introduction

Structured Query Language (SQL) is the standard language used for managing and manipulating relational databases. Among all SQL operations, retrieval queries—primarily implemented through the SELECT statement—are the most frequently used in real-world applications. Whether you are building a simple student record system or a complex enterprise application, the ability to fetch and transform data efficiently is fundamental to database-driven development.

In the context of the university's Database Management System syllabus (BCS403), Module-3 focuses on retrieval queries, which form the backbone of data access in any database application. This topic covers everything from basic data selection to complex aggregations and filtering. Understanding these concepts is essential not only for passing examinations but also for practical software development roles where SQL proficiency is mandatory.

Retrieval queries allow users to extract specific information from one or more tables, apply conditions, sort results, and perform calculations. Mastery of these techniques enables database users to transform raw data into meaningful information, supporting decision-making processes in organizations.

## Key Concepts

### 1. Basic SELECT Statement

The SELECT statement is the foundation of all SQL queries. It specifies which columns to retrieve from the database.

**Syntax:**

```sql
SELECT column1, column2, ...
FROM table_name;
```

To select all columns, use the asterisk (\*) wildcard:

```sql
SELECT * FROM table_name;
```

The SELECT statement can also be used without a WHERE clause to display all rows, making it useful for viewing complete table contents.

### 2. Column Aliases

Aliases provide temporary names to columns or tables, making output more readable.

**Syntax:**

```sql
SELECT column_name AS alias_name
FROM table_name;
```

Example:

```sql
SELECT student_name AS "Student Name",
 marks AS "Score"
FROM students;
```

### 3. DISTINCT Keyword

The DISTINCT keyword eliminates duplicate values from query results.

**Syntax:**

```sql
SELECT DISTINCT column_name
FROM table_name;
```

Example:

```sql
SELECT DISTINCT department
FROM employees;
```

This returns only unique department values, removing all duplicates.

### 4. WHERE Clause

The WHERE clause filters records based on specified conditions. It extracts only those records that satisfy the given criteria.

**Syntax:**

```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

**Comparison Operators:** =, <>, !=, <, >, <=, >=

**Example:**

```sql
SELECT * FROM employees
WHERE salary > 50000;
```

### 5. Logical Operators

SQL supports three logical operators: AND, OR, and NOT. These combine multiple conditions in WHERE clauses.

- **AND:** Returns records satisfying ALL conditions
- **OR:** Returns records satisfying ANY condition
- **NOT:** Negates a condition

**Example:**

```sql
SELECT * FROM employees
WHERE department = 'IT' AND salary > 60000;
```

### 6. LIKE Operator

The LIKE operator performs pattern matching on string columns. It supports two wildcards:

- **% (Percent):** Matches zero or more characters
- **\_ (Underscore):** Matches exactly one character

**Examples:**

```sql
-- Names starting with 'A'
SELECT * FROM students
WHERE student_name LIKE 'A%';

-- Names ending with 'n'
SELECT * FROM students
WHERE student_name LIKE '%n';

-- Second letter is 'a'
SELECT * FROM students
WHERE student_name LIKE '_a%';
```

### 7. IN Operator

The IN operator checks whether a value matches any value in a list of values.

**Syntax:**

```sql
SELECT * FROM table_name
WHERE column_name IN (value1, value2, ...);
```

**Example:**

```sql
SELECT * FROM employees
WHERE department IN ('IT', 'HR', 'Finance');
```

### 8. BETWEEN Operator

The BETWEEN operator selects values within a given range (inclusive).

**Syntax:**

```sql
SELECT * FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

**Example:**

```sql
SELECT * FROM products
WHERE price BETWEEN 100 AND 500;
```

### 9. NULL Values

NULL represents missing or unknown data. Special operators IS NULL and IS NOT NULL are used to check NULL values.

**Examples:**

```sql
-- Find records with NULL values
SELECT * FROM employees
WHERE phone_number IS NULL;

-- Find records without NULL values
SELECT * FROM employees
WHERE phone_number IS NOT NULL;
```

### 10. ORDER BY Clause

The ORDER BY clause sorts query results in ascending (ASC) or descending (DESC) order. Default is ascending.

**Syntax:**

```sql
SELECT column1, column2
FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC];
```

**Example:**

```sql
SELECT * FROM students
ORDER BY marks DESC, student_name ASC;
```

### 11. Aggregate Functions

Aggregate functions perform calculations on sets of rows and return a single result. SQL provides five major aggregate functions:

| Function | Description                |
| -------- | -------------------------- |
| COUNT()  | Returns the number of rows |
| SUM()    | Returns the sum of values  |
| AVG()    | Returns the average value  |
| MIN()    | Returns the minimum value  |
| MAX()    | Returns the maximum value  |

**Examples:**

```sql
SELECT COUNT(*) FROM employees;
SELECT SUM(salary) FROM employees;
SELECT AVG(marks) FROM students;
SELECT MIN(price) FROM products;
SELECT MAX(salary) FROM employees;
```

### 12. GROUP BY Clause

The GROUP BY clause groups rows with the same values into summary rows. It is typically used with aggregate functions.

**Syntax:**

```sql
SELECT column_name, aggregate_function(column_name)
FROM table_name
GROUP BY column_name;
```

**Example:**

```sql
SELECT department, COUNT(*) as emp_count
FROM employees
GROUP BY department;
```

### 13. HAVING Clause

The HAVING clause filters groups after GROUP BY aggregation. Unlike WHERE, HAVING works with aggregate functions.

**Syntax:**

```sql
SELECT column_name, aggregate_function(column_name)
FROM table_name
GROUP BY column_name
HAVING condition;
```

**Example:**

```sql
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

### 14. LIMIT / TOP Clause

These clauses restrict the number of rows returned:

- **MySQL/PostgreSQL:** LIMIT
- **SQL Server:** TOP
- **Oracle:** ROWNUM

**Examples:**

```sql
-- MySQL/PostgreSQL
SELECT * FROM employees LIMIT 10;

-- SQL Server
SELECT TOP 10 * FROM employees;
```

### 15. Pattern Matching with REGEXP (Advanced)

Modern SQL databases support regular expressions for complex pattern matching:

```sql
SELECT * FROM students
WHERE student_name REGEXP '^[A-Z].*[a-z]$';
```

## Examples

### Example 1: Basic Retrieval with Filtering

**Problem:** From the `products` table, retrieve product names and prices for all products priced above 1000, sorted by price in descending order.

**Table: products**
| product_id | product_name | price | category |
|------------|--------------|-------|----------|
| 1 | Laptop | 50000 | Electronics |
| 2 | Mouse | 500 | Electronics |
| 3 | Keyboard | 1500 | Electronics |
| 4 | Monitor | 12000 | Electronics |
| 5 | Pen Drive | 800 | Electronics |

**Solution:**

```sql
SELECT product_name, price
FROM products
WHERE price > 1000
ORDER BY price DESC;
```

**Output:**
| product_name | price |
|--------------|-------|
| Laptop | 50000 |
| Monitor | 12000 |
| Keyboard | 1500 |

**Explanation:** The WHERE clause filters products with price > 1000, and ORDER BY sorts them in descending order.

### Example 2: Grouping with Aggregate Functions

**Problem:** From the `orders` table, find the total sales amount for each customer and display only those customers whose total purchase exceeds 5000.

**Table: orders**
| order_id | customer_id | amount |
|----------|-------------|--------|
| 1 | C001 | 2000 |
| 2 | C001 | 4000 |
| 3 | C002 | 3000 |
| 4 | C003 | 6000 |
| 5 | C002 | 2500 |

**Solution:**

```sql
SELECT customer_id,
 SUM(amount) AS total_purchase
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 5000;
```

**Output:**
| customer_id | total_purchase |
|-------------|----------------|
| C001 | 6000 |
| C002 | 5500 |
| C003 | 6000 |

**Explanation:** GROUP BY groups orders by customer_id, SUM() calculates total purchase per customer, and HAVING filters groups with total > 5000.

### Example 3: Complex Query with Multiple Conditions

**Problem:** From the `employees` table, find employees who work in 'IT' or 'HR' departments, have salary between 30000 and 80000, and whose names start with 'S'. Sort results by salary descending.

**Table: employees**
| emp_id | emp_name | department | salary |
|--------|----------|------------|--------|
| 101 | Suresh | IT | 75000 |
| 102 | Ramesh | HR | 50000 |
| 103 | Sita | IT | 45000 |
| 104 | Sunita | HR | 35000 |
| 105 | Rajesh | Sales | 40000 |

**Solution:**

```sql
SELECT emp_name, department, salary
FROM employees
WHERE (department = 'IT' OR department = 'HR')
 AND salary BETWEEN 30000 AND 80000
 AND emp_name LIKE 'S%'
ORDER BY salary DESC;
```

**Output:**
| emp_name | department | salary |
|----------|------------|--------|
| Suresh | IT | 75000 |
| Sunita | HR | 35000 |

**Explanation:** Multiple conditions are combined using AND/OR. The LIKE 'S%' pattern matches names starting with 'S'. The BETWEEN operator is inclusive, matching salaries 30000 to 80000.

## Exam Tips

1. **Understand the Difference Between WHERE and HAVING:** WHERE filters rows before grouping, while HAVING filters groups after GROUP BY. This is a frequently asked exam question.

2. **Remember Aggregate Function Behavior:** COUNT(\*) counts all rows including NULLs, while COUNT(column) counts non-NULL values only.

3. **Operator Precedence:** In complex queries, AND has higher precedence than OR. Use parentheses to clarify logic.

4. **DISTINCT with Multiple Columns:** SELECT DISTINCT col1, col2 returns unique combinations of both columns, not unique values of col1 alone.

5. **NULL Handling:** Never use = NULL to check NULL values. Always use IS NULL or IS NOT NULL.

6. **Pattern Matching:** Remember that LIKE is case-insensitive in MySQL by default but case-sensitive in some databases. Use wildcards correctly: % matches any sequence, \_ matches single character.

7. **ORDER BY Default:** If ASC/DESC is not specified, ORDER BY defaults to ascending order.

8. **Group By Non-Aggregate Columns:** When using GROUP BY, any column in the SELECT list must either be an aggregate function or be included in the GROUP BY clause.

9. **LIMIT Syntax Varies:** Know the syntax for your specific database system (LIMIT for MySQL/PostgreSQL, TOP for SQL Server, ROWNUM for Oracle).

10. **Practice Writing Queries:** Regular practice with sample tables is essential. Understand how to build queries step-by-step.
