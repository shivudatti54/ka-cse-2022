# Constraints On Relationships — DBMS

## Introduction

In Database Management Systems, **relationship constraints** define the rules and restrictions that govern how entities relate to each other in a database. These constraints ensure data integrity, consistency, and accuracy. For Delhi University's BSc (Hons) Computer Science (NEP 2024 UGCF) syllabus, understanding these constraints is essential for designing reliable relational databases.

---

## Key Concepts

### 1. Types of Relationship Constraints

- **Cardinality Constraints**: Define the number of entities that can participate in a relationship
  - One-to-One (1:1)
  - One-to-Many (1:N)
  - Many-to-Many (M:N)

- **Participation Constraints**: Determine whether entity existence depends on the relationship
  - **Total Participation**: Entity must participate (e.g., every student must enroll in a course)
  - **Partial Participation**: Entity may or may not participate

### 2. Integrity Constraints on Relationships

- **Referential Integrity**: Foreign key must reference an existing primary key value or be NULL
  - Ensures relationship validity between tables
  - Maintained through **cascading actions**: CASCADE, SET NULL, SET DEFAULT, RESTRICT

- **Entity Integrity**: Primary key cannot contain NULL values
  - Each entity must be uniquely identifiable

- **Domain Constraints**: Values must belong to valid domains (data types, formats, ranges)

### 3. Keys in Relationships

- **Primary Key (PK)**: Uniquely identifies each entity
- **Foreign Key (FK)**: Creates relationship between tables
- **Candidate Key**: Potential primary key
- **Composite Key**: Multiple attributes forming a unique identifier

### 4. Weak Entity Constraints

- Weak entities depend on owner entity for identification
- Owner entity's PK + weak entity's partial key = full identifier
- Total participation in identifying relationship

### 5. Additional Constraints

- **Check Constraints**: User-defined conditions on column values
- **Unique Constraints**: No duplicate values (except NULL)
- **Not NULL Constraints**: Mandatory values

---

## Conclusion

Relationship constraints are fundamental to maintaining database consistency and reliability. Understanding cardinality, participation, referential integrity, and key constraints enables students to design robust database schemas that prevent data anomalies. These concepts form the foundation for effective database management and are crucial for exam success in Delhi University's DBMS curriculum.

---

*Reference: Delhi University NEP 2024 UGCF — BSc (Hons) Computer Science, Database Management Systems Syllabus*