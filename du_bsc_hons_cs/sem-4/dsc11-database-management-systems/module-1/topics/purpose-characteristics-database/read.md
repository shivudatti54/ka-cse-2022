# Purpose and Characteristics of Database Systems

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

In today's data-driven world, the ability to store, manage, and retrieve information efficiently is fundamental to virtually every organization and application. From banking transactions to social media platforms, from healthcare records to e-commerce inventories—databases form the backbone of modern information systems.

This study material covers the **Purpose and Characteristics of Database Systems**, a foundational topic in the Database Management Systems (DBMS) course as prescribed in the Delhi University BSc (Hons) Computer Science syllabus under NEP 2024 UGCF. We will explore why database systems were developed, what distinguishes them from traditional file processing systems, and examine the key characteristics that make them indispensable in computing.

---

## 2. What is a Database?

A **database** is a structured collection of organized data that is stored electronically in a computer system. It is designed to allow efficient storage, retrieval, modification, and deletion of data while maintaining data integrity and security.

### Key Definitions

- **Database Management System (DBMS)**: Software that provides an interface to store and manage data in a database. Examples: MySQL, PostgreSQL, Oracle, SQL Server, MongoDB.

- **Database System**: The combination of the database, the DBMS software, and the application programs that interact with the database.

---

## 3. Purpose of Database Systems

The primary purpose of database systems evolved from the limitations of traditional file processing systems. Let's examine why databases were developed:

### 3.1 Problems with File Processing Systems

1. **Data Redundancy**: The same data may be stored in multiple files, leading to wastage of storage space and inconsistencies.

2. **Data Inconsistency**: Due to redundancy, updates to one file may not be reflected in others, causing data integrity issues.

3. **Difficulty in Data Access**: Non-programmers find it challenging to retrieve specific data without writing custom programs.

4. **Data Isolation**: Data scattered across multiple files makes it difficult to develop new applications.

5. **Security Problems**: Implementing proper access controls is challenging in file systems.

6. **No Concurrent Access Control**: Multiple users cannot safely access the same data simultaneously.

7. **No Backup and Recovery**: File systems lack robust mechanisms for automatic backup and recovery after failures.

### 3.2 How Database Systems Address These Problems

| Problem | Database Solution |
|---------|-------------------|
| Data Redundancy | Centralized data storage, normalization |
| Data Inconsistency | Integrity constraints, controlled updates |
| Difficulty in Data Access | Query languages (SQL), user-friendly interfaces |
| Data Isolation | Integrated data architecture |
| Security Problems | User authentication, role-based access control |
| Concurrent Access | Transaction management, locking mechanisms |
| Backup/Recovery | Automated logging and recovery procedures |

---

## 4. Characteristics of Database Systems

The modern DBMS possesses several distinguishing characteristics:

### 4.1 Data Abstraction

Database systems provide **levels of abstraction** to hide complexity from users:

- **Physical Level**: How data is physically stored (storage structures, indexing, file organization)
- **Logical Level**: What data is stored and the relationships among data (schema definition)
- **View Level**: Individual user perspectives (different users see different subsets of data)

### 4.2 Data Independence

- **Physical Data Independence**: Changes to the physical storage structure do not affect the logical schema
- **Logical Data Independence**: Changes to the logical schema do not affect application programs

### 4.3 Data Consistency and Integrity

Database systems enforce **integrity constraints** to maintain accuracy and validity:

- **Domain Constraints**: Valid values for each attribute (e.g., age > 0)
- **Entity Integrity**: Primary key cannot be NULL
- **Referential Integrity**: Foreign key values must match primary key values in related tables
- **User-defined Integrity**: Application-specific rules

### 4.4 Concurrent Access Control

Multiple users can access the database simultaneously without interfering with each other through mechanisms like **locking** and **timestamping**.

### 4.5 Transaction Support

A **transaction** is a logical unit of work that must be executed completely or not at all. Database systems ensure transactions are:

- **Atomic**: All operations complete or none do
- **Consistent**: Database moves from one valid state to another
- **Isolated**: Concurrent transactions appear to execute serially
- **Durable**: Once committed, changes persist even after system failure

This leads to the famous **ACID properties**.

---

## 5. ACID Properties (Detailed)

The ACID properties form the foundation of reliable database transactions:

### 5.1 Atomicity

A transaction is treated as a single, indivisible unit. Either **all** operations execute successfully, or **none** do.

**Example**: Consider a money transfer from Account A to Account B:
```sql
BEGIN TRANSACTION;
    UPDATE Accounts SET balance = balance - 1000 WHERE account_id = 'A';
    UPDATE Accounts SET balance = balance + 1000 WHERE account_id = 'B';
COMMIT;
```
If the first UPDATE succeeds but the system fails before the second, atomicity ensures the entire transaction is rolled back—Account A is not debited.

### 5.2 Consistency

A transaction must transform the database from one consistent state to another, respecting all integrity constraints.

**Example**: If a database has a constraint that `CHECK (age >= 18)`, any transaction that attempts to insert age = 15 will be rejected, preserving consistency.

### 5.3 Isolation

The execution of concurrent transactions appears sequential—each transaction executes as if it is the only one running, even when multiple transactions run simultaneously.

**Example**: If two transactions read and modify the same data, isolation ensures the final result is as if they executed one after another, not interleaved.

### 5.4 Durability

Once a transaction commits, its changes are permanent and survive any subsequent system failure (power outage, crash, etc.).

**Example**: After a successful `COMMIT`, even if the database server crashes moments later, the changes are persisted to disk and will be there when the system restarts.

---

## 6. Data Models

A **data model** is a collection of concepts that describe the structure of a database. Different data models represent data at different levels of abstraction.

### 6.1 Hierarchical Model

- Data organized in tree-like structure
- Parent-child relationships (one-to-many)
- Example: IBM Information Management System (IMS)
- Used in early mainframe systems

### 6.2 Network Model

- Data organized as a graph with multiple connections
- Many-to-many relationships supported
- More flexible than hierarchical
- Example: Integrated Data Store (IDS)

### 6.3 Relational Model (Most Important)

- Data organized in **tables** (relations)
- Rows = records (tuples)
- Columns = attributes
- Relationships established through keys
- Based on set theory and predicate logic
- Foundation of modern databases (MySQL, PostgreSQL, Oracle)

**Example**:
```sql
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    enrollment_date DATE
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT
);

CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    grade VARCHAR(2),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
```

### 6.4 Object-Oriented Model

- Data stored as objects (like in OOP)
- Supports complex data types
- Examples: ObjectDB,db4o
- Used in specialized applications

### 6.5 Entity-Relationship (ER) Model

- Conceptual model for database design
- Entities, attributes, and relationships
- Not a data storage model, but a design tool

---

## 7. Normalization

**Normalization** is the process of organizing data to reduce redundancy and improve data integrity. It involves decomposing tables into smaller, related tables.

### 7.1 First Normal Form (1NF)

- Each column contains atomic (indivisible) values
- Each column contains values of a single type
- Each row is unique
- Order of rows and columns is insignificant

**Example - Not in 1NF**:
| Student_ID | Name | Phone_Numbers |
|------------|------|---------------|
| 1 | John | 9876543210, 9876543211 |
| 2 | Alice | 9876543212 |

**1NF Version**:
| Student_ID | Name | Phone_Number |
|------------|------|--------------|
| 1 | John | 9876543210 |
| 1 | John | 9876543211 |
| 2 | Alice | 9876543212 |

### 7.2 Second Normal Form (2NF)

- Must be in 1NF
- No partial dependencies (non-key attributes must depend on the entire primary key)

**Example**:
| Order_ID | Product_ID | Product_Name | Quantity |
|----------|------------|--------------|----------|
| 1 | P1 | Laptop | 2 |
| 1 | P2 | Mouse | 5 |

- Here, (Order_ID, Product_ID) is the composite primary key
- Product_Name depends only on Product_ID (partial dependency)
- To achieve 2NF, we split into:
  - Orders(Order_ID, Product_ID, Quantity)
  - Products(Product_ID, Product_Name)

### 7.3 Third Normal Form (3NF)

- Must be in 2NF
- No transitive dependencies (non-key attributes should depend only on the primary key)

**Example**:
| Student_ID | Name | City | Zip_Code |
|------------|------|------|----------|
| 1 | John | Delhi | 110001 |

- City depends on Zip_Code, which depends on Student_ID (transitive)
- Split into:
  - Students(Student_ID, Name, Zip_Code)
  - ZipCodes(Zip_Code, City)

### 7.4 Boyce-Codd Normal Form (BCNF)

- Must be in 3NF
- For every functional dependency A → B, A must be a superkey

---

## 8. Structured Query Language (SQL)

SQL is the standard language for managing relational databases. It includes commands for data definition, manipulation, and control.

### 8.1 Data Definition Language (DDL)

```sql
-- Create a table
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    department_id INT,
    salary DECIMAL(10,2),
    hire_date DATE
);

-- Alter table structure
ALTER TABLE Employee ADD COLUMN email VARCHAR(100);

-- Drop table
DROP TABLE Employee;

-- Create index
CREATE INDEX idx_dept ON Employee(department_id);
```

### 8.2 Data Manipulation Language (DML)

```sql
-- Insert data
INSERT INTO Employee (emp_id, emp_name, department_id, salary, hire_date)
VALUES (101, 'Rahul Sharma', 1, 55000.00, '2023-01-15');

-- Update data
UPDATE Employee 
SET salary = salary * 1.10 
WHERE department_id = 1;

-- Delete data
DELETE FROM Employee WHERE emp_id = 101;

-- Query data
SELECT emp_name, salary 
FROM Employee 
WHERE department_id = 1 
ORDER BY salary DESC;
```

### 8.3 Complex Queries

```sql
-- Join operation
SELECT e.emp_name, d.department_name
FROM Employee e
INNER JOIN Department d ON e.department_id = d.department_id;

-- Subquery
SELECT emp_name, salary
FROM Employee
WHERE salary > (SELECT AVG(salary) FROM Employee);

-- Aggregate functions
SELECT department_id, COUNT(*) as emp_count, AVG(salary) as avg_salary
FROM Employee
GROUP BY department_id
HAVING COUNT(*) > 5;

-- Set operations
SELECT name FROM Students WHERE course = 'CS'
UNION
SELECT name FROM Faculty WHERE department = 'CS';
```

### 8.4 Transaction Control

```sql
START TRANSACTION;
UPDATE Account SET balance = balance - 5000 WHERE account_id = 'A';
UPDATE Account SET balance = balance + 5000 WHERE account_id = 'B';
-- If both succeed
COMMIT;
-- If error occurs
ROLLBACK;
```

---

## 9. Concurrency Control

**Concurrency control** ensures that multiple transactions can execute simultaneously without violating data integrity.

### 9.1 Problems Without Concurrency Control

1. **Lost Update**: Two transactions read and update the same data, one update is lost

2. **Dirty Read**: Transaction reads data written by an uncommitted transaction

3. **Non-repeatable Read**: Re-reading data gives different results due to concurrent updates

4. **Phantom Read**: New rows appear during repeated queries

### 9.2 Concurrency Control Techniques

**Locking**:
- **Shared Lock (S)**: Allows reading; multiple shared locks can be held simultaneously
- **Exclusive Lock (X)**: Allows both reading and writing; only one transaction can hold it

```sql
-- Locking in practice (implicit)
SELECT * FROM Employee WHERE department_id = 1 FOR UPDATE;
```

**Timestamping**:
- Assigns unique timestamps to transactions
- Ensures older transactions don't interfere with newer ones

**Multiversion Concurrency Control (MVCC)**:
- Maintains multiple versions of data
- Readers don't block writers and vice versa
- Used by PostgreSQL, MySQL (InnoDB)

---

## 10. Backup and Recovery

### 10.1 Backup Types

1. **Full Backup**: Complete copy of entire database
2. **Incremental Backup**: Only changes since last backup
3. **Differential Backup**: Changes since last full backup

### 10.2 Recovery Techniques

- **Log-based Recovery**: Records all transactions in a log file
- **Checkpointing**: Periodically saves database state
- **Shadow Paging**: Maintains two copies of database pages

```sql
-- MySQL backup example
-- Command line: mysqldump -u root -p database_name > backup.sql

-- Recovery
-- Command line: mysql -u root -p database_name < backup.sql
```

---

## 11. Database Views

A **view** is a virtual table based on the result of a query. It does not store data physically but presents data from one or more tables.

### 11.1 Creating Views

```sql
-- Simple view
CREATE VIEW CS_Students AS
SELECT student_id, name, email
FROM Students
WHERE course = 'Computer Science';

-- Complex view with joins
CREATE VIEW StudentCourseView AS
SELECT s.student_id, s.name, c.course_name, e.grade
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;
```

### 11.2 Using Views

```sql
-- Query a view like a table
SELECT * FROM CS_Students WHERE name LIKE 'A%';

-- Update through view (with conditions)
UPDATE CS_Students SET email = 'new@email.com' WHERE student_id = 1;
```

### 11.3 Advantages of Views

- **Data Security**: Restrict access to specific columns/rows
- **Simplified Queries**: Complex queries saved as views
- **Logical Data Independence**: Application programs unaffected by table changes
- **Reduced Complexity**: Users see simplified data representation

---

## 12. Real-World Example: University Management System

Consider a real-world implementation of a database system:

### Scenario: Delhi University Examination System

```sql
-- Core tables for examination database

CREATE TABLE Students (
    student_id VARCHAR(20) PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    program VARCHAR(50),
    semester INT
);

CREATE TABLE Courses (
    course_code VARCHAR(10) PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT,
    department_id INT
);

CREATE TABLE Faculty (
    faculty_id INT PRIMARY KEY,
    faculty_name VARCHAR(100),
    department_id INT
);

CREATE TABLE CourseAssignment (
    assignment_id INT PRIMARY KEY,
    course_code VARCHAR(10),
    faculty_id INT,
    semester INT,
    academic_year VARCHAR(10),
    FOREIGN KEY (course_code) REFERENCES Courses(course_code),
    FOREIGN KEY (faculty_id) REFERENCES Faculty(fulty_id)
);

CREATE TABLE Examinations (
    exam_id INT PRIMARY KEY,
    course_code VARCHAR(10),
    exam_date DATE,
    exam_type VARCHAR(20),
    FOREIGN KEY (course_code) REFERENCES Courses(course_code)
);

CREATE TABLE Marks (
    mark_id INT PRIMARY KEY,
    student_id VARCHAR(20),
    exam_id INT,
    marks_obtained DECIMAL(5,2),
    grade VARCHAR(2),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (exam_id) REFERENCES Examinations(exam_id)
);

-- Complex query: Get top performers in a course
SELECT s.student_id, s.student_name, m.marks_obtained
FROM Students s
JOIN Marks m ON s.student_id = m.student_id
JOIN Examinations e ON m.exam_id = e.exam_id
WHERE e.course_code = 'CS301'
ORDER BY m.marks_obtained DESC
LIMIT 10;

-- View for student results
CREATE VIEW StudentResults AS
SELECT 
    s.student_id,
    s.student_name,
    c.course_name,
    e.exam_type,
    m.marks_obtained,
    m.grade
FROM Students s
JOIN Marks m ON s.student_id = m.student_id
JOIN Examinations e ON m.exam_id = e.exam_id
JOIN Courses c ON e.course_code = c.course_code;
```

---

## 13. Key Takeaways

1. **Purpose of Database Systems**: Databases were developed to overcome limitations of file processing systems, including data redundancy, inconsistency, and security issues.

2. **ACID Properties**: The four properties—Atomicity, Consistency, Isolation, and Durability—ensure reliable transaction processing in database systems.

3. **Data Models**: Various models (hierarchical, network, relational, object-oriented) provide different ways to structure and represent data. The relational model is most widely used.

4. **Normalization**: The process of organizing data through 1NF, 2NF, 3NF, and BCNF eliminates redundancy and ensures data integrity.

5. **SQL**: The standard query language provides comprehensive commands for defining, manipulating, and controlling database data.

6. **Concurrency Control**: Techniques like locking and timestamp ensure multiple users can safely access data simultaneously.

7. **Views**: Virtual tables provide data abstraction, security, and simplified access to complex data.

8. **Data Abstraction and Independence**: Database systems separate physical storage from logical structure, enabling flexibility in application development.

---

## 14. Assessment Section

### Part A: Multiple Choice Questions (University Level)

**1. Which ACID property ensures that a transaction is executed as a single unit?**

A) Consistency
B) Isolation
C) Atomicity
D) Durability

**2. In the relational model, a tuple corresponds to:**

A) A column
B) A table
C) A row
D) A relationship

**3. A relation is in which normal form if it has no transitive dependencies?**

A) 1NF
B) 2NF
C) 3NF
D) BCNF

**4. Which SQL command is used to remove all data from a table but keep its structure?**

A) DROP
B) DELETE
C) TRUNCATE
D) REMOVE

**5. In a deadlock situation, what happens to the transactions?**

A) They continue normally
B) They are automatically committed
C) They wait indefinitely for each other
D) They are rolled back immediately

**Answers**: 1-C, 2-C, 3-C, 4-C, 5-C

---

### Part B: Scenario-Based Questions

**Scenario 1: Banking Transaction System**

In a banking database, a funds transfer operation involves debiting Account A and crediting Account B. During this transaction, the system crashes after the debit operation but before the credit operation.

**Questions:**
1. Which ACID property should prevent any permanent changes to the database?
2. How would the DBMS recover from this situation?
3. If the system uses write-ahead logging, explain how this helps in recovery.

**Scenario 2: University Result System**

A university database has tables for Students, Courses, and Enrollments. The examination cell needs to:
- Allow faculty to enter marks for their assigned courses only
- Allow students to view their own marks
- Generate statistical reports for administration

**Questions:**
1. Design an SQL view to restrict student access to only their own marks.
2. Explain how you would implement row-level security for faculty.
3. Write a query to find the average marks per course for the current semester.

---

### Part C: SQL Query Practice

**Given Schema:**
```sql
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock_quantity INT,
    supplier_id INT
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    status VARCHAR(20)
);

CREATE TABLE OrderItems (
    item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
```

**Queries to Write:**

1. List all products with stock below 10 units, ordered by stock quantity.
2. Find the total revenue generated by each product category.
3. Update the price of all products in 'Electronics' category by 15% increase.
4. Create a view showing order details with product names and quantities.
5. Write a transaction to process a new order and update stock atomically.

---

### Part D: Flashcards

| Term | Definition |
|------|------------|
| **ACID** | Atomicity, Consistency, Isolation, Durability — four properties ensuring reliable transactions |
| **Normalization** | Process of organizing data to reduce redundancy through decomposition of tables |
| **Primary Key** | Unique identifier for each record; cannot be NULL |
| **Foreign Key** | Attribute that references primary key of another table; enforces referential integrity |
| **Transaction** | Logical unit of work that must be executed completely or not at all |
| **View** | Virtual table based on a query; does not store data physically |
| **Schema** | Logical structure or blueprint of the database |
| **Index** | Data structure that improves the speed of data retrieval operations |
| **Join** | Operation combining rows from two or more tables based on related columns |
| **Concurrency** | Ability of database to handle multiple simultaneous transactions |

---

## 15. Conclusion

This comprehensive study material covers all essential aspects of the **Purpose and Characteristics of Database Systems** as required for the Delhi University BSc (Hons) Computer Science curriculum. Students should focus on understanding the theoretical concepts while practicing SQL queries and normalization techniques to build proficiency in database management.

The knowledge of database systems is fundamental for any computer science professional, as data management forms the core of modern software applications and enterprise systems.

---

*Study Material prepared for Delhi University NEP 2024 UGCF Curriculum*