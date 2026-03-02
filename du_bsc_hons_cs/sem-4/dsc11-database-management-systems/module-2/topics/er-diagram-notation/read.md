# ER Diagram Notation: Comprehensive Study Material

## Database Management Systems — BSc (Hons) Computer Science (Delhi University NEP 2024 UGCF)

---

## 1. Introduction to ER Diagram Notation

**Entity-Relationship (ER) Diagram** is a fundamental tool in database design that provides a visual representation of data and its relationships within a system. Developed by **Peter Chen** in 1976, the ER model serves as a blueprint for organizing data logically before implementing the physical database.

### Why ER Diagrams Matter in Real-World Applications

Consider a university management system where you need to track students, courses, instructors, and enrollments. Without proper modeling, the system would become chaotic with redundant data and inconsistent records. ER diagrams help database designers:

- **Visualize data structure** before writing any code
- **Identify entities** and their attributes clearly
- **Establish relationships** between different data components
- **Ensure data integrity** through proper constraints
- **Communicate effectively** with stakeholders and development teams

For Delhi University students, understanding ER diagram notation is essential as it forms the foundation of database design, which is a core component of the **Database Management Systems (DBMS)** paper in the BSc (Hons) Computer Science curriculum under NEP 2024 UGCF.

---

## 2. Entity Sets and Attributes

### 2.1 What is an Entity?

An **entity** represents a real-world object or concept that can be uniquely identified. An **entity set** is a collection of similar entities that share the same properties or attributes.

**Examples:**
- `STUDENT` — represents all students in the university
- `COURSE` — represents all courses offered
- `INSTRUCTOR` — represents all faculty members

### 2.2 Types of Attributes

#### Simple (Atomic) Attributes
Simple attributes cannot be divided further into meaningful components.

```
Student: {Student_ID, Name, Age, Gender}
```

#### Composite Attributes
Composite attributes can be broken down into smaller sub-attributes.

```
Address: {Street, City, State, PinCode}
Name: {FirstName, MiddleName, LastName}
```

In ER diagrams, composite attributes are shown with their component attributes connected below them.

#### Single-Valued vs Multi-Valued Attributes

| Attribute Type | Description | Example |
|----------------|-------------|---------|
| Single-Valued | Contains only one value | Student_ID, Age |
| Multi-Valued | Can contain multiple values | PhoneNumbers, EmailAddresses |

In Chen notation, multi-valued attributes are represented by **double ellipses** (oval shapes).

#### Derived Attributes
Derived attributes are those whose values can be calculated from other attributes.

```
Age can be derived from DateOfBirth
TotalCredits can be derived from sum of enrolled course credits
```

Derived attributes are represented by **dashed ellipses** in ER diagrams.

#### Key Attributes
Key attributes uniquely identify an entity within an entity set. A key attribute cannot have null values and must contain unique values.

```
Student_ID (Primary Key for STUDENT entity)
Course_ID (Primary Key for COURSE entity)
```

Key attributes are typically underlined in ER diagrams.

### 2.3 Entity Set Notation (Chen Notation)

```
    +---------------+
    |    STUDENT    |
    +---------------+
    | Student_ID(PK)|  ← Key attribute (underlined)
    | First_Name    |  ← Simple attribute
    | Last_Name     |  ← Simple attribute
    | Date_of_Birth |  ← Simple attribute
    | Email         |  ← Simple attribute
    | Phone#        |  ← Multi-valued attribute (double oval)
    | Age           |  ← Derived attribute (dashed)
    +---------------+
```

---

## 3. Relationship Sets and Relationship Types

### 3.1 Understanding Relationships

A **relationship** describes an association between two or more entities. A **relationship set** is a collection of relationships of the same type.

**Example:**
The relationship `ENROLLED_IN` connects `STUDENT` and `COURSE` entities, representing which students are enrolled in which courses.

### 3.2 Degree of a Relationship

The degree of a relationship refers to the number of entity sets participating in the relationship.

| Degree | Description | Example |
|--------|-------------|---------|
| Unary (Recursive) | One entity set relates to itself | Employee manages Employee |
| Binary | Two entity sets relate to each other | Student enrolls in Course |
| Ternary | Three entity sets relate together | Student enrolls in Course under Instructor |
| N-ary | Multiple entity sets relate | Complex multi-party relationships |

### 3.3 Types of Relationship Sets

#### Unary Relationship Example (Self-Referencing)

```
EMPLOYEE ---- manages ---- EMPLOYEE
```

An employee can manage other employees, and each employee is managed by another employee (except the top-level manager).

#### Binary Relationship Example

```
STUDENT ---- enrolls_in ---- COURSE
```

#### Ternary Relationship Example

```
STUDENT ---- registers ---- COURSE
      |                      |
      +---- INSTRUCTOR -------+
```

A ternary relationship `REGISTERS` involves three entities: Student, Course, and Instructor.

---

## 4. Cardinality Ratios

**Cardinality** defines the number of instances of one entity that can be associated with a single instance of another entity. This is a crucial concept for Delhi University exams.

### 4.1 Types of Cardinality

#### One-to-One (1:1)

Each entity in entity set A is associated with exactly one entity in entity set B, and vice versa.

**Example:**
```
DEPARTMENT ---- has ---- HEAD
```

Each department has exactly one head, and each faculty member is head of exactly one department.

```
      1                   1
DEPARTMENT ------------ HEAD
```

#### One-to-Many (1:N) or Many-to-One (N:1)

One entity in A can be associated with multiple entities in B, but each entity in B is associated with only one entity in A.

**Example:**
```
INSTRUCTOR ---- teaches ---- COURSE
```

One instructor can teach many courses, but each course is taught by exactly one instructor.

```
      1                   N
INSTRUCTOR ------------ COURSE
```

#### Many-to-Many (M:N)

Multiple entities in A can be associated with multiple entities in B.

**Example:**
```
STUDENT ---- enrolls_in ---- COURSE
```

A student can enroll in many courses, and a course can have many students enrolled.

```
      M                   N
STUDENT ------------ COURSE
```

### 4.2 Visual Representation of Cardinality

| Cardinality | Chen Notation | Crow's Foot Notation |
|-------------|---------------|---------------------|
| One (1) | 1 | || (single line) |
| Many (N) | N | }| (crow's foot) |

---

## 5. Participation Constraints

Participation constraints determine whether the existence of an entity depends on its being related to another entity through a relationship.

### 5.1 Total Participation (Existence-Dependence)

An entity **must** participate in the relationship. Total participation is also called **existence dependency**.

**Symbol:** Double line (thick lines) in ER diagrams

**Example:**
```
STUDENT ---- enrolls_in ---- COURSE
```

Every student must enroll in at least one course. The participation of STUDENT in the `enrolls_in` relationship is total.

```
          TOTAL              PARTIAL
       +--------+          +--------+
       |        |          |        |
  STUDENT=======enrolls_in=======COURSE
       |        |          |        |
       +--------+          +--------+
```

### 5.2 Partial Participation

An entity **may or may not** participate in the relationship.

**Symbol:** Single line in ER diagrams

**Example:**
```
INSTRUCTER ---- teaches ---- COURSE
```

An instructor may teach courses (partial participation), but every course must be taught by an instructor (total participation).

### 5.3 Summary Table

| Constraint | Description | Notation |
|------------|-------------|----------|
| Total Participation | Every entity must participate | Double line |
| Partial Participation | Participation is optional | Single line |

---

## 6. Weak Entity Sets

A **weak entity set** is an entity that cannot be uniquely identified by its own attributes alone. It depends on a **identifying owner** entity.

### 6.1 Characteristics of Weak Entities

- Does not have a primary key of its own
- Identified by combining its own **partial key** with the primary key of its owner
- Existence-dependent on the owner (total participation in identifying relationship)
- Owner must have a one-to-many relationship with the weak entity

### 6.2 Example

```
        +-------------+          +-------------+
        |  DEPARTMENT |<--------|    COURSE   |
        +-------------+          +-------------+
        | Dept_ID(PK) |          | Course_No   |  ← Partial Key
        | Dept_Name   |          | Course_Name |
        +-------------+          | Credits     |
                                  +-------------+
```

Here, `COURSE` is a weak entity because:
- It has a partial key `Course_No`
- It is identified by combining `Course_No` with `Dept_ID` (from DEPARTMENT)
- Course depends on Department (total participation in identifying relationship)

In Chen notation, weak entities are represented by **double rectangles**, and the identifying relationship is shown with a **double diamond**.

---

## 7. Enhanced ER Diagrams (EER)

For the Delhi University curriculum, understanding Enhanced ER diagrams is important as they extend basic ER concepts.

### 7.1 Specialization

Specialization is the process of defining a set of subclasses of an entity type. An entity can belong to a specialized entity based on specific characteristics.

**Example:**
```
          EMPLOYEE
              |
    +---------+---------+
    |         |         |
PROFESSOR  TECHNICAL  ADMIN
```

`EMPLOYEE` is the superclass, and `PROFESSOR`, `TECHNICAL`, and `ADMIN` are subclasses.

### 7.2 Generalization

Generalization is the reverse process—combining common attributes of multiple entity types into a single superclass.

**Example:**
```
PROFESSOR    TECHNICAL    ADMIN
      \        |         /
       \       |        /
          EMPLOYEE
```

### 7.3 Aggregation

Aggregation treats a relationship as a higher-level entity, allowing relationships to participate in other relationships.

---

## 8. ER Diagram Notation Styles

### 8.1 Chen Notation

Named after Peter Chen, this classical notation uses:

- **Rectangles** for entity sets
- **Ellipses** for attributes
- **Diamonds** for relationships
- **Lines** to connect entities to relationships

### 8.2 Crow's Foot Notation (Most Popular in Industry)

This notation uses a "crow's foot" symbol to represent cardinality:

```
      ||---------------o<
    (One)          (Many)
```

### 8.3 UML Class Diagrams

Used in object-oriented design, UML diagrams represent:

- Classes as rectangles with three sections (name, attributes, methods)
- Associations as lines
- Multiplicity shown as numbers or asterisks

---

## 9. Comprehensive Examples

### Example 1: University Database

Let's design a complete ER diagram for a university management system:

**Entities:**
- `STUDENT` (Student_ID, Name, DOB, Address, Phone)
- `COURSE` (Course_ID, Course_Name, Credits)
- `INSTRUCTOR` (Instructor_ID, Name, Specialization, Salary)
- `DEPARTMENT` (Dept_ID, Dept_Name, Budget)

**Relationships:**
- `STUDENT` enrolls in `COURSE` (M:N cardinality, with attributes: EnrollmentDate, Grade)
- `INSTRUCTOR` teaches `COURSE` (1:N cardinality)
- `DEPARTMENT` has `INSTRUCTOR` (1:N cardinality)
- `DEPARTMENT` offers `COURSE` (1:N cardinality)

**ER Diagram (Conceptual):**

```
           M           N
    STUDENT -------- enrolls_in -------- COURSE
      |                                      ^
      |                                      |
      |           1                      N  |
      +----------- teaches --------------+--+
      |
      |           1                       N
    INSTRUCTOR -------- belongs_to -------- DEPARTMENT
```

**SQL Implementation:**

```sql
-- Create tables based on ER diagram
CREATE TABLE DEPARTMENT (
    Dept_ID INT PRIMARY KEY,
    Dept_Name VARCHAR(50),
    Budget DECIMAL(10,2)
);

CREATE TABLE INSTRUCTOR (
    Instructor_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Specialization VARCHAR(50),
    Salary DECIMAL(10,2),
    Dept_ID INT,
    FOREIGN KEY (Dept_ID) REFERENCES DEPARTMENT(Dept_ID)
);

CREATE TABLE COURSE (
    Course_ID INT PRIMARY KEY,
    Course_Name VARCHAR(50),
    Credits INT,
    Dept_ID INT,
    Instructor_ID INT,
    FOREIGN KEY (Dept_ID) REFERENCES DEPARTMENT(Dept_ID),
    FOREIGN KEY (Instructor_ID) REFERENCES INSTRUCTOR(Instructor_ID)
);

CREATE TABLE STUDENT (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    DOB DATE,
    Address VARCHAR(200),
    Phone VARCHAR(20)
);

-- Junction table for M:N relationship
CREATE TABLE ENROLLMENTS (
    Student_ID INT,
    Course_ID INT,
    EnrollmentDate DATE,
    Grade CHAR(2),
    PRIMARY KEY (Student_ID, Course_ID),
    FOREIGN KEY (Student_ID) REFERENCES STUDENT(Student_ID),
    FOREIGN KEY (Course_ID) REFERENCES COURSE(Course_ID)
);
```

### Example 2: Library Management System

**Entities:**
- `MEMBER` (Member_ID, Name, Address, Join_Date)
- `BOOK` (Book_ID, Title, ISBN, Publication_Year)
- `AUTHOR` (Author_ID, Name, Biography)
- `PUBLISHER` (Publisher_ID, Name, Address)

**Relationships:**
- `BOOK` is written by `AUTHOR` (M:N - a book can have multiple authors)
- `PUBLISHER` publishes `BOOK` (1:N)
- `MEMBER` borrows `BOOK` (M:N with attributes: Borrow_Date, Due_Date, Return_Date)

**ER Diagram Attributes Detail:**

```
MEMBER
├── Member_ID (PK)
├── Name
├── Address
└── Join_Date

BOOK
├── Book_ID (PK)
├── Title
├── ISBN
├── Publication_Year
└── Publisher_ID (FK)

AUTHOR
├── Author_ID (PK)
├── Name
└── Biography

BORROWS (Relationship with attributes)
├── Borrow_Date
├── Due_Date
└── Return_Date
```

**SQL Implementation:**

```sql
CREATE TABLE PUBLISHER (
    Publisher_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Address VARCHAR(200)
);

CREATE TABLE AUTHOR (
    Author_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Biography TEXT
);

CREATE TABLE BOOK (
    Book_ID INT PRIMARY KEY,
    Title VARCHAR(200),
    ISBN VARCHAR(13),
    Publication_Year INT,
    Publisher_ID INT,
    FOREIGN KEY (Publisher_ID) REFERENCES PUBLISHER(Publisher_ID)
);

-- Junction table for M:N between BOOK and AUTHOR
CREATE TABLE BOOK_AUTHOR (
    Book_ID INT,
    Author_ID INT,
    PRIMARY KEY (Book_ID, Author_ID),
    FOREIGN KEY (Book_ID) REFERENCES BOOK(Book_ID),
    FOREIGN KEY (Author_ID) REFERENCES AUTHOR(Author_ID)
);

CREATE TABLE MEMBER (
    Member_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Address VARCHAR(200),
    Join_Date DATE
);

CREATE TABLE BORROWS (
    Member_ID INT,
    Book_ID INT,
    Borrow_Date DATE,
    Due_Date DATE,
    Return_Date DATE,
    PRIMARY KEY (Member_ID, Book_ID, Borrow_Date),
    FOREIGN KEY (Member_ID) REFERENCES MEMBER(Member_ID),
    FOREIGN KEY (Book_ID) REFERENCES BOOK(Book_ID)
);
```

---

## 10. Key Takeaways

1. **ER Diagrams** are essential tools for conceptual database design, providing a visual representation of data and relationships.

2. **Entities** are objects that can be identified uniquely, represented by rectangles in Chen notation.

3. **Attributes** describe properties of entities:
   - Simple vs Composite
   - Single-valued vs Multi-valued
   - Derived (dashed ellipse)
   - Key attributes (underlined)

4. **Relationships** describe associations between entities:
   - Degree: Unary, Binary, Ternary, N-ary
   - Cardinality: 1:1, 1:N, M:N

5. **Participation Constraints**:
   - Total participation (double line) - mandatory
   - Partial participation (single line) - optional

6. **Weak Entities** (double rectangle) depend on owner entities and use partial keys for identification.

7. **ER Diagram Notations**: Chen notation, Crow's foot notation, and UML class diagrams each have their own symbols and applications.

8. **Practical Application**: ER diagrams translate directly into SQL table structures, with relationships becoming foreign keys or junction tables.

---

## References for Delhi University Syllabus

This content aligns with the **Database Management Systems** paper for BSc (Hons) Computer Science under NEP 2024 UGCF. Key topics to focus on for examinations include:

- Entity-Relationship modeling
- Cardinality and participation constraints
- Weak entity sets
- Conversion of ER diagrams to relational schema

**Recommended Further Reading:**
- "Database System Concepts" by Korth and Silberschatz
- "Fundamentals of Database Systems" by Elmasri and Navathe

---

*This comprehensive study material covers all essential topics for ER Diagram Notation as required by the Delhi University curriculum.*