# Normalization: 1NF, 2NF, 3NF, and BCNF

## Introduction

Normalization is a fundamental concept in relational database design that organizes data into tables to minimize redundancy and eliminate undesirable characteristics like insertion, update, and deletion anomalies. Developed by Edgar F. Codd in the early 1970s as part of his relational model, normalization has become an essential skill for database professionals and remains a core topic in the University of Delhi MCA curriculum.

In real-world applications, poorly designed databases lead to significant problems. Consider an e-commerce platform managing customer orders without proper normalization: storing customer details repeatedly for each order wastes storage space, updating a customer's address requires modifying multiple rows (update anomaly), adding a new customer without an order becomes problematic (insertion anomaly), and deleting the last order of a customer might accidentally remove essential customer information (deletion anomaly). Normalization addresses these issues systematically through progressive normal forms.

For the DU MCA examinations, normalization carries substantial weightage, typically 8-12 marks in the end semester examination. Understanding not just the definitions but the practical application of each normal form is crucial for scoring well. This module covers the first through Boyce-Codd normal forms, providing a solid foundation for advanced database design concepts.

## Key Concepts

### Functional Dependencies

Before understanding normal forms, one must grasp the concept of functional dependencies. A functional dependency (FD) is a constraint between two sets of attributes in a relation. If attribute A functionally determines attribute B (written as A → B), then for any two tuples with the same A value, they must have the same B value.

For example, in a Student(StudentID, Name, CourseID, CourseName, Grade) relation:
- StudentID → Name (knowing the StudentID uniquely identifies the student's name)
- CourseID → CourseName (course ID determines course name)
- StudentID, CourseID → Grade (composite key determines grade)

Functional dependencies are the backbone of normalization theory. Identifying all functional dependencies in a relation is the first step toward normalizing a database.

### First Normal Form (1NF)

A relation is in First Normal Form (1NF) if it contains only atomic (indivisible) values. No attribute can contain a set, list, array, or any composite value. Each cell must hold a single value, and each tuple must be unique.

**Requirements for 1NF:**
1. The relation must have a primary key
2. Each attribute must contain only atomic (single) values
3. Each column must have a unique name
4. There should be no repeating groups

**Example of violation:** A Student(StudentID, Name, PhoneNumbers) relation where PhoneNumbers contains multiple phone numbers like "9876543210, 9876543211" violates 1NF.

**Conversion to 1NF:** To convert a non-1NF relation to 1NF, we remove repeating groups by creating separate rows for each value or by splitting composite attributes.

### Second Normal Form (2NF)

A relation is in Second Normal Form (2NF) if:
1. It is in 1NF
2. No non-prime attribute is partially dependent on a proper subset of any candidate key

A non-prime attribute is an attribute that is not part of any candidate key. In simpler terms, 2NF eliminates partial dependencies where a non-key attribute depends on only part of a composite primary key.

**Partial Dependency:** X → Y where X is a proper subset of a candidate key, and Y is a non-prime attribute.

**Example:** Consider the relation Enroll(StudentID, CourseID, StudentName, CourseName, Grade, InstructorName) with:
- Candidate key: (StudentID, CourseID)
- Functional dependencies: StudentID → StudentName, CourseID → {CourseName, InstructorName}

Here, StudentName depends only on StudentID (part of the key), and CourseName and InstructorName depend only on CourseID (part of the key). This is a partial dependency violation.

**Conversion to 2NF:** Decompose the relation to remove partial dependencies, creating separate relations for each functional dependency.

### Third Normal Form (3NF)

A relation is in Third Normal Form (3NF) if:
1. It is in 2NF
2. No transitive dependency exists where a non-key attribute depends on another non-key attribute

A transitive dependency occurs when: X → Y (where Y is non-prime), and Y → Z (where Z is non-prime). This creates an indirect dependency X → Z through Y.

**Example:** Consider the relation Employee(EmpID, EmpName, DeptID, DeptName, DeptLocation) with:
- EmpID → EmpName, DeptID
- DeptID → DeptName, DeptLocation

Here, DeptName and DeptLocation depend on DeptID, which itself depends on EmpID. This is a transitive dependency.

**Conversion to 3NF:** Decompose the relation to eliminate transitive dependencies, typically using the closure of functional dependencies to identify the minimal decomposition.

### Boyce-Codd Normal Form (BCNF)

Boyce-Codd Normal Form (BCNF) is a stricter version of 3NF. A relation is in BCNF if for every non-trivial functional dependency X → Y, X is a superkey.

In other words, the left side of every functional dependency must be a superkey. BCNF handles certain anomalies that 3NF might not fully eliminate, particularly when:
- There are multiple overlapping candidate keys
- The primary key is a composite of three or more attributes

**Example:** Consider the relation Project(StudentID, ProjectID, Advisor) with:
- Candidate keys: (StudentID, ProjectID), (StudentID, Advisor), (ProjectID, Advisor)
- Functional dependency: Advisor → ProjectID

Here, Advisor determines ProjectID, but Advisor is not a superkey. This relation is in 3NF but not in BCNF.

**Conversion to BCNF:** May require decomposing relations that cannot be loss-joined, potentially losing some functional dependencies in the process.

## Examples

### Example 1: Converting to 1NF

**Problem:** Given the relation CustomerOrder(OrderID, CustomerName, Items, TotalAmount):
- OrderID: 101, CustomerName: "Rohit Sharma", Items: "Laptop, Mouse, Keyboard", TotalAmount: 55000
- OrderID: 102, CustomerName: "Priya Patel", Items: "Monitor", TotalAmount: 15000

**Solution:**
The attribute Items contains multiple values, violating 1NF. Convert to 1NF:

CustomerOrder1NF(OrderID, CustomerName, Item, TotalAmount):
- (101, "Rohit Sharma", "Laptop", 55000)
- (101, "Rohit Sharma", "Mouse", 55000)
- (101, "Rohit Sharma", "Keyboard", 55000)
- (102, "Priya Patel", "Monitor", 15000)

Note: TotalAmount is now duplicated, which leads to update anomalies—this will be addressed in higher normal forms.

### Example 2: Converting to 2NF

**Problem:** Given relation StudentCourse(StudentID, CourseID, StudentName, CourseName, Grade):
- Candidate key: (StudentID, CourseID)
- FDs: StudentID → StudentName; CourseID → CourseName; (StudentID, CourseID) → Grade

**Analysis:**
- This relation is in 1NF (atomic values)
- StudentName depends on StudentID (part of key) - partial dependency
- CourseName depends on CourseID (part of key) - partial dependency
- Grade depends on full key - no partial dependency

**Solution - Decompose into 2NF:**

Student(StudentID, StudentName)
Course(CourseID, CourseName)
Enrollment(StudentID, CourseID, Grade)

All three relations are now in 2NF.

### Example 3: Converting to 3NF

**Problem:** Given relation Employee(EmpID, EmpName, DeptID, DeptName, DeptLocation):
- FDs: EmpID → EmpName, DeptID; DeptID → DeptName, DeptLocation
- Candidate key: EmpID

**Analysis:**
- In 2NF (no partial dependencies since EmpID is single attribute)
- Transitive dependency: EmpID → DeptID → {DeptName, DeptLocation}
- DeptName and DeptLocation depend on DeptID, which depends on EmpID

**Solution - Decompose into 3NF:**

EmployeeNew(EmpID, EmpName, DeptID)
Department(DeptID, DeptName, DeptLocation)

Both relations are now in 3NF.

### Example 4: Converting to BCNF

**Problem:** Given relation Advising(StudentID, Advisor, Major):
- FDs: Advisor → Major; StudentID, Major → Advisor
- Candidate keys: (StudentID, Advisor), (StudentID, Major)

**Analysis:**
- In 3NF (each dependency has a key on RHS)
- BCNF violation: Advisor → Major, but Advisor is not a superkey

**Solution - Decompose into BCNF:**

This decomposition is challenging. One possible decomposition:
AdvisorMajor(Advisor, Major)
StudentAdvisor(StudentID, Advisor)

However, this loses the dependency StudentID, Major → Advisor, demonstrating that BCNF decomposition may not preserve all functional dependencies.

## Exam Tips

1. **Remember the progression:** Always check lower normal forms first—1NF must be satisfied before 2NF, 2NF before 3NF, and so on. Many students lose marks by directly jumping to higher normal forms.

2. **Identify candidate keys correctly:** Before determining if a relation is in any normal form, you must identify all candidate keys. The primary key alone is insufficient for normalization analysis.

3. **Focus on non-prime attributes:** 2NF and 3NF specifically deal with non-prime attributes. Carefully distinguish between prime (part of candidate key) and non-prime attributes.

4. **Practice decomposition steps:** Understand the algorithm for each normal form—identify the violating dependency, decompose, and verify losslessness and dependency preservation.

5. **BCNF vs 3NF distinction:** Remember that BCNF is stricter. A relation in BCNF is always in 3NF, but the converse is not true. Watch for multiple candidate keys and non-key dependencies.

6. **Lossless-join decomposition:** When decomposing relations, always verify that the decomposition is lossless (no information loss). The formula: (R1 ∩ R2) → R1 or (R1 ∩ R2) → R2 must hold.

7. **Dependency preservation:** For 3NF, try to preserve dependencies if possible. Use the minimal cover to ensure all original FDs can be enforced in the decomposed relations.

8. **Time management in exams:** Start by listing all functional dependencies clearly, identify candidate keys, then systematically check each normal form. This structured approach ensures no marks are missed.