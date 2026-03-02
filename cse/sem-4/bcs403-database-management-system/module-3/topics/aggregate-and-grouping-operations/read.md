# Aggregate and Grouping Operations in SQL

## Table of Contents

- [Aggregate and Grouping Operations in SQL](#aggregate-and-grouping-operations-in-sql)
- [Introduction](#introduction)
- [Aggregate Functions](#aggregate-functions)
  - [1. COUNT](#1-count)
  - [2. SUM](#2-sum)
  - [3. AVG](#3-avg)
  - [4. MAX](#4-max)
  - [5. MIN](#5-min)
- [GROUP BY Clause](#group-by-clause)
  - [Syntax](#syntax)
  - [Examples](#examples)
  - [Important Rules](#important-rules)
- [HAVING Clause](#having-clause)
  - [Syntax](#syntax)
  - [Examples](#examples)
  - [WHERE vs HAVING](#where-vs-having)
- [Important Points](#important-points)

## Introduction

Aggregate functions in SQL perform calculations on a set of values and return a single result. These functions are essential for data analysis as they help summarize large datasets. In DBMS, aggregate operations allow us to compute totals, averages, counts, and find maximum/minimum values from tables. These operations are widely used in reporting and decision-making queries.

## Aggregate Functions

SQL provides five basic aggregate functions:

### 1. COUNT

Returns the number of rows matching a condition.

```sql
SELECT COUNT(*) FROM Students;
SELECT COUNT(DISTINCT City) FROM Customers;
```

### 2. SUM

Returns the total sum of a numeric column.

```sql
SELECT SUM(Salary) FROM Employees;
SELECT SUM(Marks) FROM Results WHERE Grade = 'A';
```

### 3. AVG

Returns the average value of a numeric column.

```sql
SELECT AVG(Price) FROM Products;
SELECT AVG(Age) FROM Students WHERE Branch = 'CSE';
```

### 4. MAX

Returns the maximum value from a column.

```sql
SELECT MAX(Salary) FROM Employees;
SELECT MAX(Marks) FROM ExamResults;
```

### 5. MIN

Returns the minimum value from a column.

```sql
SELECT MIN(Age) FROM Students;
SELECT MIN(Price) FROM Products WHERE Category = 'Electronics';
```

## GROUP BY Clause

The GROUP BY clause groups rows with the same values into summary rows. It is used with aggregate functions to perform calculations for each group.

### Syntax

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1;
```

### Examples

```sql
-- Count employees in each department
SELECT Dept_ID, COUNT(*) FROM Employees GROUP BY Dept_ID;

-- Find average salary per department
SELECT Department, AVG(Salary) FROM Staff GROUP BY Department;

-- Total sales by product category
SELECT Category, SUM(Amount) FROM Sales GROUP BY Category;
```

### Important Rules

- All non-aggregated columns in SELECT must be included in GROUP BY
- GROUP BY comes after WHERE but before ORDER BY
- NULL values are grouped together

## HAVING Clause

The HAVING clause filters groups after GROUP BY aggregation. It is similar to WHERE but works on grouped data.

### Syntax

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1
HAVING condition;
```

### Examples

```sql
-- Departments with more than 5 employees
SELECT Dept_ID, COUNT(*) FROM Employees
GROUP BY Dept_ID
HAVING COUNT(*) > 5;

-- Categories with average price > 1000
SELECT Category, AVG(Price) FROM Products
GROUP BY Category
HAVING AVG(Price) > 1000;
```

### WHERE vs HAVING

| WHERE                          | HAVING                        |
| ------------------------------ | ----------------------------- |
| Filters rows before grouping   | Filters groups after grouping |
| Cannot use aggregate functions | Can use aggregate functions   |
| Used with individual records   | Used with grouped data        |

## Important Points

1. Aggregate functions ignore NULL values except COUNT(\*)
2. Always use GROUP BY when selecting both aggregate and non-aggregate columns
3. HAVING filters groups; WHERE filters rows before grouping
4. DISTINCT can be used with aggregate functions: COUNT(DISTINCT column)
5. Multiple aggregate functions can be used in a single query
6. NULL values in GROUP BY are treated as a separate group
7. Always verify column names in GROUP BY match SELECT non-aggregated columns
