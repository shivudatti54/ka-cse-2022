# Data Models and DBMS Architecture

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University

---

## 1. Introduction

### What is a Database Management System (DBMS)?

A **Database Management System (DBMS)** is specialized software that enables users to define, create, maintain, and control access to databases. It serves as an interface between the database and end-users or application programs, ensuring data is stored efficiently and can be retrieved reliably.

### Real-World Relevance

In today's digital age, virtually every application relies on databases. Consider these examples:

- **Banking Systems**: Banks store customer accounts, transactions, and loan details in databases. When you withdraw money from an ATM, the DBMS verifies your account balance, processes the transaction, and updates your account in real-time.
- **E-Commerce Platforms**: Amazon, Flipkart, and other online stores maintain massive databases of products, customers, orders, and inventory. Every search, cart addition, and purchase involves database operations.
- **Healthcare Systems**: Hospitals maintain patient records, appointment schedules, and medical histories in databases, enabling quick access to critical patient information.
- **Social Media**: Facebook, Instagram, and Twitter use databases to store billions of user profiles, posts, comments, and connections.

### Context: Delhi University NEP 2024 UGCF Syllabus

This topic forms a fundamental part of the Database Management Systems course under the NEP 2024 curriculum. Students must understand how data is structured, stored, and managed in modern database systems, with emphasis on different data models and the architectural framework that supports database operations.

---

## 2. DBMS Architecture

### 2.1 Three-Schema Architecture (Three-Level Architecture)

The three-schema architecture is a framework that describes database organization at three distinct levels. This architecture was proposed by the ANSI/SPARC (American National Standards Institute / Standards Planning and Requirements Committee) in 1975.

```
┌─────────────────────────────────────────────────────────────────┐
│                    THREE-SCHEMA ARCHITECTURE                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌───────────────┐     ┌───────────────┐     ┌────────────┐   │
│   │   EXTERNAL    │     │   CONCEPTUAL  │     │  INTERNAL  │   │
│   │    SCHEMA     │────▶│    SCHEMA     │────▶│   SCHEMA   │   │
│   │  (View Level) │     │ (Logical Level)│    │(Physical)  │   │
│   └───────────────┘     └───────────────┘     └────────────┘   │
│          ▲                      ▲                     ▲         │
│          │                      │                     │         │
│          └──────────────────────┴─────────────────────┘         │
│                          DBMS                                    │
└─────────────────────────────────────────────────────────────────┘
```

#### Level 1: External Schema (View Level)

- **Definition**: The highest level of abstraction, representing how individual users or user groups view the database.
- **Characteristics**:
  - Describes a portion of the database relevant to a particular user
  - Provides security by hiding sensitive data from unauthorized users
  - Multiple external schemas can exist for different users
  - Examples: A manager sees sales summaries; a clerk sees transaction details

**Example**: In a university database:
- **Professor's view**: Sees courses taught, student grades, and assignments
- **Student's view**: Sees own grades, course registration, and timetable
- **Admin's view**: Sees all financial and administrative data

#### Level 2: Conceptual Schema (Logical Level)

- **Definition**: The complete view of the entire database, representing all data and relationships without physical storage details.
- **Characteristics**:
  - Integrates all external views into a single global view
  - Describes what data is stored and the relationships among data
  - Independent of both physical storage and application programs
  - Maintained by database administrators (DBAs)

**Example**: The conceptual schema might define:
```
STUDENT(StudentID, Name, DOB, Address, Phone, Email)
COURSE(CourseID, CourseName, Credits, DepartmentID)
ENROLLMENT(StudentID, CourseID, Grade, Semester)
```

#### Level 3: Internal Schema (Physical Level)

- **Definition**: The lowest level of abstraction, describing how data is physically stored in the database.
- **Characteristics**:
  - Defines storage structures, indexing methods, data compression techniques
  - Deals with file organization, storage allocation, access paths
  - Highly dependent on hardware and DBMS implementation
  - Transparent to users and application programs

**Example**: The internal schema might specify:
- B+ tree indexing on StudentID
- Clustered index on CourseID
- Data compression using page-level encoding
- Storage in specific disk sectors

### 2.2 Data Independence

One of the primary benefits of the three-schema architecture is **data independence**—the ability to change the schema at one level without affecting the schema at the next higher level.

| Type | Description | Example |
|------|-------------|---------|
| **Logical Data Independence** | Changes to conceptual schema don't affect external schemas | Adding a new field to a table doesn't affect user views |
| **Physical Data Independence** | Changes to internal schema don't affect conceptual schema | Changing storage structure or indexing doesn't affect logical structure |

### 2.3 DBMS Components

A DBMS consists of several interconnected components that work together to manage data efficiently:

```
┌─────────────────────────────────────────────────────────────────┐
│                      DBMS COMPONENTS                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │   Query     │  │   Storage   │  │  Transaction│              │
│  │  Processor │  │  Manager    │  │   Manager   │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │   Data      │  │   Catalog   │  │    Data     │              │
│  │  Dictionary│  │  Manager    │  │  Integrity  │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐                               │
│  │   Backup &  │  │   Security  │                               │
│  │  Recovery   │  │   Manager   │                               │
│  └─────────────┘  └─────────────┘                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Component | Function |
|-----------|----------|
| **Query Processor** | Interprets and executes DML and DDL statements; optimizes query execution |
| **Storage Manager** | Handles physical storage of data, file management, and buffer management |
| **Transaction Manager** | Ensures ACID properties; handles concurrency control and recovery |
| **Data Dictionary** | Stores metadata about database structure, constraints, and schema |
| **Catalog Manager** | Manages information about database objects and their relationships |
| **Data Integrity Manager** | Enforces integrity constraints (primary key, foreign key, checks) |
| **Backup & Recovery Manager** | Performs regular backups and handles system failures |
| **Security Manager** | Implements authentication, authorization, and access control |

---

## 3. Data Models

A **data model** is a collection of concepts, rules, and notations that describe the logical structure of a database. It defines how data is organized, stored, and manipulated. Data models bridge the gap between real-world entities and their representation in a database.

### 3.1 Categories of Data Models

Data models are broadly categorized based on their level of abstraction:

```
┌─────────────────────────────────────────────────────────────────┐
│                    TYPES OF DATA MODELS                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              HIGH-LEVEL (CONCEPTUAL)                    │   │
│  │     Entity-Relationship (ER) Model, Object-Oriented      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                           ▲                                     │
│                           │                                     │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │            REPRESENTATIONAL (LOGICAL)                    │   │
│  │  Relational, Network, Hierarchical, Object-Relational   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                           ▲                                     │
│                           │                                     │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │               LOW-LEVEL (PHYSICAL)                        │   │
│  │     File-based, Index structures, Storage formats        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 3.2 File-Based Systems (Precursor to DBMS)

Before DBMS, file-based systems were used to store data. Each application program defined its own file structure and accessed data directly.

**Limitations of File-Based Systems**:
- **Data Redundancy**: Same data stored in multiple files
- **Data Inconsistency**: Updates may not reflect in all copies
- **Integrity Problems**: No automatic constraint enforcement
- **Security Issues**: Limited access control
- **Concurrent Access**: No built-in support for multi-user access

---

### 3.3 Hierarchical Data Model

The **hierarchical data model** organizes data in a tree-like structure with parent-child relationships. Each child has exactly one parent, but a parent can have multiple children.

**Key Concepts**:
- **Parent-Child Relationship (1:N)**: One parent can have many children
- **Root**: The top-level node with no parent
- **Segment**: The equivalent of a record type
- **Path**: The navigation path from root to any segment

**Example**: Organizational Structure

```
                           ┌─────────────┐
                           │  CEO (Root) │
                           └──────┬──────┘
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
            ┌───────────┐  ┌───────────┐  ┌───────────┐
            │  Finance  │  │   IT      │  │  Sales    │
            │  Manager  │  │  Manager  │  │  Manager  │
            └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
                  │              │              │
            ┌─────┴─────┐  ┌─────┴─────┐  ┌─────┴─────┐
            ▼           ▼  ▼           ▼  ▼           ▼
        [Employee]  [Employee]   [Employee]   [Employee]
```

**Example Code (IBM Information Management System - IMS)**:

```
DEFSEG NAME=DEPARTMENT, RANK=1
  FIELD NAME=DEPT_ID, POS=1, LENGTH=4
  FIELD NAME=DEPT_NAME, POS=5, LENGTH=30

DEFSEG NAME=EMPLOYEE, RANK=2, PARENT=DEPARTMENT
  FIELD NAME=EMP_ID, POS=1, LENGTH=6
  FIELD NAME=EMP_NAME, POS=7, LENGTH=30
  FIELD NAME=SALARY, POS=37, LENGTH=8
```

**Advantages**:
- Simple and intuitive structure
- Fast access due to predefined paths
- Efficient for one-to-many relationships

**Disadvantages**:
- Limited flexibility (rigid structure)
- Complex many-to-many relationships difficult to model
- Navigational access (procedural)

---

### 3.4 Network Data Model

The **network data model** extends the hierarchical model by allowing many-to-many relationships. Data is organized as a graph with records connected by links.

**Key Concepts**:
- **Sets**: Define relationships between record types (1:N or M:N)
- **Members**: Child records in a set
- **Owners**: Parent records in a set
- **Pointers**: Physical links connecting related records

**Example**: Library Management System

```
┌─────────────┐         ┌─────────────┐
│   AUTHOR    │◀───────▶│    BOOK     │
│             │  writes │             │
└─────────────┘         └──────┬──────┘
                               │
                               ▼
                        ┌─────────────┐
                        │  BORROWER   │
                        │             │
                        └─────────────┘
```

**Example Code (CODASYL DBTG)**:

```
SCHEMA NAME LIBRARY

RECORD NAME AUTHOR
  01 AUTHOR_ID PIC X(5)
  01 AUTHOR_NAME PIC X(30)

RECORD NAME BOOK
  01 BOOK_ID PIC X(10)
  01 TITLE PIC X(50)
  01 PUBLICATION_YEAR PIC 9(4)

SET NAME WRITES
  OWNER AUTHOR
  MEMBER BOOK
```

**Advantages**:
- More flexible than hierarchical model
- Supports many-to-many relationships
- Efficient navigation through pointers

**Disadvantages**:
- Complex structure and navigation
- Highly procedural (requires knowledge of data paths)
- Database restructuring is difficult

---

### 3.5 Relational Data Model

The **relational data model**, introduced by Edgar F. Codd in 1970, is the most widely used data model in modern database systems. It organizes data into tables (relations) with rows and columns.

**Key Concepts**:

| Term | Description |
|------|-------------|
| **Relation** | A table with rows and columns |
| **Tuple** | A row (record) in a relation |
| **Attribute** | A column (field) in a relation |
| **Domain** | Set of permissible values for an attribute |
| **Primary Key** | Unique identifier for each tuple |
| **Foreign Key** | Attribute referencing primary key of another relation |
| **Degree** | Number of attributes in a relation |
| **Cardinality** | Number of tuples in a relation |

**Example**: University Database Schema

```sql
-- Create Students Table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    DOB DATE,
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(15),
    DepartmentID INT
);

-- Create Departments Table
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100),
    HOD VARCHAR(100)
);

-- Create Courses Table
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    Credits INT,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Create Enrollments Table
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    Semester VARCHAR(20),
    Grade CHAR(2),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Sample Data Insertion
INSERT INTO Departments VALUES 
(1, 'Computer Science', 'Dr. Sharma'),
(2, 'Mathematics', 'Dr. Gupta'),
(3, 'Physics', 'Dr. Verma');

INSERT INTO Students VALUES 
(101, 'Amit Kumar', '2003-05-15', 'amit@example.com', '9876543210', 1),
(102, 'Priya Singh', '2003-08-22', 'priya@example.com', '9876543211', 1),
(103, 'Raj Patel', '2002-11-10', 'raj@example.com', '9876543212', 2);

INSERT INTO Courses VALUES 
(CS101, 'Data Structures', 4, 1),
(CS102, 'Database Systems', 4, 1),
(MATH201, 'Linear Algebra', 3, 2);

INSERT INTO Enrollments VALUES 
(1, 101, 'CS101', 'Fall 2024', 'A'),
(2, 101, 'CS102', 'Fall 2024', 'A-'),
(3, 102, 'CS101', 'Fall 2024', 'B+'),
(4, 103, 'MATH201', 'Fall 2024', 'A');
```

**Query Examples**:

```sql
-- Find all students in Computer Science department
SELECT s.Name, s.Email 
FROM Students s 
JOIN Departments d ON s.DepartmentID = d.DepartmentID 
WHERE d.DepartmentName = 'Computer Science';

-- Find courses enrolled by a specific student
SELECT c.CourseName, e.Grade, e.Semester 
FROM Enrollments e 
JOIN Courses c ON e.CourseID = c.CourseID 
WHERE e.StudentID = 101;

-- Count students per department
SELECT d.DepartmentName, COUNT(s.StudentID) AS StudentCount 
FROM Departments d 
LEFT JOIN Students s ON d.DepartmentID = s.DepartmentID 
GROUP BY d.DepartmentName;
```

**Advantages**:
- Mathematical foundation (set theory and relational algebra)
- Data independence
- Simple query language (SQL)
- Flexible and easily extensible
- Handles complex relationships through joins

**Disadvantages**:
- Performance issues with large datasets
- Limited object-oriented features
- Impedance mismatch with object-oriented programming

---

### 3.6 Object-Oriented Data Model

The **object-oriented data model** combines database technology with object-oriented programming concepts. Objects encapsulate both data and behavior (methods).

**Key Concepts**:

| Concept | Description |
|---------|-------------|
| **Object** | Entity with identity, state (attributes), and behavior (methods) |
| **Class** | Template defining attributes and methods for a group of objects |
| **Inheritance** | Mechanism allowing a class to inherit properties from parent class |
| **Polymorphism** | Ability of objects to respond differently to same message |
| **Encapsulation** | Hiding internal details; only interface is exposed |

**Example**: Object-Oriented Model for E-Commerce

```
┌─────────────────────────────────────────────────────────┐
│                    CLASS: PRODUCT                       │
├─────────────────────────────────────────────────────────┤
│  ATTRIBUTES:                                            │
│    - productID: String                                  │
│    - name: String                                       │
│    - price: Double                                      │
│    - stock: Integer                                     │
│    - category: String                                   │
├─────────────────────────────────────────────────────────┤
│  METHODS:                                               │
│    + calculateDiscount(): Double                        │
│    + updateStock(quantity: Integer): void               │
│    + getDisplayPrice(): Double                         │
└─────────────────────────────────────────────────────────┘
                          △
                          │ inherits
┌─────────────────────────────────────────────────────────┐
│               CLASS: ELECTRONIC_PRODUCT                 │
├─────────────────────────────────────────────────────────┤
│  ATTRIBUTES:                                            │
│    - warrantyPeriod: Integer                            │
│    - brand: String                                      │
├─────────────────────────────────────────────────────────┤
│  METHODS:                                               │
│    + getWarrantyStatus(): String                        │
└─────────────────────────────────────────────────────────┘
```

**Example Code (Object-Oriented Database - ObjectDB)**:

```java
// Java-based OODBMS example using ObjectDB

@Entity
public class Product {
    @Id
    private String productID;
    private String name;
    private double price;
    private int stock;
    private String category;
    
    // Constructor
    public Product(String productID, String name, double price, int stock) {
        this.productID = productID;
        this.name = name;
        this.price = price;
        this.stock = stock;
    }
    
    // Methods
    public double calculateDiscount() {
        if (stock > 100) return 0.20;
        else if (stock > 50) return 0.10;
        else return 0.0;
    }
    
    public void updateStock(int quantity) {
        this.stock -= quantity;
    }
}

@Entity
public class Order {
    @Id
    private String orderID;
    private Date orderDate;
    private List<OrderItem> items;
    private Customer customer;
    
    public double calculateTotal() {
        double total = 0;
        for (OrderItem item : items) {
            total += item.getSubtotal();
        }
        return total;
    }
}
```

**Advantages**:
- Natural representation of complex objects
- Supports inheritance and polymorphism
- Encapsulation provides data security
- Better for CAD, multimedia, and scientific databases

**Disadvantages**:
- Complex and expensive to implement
- Steep learning curve
- Less mature than relational databases
- Performance overhead

---

### 3.7 Object-Relational Data Model

The **object-relational data model** (ORDBMS) combines features of both relational and object-oriented models. It extends traditional relational databases with object-oriented capabilities.

**Key Features**:
- User-defined types (UDT)
- Complex data types (arrays, nested tables)
- Methods on user-defined types
- Inheritance for table types

**Example**: PostgreSQL Object-Relational Features

```sql
-- Create a composite type (user-defined type)
CREATE TYPE address AS (
    street VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    pincode VARCHAR(10)
);

-- Create table using composite type
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    emp_name VARCHAR(100),
    emp_address address,
    salary NUMERIC(10, 2)
);

-- Insert data
INSERT INTO employees (emp_name, emp_address, salary) VALUES 
('Rahul Sharma', ('123 MG Road', 'Delhi', 'Delhi', '110001'), 50000);

-- Query composite type
SELECT emp_name, (emp_address).city FROM employees;

-- Create a table with array type
CREATE TABLE student_courses (
    student_id INT,
    course_names VARCHAR(50)[],
    enrollment_dates DATE[]
);

INSERT INTO student_courses VALUES 
(101, ARRAY['Data Structures', 'Database Systems', 'Algorithms'], 
     ARRAY['2024-01-15', '2024-01-15', '2024-01-15']);

-- Create user-defined type with methods
CREATE TYPE circle AS OBJECT (
    radius NUMBER,
    MEMBER FUNCTION area RETURN NUMBER,
    MEMBER FUNCTION circumference RETURN NUMBER
);

CREATE TYPE BODY circle AS
    MEMBER FUNCTION area RETURN NUMBER IS
    BEGIN
        RETURN 3.14159 * SELF.radius * SELF.radius;
    END;
    
    MEMBER FUNCTION circumference RETURN NUMBER IS
    BEGIN
        RETURN 2 * 3.14159 * SELF.radius;
    END;
END;
```

---

## 4. Comparison of Data Models

| Feature | Hierarchical | Network | Relational | Object-Oriented |
|---------|--------------|---------|------------|------------------|
| **Structure** | Tree | Graph | Table | Objects |
| **Relationship** | 1:N | M:N | M:N (via keys) | Through messages |
| **Access Path** | Navigational | Navigational | Set-oriented | Method-based |
| **Data Independence** | Low | Low | High | High |
| **Complexity** | Simple | Moderate | Simple | Complex |
| **Query Language** | Procedural | Procedural | SQL (Declarative) | OQL |
| **Flexibility** | Low | Moderate | High | Very High |
| **Popular DBMS** | IBM IMS | IDMS, RDB | Oracle, MySQL, SQL Server | ObjectDB, db4o |

---

## 5. Key Takeaways

1. **DBMS Architecture**: The three-schema architecture (external, conceptual, internal) provides data abstraction and independence, allowing users to work at different levels without concern for physical storage details.

2. **Data Independence**: Two types—logical (changes to conceptual schema don't affect external schemas) and physical (changes to internal schema don't affect conceptual schema)—ensure flexibility in database evolution.

3. **Data Models**: Different data models serve different purposes:
   - **Hierarchical**: Best for one-to-many hierarchical data (organization charts, file systems)
   - **Network**: Suitable for complex many-to-many relationships (transportation networks)
   - **Relational**: Industry standard for business applications (banking, e-commerce)
   - **Object-Oriented**: Ideal for complex data (CAD, multimedia, scientific applications)

4. **Relational Model Dominance**: The relational model remains the most widely adopted due to its mathematical foundation (relational algebra, set theory), simple tabular structure, and powerful query language (SQL).

5. **Evolution of Data Models**: The progression from file-based → hierarchical → network → relational → object-oriented reflects the growing complexity of data management needs.

6. **Modern Trends**: Object-relational databases (PostgreSQL, Oracle) combine the best of both worlds, offering relational simplicity with object-oriented capabilities for complex data types.

---

## 6. Practice Questions (Multiple Choice)

### Level 1: Basic Concepts

**Q1. Which architecture level in DBMS defines the physical storage structure?**
- A) External Schema
- B) Conceptual Schema
- C) Internal Schema
- D) None of the above

**Q2. The process of hiding database complexity from users is called:**
- A) Data Abstraction
- B) Data Independence
- C) Data Security
- D) Data Encryption

### Level 2: Intermediate

**Q3. Which data model uses tables with rows and columns?**
- A) Hierarchical
- B) Network
- C) Relational
- D) Object-Oriented

**Q4. In the relational model, a primary key can have:**
- A) Duplicate values
- B) Null values
- C) Unique and non-null values
- D) Multiple values

**Q5. Which DBMS component handles query optimization?**
- A) Storage Manager
- B) Query Processor
- C) Transaction Manager
- D) Data Dictionary

### Level 3: Advanced

**Q6. In a hierarchical data model, each child can have:**
- A) Multiple parents
- B) Exactly one parent
- C) No parent
- D) Either zero or multiple parents

**Q7. The capability that allows changing schema at one level without affecting the next higher level is:**
- A) Data Abstraction
- B) Data Integrity
- C) Data Independence
- D) Data Security

**Q8. Which of the following is NOT a feature of Object-Oriented data model?**
- A) Encapsulation
- B) Inheritance
- C) Primary keys
- D) Polymorphism

### Level 4: Application-Based

**Q9. Consider a university database with tables: STUDENT, COURSE, ENROLLMENT. The ENROLLMENT table typically contains:**
- A) Only foreign keys
- B) Foreign keys referencing STUDENT and COURSE
- C) No foreign keys
- D) Only primary keys

**Q10. Which data model is most suitable for storing complex scientific data with multimedia elements?**
- A) Hierarchical
- B) Network
- C) Relational
- D) Object-Oriented

---

## 7. Answers to MCQs

| Q.No | Answer | Explanation |
|------|--------|-------------|
| 1 | C | Internal schema describes physical storage details |
| 2 | A | Data abstraction hides complexity at different levels |
| 3 | C | Relational model uses tables (relations) |
| 4 | C | Primary key must be unique and cannot be null |
| 5 | B | Query processor interprets and optimizes queries |
| 6 | B | Hierarchical model: one parent per child (1:N) |
| 7 | C | Data independence allows schema changes without affecting upper levels |
| 8 | C | Primary keys are a relational concept, not OO |
| 9 | B | ENROLLMENT links STUDENT and COURSE via foreign keys |
| 10 | D | Object-oriented model handles complex data and multimedia effectively |

---

*Prepared for BSc (Hons) Computer Science - Delhi University, NEP 2024 UGCF Curriculum*