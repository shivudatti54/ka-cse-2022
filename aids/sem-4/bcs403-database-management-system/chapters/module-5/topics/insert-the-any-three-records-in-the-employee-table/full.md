# **DATABASE MANAGEMENT SYSTEM**

**Module:** No. of Hours: 08
**Topic:** Insert the any three records in the employee table contains attributes EMPNO,ENAME JOB, MANAGER_NO, SAL, COMMISSION and use rollback

## **Introduction**

In this module, we will explore the concept of inserting records into a database table using SQL. We will focus on the employee table, which contains attributes such as EMPNO, ENAME, JOB, MANAGER_NO, SAL, and COMMISSION. We will also discuss the importance of using rollback statements to maintain data consistency.

## **Historical Context**

The concept of database management systems (DBMS) has been around for several decades. The first DBMS was developed in the 1960s, and since then, it has evolved significantly. The introduction of relational databases in the 1970s revolutionized the field of database management. Today, DBMS is an essential tool in many industries, including business, finance, healthcare, and more.

## **Modern Developments**

In recent years, there have been significant advancements in DBMS. Some of the key developments include:

- **Cloud-based DBMS**: Cloud-based DBMS allows for scalable and flexible database management.
- **Big Data**: The availability of large amounts of data has led to the development of big data analytics and processing techniques.
- **NoSQL Databases**: NoSQL databases are designed to handle large amounts of unstructured data and provide high scalability.

## **Employee Table**

The employee table is a fundamental table in any database management system. It contains attributes such as EMPNO, ENAME, JOB, MANAGER_NO, SAL, and COMMISSION. Here is a simple diagram of the employee table:

```
+---------+----------+--------+--------+-------+--------+
| EMPNO  | ENAME   | JOB    | MANAGER_NO | SAL | COMMISSION |
+---------+----------+--------+--------+-------+--------+
| 101    | John     | Manager | 102      | 5000 | 10%      |
| 102    | Jane     | Employee| 101      | 4000 | 5%       |
| 103    | Bob      | Employee| 102      | 4500 | 8%       |
+---------+----------+--------+--------+-------+--------+
```

## **Inserting Records**

To insert records into the employee table, we can use the following SQL command:

```sql
INSERT INTO employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES (104, 'Alice', 'Employee', 103, 4200, 6%)
```

This command inserts a new record into the employee table with the specified attributes.

## **Using Rollback**

Rollback is an essential concept in database management. It allows us to undo changes made to the database in case of an error or failure. To use rollback, we need to use the following SQL command:

```sql
BEGIN TRANSACTION;
INSERT INTO employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES (104, 'Alice', 'Employee', 103, 4200, 6%)
ON CONFLICT (EMPNO) DO NOTHING;
COMMIT;
```

In this example, we use the `BEGIN TRANSACTION` command to start a new transaction. We then insert the record into the employee table using the `INSERT INTO` command. The `ON CONFLICT (EMPNO) DO NOTHING` clause is used to handle conflicts when inserting a new record with an existing EMPNO. Finally, we use the `COMMIT` command to commit the transaction.

However, what if we want to cancel the transaction and undo the changes made? In that case, we can use the `ROLLBACK` command:

```sql
BEGIN TRANSACTION;
INSERT INTO employee (EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION)
VALUES (104, 'Alice', 'Employee', 103, 4200, 6%)
ON CONFLICT (EMPNO) DO NOTHING;
COMMIT;
ROLLBACK;
```

In this example, we use the `ROLLBACK` command to undo the changes made to the database.

## **Case Studies**

Here are a few case studies that demonstrate the use of inserting records into a database table and using rollback:

- **Employee Onboarding**: When a new employee joins the company, their details need to be inserted into the employee table. To ensure data consistency, we can use rollback to handle any errors that may occur during the onboarding process.
- **Employee Termination**: When an employee is terminated, their details need to be deleted from the employee table. To ensure data consistency, we can use rollback to handle any errors that may occur during the termination process.

## **Applications**

Inserting records into a database table and using rollback have numerous applications in various industries. Some of the key applications include:

- **Human Resource Management**: Employee data needs to be inserted into the database to manage employee information.
- **Accounting**: Financial data needs to be inserted into the database to manage financial transactions.
- **Healthcare**: Patient data needs to be inserted into the database to manage patient information.

## **Diagrams and Descriptions**

Here is a simple diagram of the employee table:

```
+---------+----------+--------+--------+-------+--------+
| EMPNO  | ENAME   | JOB    | MANAGER_NO | SAL | COMMISSION |
+---------+----------+--------+--------+-------+--------+
| 101    | John     | Manager | 102      | 5000 | 10%      |
| 102    | Jane     | Employee| 101      | 4000 | 5%       |
| 103    | Bob      | Employee| 102      | 4500 | 8%       |
+---------+----------+--------+--------+-------+--------+
```

This diagram shows the attributes of the employee table, including EMPNO, ENAME, JOB, MANAGER_NO, SAL, and COMMISSION.

## **Further Reading**

For further reading, I recommend the following resources:

- **Database Systems: The Complete Book** by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- **Database Systems: Design, Implementation, and Management** by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- **Oracle Database SQL Developer**: A comprehensive guide to SQL and database management

Note: The above resources are just a few examples and are not an exhaustive list.
