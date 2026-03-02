# Normal Forms Based on Primary Keys

## Table of Contents

- [Normal Forms Based on Primary Keys](#normal-forms-based-on-primary-keys)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Functional Dependencies](#functional-dependencies)
  - [First Normal Form (1NF)](#first-normal-form-1nf)
  - [Second Normal Form (2NF)](#second-normal-form-2nf)
  - [Third Normal Form (3NF)](#third-normal-form-3nf)
  - [Boyce-Codd Normal Form (BCNF)](#boyce-codd-normal-form-bcnf)
  - [Keys and Prime Attributes](#keys-and-prime-attributes)
- [Examples](#examples)
  - [Example 1: Converting to 1NF](#example-1-converting-to-1nf)
  - [Example 2: Converting to 2NF](#example-2-converting-to-2nf)
  - [Example 3: Converting to 3NF](#example-3-converting-to-3nf)
  - [Example 4: BCNF Decomposition](#example-4-bcnf-decomposition)
- [Exam Tips](#exam-tips)

## Introduction

Database normalization is a fundamental concept in relational database design that organizes tables to reduce redundancy and improve data integrity. The process of normalization involves dividing large tables into smaller, well-structured tables and defining relationships between them using primary keys and foreign keys. Understanding normal forms based on primary keys is essential for any database professional, as improper normalization can lead to anomalies in data insertion, deletion, and modification.

The concept of normal forms was introduced by Edgar F. Codd, the founder of the relational model, in the early 1970s. Normal forms are categorized into levels ranging from First Normal Form (1NF) to Fifth Normal Form (5NF), with each higher normal form building upon the previous ones. For university examinations, students are typically expected to have a thorough understanding of 1NF through Boyce-Codd Normal Form (BCNF), with some coverage of higher normal forms.

The primary key plays a crucial role in normalization as it uniquely identifies each tuple (row) in a relation. Many normal forms are defined specifically in terms of primary keys and functional dependencies, making this topic one of the most important chapters in the Database Management System syllabus. In this module, we will explore each normal form in detail, understand the normalization process, and learn how to convert tables from lower normal forms to higher normal forms.

## Key Concepts

### Functional Dependencies

Before understanding normal forms, one must grasp the concept of functional dependencies. A functional dependency (FD) is a constraint between two sets of attributes in a relation. If A and B are sets of attributes in relation R, then A → B (A functionally determines B) means that if two tuples have the same values for attributes in A, they must also have the same values for attributes in B. For example, in a Student relation with attributes (StudentID, Name, CourseID, Grade), if StudentID uniquely identifies Name, then StudentID → Name.

Functional dependencies are the foundation upon which normal forms are defined. The process of normalization aims to eliminate undesirable functional dependencies that cause data redundancy and anomalies.

### First Normal Form (1NF)

A relation is in First Normal Form (1NF) if it contains only atomic (indivisible) values. This means that each attribute must contain a single value for each tuple, not a set of values or a list. In other words, there should be no repeating groups or arrays within columns.

To convert a table to 1NF, we must:

1. Remove repeating groups by creating separate rows for each value
2. Ensure each column contains atomic values
3. Identify and define a primary key for the relation

For example, consider a table where a student can enroll in multiple courses stored as a comma-separated list in a single cell. This violates 1NF. To make it 1NF compliant, we create separate rows for each course enrollment.

### Second Normal Form (2NF)

A relation is in Second Normal Form (2NF) if:

1. It is in 1NF already
2. No non-prime attribute (an attribute that is not part of any candidate key) is partially dependent on a proper subset of any candidate key

In simpler terms, 2NF eliminates partial dependencies. A partial dependency exists when a non-key attribute is functionally dependent on part of a composite key. To convert a table to 2NF, we decompose the relation to remove partial dependencies, creating separate relations for each candidate key and its dependent attributes.

Consider a relation Enroll(StudentID, CourseID, StudentName, Grade, Fee) where StudentID and CourseID together form the composite primary key. If StudentName depends only on StudentID (part of the key), this is a partial dependency violating 2NF.

### Third Normal Form (3NF)

A relation is in Third Normal Form (3NF) if:

1. It is in 2NF already
2. No transitive dependency exists - meaning non-prime attributes should not depend on other non-prime attributes

A transitive dependency occurs when a non-key attribute determines another non-key attribute, which in turn determines a non-key attribute. For example, in a relation with attributes (StudentID, CourseID, Fee, Discount), if Fee determines Discount, we have a transitive dependency that violates 3NF.

The general guideline is that each non-key attribute must provide a fact about the key, the whole key, and nothing but the key.

### Boyce-Codd Normal Form (BCNF)

Boyce-Codd Normal Form (BCNF) is a stricter version of 3NF. A relation is in BCNF if, for every non-trivial functional dependency A → B, A must be a superkey. In other words, the left side of every functional dependency must be a superkey.

BCNF handles certain anomalies that 3NF might not fully address, particularly when:

- A relation has multiple overlapping candidate keys
- A candidate key determines another candidate key

While BCNF is desirable, it's not always possible to decompose a relation into BCNF while preserving all functional dependencies. In such cases, 3NF is considered acceptable.

### Keys and Prime Attributes

Understanding keys is crucial for normal forms:

- **Candidate Key**: A minimal superkey that can uniquely identify each tuple
- **Primary Key**: The selected candidate key used to identify tuples
- **Prime Attribute**: An attribute that is part of any candidate key
- **Non-prime Attribute**: An attribute that is not part of any candidate key

These concepts help determine whether a relation satisfies the conditions of various normal forms.

## Examples

### Example 1: Converting to 1NF

**Problem**: Given the relation StudentCourses(StudentID, Name, Courses) where Courses contains a list of courses, normalize it to 1NF.

**Solution**:
The original relation violates 1NF because Courses contains multiple values. To make it 1NF compliant:

**Original Table**:
| StudentID | Name | Courses |
|-----------|---------|----------------------|
| S001 | Alice | DBMS, OS, Networks |
| S002 | Bob | DBMS, AI |

**1NF Table**:
| StudentID | Name | Courses |
|-----------|---------|---------|
| S001 | Alice | DBMS |
| S001 | Alice | OS |
| S001 | Alice | Networks|
| S002 | Bob | DBMS |
| S002 | Bob | AI |

The primary key becomes (StudentID, Courses) since both together uniquely identify each row.

### Example 2: Converting to 2NF

**Problem**: Given relation R(A, B, C, D) with functional dependencies A → C and AB → D, determine if R is in 2NF and normalize if needed.

**Solution**:

- The candidate key is AB (since A → C gives us C from A, and AB → D gives us D)
- A is a proper subset of the candidate key AB
- Since A → C (non-prime attribute C depends on part of the key), we have a partial dependency

**Decomposition to 2NF**:

- R1(A, C) - A is the key
- R2(A, B, D) - AB is the key

Both relations are now in 2NF as there are no partial dependencies.

### Example 3: Converting to 3NF

**Problem**: Given relation R(A, B, C, D) with FDs: A → B, B → C, C → D, normalize to 3NF.

**Solution**:

- Candidate key is A (since A → B, B → C, C → D gives us all attributes)
- We have transitive dependency: A → B → C → D
- B → C and C → D are transitive dependencies (non-key attributes determining other non-key attributes)

**Decomposition to 3NF using synthesis algorithm**:

- R1(A, B) with FD A → B
- R2(B, C) with FD B → C
- R3(C, D) with FD C → D

This decomposition is lossless and dependency-preserving.

### Example 4: BCNF Decomposition

**Problem**: Given relation R(A, B, C) with FD A → B and B → C, and candidate keys A and AB, normalize to BCNF.

**Solution**:

- Check FD A → B: A is a candidate key, so this is in BCNF
- Check FD B → C: B is not a superkey, violates BCNF

**Decomposition to BCNF**:

- Decompose R into R1(B, C) with FD B → C
- R1 is in BCNF (B is the key)
- R2(A, B) with FD A → B
- R2 is in BCNF (A is the key)

The decomposition results in R1(B, C) and R2(A, B).

## Exam Tips

1. **Understand the definitions thoroughly**: Memorize the exact conditions for each normal form (1NF, 2NF, 3NF, BCNF). university frequently asks short answer questions testing these definitions.

2. **Know the relationship between normal forms**: Remember that if a relation is in BCNF, it's also in 3NF, 2NF, and 1NF. This hierarchical relationship is important for solving problems.

3. **Identify keys correctly**: Before determining normal forms, always identify all candidate keys and prime attributes. This is the first step in analyzing any relation.

4. **Practice decomposition problems**: Most university exam questions involve decomposing relations to higher normal forms. Practice with different sets of functional dependencies.

5. **Check for anomalies**: When explaining why a relation is not in a particular normal form, mention the specific anomaly (insertion, deletion, update) that would occur.

6. **Lossless-join decomposition**: Remember to verify that your decomposition is lossless, meaning natural joins of the decomposed relations give back the original relation.

7. **Dependency preservation**: Try to preserve all original functional dependencies in your decomposition when possible. This is crucial for 3NF but may not always be possible for BCNF.

8. **Time management in exams**: Start by listing all functional dependencies, then identify candidate keys, then check each normal form in sequence from 1NF upwards.
