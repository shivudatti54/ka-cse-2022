# **DATABASE MANAGEMENT SYSTEM**

## **Module: No. of Hours: 8**

## **Topic: Ch 8.1 to 8.5**

### 8.1 Introduction to Database Management Systems

A Database Management System (DBMS) is a software system that allows you to define, create, maintain, and manipulate databases. It acts as an intermediary between the user and the physical database, providing a layer of abstraction and making it easier to manage and interact with the data.

## **Historical Context**

The concept of DBMS dates back to the 1960s, when the first relational databases were developed. The relational model, introduced by Edgar F. Codd in 1970, revolutionized the field of database management. The relational model consists of entities, attributes, and relationships between them, and it is still the basis for most modern DBMS.

## **Modern Developments**

In recent years, there has been a shift towards more modern and flexible DBMS, such as NoSQL databases and cloud-based databases. NoSQL databases, such as MongoDB and Cassandra, are designed to handle large amounts of unstructured or semi-structured data, while cloud-based databases, such as Amazon RDS and Google Cloud SQL, provide scalability and flexibility.

## **Components of a DBMS**

A DBMS typically consists of the following components:

- **Database**: The actual collection of data.
- **Database Management System**: The software system that manages the database.
- **Database Designer**: A tool used to design and create the database schema.
- **Query Language**: A language used to retrieve and manipulate data.

### 8.2 Relational Database Management Systems (RDBMS)

Relational databases are the most widely used type of database. They use the relational model, which consists of entities, attributes, and relationships between them.

## **Characteristics of RDBMS**

- **Data normalization**: Data is organized into tables, with each table having a primary key and foreign keys to establish relationships.
- **Data consistency**: Data is consistent and up-to-date, with transactions ensuring that data is not modified until it is confirmed.
- **Data integrity**: Data is accurate and reliable, with checks and balances in place to prevent errors.

**Example:**

```sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(255),
    Address VARCHAR(255),
    Phone VARCHAR(20)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
```

### 8.3 Object-Relational Database Management Systems (ORDBMS)

Object-relational databases are a type of database that combines the features of relational databases with those of object-oriented databases.

## **Characteristics of ORDBMS**

- **Object-oriented data model**: Data is organized as objects, with each object having its own attributes and relationships.
- **Support for inheritance**: Objects can inherit attributes and behaviors from other objects.
- **Support for polymorphism**: Objects can take on multiple forms, depending on the context.

**Example:**

```sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(255),
    Address VARCHAR(255),
    Phone VARCHAR(20)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TYPE AddressType AS OBJECT (
    Street VARCHAR(255),
    City VARCHAR(255),
    PostCode VARCHAR(10)
);

CREATE TYPE CustomerAddress AS REF AddressType;
```

### 8.4 NoSQL Database Management Systems

NoSQL databases are designed to handle large amounts of unstructured or semi-structured data.

## **Characteristics of NoSQL DBMS**

- **Schema-less data model**: Data is stored without a predefined schema.
- **Flexible data model**: Data can be stored in various formats, such as key-value pairs, documents, or graphs.
- **Scalability**: NoSQL databases are designed to handle large amounts of data and can scale horizontally.

**Example:**

```javascript
const mongoose = require('mongoose');

const customerSchema = new mongoose.Schema({
  name: String,
  address: {
    street: String,
    city: String,
    postcode: String,
  },
});

const Customer = mongoose.model('Customer', customerSchema);
```

### 8.5 Cloud-Based Database Management Systems

Cloud-based databases are designed to provide scalability and flexibility.

## **Characteristics of Cloud-Based DBMS**

- **Scalability**: Cloud-based databases can scale up or down as needed.
- **Flexibility**: Cloud-based databases can be accessed from anywhere and can be used on various devices.
- **Cost-effectiveness**: Cloud-based databases can be more cost-effective than traditional databases.

**Example:**

```bash
aws rds create-db-instance --db-instance-identifier mydb --engine postgres --instance-class db.t3.micro
```

### Further Reading

---

- [Database Systems: The Complete Book](https://www.amazon.com/Database-Systems-Complete-Book-Computer/dp/0123737001)
- [Database Systems: The Complete Book](https://books.google.com/books/about/Database_Systems_The_Complete_Book.html?id=QYvRAgAAQBAJ)
- [Database Management Systems](https://www.coursera.org/specializations/database-management)
- [Database Management Systems](<https://www.msdn.microsoft.com/en-us/library/aa580710(v=vs.71).aspx>)

### Diagrams and Figures

---

- **Entity-Relationship Diagram (ERD)**: A diagram used to visualize the relationships between entities in a database.
- **Database Schema Diagram**: A diagram used to visualize the structure of a database.
- **Query Plan Diagram**: A diagram used to visualize the execution plan of a query.

### Case Studies

---

- **E-commerce Website**: A database management system was used to manage the e-commerce website's customer database, order database, and product database.
- **Social Media Platform**: A database management system was used to manage the social media platform's user database, post database, and comment database.

### Applications

---

- **Customer Relationship Management (CRM)**: A database management system was used to manage customer data, orders, and sales.
- **E-commerce Platform**: A database management system was used to manage product data, orders, and inventory.
- **Social Media Platform**: A database management system was used to manage user data, posts, and comments.
