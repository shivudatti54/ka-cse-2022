# History of Database Applications

## Introduction

For  engineering students, understanding the evolution of Database Management Systems (DBMS) is crucial. It provides context for why modern systems are designed the way they are, highlighting the problems they solved and the limitations they overcame. This journey from manual files to sophisticated relational and NoSQL systems is a fascinating study in engineering innovation.

## The Era Before DBMS: File-Based Systems

Initially, data was stored in flat files, closely associated with specific application programs. This approach is often called the **File Processing System**.

*   **How it worked:** Each application, such as payroll, inventory, or student registration, had its own set of data files. The data structure (e.g., the order and type of fields in a record) was defined within the application program itself.
*   **Major Limitations:**
    *   **Data Redundancy and Inconsistency:** The same data (e.g., a student's address) could be stored in multiple files for different applications. This wasted storage space and, more critically, led to inconsistency. If the address was updated in the payroll file but not in the library file, the system had conflicting information.
    *   **Data Isolation:** Since data was scattered across various files in different formats, it was extremely difficult to write new applications to retrieve meaningful, combined information.
    *   **Data Dependency:** The application programs were dependent on the physical structure and storage format of the files. Any change to the data structure, like adding a new field (e.g., a student's mobile number), required modifying all programs that accessed that file—a maintenance nightmare.
    *   **Integrity and Atomicity Issues:** It was hard to enforce constraints (e.g., "account balance > 0"). Furthermore, ensuring that a transaction (like a fund transfer) either completes fully or not at all was the programmer's responsibility and very complex to implement.

**Example:** A `Student.exe` program managed `students.txt`, while a `Library.exe` program managed `books_issued.txt`. There was no direct link between a student and the books they borrowed without writing complex, custom code.

## The Evolution: The Database Era

The limitations of file systems led to the development of DBMS, which introduced the concept of data as a shared, integrated resource that could be managed independently of the applications.

### 1. Hierarchical Data Model (1960s-1970s)

This model organized data in a tree-like structure of parent-child relationships.

*   **Concept:** Each parent can have many children, but each child has only one parent. Data was accessed through navigational paths, moving from root to leaves.
*   **Example:** A `COLLEGE` record could be the root, with children `DEPARTMENT` records. Each `DEPARTMENT` could have children `STUDENT` and `PROFESSOR` records.
*   **Limitation:** Representing many-to-many relationships (e.g., one student taking multiple courses) was awkward and inefficient. The model was rigid and complex for ad-hoc queries.

### 2. Network Data Model (1970s)

An improvement on the hierarchical model, it allowed a more flexible graph structure.

*   **Concept:** Represented by the **CODASYL DBTG** model, it allowed a child record (called a *member*) to have more than one parent (called an *owner*). This made many-to-many relationships easier to model.
*   **Example:** A `STUDENT` record could be owned by both a `DEPARTMENT` record and a `COURSE` record.
*   **Limitation:** While more flexible, the system was still highly complex. Programmers had to navigate through the database using pointers, making applications complicated to write and maintain.

Both hierarchical and network models are known as **navigational databases** because programs "navigated" through the data using these paths and pointers.

### 3. The Relational Revolution (1970s-Present)

A seminal 1970 paper by **E.F. Codd** of IBM introduced the **Relational Data Model**, a fundamental shift in database philosophy. It separated the logical view of data from its physical storage.

*   **Core Concept:** Data is organized in simple, intuitive **tables (relations)** of rows and columns. Relationships between tables are represented not by physical pointers but by matching data values (e.g., a `dept_id` in a `Student` table matching an `id` in a `Department` table).
*   **Advantages:**
    *   **Data Independence:** The logical structure is independent of physical storage.
    *   **Simplicity:** The tabular structure is easy for users and developers to understand.
    *   **Powerful Querying:** The **Structured Query Language (SQL)** was developed to perform complex, declarative queries. Instead of saying *how* to get the data (navigate), you simply declare *what* data you want.
*   **Impact:** This model became the gold standard for decades. Systems like **Oracle, IBM DB2, Microsoft SQL Server, and MySQL** are all based on the relational model.

### 4. Object-Oriented and Object-Relational Models (1990s)

As programming languages became object-oriented (Java, C++), a mismatch arose between the object-based code and the relational tables. This "impedance mismatch" led to:

*   **Object-Oriented DBMS (OODBMS):** Stored data directly as objects, complete with methods and inheritance.
*   **Object-Relational DBMS (ORDBMS):** Extended relational databases to incorporate object-oriented concepts like user-defined types and inheritance. **PostgreSQL** is a prime example.

### 5. The NoSQL Movement (2000s-Present)

The rise of the internet and Big Data (characterized by Volume, Velocity, and Variety) exposed some limitations of rigid relational schemas for specific use cases.

*   **Concept:** "NoSQL" (Not Only SQL) encompasses a range of non-relational databases designed for scalability, flexibility, and specific data models.
*   **Types:** Key-Value stores (Redis), Document databases (MongoDB), Column-family stores (Cassandra), and Graph databases (Neo4j).

## Key Points & Summary

*   **The driving force** behind database evolution has been to achieve **data independence**, reduce **redundancy**, maintain **integrity**, and support **efficient querying**.
*   The journey moved from **application-specific file systems** to **centralized, shared database systems**.
*   Data models evolved from **navigational (Hierarchical/Network)** models to the highly influential **Relational model** and its declarative language, **SQL**.
*   Modern demands have led to the adoption of **Object-Oriented** and **NoSQL** databases to handle complex data types and massive scale, often used alongside traditional relational systems.
*   Understanding this history explains the "why" behind the core principles of DBMS you will study, such as ACID properties, normalization, and SQL.