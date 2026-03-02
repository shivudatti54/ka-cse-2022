# **DATABASE MANAGEMENT SYSTEM**

## **Module: No. of Hours:08**

## **Topic: Insert any five records into the table**

## **Introduction**

In this topic, we will learn about the concept of inserting records into a database table. A database table is a fundamental concept in database management systems, and inserting records into it is an essential operation in managing data. In this topic, we will explore the concept of inserting records into a table, discuss the different methods of insertion, and provide examples and case studies to illustrate the concept.

## **Historical Context**

The concept of database tables and insertion of records dates back to the 1960s when the first relational database management systems (RDBMS) were developed. The first RDBMS, called System R, was developed in 1970 by IBM. System R used a flat file structure to store data, but it was later replaced by a relational database management system, called System F, which used tables to store data.

The concept of insertion of records into a table was first introduced in the 1970s with the development of the relational algebra model. The relational algebra model is a mathematical model for manipulating data in relational databases. It provides a set of operators for inserting, selecting, and modifying data in a relational database.

## **Modern Developments**

In recent years, database management systems have evolved to support more advanced features and technologies. Some of the modern developments in database management systems include:

- **NoSQL databases**: NoSQL databases are designed to handle large amounts of unstructured or semi-structured data. They use a different data model than relational databases and do not support the concept of tables.
- **Cloud-based databases**: Cloud-based databases are designed to be scalable and flexible. They use a cloud-based infrastructure to store and manage data.
- **Big data analytics**: Big data analytics is a set of technologies and techniques used to analyze large amounts of data. It uses a combination of data processing, machine learning, and data visualization to gain insights from data.

## **Inserting Records into a Table**

Inserting records into a table is an essential operation in managing data in a database management system. There are several methods of inserting records into a table, including:

### 1. **INSERT INTO Statement**

The INSERT INTO statement is used to insert new records into a table. The syntax of the INSERT INTO statement is as follows:

```sql
INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);
```

For example, suppose we have a table called `employees` with columns `employee_id`, `name`, and `department`. We can insert a new record into the table using the following SQL statement:

```sql
INSERT INTO employees (employee_id, name, department)
VALUES (101, 'John Doe', 'Sales');
```

### 2. **INSERT INTO SELECT Statement**

The INSERT INTO SELECT statement is used to insert new records into a table using data from another table. The syntax of the INSERT INTO SELECT statement is as follows:

```sql
INSERT INTO table_name (column1, column2, column3)
SELECT column1, column2, column3
FROM table_name;
```

For example, suppose we have two tables called `employees` and `departments`. We can insert new records into the `employees` table using data from the `departments` table using the following SQL statement:

```sql
INSERT INTO employees (employee_id, name, department_id)
SELECT employee_id, name, department_id
FROM departments;
```

### 3. **INSERT INTO VALUES Statement**

The INSERT INTO VALUES statement is used to insert new records into a table using a single value. The syntax of the INSERT INTO VALUES statement is as follows:

```sql
INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);
```

For example, suppose we have a table called `employees` with columns `employee_id`, `name`, and `department`. We can insert a new record into the table using the following SQL statement:

```sql
INSERT INTO employees (employee_id, name, department)
VALUES (102, 'Jane Doe', 'Marketing');
```

## **Case Studies**

### 1. **Inserting Records into a Table**

Suppose we have a table called `orders` with columns `order_id`, `customer_id`, and `order_date`. We want to insert a new record into the table using the following data:

| order_id | customer_id | order_date |
| -------- | ----------- | ---------- |
| 201      | 101         | 2022-01-01 |
| 202      | 102         | 2022-01-15 |
| 203      | 103         | 2022-02-01 |

We can insert the records into the table using the following SQL statement:

```sql
INSERT INTO orders (order_id, customer_id, order_date)
VALUES (201, 101, '2022-01-01'),
       (202, 102, '2022-01-15'),
       (203, 103, '2022-02-01');
```

### 2. **Inserting Records into a Table using Data from Another Table**

Suppose we have two tables called `employees` and `departments`. We want to insert new records into the `employees` table using data from the `departments` table. We can insert the records into the table using the following SQL statement:

```sql
INSERT INTO employees (employee_id, name, department_id)
SELECT employee_id, name, department_id
FROM departments;
```

## **Applications**

Inserting records into a table has numerous applications in various fields, including:

- **Business**: Inserting records into a table can be used to manage customer data, order data, and product data.
- **Healthcare**: Inserting records into a table can be used to manage patient data, medical records, and billing information.
- **Finance**: Inserting records into a table can be used to manage transaction data, account information, and financial reports.

## **Diagrams and Descriptions**

The following diagram illustrates the process of inserting records into a table:

```
  +---------------+
  |  Table      |
  +---------------+
           |
           |
           v
  +---------------+
  |  INSERT INTO  |
  |  Statement    |
  +---------------+
           |
           |
           v
  +---------------+
  |  Table Data  |
  +---------------+
           |
           |
           v
  +---------------+
  |  New Record  |
  +---------------+
```

## **Further Reading**

- **Database Management Systems**: A Modern Approach (2nd Edition) by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- **Database Systems: The Complete Book (4th Edition)** by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- **SQL Queries for Mere Mortals (2nd Edition)** by John D. Cook
- **Database Systems: An Introduction (6th Edition)** by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
