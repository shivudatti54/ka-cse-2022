# Database Management Systems (DBMS)

## Unit 3: DML Operations - SELECT, INSERT, UPDATE, DELETE

---

## 1. Introduction to Data Manipulation Language (DML)

Data Manipulation Language (DML) is a subset of SQL (Structured Query Language) that enables users to retrieve, insert, update, and delete data within a database. As a BSc (Hons) Computer Science student at Delhi University under NEP 2024 UGCF curriculum, understanding DML operations is fundamental to working with relational database management systems (RDBMS).

### Why DML Matters in Real-World Applications

In today's data-driven world, virtually every application interacts with databases. Consider these practical scenarios:

- **E-commerce platforms** use DML to manage product inventories (INSERT new products, UPDATE stock levels, DELETE discontinued items)
- **Banking systems** process transactions using UPDATE to modify account balances
- **Social media applications** rely on SELECT queries to display user feeds
- **Hospital management systems** maintain patient records through INSERT, UPDATE, and DELETE operations

According to the Delhi University syllabus for DBMS (Paper Code: DSC-3), students must demonstrate proficiency in writing DML queries to manage data effectively in relational databases.

---

## 2. The SELECT Statement

The SELECT statement is the most frequently used DML command. It retrieves data from one or more tables and returns the result as a result set.

### 2.1 Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name;
```

### 2.2 Selecting All Columns

To retrieve all columns from a table, use the asterisk (*) wildcard:

```sql
SELECT * 
FROM Students;
```

### 2.3 The WHERE Clause

The WHERE clause filters records based on specified conditions. It supports various operators:

| Operator | Description |
|----------|-------------|
| = | Equal |
| <> | Not equal |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal |
| <= | Less than or equal |
| BETWEEN | Between a range |
| LIKE | Pattern matching |
| IN | Multiple values |

#### Example 1: Filtering with WHERE Clause

```sql
-- Find all students from Delhi
SELECT student_name, roll_number, city 
FROM Students 
WHERE city = 'Delhi';

-- Find students with marks greater than 75
SELECT student_name, marks 
FROM Students 
WHERE marks > 75;

-- Find students whose name starts with 'A'
SELECT student_name, course 
FROM Students 
WHERE student_name LIKE 'A%';
```

### 2.4 ORDER BY Clause

The ORDER BY clause sorts the result set in ascending (ASC) or descending (DESC) order:

```sql
-- Sort students by marks in descending order
SELECT student_name, marks 
FROM Students 
ORDER BY marks DESC;
```

### 2.5 Aggregate Functions

SQL provides built-in aggregate functions for calculations:

```sql
-- Count total students
SELECT COUNT(*) AS total_students 
FROM Students;

-- Calculate average marks
SELECT AVG(marks) AS average_marks 
FROM Students;

-- Find maximum and minimum marks
SELECT MAX(marks) AS highest_marks, MIN(marks) AS lowest_marks 
FROM Students;
```

### 2.6 GROUP BY and HAVING

The GROUP BY clause groups rows with same values, while HAVING filters groups:

```sql
-- Count students in each department
SELECT department, COUNT(*) AS student_count 
FROM Students 
GROUP BY department;

-- Departments with more than 10 students
SELECT department, COUNT(*) AS student_count 
FROM Students 
GROUP BY department 
HAVING COUNT(*) > 10;
```

---

## 3. The INSERT Statement

The INSERT statement adds new rows of data into a table. It is essential for populating databases with initial data and adding new records.

### 3.1 Basic Syntax

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

### 3.2 Inserting Single Row

#### Example 2: Adding a Student Record

```sql
-- Insert a new student into the Students table
INSERT INTO Students (student_id, student_name, roll_number, course, marks, city)
VALUES (101, 'Amit Kumar', 'CS/2024/001', 'BSc CS', 85, 'Delhi');
```

### 3.3 Inserting Multiple Rows

```sql
-- Insert multiple students at once
INSERT INTO Students (student_id, student_name, roll_number, course, marks, city)
VALUES 
    (102, 'Priya Sharma', 'CS/2024/002', 'BSc CS', 92, 'Mumbai'),
    (103, 'Rahul Verma', 'CS/2024/003', 'BSc CS', 78, 'Delhi'),
    (104, 'Sneha Gupta', 'CS/2024/004', 'BSc CS', 88, 'Noida');
```

### 3.4 Inserting into Specific Columns

You can insert data into only selected columns:

```sql
-- Insert partial data (other columns will be NULL or default)
INSERT INTO Students (student_id, student_name, roll_number)
VALUES (105, 'Ankit Patel', 'CS/2024/005');
```

### 3.5 Inserting Data from Another Table

```sql
-- Copy data from one table to another
INSERT INTO Passed_Students (student_id, student_name, marks)
SELECT student_id, student_name, marks 
FROM Students 
WHERE marks >= 60;
```

---

## 4. The UPDATE Statement

The UPDATE statement modifies existing data in a table. It is crucial for maintaining data accuracy and reflecting changes in real-world scenarios.

### 4.1 Basic Syntax

```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

**Important:** Always include a WHERE clause to avoid updating all rows unintentionally.

### 4.2 Updating Single Column

#### Example 3: Updating Student Marks

```sql
-- Update marks for a specific student
UPDATE Students
SET marks = 90
WHERE student_id = 101;
```

### 4.3 Updating Multiple Columns

```sql
-- Update multiple columns for a student
UPDATE Students
SET marks = 87, city = 'Gurgaon'
WHERE roll_number = 'CS/2024/002';
```

### 4.4 Update with Calculations

```sql
-- Increase marks by 5 for all students
UPDATE Students
SET marks = marks + 5;

-- Set marks to 0 for students who were absent (NULL marks)
UPDATE Students
SET marks = 0
WHERE marks IS NULL;
```

### 4.5 Update Using Subqueries

```sql
-- Update marks based on a subquery
UPDATE Students
SET marks = (SELECT AVG(marks) FROM Students)
WHERE student_id = 105;
```

### 4.6 Practical Example: Academic Record Management

```sql
-- Update course for all students from Delhi
UPDATE Students
SET course = 'BSc CS (Honors)'
WHERE city = 'Delhi';

-- Update student name (typo correction)
UPDATE Students
SET student_name = 'Rahul Kumar Verma'
WHERE student_id = 103;
```

---

## 5. The DELETE Statement

The DELETE statement removes one or more rows from a table. Care must be taken when using DELETE, as it permanently removes data.

### 5.1 Basic Syntax

```sql
DELETE FROM table_name
WHERE condition;
```

### 5.2 Deleting Specific Rows

```sql
-- Delete a specific student
DELETE FROM Students
WHERE student_id = 105;
```

### 5.3 Deleting Multiple Rows

```sql
-- Delete all students who failed (marks < 40)
DELETE FROM Students
WHERE marks < 40;

-- Delete students from a specific city
DELETE FROM Students
WHERE city = 'Mumbai';
```

### 5.4 Deleting All Rows

```sql
-- Delete all rows from a table (table structure remains)
DELETE FROM Students;
-- OR
TRUNCATE TABLE Students;
```

**Key Difference:** DELETE is a DML operation (can be rolled back in some databases), while TRUNCATE is a DDL operation (cannot be rolled back and resets auto-increment counters).

### 5.5 Delete Using Subqueries

```sql
-- Delete students whose marks are below average
DELETE FROM Students
WHERE marks < (SELECT AVG(marks) FROM (SELECT marks FROM Students) AS avg_table);
```

---

## 6. Comparison of DML Operations

| Operation | Purpose | Can Undo? | Effect on Data |
|-----------|---------|-----------|----------------|
| SELECT | Retrieve data | Yes (no change) | Read-only |
| INSERT | Add new rows | Yes (with transaction) | Increases row count |
| UPDATE | Modify existing data | Yes (with transaction) | Changes column values |
| DELETE | Remove rows | Yes (with transaction) | Decreases row count |

---

## 7. Assessment Questions

### Multiple Choice Questions (MCQs)

**Q1. Which SQL statement is used to extract data from a database?**
- a) GET
- b) EXTRACT
- c) SELECT
- d) PICK
- **Answer: c) SELECT**

**Q2. What is the correct syntax to insert data into a table?**
- a) INSERT INTO table_name VALUES (value1, value2)
- b) ADD INTO table_name VALUES (value1, value2)
- c) INSERT VALUES (value1, value2) INTO table_name
- d) SET INTO table_name VALUES (value1, value2)
- **Answer: a) INSERT INTO table_name VALUES (value1, value2)**

**Q3. Which clause is used to filter records in a SELECT statement?**
- a) FILTER
- b) WHERE
- c) GROUP BY
- d) ORDER BY
- **Answer: b) WHERE**

**Q4. What will happen if you execute: UPDATE Students SET marks = 100; without a WHERE clause?**
- a) No changes will occur
- b) Only one row will be updated
- c) All rows will have marks = 100
- d) An error will occur
- **Answer: c) All rows will have marks = 100**

**Q5. Which SQL command is used to delete all rows from a table?**
- a) REMOVE
- b) DELETE
- c) DROP
- d) CLEAR
- **Answer: b) DELETE**

**Q6. What is the difference between DELETE and TRUNCATE?**
- a) DELETE can be rolled back, TRUNCATE cannot
- b) They are identical operations
- c) DELETE is faster than TRUNCATE
- d) TRUNCATE requires WHERE clause
- **Answer: a) DELETE can be rolled back, TRUNCATE cannot**

**Q7. Which function is used to count total rows in a table?**
- a) SUM()
- b) TOTAL()
- c) COUNT()
- d) NUMBER()
- **Answer: c) COUNT()**

**Q8. The SELECT statement with ORDER BY DESC will sort results in:**
- a) Ascending order
- b) Descending order
- c) Random order
- d) No sorting
- **Answer: b) Descending order**

### Fill in the Blanks

**Q9.** The ______ clause is used to sort the results of a SELECT query.  
**Answer:** ORDER BY

**Q10.** To add new records to a table, we use the ______ statement.  
**Answer:** INSERT

**Q11.** The ______ statement is used to modify existing data in a table.  
**Answer:** UPDATE

**Q12.** To remove specific rows from a table, we use the ______ statement with a WHERE clause.  
**Answer:** DELETE

### True or False

**Q13.** The WHERE clause is mandatory in UPDATE statements.  
**Answer:** False (though highly recommended)

**Q14.** SELECT statement modifies the data in the database.  
**Answer:** False (SELECT only retrieves data)

**Q15.** LIKE 'A%' pattern matches strings starting with 'A'.  
**Answer:** True

### Flashcards for Quick Review

| Term | Definition |
|------|------------|
| **SELECT** | DML command to retrieve data from one or more tables |
| **INSERT** | DML command to add new rows into a table |
| **UPDATE** | DML command to modify existing data in a table |
| **DELETE** | DML command to remove rows from a table |
| **WHERE clause** | Filters records based on specified conditions |
| **ORDER BY** | Sorts query results (ASC/DESC) |
| **GROUP BY** | Groups rows with identical values |
| **HAVING** | Filters groups after GROUP BY operation |
| **Aggregate Functions** | Functions that perform calculations (COUNT, SUM, AVG, MAX, MIN) |
| **LIKE operator** | Pattern matching in WHERE clause |

---

## 8. Key Takeaways

1. **DML (Data Manipulation Language)** forms the core of database interactions, enabling users to manage data effectively in relational database systems.

2. **SELECT** is the most versatile DML command used for data retrieval with powerful features like:
   - Filtering with WHERE clause
   - Sorting with ORDER BY
   - Grouping with GROUP BY
   - Aggregate functions for calculations

3. **INSERT** adds new data to tables:
   - Can insert single or multiple rows
   - Can insert into all or specific columns
   - Can insert data from another table using SELECT

4. **UPDATE** modifies existing data:
   - Always use WHERE clause to target specific rows
   - Can update multiple columns in a single statement
   - Supports mathematical operations in SET clause

5. **DELETE** removes data:
   - Can be rolled back if within a transaction
   - Use TRUNCATE for faster deletion of all rows (cannot be rolled back)
   - Always verify conditions in WHERE clause before execution

6. **Data integrity is crucial** - always backup data before performing UPDATE or DELETE operations in production databases.

7. **Practice with real-world scenarios** - understanding DML operations through practical examples like student record management, inventory systems, and transaction processing will strengthen your database management skills for both academic and professional applications.

---

*Prepared for BSc (Hons) Computer Science - Delhi University, NEP 2024 UGCF Curriculum*