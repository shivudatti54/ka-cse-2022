# **Views in SQL**

## **Introduction**

A view in SQL is a virtual table based on the result of a SQL query. It provides a way to simplify complex queries and expose only the required data to the user. Views are useful for providing a layer of abstraction between the physical database tables and the external user, thus improving data security and reducing the complexity of the database.

## **Definition and Characteristics**

- A view is a virtual table that is based on the result of a SQL query.
- It is a user-defined object that is created based on the existing database tables.
- A view can be updated, inserted into, or deleted, but it does not store any actual data.
- A view can be used to simplify complex queries, provide a layer of abstraction between the physical database tables, and improve data security.

## **Types of Views**

### 1. Simple View

A simple view is a view that is based on a single table. It can have multiple tables joined together, but it can only contain a single table.

### 2. Complex View

A complex view is a view that is based on multiple tables. It can contain multiple tables joined together, subqueries, and other complex queries.

### 3. Derived View

A derived view is a view that is based on the result of a query that is derived from another query.

### 4. Materialized View

A materialized view is a physical table that is based on the result of a query. It stores the actual data in a physical table and can be updated periodically.

## **Creating a View**

To create a view in SQL, you need to use the `CREATE VIEW` statement followed by the name of the view, the `AS` keyword, and the query that defines the view.

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name;
```

## **Using a View**

To use a view in SQL, you need to use the `SELECT` statement followed by the name of the view.

```sql
SELECT * FROM view_name;
```

## **Example**

Suppose we have a database called `employees` with a table called `departments` that contains the following information:

| department_id | department_name |
| ------------- | --------------- |
| 1             | Sales           |
| 2             | Marketing       |
| 3             | IT              |

We can create a view called `sales_representatives` that contains the department name and the names of the sales representatives in each department.

```sql
CREATE VIEW sales_representatives AS
SELECT d.department_name, e.employee_name
FROM departments d
JOIN employees e ON d.department_id = e.department_id
WHERE e.employee_type = 'Sales Representative';
```

We can then use the `sales_representatives` view to retrieve the department name and the names of the sales representatives in each department.

```sql
SELECT * FROM sales_representatives;
```

This will return the following result:

| department_name | employee_name |
| --------------- | ------------- |
| Sales           | John Smith    |
| Sales           | Jane Doe      |
| Marketing       | Bob Johnson   |
| IT              | Alice Brown   |

## **Key Concepts**

- **Virtual table**: A view is a virtual table that is based on the result of a SQL query.
- **User-defined object**: A view is a user-defined object that is created based on the existing database tables.
- **Simplifies complex queries**: Views can simplify complex queries and expose only the required data to the user.
- **Improves data security**: Views can improve data security by providing a layer of abstraction between the physical database tables and the external user.
- **Materialized view**: A materialized view is a physical table that is based on the result of a query. It stores the actual data in a physical table and can be updated periodically.
