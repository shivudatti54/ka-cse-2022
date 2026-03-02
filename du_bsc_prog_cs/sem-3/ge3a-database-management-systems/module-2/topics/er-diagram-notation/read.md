# ER Diagram Notation - Comprehensive Study Material

## Subject: Ge3A Database Management Systems | BSc Physical Science (CS) - Delhi University (NEP 2024)

---

## 1. Introduction

An **Entity-Relationship (ER) Diagram** is a fundamental tool in database design that provides a visual representation of the data objects, their attributes, and the relationships between them. Developed by **Peter Chen** in 1976, the ER model serves as a blueprint for organizing data logically before implementing a physical database.

### Real-World Relevance

In today's data-driven world, organizations rely on well-designed databases to manage vast amounts of information. Consider these scenarios:

- **Banking Systems**: Managing millions of customer accounts, transactions, and loans requires carefully designed databases where entities like Customer, Account, and Transaction are clearly defined with proper relationships.
- **E-Commerce Platforms**: Amazon or Flipkart manage inventory, orders, customers, and shipping details—all interconnected through carefully planned relationships.
- **University Management**: Delhi University's own student record system needs to track students, courses, enrollments, and grades.

The ER diagram acts as the **foundation** before any SQL code is written. A poorly designed ER model leads to data redundancy, anomalies, and inefficient queries—common pitfalls that database administrators struggle with later.

---

## 2. Core Components of ER Model

### 2.1 Entities

An **entity** represents a real-world object or concept that has independent existence and can be uniquely identified.

**Examples:**
- Student (a person)
- Course (an academic offering)
- BankAccount (a financial entity)

**Entity Set**: A collection of similar entities (e.g., all students in the university).

**Entity Type**: The schema that defines the structure (e.g., Student entity type with attributes like RollNo, Name, DateOfBirth).

### 2.2 Attributes

**Attributes** are properties or characteristics of an entity. Each attribute stores a specific type of information.

#### Types of Attributes:

| Attribute Type | Description | Example |
|----------------|-------------|---------|
| **Simple Attribute** | Cannot be divided further | StudentID, Age |
| **Composite Attribute** | Can be broken into sub-attributes | Name (FirstName, LastName), Address (Street, City, PinCode) |
| **Single-valued Attribute** | Holds one value | DateOfBirth |
| **Multi-valued Attribute** | Can hold multiple values | PhoneNumber, Email |
| **Derived Attribute** | Calculated from other attributes | Age (derived from DateOfBirth), TotalCredits |

**Notation (Chen's Notation):**
- Entity: Rectangle
- Attribute: Ellipse (oval)
- Connecting lines: Solid lines from entity to attributes

---

## 3. Relationships

A **relationship** describes how two or more entities are associated with each other. Relationships represent the **associations** or **interactions** between entity sets.

### 3.1 Degree of Relationship

- **Unary (Recursive)**: Relationship between entities of the same type (e.g., Employee manages Employee)
- **Binary**: Relationship between two entity types (e.g., Student enrolls in Course)
- **Ternary**: Relationship involving three entity types (e.g., Student enrolls in Course taught by Professor)
- **N-ary**: Relationship involving 'n' entity types

### 3.2 Cardinality (Cardinality Ratios)

Cardinality defines the **number of instances** of one entity that can be associated with a single instance of another entity.

| Cardinality | Notation | Meaning | Example |
|-------------|----------|---------|---------|
| **One-to-One (1:1)** | 1:1 | Each entity in A relates to exactly one entity in B, and vice versa | Person has one Passport |
| **One-to-Many (1:N)** | 1:N | One entity in A relates to multiple entities in B | Department has many Employees |
| **Many-to-Many (N:M)** | N:M | Multiple entities in A relate to multiple entities in B | Student enrolls in many Courses |

### 3.3 Participation Constraints

Participation determines whether the existence of an entity **depends** on its association with another entity.

- **Total Participation (Existence Dependency)**: Every entity in the entity set MUST participate in the relationship. Also called "existence-dependent." Denoted by double line in ER diagram.
- **Partial Participation**: Entities may or may not participate in the relationship. Denoted by single line.

**Example:**
- Every student MUST enroll in at least one course (total participation)
- A course MAY have enrolled students (partial participation)

---

## 4. ER Diagram Notations

### 4.1 Chen's Notation (Classical)

This is the original notation developed by Peter Chen.

| Component | Symbol |
|-----------|--------|
| Entity | Rectangle |
| Attribute | Ellipse (Oval) |
| Relationship | Diamond |
| Primary Key | Underlined attribute |
| Multi-valued Attribute | Double ellipse |
| Derived Attribute | Dashed ellipse |

**Example:**
```
    Student (entity)
        |
        +-- RollNo (PK)
        +-- Name
        +-- Email
        +-- Phone# (multi-valued)
        +-- Age (derived)
```

### 4.2 Crow's Foot Notation (Information Engineering)

Also known as **IE Notation** or **Bird's Foot Notation**, this is widely used in industry and database design tools.

| Symbol | Meaning |
|--------|---------|
| ○ (Circle) | Zero (optional) |
| | (Vertical line) | Exactly one |
| } (Crow's foot) | Many (one or more) |
| --- | Single line = Partial participation |
| === | Double line = Total participation |

**Cardinality Visualization:**

```
One-to-One:        One-to-Many:        Many-to-Many:
    |   |              |   }               }   }
    |   |              |   }               }   }
    A   B              A   B               A   B
```

### 4.3 UML Class Diagram Notation

The **Unified Modeling Language (UML)** is commonly used in software engineering and provides an object-oriented perspective.

| Component | Representation |
|-----------|----------------|
| Entity (Class) | Rectangle with three sections (Class name, Attributes, Methods) |
| Relationship | Various lines with different arrowheads |
| Multiplicity | Numbers or ranges near ends |

**UML Relationship Types:**
- **Association**: Simple relationship (single line)
- **Aggregation**: "Has-a" relationship, part can exist independently (diamond outline)
- **Composition**: Strong "has-a", part cannot exist independently (filled diamond)
- **Inheritance**: "Is-a" relationship (triangle arrow)

---

## 5. Concrete Examples

### Example 1: College Management System

**Scenario**: Design an ER diagram for a college system that manages Students, Courses, Departments, and Professors.

**Entities and Attributes:**

```
DEPARTMENT
- DeptID (PK)
- DeptName
- Location

PROFESSOR
- ProfID (PK)
- ProfName
- Designation
- Salary

COURSE
- CourseID (PK)
- CourseName
- Credits

STUDENT
- StudentID (PK)
- StudentName
- DateOfBirth
- Address
- Phone (Multi-valued)
```

**Relationships:**

1. **Department HAS Professors** (1:N)
   - A department has many professors
   - A professor belongs to one department
   - Total participation for professor

2. **Professor TEACHES Course** (M:N)
   - A course can be taught by multiple professors
   - A professor can teach multiple courses

3. **Student ENROLLS IN Course** (M:N)
   - A student can enroll in multiple courses
   - A course can have multiple students
   - Grade is an attribute of the enrollment relationship

**ER Diagram (Conceptual):**

```text
    +-----------+         +-----------+
    | DEPARTMENT|         | PROFESSOR |
    +-----------+         +-----------+
    | DeptID (PK) | 1   N | ProfID (PK)|
    | DeptName   |<------>| ProfName  |
    | Location   |        | Designation|
    +-----------+        | Salary    |
                         +-----------+
                             |
                             | teaches (M:N)
                             |
                         +-----------+
                         |  COURSE   |
                         +-----------+
                         | CourseID(PK)|
                         | CourseName |
                         | Credits    |
                         +-----------+
                               |
                               | enrolls (M:N)
                               |
                         +-----------+
                         |  STUDENT  |
                         +-----------+
                         | StudentID |
                         | StudentName|
                         | DOB       |
                         | Address   |
                         +-----------+
```

### Example 2: Online Shopping System

**Scenario**: Design an ER diagram for an e-commerce platform.

**Entities:**

```
CUSTOMER
- CustomerID (PK)
- Name
- Email
- Password

PRODUCT
- ProductID (PK)
- ProductName
- Price
- StockQuantity
- Category

ORDER
- OrderID (PK)
- OrderDate
- TotalAmount
- Status

SHIPPING_ADDRESS
- AddressID (PK)
- Street
- City
- State
- PinCode
```

**Relationships:**

1. **Customer PLACES Order** (1:N)
   - One customer can place multiple orders
   - Customer participation: Partial (can browse without ordering)
   - Order participation: Total (every order must have a customer)

2. **Order CONTAINS Product** (M:N with attributes)
   - An order contains multiple products
   - A product can appear in multiple orders
   - Attributes: Quantity, UnitPrice (at time of order)

3. **Order HAS Shipping Address** (1:1)
   - Each order has exactly one shipping address

---

## 6. Converting ER Diagram to Relational Schema

The **relational model** is the foundation of modern database systems. Converting an ER diagram to relational schema is a critical skill.

### 6.1 Mapping Rules

**Rule 1: Strong Entity Types**
- Create a relation (table) with all simple attributes
- Primary key becomes the primary key of the new table

**Example:**
```
STUDENT(StudentID, Name, DateOfBirth, Address)
```

**Rule 2: Weak Entity Types**
- Create a relation including all attributes
- Include the primary key of the owning entity as a foreign key
- The combination forms the composite primary key

**Example:**
```
DEPENDENT(EmpID, DependentName, Relationship, Age)
-- EmpID is foreign key referencing EMPLOYEE
-- (EmpID, DependentName) is the composite primary key
```

**Rule 3: Binary Relationships**

| Cardinality | Mapping Strategy |
|-------------|------------------|
| 1:1 | Choose one entity, add foreign key referencing the other |
| 1:N | Add foreign key in the "N" side entity referencing "1" side |
| M:N | Create a new relation with foreign keys to both entities |

**Example (1:N - Department HAS Employees):**
```
DEPARTMENT(DeptID, DeptName)
EMPLOYEE(EmpID, EmpName, DeptID) 
-- DeptID is foreign key referencing DEPARTMENT
```

**Example (M:N - Student Enrolls in Course):**
```
STUDENT(StudentID, Name)
COURSE(CourseID, CourseName)
ENROLLMENT(StudentID, CourseID, Grade, Semester)
-- StudentID references STUDENT
-- CourseID references COURSE
-- Composite primary key (StudentID, CourseID)
```

**Rule 4: Composite Attributes**
- Split into simple attributes

**Rule 5: Multi-valued Attributes**
- Create a new relation with the primary key of the entity as foreign key
- The multi-valued attribute becomes the primary key of the new relation

**Example:**
```
STUDENT(StudentID, Name, DOB)
PHONE(StudentID, PhoneNumber)
-- StudentID references STUDENT
```

### 6.2 Complete Conversion Example

**ER Diagram: College System**

```
DEPARTMENT(DeptID PK, DeptName, Location)
PROFESSOR(ProfID PK, ProfName, DeptID FK, Salary)
COURSE(CourseID PK, CourseName, Credits, ProfID FK)
STUDENT(StudentID PK, StudentName, DOB, Address)
ENROLLMENT(StudentID FK, CourseID FK, Grade, Semester)
-- Primary key: (StudentID, CourseID)
-- References: STUDENT, COURSE
```

**SQL DDL Implementation:**

```sql
CREATE TABLE DEPARTMENT (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50) NOT NULL,
    Location VARCHAR(50)
);

CREATE TABLE PROFESSOR (
    ProfID INT PRIMARY KEY,
    ProfName VARCHAR(100) NOT NULL,
    DeptID INT NOT NULL,
    Salary DECIMAL(10, 2),
    FOREIGN KEY (DeptID) REFERENCES DEPARTMENT(DeptID)
);

CREATE TABLE COURSE (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50) NOT NULL,
    Credits INT,
    ProfID INT,
    FOREIGN KEY (ProfID) REFERENCES PROFESSOR(ProfID)
);

CREATE TABLE STUDENT (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100) NOT NULL,
    DateOfBirth DATE,
    Address VARCHAR(200)
);

CREATE TABLE ENROLLMENT (
    StudentID INT NOT NULL,
    CourseID INT NOT NULL,
    Grade CHAR(2),
    Semester VARCHAR(20),
    PRIMARY KEY (StudentID, CourseID),
    FOREIGN KEY (StudentID) REFERENCES STUDENT(StudentID),
    FOREIGN KEY (CourseID) REFERENCES COURSE(CourseID)
);
```

---

## 7. Delhi University Syllabus Context

As per the **Ge3A Database Management Systems** syllabus under NEP 2024 for BSc Physical Science (CS), this topic covers:

- ER Model concepts and notation
- Entity types, attributes, and relationships
- Cardinality and participation constraints
- Conversion of ER diagrams to relational schemas
- Understanding different notations (Chen, Crow's Foot, UML)

**Relevant Units:**
- Unit 2: Entity-Relationship Model
- Unit 3: Relational Model and SQL

---

## 8. Key Takeaways

1. **ER Diagrams** are the blueprint for database design—they define what data to store and how data elements relate.

2. **Entities** represent real-world objects; **attributes** describe their properties; **relationships** define associations.

3. **Cardinality** (1:1, 1:N, N:M) and **participation** (total/partial) are critical for accurately modeling business rules.

4. **Chen's notation** uses diamonds and ovals; **Crow's foot** uses lines and crow's feet symbols; **UML** uses class diagrams—each has specific use cases.

5. Converting ER to relational schema requires systematic application of mapping rules based on entity types and relationship cardinalities.

6. A well-designed ER model prevents data redundancy and ensures database integrity.

7. Understanding all notations is essential for working with different database design tools and understanding existing documentation.

---

## 9. Assessment MCQs

### Easy Level

1. In ER diagrams, what does a rectangle represent?
   - a) Attribute
   - b) Entity
   - c) Relationship
   - d) Key
   
   **Answer: b) Entity**

2. Which notation uses "crow's foot" symbols?
   - a) Chen's Notation
   - b) UML Notation
   - c) Information Engineering Notation
   - d) Bachman Notation
   
   **Answer: c) Information Engineering Notation**

3. A relationship where one entity is associated with many entities of another type is called:
   - a) One-to-One
   - b) One-to-Many
   - c) Many-to-Many
   - d) Binary
   
   **Answer: b) One-to-Many**

### Medium Level

4. Consider the relationship "Student enrolls in Course". If every student MUST enroll in at least one course, what is the participation constraint for Student?
   - a) Partial participation
   - b) Total participation
   - c) Minimum participation
   - d) Optional participation
   
   **Answer: b) Total participation**

5. In Chen's notation, which symbol represents a multi-valued attribute?
   - a) Double rectangle
   - b) Double oval
   - c) Double diamond
   - d) Dashed oval
   
   **Answer: b) Double oval**

6. For a binary 1:N relationship, where should the foreign key be placed?
   - a) In the "1" side entity
   - b) In the "N" side entity
   - c) In a separate relation
   - d) Both entities
   
   **Answer: b) In the "N" side entity**

### Hard Level

7. Consider a ternary relationship "Employee works on Project in Department". To convert this to relational schema, how many foreign keys will the resulting relation have?
   - a) 1
   - b) 2
   - c) 3
   - d) 0
   
   **Answer: c) 3** (One foreign key for each participating entity)

8. In UML class diagrams, which relationship type represents a "has-a" relationship where the part can exist independently?
   - a) Composition
   - b) Aggregation
   - c) Association
   - d) Inheritance
   
   **Answer: b) Aggregation**

9. Which of the following is NOT a component of the ER model?
   - a) Entities
   - b) Attributes
   - c) Methods
   - d) Relationships
   
   **Answer: c) Methods** (Methods belong to object-oriented models, not ER)

10. A weak entity type is identified by:
    - a) Its own primary key only
    - b) A foreign key plus its own partial key
    - c) A composite key with no foreign key
    - d) Only foreign keys
    
    **Answer: b) A foreign key plus its own partial key**

---

## 10. Flashcards

| Term | Definition |
|------|------------|
| **Entity** | A real-world object with independent existence that can be uniquely identified |
| **Attribute** | A property or characteristic of an entity |
| **Relationship** | An association between two or more entities |
| **Cardinality** | The number of instances of one entity associated with another entity |
| **Participation Constraint** | Determines whether an entity must participate in a relationship (total) or may participate (partial) |
| **Primary Key** | A unique identifier for each entity instance |
| **Foreign Key** | An attribute that references the primary key of another relation |
| **Weak Entity** | An entity that cannot be uniquely identified by its own attributes alone |
| **Composite Attribute** | An attribute that can be divided into smaller sub-attributes |
| **Multi-valued Attribute** | An attribute that can hold multiple values |
| **Derived Attribute** | An attribute whose value can be computed from other attributes |
| **Chen’s Notation** | Classical ER notation using rectangles, ovals, and diamonds |
| **Crow’s Foot Notation** | Industry notation using lines and "foot" symbols to show cardinality |
| **UML** | Unified Modeling Language used for object-oriented design |
| **M:N Relationship** | Many-to-many relationship requiring a junction table |

---

*Material prepared for Ge3A Database Management Systems, BSc Physical Science (CS), Delhi University NEP 2024*