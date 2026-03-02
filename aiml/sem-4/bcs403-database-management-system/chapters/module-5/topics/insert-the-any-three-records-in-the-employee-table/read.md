# **DATABASE MANAGEMENT SYSTEM: INSERTING RECORDS INTO THE EMPLOYEE TABLE**

## **Introduction**

In this module, we will be learning about inserting records into the employee table in a database management system. The employee table contains various attributes that provide information about each employee, including their employee number, name, job, manager, salary, and commission.

## **Key Concepts**

- **Insert Statement**: An insert statement is used to add new records to a table in a database management system.
- **Rollback**: Rollback is a feature that allows you to undo changes made to a database after they have been committed.

## **The Employee Table**

The employee table contains the following attributes:

| Attribute  | Description                         |
| ---------- | ----------------------------------- |
| EMPNO      | Unique identifier for each employee |
| ENAME      | Employee's name                     |
| JOB        | Employee's job title                |
| MANAGER_NO | Manager's employee number           |
| SAL        | Employee's salary                   |
| COMMISSION | Employee's commission               |

## **INSERT Statement**

To insert a new record into the employee table, you use the following SQL statement:

```sql
INSERT INTO employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION);
```

However, this statement is incomplete as it doesn't specify the values for EMPNO, ENAME, JOB, MANAGER_NO, SAL, and COMMISSION.

## **Using Rollback**

Rollback is a feature that allows you to undo changes made to a database after they have been committed. To use rollback, you use the following SQL statement:

```sql
ROLLBACK;
```

This statement will undo all the changes made to the database since the last commit.

## **Inserting Records with Rollback**

To insert a new record into the employee table with rollback, you can use the following SQL statement:

```sql
INSERT INTO employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES (1001, 'John Doe', 'Manager', 1002, 50000, 1000);

-- attempt to insert another record
INSERT INTO employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES (1003, 'Jane Smith', 'Employee', 1001, 40000, 500);

-- use rollback to undo changes
ROLLBACK;
```

In the above example, the first insert statement is successful and a new record is added to the employee table. However, the second insert statement is not successful because the values for EMPNO, ENAME, JOB, MANAGER_NO, SAL, and COMMISSION conflict with the existing records in the employee table. When you use rollback, all the changes made to the database since the last commit are undone, and the employee table is restored to its previous state.

## **Best Practices**

When working with insert statements and rollback, follow these best practices:

- Always specify all the required attributes in the insert statement.
- Use rollback to undo changes made to the database.
- Test your insert statements thoroughly to avoid errors.

## **Example Use Cases**

- **Inserting new employees**: To insert new employees into the employee table, you can use the following SQL statement:

```sql
INSERT INTO employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES (1001, 'John Doe', 'Manager', 1002, 50000, 1000);
```

- **Inserting updated information**: To insert updated information into the employee table, you can use the following SQL statement:

```sql
UPDATE employee
SET ENAME = 'Jane Doe', SAL = 60000
WHERE EMPNO = 1001;
```

- **Inserting deleted information**: To insert deleted information into the employee table, you can use the following SQL statement:

```sql
DELETE FROM employee
WHERE EMPNO = 1001;
```
