# SELECT Queries and Aggregations in SQL

## 1. Introduction to the SELECT Statement

The `SELECT` statement is the most fundamental and frequently used command in SQL (Structured Query Language). Its primary purpose is to retrieve data from one or more database tables. Think of it as a way to ask a question of your database. A `SELECT` query does not modify the underlying data; it only reads it.

The basic syntax is:
```sql
SELECT column1, column2, ...
FROM table_name;
```

**Example:** To retrieve all columns from a table named `Employees`, you would use:
```sql
SELECT * FROM Employees;
```
The asterisk (`*`) is a wildcard that means "all columns."

## 2. Anatomy of a Basic SELECT Query

A `SELECT` statement is composed of several clauses, each serving a specific purpose. While `SELECT` and `FROM` are the only mandatory clauses for a simple query, understanding the full structure is key.

```sql
SELECT [DISTINCT] column_list
FROM table_list
[WHERE search_condition]
[GROUP BY group_by_expression]
[HAVING search_condition]
[ORDER BY order_by_expression [ASC | DESC]];
```

*   **SELECT:** Specifies the columns to be retrieved.
*   **FROM:** Specifies the table(s) from which to retrieve the data.
*   **WHERE:** Filters rows based on a specified condition.
*   **GROUP BY:** Groups rows that have the same values into summary rows.
*   **HAVING:** Filters groups based on a condition (used after `GROUP BY`).
*   **ORDER BY:** Sorts the result set by one or more columns.

## 3. Filtering Data with the WHERE Clause

The `WHERE` clause is used to filter records and extract only those that fulfill a specified condition. It comes after the `FROM` clause.

**Operators in WHERE clause:**
*   `=`, `<>` or `!=` (not equal)
*   `>`, `<`, `>=`, `<=`
*   `BETWEEN` (within a range)
*   `LIKE` (search for a pattern, using `%` for multiple characters and `_` for a single character)
*   `IN` (specify multiple possible values)
*   `IS NULL` / `IS NOT NULL` (check for null values)
*   `AND`, `OR`, `NOT` (logical operators)

**Example:** Find all employees in the 'Sales' department with a salary greater than 50000.
```sql
SELECT FirstName, LastName, Department, Salary
FROM Employees
WHERE Department = 'Sales' AND Salary > 50000;
```

## 4. Sorting Results with ORDER BY

The `ORDER BY` clause is used to sort the result set in ascending (`ASC`) or descending (`DESC`) order. The default is ascending.

**Example:** List all employees sorted by their salary in descending order, and then by last name in ascending order for those with the same salary.
```sql
SELECT FirstName, LastName, Salary
FROM Employees
ORDER BY Salary DESC, LastName ASC;
```

## 5. Introduction to Aggregate Functions

Aggregate functions perform a calculation on a set of values and return a single summary value. They are essential for data analysis and reporting. They are typically used with the `GROUP BY` clause.

The five primary aggregate functions are:

| Function | Description                                          | Ignores NULL? |
| :------- | :--------------------------------------------------- | :------------ |
| `COUNT()` | Returns the number of items in a set.                | Yes           |
| `SUM()`   | Returns the sum of all values in a set.              | Yes           |
| `AVG()`   | Returns the average of the values in a set.         | Yes           |
| `MIN()`   | Returns the smallest value in a set.                | Yes           |
| `MAX()`   | Returns the largest value in a set.                 | Yes           |

**Examples:**
```sql
-- Count the total number of employees
SELECT COUNT(*) AS TotalEmployees FROM Employees;

-- Find the average, minimum, and maximum salary
SELECT AVG(Salary) AS AvgSalary,
       MIN(Salary) AS MinSalary,
       MAX(Salary) AS MaxSalary
FROM Employees;

-- Find the total salary expenditure for the company
SELECT SUM(Salary) AS TotalPayroll FROM Employees;
```

## 6. Grouping Data with GROUP BY

The `GROUP BY` clause groups rows that have the same values in specified columns into summary rows. It is almost always used with aggregate functions to generate reports per group.

**Key Concept:** Any column in the `SELECT` list that is not an aggregate function must appear in the `GROUP BY` clause.

**Example:** Find the total number of employees and the average salary in each department.
```sql
SELECT Department,
       COUNT(*) AS NumOfEmployees,
       AVG(Salary) AS AvgDeptSalary
FROM Employees
GROUP BY Department;
```

**Visualization of GROUP BY:**
Imagine the `Employees` table:

```
| ID | Name  | Department | Salary |
|----|-------|------------|--------|
| 1  | Alice | Sales      | 60000  |
| 2  | Bob   | IT         | 80000  |
| 3  | Carol | Sales      | 55000  |
| 4  | Dave  | IT         | 75000  |
```

The `GROUP BY Department` operation would create two groups:
*   **Group 1 (Sales):** Rows with ID 1 and 3
*   **Group 2 (IT):** Rows with ID 2 and 4

The aggregate functions (`COUNT`, `AVG`) are then applied to each group.

The result would be:
```
| Department | NumOfEmployees | AvgDeptSalary |
|------------|----------------|---------------|
| Sales      | 2              | 57500.0       |
| IT         | 2              | 77500.0       |
```

## 7. Filtering Groups with HAVING

The `WHERE` clause filters rows *before* they are grouped. The `HAVING` clause filters groups *after* the `GROUP BY` has been applied. It is used to apply conditions to aggregate values.

**Example:** Find departments that have more than 10 employees and an average salary greater than 70000.
```sql
SELECT Department,
       COUNT(*) AS NumOfEmployees,
       AVG(Salary) AS AvgDeptSalary
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 10 AND AVG(Salary) > 70000;
```

**Crucial Difference:**
*   `WHERE` is for individual rows. (`Salary > 50000`)
*   `HAVING` is for aggregate groups. (`AVG(Salary) > 70000`)

## 8. Combining Clauses: The Complete Query Flow

A `SELECT` statement is processed in the following logical order. Understanding this order is critical to writing correct queries, especially when using `WHERE`, `GROUP BY`, and `HAVING` together.

1.  **FROM:** Identifies the source tables.
2.  **WHERE:** Filters the rows from the source tables.
3.  **GROUP BY:** Groups the filtered rows.
4.  **HAVING:** Filters the created groups.
5.  **SELECT:** Defines the columns to be returned.
6.  **ORDER BY:** Sorts the final result set.

**Example:** Find the total sales per salesperson for the year 2023, but only for those salespeople whose total sales exceeded $100,000. Present the results sorted from highest to lowest sales.

```sql
SELECT SalespersonID,
       SUM(SaleAmount) AS TotalSales
FROM Sales
WHERE SaleDate BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY SalespersonID
HAVING SUM(SaleAmount) > 100000
ORDER BY TotalSales DESC;
```

**Flow Explanation:**
1.  `FROM Sales`: Get all records from the Sales table.
2.  `WHERE ...`: Keep only the sales records from the year 2023.
3.  `GROUP BY SalespersonID`: Group the remaining 2023 sales records by the salesperson.
4.  `HAVING SUM(...) > 100000`: From these groups, only keep those where the sum of sales is over $100k.
5.  `SELECT ...`: For the kept groups, show the salesperson's ID and their total sales.
6.  `ORDER BY ...`: Sort this final list by total sales in descending order.

## 9. Exam Tips and Common Pitfalls

1.  **`WHERE` vs. `HAVING`:**
    *   Use `WHERE` to filter rows based on column values. It cannot be used with aggregate functions.
    *   Use `HAVING` to filter groups based on the results of aggregate functions. It must follow a `GROUP BY` clause.

2.  **`GROUP BY` Rule:** Every non-aggregated column in your `SELECT` list must be in your `GROUP BY` clause. Forgetting this is a very common error.

3.  **Aliases in `ORDER BY`:**
    *   You can use column aliases (defined in the `SELECT` list with `AS`) in the `ORDER BY` clause because `ORDER BY` is processed after `SELECT`.
    *   You **cannot** use column aliases in the `WHERE` or `GROUP BY` or `HAVING` clauses because they are processed before the `SELECT` clause and the alias is not yet defined.

4.  **`COUNT(*)` vs. `COUNT(column_name)`:**
    *   `COUNT(*)` counts all rows in the group, including those with NULL values.
    *   `COUNT(column_name)` counts only the rows where `column_name` is not NULL.

5.  **Readability:** Format your SQL queries clearly. Using uppercase for keywords and indenting clauses makes your code much easier to read and debug, especially in an exam setting.