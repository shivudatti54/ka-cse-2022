# **DATABASE MANAGEMENT SYSTEM**

## **Module: Textbook 1, Ch 5.1 to 5.3**

## **Table of Contents**

1. [5.1: Database Concepts](#5.1-database-concepts)
2. [5.2: Database Types](#5.2-database-types)
3. [5.3: Database Normalization](#5.3-database-normalization)

## **5.1: Database Concepts**

### Definition

A database is a collection of organized data that is stored in a way that allows for efficient retrieval and manipulation.

### Key Concepts

- **Database Management System (DBMS):** A software system that allows users to create, maintain, and manipulate databases.
- **Database Schema:** The overall structure of a database, including the relationships between different tables.
- **Data Types:** The categories into which data is divided, such as integers, strings, and dates.
- **Database Entities:** The objects that are represented in a database, such as customers, orders, and products.

### Examples

- A university's database may include entities such as students, courses, and grades.
- A retail database may include entities such as customers, products, and orders.

## **5.2: Database Types**

### Definition

A database type refers to the way in which data is organized and stored.

### Types of Databases

- **Relational Database:** A database that stores data in tables with defined relationships between them. (e.g., MySQL, Microsoft SQL Server)
- **NoSQL Database:** A database that stores data in a variety of formats, such as key-value pairs, documents, or graphs. (e.g., MongoDB, Cassandra)
- **Object-Oriented Database:** A database that stores data in the form of objects, which are instances of classes. (e.g., ObjectDB, Gemstone)

### Benefits of Different Database Types

- **Relational Databases:**
  - Well-established and widely supported
  - Support complex transactions and relationships between tables
  - Scalable and performant
- **NoSQL Databases:**
  - Highly scalable and performant
  - Support flexible schema and high volumes of data
  - Suitable for big data and real-time applications
- **Object-Oriented Databases:**
  - Support complex business logic and relationships between data
  - Handle large amounts of unstructured data
  - Suitable for applications with complex transactions and relationships

### Examples

- A relational database may be used for a company's employee database, which includes entities such as employees, departments, and job titles.
- A NoSQL database may be used for a social media platform, which stores data in the form of key-value pairs, such as user IDs and profile information.

## **5.3: Database Normalization**

### Definition

Database normalization is the process of organizing data in a database to minimize data redundancy and improve data integrity.

### Normalization Rules

- **First Normal Form (1NF):** Each table cell must contain a single value, and each row must have a unique combination of values. (e.g., customers table with customer ID, name, and address)
- **Second Normal Form (2NF):** Each non-key attribute must depend on the entire primary key. (e.g., orders table with order ID, customer ID, and order date)
- **Third Normal Form (3NF):** If a table is in 2NF, and a non-key attribute depends on another non-key attribute, then it should be moved to a separate table. (e.g., orders table with order ID, customer ID, and order date, and separate tables for customers and dates)

### Benefits of Normalization

- **Reduced Data Redundancy:** Normalization eliminates duplicate data and reduces the need for data maintenance.
- **Improved Data Integrity:** Normalization ensures that data is consistent and accurate across the database.
- **Scalability:** Normalization makes it easier to add new data and relationships to the database.

### Examples

- A normalized database may include separate tables for customers, orders, and products, each with their own primary key and non-key attributes.
- A normalized database may include separate tables for departments, employees, and job titles, each with their own primary key and non-key attributes.

## **Key Concepts Summary**

- Database concepts, including DBMS, database schema, data types, and database entities
- Database types, including relational, NoSQL, and object-oriented databases
- Database normalization, including 1NF, 2NF, and 3NF rules
- Benefits of normalization, including reduced data redundancy, improved data integrity, and scalability
