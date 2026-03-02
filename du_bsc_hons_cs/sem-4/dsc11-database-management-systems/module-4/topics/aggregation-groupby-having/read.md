# Aggregation, GROUP BY, and HAVING in SQL

## Introduction

In the realm of database management systems, the ability to transform raw data into meaningful insights is fundamental to decision-making. SQL (Structured Query Language) provides powerful mechanisms for data summarization through **aggregate functions**, the **GROUP BY** clause, and the **HAVING** clause. These constructs allow database users to perform calculations across multiple rows, group data based on specific criteria, and filter grouped results—capabilities that form the backbone of business intelligence and analytical reporting.

Consider a university database containing student records, course enrollments, and examination scores. A dean might ask: "What is the average marks scored by students in each department?" or "Which departments have more than 50 students with first-class distinction?" Answering such questions requires aggregating data, grouping it by relevant categories, and applying filters on the aggregated results. This is precisely where GROUP BY and HAVING become indispensable.

In the DU BSc (Hons) Computer Science curriculum, this topic carries significant weight in end-semester examinations. Understanding the nuanced differences between WHERE and HAVING, mastering the execution order of SQL clauses, and learning to write efficient aggregation queries are essential skills for scoring well in both internal assessments and the final examination.

## Key Concepts

### Aggregate Functions

SQL aggregate functions perform calculations on a set of rows and return a single result. The five fundamental aggregate functions are:

**COUNT()**: Returns the number of rows matching specified criteria. `COUNT(*)` counts all rows including duplicates and NULLs, while `COUNT(column_name)` counts non-NULL values in that specific column.

**SUM()**: Calculates the total of numeric values in a column. It automatically excludes NULL values during calculation.

**AVG()**: Computes the arithmetic mean of numeric values, again ignoring NULL entries.

**MIN()** and **MAX()**: Return the smallest and largest values respectively. These functions work with numeric, string, and date data types.

```sql
-- Example aggregate functions
SELECT 
    COUNT(*) AS total_students,
    SUM(marks) AS total_marks,
    AVG(marks) AS average_marks,
    MIN(marks) AS lowest_score,
    MAX(marks) AS highest_score
FROM Student;
```

### The GROUP BY Clause

The GROUP BY clause divides rows into groups based on one or more columns. When used with aggregate functions, it performs calculations *per group* rather than across the entire table. Each group produces one row in the result set.

**Syntax:**
```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1;
```

**Key Rules:**
- Every column in the SELECT list must either be an aggregate function or appear in the GROUP BY clause
- The database groups rows with identical values in the grouped columns
- NULL values are treated as a single group

```sql
-- Find average marks by department
SELECT department, AVG(marks) AS avg_marks
FROM Student
GROUP BY department;
```

### The HAVING Clause

The HAVING clause filters groups after the GROUP BY operation. It is analogous to WHERE, but WHERE filters individual rows before grouping, while HAVING filters aggregated groups.

**Syntax:**
```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1
HAVING aggregate_function(column2) condition;
```

**Critical Distinction:**
- WHERE: Evaluated before grouping (filters raw rows)
- HAVING: Evaluated after grouping (filters grouped results)

```sql
-- Departments with average marks > 75
SELECT department, AVG(marks) AS avg_marks
FROM Student
GROUP BY department
HAVING AVG(marks) > 75;
```

### Combined Execution Order

Understanding the logical execution order is crucial for writing correct queries:

1. **FROM**: Identify source tables
2. **WHERE**: Filter individual rows
3. **GROUP BY**: Create groups
4. **HAVING**: Filter groups
5. **SELECT**: Project final columns
6. **ORDER BY**: Sort results

## Examples

### Example 1: Department-wise Statistics

**Problem:** Given a Student table (RollNo, Name, Department, Marks), find the total students, average marks, and maximum marks for each department, but only for departments with at least 10 students.

**Solution:**
```sql
SELECT 
    Department,
    COUNT(*) AS TotalStudents,
    ROUND(AVG(Marks), 2) AS AverageMarks,
    MAX(Marks) AS HighestMarks
FROM Student
GROUP BY Department
HAVING COUNT(*) >= 10
ORDER BY AverageMarks DESC;
```

**Step-by-step execution:**
1. FROM retrieves all rows from Student table
2. No WHERE clause, so all rows are processed
3. GROUP BY creates groups based on Department
4. HAVING filters out departments with fewer than 10 students
5. SELECT calculates aggregate functions for remaining groups
6. ORDER BY sorts by average marks in descending order

### Example 2: Complex Filtering with Multiple Conditions

**Problem:** Find courses that have more than 5 enrolled students AND where the average fee collected is greater than Rs. 50,000.

**Given tables:**
- Enrollments (StudentID, CourseID, Fee)
- Courses (CourseID, CourseName)

**Solution:**
```sql
SELECT 
    c.CourseID,
    c.CourseName,
    COUNT(e.StudentID) AS EnrollmentCount,
    SUM(e.Fee) AS TotalFee
FROM Courses c
JOIN Enrollments e ON c.CourseID = e.CourseID
GROUP BY c.CourseID, c.CourseName
HAVING COUNT(e.StudentID) > 5 
   AND SUM(e.Fee) > 50000;
```

### Example 3: Finding Top-Performing Categories

**Problem:** Identify the top 2 product categories by total sales amount, where total sales exceed Rs. 1 lakh.

**Solution:**
```sql
SELECT 
    Category,
    SUM(SalesAmount) AS TotalSales
FROM Products
GROUP BY Category
HAVING SUM(SalesAmount) > 100000
ORDER BY TotalSales DESC
LIMIT 2;
```

**Common Pitfall:** Using LIMIT without ORDER BY produces undefined results. Always include ORDER BY when seeking "top N" results.

## Exam Tips

1. **Memorize the SQL clause order**: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY. This sequence is frequently tested in DU examinations.

2. **Never use HAVING without GROUP BY**: While some databases might allow this syntactically, it doesn't serve the intended purpose of filtering groups.

3. **WHERE vs HAVING distinction**: This is a classic exam question. Remember: WHERE filters before aggregation, HAVING filters after aggregation.

4. **Include all non-aggregated columns in GROUP BY**: Violating this rule produces non-deterministic results in strict SQL modes.

5. **Use meaningful aliases**: `SELECT department AS "Department Name"` improves readability and is often expected in answer scripts.

6. **Practice NULL handling**: Remember that aggregate functions (except COUNT(*)) ignore NULL values. This affects results significantly.

7. **Combine with JOINs**: Many exam questions require joining tables before applying aggregation. Practice queries that involve multiple tables with GROUP BY.

8. **Use ROUND() for decimal display**: When calculating averages, use ROUND(AVG(column), 2) to avoid lengthy decimal outputs.

9. **ORDER BY placement**: Remember ORDER BY always comes after GROUP BY and HAVING, never before.

10. **Multiple grouping columns**: Understand how multiple columns in GROUP BY create subgroups. For example, `GROUP BY Department, Year` creates groups for each Department-Year combination.