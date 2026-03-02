# Introduction to Database Management System

## Introduction

Database Management System (DBMS) is a software system that enables users to define, create, maintain, and control access to databases. It serves as an interface between the database and end-users or application programs, ensuring that data is organized, stored, and retrieved efficiently. The concept of DBMS emerged in the 1960s as a solution to the limitations of traditional file processing systems, where data was stored in separate files with no standardized method of access or management.

In today's digital world, DBMS plays a crucial role in virtually every organization. From banking transactions and airline reservations to social media platforms and e-commerce websites, database systems form the backbone of modern information systems. The ability to efficiently manage large volumes of data while ensuring data integrity, security, and concurrent access has made DBMS an indispensable tool for businesses and institutions. For Computer Science and Engineering students at university, understanding DBMS fundamentals is essential as it forms the foundation for advanced database technologies and prepares students for real-world software development challenges.

The study of DBMS encompasses various aspects including data modeling, database design, query processing, transaction management, and database administration. This introductory module aims to establish a strong conceptual foundation by exploring the basic terminology, architecture, and characteristics of database systems. By the end of this module, students will have a clear understanding of why database systems are preferred over traditional file systems and how they address the inherent limitations of data management.

## Key Concepts

### Data vs Information

Understanding the distinction between data and information is fundamental to database management. **Data** refers to raw, unprocessed facts and figures that exist in their elementary form. For example, numbers like "15000", "John", "1995-08-15" are data items. On the other hand, **information** is processed, organized, and meaningful data that provides value and context. When "15000" is identified as an employee's salary, "John" as an employee's name, and "1995-08-15" as the date of birth, these become information because they convey meaning.

The transformation from data to information involves processing, organizing, and presenting data in a meaningful context. This transformation is one of the primary functions of a DBMS, where queries and operations are used to extract meaningful information from raw data stored in the database.

### Need for DBMS

Traditional file processing systems suffered from numerous problems that led to the development of DBMS:

**Data Redundancy and Inconsistency**: In file systems, the same data might be stored in multiple files, leading to redundancy. When updates are made to one file but not others, data inconsistency occurs, resulting in conflicting information.

**Difficulty in Data Access**: File systems require users to write specific programs for each data retrieval task. There is no standardized query language to access data flexibly.

**Data Isolation**: Because data is scattered across various files with different formats, writing new applications to retrieve appropriate data is complex and time-consuming.

**Integrity Problems**: Maintaining data integrity constraints (such as an employee's department number must exist in the department table) requires embedding rules in application programs, which is difficult and error-prone.

**Atomicity Issues**: Transactions in file systems may fail partially, leaving the database in an inconsistent state. For example, in a fund transfer, if the debit succeeds but credit fails, money is lost.

**Security Problems**: File systems lack flexible security mechanisms. Implementing access controls requires significant programming effort.

### Characteristics of DBMS

A DBMS exhibits several important characteristics that distinguish it from file processing systems:

**Data Abstraction**: DBMS provides multiple levels of data abstraction—physical level (how data is actually stored), logical level (what data is stored and relationships), and view level (different perspectives for different users).

**Data Independence**: The ability to change the schema at one level without affecting the schema at the next higher level. Physical data independence allows changes to the physical storage without affecting the logical structure, while logical data independence allows changes to the logical schema without affecting application programs.

**Efficient Data Access**: DBMS employs sophisticated techniques like indexing, hashing, and query optimization to ensure efficient data retrieval and manipulation.

**Data Integrity and Security**: DBMS enforces integrity constraints and provides security mechanisms to protect sensitive data from unauthorized access.

**Concurrent Access**: DBMS supports multiple users accessing the database simultaneously through sophisticated concurrency control mechanisms.

**Recovery and Backup**: DBMS provides facilities for backing up data and recovering from failures, ensuring data is not lost.

### Database Users

DBMS serves different types of users with varying technical expertise:

**Database Administrators (DBA)**: Responsible for overall management of the database system, including security, backup, recovery, and performance tuning.

**Database Designers**: Design the logical and physical structure of the database, defining tables, relationships, and constraints.

**Application Developers**: Write programs that interact with the database to perform specific business functions.

**End Users**: Interact with the database through applications or query tools to retrieve and manipulate data.

### ANSI/SPARC Architecture

The American National Standards Institute/Standards Planning and Requirements Committee (ANSI/SPARC) proposed a three-level architecture for database systems:

**External Level (User Level)**: This is the highest level, representing individual user views. Each user sees a customized view of the database that includes only the data relevant to their needs. Multiple external schemas can exist for different users.

**Conceptual Level (Logical Level)**: This represents the entire database from a community user perspective. It describes what data is stored in the database and the relationships among data elements. The conceptual schema is the logical structure of the entire database, independent of any physical storage considerations.

**Internal Level (Physical Level)**: This is the lowest level, describing how data is physically stored on storage devices. It includes details about file organization, indexing, data compression, and encryption.

Mappings exist between each pair of adjacent levels to transform requests and data between levels.

### Types of Database Systems

**Based on Number of Users**: Single-user databases (used by one person) versus multi-user databases (support multiple concurrent users).

**Based on Distribution**: Centralized databases (stored at a single location) versus distributed databases (data stored across multiple locations, potentially connected via a network).

**Based on Data Model**: Relational databases (organize data in tables), Object-oriented databases (organize data as objects), NoSQL databases (flexible, schema-less databases for big data applications).

**Based on Purpose**: General-purpose databases (designed for various applications) versus Special-purpose databases (designed for specific applications like data warehouses, real-time databases).

### Data Models

A data model is a collection of concepts that describe the structure of a database. It provides the necessary abstraction to represent real-world data. Common data models include:

**Hierarchical Model**: Organizes data in a tree-like structure with parent-child relationships. Used in early mainframe database systems.

**Network Model**: Extends hierarchical model by allowing many-to-many relationships. Data is organized as a graph.

**Relational Model**: Represents data as tables (relations) with rows and columns. The most widely used model in modern DBMS.

**Entity-Relationship (ER) Model**: A conceptual data model that represents data as entities, attributes, and relationships. Used for database design.

**Object-Oriented Model**: Represents data as objects with attributes and methods, incorporating object-oriented programming concepts.

## Examples

### Example 1: File Processing vs DBMS Problem

Consider a university information system managing student records:

**Scenario in File Processing**: Student information is stored in multiple files: STUDENT.dat (containing student details), COURSE.dat (containing course information), and ENROLLMENT.dat (containing enrollment records). If a student changes their phone number, this change must be made in STUDENT.dat. However, the same student record might also exist in ENROLLMENT.dat for tracking purposes. Updating only one file leads to data inconsistency.

**Solution with DBMS**: Using a DBMS like MySQL or PostgreSQL, all this information would be stored in related tables. When a student's phone number changes, only one update operation is required, and the DBMS ensures all related records reflect this change through referential integrity constraints. The database administrator can define such constraints once, and the DBMS automatically enforces them.

### Example 2: Query Processing in DBMS

Consider retrieving all students who have scored above 90 marks in Database Management System:

**Without DBMS (File Processing)**: The programmer would need to:

1. Open the student marks file
2. Read each record sequentially
3. Check if the Database Management System marks are greater than 90
4. Print or store matching records
5. Handle file operations, error checking, and memory management manually

**With DBMS (Using SQL)**: The user simply writes:

```sql
SELECT student_name, marks
FROM Students
WHERE subject = 'DBMS' AND marks > 90;
```

The DBMS handles all the underlying complexity—reading files, applying indexes for optimization, filtering records, and presenting results. The user focuses on what data is needed, not how to retrieve it.

### Example 3: Concurrent Access Scenario

In a banking system, two customers simultaneously try to withdraw money from the same account:

**Without DBMS**: If Customer A withdraws Rs. 5000 and Customer B withdraws Rs. 3000 at exactly the same time, both might read the balance as Rs. 10,000. After both transactions, the balance might become Rs. 5000 (if A writes last) or Rs. 7000 (if B writes last), instead of the correct Rs. 2000. This is called a "lost update" problem.

**With DBMS**: The DBMS implements concurrency control using techniques like locking. When Customer A starts a withdrawal, the DBMS locks that account record. When Customer B attempts the withdrawal, the DBMS waits until Customer A's transaction completes. This ensures serializability—equivalent to executing transactions one after another—maintaining data consistency.

## Exam Tips

1. **Know the Difference**: Clearly distinguish between data and information—data is raw facts, information is processed meaningful data. This is a frequently asked question in university exams.

2. **File System vs DBMS**: Memorize at least 5 problems of file processing systems—data redundancy, data isolation, integrity problems, atomicity issues, and security problems. This is a crucial comparison.

3. **ANSI/SPARC Architecture**: Remember the three levels—External, Conceptual, and Internal—and understand what each level represents. Be prepared to draw a diagram if required.

4. **Data Independence**: Understand the difference between physical and logical data independence. Physical independence means changes in storage don't affect the logical schema; logical independence means changes in logical schema don't affect application programs.

5. **Characteristics of DBMS**: Study all 6-7 characteristics thoroughly—data abstraction, data independence, efficient data access, data integrity and security, concurrent access, and recovery and backup.

6. **Data Models**: Know the basic data models—hierarchical, network, relational, ER, and object-oriented. The relational model is the most important.

7. **Database Users**: Remember the four types of database users—DBA, database designers, application developers, and end users—and their responsibilities.

8. **SQL**: Although this is an introductory module, understanding that SQL (Structured Query Language) is the standard language for interacting with relational databases provides context for future modules.

9. **ACID Properties**: Remember the four properties of transactions—Atomicity (all or nothing), Consistency (valid state to valid state), Isolation (concurrent transactions appear sequential), and Durability (committed data is permanent).

10. **Draw Diagrams**: Practice drawing the ANSI/SPARC architecture diagram and understanding data flow between levels. Diagrams are often asked in exams.
