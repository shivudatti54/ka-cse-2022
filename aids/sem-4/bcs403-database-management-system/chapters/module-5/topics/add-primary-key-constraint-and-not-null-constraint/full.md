# Add Primary Key Constraint and Not Null Constraint to the Employee Table

## **Introduction**

In this section, we will delve into the world of database management systems and explore the importance of adding primary key constraints and not null constraints to the employee table. These constraints are fundamental building blocks of a database, ensuring data integrity and enforcing relationships between tables.

## **Historical Context**

The concept of primary keys dates back to the early days of relational databases. The first relational database management system (RDBMS), CODASYL, introduced the concept of primary keys in the 1960s. However, it was not until the development of relational RDBMS like IBM DB2 and Oracle that primary keys became a standard feature.

The not null constraint, on the other hand, was introduced later, in the 1980s, as a way to prevent null values from being stored in tables.

## **Why Are Primary Keys and Not Null Constraints Important?**

### Primary Keys

A primary key is a unique identifier for each row in a table. It ensures that each row is distinct and prevents duplicate records from being inserted.

- **Benefits:**
  - **Data integrity:** Primary keys ensure that each row is unique, preventing duplicate records from being inserted.
  - **Efficient queries:** Primary keys enable efficient querying, as the database can quickly identify the specific row(s) being queried.
  - **Data consistency:** Primary keys maintain data consistency by preventing null or duplicate values.

### Not Null Constraints

A not null constraint specifies that a column cannot contain null values. It ensures that all values in a column are valid and meaningful.

- **Benefits:**
  - **Data accuracy:** Not null constraints ensure that all values in a column are accurate and meaningful.
  - **Data integrity:** Not null constraints maintain data integrity by preventing null values from being stored in tables.
  - **Efficient data retrieval:** Not null constraints enable efficient data retrieval, as the database can quickly identify the specific values being queried.

## **Adding Primary Key Constraint and Not Null Constraint to the Employee Table**

Let's assume we have an employee table with the following structure:

| Column Name | Data Type      | Description                         |
| ----------- | -------------- | ----------------------------------- |
| employee_id | int            | Unique identifier for each employee |
| name        | varchar(255)   | Employee name                       |
| department  | varchar(255)   | Department the employee belongs to  |
| job_title   | varchar(255)   | Job title of the employee           |
| salary      | decimal(10, 2) | Salary of the employee              |

To add a primary key constraint and not null constraint to the employee table, we would follow these steps:

### Step 1: Create a Primary Key Constraint

We will create a primary key constraint on the `employee_id` column, which uniquely identifies each employee.

```sql
ALTER TABLE employee
ADD PRIMARY KEY (employee_id);
```

### Step 2: Create a Not Null Constraint

We will create a not null constraint on the `name` column, ensuring that all employee names are valid and meaningful.

```sql
ALTER TABLE employee
ADD CONSTRAINT not_null_name
NOT NULL CONSTRAINT name;

ALTER TABLE employee
ADD CONSTRAINT not_null_department
NOT NULL CONSTRAINT department;

ALTER TABLE employee
ADD CONSTRAINT not_null_job_title
NOT NULL CONSTRAINT job_title;

ALTER TABLE employee
ADD CONSTRAINT not_null_salary
NOT NULL CONSTRAINT salary;
```

Note that we have created separate not null constraints for each column, as each column has different requirements.

## **Case Study: Adding Primary Key Constraint and Not Null Constraint to the Employee Table**

Suppose we have a scenario where we want to add a primary key constraint and not null constraint to the employee table. We have the following data:

| employee_id | name       | department | job_title   | salary   |
| ----------- | ---------- | ---------- | ----------- | -------- |
| 1           | John Smith | Sales      | Manager     | 50000.00 |
| 2           | Jane Doe   | Marketing  | Coordinator | 40000.00 |
| null        | null       | IT         | Developer   | 60000.00 |

If we add a primary key constraint to the `employee_id` column, the data would be updated as follows:

| employee_id | name       | department | job_title   | salary                                             |
| ----------- | ---------- | ---------- | ----------- | -------------------------------------------------- |
| 1           | John Smith | Sales      | Manager     | 50000.00                                           |
| 2           | Jane Doe   | Marketing  | Coordinator | 40000.00                                           |
| 1           | John Smith | Sales      | Manager     | 50000.00 (Error: Primary key constraint violation) |

This is because we cannot insert a new row with an `employee_id` value that already exists in the table.

Similarly, if we add not null constraints to the `name`, `department`, `job_title`, and `salary` columns, the data would be updated as follows:

| employee_id | name       | department | job_title   | salary   |
| ----------- | ---------- | ---------- | ----------- | -------- |
| 1           | John Smith | Sales      | Manager     | 50000.00 |
| 2           | Jane Doe   | Marketing  | Coordinator | 40000.00 |

| Error: Not null constraint violation for employee_id column

This is because we cannot insert a new row with null values in the `name`, `department`, `job_title`, and `salary` columns.

## **Applications and Further Reading**

The primary key constraint and not null constraint are essential components of database management systems. They ensure data integrity, maintain data consistency, and enable efficient data retrieval.

Some applications of these constraints include:

- **Data warehousing:** Primary keys and not null constraints are crucial in data warehousing, as they enable efficient data retrieval and ensure data integrity.
- **Business intelligence:** Primary keys and not null constraints are necessary in business intelligence, as they enable efficient data analysis and ensure data accuracy.
- **Data mining:** Primary keys and not null constraints are essential in data mining, as they enable efficient data retrieval and ensure data quality.

For further reading, please refer to the following resources:

- **"Database Systems: The Complete Book" by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza**
- **"Database Design for Mere Mortals" by Michael J. Hernández**
- **"Database Systems: A Practical Approach" by Rakesh V. Rangarajan**

We hope this comprehensive guide has provided you with a deep understanding of the primary key constraint and not null constraint. Remember to always follow best practices when designing your database schema, and don't hesitate to reach out if you have any further questions or concerns.
