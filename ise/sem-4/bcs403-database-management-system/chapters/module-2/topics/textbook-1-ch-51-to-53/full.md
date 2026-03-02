# **DATABASE MANAGEMENT SYSTEM**

## **Module: No. of Hours: 8**

## **Topic: Textbook 1: Ch 5.1 to 5.3**

## **Introduction**

Database management systems (DBMS) are software programs that allow us to define, create, maintain, and manipulate databases. In this module, we will explore the fundamental concepts of DBMS, including data modeling, database design, and database implementation.

## **Chapter 5.1: Data Modeling**

Data modeling is the process of creating a conceptual representation of the data that will be stored in a database. It involves identifying the entities, attributes, and relationships between them.

### Types of Data Models

There are several types of data models, including:

- **Entity-Relationship Model (ERM)**: This is the most common data model, which represents data as entities and their relationships using entities, attributes, and relationships.
- **Object-Oriented Model**: This model represents data as objects and their interactions using classes, objects, and attributes.
- **Hierarchical Model**: This model represents data as a hierarchy of entities, with each entity having a parent-child relationship.

### Data Modeling Techniques

There are several data modeling techniques, including:

- **Entity-relationship diagram (ERD)**: This is a visual representation of the data model, which shows the entities, attributes, and relationships between them.
- **Data flow diagram (DFD)**: This is a visual representation of the data flow between different processes and entities.
- **Business process model**: This is a visual representation of the business processes and their relationships.

**Example:**
Suppose we want to create a database to manage customer information. We can use the entity-relationship model to define the entities and attributes as follows:

| Entity   | Attribute                                |
| -------- | ---------------------------------------- |
| Customer | Customer ID, Name, Address, Phone Number |
| Order    | Order ID, Customer ID, Order Date, Total |

## **Chapter 5.2: Database Design**

Database design is the process of creating a logical representation of the database, including the relationships between tables and the data types of the attributes.

### Types of Database Designs

There are several types of database designs, including:

- **First Normal Form (1NF)**: This is a design where each table has a unique combination of attributes, with no repeating groups.
- **Second Normal Form (2NF)**: This is a design where each non-key attribute depends on the entire primary key.
- **Third Normal Form (3NF)**: This is a design where each non-key attribute depends on the entire primary key, and there are no transitive dependencies.

### Database Design Tools

There are several database design tools, including:

- **ERWin**: This is a commercial database design tool that supports various database management systems.
- **DBDesigner**: This is a free and open-source database design tool that supports MySQL and PostgreSQL.
- **Microsoft Visio**: This is a commercial database design tool that supports various database management systems.

**Example:**
Suppose we want to design a database to manage employee information. We can use the third normal form (3NF) design to create the following tables:

| Table               | Attribute                     | Data Type        |
| ------------------- | ----------------------------- | ---------------- |
| Employees           | Employee ID, Name, Department | varchar, varchar |
| Departments         | Department ID, Name           | varchar, varchar |
| Employee_Dependents | Employee ID, Dependent Name   | int, varchar     |

## **Chapter 5.3: Database Implementation**

Database implementation is the process of creating the physical database, including the storage and retrieval of data.

### Types of Database Management Systems

There are several types of database management systems, including:

- **Relational databases**: These are databases that use the relational model, which stores data in tables with relationships between them.
- **Object-oriented databases**: These are databases that use the object-oriented model, which stores data as objects and their interactions.
- **NoSQL databases**: These are databases that do not use the traditional relational model, which stores data in a variety of formats.

### Database Implementation Tools

There are several database implementation tools, including:

- **MySQL**: This is a popular open-source relational database management system.
- **PostgreSQL**: This is a popular open-source relational database management system.
- **MongoDB**: This is a popular NoSQL database management system.

**Example:**
Suppose we want to implement a database to manage customer information. We can use a relational database management system such as MySQL to create the following tables:

| Table     | Attribute                                | Data Type                      |
| --------- | ---------------------------------------- | ------------------------------ |
| Customers | Customer ID, Name, Address, Phone Number | int, varchar, varchar, varchar |
| Orders    | Order ID, Customer ID, Order Date, Total | int, int, date, decimal        |

## **Conclusion**

In this module, we have explored the fundamental concepts of database management systems, including data modeling, database design, and database implementation. We have discussed the types of data models, data modeling techniques, and database design tools. We have also explored the types of database management systems and database implementation tools.

## **Further Reading**

- **"Database Systems: The Complete Book"** by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- **"Database Systems: Design, Implementation, and Management"** by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- **"Introduction to Database Systems"** by Abraham Silberschatz, Henry F. Korth, and S. Sudarshan
- **"Database Management Systems"** by Raghu Ramakrishnan and Johannes Gehrke

## **Diagrams Descriptions**

- **Entity-Relationship Diagram (ERD)**: A visual representation of the data model, which shows the entities, attributes, and relationships between them.
- **Data Flow Diagram (DFD)**: A visual representation of the data flow between different processes and entities.
- **Business Process Model**: A visual representation of the business processes and their relationships.

## **Case Studies**

- **Case Study 1:** A company wants to create a database to manage customer information. The company uses the entity-relationship model to define the entities and attributes, and implements the database using a relational database management system.
- **Case Study 2:** A university wants to create a database to manage student information. The university uses the object-oriented model to define the objects and their interactions, and implements the database using a NoSQL database management system.
