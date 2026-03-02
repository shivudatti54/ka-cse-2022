# **Database Management System Study Material**

## **Module: Inserting Records into a Table**

### Introduction

In a database management system, inserting records into a table is an essential operation that allows you to add new data to a table. The purpose of this module is to explain the concept of inserting records into a table, including the types of inserts, constraints, and best practices.

### Types of Inserts

There are two types of inserts:

- **INSERT INTO**: This statement is used to add a new record to an existing table.
- **INSERT INTO ... SELECT**: This statement is used to add a new record to an existing table by selecting data from another table.

#### Example of INSERT INTO Statement

```sql
INSERT INTO Employees (Name, Age, Department)
VALUES ('John Doe', 30, 'HR');
```

#### Example of INSERT INTO ... SELECT Statement

```sql
INSERT INTO Orders (CustomerID, OrderDate, Total)
SELECT CustomerID, OrderDate, Total
FROM Sales;
```

### Constraints

Constraints are used to enforce data consistency and integrity in a database. The following are some common types of constraints:

- **Primary Key (PK)**: Each record in a table must have a unique primary key value.
- **Foreign Key (FK)**: A foreign key value must match the primary key value in another table.
- **Unique Constraint (UC)**: Each value in a column must be unique.
- **Check Constraint (CC)**: A specific condition must be met for a value in a column.

#### Example of Primary Key Constraint

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT
);
```

#### Example of Foreign Key Constraint

```sql
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
```

### Best Practices

The following are some best practices for inserting records into a table:

- **Use meaningful column names**: Use descriptive and meaningful column names to make your data more readable.
- **Use indexes**: Create indexes on columns that are frequently used in WHERE and JOIN clauses to improve query performance.
- **Use transactions**: Use transactions to ensure that multiple inserts or updates are executed as a single, atomic operation.
- **Test and verify**: Test and verify the data being inserted to ensure that it is accurate and up-to-date.

### Example Records

The following are five example records that can be inserted into a table:

- **Employee Table**

  | EmployeeID | Name  | Age | Department |
  | ---------- | ----- | --- | ---------- |
  | 1          | John  | 30  | HR         |
  | 2          | Jane  | 25  | Marketing  |
  | 3          | Bob   | 40  | Sales      |
  | 4          | Alice | 28  | IT         |
  | 5          | Mike  | 35  | HR         |

- **Order Table**

  | OrderID | CustomerID | OrderDate  | Total |
  | ------- | ---------- | ---------- | ----- |
  | 1       | 1          | 2022-01-01 | 100   |
  | 2       | 2          | 2022-01-15 | 200   |
  | 3       | 3          | 2022-02-01 | 300   |
  | 4       | 4          | 2022-03-01 | 400   |
  | 5       | 5          | 2022-04-01 | 500   |

### Conclusion

Inserting records into a table is an essential operation in a database management system. By understanding the different types of inserts, constraints, and best practices, you can effectively manage and maintain your database.
