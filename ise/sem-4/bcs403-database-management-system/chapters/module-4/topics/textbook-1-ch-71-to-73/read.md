# **DATABASE MANAGEMENT SYSTEM**

**Module:** 8 hours
**Topic:** Textbook 1: Ch 7.1 to 7.3

## **Introduction**

Database management system (DBMS) is a software that helps in managing and organizing data in a database. It provides a layer of abstraction between the user and the database, making it easier to perform various operations such as creation, modification, and retrieval of data.

## **7.1 Data Types**

### Definition:

Data types are the categories into which data is classified based on its characteristics. In a DBMS, data types are used to define the structure of the data in a database.

### Types of Data Types:

- **Integer**: whole numbers, decimal numbers
- **Character**: alphabets, special characters
- **Date**: date of birth, date of hire
- **Time**: time of birth, time of hire
- **Boolean**: true or false values
- **String**: a sequence of characters

### Example:

```sql
CREATE TABLE employees (
    employee_id INT,
    name VARCHAR(255),
    date_of_birth DATE,
    time_of_birth TIME,
    is_active BOOLEAN,
    address VARCHAR(255)
);
```

## **7.2 Database Normalization**

### Definition:

Database normalization is the process of organizing the data in a database to minimize data redundancy and dependency. It involves dividing large tables into smaller ones and creating relationships between them.

### Types of Normalization:

- **First Normal Form (1NF)**: each table cell must contain a single value
- **Second Normal Form (2NF)**: each non-key attribute must depend on the entire primary key
- **Third Normal Form (3NF)**: if a table is in 2NF, and a non-key attribute depends on another non-key attribute, then it should be moved to a separate table

### Example:

Suppose we have a table `orders` with the following structure:

| Order ID | Customer ID | Order Date | Product |
| -------- | ----------- | ---------- | ------- |
| 1        | 1           | 2022-01-01 | A       |
| 1        | 1           | 2022-01-01 | B       |
| 2        | 2           | 2022-01-15 | A       |

This table is not normalized because the `Order Date` column contains data for multiple orders. We can normalize this table by creating separate tables for `customers`, `orders`, and `order_products`.

## **7.3 Database Design**

### Definition:

Database design is the process of creating a conceptual schema of a database. It involves defining the relationships between different tables and the constraints that govern the data.

### Types of Database Design:

- **Entity-Relationship Diagram (ERD)**: a visual representation of the relationships between different entities in a database
- **Relational Model**: a model that uses tables and relationships to store data

### Example:

Suppose we have a database that stores information about students, courses, and enrollments. We can design a database using an ERD that includes the following entities:

- Students
- Courses
- Enrollments

The ERD can be represented as follows:

#### Students

| Attribute  | Data Type    |
| ---------- | ------------ |
| Student ID | INT          |
| Name       | VARCHAR(255) |
| Email      | VARCHAR(255) |

#### Courses

| Attribute | Data Type    |
| --------- | ------------ |
| Course ID | INT          |
| Name      | VARCHAR(255) |
| Credits   | INT          |

#### Enrollments

| Attribute     | Data Type |
| ------------- | --------- |
| Enrollment ID | INT       |
| Student ID    | INT       |
| Course ID     | INT       |

The relationships between these entities can be represented as follows:

- One-to-many: a student can enroll in many courses, but a course can only have one student enrolled.
- Many-to-many: a course can have many students enrolled, but a student can only enroll in one course.
