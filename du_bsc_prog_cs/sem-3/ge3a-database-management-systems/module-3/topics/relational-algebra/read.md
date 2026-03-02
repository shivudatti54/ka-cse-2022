# Relational Algebra: Comprehensive Study Material

## Database Management Systems (Ge3A)

### BSc Physical Science (CS) — Delhi University, NEP 2024

---

## Table of Contents

1. [Introduction to Relational Algebra](#1-introduction-to-relational-algebra)
2. [Fundamental Operators](#2-fundamental-operators)
3. [Derived/Additional Operators](#3-derivedadditional-operators)
4. [Extended Operators](#4-extended-operators)
5. [Practical Examples with Tables](#5-practical-examples-with-tables)
6. [SQL Mapping](#6-sql-mapping)
7. [Key Takeaways](#7-key-takeaways)
8. [Assessment Section](#8-assessment-section)

---

## 1. Introduction to Relational Algebra

### What is Relational Algebra?

Relational Algebra is a **theoretical query language** for the relational model of data. It provides a set of mathematical operations that take one or two relations (tables) as input and produce a new relation as output. It serves as the **theoretical foundation** for all query languages used in relational database management systems (RDBMS).

### Why is Relational Algebra Important?

| Aspect | Importance |
|--------|------------|
| **Theoretical Foundation** | Forms the basis for understanding query optimization |
| **Query Processing** | Helps DBMS understand how to execute queries efficiently |
| **SQL Equivalence** | Every SQL query can be translated to relational algebra |
| **Research & Development** | Enables development of new query optimization techniques |

### Real-World Relevance

Consider a university database where you need to find:
- Students enrolled in multiple courses
- Professors teaching specific subjects
- Departments with budget exceeding a threshold

These queries are expressed using relational algebra operations, which the DBMS optimizes and executes. Major tech companies like **Google (BigQuery), Amazon (Redshift), and Oracle** use relational algebra principles in their query optimization engines.

### Delhi University Syllabus Context

This topic aligns with **Unit III: Relational Algebra** of the Ge3A Database Management Systems syllabus for BSc Physical Science (CS) under NEP 2024. The syllabus emphasizes understanding both fundamental and derived operators with practical implementation.

---

## 2. Fundamental Operators

The fundamental operators (also called **primitive operators**) were defined by Edgar F. Codd and form the complete set needed to express any relational query.

### 2.1 Selection (σ) — The Filter Operator

**Definition:** Selects rows (tuples) from a relation that satisfy a given predicate/condition.

**Syntax:** `σ_condition(Relation)`

**Properties:**
- Unary operator (operates on single relation)
- Produces a horizontal subset (fewer rows, same columns)
- Can use: `=`, `≠`, `<`, `>`, `≤`, `≥`, `AND`, `OR`, `NOT`

**Example Table: EMPLOYEES**

| E_ID | Name | Dept | Salary |
|------|------|------|--------|
| E001 | Amit | CS | 50000 |
| E002 | Priya | IT | 55000 |
| E003 | Rahul | CS | 45000 |
| E004 | Sara | MA | 60000 |

**Query:** Find all employees in Department 'CS'
```
σ_Dept='CS'(EMPLOYEES)
```

**Result:**

| E_ID | Name | Dept | Salary |
|------|------|------|--------|
| E001 | Amit | CS | 50000 |
| E003 | Rahul | CS | 45000 |

### 2.2 Projection (π) — The Column Selector

**Definition:** Selects specific columns (attributes) from a relation, eliminating duplicate rows.

**Syntax:** `π_column1, column2, ...(Relation)`

**Properties:**
- Unary operator
- Produces a vertical subset (same rows, fewer columns)
- **Automatically eliminates duplicates** (set theory property)
- If no condition specified, selects all attributes

**Query:** Get names and salaries of all employees
```
π_Name, Salary(EMPLOYEES)
```

**Result:**

| Name | Salary |
|------|--------|
| Amit | 50000 |
| Priya | 55000 |
| Rahul | 45000 |
| Sara | 60000 |

### 2.3 Union (∪) — Combination Operator

**Definition:** Combines results from two relations, returning all tuples that appear in either relation.

**Syntax:** `R ∪ S`

**Properties:**
- Binary operator
- **Both relations must have same schema** (same number and types of attributes)
- Automatically removes duplicates
- Commutative: `R ∪ S = S ∪ R`

**Example Tables:**

STUDENTS_CS:

| SID | Name |
|-----|------|
| S1 | Amit |
| S2 | Priya |

STUDENTS_IT:

| SID | Name |
|-----|------|
| S3 | Rahul |
| S4 | Amit |

**Query:** Get all students from both departments
```
STUDENTS_CS ∪ STUDENTS_IT
```

**Result:**

| SID | Name |
|-----|------|
| S1 | Amit |
| S2 | Priya |
| S3 | Rahul |
| S4 | Amit |

*(Note: 'Amit' appears once due to set semantics)*

### 2.4 Set Difference (−) — The Subtraction Operator

**Definition:** Returns tuples that exist in the first relation but NOT in the second relation.

**Syntax:** `R − S`

**Properties:**
- Binary operator
- **Both relations must have same schema**
- Not commutative: `R − S ≠ S − R`

**Query:** Find students in CS but NOT in IT
```
STUDENTS_CS − STUDENTS_IT
```

**Result:**

| SID | Name |
|-----|------|
| S1 | Amit |
| S2 | Priya |

### 2.5 Cartesian Product (×) — The Cross Join

**Definition:** Combines every tuple from the first relation with every tuple from the second relation.

**Syntax:** `R × S`

**Properties:**
- Binary operator
- Result has all attributes from both relations
- If |R| = m tuples and |S| = n tuples, result has m×n tuples
- Usually followed by Selection to find meaningful relationships

**Example:**

R (Students):

| SID | Name |
|-----|------|
| S1 | Amit |
| S2 | Priya |

S (Courses):

| CID | CName |
|-----|-------|
| C1 | DBMS |
| C2 | OS |

**Query:** `R × S`

**Result:**

| SID | Name | CID | CName |
|-----|------|-----|-------|
| S1 | Amit | C1 | DBMS |
| S1 | Amit | C2 | OS |
| S2 | Priya | C1 | DBMS |
| S2 | Priya | C2 | OS |

### 2.6 Rename (ρ) — The Alias Operator

**Definition:** Renames relation attributes or the relation itself for clarity and to enable operations like self-joins.

**Syntax:** `ρ_newName(attribute1 → newAttr1, attribute2 → newAttr2, ...)(Relation)`

**Properties:**
- Unary operator
- Useful for:
  - Distinguishing attributes in self-joins
  - Simplifying complex queries
  - Creating alias names

**Example:** Rename EMPLOYEES to E with new attribute names
```
ρ_E(EmpID → EID, Name → Ename)(EMPLOYEES)
```

---

## 3. Derived/Additional Operators

These operators are **not primitive** but can be expressed using fundamental operators. They provide convenience and are commonly used in practice.

### 3.1 Join (⋈) — The Most Important Derived Operator

Join combines related tuples from two relations based on a join condition. It is essentially a **Cartesian Product followed by Selection**.

#### 3.1.1 Natural Join (⋈)

Joins two relations on **common attributes with same name and value**.

**Syntax:** `R ⋈ S`

**Internal Representation:**
```
R ⋈ S = π_... (σ_(R.A = S.A) (R × S))
```

**Example:**

EMPLOYEES:

| E_ID | Name | Dept_ID |
|------|------|---------|
| E001 | Amit | D1 |
| E002 | Priya | D2 |
| E003 | Rahul | D1 |

DEPARTMENTS:

| Dept_ID | Dept_Name | Location |
|---------|-----------|----------|
| D1 | CS | Delhi |
| D2 | IT | Mumbai |

**Query:** Get employee names with their department locations
```
EMPLOYEES ⋈ DEPARTMENTS
```

**Result:**

| E_ID | Name | Dept_ID | Dept_Name | Location |
|------|------|---------|-----------|----------|
| E001 | Amit | D1 | CS | Delhi |
| E003 | Rahul | D1 | CS | Delhi |
| E002 | Priya | D2 | IT | Mumbai |

#### 3.1.2 Theta Join (⋈_θ)

Joins based on a specific condition (θ can be =, <, >, etc.)

**Syntax:** `R ⋈_condition S`

**Query:** Find employees with salary > department average (simplified example)
```
σ_Salary > 50000 (EMPLOYEES ⋈ DEPARTMENTS)
```

#### 3.1.3 Equijoin

A theta join where the condition is equality (=).

**Example:**
```
EMPLOYEES ⋈_(Dept_ID = Dept_ID) DEPARTMENTS
```

### 3.2 Intersection (∩) — The Common Elements Operator

**Definition:** Returns tuples that exist in **both** relations.

**Syntax:** `R ∩ S`

**Internal Representation:**
```
R ∩ S = R − (R − S)
```

**Properties:**
- Both relations must have same schema
- Commutative: `R ∩ S = S ∩ R`

**Example:**

STUDENTS_CS:

| SID | Name |
|-----|------|
| S1 | Amit |
| S2 | Priya |
| S3 | Rahul |

STUDENTS_IT:

| SID | Name |
|-----|------|
| S2 | Priya |
| S3 | Rahul |
| S4 | Sara |

**Query:** Find students in both CS and IT
```
STUDENTS_CS ∩ STUDENTS_IT
```

**Result:**

| SID | Name |
|-----|------|
| S2 | Priya |
| S3 | Rahul |

### 3.3 Division (÷) — The Inverse of Cartesian Product

**Definition:** Returns tuples from the first relation that relate to **ALL** tuples in the second relation.

**Syntax:** `R ÷ S`

**Internal Representation:**
```
R ÷ S = π_A(R) − π_A((π_A(R) × S) − R)
```

Where A is the set of attributes in R but not in S.

**Use Case:** "Find all X such that for every Y, X relates to Y"

**Example:**

ENROLLED (Students enrolled in courses):

| SID | CID |
|-----|-----|
| S1 | C1 |
| S1 | C2 |
| S1 | C3 |
| S2 | C1 |
| S2 | C2 |
| S3 | C1 |

COURSES_NEEDED (Courses all students must take):

| CID |
|-----|
| C1 |
| C2 |

**Query:** Find students enrolled in ALL required courses
```
ENROLLED ÷ COURSES_NEEDED
```

**Result:**

| SID |
|-----|
| S1 |
| S2 |

**Explanation:**
- S1 has C1, C2, C3 → Contains both C1 and C2 ✓
- S2 has C1, C2 → Contains both C1 and C2 ✓
- S3 has C1 only → Missing C2 ✗

### 3.4 Assignment (←)

**Definition:** Assigns the result of an expression to a temporary relation variable.

**Syntax:** `Temp ← Expression`

**Use:** Breaks complex queries into simpler steps

**Example:**
```
Temp1 ← σ_Dept='CS'(EMPLOYEES)
Result ← π_Name(Temp1)
```

---

## 4. Extended Operators

These operators enhance the capability of relational algebra for real-world scenarios.

### 4.1 Outer Joins

Designed to preserve tuples that would be lost in regular joins.

#### 4.1.1 Left Outer Join (⟕)

Preserves all tuples from the left relation, matching right relation where possible.

**Example:**
```
EMPLOYEES ⟕ DEPARTMENTS
```

| E_ID | Name | Dept_ID | Dept_Name | Location |
|------|------|---------|-----------|----------|
| E001 | Amit | D1 | CS | Delhi |
| E002 | Priya | D2 | IT | Mumbai |
| E003 | Rahul | D1 | CS | Delhi |
| E004 | NULL | NULL | NULL | NULL |

#### 4.1.2 Right Outer Join (⟖)

Preserves all tuples from the right relation.

#### 4.1.3 Full Outer Join (⟗)

Preserves all tuples from both relations.

### 4.2 Semi-Join (⋉/⋊)

Returns tuples from the first relation that match tuples in the second relation (based on join condition), but **only the first relation's attributes**.

**Syntax:** `R ⋉ S` or `R ⋊ S`

**Use:** Reduces data transfer in distributed databases

**Query:** Find departments that have employees (without listing employees)
```
DEPARTMENTS ⋉ EMPLOYEES
```

---

## 5. Practical Examples with Tables

Let's create a comprehensive database for a **University Management System** and demonstrate various relational algebra operations.

### Database Schema

**STUDENTS:**

| SID | SName | Major | GPA |
|-----|-------|-------|-----|
| S1 | Amit | CS | 3.8 |
| S2 | Priya | IT | 3.5 |
| S3 | Rahul | CS | 3.2 |
| S4 | Sara | MA | 3.9 |
| S5 | Vikram | IT | 3.6 |

**ENROLLMENT:**

| SID | CID | Grade |
|-----|-----|-------|
| S1 | C1 | A |
| S1 | C2 | B |
| S2 | C1 | A |
| S3 | C1 | C |
| S3 | C2 | B |
| S4 | C3 | A |

**COURSES:**

| CID | CName | Credits | Instructor |
|-----|-------|---------|------------|
| C1 | DBMS | 4 | Prof. Sharma |
| C2 | OS | 3 | Prof. Gupta |
| C3 | AI | 4 | Prof. Singh |

### Example 1: Find students with GPA > 3.5 enrolled in DBMS

**Step-by-step:**

1. Find students with GPA > 3.5:
```
HighGPA ← σ_GPA > 3.5(STUDENTS)
```

**Result:**

| SID | SName | Major | GPA |
|-----|-------|-------|-----|
| S1 | Amit | CS | 3.8 |
| S4 | Sara | MA | 3.9 |
| S5 | Vikram | IT | 3.6 |

2. Find students enrolled in DBMS (C1):
```
DBMS_Enrolled ← σ_CID='C1'(ENROLLMENT)
```

**Result:**

| SID | CID | Grade |
|-----|-----|-------|
| S1 | C1 | A |
| S2 | C1 | A |
| S3 | C1 | C |

3. Join to get final result:
```
Result ← HighGPA ⋈ DBMS_Enrolled
```

**Final Result:**

| SID | SName | Major | GPA | CID | Grade |
|-----|-------|-------|-----|-----|-------|
| S1 | Amit | CS | 3.8 | C1 | A |

### Example 2: Find courses taken by ALL CS majors

**Step-by-step:**

1. Find all CS major students:
```
CS_Students ← σ_Major='CS'(STUDENTS)
```

**Result:**

| SID | SName | Major | GPA |
|-----|-------|-------|-----|
| S1 | Amit | CS | 3.8 |
| S3 | Rahul | CS | 3.2 |

2. Get SID-CID pairs for CS students:
```
CS_Enrollment ← π_SID, CID(CS_Students ⋈ ENROLLMENT)
```

**Result:**

| SID | CID |
|-----|-----|
| S1 | C1 |
| S1 | C2 |
| S3 | C1 |
| S3 | C2 |

3. Get distinct courses taken by CS students:
```
Courses_By_CS ← π_CID(CS_Enrollment)
```

**Result:**

| CID |
|-----|
| C1 |
| C2 |

4. Find courses taken by ALL CS students (using division):
```
Result ← CS_Enrollment ÷ Courses_By_CS
```

**Final Result:**

| SID |
|-----|
| S1 |
| S3 |

### Example 3: Complex query using multiple operators

**Query:** Find names of students who are CS majors OR have GPA > 3.7, but NOT enrolled in OS

**Step-by-step:**

1. CS majors:
```
CS_Majors ← π_SName(σ_Major='CS'(STUDENTS))
```

2. High GPA students:
```
High_GPA ← π_SName(σ_GPA > 3.7(STUDENTS))
```

3. Union (CS majors OR High GPA):
```
Union_Result ← CS_Majors ∪ High_GPA
```

4. Students enrolled in OS (C2):
```
OS_Enrolled ← π_SID(σ_CID='C2'(ENROLLMENT))
```

5. Get SIDs of students in union result:
```
Union_SIDs ← π_SID(STUDENTS ⋈ Union_Result)
```

6. Difference (CS/HighGPA but NOT in OS):
```
Final_Result ← Union_SIDs − OS_Enrolled
```

7. Get names:
```
Result ← Final_Result ⋈ STUDENTS
```

---

## 6. SQL Mapping

Understanding how relational algebra maps to SQL is crucial for practical database work.

| Relational Algebra | SQL Equivalent | Example |
|--------------------|----------------|---------|
| **Selection (σ)** | WHERE clause | `SELECT * FROM Employees WHERE Dept='CS'` |
| **Projection (π)** | SELECT columns | `SELECT Name, Salary FROM Employees` |
| **Union (∪)** | UNION | `SELECT * FROM R UNION SELECT * FROM S` |
| **Difference (−)** | EXCEPT/MINUS | `SELECT * FROM R EXCEPT SELECT * FROM S` |
| **Cartesian Product (×)** | CROSS JOIN | `SELECT * FROM R CROSS JOIN S` |
| **Intersection (∩)** | INTERSECT | `SELECT * FROM R INTERSECT SELECT * FROM S` |
| **Join (⋈)** | JOIN/INNER JOIN | `SELECT * FROM R JOIN S ON R.id = S.id` |
| **Natural Join (⋈)** | NATURAL JOIN | `SELECT * FROM R NATURAL JOIN S` |
| **Left Outer Join (⟕)** | LEFT JOIN | `SELECT * FROM R LEFT JOIN S ON condition` |
| **Division (÷)** | NOT DIRECT (requires subquery) | See example below |

### SQL Examples for Our University Database

**Query 1: Selection and Projection**
```sql
-- Relational: π_SName, GPA(σ_GPA > 3.5(STUDENTS))
SELECT SName, GPA 
FROM STUDENTS 
WHERE GPA > 3.5;
```

**Query 2: Natural Join**
```sql
-- Relational: STUDENTS ⋈ ENROLLMENT
SELECT * 
FROM STUDENTS 
NATURAL JOIN ENROLLMENT;
```

**Query 3: Division (Finding students enrolled in ALL courses)**
```sql
-- Relational: ENROLLMENT ÷ COURSES
SELECT SID 
FROM ENROLLMENT 
WHERE CID IN (SELECT CID FROM COURSES)
GROUP BY SID 
HAVING COUNT(DISTINCT CID) = (SELECT COUNT(*) FROM COURSES);
```

**Query 4: Outer Join with Condition**
```sql
-- Relational: STUDENTS ⟕ ENROLLMENT
SELECT S.SID, S.SName, E.CID, E.Grade
FROM STUDENTS S
LEFT JOIN ENROLLMENT E ON S.SID = E.SID;
```

**Query 5: Complex Query**
```sql
-- Find students in CS department with A grade in DBMS
SELECT S.SName
FROM STUDENTS S
JOIN ENROLLMENT E ON S.SID = E.SID
JOIN COURSES C ON E.CID = C.CID
WHERE S.Major = 'CS' 
  AND E.Grade = 'A' 
  AND C.CName = 'DBMS';
```

---

## 7. Key Takeaways

### Core Concepts

1. **Relational Algebra** is a formal query language based on set theory and predicate logic
2. **Six Fundamental Operators**: Selection (σ), Projection (π), Union (∪), Difference (−), Cartesian Product (×), Rename (ρ)
3. **Derived Operators**: Join (⋈), Intersection (∩), Division (÷) can be expressed using fundamental operators
4. **Extended Operators**: Outer joins and semi-joins enhance capability for real-world queries

### Important Properties

| Property | Description |
|----------|-------------|
| **Closure** | Operations on relations always produce relations |
| **Closure Property** | Allows nesting of operations |
| **Set Operations** | Union, Intersection, Difference require compatible schemas |
| **Equivalence** | Multiple ways to express same query; DBMS optimizes execution |

### Query Execution Order

When processing queries, DBMS typically follows:

```
1. FROM (Cartesian Product/Joins)
2. WHERE (Selection conditions)
3. GROUP BY
4. HAVING
5. SELECT (Projection)
6. ORDER BY
```

### Common Patterns

- **Selection followed by Projection**: Filter then choose columns
- **Cartesian Product followed by Selection**: Basis of join operations
- **Nested Queries**: Division often implemented using subqueries
- **Aliases (Rename)**: Essential for self-joins and complex queries

---

## 8. Assessment Section

### Multiple Choice Questions (MCQs)

#### Level 1: Basic (Recall)

**Question 1:** Which operator is used to select specific columns from a relation?
- A) Selection (σ)
- B) Projection (π)
- C) Union (∪)
- D) Rename (ρ)

**Answer:** B) Projection (π)

---

**Question 2:** The Cartesian product of two relations with 5 and 7 tuples respectively will produce:
- A) 12 tuples
- B) 35 tuples
- C) 2 tuples
- D) 57 tuples

**Answer:** B) 35 tuples (5 × 7 = 35)

---

#### Level 2: Intermediate (Application)

**Question 3:** Given relations R(A, B) and S(B, C), which operation will give result with attributes A, B, C?
- A) R ∪ S
- B) R × S
- C) R − S
- D) π_A(R)

**Answer:** B) R × S (Cartesian product combines all attributes)

---

**Question 4:** What is the result of (R ∩ S) given:
- R = {1, 2, 3}
- S = {2, 3, 4}
- A) {1, 2, 3, 4}
- B) {2, 3}
- C) {1}
- D) {4}

**Answer:** B) {2, 3}

---

**Question 5:** Which join type preserves all tuples from the left relation only?
- A) Right Outer Join
- B) Full Outer Join
- C) Left Outer Join
- D) Natural Join

**Answer:** C) Left Outer Join

---

#### Level 3: Challenging (Analysis)

**Question 6:** Consider relations:
- ENROLLMENT(SID, CID)
- COURSES(CID, CName)

To find course names taken by student S1, which relational algebra expression is CORRECT?
- A) π_CName(σ_SID='S1'(ENROLLMENT)) × COURSES
- B) π_CName(σ_SID='S1'(ENROLLMENT ⋈ COURSES))
- C) σ_SID='S1'(ENROLLMENT) ∪ COURSES
- D) π_CID(ENROLLMENT) ÷ COURSES

**Answer:** B) π_CName(σ_SID='S1'(ENROLLMENT ⋈ COURSES))

---

**Question 7:** Division operator R ÷ S is applicable when:
- A) S has more attributes than R
- B) Attributes of S are a subset of attributes of R
- C) R and S have no common attributes
- D) R and S have exactly the same schema

**Answer:** B) Attributes of S are a subset of attributes of R

---

### Scenario-Based Questions

#### Scenario 1: Library Management System

**Context:** A library database has:
- BOOKS(BookID, Title, Author, Category)
- MEMBERS(MemberID, Name, MembershipType)
- BORROWINGS(MemberID, BookID, BorrowDate, ReturnDate)

**Question 8:** Write relational algebra to find names of members who have borrowed books in 'Science' category but never borrowed any 'Fiction' book.

**Answer:**
```
ScienceBorrowers ← π_MemberID(σ_Category='Science'(BOOKS ⋈ BORROWINGS))
FictionBorrowers ← π_MemberID(σ_Category='Fiction'(BOOKS ⋈ BORROWINGS))
Result ← π_Name(ScienceBorrowers − FictionBorrowers) ⋈ MEMBERS
```

---

#### Scenario 2: E-Commerce Database

**Context:**
- CUSTOMERS(CustomerID, Name, City, Email)
- ORDERS(OrderID, CustomerID, OrderDate, TotalAmount)
- PRODUCTS(ProductID, ProductName, Category, Price)
- ORDER_ITEMS(OrderID, ProductID, Quantity)

**Question 9:** Find the total amount spent by customers from 'Delhi' on 'Electronics' products.

**Answer:**
```
DelhiCustomers ← σ_City='Delhi'(CUSTOMERS)
Electronics ← σ_Category='Electronics'(PRODUCTS)
DelhiElectronics ← DelhiCustomers ⋈ ORDERS ⋈ ORDER_ITEMS ⋈ Electronics
Result ← π_Name, TotalAmount(DelhiElectronics)
```

**SQL Equivalent:**
```sql
SELECT C.Name, SUM(OI.Quantity * P.Price) AS TotalSpent
FROM CUSTOMERS C
JOIN ORDERS O ON C.CustomerID = O.CustomerID
JOIN ORDER_ITEMS OI ON O.OrderID = OI.OrderID
JOIN PRODUCTS P ON OI.ProductID = P.ProductID
WHERE C.City = 'Delhi' AND P.Category = 'Electronics'
GROUP BY C.CustomerID, C.Name;
```

---

#### Scenario 3: Employee Database (Complex Division)

**Context:**
- EMPLOYEES(EmpID, Name, Department, Salary)
- SKILLS(EmpID, SkillName, ProficiencyLevel)
- REQUIRED_SKILLS(SkillName)

**Question 10:** Find employee IDs who possess ALL skills listed in REQUIRED_SKILLS table.

**Answer:**
```
EmployeeSkills ← π_EmpID, SkillName(SKILLS)
Required ← π_SkillName(REQUIRED_SKILLS)
Result ← EmployeeSkills ÷ Required
```

**Explanation:** The division operation finds employees whose skill set includes every skill in the required skills table.

---

### True/False Questions

**Question 11:** Relational algebra operators can be nested to form complex queries.
- A) True
- B) False

**Answer:** A) True — This is called closure property

---

**Question 12:** The selection operator reduces the number of columns in the result.
- A) True
- B) False

**Answer:** B) False — Selection reduces rows (horizontal), Projection reduces columns (vertical)

---

### Fill in the Blanks

**Question 13:** The operator _____ is used to eliminate duplicate tuples in the result.

**Answer:** Projection (π)

---

**Question 14:** A theta join with equality condition is called _____.

**Answer:** Equijoin

---

### Short Answer Questions

**Question 15:** Explain why Cartesian product is rarely used directly in queries.

**Answer:** Cartesian product produces the cross-product of two relations, resulting in a massive number of tuples (m × n). This is computationally expensive and produces mostly meaningless combinations. In practice, Cartesian product is always followed by Selection to create meaningful Joins that match related tuples.

---

**Question 16:** How does Natural Join differ from Theta Join?

**Answer:** Natural Join automatically matches tuples based on attributes with the same name and value in both relations, requiring no explicit condition. Theta Join requires an explicit join condition (predicate) that can use any comparison operator (=, <, >, etc.). Natural Join is essentially an Equijoin on common attribute names.

---

## Conclusion

This comprehensive study material covers all aspects of Relational Algebra as required by the Delhi University Ge3A syllabus. The concepts presented here form the theoretical foundation for understanding how database management systems process and optimize queries. Master these operators and their SQL equivalents to become proficient in database query writing and optimization.

---

*Generated for BSc Physical Science (CS) - Delhi University, NEP 2024*
*Subject: Database Management Systems (Ge3A)*