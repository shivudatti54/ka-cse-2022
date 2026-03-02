# Three Schema Architecture and Data Independence

=====================================================

## Introduction

---

The three-schema architecture is a fundamental concept in database systems that separates the conceptual, logical, and physical schemas of a database. This separation allows for data independence, which is a crucial aspect of database design.

## Three Schema Architecture

---

### Conceptual Schema

- Definition: The conceptual schema represents the overall structure and organization of the data in a database.
- Characteristics:
  - High-level representation of the data
  - Focuses on data entities and relationships
  - Used for data modeling and conceptual design
- Example:
  - A database that stores information about customers, orders, and products can have a conceptual schema that includes entities such as Customer, Order, and Product.

### Logical Schema

- Definition: The logical schema represents the internal structure and organization of the data in a database.
- Characteristics:
  - Mid-level representation of the data
  - Focuses on data relationships and dependencies
  - Used for logical design and schema translation
- Example:
  - The conceptual schema of the previous example can be translated into a logical schema that includes tables such as Customers, Orders, and Products.

### Physical Schema

- Definition: The physical schema represents the actual storage and organization of the data in a database.
- Characteristics:
  - Low-level representation of the data
  - Focuses on data storage and retrieval
  - Used for physical design and database implementation
- Example:
  - The logical schema of the previous example can be translated into a physical schema that includes tables, indexes, and storage devices.

## Data Independence

---

Data independence is the ability of a database to change without affecting other parts of the system. There are several types of data independence, including:

### Horizontal Data Independence

- Definition: Horizontal data independence refers to the ability of a database to change the physical storage of data without affecting the logical structure.
- Characteristics:
  - Data is stored in different locations without changing the logical schema
  - Allows for changes in hardware or storage devices
- Example:
  - A database that stores customer information in one table can be changed to store the same information in multiple tables without affecting the logical schema.

### Vertical Data Independence

- Definition: Vertical data independence refers to the ability of a database to change the logical structure of data without affecting the physical storage.
- Characteristics:
  - Relationships between data are changed without altering the physical storage
  - Allows for changes in data relationships or dependencies
- Example:
  - A database that stores customer information in one table can change the relationships between the data without affecting the physical storage.

## Database Languages and Interfaces

---

Database languages and interfaces are used to interact with a database and manage its data.

### Database Languages

- Definition: Database languages are used to define and manipulate database schema, data, and relationships.
- Characteristics:
  - Used to create, modify, and delete database schema
  - Used to insert, update, and delete data
  - Used to retrieve and manipulate data
- Examples:
  - SQL (Structured Query Language)
  - Oracle SQL
  - MySQL

### Database Interfaces

- Definition: Database interfaces are used to interact with a database and manage its data.
- Characteristics:
  - Used to connect to a database and execute queries
  - Used to retrieve and manipulate data
  - Used to manage database schema
- Examples:
  - JDBC (Java Database Connectivity)
  - ODBC (Open Database Connectivity)
  - ADO.NET (ActiveX Data Objects .NET)

## The Database System Environment

---

The database system environment refers to the overall system that supports database operations.

### Components of the Database System Environment

- Definition: The database system environment consists of hardware, software, and human factors that support database operations.
- Characteristics:
  - Hardware: Servers, storage devices, and networks
  - Software: Database management systems, database languages, and interfaces
  - Human factors: Users, administrators, and database designers
- Example:
  - A database system that includes a server, storage devices, and a database management system can be considered part of the database system environment.

# Key Concepts

---

- Three-schema architecture
- Data independence
- Database languages
- Database interfaces
- Database system environment
- Horizontal data independence
- Vertical data independence
