# ER to Relational Mapping: Comprehensive Study Material

## Database Management Systems — BSc (Hons) Computer Science (NEP 2024 UGCF)

---

## 1. Introduction

**Entity-Relationship (ER) to Relational Mapping** is a fundamental concept in Database Management Systems that bridges the gap between the conceptual design phase and the physical implementation of a database. This process transforms the high-level ER diagram (which uses entities, attributes, and relationships) into a set of relational schemas that can be directly implemented in relational database management systems (RDBMS) like MySQL, PostgreSQL, or Oracle.

### Real-World Relevance

In practical database development, organizations first design their data requirements using ER diagrams—these are intuitive and help stakeholders understand the data structure without technical complexity. However, relational databases require data to be organized in tables with rows and columns. ER-to-relational mapping is the critical translation step that ensures:

- **Data integrity** is preserved during transformation
- **Business requirements** captured in ER diagrams are accurately represented
- **Database performance** is optimized through proper schema design
- **SQL implementation** can proceed efficiently

For Delhi University students, this topic is essential as it forms the foundation for database design and implementation, appearing frequently in examinations and practical assignments.

---

## 2. Understanding the Two Models

### 2.1 Entity-Relationship (ER) Model

The ER model represents data as:

- **Entities**: Objects with independent existence (e.g., STUDENT, COURSE)
- **Attributes**: Properties of entities (e.g., student_name, enrollment_date)
- **Relationships**: Associations between entities (e.g., STUDENT enrolls in COURSE)

### 2.2 Relational Model

The relational model represents data as:

- **Relations (Tables)**: Collection of tuples (rows) with attributes (columns)
- **Primary Key**: Unique identifier for each tuple
- **Foreign Key**: Reference to primary key in another relation

---

## 3. Step-by-Step Mapping Process

The mapping from ER to relational model follows a systematic approach:

```
ER Model → Relational Model
     │
     ├─→ Step 1: Map Strong Entities
     ├─→ Step 2: Map Weak Entities
     ├─→ Step 3: Map Attributes
     ├─→ Step 4: Map Relationships
     └─→ Step 5: Handle Constraints
```

---

## 4. Mapping Entity Types

### 4.1 Strong Entity Types

A strong entity has a primary key and exists independently. **Mapping rules:**

- Create a separate relation (table) for each strong entity
- Include all simple attributes
- The primary key of the ER entity becomes the primary key of the relation

**Example: STUDENT Entity**

| ER Attribute | Relational Attribute |
|--------------|---------------------|
| student_id (PK) | student_id |
| student_name | student_name |
| date_of_birth | date_of_birth |
| major | major |

**SQL Implementation:**

```sql
CREATE TABLE STUDENT (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    major VARCHAR(50)
);
```

### 4.2 Weak Entity Types

A weak entity depends on a strong entity and doesn't have a complete primary key. **Mapping rules:**

- Create a separate relation for the weak entity
- Include all attributes (both partial key and non-key attributes)
- The primary key is formed by combining the partial key with the foreign key referencing the owner entity

**Example: DEPENDENT Entity (weak to EMPLOYEE)**

| ER Attribute | Relational Attribute |
|--------------|---------------------|
| dependent_name (partial key) | dependent_name |
| relationship | relationship |
| EMPLOYEE (owner) → emp_id (FK) | emp_id |

**SQL Implementation:**

```sql
CREATE TABLE DEPENDENT (
    emp_id INT,
    dependent_name VARCHAR(100),
    relationship VARCHAR(50),
    PRIMARY KEY (emp_id, dependent_name),
    FOREIGN KEY (emp_id) REFERENCES EMPLOYEE(emp_id)
);
```

---

## 5. Mapping Attributes

### 5.1 Simple Attributes

Simple attributes map directly to columns in the relation.

**Example: age (simple attribute) → age column**

### 5.2 Composite Attributes

Composite attributes are broken down into their constituent simple attributes.

**Example: Address (street, city, state, zip_code)**

```
ER: Address → {street, city, state, zip_code}
Relational: street, city, state, zip_code (four separate columns)
```

### 5.3 Multi-Valued Attributes

Multi-valued attributes require special handling due to the First Normal Form (1NF) requirement that columns contain atomic values. **Mapping rules:**

- Create a separate relation for the multi-valued attribute
- Include the primary key of the entity as a foreign key
- The primary key of the new relation is the combination of the foreign key and the multi-valued attribute

**Example: phone_number (multi-valued for STUDENT)**

**SQL Implementation:**

```sql
-- Main STUDENT table (without phone_number)
CREATE TABLE STUDENT (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    major VARCHAR(50)
);

-- Separate relation for multi-valued attribute
CREATE TABLE STUDENT_PHONE (
    student_id INT,
    phone_number VARCHAR(15),
    PRIMARY KEY (student_id, phone_number),
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id)
);
```

### 5.4 Derived Attributes

Derived attributes are computed from other stored attributes and should **not** be stored in the database. **Mapping rules:**

- Do NOT create a column for derived attributes
- They can be computed at query time using SQL functions

**Example: age can be derived from date_of_birth**

```sql
-- Don't store age, compute it:
SELECT student_name, 
       TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) AS age 
FROM STUDENT;
```

---

## 6. Mapping Relationship Types

The mapping approach depends on the **cardinality** of the relationship (1:1, 1:N, or N:M).

### 6.1 One-to-One (1:1) Relationships

For 1:1 relationships, there are three possible mapping strategies:

**Strategy A: Foreign Key Approach**

- Choose one entity as the "referencing" side
- Add the primary key of one entity as a foreign key in the other relation
- Include all attributes of the relationship

**Example: PROFESSOR manages DEPARTMENT (1:1)**

```sql
-- Option 1: Add dept_id to PROFESSOR
CREATE TABLE PROFESSOR (
    prof_id INT PRIMARY KEY,
    prof_name VARCHAR(100),
    dept_id INT UNIQUE,  -- UNIQUE ensures 1:1
    FOREIGN KEY (dept_id) REFERENCES DEPARTMENT(dept_id)
);

CREATE TABLE DEPARTMENT (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100)
);
```

**Strategy B: Merge the entities**

- If both entities are closely related and have similar lifecycles, they can be merged into a single table

**Strategy C: Cross-reference table**

- Create a separate relation containing primary keys of both entities

### 6.2 One-to-Many (1:N) Relationships

The "many" side receives the foreign key reference.

**Example: DEPARTMENT has EMPLOYEES (1:N)**

```sql
CREATE TABLE DEPARTMENT (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100)
);

CREATE TABLE EMPLOYEE (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    dept_id INT,  -- Foreign key at "many" side
    FOREIGN KEY (dept_id) REFERENCES DEPARTMENT(dept_id)
);
```

### 6.3 Many-to-Many (N:M) Relationships

N:M relationships **require a separate junction (associative) relation**.

**Example: STUDENT enrolls in COURSE (N:M)**

```sql
CREATE TABLE STUDENT (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100)
);

CREATE TABLE COURSE (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100)
);

-- Junction table for N:M relationship
CREATE TABLE ENROLLMENT (
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(2),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id),
    FOREIGN KEY (course_id) REFERENCES COURSE(course_id)
);
```

---

## 7. Recursive (Unary) Relationships

A recursive relationship occurs when an entity relates to itself. The mapping requires adding a foreign key that references the same table's primary key.

### 7.1 One-to-One Recursive

**Example: EMPLOYEE manages EMPLOYEE**

```sql
CREATE TABLE EMPLOYEE (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    manager_id INT,  -- References emp_id of same table
    FOREIGN KEY (manager_id) REFERENCES EMPLOYEE(emp_id)
);
```

### 7.2 One-to-Many Recursive

**Example: CATEGORY contains sub-categories**

```sql
CREATE TABLE CATEGORY (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100),
    parent_category_id INT,  -- Self-referencing foreign key
    FOREIGN KEY (parent_category_id) REFERENCES CATEGORY(category_id)
);
```

### 7.3 Many-to-Many Recursive

**Example: STUDENT tutors other STUDENTs**

```sql
CREATE TABLE STUDENT (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100)
);

CREATE TABLE TUTORSHIP (
    tutor_id INT,
    tutee_id INT,
    hours_per_week INT,
    PRIMARY KEY (tutor_id, tutee_id),
    FOREIGN KEY (tutor_id) REFERENCES STUDENT(student_id),
    FOREIGN KEY (tutee_id) REFERENCES STUDENT(student_id)
);
```

---

## 8. Participation Constraints

Participation constraints define whether the existence of an entity depends on its association with another entity.

### 8.1 Total Participation (Existence Dependent)

If every entity in an entity set must participate in the relationship, it's **total participation**. This is represented by a double line in ER diagrams.

**Mapping:** The foreign key cannot be NULL.

**Example: Every STUDENT must enroll in at least one COURSE (total participation of STUDENT in Enrollment)**

```sql
CREATE TABLE ENROLLMENT (
    student_id INT NOT NULL,  -- NOT NULL indicates total participation
    course_id INT NOT NULL,
    enrollment_date DATE,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id),
    FOREIGN KEY (course_id) REFERENCES COURSE(course_id)
);
```

### 8.2 Partial Participation

Entities may or may not participate in the relationship. Foreign key can be NULL.

**Example: PROFESSOR may or may not manage a DEPARTMENT**

```sql
CREATE TABLE PROFESSOR (
    prof_id INT PRIMARY KEY,
    prof_name VARCHAR(100),
    dept_id INT,  -- Can be NULL (partial participation)
    FOREIGN KEY (dept_id) REFERENCES DEPARTMENT(dept_id)
);
```

### 8.3 Handling Total Participation with Weak Entities

When a weak entity has total participation with its owner:

```sql
-- DEPENDENT has total participation with EMPLOYEE
CREATE TABLE DEPENDENT (
    emp_id INT NOT NULL,  -- NOT NULL enforces total participation
    dependent_name VARCHAR(100),
    relationship VARCHAR(50),
    PRIMARY KEY (emp_id, dependent_name),
    FOREIGN KEY (emp_id) REFERENCES EMPLOYEE(emp_id) ON DELETE CASCADE
);
```

---

## 9. Complete Example with Full ER Diagram

### Scenario: University Database

**ER Diagram Components:**

- **STUDENT** (Strong Entity): student_id (PK), name, dob
- **COURSE** (Strong Entity): course_id (PK), course_name, credits
- **DEPARTMENT** (Strong Entity): dept_id (PK), dept_name
- **ENROLLMENT** (N:M relationship between STUDENT and COURSE): student_id, course_id, grade
- **PROFESSOR** (Strong Entity): prof_id (PK), name, dept_id (FK)
- **TEACHES** (1:N relationship: PROFESSOR teaches COURSE): prof_id, course_id
- **phone_numbers** (Multi-valued for STUDENT)
- **age** (Derived from dob for STUDENT)

### Complete SQL Schema

```sql
-- Strong Entity: DEPARTMENT
CREATE TABLE DEPARTMENT (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL
);

-- Strong Entity: STUDENT (excluding multi-valued and derived)
CREATE TABLE STUDENT (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    major VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES DEPARTMENT(dept_id)
);

-- Multi-valued attribute: phone_numbers
CREATE TABLE STUDENT_PHONE (
    student_id INT,
    phone_number VARCHAR(15),
    PRIMARY KEY (student_id, phone_number),
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id) ON DELETE CASCADE
);

-- Strong Entity: COURSE
CREATE TABLE COURSE (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits INT,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES DEPARTMENT(dept_id)
);

-- Strong Entity: PROFESSOR
CREATE TABLE PROFESSOR (
    prof_id INT PRIMARY KEY,
    prof_name VARCHAR(100) NOT NULL,
    salary DECIMAL(10, 2),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES DEPARTMENT(dept_id)
);

-- N:M Relationship: ENROLLMENT
CREATE TABLE ENROLLMENT (
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(2),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES COURSE(course_id) ON DELETE CASCADE
);

-- 1:N Relationship: TEACHES (mapped as attribute in COURSE)
ALTER TABLE COURSE ADD COLUMN prof_id INT;
ALTER TABLE COURSE ADD FOREIGN KEY (prof_id) REFERENCES PROFESSOR(prof_id);

-- View for derived attribute: age
CREATE VIEW STUDENT_AGE AS
SELECT student_id, student_name, 
       TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) AS age
FROM STUDENT;
```

---

## 10. Key Takeaways

1. **Strong Entities**: Map directly to relations with their primary key as the relation's primary key.

2. **Weak Entities**: Include the owner's primary key as a foreign key; composite primary key = (foreign key + partial key).

3. **Multi-Valued Attributes**: Create separate relations; primary key = (entity's PK + multi-valued attribute).

4. **Derived Attributes**: Do NOT store; compute at query time using SQL functions.

5. **1:1 Relationships**: Use foreign key in either entity or merge relations.

6. **1:N Relationships**: Add foreign key at the "many" side referencing the "one" side.

7. **N:M Relationships**: Create a separate junction table with composite primary key.

8. **Recursive Relationships**: Add self-referencing foreign key; for N:M, create separate associative relation.

9. **Participation Constraints**: Total participation → NOT NULL foreign key; Partial → nullable foreign key.

10. **Cardinality Enforcement**: Use UNIQUE constraint for 1:1, junction tables for N:M relationships.

---

## 11. Assessment Section

### Multiple Choice Questions (MCQs)

**MCQ-1 (Easy):** Which of the following is CORRECT regarding the mapping of a multi-valued attribute in ER to relational model?
- A) It is stored as a single column with multiple values
- B) A separate relation is created with the entity's primary key
- C) It is converted to a derived attribute
- D) It is ignored during mapping
- **Answer: B**

**MCQ-2 (Medium):** For a many-to-many relationship between entity A and entity B, which of the following is the correct mapping approach?
- A) Add foreign key in entity A's table
- B) Add foreign key in entity B's table
- C) Create a junction table with foreign keys referencing both A and B
- D) Merge both entities into a single table
- **Answer: C**

**MCQ-3 (Hard):** Consider a recursive relationship "EMPLOYEE manages EMPLOYEE" with cardinality 1:N (each employee is managed by one other employee, but a senior employee can manage multiple subordinates). What is the correct SQL representation?
- A) `manager_id VARCHAR(10)` with no foreign key constraint
- B) `manager_id INT FOREIGN KEY REFERENCES EMPLOYEE(emp_id)`
- C) `manager_id INT PRIMARY KEY`
- D) `managed_by INT UNIQUE`
- **Answer: B**

**MCQ-4 (Medium):** In an ER diagram, total participation of entity B in relationship R with entity A is represented by:
- A) Single line connecting B to R
- B) Double line connecting B to R
- C) Double diamond for R
- D) Weak entity symbol
- **Answer: B**

### Flashcards

**FC-1 (Easy):** What is the primary key in the relation created from a weak entity?
- **Answer:** The combination of the partial key from the weak entity and the primary key of the owner (strong) entity.

**FC-2 (Easy):** How are derived attributes handled in relational mapping?
- **Answer:** They are NOT stored in the database; they are computed at query time using functions or expressions.

**FC-3 (Hard):** For a 1:1 relationship between STUDENT and LAPTOP where each student must have a laptop and each laptop must be assigned to a student, how would you map this?
- **Answer:** Merge into a single table (since both have total participation) or use foreign key with NOT NULL constraints on both sides and UNIQUE constraint.

**FC-4 (Medium):** What is a junction table and when is it required?
- **Answer:** A junction table (associative relation) is a separate table created to implement many-to-many relationships, containing foreign keys referencing the primary keys of both related entities.

**FC-5 (Medium):** Explain the difference between total participation and partial participation with respect to foreign key implementation.
- **Answer:** Total participation uses NOT NULL foreign key constraint (entity must participate), while partial participation allows NULL values in the foreign key (participation is optional).

**FC-6 (Hard):** How do you handle a composite attribute "Address" with components: street, city, state, zip_code?
- **Answer:** Break it into separate atomic attributes: street, city, state, zip_code as individual columns in the relation.

### Short Answer Questions

**SAQ-1 (Medium):** Explain the mapping process for a weak entity with an identifying relationship.
- **Answer:** For a weak entity with identifying relationship: (1) Create a relation for the weak entity including all its attributes, (2) Include the primary key of the strong (owner) entity as a foreign key, (3) The primary key of the new relation is the combination of the foreign key and the weak entity's partial key, (4) Use ON DELETE CASCADE to maintain referential integrity.

**SAQ-2 (Hard):** A library system has BOOKS and AUTHORS with N:M relationship. Each book has multiple copies (entity: BOOK_COPY) linked to BOOK with 1:N relationship. Design the relational schema.
- **Answer:** 
  - BOOK(book_id PK, title, ISBN)
  - AUTHOR(author_id PK, author_name)
  - BOOK_AUTHOR(book_id FK, author_id FK, PRIMARY KEY(book_id, author_id)) -- Junction table
  - BOOK_COPY(copy_id PK, book_id FK, status, location)
  - Foreign key constraints maintain referential integrity between BOOK and BOOK_COPY (1:N).

---

## References

- Delhi University BSc (Hons) Computer Science NEP 2024 UGCF Syllabus
- Elmasri, R., & Navathe, S. B. (7th Ed.). *Fundamentals of Database Systems*
- Silberschatz, A., Korth, H. F., & Sudarshan, S. (7th Ed.). *Database System Concepts*

---

*This study material covers the complete ER-to-Relational mapping syllabus as per Delhi University NEP 2024 curriculum.*