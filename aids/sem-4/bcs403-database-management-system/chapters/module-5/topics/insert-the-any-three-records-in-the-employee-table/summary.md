# **Inserting Records in the Employee Table**

## **Key Points**

- **Insert Statement**: Used to add new records to a table.
- **INSERT INTO** statement syntax:
  ```sql
  INSERT INTO table_name (column1, column2, column3, ...)
  VALUES (value1, value2, value3, ...)
  ```

````
* **Attributes**:
  + EMPNO (Employee Number)
  + ENAME (Employee Name)
  + JOB (Job Title)
  + MANAGER_NO (Manager's Employee Number)
  + SAL (Salary)
  + COMMISSION (Commission)

**Rollback**
------------

* **ROLLBACK** statement:
  ```sql
ROLLBACK;
````

Used to undo the last operation (i.e., delete or modify a record).

## **Example**

```sql
INSERT INTO employees (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES (101, 'John Smith', 'Manager', 102, 5000, 1000);
```

## **Important Formulas, Definitions, and Theorems**

- **Primary Key**: A unique identifier for each record in a table (EMPNO in this case).
- **Foreign Key**: A field that references the primary key of another table (MANAGER_NO references EMPNO).

## **Revision Tips**

- Make sure to specify the correct table and column names.
- Use the correct data types for each column.
- Practice inserting records and using rollback statements.
