# **DATABASE MANAGEMENT SYSTEM**

**Module:** No. of Hours: 8
**Topic:** Three schema architecture and data independence, database languages, and interfaces, The Database System environment

## **Table of Contents**

1. [Introduction](#introduction)
2. [Historical Context](#historical-context)
3. [Three Schema Architecture](#three-schema-architecture)
   - [First-Generation Schema](#first-generation-schema)
   - [Second-Generation Schema](#second-generation-schema)
   - [Third-Generation Schema](#third-generation-schema)
4. [Data Independence](#data-independence)
5. [Database Languages](#database-languages)
   - [Structured Query Language (SQL)](#structured-query-language-sql)
   - [Other Database Languages](#other-database-languages)
6. [Database Interfaces](#database-interfaces)
   - [Direct-Access Method](#direct-access-method)
   - [Networked-Access Method](#networked-access-method)
7. [The Database System Environment](#the-database-system-environment)
   - [Components of a Database System](#components-of-a-database-system)
   - [Database Management System (DBMS)](#database-management-system-dbms)
8. [Case Studies and Applications](#case-studies-and-applications)
9. [Conclusion](#conclusion)
10. [Further Reading](#further-reading)

## **Introduction**

A database management system (DBMS) is a software application that enables organizations to store, manage, and retrieve data in a controlled, efficient, and secure manner. The DBMS acts as an intermediary between the user and the physical data storage devices, providing a layer of abstraction and facilitating data independence.

The development of DBMS has a rich history, dating back to the 1960s. The first generation of DBMS was characterized by direct-access methods, which relied on physical storage devices. The second generation introduced networked-access methods, which enabled multiple users to access the same data. The third generation marked a significant milestone, introducing three-schema architecture, data independence, and advanced database languages.

## **Historical Context**

The development of DBMS was influenced by several factors, including:

1. **Computing Technology**: The advent of computers in the 1950s and 1960s led to the development of data processing systems.
2. **Administrative Needs**: As organizations grew, the need for efficient data management and retrieval became increasingly important.
3. **Research and Development**: Researchers and developers sought to create systems that could handle large volumes of data and provide flexible data management capabilities.

## **Three Schema Architecture**

The three-schema architecture is a fundamental concept in DBMS design. It consists of three interconnected schemas:

### First-Generation Schema

The first-generation schema, also known as the physical schema, was the first to be developed. It consisted of a single, physical schema that reflected the organization's data storage structure.

Diagram: Physical Schema

```markdown
+---------------+
| Data Storage |
+---------------+
|
|
v
+---------------+
| First-Generation |
| Schema |
+---------------+
```

### Second-Generation Schema

The second-generation schema, also known as the logical schema, was introduced in the 1970s. It provided a higher level of abstraction, separating the data storage structure from the data definition.

Diagram: Logical Schema

```markdown
+---------------+
| Data Definition |
+---------------+
|
|
v
+---------------+
| Second-Generation |
| Schema |
+---------------+
|
|
v
+---------------+
| Physical Schema |
+---------------+
```

### Third-Generation Schema

The third-generation schema, also known as the conceptual schema, is the most advanced schema. It provides a high level of abstraction, separating the conceptual data structure from the physical storage structure.

Diagram: Conceptual Schema

```markdown
+---------------+
| Business Logic |
+---------------+
|
|
v
+---------------+
| Third-Generation |
| Schema |
+---------------+
|
|
v
+---------------+
| Logical Schema |
+---------------+
|
|
v
+---------------+
| Physical Schema |
+---------------+
```

## **Data Independence**

Data independence is a fundamental concept in DBMS design. It refers to the ability of a DBMS to provide a level of abstraction, allowing users to modify the data storage structure without affecting the application.

Types of Data Independence:

1. **Physical Data Independence**: The ability to modify the physical storage structure without affecting the application.
2. **Logical Data Independence**: The ability to modify the logical structure of the data without affecting the application.
3. **Conceptual Data Independence**: The ability to modify the conceptual structure of the data without affecting the application.

## **Database Languages**

Database languages are used to interact with a DBMS. The most widely used database language is Structured Query Language (SQL).

### Structured Query Language (SQL)

SQL is a declarative language, meaning that it specifies what data to retrieve, rather than how to retrieve it.

Example:

```sql
SELECT * FROM customers WHERE country='USA';
```

### Other Database Languages

Other database languages include:

1. **Procedural Languages**: These languages, such as PL/SQL and T-SQL, are used to create stored procedures and functions.
2. **Object-Oriented Languages**: These languages, such as Java and Python, are used to create objects and classes.

## **Database Interfaces**

Database interfaces are used to interact with a DBMS. There are two main types of database interfaces:

### Direct-Access Method

The direct-access method involves direct access to the physical storage devices.

Example:

```markdown
+---------------+
| Application |
+---------------+
|
|
v
+---------------+
| Direct-Access |
| Method |
+---------------+
|
|
v
+---------------+
| Physical Storage |
+---------------+
```

### Networked-Access Method

The networked-access method involves accessing the DBMS through a network.

Example:

```markdown
+---------------+
| Application |
+---------------+
|
|
v
+---------------+
| Networked-Access |
| Method |
+---------------+
|
|
v
+---------------+
| DBMS |
+---------------+
|
|
v
+---------------+
| Physical Storage |
+---------------+
```

## **The Database System Environment**

A database system environment consists of several components:

### Components of a Database System

1. **Hardware**: The physical devices used to store and retrieve data.
2. **Software**: The DBMS and database languages.
3. **Data**: The actual data stored in the database.

### Database Management System (DBMS)

A DBMS is a software application that enables organizations to store, manage, and retrieve data.

Example:

```markdown
+---------------+
| DBMS |
+---------------+
|
|
v
+---------------+
| Database |
+---------------+
|
|
v
+---------------+
| Data |
+---------------+
```

## **Case Studies and Applications**

DBMS has numerous applications in various industries, including:

1. **Finance**: Banking and financial institutions use DBMS to manage customer data and transactions.
2. **Healthcare**: Hospitals and medical institutions use DBMS to manage patient data and medical records.
3. **E-commerce**: Online retailers use DBMS to manage customer data and inventory.

Example:

```markdown
+---------------+
| E-commerce |
| Platform |
+---------------+
|
|
v
+---------------+
| DBMS |
+---------------+
|
|
v
+---------------+
| Customer Data |
| Inventory |
+---------------+
```

## **Conclusion**

In conclusion, the development of DBMS has a rich history, with significant milestones in the three-schema architecture, data independence, and advanced database languages. DBMS has numerous applications in various industries, and continues to evolve with modern developments.

## **Further Reading**

1. **"Database Systems: The Complete Book"** by Hector Garcia-Molina, Juan Perez, and Jose Valenza
2. **"Database Systems: Design, Implementation, and Management"** by Edgar F. Codd
3. **"Introduction to Database Systems"** by Hector Garcia-Molina and Juan Perez
