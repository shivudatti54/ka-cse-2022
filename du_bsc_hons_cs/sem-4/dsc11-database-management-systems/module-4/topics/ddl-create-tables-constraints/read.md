# DDL: CREATE TABLE and Constraints

## A Comprehensive Study Material for Database Management Systems

---

## 1. Introduction

**Data Definition Language (DDL)** is a subset of SQL (Structured Query Language) used to define and manage database structures. In the context of the Delhi University BSc (Hons) Computer Science curriculum under NEP 2024 UGCF, understanding DDL operations is fundamental to mastering Database Management Systems (DBMS). This chapter focuses on the **CREATE TABLE** statement and various **constraints** that ensure data integrity, accuracy, and consistency within relational databases.

In real-world applications, databases form the backbone of virtually every software system—from banking applications that manage millions of transactions to e-commerce platforms tracking inventory and customer orders. When designing such databases, it is imperative that the data stored adheres to certain rules and relationships. This is where **constraints** come into play.

### Real-World Relevance

Consider an online examination system used by Delhi University for conducting semester exams. The system needs to store student records, examination details, and marks. Without proper constraints:
- Duplicate student records could be created
- Invalid marks (e.g., negative numbers or values exceeding 100) could be entered
- Marks could be assigned to non-existent students

Constraints prevent such data anomalies, ensuring that the database remains a reliable source of truth. This chapter will equip you with the knowledge to design robust database schemas using DDL commands.

---

## 2. Understanding the CREATE TABLE Statement

The **CREATE TABLE** statement is used to create a new table in a database. A table is the fundamental structure that holds data in rows and columns. Each column represents an attribute, and each row represents a record.

### Basic Syntax

```sql
CREATE TABLE table_name (
    column_name1 data_type constraints,
    column_name2 data_type constraints,
    ...
);
```

### Common Data Types

Before diving into constraints, it's essential to understand common data types:

| Data Type | Description | Example |
|-----------|-------------|---------|
| INT / INTEGER | Whole numbers | 123, -45 |
| VARCHAR(n) | Variable-length character string | 'Delhi University' |
| CHAR(n) | Fixed-length character string | 'M' |
| DATE | Date value | '2024-01-15' |
| DECIMAL(p,s) | Exact numeric value | 99.99 |
| BOOLEAN | True/False value | TRUE |

---

## 3. Database Constraints: An In-Depth Study

**Constraints** are rules applied to table columns to enforce data integrity. They prevent invalid or inconsistent data from being inserted into the database. SQL supports several types of constraints:

### 3.1 NOT NULL Constraint

The **NOT NULL** constraint ensures that a column cannot contain NULL values. Every record must have a value for that column.

**Example:**

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15),
    enrollment_year INT
);
```

In this example, `student_name` and `email` must be provided for every student record. The `phone_number` is optional (can be NULL).

**Real-World Scenario:** In a university's admission system, a student's name and application number are mandatory fields. Without the NOT NULL constraint, incomplete records could be admitted to the system, causing issues in later stages of the admission process.

### 3.2 PRIMARY KEY Constraint

The **PRIMARY KEY** uniquely identifies each record in a table. A primary key must contain unique values and cannot be NULL. A table can have only one primary key, but it can consist of multiple columns (composite primary key).

**Key Characteristics:**
- Unique values for each row
- Cannot contain NULL values
- Automatically creates an index for faster queries
- Only one PRIMARY KEY per table

**Example:**

```sql
CREATE TABLE courses (
    course_code VARCHAR(10) PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL,
    department VARCHAR(50)
);
```

Here, `course_code` serves as the primary key. No two courses can have the same course code.

**Composite Primary Key Example:**

```sql
CREATE TABLE enrollments (
    student_id INT,
    course_code VARCHAR(10),
    enrollment_date DATE,
    PRIMARY KEY (student_id, course_code)
);
```

In this case, the combination of `student_id` and `course_code` must be unique. A student can enroll in multiple courses, and a course can have multiple students, but the combination of both must be unique.

### 3.3 FOREIGN KEY Constraint

The **FOREIGN KEY** constraint establishes a relationship between two tables. A foreign key in one table refers to the primary key of another table, ensuring referential integrity. This means:
- A value in the foreign key column must exist in the referenced table's primary key
- Records in the child table cannot reference non-existent records in the parent table
- Records in the parent table cannot be deleted if referenced by child records (unless ON DELETE is specified)

**Example:**

```sql
-- Parent Table
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);

-- Child Table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100) NOT NULL,
    dept_id INT NOT NULL,
    salary DECIMAL(10,2),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

In this example, `dept_id` in the `employees` table is a foreign key that references the `dept_id` primary key in the `departments` table. This ensures that every employee belongs to a valid department.

**Advanced FOREIGN KEY Options:**

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

- **ON DELETE CASCADE**: When a parent record is deleted, all corresponding child records are automatically deleted.
- **ON UPDATE CASCADE**: When a parent key value is updated, all corresponding foreign key values are automatically updated.

**Real-World Scenario:** In the University management system, the `students` table might have a `department_id` foreign key referencing the `departments` table. This ensures that every student is associated with an existing department. If a department is closed, the administrator must decide whether to cascade delete all students in that department or prevent the deletion.

### 3.4 UNIQUE Constraint

The **UNIQUE** constraint ensures that all values in a column (or combination of columns) are distinct. Unlike primary key, a table can have multiple unique constraints, and unique columns can contain NULL values (depending on the database system).

**Example:**

```sql
CREATE TABLE faculty (
    faculty_id INT PRIMARY KEY,
    faculty_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15) UNIQUE,
    specialization VARCHAR(50)
);
```

Here, each faculty member must have a unique email address and phone number. Two faculty members cannot share the same email or phone number.

**Composite UNIQUE Constraint:**

```sql
CREATE TABLE course_schedule (
    course_code VARCHAR(10),
    room_number VARCHAR(10),
    time_slot VARCHAR(20),
    day VARCHAR(10),
    UNIQUE (room_number, time_slot, day)
);
```

This ensures that a room cannot be booked for two different courses at the same time slot on the same day.

### 3.5 CHECK Constraint

The **CHECK** constraint restricts the values that can be placed in a column based on a specified condition. It ensures that all values in a column satisfy a particular condition.

**Example:**

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    quantity INT NOT NULL CHECK (quantity >= 0),
    discount_percent DECIMAL(5,2) CHECK (discount_percent >= 0 AND discount_percent <= 100)
);
```

In this example:
- `price` must be greater than zero
- `quantity` cannot be negative
- `discount_percent` must be between 0 and 100

**Complex CHECK Constraint:**

```sql
CREATE TABLE exam_registration (
    registration_id INT PRIMARY KEY,
    student_id INT NOT NULL,
    exam_date DATE NOT NULL,
    subject_code VARCHAR(10) NOT NULL,
    CHECK (exam_date >= '2024-01-01')
);
```

This ensures that exam registrations can only be made for dates from January 1, 2024, onwards.

**Real-World Scenario:** In a grade management system, you might use a CHECK constraint to ensure that marks entered are between 0 and 100, preventing data entry errors like negative marks or marks exceeding the maximum.

### 3.6 DEFAULT Constraint

The **DEFAULT** constraint provides a default value for a column when no value is specified during insertion. If a value is explicitly provided, the default value is overridden.

**Example:**

```sql
CREATE TABLE library_books (
    book_id INT PRIMARY KEY,
    book_title VARCHAR(200) NOT NULL,
    author VARCHAR(100),
    publication_year INT DEFAULT 2024,
    status VARCHAR(20) DEFAULT 'Available',
    date_added DATE DEFAULT (CURRENT_DATE)
);
```

In this example:
- If `publication_year` is not specified, it defaults to 2024
- If `status` is not specified, it defaults to 'Available'
- `date_added` defaults to the current date

**Practical Example with Multiple Tables:**

```sql
-- Creating a complete Student Information System

-- Table 1: Departments (Parent Table)
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL UNIQUE,
    hod_name VARCHAR(100),
    established_year INT DEFAULT 2020
);

-- Table 2: Students (Child Table with multiple constraints)
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    date_of_birth DATE NOT NULL,
    enrollment_year INT DEFAULT 2024,
    dept_id INT NOT NULL,
    cgpa DECIMAL(3,2) CHECK (cgpa >= 0.0 AND cgpa <= 10.0),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Table 3: Courses
CREATE TABLE courses (
    course_code VARCHAR(10) PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL CHECK (credits BETWEEN 1 AND 6),
    dept_id INT NOT NULL,
    instructor_name VARCHAR(100),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Table 4: Enrollments (Uses composite primary key and foreign keys)
CREATE TABLE enrollments (
    student_id INT,
    course_code VARCHAR(10),
    semester VARCHAR(20) DEFAULT 'Odd Semester',
    year INT DEFAULT 2024,
    grade VARCHAR(2),
    PRIMARY KEY (student_id, course_code),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE CASCADE,
    FOREIGN KEY (course_code) REFERENCES courses(course_code)
        ON DELETE CASCADE
);
```

---

## 4. ALTER TABLE: Modifying Constraints

After creating a table, you can modify constraints using the ALTER TABLE statement.

### Adding a Constraint

```sql
ALTER TABLE students
ADD CONSTRAINT valid_email CHECK (email LIKE '%@%.%');
```

### Dropping a Constraint

```sql
ALTER TABLE students
DROP CONSTRAINT valid_email;
```

### Adding a Foreign Key

```sql
ALTER TABLE employees
ADD FOREIGN KEY (dept_id) REFERENCES departments(dept_id);
```

---

## 5. Summary Table of Constraints

| Constraint | Purpose | Can be NULL? | Multiple per Table? |
|------------|---------|--------------|---------------------|
| NOT NULL | Ensures column has a value | No | Yes |
| PRIMARY KEY | Uniquely identifies rows | No | No (one only) |
| FOREIGN KEY | Establishes relationship between tables | Yes | Yes |
| UNIQUE | Ensures all values are distinct | Yes* | Yes |
| CHECK | Validates values against condition | Yes | Yes |
| DEFAULT | Provides default value when not specified | N/A | Yes |

*Note: Some database systems allow one NULL value in UNIQUE columns, while others do not.

---

## 6. Multiple Choice Questions (MCQs)

**Question 1:** Which constraint is used to ensure that a column cannot contain NULL values?
- a) UNIQUE
- b) PRIMARY KEY
- c) NOT NULL
- d) DEFAULT

**Answer:** c) NOT NULL

**Question 2:** What is the maximum number of PRIMARY KEY constraints a table can have?
- a) 1
- b) 2
- c) Unlimited
- d) Equal to number of columns

**Answer:** a) 1

**Question 3:** Which constraint is used to establish a relationship between two tables?
- a) NOT NULL
- b) CHECK
- c) FOREIGN KEY
- d) UNIQUE

**Answer:** c) FOREIGN KEY

**Question 4:** What will happen if a foreign key constraint with ON DELETE CASCADE is defined and the parent record is deleted?
- a) The deletion will fail
- b) The child records will also be deleted
- c) The foreign key will be set to NULL
- d) An error will be raised

**Answer:** b) The child records will also be deleted

**Question 5:** Which constraint ensures that values in a column fall within a specific range?
- a) CHECK
- b) UNIQUE
- c) DEFAULT
- d) PRIMARY KEY

**Answer:** a) CHECK

**Question 6:** What is the default behavior if no value is provided for a column with a DEFAULT constraint?
- a) An error is raised
- b) NULL is inserted
- c) The default value is used
- d) The row is rejected

**Answer:** c) The default value is used

**Question 7:** Which constraint can be applied to multiple columns to create a composite key?
- a) UNIQUE
- b) CHECK
- c) PRIMARY KEY
- d) Both a) and c)

**Answer:** d) Both a) and c)

**Question 8:** In the following CREATE TABLE statement, which column will automatically receive a default value?

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) DEFAULT 'Pending'
);
```

- a) order_id
- b) order_date
- c) status
- d) Both b) and c)

**Answer:** d) Both b) and c)

---

## 7. Flashcards for Quick Revision

| Term | Definition |
|------|------------|
| **DDL** | Data Definition Language - SQL commands for defining database structures (CREATE, ALTER, DROP) |
| **NOT NULL** | Constraint that ensures a column cannot have NULL values |
| **PRIMARY KEY** | Unique identifier for each record; cannot be NULL; only one per table |
| **FOREIGN KEY** | Constraint that creates a relationship between two tables |
| **UNIQUE** | Constraint ensuring all values in a column are different |
| **CHECK** | Constraint that limits values based on a specified condition |
| **DEFAULT** | Constraint that provides a default value when none is specified |
| **Composite Key** | A primary or unique key made of multiple columns |
| **Referential Integrity** | The guarantee that foreign key values point to existing records |
| **ON DELETE CASCADE** | Option that automatically deletes child records when parent is deleted |

---

## 8. Key Takeaways

1. **DDL Commands** are essential for creating and managing database structures. The CREATE TABLE statement is foundational for any database design.

2. **Constraints** are rules that enforce data integrity and prevent invalid data entry. They are applied at the column or table level.

3. **NOT NULL** ensures essential data is always present, while **PRIMARY KEY** uniquely identifies each record.

4. **FOREIGN KEY** establishes relationships between tables, ensuring referential integrity. Understanding CASCADE operations is crucial for maintaining data consistency.

5. **UNIQUE** prevents duplicate values (except NULL in some databases), while **CHECK** validates data against specific conditions.

6. **DEFAULT** provides fallback values, improving data entry efficiency and consistency.

7. Real-world database design requires careful consideration of all constraint types to prevent data anomalies and ensure system reliability.

8. For the Delhi University NEP 2024 UGCF examination, focus on understanding the syntax, purpose, and practical applications of each constraint type.

---

*This study material is prepared in accordance with the BSc (Hons) Computer Science syllabus under NEP 2024 UGCF for Delhi University.*