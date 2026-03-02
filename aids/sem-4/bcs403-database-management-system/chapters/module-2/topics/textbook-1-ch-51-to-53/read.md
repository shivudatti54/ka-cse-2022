# Database Management System

## Module: Textbook 1, Ch 5.1 to 5.3

### Study Material

#### 5.1: Introduction to Database Management System

### Overview

A Database Management System (DBMS) is a software system that allows you to define, create, maintain, and manipulate databases. It is a crucial component of any organization that deals with large amounts of data.

### Key Concepts

- **Database**: A collection of organized data stored in a way that allows for efficient retrieval and manipulation.
- **Database Management System (DBMS)**: A software system that manages a database.
- **Database Administrator (DBA)**: A person responsible for the maintenance and administration of a database.

#### 5.2: Types of Databases

### Overview

There are several types of databases, including:

### Key Concepts

- **Relational Database**: A database that stores data in the form of tables with well-defined relationships between them.
- **Object-Oriented Database**: A database that stores data as objects and uses inheritance and polymorphism to define relationships between them.
- **Hierarchical Database**: A database that stores data in a hierarchical structure, with each record having a unique identifier.
- **Network Database**: A database that stores data in a network of records linked together.

#### 5.3: Database Design

### Overview

Database design is the process of creating a database schema to organize the data in a logical and efficient way.

### Key Concepts

- **Entity Relationship Diagram (ERD)**: A visual representation of the relationships between entities in a database.
- **Entity**: A thing or concept that has attributes or properties.
- **Attribute**: A characteristic or feature of an entity.
- **Relationship**: The connection between two or more entities.

### Example

Suppose we want to design a database to store information about customers. We can create an ERD to represent the entities and their relationships.

| Entity   | Attributes                               |
| -------- | ---------------------------------------- |
| Customer | Customer ID, Name, Address, Phone Number |
| Order    | Order ID, Customer ID, Order Date        |
| Product  | Product ID, Name, Price                  |

The relationships between these entities can be represented as follows:

- A customer can have many orders (one-to-many).
- An order is associated with one customer (many-to-one).
- A product can be part of many orders (one-to-many).

By creating an ERD, we can ensure that our database design is logical and efficient.

### Key Takeaways

- A DBMS is a software system that manages a database.
- There are several types of databases, including relational, object-oriented, hierarchical, and network databases.
- Database design is the process of creating a database schema to organize data logically and efficiently.
- Entity Relationship Diagrams (ERDs) are used to represent the relationships between entities in a database.
