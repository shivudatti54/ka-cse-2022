# **Introduction to Databases: Introduction, Characteristics of Database Approach, Advantages of using the DBMS Approach, History of Database Applications**

## **Module: DATABASE MANAGEMENT SYSTEM**

## **Duration: 8 hours**

## **Topic Overview**

This module provides a comprehensive introduction to databases, covering the fundamental concepts, characteristics of the database approach, advantages of using a Database Management System (DBMS), and a brief history of database applications. Students will gain a deep understanding of databases and how they are used to manage and store data.

## **Introduction to Databases**

A database is a collection of organized data that is stored in a way that allows for efficient retrieval and manipulation. Databases are used to store and manage large amounts of data, and they provide a structured way of organizing and accessing data. The database approach is based on the following fundamental principles:

### 1. **Data Independence**

The database approach is based on the principle of data independence, which means that the data is separate from the application that accesses it. This allows for changes to be made to the database without affecting the application.

### 2. **Concurrent Access**

The database approach allows for multiple users to access the data simultaneously, without affecting the integrity of the data.

### 3. **Data Integrity**

The database approach ensures that the data is consistent and accurate, by using techniques such as transactions and checksums.

### 4. **Data Security**

The database approach provides a way to control access to the data, by using authentication and authorization mechanisms.

## **Characteristics of the Database Approach**

The database approach has several key characteristics, including:

### 1. **Centralized Data Storage**

The database approach stores data in a centralized location, which makes it easier to manage and retrieve.

### 2. **Structured Data**

The database approach stores data in a structured format, which makes it easier to retrieve and manipulate.

### 3. **Autonomous Data**

The database approach allows the data to be autonomous, which means that it can be managed and maintained independently.

### 4. **Scalability**

The database approach is scalable, which means that it can be used to manage large amounts of data.

## **Advantages of using the DBMS Approach**

The DBMS approach has several advantages, including:

### 1. **Improved Data Security**

The DBMS approach provides a way to control access to the data, which improves data security.

### 2. **Improved Data Integrity**

The DBMS approach ensures that the data is consistent and accurate, which improves data integrity.

### 3. **Improved Data Scalability**

The DBMS approach is scalable, which means that it can be used to manage large amounts of data.

### 4. **Improved Data Performance**

The DBMS approach provides a way to optimize data performance, which improves the speed and efficiency of data retrieval and manipulation.

## **History of Database Applications**

The history of database applications dates back to the 1950s, when the first databases were developed. The first databases were primarily used for scientific and engineering applications, but they quickly gained popularity in the 1960s and 1970s, when they were used in business and government applications.

### 1. **Early Database Systems (1950s-1960s)**

The first databases were developed in the 1950s and 1960s, primarily for scientific and engineering applications. These early database systems were based on the concept of a centralized data storage system.

### 2. **Relational Database Management Systems (1970s-1980s)**

In the 1970s and 1980s, relational database management systems (RDBMS) were developed. RDBMS were based on the concept of a relational database, which used tables and relationships to store and retrieve data.

### 3. **Object-Oriented Database Management Systems (1990s-2000s)**

In the 1990s and 2000s, object-oriented database management systems (OODBMS) were developed. OODBMS were based on the concept of an object-oriented database, which used objects and relationships to store and retrieve data.

### 4. **Modern Database Management Systems (2000s-present)**

In the 2000s, modern database management systems (DBMS) were developed. These DBMS were based on the concept of a hybrid database, which combined the benefits of RDBMS and OODBMS.

## **Case Study: Online Shopping Database**

Online shopping databases are used to manage and store data related to online shopping. A typical online shopping database would include the following tables:

- **Customers**: This table stores data about customers, including their names, addresses, and contact information.
- **Products**: This table stores data about products, including their names, descriptions, prices, and images.
- **Orders**: This table stores data about orders, including the customer's name, the product's name, the order date, and the total cost.
- **Payments**: This table stores data about payments, including the payment date, the payment amount, and the payment method.

## **Example Use Case: Database Query**

Suppose we want to retrieve all orders made by a specific customer. We can use a database query to achieve this. The query would involve the following steps:

1.  **Connect to the database**: We need to connect to the database using a DBMS driver.
2.  **Select the relevant tables**: We need to select the relevant tables in the database, which in this case are the **Customers** and **Orders** tables.
3.  **Join the tables**: We need to join the **Customers** and **Orders** tables based on the customer's name.
4.  **Filter the results**: We need to filter the results to retrieve only the orders made by the specific customer.
5.  **Retrieve the data**: We need to retrieve the data from the database using the query.

## **Diagram: Database Schema**

Here is a diagram of a typical database schema:

```markdown
+---------------+
| Customers |
+---------------+
| +-----------+ |
| | Customer | |
| | ID (PK) | |
| +-----------+ |
| | Name | |
| | Address | |
| | Phone | |
| +-----------+ |
+---------------+

+---------------+
| Products |
+---------------+
| +-----------+ |
| | Product | |
| | ID (PK) | |
| +-----------+ |
| | Name | |
| | Description| |
| | Price | |
| | Image | |
| +-----------+ |
+---------------+

+---------------+
| Orders |
+---------------+
| +-----------+ |
| | Order | |
| | ID (PK) | |
| +-----------+ |
| | Customer | |
| | ID (FK) | |
| | Order Date| |
| | Total Cost| |
| +-----------+ |
+---------------+

+---------------+
| Payments |
+---------------+
| +-----------+ |
| | Payment | |
| | ID (PK) | |
| +-----------+ |
| | Payment Date| |
| | Payment Amount| |
| | Payment Method| |
| +-----------+ |
+---------------+
```

## **Conclusion**

In this module, we have covered the fundamental concepts of databases, including the database approach, characteristics of the database approach, advantages of using the DBMS approach, and a brief history of database applications. We have also provided a case study and an example use case to illustrate the use of a database. Finally, we have provided a diagram of a typical database schema to help visualize the structure of a database.

## **Further Reading**

- "Database Systems: The Complete Book" by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- "Data Warehousing for Business Intelligence" by Hans-Peter Kriegel, Peter N. Lindner, and John P. Shepherd
- "Database Systems: A Practical Approach" by David J. DeWitt, Ralph L. Carter, and James M. Ullman
- "Data Mining: Concepts and Techniques" by Jiawei Han, Micheline Kamber, and Jian Pei
