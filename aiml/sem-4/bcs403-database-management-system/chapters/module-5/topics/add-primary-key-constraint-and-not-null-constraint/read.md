# **Add Primary Key Constraint and Not Null Constraint to the Employee Table**

## **Introduction**

In a database, a table is a collection of related data. To ensure data integrity and prevent duplicate records, we need to define constraints on a table. In this study material, we will focus on adding primary key constraint and not null constraint to the employee table.

## **Primary Key Constraint**

A primary key constraint is a unique identifier for each record in a table. It ensures that each record is distinct and cannot be duplicated.

**Definition:** A primary key is a column or a combination of columns that uniquely identifies each record in a table.

**Purpose:** To ensure data integrity and prevent duplicate records.

**Example:** Consider an employee table with columns for employee ID, name, address, and salary. We can define the employee ID as the primary key constraint.

| Employee ID (PK) | Name        | Address     | Salary |
| ---------------- | ----------- | ----------- | ------ |
| 1                | John Smith  | 123 Main St | 50000  |
| 2                | Jane Doe    | 456 Elm St  | 60000  |
| 3                | Bob Johnson | 789 Oak St  | 70000  |

In this example, the employee ID is the primary key constraint, and it ensures that each record is unique.

## **Not Null Constraint**

A not null constraint is a constraint that ensures a column cannot contain null values.

**Definition:** A not null constraint is a constraint that prevents a column from containing null values.

**Purpose:** To ensure data integrity and prevent missing data.

**Example:** Consider an employee table with columns for employee ID, name, address, and salary. We can define the salary as a not null constraint.

| Employee ID (PK) | Name        | Address     | Salary (NotNull) |
| ---------------- | ----------- | ----------- | ---------------- |
| 1                | John Smith  | 123 Main St | 50000            |
| 2                | Jane Doe    | 456 Elm St  | 60000            |
| 3                | Bob Johnson | 789 Oak St  | 70000            |

In this example, the salary is a not null constraint, and it ensures that each record has a valid salary value.

## **Adding Primary Key Constraint and Not Null Constraint to the Employee Table**

To add a primary key constraint and not null constraint to the employee table, we can use SQL commands.

```sql
CREATE TABLE employee (
  employee_id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  salary DECIMAL(10, 2) NOT NULL
);
```

In this example, we define the employee ID as the primary key constraint and the name, address, and salary as not null constraints.

## **Benefits of Adding Primary Key Constraint and Not Null Constraint**

- Ensures data integrity and prevents duplicate records.
- Ensures data integrity and prevents missing data.
- Reduces errors and inconsistencies in the data.
- Improves data security and access control.

## **Best Practices**

- Define primary key constraint and not null constraint for each column that requires uniqueness and non-null values.
- Use meaningful and consistent column names.
- Use comments to explain the purpose and requirements of the table and its columns.
- Test the table and its constraints to ensure data integrity and accuracy.

## **Conclusion**

In conclusion, adding primary key constraint and not null constraint to the employee table is essential to ensure data integrity and prevent errors. By following best practices and using meaningful and consistent column names, we can create a robust and reliable database system.
