# Concept of Relations and Keys in DBMS

## Introduction

The relational model, introduced by Edgar F. Codd in 1970, forms the foundation of modern database management systems. This model represents data in the form of relations (tables), where each relation consists of tuples (rows) and attributes (columns). Understanding relations and keys is fundamental to mastering database design, normalization, and query processing—core topics in the University of Delhi's Computer Science curriculum.

In the context of CUET-qualified DU students, a thorough grasp of relations and keys is essential because these concepts appear consistently in both internal assessments and end-semester examinations. Keys serve as the backbone of data integrity, ensuring that each record can be uniquely identified and that relationships between tables can be established efficiently. This topic also connects directly to advanced concepts like functional dependencies and normalization forms, making it a critical building block for your entire database knowledge.

## Key Concepts

### 1. Relation: The Foundation of Relational Database

A **relation** is a two-dimensional table that organizes data into rows and columns. In database terminology:

- **Tuple**: A single row in a relation, representing one record
- **Attribute**: A column in a relation, representing a property of an entity
- **Degree**: The number of attributes (columns) in a relation
- **Cardinality**: The number of tuples (rows) in a relation

For example, consider a STUDENT relation:

| Roll_No | Name | Age | Course |
|---------|------|-----|--------|
| 001 | Rahul Sharma | 20 | B.Sc. CS |
| 002 | Priya Singh | 19 | B.Sc. CS |
| 003 | Amit Kumar | 21 | B.A. Eco |

This relation has degree 4 (4 attributes) and cardinality 3 (3 tuples).

### 2. Properties of a Relation

A valid relation in the relational model must satisfy the following properties:

- **Atomic Values**: Each cell must contain a single, indivisible value (First Normal Form)
- **Unique Attribute Names**: All attribute names within a relation must be unique
- **No Duplicate Tuples**: No two rows can be identical
- **Order is Insignificant**: The order of rows and columns does not affect the data
- **Same Domain**: Attributes in the same column must have values from the same domain

### 3. Keys: Types and Characteristics

Keys are essential for identifying unique tuples and establishing relationships between relations.

#### Super Key
A **super key** is a set of one or more attributes that can uniquely identify a tuple in a relation. The combination of {Roll_No} and {Roll_No, Name} are both super keys in the STUDENT relation.

#### Candidate Key
A **candidate key** is a minimal super key—no proper subset of candidate key attributes can be a super key. In STUDENT, if Roll_No is unique for each student, it is a candidate key. If there is also a unique Aadhar_No, then both are candidate keys.

#### Primary Key
The **primary key** is the selected candidate key used to uniquely identify tuples in a relation. It cannot contain NULL values and must have unique values. In STUDENT, Roll_No would typically be the primary key.

**Rules for Primary Key:**
- Must have a unique value for each tuple
- Cannot be NULL
- Should be stable (rarely changed)
- Preferably single attribute rather than composite

#### Alternate Key
Any candidate key not chosen as the primary key is called an **alternate key** or secondary key. If Roll_No is primary and Aadhar_No is another candidate, Aadhar_No becomes the alternate key.

#### Composite Key
When a single attribute cannot uniquely identify a tuple, we combine multiple attributes to form a **composite key**. For example, in an ENROLLMENT relation:

| Student_ID | Course_ID | Semester | Grade |
|------------|-----------|----------|-------|
| 001 | CS101 | Fall 2024 | A |
| 001 | CS102 | Fall 2024 | B |
| 002 | CS101 | Fall 2024 | A |

Here, {Student_ID, Course_ID} together form the composite primary key because neither attribute alone can uniquely identify an enrollment record.

#### Foreign Key
A **foreign key** is an attribute in one relation that references the primary key of another relation, establishing a relationship between the two tables. Consider:

STUDENT (Primary Key: Roll_No)
| Roll_No | Name | Dept_ID |
|---------|------|---------|
| 001 | Rahul | CS01 |
| 002 | Priya | CS02 |

DEPARTMENT (Primary Key: Dept_ID)
| Dept_ID | Dept_Name |
|---------|-----------|
| CS01 | Computer Science |
| CS02 | Mathematics |

Here, Dept_ID in STUDENT is a foreign key referencing the primary key of DEPARTMENT.

**Referential Integrity Rules:**
- A foreign key value must either match a primary key value in the referenced table or be NULL
- Cannot reference a non-existent primary key value
- When referenced primary key is deleted, appropriate action (cascade, set null, restrict) must be taken

#### Unique Key
A **unique key** is similar to primary key but allows one NULL value. It ensures all non-NULL values are unique. Unlike primary key, a table can have multiple unique keys.

### 4. Keys in Relational Algebra

Keys play a crucial role in relational algebra operations:

- **Selection (σ)**: Used to select specific tuples based on conditions
- **Projection (π)**: Used to select specific columns/attributes
- **Join (⋈)**: Combines relations based on common attributes, often using primary key-foreign key relationships

### 5. Integrity Constraints

#### Entity Integrity
The primary key cannot contain NULL values. This ensures each tuple can be uniquely identified.

#### Referential Integrity
Foreign key values must reference existing primary key values in the referenced relation, or be NULL.

#### Domain Integrity
All attributes must have values from the defined domain (data type, format, constraints).

## Examples

### Example 1: Identifying Keys in Employee Relation

Consider an EMPLOYEE relation:

| Emp_ID | Email | Phone | Dept_Code | Salary |
|--------|-------|-------|-----------|--------|
| E001 | rahul@email.com | 9876543210 | D01 | 50000 |
| E002 | priya@email.com | 9876543211 | D02 | 55000 |
| E003 | amit@email.com | 9876543212 | D01 | 45000 |

**Solution:**

- **Super Keys**: {Emp_ID}, {Email}, {Emp_ID, Phone}, {Email, Dept_Code}, {Emp_ID, Email}, and many more combinations
- **Candidate Keys**: {Emp_ID} (unique, minimal), {Email} (unique, minimal)
- **Primary Key**: Choose Emp_ID (commonly used as primary key)
- **Alternate Key**: Email
- **Foreign Key**: Dept_Code (if referencing a DEPARTMENT table)

### Example 2: Composite Key Scenario

Consider a BOOK_AUTHORS relation:

| ISBN | Author_ID | Author_Name | Royalty_Percent |
|------|-----------|-------------|-----------------|
| 978-1 | A001 | R.K. Narayan | 10% |
| 978-1 | A002 | Author 2 | 8% |
| 978-2 | A001 | R.K. Narayan | 12% |

**Solution:**

- **Why Composite Key?** A single ISBN cannot identify the tuple uniquely because one book can have multiple authors. Similarly, a single Author_ID cannot identify because one author can write multiple books.
- **Primary Key**: {ISBN, Author_ID} - together they uniquely identify each record
- This relation is in First Normal Form (atomic values) but may require normalization for higher normal forms

### Example 3: Foreign Key and Referential Integrity

Consider two relations:

BOOK (Primary Key: Book_ID)
| Book_ID | Title | Publisher_ID |
|---------|-------|--------------|
| B001 | DBMS Concepts | P001 |
| B002 | Data Structures | P002 |

PUBLISHER (Primary Key: Publisher_ID)
| Publisher_ID | Publisher_Name |
|-------------|----------------|
| P001 | Pearson |
| P002 | McGraw Hill |

**Scenario 1: Inserting a book with non-existent publisher**
```sql
INSERT INTO BOOK VALUES ('B003', 'Python', 'P005');
```
This violates referential integrity because P005 does not exist in PUBLISHER.

**Scenario 2: Deleting a publisher with existing books**
```sql
DELETE FROM PUBLISHER WHERE Publisher_ID = 'P001';
```
Options:
- RESTRICT: Delete fails if books exist
- CASCADE: Books are also deleted
- SET NULL: Book's Publisher_ID becomes NULL
- SET DEFAULT: Book's Publisher_ID becomes default value

## Exam Tips

1. **Remember the key hierarchy**: Super Key → Candidate Key → Primary Key. Every primary key is a candidate key, and every candidate key is a super key.

2. **Primary vs Unique Key**: Primary key allows NO NULL values and only one per table; Unique key allows ONE NULL value and multiple per table.

3. **Composite Key Formula**: Use composite key when no single attribute can uniquely identify tuples, but their combination can.

4. **Foreign Key Purpose**: Remember that foreign keys establish relationships between tables and enforce referential integrity.

5. **Integrity Constraints**: Know the difference between entity integrity (primary key not NULL) and referential integrity (foreign key references valid primary key).

6. **Normalization Connection**: Keys are fundamental to normalization—determining candidate keys helps identify normal forms.

7. **Relational Algebra**: Understand how keys are used in JOIN operations—the common attributes are typically primary key-foreign key pairs.

8. **NULL Handling**: Remember that NULL ≠ 0 or empty string; NULL represents missing or unknown information.

9. **Minimality Rule**: For candidate keys, ensure no proper subset can uniquely identify tuples—this is frequently tested in exams.

10. **Real-world Examples**: Be prepared to identify keys in practical scenarios like library management, hospital records, or bank transactions.