# **Textbook 1: Ch 5.1 to 5.3: Database Management Systems**

## **Table of Contents**

1. [Introduction to Database Management Systems](#introduction-to-database-management-systems)
2. [Database Design Principles](#database-design-principles)
   2.1 [Entity-Relationship Modeling](#entity-relationship-modeling)
   2.2 [Data Normalization](#data-normalization)
3. [Database Management System Components](#database-management-system-components)
   3.1 [Database Engine](#database-engine)
   3.2 [Database Interface](#database-interface)
   3.3 [Database Utilities](#database-utilities)
4. [Database Operations](#database-operations)
   4.1 [Insert, Update, and Delete Operations](#insert-update-and-delete-operations)
   4.2 [Querying and Retrieval of Data](#querying-and-retrieval-of-data)
5. [Case Study: Online Shopping Database](#case-study-online-shopping-database)
6. [Conclusion and Further Reading](#conclusion-and-further-reading)

## **Introduction to Database Management Systems**

A Database Management System (DBMS) is a software system that allows you to define, create, maintain, and manipulate databases. It acts as an intermediary between the user and the database, providing a layer of abstraction and control over the data. A DBMS provides a set of rules, protocols, and procedures that enable efficient data storage, retrieval, and manipulation.

## **Database Design Principles**

Database design is an essential aspect of database management. It involves the creation of a database schema, which defines the structure and organization of the data. There are several principles of database design, including:

### Entity-Relationship Modeling

Entity-relationship modeling is a technique used to represent the relationships between entities in a database. It involves creating a diagram that shows the entities, attributes, and relationships between them.

![Entity-Relationship Modeling Diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/ER_modeling_diagram.svg/1200px-ER_modeling_diagram.svg.png)

In this diagram, we have two entities: Customer and Order. The Customer entity has attributes such as Customer ID, Name, and Address. The Order entity has attributes such as Order ID, Customer ID, and Order Date. The relationship between the two entities is a one-to-many relationship, where one customer can have multiple orders.

### Data Normalization

Data normalization is the process of organizing data in a database to minimize data redundancy and dependency. It involves creating multiple tables that contain the same data, with a common attribute that links the tables.

![Data Normalization Diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Data_normalization.svg/800px-Data_normalization.svg.png)

In this diagram, we have two tables: Customers and Orders. The Customers table contains the customer ID, name, and address. The Orders table contains the order ID, customer ID, and order date. The relationship between the two tables is a one-to-many relationship, where one customer can have multiple orders.

## **Database Management System Components**

A DBMS consists of several components, including:

### Database Engine

The database engine is the core component of the DBMS. It is responsible for managing the database, including creating, modifying, and deleting database objects. The database engine also handles data storage, retrieval, and manipulation.

### Database Interface

The database interface is the component that allows users to interact with the database. It provides a set of commands and procedures that enable users to create, modify, and delete database objects.

### Database Utilities

Database utilities are tools that provide additional functionality to the DBMS. They can be used to perform tasks such as data backup, recovery, and optimization.

## **Database Operations**

Database operations are the actions that can be performed on a database. There are several types of database operations, including:

### Insert, Update, and Delete Operations

Insert, update, and delete operations are used to manipulate data in a database.

- **Insert Operation**: The insert operation is used to add new data to a database.
- **Update Operation**: The update operation is used to modify existing data in a database.
- **Delete Operation**: The delete operation is used to remove data from a database.

### Querying and Retrieval of Data

Querying and retrieval of data are used to retrieve data from a database.

- **Query**: A query is a request to retrieve data from a database.
- **Query Language**: A query language is a set of commands and procedures that enable users to create and execute queries.

## **Case Study: Online Shopping Database**

An online shopping database is a database that stores information about products, customers, orders, and payments. The database can be designed using the principles of entity-relationship modeling and data normalization.

```sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(255),
    Address VARCHAR(255)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(255),
    Price DECIMAL(10,2)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY,
    OrderID INT,
    PaymentDate DATE,
    Amount DECIMAL(10,2),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);
```

## **Conclusion and Further Reading**

In conclusion, database management systems are essential for managing and manipulating data. DBMS provides a layer of abstraction and control over data, enabling efficient data storage, retrieval, and manipulation.

For further reading, we recommend the following resources:

- [Database Systems: The Complete Book](https://www.amazon.com/Database-Systems-Complete-Book-4th/dp/0123736278)
- [Database Systems: A User's Manual](https://www.amazon.com/Database-Systems-Manual-3rd-Edition/dp/0123736210)
- [Database Management Systems: An Introduction](https://www.amazon.com/Database-Management-Systems-Introduction-3rd/dp/0123736229)

We hope this comprehensive guide has provided you with a thorough understanding of database management systems.
