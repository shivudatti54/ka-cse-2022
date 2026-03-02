# **Database Management System Revision Notes**

### Topic: Inserting Records in the Employee Table

**Key Points:**

- To insert records into the employee table, we use the `INSERT INTO` statement.
- The `INSERT INTO` statement is used to add new records to a database table.
- The general syntax for inserting records into the employee table is:

  ```sql
  INSERT INTO Employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
  VALUES (EMPNO_VALUE, ENAME_VALUE, JOB_VALUE, MANAGER_NO_VALUE, SAL_VALUE, COMMISSION_VALUE);
  ```

````

**Important Formulas/Definitions/Theorems:**
* **Primary Key**: A unique identifier for each record in a table (EMPNO).
* **Foreign Key**: A field in a table that refers to the primary key of another table (MANAGER_NO).
* **Auto Increment**: A feature that automatically assigns a unique value to a field (EMPNO).

**SQL Code for Inserting Records:**
```sql
-- Insert three records into the employee table
INSERT INTO Employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES
(1001, 'John Doe', 'Manager', NULL, 50000, 5000),
(1002, 'Jane Smith', 'Employee', 1001, 40000, 4000),
(1003, 'Bob Brown', 'Manager', NULL, 60000, 6000);
````

**Using Rollback:**

- To undo changes made by an `INSERT` statement, we use the `ROLLBACK` statement:

```sql
-- Rollback changes made by the insert statement
ROLLBACK;
```

**Revision Tips:**

- Make sure to identify the primary key and foreign key fields in the employee table.
- Understand the syntax for inserting records into a table.
- Familiarize yourself with the `ROLLBACK` statement and its usage.
