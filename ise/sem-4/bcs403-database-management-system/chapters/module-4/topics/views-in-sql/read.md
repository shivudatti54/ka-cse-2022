# **Views in SQL**

## **Introduction**

In database management systems, a view is a virtual table that is based on the result of a SQL query. It provides a way to simplify complex queries and provide an interface to the data in a database. Views can be used to hide the implementation details of a database, provide a layer of abstraction, and improve data security.

## **Definition**

A view in SQL is a virtual table that is based on the result of a SQL query. It is a stored query that can be used to retrieve data from one or more tables.

## **Types of Views**

### 1. Simple View

A simple view is a view that is based on a single table. It is a straightforward way to retrieve data from a table.

### 2. Complex View

A complex view is a view that is based on multiple tables. It is used to combine data from multiple tables and perform complex operations.

### 3. Derived View

A derived view is a view that is based on the result of another view. It is used to create a new view that is based on the result of another view.

## **Creating a View**

A view can be created using the `CREATE VIEW` statement. The syntax for creating a view is as follows:

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name;
```

## **Dropping a View**

A view can be dropped using the `DROP VIEW` statement. The syntax for dropping a view is as follows:

```sql
DROP VIEW view_name;
```

## **Using Views**

Views can be used in various ways, including:

- **Querying Data**: Views can be used to query data from one or more tables.
- **Restricting Access**: Views can be used to restrict access to sensitive data by hiding the underlying tables.
- **Improving Performance**: Views can be used to improve performance by reducing the amount of data that needs to be retrieved.

## **Example**

Suppose we have two tables, `employees` and `departments`, and we want to create a view that shows the name and department of each employee.

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    department VARCHAR(255)
);

CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO employees (id, name, department)
VALUES (1, 'John Doe', 'Sales');

INSERT INTO employees (id, name, department)
VALUES (2, 'Jane Doe', 'Marketing');

INSERT INTO departments (id, name)
VALUES (1, 'Sales');
VALUES (2, 'Marketing');

CREATE VIEW employee_departments AS
SELECT e.name, d.name AS department
FROM employees e
JOIN departments d ON e.department = d.name;

SELECT * FROM employee_departments;
```

This will create a view called `employee_departments` that shows the name and department of each employee. The `SELECT` statement in the `CREATE VIEW` statement joins the `employees` table with the `departments` table on the `department` column, and the `SELECT` statement in the `SELECT` statement retrieves the name and department of each employee.

## **Key Concepts**

- **Virtual Table**: A view is a virtual table that is based on the result of a SQL query.
- **Stored Query**: A view is a stored query that can be used to retrieve data from one or more tables.
- **Abstracts Data**: Views can be used to abstract data, providing a layer of abstraction between the data and the user.
- **Improves Performance**: Views can be used to improve performance by reducing the amount of data that needs to be retrieved.
