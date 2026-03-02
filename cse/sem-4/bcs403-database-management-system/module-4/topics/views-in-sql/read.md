# Views in SQL

## Table of Contents

- [Views in SQL](#views-in-sql)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition and Nature of Views](#definition-and-nature-of-views)
  - [Types of Views](#types-of-views)
  - [Creating and Managing Views](#creating-and-managing-views)
  - [View Updates and Limitations](#view-updates-and-limitations)
- [Examples](#examples)
  - [Example 1: Creating a Simple View](#example-1-creating-a-simple-view)
  - [Example 2: View with WITH CHECK OPTION](#example-2-view-with-with-check-option)
  - [Example 3: Complex View with Aggregate Function](#example-3-complex-view-with-aggregate-function)
  - [Example 4: Joining Tables in a View](#example-4-joining-tables-in-a-view)
- [Exam Tips](#exam-tips)

## Introduction

A view in SQL is a virtual table based on the result of a SELECT query. Unlike physical tables that store data persistently, views do not store data themselves but provide a window into one or more underlying tables. When you query a view, the database engine executes the underlying SELECT statement and returns the result as if it were a regular table. Views are a powerful feature of relational database management systems that enhance data security, simplify complex queries, and provide logical data independence.

In the context of database management systems, views play a crucial role in abstracting the underlying schema from users. They allow database administrators to present only relevant data to specific users while hiding sensitive information. This makes views essential for implementing security mechanisms in multi-user database environments. Additionally, views help in maintaining backward compatibility when the base table structure changes, as applications can continue to query views without modifications.

## Key Concepts

### Definition and Nature of Views

A view is a stored SELECT query that defines a virtual table. The definition of a view is stored in the database system catalog, and when a user queries a view, the database engine substitutes the view name with the underlying query definition. This process is called view resolution. Views can be based on one or more tables, and they can include columns derived from expressions, aggregate functions, or joins.

The syntax for creating a view in SQL is straightforward. The basic CREATE VIEW statement includes the view name, column names (optional), and the SELECT query that defines the view. For example, to create a view showing employee names and salaries from an employees table, you would use: CREATE VIEW emp_salary_view AS SELECT emp_name, salary FROM employees;

### Types of Views

**Simple Views**: A simple view is created from a single table and does not contain aggregate functions, GROUP BY clause, or join operations. Simple views are always updatable, meaning you can perform INSERT, UPDATE, and DELETE operations on them. These views derive their data directly from one base table, making the mapping between the view and the underlying table straightforward.

**Complex Views**: Complex views are created from multiple tables or include aggregate functions, GROUP BY clause, DISTINCT keyword, or set operations. These views are not always updatable, and certain restrictions apply to modifications. For instance, if a view contains a GROUP BY clause, you cannot perform UPDATE or DELETE operations on it. Complex views are primarily used for query simplification and reporting purposes.

**Materialized Views**: Unlike regular views that are virtual, materialized views store the actual result of the query physically on disk. These views are periodically refreshed to reflect changes in the underlying tables. Materialized views are particularly useful in data warehousing scenarios where complex aggregations need to be computed frequently without impacting the performance of the base tables.

### Creating and Managing Views

The CREATE VIEW statement is the primary DDL command for creating views. You can specify column aliases in the view definition to provide more meaningful names to the derived columns. The WITH CHECK OPTION is an important clause that ensures any modification through the view satisfies the view's defining condition. This prevents users from inserting or updating data that would not be visible through the view.

To modify an existing view, you can use the CREATE OR REPLACE VIEW statement, which updates the view definition without dropping it. This is particularly useful when you want to preserve permissions and dependencies associated with the view. The DROP VIEW statement removes the view definition from the database, but it does not affect the underlying base tables.

### View Updates and Limitations

The ability to update data through a view depends on the view's definition. An updatable view must meet several criteria: it must be based on a single table, it must not contain aggregate functions or window functions, it must not use DISTINCT, GROUP BY, HAVING, or UNION, and each column in the view must be directly mapped to a column in the base table without expressions or functions.

When updating through a view, the WITH CHECK OPTION adds an additional layer of validation. If this option is specified, any row that would not be visible in the view after the update is rejected. This ensures data integrity and maintains the view's filtering criteria.

## Examples

### Example 1: Creating a Simple View

Consider a database with an employees table with columns: emp_id, emp_name, department, salary, and hire_date. To create a view that shows only employees from the IT department:

```sql
CREATE VIEW it_employees AS
SELECT emp_id, emp_name, salary
FROM employees
WHERE department = 'IT';
```

To query this view:

```sql
SELECT * FROM it_employees;
```

This returns all IT employees with their IDs, names, and salaries.

### Example 2: View with WITH CHECK OPTION

```sql
CREATE VIEW it_salary_view AS
SELECT emp_id, emp_name, salary
FROM employees
WHERE department = 'IT'
WITH CHECK OPTION;
```

Now, if you try to update an employee's department to 'Sales' through this view:

```sql
UPDATE it_salary_view SET department = 'Sales' WHERE emp_id = 101;
```

This update will fail because it would violate the WITH CHECK OPTION constraint—the updated row would no longer appear in the view.

### Example 3: Complex View with Aggregate Function

```sql
CREATE VIEW dept_salary_summary AS
SELECT department,
 COUNT(*) AS total_employees,
 AVG(salary) AS avg_salary,
 MIN(salary) AS min_salary,
 MAX(salary) AS max_salary
FROM employees
GROUP BY department;
```

This view cannot be updated directly because it contains aggregate functions and GROUP BY clause. It serves as a read-only summary view for reporting purposes.

### Example 4: Joining Tables in a View

```sql
CREATE VIEW emp_dept_view AS
SELECT e.emp_id, e.emp_name, d.department_name, e.salary
FROM employees e
JOIN departments d ON e.department = d.dept_id;
```

This view combines data from two tables and presents a unified view of employees with their department names.

## Exam Tips

1. **Definition Matters**: Remember that a view is a virtual table—it does not store data physically but stores the SELECT query definition.

2. **Simple vs Complex Views**: Simple views are always updatable; complex views with aggregates, GROUP BY, or joins are typically read-only.

3. **WITH CHECK OPTION**: This constraint ensures that any data modification through the view satisfies the view's WHERE condition.

4. **Data Security**: Views provide column-level and row-level security by exposing only necessary data to specific users.

5. **View Resolution**: Understand that when querying a view, the database optimizer performs view substitution, replacing the view name with its defining query.

6. **Updatability Conditions**: For a view to be updatable, it must be based on a single table without aggregates, GROUP BY, or complex expressions.

7. **Materialized Views**: Remember these are different—they store physical data and can be refreshed periodically.

8. **DROP vs CREATE OR REPLACE**: Dropping a view removes it entirely, while CREATE OR REPLACE preserves dependencies and permissions.

9. **Practical Applications**: Views are used for simplifying complex queries, providing logical data independence, and implementing security policies.

10. **university Exam Focus**: Pay special attention to the syntax of CREATE VIEW, understanding updatability rules, and the purpose of WITH CHECK OPTION.
