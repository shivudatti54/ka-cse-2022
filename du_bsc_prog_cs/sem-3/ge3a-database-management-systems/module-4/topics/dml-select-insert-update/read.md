# DML Operations: SELECT, INSERT, UPDATE

## Introduction

Data Manipulation Language (DML) forms the backbone of database interactions in any relational database management system. These operations enable users to retrieve, insert, modify, and delete data within database tables. For students studying Database Management Systems at the University of Delhi, mastering DML operations is essential, as these commands constitute approximately 60-70% of real-world SQL usage in applications ranging from e-commerce platforms to banking systems.

The three fundamental DML operations—SELECT, INSERT, and UPDATE—are critical for the DU Computer Science curriculum. The SELECT statement, being the most frequently used SQL command, allows data retrieval with powerful filtering, sorting, and aggregation capabilities. INSERT enables new record creation, while UPDATE modifies existing data. Understanding the nuances of these operations, including transaction control and constraint handling, is vital for both internal assessments and end-semester examinations.

This module covers the practical implementation of these DML commands with extensive examples using a student database scenario, which is highly relevant for examination preparation.

## Key Concepts

### 1. SELECT Statement

The SELECT statement is used to query and retrieve data from one or more database tables. Its basic syntax is:

```sql
SELECT column1, column2, ... 
FROM table_name;
```

To retrieve all columns, use the wildcard operator (*):

```sql
SELECT * FROM table_name;
```

**Key Clauses in SELECT:**

- **DISTINCT**: Eliminates duplicate rows from result sets
```sql
SELECT DISTINCT city FROM students;
```

- **WHERE Clause**: Filters rows based on conditions
```sql
SELECT * FROM students WHERE marks > 75;
```

- **ORDER BY**: Sorts results in ascending (ASC) or descending (DESC) order
```sql
SELECT * FROM students ORDER BY marks DESC;
```

- **GROUP BY**: Groups rows with same values for aggregate calculations
```sql
SELECT department, COUNT(*) FROM students GROUP BY department;
```

- **HAVING**: Filters groups after GROUP BY operation
```sql
SELECT department, AVG(marks) FROM students 
GROUP BY department 
HAVING AVG(marks) > 70;
```

**Operators in WHERE Clause:**
- Comparison: =, <>, <, >, <=, >=
- Logical: AND, OR, NOT
- Special: BETWEEN, IN, LIKE, IS NULL, IS NOT NULL

**Pattern Matching with LIKE:**
- `%` - Matches any sequence of characters
- `_` - Matches exactly one character
```sql
SELECT * FROM students WHERE name LIKE 'A%';  -- Names starting with A
SELECT * FROM students WHERE name LIKE '_a%'; -- Second letter is 'a'
```

### 2. INSERT Statement

The INSERT statement adds new rows to a table. There are two primary forms:

**Single Row Insert:**
```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

**Multiple Row Insert:**
```sql
INSERT INTO table_name (column1, column2)
VALUES 
    (value1a, value2a),
    (value1b, value2b),
    (value1c, value2c);
```

**INSERT with SELECT:**
```sql
INSERT INTO table_name (column1, column2)
SELECT column_a, column_b 
FROM another_table 
WHERE condition;
```

### 3. UPDATE Statement

The UPDATE statement modifies existing data in a table:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

**Critical Note:** The WHERE clause is crucial in UPDATE operations. Omitting it will update ALL rows in the table, which is a common and dangerous mistake.

**UPDATE with Subqueries:**
```sql
UPDATE students
SET marks = marks + 5
WHERE roll_no IN (
    SELECT roll_no FROM students 
    WHERE department = 'Computer Science'
);
```

### 4. Transaction Control

DML operations can be controlled using transaction commands:
- **COMMIT**: Saves all pending changes permanently
- **ROLLBACK**: Undoes all pending changes
- **SAVEPOINT**: Creates a point within a transaction to which you can roll back

## Examples

### Example 1: Complex SELECT Query

**Problem:** Given a table `STUDENTS(roll_no, name, department, marks, city)`, write a query to display names and marks of students from Computer Science department who scored above average marks, sorted by marks in descending order.

**Solution:**
```sql
SELECT name, marks 
FROM students 
WHERE department = 'Computer Science' 
  AND marks > (SELECT AVG(marks) FROM students)
ORDER BY marks DESC;
```

**Step-by-step execution:**
1. Inner query calculates average marks from the STUDENTS table
2. WHERE clause filters Computer Science students
3. Additional condition selects only those above average
4. ORDER BY arranges results in descending order of marks

### Example 2: INSERT with Data Validation

**Problem:** Insert a new student record with roll_no=101, name='Amit Kumar', department='Physics', marks=82, city='Delhi'. Also insert all students from 'Mathematics' department into a backup table.

**Solution:**
```sql
-- Insert single row
INSERT INTO students (roll_no, name, department, marks, city)
VALUES (101, 'Amit Kumar', 'Physics', 82, 'Delhi');

-- Insert from another table (assuming backup table exists)
INSERT INTO students_backup (roll_no, name, department, marks, city)
SELECT roll_no, name, department, marks, city
FROM students
WHERE department = 'Mathematics';
```

### Example 3: UPDATE with Conditional Logic

**Problem:** Increase marks by 10% for all students in 'Computer Science' department who scored below 60, but only for those residing in Delhi.

**Solution:**
```sql
UPDATE students
SET marks = marks * 1.10
WHERE department = 'Computer Science'
  AND marks < 60
  AND city = 'Delhi';
```

**Verification query:**
```sql
SELECT name, marks AS "Old Marks", 
       marks * 1.10 AS "New Marks"
FROM students
WHERE department = 'Computer Science'
  AND city = 'Delhi';
```

## Exam Tips

1. **WHERE Clause Priority**: Remember that AND has higher precedence than OR. Use parentheses to control evaluation order in complex conditions.

2. **NULL Handling**: Always use IS NULL or IS NOT NULL for NULL comparisons. Using = NULL will never work because NULL represents unknown value.

3. **DISTINCT Application**: DISTINCT applies to the entire result set, not individual columns. `SELECT DISTINCT city, department` treats the combination as unique.

4. **UPDATE Safety**: Always write the WHERE clause first, then build the SET clause. Test SELECT equivalent before executing UPDATE to prevent accidental mass updates.

5. **Aggregate Functions in WHERE**: You cannot use aggregate functions directly in WHERE clause. Use HAVING for filtering after GROUP BY, or use subqueries.

6. **String Literals**: String values in SQL must be enclosed in single quotes ('). Numeric values should not be quoted.

7. **Execution Order**: Remember the logical order: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY. This helps in understanding query behavior.

8. **Wildcard Escaping**: If you need to search for literal % or _ characters in LIKE, use ESCAPE clause: `WHERE name LIKE '%\_%' ESCAPE '\'`

9. **String Functions**: Know CONCAT, UPPER, LOWER, LENGTH, SUBSTR, TRIM for string manipulation in SELECT queries.

10. **Practice Previous Year Questions**: DU exams frequently ask to write SQL queries for given scenarios. Practice at least 50 queries before the examination.