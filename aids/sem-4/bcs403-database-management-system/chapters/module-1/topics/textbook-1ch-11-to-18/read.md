# **Database Management System Study Material**

**Module:** 8 hours
**Topic:** Textbook 1: Ch 1.1 to 1.8

## **What is a Database?**

### Definition

A database is a collection of organized data that is stored in a way that allows for efficient retrieval and manipulation. It is a repository of data that is used to support the operations of an organization or application.

### Types of Databases

- Relational databases: store data in tables with defined relationships between them
- Non-relational databases: store data in a flexible, schema-less format
- Hierarchical databases: store data in a tree-like structure
- Network databases: store data in a network-like structure

## **Characteristics of a Database**

### Properties

- **Data independence**: a database is independent of the hardware and software it runs on
- **Autonomy**: a database operates independently of other applications
- **Active view**: a database maintains a view of its own schema and data
- **Stockage**: a database stores data in a physical medium such as disk storage

### Functions

- **Data storage**: a database stores data in a structured format
- **Data retrieval**: a database retrieves data from storage
- **Data manipulation**: a database updates, inserts, or deletes data
- **Data control**: a database controls access to its data and schema

## **Database Management System**

### Definition

A database management system (DBMS) is a software system that manages a database. It provides a layer of abstraction between the user and the database, allowing users to interact with the database using a high-level interface.

### Components of a DBMS

- **Database**: the collection of data and schema
- **Database management system**: the software that manages the database
- **User**: the person who interacts with the database

## **DBMS Functions**

### Types of DBMS Functions

- **Data definition**: creates, modifies, and drops database objects
- **Data control**: manages access to database objects
- **Data manipulation**: updates, inserts, or deletes data
- **Data retrieval**: retrieves data from the database
- **Transaction management**: manages the execution of multiple operations as a single, atomic unit

## **Key Concepts**

- **Schema**: the structure of a database
- **Database object**: a component of a database such as a table or view
- **Database relationship**: a link between two or more database objects
- **Database query**: a request to retrieve data from the database
- **Database index**: a data structure that improves query performance

**Example:**

```markdown
# Creating a Database Schema

CREATE TABLE customers (
id INT PRIMARY KEY,
name VARCHAR(255),
email VARCHAR(255)
);

# Creating a Database Object

CREATE VIEW customer_details AS
SELECT c.name, c.email, o.order_total
FROM customers c
JOIN orders o ON c.id = o.customer_id;

# Database Relationship

CREATE TABLE orders (
id INT PRIMARY KEY,
customer_id INT,
FOREIGN KEY (customer_id) REFERENCES customers(id)
);

# Database Query

SELECT \* FROM customers WHERE email LIKE '%@example.com';
```

This example demonstrates the creation of a database schema, database object, and database relationship, as well as a database query.
