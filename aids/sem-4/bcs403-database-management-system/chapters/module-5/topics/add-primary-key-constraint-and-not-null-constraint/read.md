# **Add Primary Key Constraint and Not Null Constraint to the Employee Table**

## **Introduction**

In this module, we will learn how to add primary key constraint and not null constraint to the employee table. A primary key constraint is a constraint that uniquely identifies each record in a table, while a not null constraint specifies that a field cannot contain null values.

## **Primary Key Constraint**

A primary key constraint is a unique identifier for each record in a table. It ensures that each record in the table has a unique combination of values in its primary key fields.

**Definition:** A primary key is a column or set of columns in a database table that uniquely identifies each row in the table.

**Explanation:** When you create a primary key constraint, the database engine ensures that:

- Each record in the table has a unique combination of values in its primary key fields.
- No two records in the table can have the same primary key values.

**Example:**

Suppose we have an `Employee` table with the following columns:

| Column Name     | Data Type      |
| --------------- | -------------- |
| EmployeeID (PK) | int            |
| FirstName       | varchar(50)    |
| LastName        | varchar(50)    |
| Salary          | decimal(10, 2) |

We can add a primary key constraint to the `EmployeeID` column to ensure that each employee has a unique ID.

```sql
CREATE TABLE Employee (
  EmployeeID int PRIMARY KEY,
  FirstName varchar(50),
  LastName varchar(50),
  Salary decimal(10, 2)
);
```

## **Not Null Constraint**

A not null constraint specifies that a field cannot contain null values. This ensures that all records in the table have values in the specified fields.

**Definition:** A not null constraint is a constraint that specifies that a field cannot contain null values.

**Explanation:** When you create a not null constraint, the database engine ensures that:

- No record in the table can have null values in the specified fields.
- All records in the table must have values in the specified fields.

**Example:**

Suppose we have an `Employee` table with the following columns:

| Column Name     | Data Type      | Not Null |
| --------------- | -------------- | -------- |
| EmployeeID (PK) | int            |          |
| FirstName       | varchar(50)    |          |
| LastName        | varchar(50)    |          |
| Salary          | decimal(10, 2) |          |

We can add a not null constraint to the `FirstName` and `LastName` columns to ensure that all employees have a first name and a last name.

```sql
CREATE TABLE Employee (
  EmployeeID int PRIMARY KEY,
  FirstName varchar(50) NOT NULL,
  LastName varchar(50) NOT NULL,
  Salary decimal(10, 2)
);
```

**Best Practices:**

- Use primary key constraints to uniquely identify each record in a table.
- Use not null constraints to ensure that all records in the table have values in specified fields.
- Use both primary key and not null constraints together to ensure that each record in the table has a unique combination of values and no null values.

## **Conclusion:**

In this module, we learned how to add primary key constraint and not null constraint to the employee table. We understand the definitions, explanations, and examples of these constraints, and we know how to use them to ensure data integrity in a database.
