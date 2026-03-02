# Relations, Keys, and Integrity Constraints

## Introduction

The **Relational Model**, introduced by Edgar F. Codd in 1970, forms the foundation of modern database management systems. This model represents data in the form of **relations** (tables), making it intuitively easy to understand while being mathematically rigorous. In the context of University of Delhi's Computer Science curriculum, understanding relations, keys, and integrity constraints is essential for designing robust databases and passing competitive examinations like CUET-PG and other placement tests.

The relational model organizes data into **tables** (relations) consisting of rows (tuples) and columns (attributes). Each table has a specific structure defined by its **schema**, which specifies the table name, attribute names, and their respective domains. The actual data stored in the table at any given moment is called the **instance** or **state** of the relation. 

**Keys** play a pivotal role in the relational model by providing unique identification of records and establishing relationships between tables. Without proper keys, databases would become chaotic collections of unidentifiable data. **Integrity Constraints** ensure that data remains accurate, consistent, and valid throughout its lifecycle. These constraints act as guardians of data quality, preventing erroneous or meaningless data from entering the system. Together, keys and integrity constraints form the backbone of relational database design, enabling efficient querying, data retrieval, and maintaining data integrity.

## Key Concepts

### 1. Relations: The Building Blocks

A **relation** is a two-dimensional table that satisfies certain properties:

- **Atomic Values**: Each cell contains a single, atomic (indivisible) value. Relations that satisfy this property are said to be in **First Normal Form (1NF)**.
- **Unique Column Names**: Each column (attribute) has a distinct name within the relation.
- **Unique Row Identifiers**: Each row (tuple) is unique; no duplicate rows exist.
- **Order Independence**: The order of rows and columns is immaterial; they do not affect the meaning of the data.

**Notation**: A relation R with attributes A1, A2, ..., An is denoted as R(A1, A2, ..., An). For example, STUDENT(RollNo, Name, Age, Course) defines a relation named STUDENT with four attributes.

### 2. Types of Keys

Keys are fundamental to database design and come in several varieties, each serving a specific purpose:

**Super Key**: A set of one or more attributes that uniquely identifies a tuple in a relation. A super key can have redundant attributes. For instance, in a STUDENT relation, {RollNo}, {Name, Email}, and {RollNo, Name, Age} are all super keys because they can uniquely identify students.

**Candidate Key**: A minimal super key—that is, a super key without any proper subset that is also a super key. Candidate keys represent the "true" identifiers for a relation. Between multiple candidate keys, one is chosen as the **Primary Key**. For example, in STUDENT(RollNo, AadharNo, Name, Email), both RollNo and AadharNo could be candidate keys, but only one becomes the primary key.

**Primary Key**: The selected candidate key used to uniquely identify tuples in a relation. It cannot contain NULL values and must have unique values. Primary keys enforce **entity integrity**, ensuring each record is identifiable. In MySQL, you define a primary key as: `PRIMARY KEY (RollNo)`.

**Alternate Key**: Any candidate key that is not selected as the primary key. These become alternative ways to identify records. Using the previous example, if RollNo is the primary key, then AadharNo is the alternate key.

**Foreign Key**: An attribute (or set of attributes) in one relation that references the primary key of another relation (or sometimes the same relation). Foreign keys establish **referential integrity** between related tables. For instance, in a ENROLLMENT(RollNo, CourseID, Grade) relation, RollNo references the STUDENT table's primary key, establishing a relationship between these tables.

**Composite Key**: A key consisting of two or more attributes that together uniquely identify a tuple. Neither attribute alone can serve as a key. For example, in ORDER_ITEMS(OrderID, ProductID, Quantity), the combination of OrderID and ProductID uniquely identifies each item, as a single order can contain multiple products.

**Unique Key**: Similar to a primary key, but allows one NULL value and can have multiple unique keys in a table. Unlike primary keys, unique keys may not necessarily represent the main identifier. In Oracle: `UNIQUE (Email)`.

### 3. Integrity Constraints

Integrity constraints are rules that maintain the correctness and validity of data in a database:

**Domain Integrity (Null Integrity)**: Ensures that all attributes in a relation have values from their defined domains (data types and constraints). Every attribute must either have a valid value or be explicitly marked as NULL (if allowed). Domain integrity is enforced through:
- Data type specifications (INT, VARCHAR, DATE)
- Constraints like CHECK, DEFAULT
- Domain definitions in the schema

For example: `Age INT CHECK (Age >= 0 AND Age <= 150)` ensures age values remain within a valid range.

**Entity Integrity**: States that the primary key cannot contain NULL values. Since the primary key uniquely identifies each tuple, a NULL primary key would make it impossible to identify that tuple. This constraint ensures every record in a table is identifiable.

**Referential Integrity**: Maintains consistency between related tables. If a foreign key references a primary key in another table, the referenced value must either exist in that table or be NULL. This prevents "orphaned" records—records that reference non-existent data. In SQL, referential integrity is enforced through FOREIGN KEY constraints:

```sql
CREATE TABLE ENROLLMENT (
    RollNo INT,
    CourseID VARCHAR(10),
    Grade CHAR(1),
    FOREIGN KEY (RollNo) REFERENCES STUDENT(RollNo),
    FOREIGN KEY (CourseID) REFERENCES COURSE(CourseID)
);
```

When you attempt to delete a student who has enrollment records, the database will either:
- Reject the deletion (NO ACTION)
- Cascade the deletion (CASCADE)
- Set the foreign key to NULL (SET NULL)

**User-Defined Integrity**: Domain-specific rules defined by users or application requirements. These include:
- Business rules (e.g., "Employee salary cannot exceed manager's salary")
- Enterprise constraints (e.g., "Only final year students can register for placement drives")

**Key Constraints**: The uniqueness property, ensuring no two tuples have the same values for the key attributes. This is enforced through PRIMARY KEY and UNIQUE constraints.

**Null Constraints**: Specified at the attribute level to indicate whether NULL values are permitted. Primary key columns automatically have NOT NULL constraint.

## Examples

### Worked Example 1: Identifying Keys in a Relation

Consider the relation: `EMPLOYEE(EmpID, SSN, Name, DepartmentID, Email)`

**Solution:**
- **Super Keys**: {EmpID}, {SSN}, {Email}, {EmpID, Name}, {SSN, DepartmentID}, {EmpID, Name, Email}, and so on.
- **Candidate Keys**: {EmpID} and {SSN} are minimal super keys (neither can be reduced further). Email could be a candidate key if we guarantee every employee has a unique email.
- **Primary Key**: Choose EmpID (common practice as it's shorter and internally generated).
- **Alternate Keys**: SSN and Email (if unique) become alternate keys.

### Worked Example 2: Referential Integrity Demonstration

Consider two tables:

```sql
CREATE TABLE DEPARTMENT (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50)
);

CREATE TABLE EMPLOYEE (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    DeptID INT,
    FOREIGN KEY (DeptID) REFERENCES DEPARTMENT(DeptID)
);
```

If we attempt:
```sql
INSERT INTO EMPLOYEE VALUES (101, 'Amit', 99);  -- Assuming DeptID 99 doesn't exist
```

This will fail because DeptID 99 violates referential integrity—no such department exists in the DEPARTMENT table.

### Worked Example 3: CHECK Constraint Implementation

Create a relation ensuring data validity:

```sql
CREATE TABLE STUDENT (
    RollNo INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Age INT CHECK (Age >= 18 AND Age <= 30),
    Gender CHAR(1) CHECK (Gender IN ('M', 'F', 'O')),
    Email VARCHAR(100) UNIQUE
);
```

This enforces:
- Entity integrity: RollNo is primary key (NOT NULL, UNIQUE)
- Domain integrity: Age must be between 18-30, Gender must be M/F/O
- Key constraint: Email must be unique
- Null constraint: Name cannot be NULL

## Exam Tips

1. **Distinguish between Super Key and Candidate Key**: Remember that a candidate key is a minimal super key—if you can remove any attribute and still have a unique identifier, it's a candidate key.

2. **Primary Key vs. Foreign Key**: Primary keys identify records within a table; foreign keys establish relationships between tables. A table can have multiple foreign keys but only one primary key.

3. **NULL Handling**: Primary keys cannot be NULL; foreign keys can be NULL (representing no relationship). Remember that NULL ≠ 0 or empty string.

4. **Cascading Actions**: Understand the referential integrity actions—CASCADE, SET NULL, NO ACTION, and RESTRICT—as these frequently appear in exam questions.

5. **Entity vs. Referential Integrity**: Entity integrity applies to primary keys (no NULLs). Referential integrity applies to foreign keys (must match referenced primary key or be NULL).

6. **Composite Key Usage**: When using composite keys, remember the entire combination must be unique—not each attribute individually.

7. **Practical SQL Knowledge**: Be familiar with PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, and CHECK constraints in SQL, as DU exams often include practical queries.

8. **Real-World Example**: Always relate concepts to real scenarios—Aadhar number as candidate key, course enrollment linking students and courses, etc.