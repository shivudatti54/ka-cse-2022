# **Database Management System Study Material**

## **Topic: Inserting Records into a Database**

## **Introduction**

In this topic, we will learn about inserting records into a database table. A record in a database is a set of values that describe a particular entity, such as an employee. In this case, we will be working with the employee table, which contains attributes such as EMPNO, ENAME, JOB, MANAGER_NO, SAL, and COMMISSION.

## **What is a Database Table?**

A database table is a collection of related data that is organized into rows and columns. Each column represents an attribute of the entity, and each row represents a single record.

## **Attributes of the Employee Table**

The employee table contains the following attributes:

- **EMPNO**: a unique identifier for each employee
- **ENAME**: the name of the employee
- **JOB**: the job title of the employee
- **MANAGER_NO**: the identifier of the employee's manager
- **SAL**: the salary of the employee
- **COMMISSION**: the commission earned by the employee

## **Inserting Records into the Employee Table**

To insert a record into the employee table, we use the INSERT INTO statement followed by the table name and the values to be inserted.

**Syntax:**

```sql
INSERT INTO table_name (attribute1, attribute2, ...)
VALUES (value1, value2, ...)
```

**Example:**

```sql
INSERT INTO employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES (101, 'John Doe', 'Manager', 101, 50000, 1000)
```

This statement inserts a new record into the employee table with the attributes EMPNO, ENAME, JOB, MANAGER_NO, SAL, and COMMISSION, and the values 101, 'John Doe', 'Manager', 101, 50000, and 1000, respectively.

## **Using Rollback**

Rollback is a feature that allows us to undo changes made to the database in case of an error or unexpected situation. To use rollback, we use the ROLLBACK statement.

**Syntax:**

```sql
ROLLBACK
```

**Example:**

```sql
INSERT INTO employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES (101, 'John Doe', 'Manager', 101, 50000, 1000);

-- simulate an error
INSERT INTO employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES (102, 'Jane Doe', 'Employee', 102, 40000, 500);

-- use rollback to undo the changes
ROLLBACK;
```

In this example, we first insert a new record into the employee table with the attributes EMPNO, ENAME, JOB, MANAGER_NO, SAL, and COMMISSION, and the values 101, 'John Doe', 'Manager', 101, 50000, and 1000, respectively. Then, we simulate an error by inserting a new record with invalid data. Finally, we use the ROLLBACK statement to undo the changes and return the database to its previous state.

**Key Concepts:**

- **INSERT INTO**: used to insert new records into a database table
- **Attributes**: define the characteristics of the data in a database table
- **Rollback**: used to undo changes made to the database in case of an error or unexpected situation

**Practice Exercises:**

1.  Insert three new records into the employee table using the INSERT INTO statement.
2.  Use rollback to undo changes made to the employee table after inserting a new record with invalid data.

## **Conclusion:**

In this topic, we learned about inserting records into a database table and using rollback to undo changes made to the database. We also learned about the attributes of the employee table and how to use the INSERT INTO statement to insert new records. We also learned about the importance of using rollback to prevent data loss in case of an error or unexpected situation.
