# Add Primary Key Constraint and Not Null Constraint to the Employee Table

===========================================================

## Introduction

---

In a database, a primary key constraint is used to uniquely identify each record in a table. On the other hand, a not null constraint ensures that a column cannot contain null values. In this study material, we will learn how to add these constraints to the employee table in a database.

## Primary Key Constraint

---

### Definition

A primary key constraint is a constraint that ensures each record in a table has a unique combination of values in its columns. It acts as a unique identifier for each record.

### Explanation

When a column is defined as the primary key of a table, the database management system (DBMS) ensures that each record in the table has a unique combination of values in that column. This prevents duplicate entries in the table.

### Example

Suppose we have an employee table with columns for employee ID, name, age, and salary.

| Employee ID | Name | Age | Salary |
| ----------- | ---- | --- | ------ |
| 1           | John | 25  | 5000   |
| 2           | Jane | 30  | 6000   |

If we add the employee ID as the primary key to this table, the DBMS will ensure that each record has a unique employee ID. For example, if we try to insert a record with an employee ID of 1, the DBMS will reject it because it already exists in the table.

### How to Add Primary Key Constraint

To add a primary key constraint to a table, follow these steps:

1. Open the table in the database management system.
2. Click on the column you want to make the primary key.
3. In the constraints section, select "Primary Key" from the dropdown menu.
4. Click "OK" to save the changes.

## Not Null Constraint

---

### Definition

A not null constraint ensures that a column cannot contain null values.

### Explanation

When a column is defined as not null, the DBMS ensures that it always contains a value. This prevents null values from being inserted into the column.

### Example

Suppose we have an employee table with columns for employee ID, name, age, and salary.

| Employee ID | Name | Age | Salary |
| ----------- | ---- | --- | ------ |
| 1           | John | 25  | 5000   |

If we add the name column as not null to this table, the DBMS will reject any attempt to insert a record with a null value in the name column.

### How to Add Not Null Constraint

To add a not null constraint to a column, follow these steps:

1. Open the table in the database management system.
2. Click on the column you want to make not null.
3. In the constraints section, select "Not Null" from the dropdown menu.
4. Click "OK" to save the changes.

## Best Practices

---

- Always define primary key constraints for tables that contain unique identifiers.
- Always define not null constraints for columns that contain meaningful data.
- Use primary key and not null constraints to ensure data integrity and prevent errors.

## Conclusion

---

In this study material, we learned how to add primary key and not null constraints to the employee table. By following the best practices and using these constraints, we can ensure data integrity and prevent errors in our database.
