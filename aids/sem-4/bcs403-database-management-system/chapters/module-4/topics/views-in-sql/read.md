# **Study Material: Views in SQL**

**Module:** Database Management System
**Duration:** 8 Hours
**Topic:** Views in SQL

## **What is a View in SQL?**

A view in SQL is a virtual table that is based on the result of a query. It is a stored query that can be used to retrieve data from one or more tables. Views are used to provide a layer of abstraction between the physical database and the users who interact with it.

## **Characteristics of a View**

- A view is a virtual table, not a physical table.
- A view is based on the result of a query, not a physical table.
- A view can be used to provide a layer of abstraction between the physical database and the users who interact with it.
- A view can be used to simplify complex queries and improve data security.

## **Advantages of Using Views**

- **Improved Data Security**: Views can be used to hide sensitive data from users who do not need to see it.
- **Simplified Complex Queries**: Views can be used to simplify complex queries and improve data consistency.
- **Data Abstraction**: Views can be used to provide a layer of abstraction between the physical database and the users who interact with it.

## **Disadvantages of Using Views**

- **Performance Overhead**: Views can introduce performance overhead due to the additional processing required to create and maintain them.
- **Data Inconsistency**: Views can introduce data inconsistency if the underlying tables are modified.
- **Difficulty in Maintenance**: Views can be difficult to maintain if the underlying tables are modified.

## **Creating a View in SQL**

To create a view in SQL, the following syntax is used:

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name;
```

## **Example: Creating a View**

Suppose we have a table called `employees` with the following structure:

| Column Name | Data Type      |
| ----------- | -------------- |
| id          | int            |
| name        | varchar(50)    |
| department  | varchar(50)    |
| salary      | decimal(10, 2) |

To create a view called `employee_details` that includes the `name`, `department`, and `salary` columns, we can use the following query:

```sql
CREATE VIEW employee_details AS
SELECT name, department, salary
FROM employees;
```

## **Querying a View in SQL**

To query a view in SQL, we can use the following syntax:

```sql
SELECT * FROM view_name;
```

## **Example: Querying a View**

To query the `employee_details` view, we can use the following query:

```sql
SELECT * FROM employee_details;
```

This query will return the `name`, `department`, and `salary` columns for all employees.

## **Updating a View in SQL**

To update a view in SQL, we can use the following syntax:

```sql
UPDATE view_name
SET column1 = value1, column2 = value2
WHERE condition;
```

## **Example: Updating a View**

Suppose we want to update the `salary` column for all employees in the `employee_details` view. We can use the following query:

```sql
UPDATE employee_details
SET salary = salary * 1.1
WHERE department = 'Sales';
```

This query will increase the `salary` column for all employees in the `Sales` department by 10%.

## **Deleting a View in SQL**

To delete a view in SQL, we can use the following syntax:

```sql
DROP VIEW view_name;
```

## **Example: Deleting a View**

To delete the `employee_details` view, we can use the following query:

```sql
DROP VIEW employee_details;
```

This query will delete the `employee_details` view and any associated data.

## **Best Practices for Using Views**

- Use views to simplify complex queries and improve data security.
- Use views to provide a layer of abstraction between the physical database and the users who interact with it.
- Use views to hide sensitive data from users who do not need to see it.
- Use views to reduce data redundancy and improve data consistency.
- Use views to improve data security and reduce the risk of data breaches.
