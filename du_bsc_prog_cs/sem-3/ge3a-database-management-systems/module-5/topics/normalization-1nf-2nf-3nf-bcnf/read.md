# Normalization (1NF, 2NF, 3NF, BCNF)

## Introduction

Normalization is a fundamental concept in relational database design that organizes data into tables to minimize redundancy and avoid anomalies. Developed by Edgar F. Codd in the 1970s, normalization theory provides a systematic approach to structuring relational databases by decomposing tables into smaller, well-designed relations based on functional dependencies. For University of Delhi's Computer Science students, understanding normalization is essential as it forms the backbone of efficient database design and is a frequently tested topic in semester examinations.

In practical terms, a poorly designed database suffers from three main anomalies: insertion anomaly (inability to add certain data due to incomplete information), deletion anomaly (unintended loss of data when deleting other data), and update anomaly (inconsistency when updating the same data in multiple places). Consider a university database where student information is stored along with course details in a single table. If a student enrolls in a new course, we must repeat all student details; if a student leaves, we lose all course information. Normalization addresses these problems by ensuring data is stored logically with minimal duplication.

The normalization process progresses through increasingly stricter normal forms: First Normal Form (1NF), Second Normal Form (2NF), Third Normal Form (3NF), and Boyce-Codd Normal Form (BCNF). Each normal form builds upon the previous one, eliminating specific types of redundancy and dependency problems.

## Key Concepts

### Functional Dependencies

Before understanding normal forms, one must grasp the concept of functional dependencies. A functional dependency (FD) is a constraint between two sets of attributes in a relation. If attribute A functionally determines attribute B (written as A → B), then for every valid tuple in the relation, if two tuples have the same value for A, they must have the same value for B. For example, in a Student relation with attributes (StudentID, Name, Email, CourseID), StudentID → Name and StudentID → Email hold, meaning knowing the StudentID uniquely determines the Name and Email.

A functional dependency is trivial if the right-hand side is a subset of the left-hand side (e.g., AB → A). Non-trivial FDs are those where the right-hand side is not a subset of the left-hand side (e.g., StudentID → CourseID). A FD is completely non-trivial if the left and right sides share no common attributes.

### Prime and Non-Prime Attributes

An attribute that is a member of any candidate key of a relation is called a prime attribute. All other attributes are non-prime attributes. For instance, if the candidate key of a relation is (StudentID, CourseID), then both StudentID and CourseID are prime attributes, while attributes like Name, Email, and Grade are non-prime.

### First Normal Form (1NF)

A relation is in First Normal Form if it contains only atomic (indivisible) values. This means each column must contain a single value, not a set, list, or array. No repeating groups or arrays are allowed. To achieve 1NF, we remove repeating groups by creating separate rows or separate tables.

For example, a table with a "PhoneNumbers" column containing multiple phone numbers violates 1NF. We would normalize this by either creating multiple rows for each phone number or creating a separate PhoneNumbers table linked to the main table.

**Rules for 1NF:**
- Eliminate repeating groups
- Each column must contain atomic values
- Each row must be unique
- Each column must have a unique name

### Second Normal Form (2NF)

A relation is in Second Normal Form if it is in 1NF and all non-prime attributes are fully functionally dependent on the entire candidate key. In other words, no partial dependency should exist, where a non-prime attribute depends on only part of a composite candidate key.

For a relation with a composite key (A, B), if A → Name (where Name is a non-prime attribute), then this is a partial dependency and the relation is not in 2NF. To achieve 2NF, we decompose the relation to remove partial dependencies, creating separate relations for the partial key and its dependent attributes.

**Rules for 2NF:**
- Must be in 1NF
- No partial dependencies
- All non-prime attributes must depend on the entire candidate key

### Third Normal Form (3NF)

A relation is in Third Normal Form if it is in 2NF and no transitive dependencies exist. A transitive dependency occurs when a non-prime attribute depends on another non-prime attribute, which in turn depends on the candidate key. In formal terms, a relation is in 3NF if for every non-trivial FD X → A, either X is a superkey or A is a prime attribute.

For example, in a relation Student(StudentID, Name, City, ZipCode) where StudentID → ZipCode and ZipCode → City, City depends transitively on StudentID through ZipCode. This creates update anomalies. To achieve 3NF, we decompose to remove transitive dependencies.

**Rules for 3NF:**
- Must be in 2NF
- No transitive dependencies
- No non-prime attribute determines part of a candidate key

### Boyce-Codd Normal Form (BCNF)

Boyce-Codd Normal Form is a stricter version of 3NF. A relation is in BCNF if for every non-trivial functional dependency X → Y, X is a superkey of the relation. While 3NF allows certain dependencies where the right side is a prime attribute, BCNF does not permit this exception.

Consider a relation Teaching(Professor, Course, Student) where each professor teaches exactly one course, and each student takes exactly one course from each professor. The FDs are: Professor → Course and (Professor, Student) → Course. The candidate key is (Professor, Student), but Professor → Course violates BCNF because Professor is not a superkey. This relation is in 3NF but not in BCNF.

**Rules for BCNF:**
- Must be in 3NF
- For every FD X → Y, X must be a superkey

## Examples

### Example 1: Normalizing a Student-Course Relation

**Initial Relation: ENROLLMENT(StudentID, StudentName, CourseID, CourseName, Instructor, Grade)**

Candidate Key: (StudentID, CourseID)

Functional Dependencies:
1. StudentID → StudentName
2. CourseID → CourseName, Instructor
3. (StudentID, CourseID) → Grade

**Step 1: Check 1NF**
All values are atomic. The relation is in 1NF.

**Step 2: Check 2NF**
- StudentID → StudentName is a partial dependency (non-prime attribute StudentName depends on part of the candidate key)
- CourseID → CourseName, Instructor is also a partial dependency

Relation is NOT in 2NF.

**Decomposition for 2NF:**
Create two relations:
- STUDENT(StudentID, StudentName)
- COURSE(CourseID, CourseName, Instructor)
- ENROLLMENT(StudentID, CourseID, Grade)

**Step 3: Check 3NF**
In ENROLLMENT relation: FDs are (StudentID, CourseID) → Grade. No transitive dependencies.

In STUDENT: StudentID → StudentName (StudentID is the key, so in 3NF)

In COURSE: CourseID → CourseName, Instructor (CourseID is the key, so in 3NF)

All relations are in 3NF.

**Step 4: Check BCNF**
In COURSE: CourseID → CourseName, Instructor. CourseID is the key, so it is in BCNF.

All relations are in BCNF.

**Final Result:** Relations in BCNF: STUDENT(StudentID, StudentName), COURSE(CourseID, CourseName, Instructor), ENROLLMENT(StudentID, CourseID, Grade)

### Example 2: Library Management System

**Initial Relation: BOOK_LOAN(BookID, Title, Author, MemberID, MemberName, DateBorrowed, DateReturned)**

Functional Dependencies:
1. BookID → Title, Author
2. MemberID → MemberName
3. (BookID, MemberID) → DateBorrowed, DateReturned

**Analysis:**
- Candidate Key: (BookID, MemberID)
- 1NF: Values are atomic ✓
- 2NF: BookID → Title (partial dependency on non-prime attribute), MemberID → MemberName (partial dependency). NOT in 2NF.
- Decompose into: BOOK(BookID, Title, Author), MEMBER(MemberID, MemberName), LOAN(BookID, MemberID, DateBorrowed, DateReturned)
- All three relations are in BCNF (keys are BookID, MemberID, and (BookID, MemberID) respectively)

### Example 3: Employee Assignment Problem

**Relation: ASSIGN(EmpID, ProjectID, Skill, Task)**

Functional Dependencies:
1. EmpID, ProjectID → Task
2. EmpID → Skill

**Analysis:**
- Candidate Key: (EmpID, ProjectID)
- 1NF: Atomic values ✓
- 2NF: EmpID → Skill is a partial dependency (Skill depends on EmpID, part of the key). NOT in 2NF.
- 3NF/BCNF Decomposition: EMP(EmpID, Skill), PROJASSIGN(EmpID, ProjectID, Task)
- Both relations are in BCNF.

## Exam Tips

1. **Understand the Hierarchy:** Remember that BCNF implies 3NF, 3NF implies 2NF, and 2NF implies 1NF. However, the reverse is not true.

2. **Identifying Normal Forms:** To determine the normal form of a relation, first identify all candidate keys, then find all functional dependencies, and check each normal form condition systematically.

3. **BCNF vs 3NF Difference:** Remember that 3NF allows a FD where the right side is a prime attribute, but BCNF does not. This is the key distinguishing factor.

4. **Lossless Join Decomposition:** When decomposing relations, always ensure the decomposition is lossless (no information is lost). A decomposition is lossless if the common attribute is a key of at least one relation.

5. **Dependency Preservation:** Try to preserve dependencies during decomposition so that all original FDs can be enforced within the decomposed relations.

6. **Common Exam Question Pattern:** "Given a relation R(A,B,C,D,E) with FDs A→BC, CD→E, B→D, determine the highest normal form." Practice such questions by systematically checking each normal form.

7. **Remember Prime Attributes:** Correctly identifying prime attributes is crucial for checking 3NF. An attribute is prime if it appears in any candidate key.