# **Creating a Table Called Employee with Attributes EMPNO**

## **Introduction**

In this module, we will be learning about database management systems, specifically how to create a table called Employee with attributes EMPNO. This module is part of a larger course that covers the fundamentals of database management systems, including data modeling, normalization, and querying.

## **Historical Context**

The concept of a database management system has been around for decades. The first database management system, called IDMS (Interactive Data Management System), was developed in the 1960s. However, it wasn't until the introduction of relational databases in the 1970s that database management systems became more widely used.

Relational databases, as developed by Edgar F. Codd, revolutionized the way data was stored and managed. They introduced the concept of tables, rows, and columns, which made it easier to store and retrieve data.

## **Modern Developments**

Today, database management systems are used in a wide range of industries, including healthcare, finance, and e-commerce. With the advent of cloud computing and big data, the need for advanced database management systems has increased.

Modern database management systems, such as MySQL, PostgreSQL, and MongoDB, offer a range of features, including data normalization, indexing, and querying. They are also highly scalable and can handle large amounts of data.

## **Creating a Table Called Employee with Attributes EMPNO**

In this section, we will learn how to create a table called Employee with attributes EMPNO using a relational database management system.

## **Table Structure**

A table is a collection of related data that is stored in a database. Each table has a unique name, and each row in the table is called a record. The attributes of a table are the columns that make up the table.

In this case, we will create a table called Employee that contains the following attributes:

- EMPNO: a unique identifier for each employee
- EMPNAME: the name of each employee
- DEPTNO: the department each employee belongs to
- SALARY: the salary of each employee

## **SQL Code**

Here is the SQL code to create the Employee table:

```sql
CREATE TABLE Employee (
  EMPNO INT PRIMARY KEY,
  EMPNAME VARCHAR(255) NOT NULL,
  DEPTNO INT NOT NULL,
  SALARY DECIMAL(10, 2) NOT NULL
);
```

In this code:

- `CREATE TABLE` is the keyword used to create a new table.
- `Employee` is the name of the table.
- `EMPNO` is the primary key of the table, which means it uniquely identifies each record.
- `EMPNAME`, `DEPTNO`, and `SALARY` are the attributes of the table.

## **Data Types**

Here is a brief explanation of the data types used in the code:

- `INT`: whole numbers, used for EMPNO and DEPTNO.
- `VARCHAR(255)`: a string of characters, used for EMPNAME.
- `DECIMAL(10, 2)`: a decimal number, used for SALARY.

## **Constraints**

Constraints are rules that are enforced on the data in a table. In this case, we have the following constraints:

- PRIMARY KEY: EMPNO must be unique for each record.
- NOT NULL: EMPNAME, DEPTNO, and SALARY cannot be empty.

## **Inserting Data**

Here is an example of how to insert data into the Employee table:

```sql
INSERT INTO Employee (EMPNO, EMPNAME, DEPTNO, SALARY)
VALUES (1, 'John Doe', 1, 50000.00),
       (2, 'Jane Smith', 2, 60000.00),
       (3, 'Bob Johnson', 1, 70000.00);
```

In this code:

- `INSERT INTO` is the keyword used to insert data into a table.
- `EMPNO`, `EMPNAME`, `DEPTNO`, and `SALARY` are the attributes of the table.
- `VALUES` is the keyword used to specify the data to be inserted.
- `(1, 'John Doe', 1, 50000.00)`, `(2, 'Jane Smith', 2, 60000.00)`, and `(3, 'Bob Johnson', 1, 70000.00)` are the data to be inserted.

## **Querying Data**

Here is an example of how to query data from the Employee table:

```sql
SELECT * FROM Employee WHERE EMPNO = 2;
```

In this code:

- `SELECT` is the keyword used to select data from a table.
- `*` is the wildcard character used to select all columns.
- `FROM` is the keyword used to specify the table.
- `Employee` is the name of the table.
- `WHERE` is the keyword used to specify the condition for which rows to select.
- `EMPNO = 2` is the condition for which rows to select.

## **Diagram Description**

Here is a diagram description of the Employee table:

```markdown
+---------------+
| EMPNO (INT) |
+---------------+
| EMPNAME (VARCHAR) |
+---------------+
| DEPTNO (INT) |
+---------------+
| SALARY (DECIMAL) |
+---------------+
```

In this diagram:

- The table has four columns: EMPNO, EMPNAME, DEPTNO, and SALARY.
- Each column has a unique data type.

## **Case Study**

Here is a case study of how the Employee table can be used in a real-world scenario:

Suppose we are a company that offers employee benefits, such as health insurance and retirement plans. We want to create a database to manage our employee data and provide benefits to our employees.

We can use the Employee table to store information about our employees, such as their name, department, salary, and benefits. We can then use the database to query the data and provide benefits to our employees.

## **Applications**

The Employee table can be used in a variety of applications, including:

- Human resources management: the Employee table can be used to store information about employees, such as their name, department, salary, and benefits.
- Payroll management: the Employee table can be used to store information about employee salaries and benefits.
- Benefits management: the Employee table can be used to store information about employee benefits, such as health insurance and retirement plans.

## **Further Reading**

Here are some further reading suggestions:

- "Database Systems: The Complete Book" by Hector Garcia-Molina
- "Database Systems: The Complete Book" by Hector Garcia-Molina (2nd edition)
- "Database Systems: A Practical Approach" by Hector Garcia-Molina
- "Database Systems: A Practical Approach" by Hector Garcia-Molina (2nd edition)
- "Database Systems: A Practical Approach" by Hector Garcia-Molina (3rd edition)
