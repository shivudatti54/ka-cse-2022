# Normalization: 1NF, 2NF, 3NF, and BCNF

## Introduction

Normalization is a fundamental concept in database design that organizes tables to reduce data redundancy and eliminate undesirable properties like insertion, update, and deletion anomalies. Developed by Edgar F. Codd in the 1970s, normalization theory provides a systematic approach to structuring relational databases through a series of normal forms. Each normal form represents a progressively stricter set of conditions that a relation must satisfy.

In the context of the University of Delhi's BSc (Hons) Computer Science program, understanding normalization is essential for designing efficient database systems. As you progress in your career as a software developer or database administrator, poorly normalized databases can lead to significant problems: duplicate data wastes storage space, update anomalies occur when modifying one instance fails to update all copies, insertion anomalies prevent adding new data without existing information, and deletion anomalies cause unintended loss of related data. This module covers the foundational normal forms: First Normal Form (1NF), Second Normal Form (2NF), Third Normal Form (3NF), and Boyce-Codd Normal Form (BCNF).

## Key Concepts

### Functional Dependencies

Before understanding normal forms, you must grasp the concept of functional dependencies. A functional dependency (FD) is a constraint between two sets of attributes in a relation. We say "X → Y" (X functionally determines Y) if for each value of X, there is exactly one value of Y. For example, in a STUDENT relation with attributes (StudentID, Name, CourseID, Grade), StudentID → Name, meaning each student ID uniquely determines the student name.

Functional dependencies are categorized into **trivial** (Y ⊆ X, always holds) and **non-trivial** (Y ⊄ X). A **full functional dependency** means X → Y holds but no proper subset of X functionally determines Y. A **transitive dependency** occurs when X → Y, Y ↛ X, and Y → Z, creating an indirect dependency X → Z through Y.

### Prime and Non-Prime Attributes

An attribute that appears in any candidate key is called a **prime attribute**. All other attributes are **non-prime attributes**. This distinction is crucial for 2NF and 3NF definitions. For instance, if a relation has candidate keys (StudentID, CourseID), then both StudentID and CourseID are prime attributes, while all other attributes like Name or Grade are non-prime.

### First Normal Form (1NF)

A relation is in 1NF if it contains only atomic (indivisible) values. No attribute should contain a set, list, or array of values. Each column must contain a single value from its domain, and each row must be unique. Consider a relation STUDENT(StudentID, Name, PhoneNumbers) where PhoneNumbers might contain multiple phone numbers—this violates 1NF. The solution is to create a separate STUDENT_PHONE relation or restructure the data so each cell contains exactly one value.

**Rules for 1NF:**
- Eliminate repeating groups
- Create separate tables for related data
- Identify each record with a unique primary key
- Each column must contain atomic values only

### Second Normal Form (2NF)

A relation is in 2NF if it is in 1NF and all non-prime attributes are fully functionally dependent on the entire candidate key. In other words, no non-prime attribute should be dependent on only part of a composite candidate key. If the candidate key is a single attribute, the relation is automatically in 2NF if it is in 1NF.

For a relation R with candidate key X that is composite (X = A ∪ B), if there exists a functional dependency A → Y where Y is a non-prime attribute, then the relation is not in 2NF. The violation is called a **partial dependency**.

**Rules for 2NF:**
- Must be in 1NF
- Remove partial dependencies
- Create separate relations for partial dependencies
- Keep the candidate key in the original relation or move it as a foreign key

### Third Normal Form (3NF)

A relation is in 3NF if it is in 2NF and no non-prime attribute is transitively dependent on the candidate key. Formally, for every functional dependency X → Y in the relation, either X is a superkey, or each attribute in Y is prime. This eliminates transitive dependencies where a non-key attribute determines another non-key attribute.

The classic example is a relation BOOK(BookID, Publisher, PublisherAddress). Here, BookID → Publisher and Publisher → PublisherAddress create a transitive dependency. Since Publisher (non-prime) determines PublisherAddress (non-prime), this violates 3NF.

**Rules for 3NF:**
- Must be in 2NF
- Eliminate transitive dependencies
- Create separate relations for attributes involved in transitive dependencies

### Boyce-Codd Normal Form (BCNF)

BCNF is a stricter version of 3NF. A relation is in BCNF if for every non-trivial functional dependency X → Y, X is a superkey. In other words, the left side of every FD must be a superkey. While 3NF allows Y to be prime in some cases, BCNF does not permit this exception.

Consider a relation STUDENT_COURSE(StudentID, CourseID, Instructor). If each course has exactly one instructor (CourseID → Instructor) but instructors can teach multiple courses, we have CourseID → Instructor where CourseID is not a superkey (since StudentID is needed to identify a tuple). This violates BCNF even though it might be in 3NF.

**Rules for BCNF:**
- Must be in 3NF
- For every FD X → Y, X must be a superkey
- May require decomposition that loses some dependencies

## Examples

### Example 1: Converting to 1NF, 2NF, and 3NF

**Problem:** Given relation R(A, B, C, D) with FDs: A → B, A → C, (A, D) → C, and candidate key {A, D}. Normalize to 3NF.

**Solution:**

**Step 1: Check 1NF**
Assume all values are atomic. Relation is in 1NF.

**Step 2: Check 2NF**
Candidate key is {A, D}. Non-prime attributes: B, C.
FD A → B and A → C show B and C depend on A (part of key), not the entire key {A, D}.
This is a **partial dependency**—violates 2NF.

**Step 3: Decompose to achieve 2NF**
Create R1(A, B, C) with FD A → B, A → C (A is the key)
Create R2(A, D, C) with FD (A, D) → C (key is {A, D})

R1: Key = {A}, R2: Key = {A, D}

**Step 4: Check for transitive dependencies in each relation**
In R1(A, B, C): No transitive dependencies since A is a non-composite key.
In R2(A, D, C): Key is {A, D}, both are prime. No violation.

**Step 5: Relations in 3NF**
R1(A, B, C) — key: A
R2(A, D, C) — key: {A, D}

Both relations are in 3NF.

### Example 2: BCNF Decomposition

**Problem:** Given relation R(A, B, C) with FDs: A → B and B → C. Determine if in BCNF and normalize if needed.

**Solution:**

**Find Candidate Keys:**
A → B, B → C implies A → B → C, so A → (A, B, C). A is a candidate key.

**Check BCNF:**
For FD A → B: A is a superkey — satisfies BCNF
For FD B → C: B is not a superkey (A is needed to identify tuples) — violates BCNF

**Decompose using BCNF:**

Step 1: Create R1(B, C) with FD B → C (key: B)
Step 2: Create R2(A, B) with FD A → B (key: A)

Now check R1: B → C, B is the key — BCNF satisfied
R2: A → B, A is the key — BCNF satisfied

**Final Result:** R1(B, C) and R2(A, B) are both in BCNF.

### Example 3: Practical University Database

**Problem:** Registration(StudentID, StudentName, CourseID, CourseName, InstructorID, InstructorName, Grade)
FDs: StudentID → StudentName
CourseID → CourseName
InstructorID → InstructorName
(StudentID, CourseID) → Grade
InstructorID → CourseID (each instructor teaches exactly one course)

Find candidate key and normalize to 3NF.

**Solution:**

**Find Candidate Key:**
From (StudentID, CourseID) → Grade and other FDs:
StudentID, CourseID → StudentName (via StudentID)
StudentID, CourseID → CourseName (via CourseID)
StudentID, CourseID → InstructorID (via CourseID)
StudentID, CourseID → InstructorName (via InstructorID)
StudentID, CourseID → Grade

Therefore, {StudentID, CourseID} is the candidate key.

**Check 1NF:** All values atomic — in 1NF.

**Check 2NF:**
Non-prime attributes: StudentName, CourseName, InstructorID, InstructorName, Grade
Partial dependency: StudentID → StudentName (violates 2NF)
CourseID → CourseName (violates 2NF)
InstructorID → InstructorName (violates 2NF)
InstructorID → CourseID (violates 2NF)

**Decompose to 2NF/3NF:**

Create separate relations for each partial dependency:
- Student(StudentID, StudentName)
- Course(CourseID, CourseName)
- Instructor(InstructorID, InstructorName, CourseID)
- Registration(StudentID, CourseID, Grade)

Now check each:
Student: StudentID → StudentName (key is StudentID) — 3NF, BCNF
Course: CourseID → CourseName (key is CourseID) — 3NF, BCNF
Instructor: InstructorID → InstructorName, CourseID — InstructorID is key — 3NF, BCNF
Registration: (StudentID, CourseID) → Grade — key is composite, no partial dependency — 3NF

**Final Result:** Four relations in 3NF (actually BCNF).

## Exam Tips

1. **Always identify candidate keys first** before checking normal forms—you cannot determine 2NF or 3NF violations without knowing the full candidate key.

2. **Memorize the formal definitions**: 2NF eliminates partial dependencies on proper subsets of candidate keys; 3NF eliminates transitive dependencies; BCNF requires left side of every FD to be a superkey.

3. **Remember the progression**: A relation in BCNF is always in 3NF, which is always in 2NF, which is always in 1NF—but the reverse is not true.

4. **BCNF decomposition may lose dependencies**: Unlike 3NF, BCNF decomposition does not always preserve all functional dependencies. This is an important trade-off.

5. **Practice decomposition algorithms**: For exams, you must be able to show step-by-step decomposition from a relation to achieve 2NF, 3NF, or BCNF.

6. **Identify prime attributes correctly**: An attribute appearing in ANY candidate key is prime—be careful with composite keys.

7. **3NF vs BCNF distinction**: The relation R(A, B, C) with A → B and B → C is in 3NF but not BCNF because B → C has B (non-prime) on the left and C (non-prime) on the right, but B is not a superkey. This is a classic counterexample.

8. **Real-world understanding**: Explain why normalization matters—reducing redundancy, preventing anomalies, and maintaining data integrity are key points for short-answer questions.