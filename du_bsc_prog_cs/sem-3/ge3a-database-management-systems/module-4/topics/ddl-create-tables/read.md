# DDL: CREATE TABLE Statement

## Introduction

The CREATE TABLE statement is one of the most fundamental Data Definition Language (DDL) commands in SQL. In any relational database management system, the first step toward storing and manipulating data is defining the structure of tables that will hold that data. The CREATE TABLE statement allows database designers to specify the exact structure of a table, including column names, data types, and various constraints that ensure data integrity.

In the context of University of Delhi's Computer Science curriculum, understanding CREATE TABLE is essential because it forms the foundation for all subsequent database operations. Whether you are building a simple student record system or a complex enterprise application, the way you define your tables directly impacts how efficiently you can store, retrieve, and maintain data. This topic carries significant weight in semester examinations, with practical questions frequently asked on writing CREATE TABLE statements with various constraints.

This module will cover the complete syntax of the CREATE TABLE statement, various SQL data types, different types of constraints, and practical examples that mirror real-world database design scenarios commonly encountered in DU examinations.

## Key Concepts

### Basic Syntax of CREATE TABLE

The fundamental syntax for creating a table in SQL is:

```sql
CREATE TABLE table_name (
    column1 datatype [constraints],
    column2 datatype [constraints],
    ...
);
```

Each column must have a name and a data type. Constraints are optional but highly recommended for maintaining data integrity.

### SQL Data Types

Understanding appropriate data types is crucial for efficient database design. The following are the most commonly used data types:

**Numeric Types:**
- `INT` or `INTEGER`: Whole numbers (-2,147,483,648 to 2,147,483,647)
- `SMALLINT`: Smaller whole numbers (-32,768 to 32,767)
- `BIGINT`: Large whole numbers
- `DECIMAL(p, s)` or `NUMERIC(p, s)`: Exact numeric with precision p and scale s
- `FLOAT` or `DOUBLE`: Approximate numeric values

**String Types:**
- `CHAR(n)`: Fixed-length string of n characters
- `VARCHAR(n)`: Variable-length string up to n characters
- `TEXT`: Long text strings

**Date and Time Types:**
- `DATE`: Date (YYYY-MM-DD)
- `TIME`: Time (HH:MM:SS)
- `DATETIME` or `TIMESTAMP`: Both date and time

### Types of Constraints

Constraints enforce rules on table columns, ensuring data integrity:

**1. NOT NULL Constraint**
Ensures a column cannot contain NULL values:
```sql
student_name VARCHAR(50) NOT NULL
```

**2. UNIQUE Constraint**
Ensures all values in a column are different:
```sql
email VARCHAR(100) UNIQUE
```

**3. PRIMARY KEY Constraint**
Uniquely identifies each row. A table can have only one primary key:
```sql
student_id INT PRIMARY KEY
```

**4. FOREIGN KEY Constraint**
References a primary key in another table, establishing relationship:
```sql
department_id INT REFERENCES department(dept_id)
```

**5. CHECK Constraint**
Limits values that can be placed in a column:
```sql
age INT CHECK (age >= 18)
```

**6. DEFAULT Constraint**
Provides a default value when no value is specified:
```sql
status VARCHAR(20) DEFAULT 'Active'
```

### Column Level vs Table Level Constraints

Constraints can be defined at two levels:

**Column Level:** Constraint is applied to a specific column
```sql
CREATE TABLE student (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
```

**Table Level:** Constraint applies to the entire table, useful for composite keys:
```sql
CREATE TABLE enrollment (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id)
);
```

### AUTO_INCREMENT / IDENTITY

Automatically generates unique sequential numbers:
```sql
student_id INT PRIMARY KEY AUTO_INCREMENT
```
(Syntax varies: AUTO_INCREMENT in MySQL, IDENTITY in SQL Server, SEQUENCE in Oracle)

## Examples

### Example 1: Creating a Student Table

**Question:** Create a table named "STUDENT" with the following specifications:
- STUDENT_ID: Integer, Primary Key, Auto-increment
- STUDENT_NAME: Varchar(50), Not Null
- EMAIL: Varchar(100), Unique
- AGE: Integer, Should be between 15 and 25
- JOIN_DATE: Date, Default today's date

**Solution:**
```sql
CREATE TABLE STUDENT (
    STUDENT_ID INT PRIMARY KEY AUTO_INCREMENT,
    STUDENT_NAME VARCHAR(50) NOT NULL,
    EMAIL VARCHAR(100) UNIQUE,
    AGE INT CHECK (AGE >= 15 AND AGE <= 25),
    JOIN_DATE DATE DEFAULT CURRENT_DATE
);
```

**Explanation:**
- STUDENT_ID is the primary key with auto-increment
- STUDENT_NAME cannot be NULL (mandatory field)
- EMAIL must be unique for each student
- AGE is validated using CHECK constraint
- JOIN_DATE defaults to current date if not specified

### Example 2: Creating Tables with Foreign Key Relationship

**Question:** Create two tables "DEPARTMENT" and "EMPLOYEE" where EMPLOYEE table has a foreign key reference to DEPARTMENT.

**Solution:**
```sql
CREATE TABLE DEPARTMENT (
    DEPT_ID INT PRIMARY KEY,
    DEPT_NAME VARCHAR(50) NOT NULL,
    DEPT_LOCATION VARCHAR(50)
);

CREATE TABLE EMPLOYEE (
    EMP_ID INT PRIMARY KEY,
    EMP_NAME VARCHAR(50) NOT NULL,
    SALARY DECIMAL(10, 2) CHECK (SALARY > 0),
    DEPT_ID INT,
    FOREIGN KEY (DEPT_ID) REFERENCES DEPARTMENT(DEPT_ID)
);
```

**Explanation:**
- DEPARTMENT table stores department information with DEPT_ID as primary key
- EMPLOYEE table has EMP_ID as primary key
- DEPT_ID in EMPLOYEE is a foreign key referencing DEPARTMENT(DEPT_ID)
- SALARY must be positive (CHECK constraint)

### Example 3: Composite Primary Key

**Question:** Create a table "COURSE_ENROLLMENT" to store which student has enrolled in which course. Each student can enroll in the same course only once.

**Solution:**
```sql
CREATE TABLE COURSE_ENROLLMENT (
    STUDENT_ID INT NOT NULL,
    COURSE_ID INT NOT NULL,
    ENROLLMENT_DATE DATE NOT NULL,
    GRADE VARCHAR(2),
    PRIMARY KEY (STUDENT_ID, COURSE_ID)
);
```

**Explanation:**
- The combination of STUDENT_ID and COURSE_ID uniquely identifies each enrollment
- This is a composite primary key defined at table level
- Both columns together must be unique; individually they can repeat

## Exam Tips

1. **Remember Syntax Order:** The correct order in CREATE TABLE is: column name → data type → constraints. Common mistakes include putting constraints before data types.

2. **Primary Key Rules:** A table can have only ONE primary key, but it can be composite (multiple columns). Know when to use column-level vs table-level constraints.

3. **Foreign Key Syntax:** Remember the FOREIGN KEY (column_name) REFERENCES table_name(column_name) syntax. Many students forget to specify the foreign key column name.

4. **CHECK Constraint Placement:** CHECK constraints can be defined at both column level and table level. For complex conditions involving multiple columns, use table-level syntax.

5. **Difference between CHAR and VARCHAR:** CHAR is fixed-length (pads with spaces), VARCHAR is variable-length. Use VARCHAR for variable-length data like names.

6. **Default Values:** DEFAULT constraint is useful for columns like status, join_date, etc. Remember the syntax: DEFAULT value (not DEFAULT(value)).

7. **Auto-increment Syntax:** Different databases use different syntax - AUTO_INCREMENT (MySQL), IDENTITY (SQL Server), SERIAL (PostgreSQL). Check which database your question assumes.

8. **NOT NULL vs UNIQUE:** NOT NULL prevents NULL values but allows duplicates. UNIQUE allows one NULL (in most databases) but prevents duplicates. They are different constraints.

9. **Data Type Selection:** Choose appropriate data types - use INT for IDs, VARCHAR for names/text, DECIMAL for currency, DATE for dates.

10. **Question Interpretation:** Carefully read what constraints are asked. Write each constraint in the correct position - column-level for single column, table-level for composite keys or multiple column conditions.