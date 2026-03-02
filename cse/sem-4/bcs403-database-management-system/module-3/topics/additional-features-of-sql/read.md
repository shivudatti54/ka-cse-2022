# Additional Features of SQL

## Introduction

Structured Query Language (SQL) is the standard language for managing relational databases. While basic SQL operations like SELECT, INSERT, UPDATE, and DELETE form the foundation, advanced SQL features significantly enhance database functionality, security, and performance. This module explores the additional features of SQL that are essential for developing robust database applications in real-world scenarios.

These advanced features include views that provide logical data independence, sequences for generating unique identifiers, indexes for performance optimization, integrity constraints for maintaining data quality, and transaction control mechanisms for ensuring database consistency. Understanding these features is crucial for CSE students as they form the backbone of enterprise-level database management systems and are frequently tested in university examinations.

## Key Concepts

### 1. Views in SQL

A view is a virtual table based on the result of a SQL query. It does not store data physically but provides a way to present data from one or more tables in a customized format. Views offer several advantages including data security, logical data independence, and simplified complex queries.

**Creating a View:**

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

**Types of Views:**

- **Simple View:** Created from a single table and contains no aggregate functions or GROUP BY clause. Can be used for DML operations.
- **Complex View:** Created from multiple tables or contains aggregate functions, GROUP BY, or DISTINCT. Generally not updatable.

**Example - Creating a View for Employee Details:**

```sql
CREATE VIEW Emp_Details AS
SELECT emp_id, emp_name, dept_id, salary
FROM employees
WHERE dept_id = 10;

-- Querying the view
SELECT * FROM Emp_Details;
```

**Dropping a View:**

```sql
DROP VIEW view_name;
```

### 2. Sequences

A sequence is a database object that generates a sequence of unique numbers, typically used for auto-incrementing primary key values. Sequences are independent of tables and can be shared across multiple tables.

**Creating a Sequence:**

```sql
CREATE SEQUENCE sequence_name
START WITH value
INCREMENT BY value
MAXVALUE value
MINVALUE value
CYCLE/NOCYCLE;
```

**Using a Sequence:**

```sql
-- Get next value
SELECT sequence_name.NEXTVAL FROM dual;

-- Get current value
SELECT sequence_name.CURRVAL FROM dual;

-- Insert using sequence
INSERT INTO employees (emp_id, emp_name)
VALUES (seq_emp.NEXTVAL, 'John');
```

### 3. Indexes

Indexes are database objects that improve the speed of data retrieval operations on a table. They work similarly to book indexes, providing quick access to data without scanning the entire table.

**Creating an Index:**

```sql
-- Simple index
CREATE INDEX index_name ON table_name(column_name);

-- Unique index
CREATE UNIQUE INDEX index_name ON table_name(column_name);

-- Composite index
CREATE INDEX index_name ON table_name(column1, column2);
```

**Types of Indexes:**

- **B-Tree Index:** Default index type, suitable for high-cardinality columns
- **Bitmap Index:** Used for low-cardinality columns
- **Composite Index:** Index on multiple columns

**Dropping an Index:**

```sql
DROP INDEX index_name;
```

### 4. Integrity Constraints

Integrity constraints enforce rules on table data to maintain data accuracy and consistency.

**Types of Constraints:**

| Constraint  | Description                                               |
| ----------- | --------------------------------------------------------- |
| NOT NULL    | Ensures column cannot contain NULL values                 |
| UNIQUE      | Ensures all values in a column are different              |
| PRIMARY KEY | Uniquely identifies each row (combines NOT NULL + UNIQUE) |
| FOREIGN KEY | Maintains referential integrity between tables            |
| CHECK       | Ensures values satisfy a specific condition               |
| DEFAULT     | Provides default value when no value is specified         |

**Adding Constraints:**

```sql
-- Adding NOT NULL
ALTER TABLE employees MODIFY emp_name NOT NULL;

-- Adding CHECK constraint
ALTER TABLE employees ADD CONSTRAINT chk_salary
CHECK (salary > 0);

-- Adding FOREIGN KEY
ALTER TABLE employees
ADD CONSTRAINT fk_dept
FOREIGN KEY (dept_id) REFERENCES departments(dept_id);
```

### 5. Set Operations

Set operations combine results from multiple SELECT statements.

**UNION:** Returns all distinct rows from both queries

```sql
SELECT column FROM table1
UNION
SELECT column FROM table2;
```

**UNION ALL:** Returns all rows including duplicates

```sql
SELECT column FROM table1
UNION ALL
SELECT column FROM table2;
```

**INTERSECT:** Returns common rows from both queries

```sql
SELECT column FROM table1
INTERSECT
SELECT column FROM table2;
```

**EXCEPT (MINUS):** Returns rows from first query not in second

```sql
SELECT column FROM table1
EXCEPT
SELECT column FROM table2;
```

### 6. Aggregate Functions with GROUP BY and HAVING

Aggregate functions perform calculations on sets of rows and return a single result.

**Common Aggregate Functions:**

- COUNT(): Counts rows
- SUM(): Calculates total
- AVG(): Calculates average
- MIN(): Finds minimum value
- MAX(): Finds maximum value

**GROUP BY:** Groups rows with same values

```sql
SELECT dept_id, COUNT(*) as emp_count, AVG(salary) as avg_sal
FROM employees
GROUP BY dept_id;
```

**HAVING:** Filters groups (used with GROUP BY)

```sql
SELECT dept_id, AVG(salary) as avg_sal
FROM employees
GROUP BY dept_id
HAVING AVG(salary) > 50000;
```

### 7. Subqueries

A subquery is a query nested inside another query. They are used to retrieve data based on unknown values.

**Scalar Subquery:** Returns single value

```sql
SELECT emp_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

**Correlated Subquery:** References outer query

```sql
SELECT e.emp_name, e.salary
FROM employees e
WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id);
```

**IN and ANY/ALL with Subqueries:**

```sql
-- IN operator
SELECT * FROM employees WHERE dept_id IN (SELECT dept_id FROM departments WHERE location = 'Bangalore');

-- ANY operator
SELECT * FROM employees WHERE salary > ANY (SELECT salary FROM employees WHERE dept_id = 10);
```

### 8. Transaction Control Language (TCL)

Transactions ensure database consistency by grouping related operations.

**COMMIT:** Saves all changes made during the transaction

```sql
COMMIT;
```

**ROLLBACK:** Undoes all changes since last COMMIT

```sql
ROLLBACK;
```

**SAVEPOINT:** Creates a point within transaction to rollback to

```sql
SAVEPOINT sp1;
ROLLBACK TO sp1;
```

**Example Transaction:**

```sql
UPDATE accounts SET balance = balance - 5000 WHERE acc_id = 101;
UPDATE accounts SET balance = balance + 5000 WHERE acc_id = 102;
COMMIT;
```

## Examples

### Example 1: Creating and Using a View

**Problem:** Create a view to display employees earning above average salary.

**Solution:**

```sql
-- Step 1: Create the view
CREATE VIEW High_Salary_Emp AS
SELECT emp_id, emp_name, salary, dept_id
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Step 2: Query the view
SELECT * FROM High_Salary_emp WHERE dept_id = 20;
```

**Explanation:** The view automatically calculates the average salary each time it's queried, showing only employees earning above average.

### Example 2: Using Sequence and Table Insert

**Problem:** Create a sequence starting from 1 with increment 1, and insert 3 new departments.

**Solution:**

```sql
-- Create sequence
CREATE SEQUENCE dept_seq
START WITH 1
INCREMENT BY 1
MAXVALUE 100
NOCYCLE;

-- Insert departments using sequence
INSERT INTO departments VALUES (dept_seq.NEXTVAL, 'IT', 'Bangalore');
INSERT INTO departments VALUES (dept_seq.NEXTVAL, 'HR', 'Mysore');
INSERT INTO departments VALUES (dept_seq.NEXTVAL, 'Sales', 'Delhi');

-- Verify
SELECT * FROM departments;
```

**Result:** Department IDs will be 1, 2, and 3 automatically assigned.

### Example 3: Complex Query with Multiple Features

**Problem:** Find departments with total salary exceeding 100000, using aggregate functions, GROUP BY, and HAVING.

**Solution:**

```sql
SELECT d.dept_name, COUNT(e.emp_id) as emp_count,
 SUM(e.salary) as total_salary, AVG(e.salary) as avg_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING SUM(e.salary) > 100000
ORDER BY total_salary DESC;
```

**Explanation:** This query joins two tables, groups by department name, filters groups with total salary > 100000, and orders results in descending order.

## Exam Tips

1. **Views are Virtual:** Remember that views do not store data physically - they only store the query definition.

2. **Difference Between UNION and UNION ALL:** UNION removes duplicates while UNION ALL keeps all rows including duplicates.

3. **WHERE vs HAVING:** WHERE filters rows before grouping, HAVING filters groups after GROUP BY aggregation.

4. **Constraint Order:** When creating tables, PRIMARY KEY should be defined first as it may be referenced by FOREIGN KEY constraints.

5. **Sequence Usage:** Remember to use .NEXTVAL to get next value and .CURRVAL to get current value of sequence.

6. **Correlated Subqueries:** These reference the outer query and are executed repeatedly for each row processed.

7. **Transaction Properties:** Remember ACID properties - Atomicity, Consistency, Isolation, Durability.

8. **Index Optimization:** Indexes improve SELECT performance but slow down INSERT, UPDATE, and DELETE operations.

9. **View DML Restrictions:** Complex views with JOINs, GROUP BY, or aggregate functions cannot be updated through DML operations.

10. **Default Constraint:** DEFAULT constraint is used to insert default values when no value is provided during insertion.
