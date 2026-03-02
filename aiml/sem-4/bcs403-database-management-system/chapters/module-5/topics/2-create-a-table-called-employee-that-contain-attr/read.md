# **Database Management System**

## **Module: Creating Tables**

### Introduction

In a database management system, a table is a collection of related data. It is a fundamental concept in database design and is used to store and manage data. In this module, we will learn how to create a table called Employee.

### Definition of a Table

A table is a collection of related data that is stored in rows and columns. Each row represents a single record, and each column represents a field or attribute of that record.

### Attributes of a Table

An attribute is a single field or column in a table that stores a specific piece of data. In this case, we are creating a table called Employee that will contain the attribute EMPNO.

### Creating a Table

To create a table, we use the CREATE TABLE statement. The basic syntax of the CREATE TABLE statement is as follows:

```sql
CREATE TABLE table_name (
  attribute1 data_type,
  attribute2 data_type,
  attribute3 data_type,
  ...
);
```

### Creating the Employee Table

Let's create the Employee table with the attribute EMPNO. The EMPNO attribute will be a unique identifier for each employee.

```sql
CREATE TABLE Employee (
  EMPNO VARCHAR(10) PRIMARY KEY,
  Name VARCHAR(50),
  Department VARCHAR(50),
  Salary DECIMAL(10, 2)
);
```

### Explanation of the Attributes

- **EMPNO**: This is a unique identifier for each employee. It is a VARCHAR(10) data type, which means it can store strings of up to 10 characters.
- **Name**: This attribute stores the name of the employee.
- **Department**: This attribute stores the department of the employee.
- **Salary**: This attribute stores the salary of the employee. It is a DECIMAL(10, 2) data type, which means it can store decimal numbers with up to 10 digits and 2 decimal places.

### Benefits of Creating a Table

Creating a table provides several benefits, including:

- **Organization**: A table helps to organize data in a structured and meaningful way.
- **Efficient Storage**: A table allows for efficient storage of data, reducing the amount of data that needs to be stored.
- **Improved Data Integrity**: A table helps to ensure data integrity by providing a clear and consistent structure for data.

### Best Practices for Creating Tables

When creating tables, it's essential to follow best practices to ensure data quality and integrity. Here are some best practices to keep in mind:

- **Use meaningful attribute names**: Use descriptive and meaningful attribute names to ensure data clarity.
- **Use a consistent data type**: Use a consistent data type for each attribute to ensure data consistency.
- **Use indexes**: Use indexes to improve data retrieval and reduce query time.

### Conclusion

In this module, we learned how to create a table called Employee that contains the attribute EMPNO. We also discussed the benefits and best practices for creating tables, including organization, efficient storage, and improved data integrity.
