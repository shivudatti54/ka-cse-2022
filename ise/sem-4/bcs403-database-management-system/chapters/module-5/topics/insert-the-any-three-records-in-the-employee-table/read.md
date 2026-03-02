# **Inserting Records into the Employee Table**

## **Introduction**

In this module, we will learn how to insert records into the employee table using SQL. We will cover the basic syntax of the INSERT statement, how to specify the columns and values, and how to use the ROLLBACK statement to undo any changes made to the table.

## **Defining the Employee Table**

The employee table has the following attributes:

- EMPNO: a unique identifier for each employee
- ENAME: the name of the employee
- JOB: the job title of the employee
- MANAGER_NO: the manager's ID
- SAL: the employee's salary
- COMMISSION: the employee's commission

Here is the SQL code to create the employee table:

```sql
CREATE TABLE Employee (
  EMPNO INT PRIMARY KEY,
  ENAME VARCHAR(50),
  JOB VARCHAR(50),
  MANAGER_NO INT,
  SAL DECIMAL(10, 2),
  COMMISSION DECIMAL(10, 2)
);
```

## **Inserting Records into the Employee Table**

To insert a record into the employee table, we use the INSERT INTO statement. Here is the basic syntax:

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

Here are a few examples of inserting records into the employee table:

### Example 1: Inserting a single record

```sql
INSERT INTO Employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES (1, 'John Doe', 'Software Engineer', 101, 50000.00, 1000.00);
```

### Example 2: Inserting multiple records

```sql
INSERT INTO Employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES
(2, 'Jane Doe', 'Marketing Manager', 102, 60000.00, 2000.00),
(3, 'Bob Smith', 'Sales Representative', 103, 40000.00, 1500.00);
```

## **Using ROLLBACK to Undo Changes**

Sometimes, we may want to undo changes that we have made to the table. To do this, we can use the ROLLBACK statement. Here is the basic syntax:

```sql
ROLLBACK;
```

This statement will undo all the changes made since the last COMMIT statement.

**Example: Using ROLLBACK to undo changes**

Let's say we have inserted the following record into the employee table:

```sql
INSERT INTO Employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES (4, 'Alice Johnson', 'Data Analyst', 104, 45000.00, 1200.00);
```

And we want to undo this change. We can use the ROLLBACK statement to do so:

```sql
INSERT INTO Employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES (4, 'Alice Johnson', 'Data Analyst', 104, 45000.00, 1200.00);
ROLLBACK;
```

## **Key Concepts**

- **INSERT INTO**: used to insert new records into a table
- **VALUES**: specifies the values to be inserted into the table
- **ROLLBACK**: used to undo changes made to the table
- **COMMIT**: used to save changes made to the table

## **Best Practices**

- Always back up your data before making any changes to the table
- Use the ROLLBACK statement to undo changes if needed
- Use the COMMIT statement to save changes made to the table

## **Conclusion**

In this module, we learned how to insert records into the employee table using SQL. We covered the basic syntax of the INSERT statement, how to specify the columns and values, and how to use the ROLLBACK statement to undo any changes made to the table. We also discussed key concepts, best practices, and how to apply them in real-world scenarios.
