# **Three Schema Architecture and Data Independence**

### Overview

Three Schema Architecture is a database design approach that separates data into three distinct schemes: conceptual, logical, and physical. This architecture provides data independence, allowing changes to be made to the data without affecting the underlying database structure.

### Three Schemas

- **Conceptual Schema**: The highest level of abstraction, representing the data entities and their relationships in a conceptual manner. It is created by the end-user and is typically represented using entity-relationship diagrams (ERDs).
- **Logical Schema**: A representation of the conceptual schema, but with a more formal and structured approach. It includes tables, fields, and relationships, and is typically represented using a relational schema diagram.
- **Physical Schema**: The lowest level of abstraction, representing the actual storage and retrieval of data in the database. It includes the database's layout, including the physical storage of tables and data.

### Data Independence

Data independence is the ability of a database to change without affecting the application that uses it. There are three types of data independence:

- **Horizontal Data Independence**: The ability to change the physical storage of data without affecting the logical schema.
- **Vertical Data Independence**: The ability to change the logical schema without affecting the physical schema.
- **Conceptual Data Independence**: The ability to change the conceptual schema without affecting the logical or physical schema.

### Database Languages and Interfaces

#### Database Languages

Database languages are used to interact with a database. Common database languages include:

- **SQL (Structured Query Language)**: A standard language for managing relational databases.
- **Procedural Languages**: Languages like PL/SQL and T-SQL that allow for stored procedures and functions.
- **Object-Oriented Languages**: Languages like Java and C# that allow for object-oriented database design.

#### Database Interfaces

Database interfaces are used to interact with a database. Common database interfaces include:

- **Command-Line Interfaces (CLI)**: Text-based interfaces like SQL\*Plus and MySQL Command Line Tool.
- **Graphical User Interfaces (GUI)**: Visual interfaces like Oracle Enterprise Manager and Microsoft SQL Server Management Studio.
- **APIs (Application Programming Interfaces)**: Programming interfaces like ODBC and JDBC that allow applications to interact with a database.

### The Database System Environment

The database system environment includes the physical storage devices, operating systems, and hardware required to support the database.

- **Storage Devices**: Disk drives, tape drives, and solid-state drives used to store database data.
- **Operating Systems**: Unix, Linux, and Windows operating systems used to manage and interact with the database.
- **Hardware**: CPU, memory, and network hardware required to support the database.

### Key Concepts

- **Normalization**: The process of organizing data to minimize data redundancy and improve data integrity.
- **Denormalization**: The process of organizing data to improve performance and reduce complexity.
- **Data Consistency**: The ability of a database to ensure data integrity and consistency.
- **Data Security**: The ability of a database to protect data from unauthorized access and modification.

### Case Study

Suppose we are designing a database for an e-commerce company. We need to create a conceptual schema, logical schema, and physical schema for the database. We can use the three-schema architecture to separate the data into three distinct schemes. The conceptual schema can include entities such as customers, orders, and products. The logical schema can include tables and fields that represent the data entities. The physical schema can include the actual storage and retrieval of data in the database.

### Summary

The three-schema architecture is a database design approach that provides data independence, allowing changes to be made to the data without affecting the underlying database structure. The conceptual schema, logical schema, and physical schema are used to separate the data into three distinct schemes. Database languages and interfaces are used to interact with a database. The database system environment includes the physical storage devices, operating systems, and hardware required to support the database.
