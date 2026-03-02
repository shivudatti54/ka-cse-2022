# Relational Algebra Operators

## A Comprehensive Study Material for Database Management Systems

---

## 1. Introduction

Relational Algebra forms the theoretical foundation of relational database management systems (RDBMS). Developed by Edgar F. Codd in 1970, it provides a set of mathematical operations that work on relations (tables) to produce new relations as results. Understanding Relational Algebra is crucial for any computer science student because it:

- **Forms the backbone of SQL**: Every SQL query you write translates to one or more relational algebra operations internally
- **Enables query optimization**: Database optimizers use relational algebra to determine the most efficient way to execute queries
- **Provides formal foundations**: Unlike SQL which is declarative, relational algebra offers procedural query processing

### Real-World Relevance

Consider a university database system like the one used at Delhi University. When a student requests "list all courses enrolled by students in BSc CS (Hons) who have scored above 85%", the database engine internally breaks this query into multiple relational algebra operations: Selection (to filter students by program), Projection (to extract relevant columns), Join (to connect with enrollment data), and more. This systematic approach ensures accurate and efficient data retrieval.

---

## 2. Fundamental Relational Algebra Operators

The six fundamental (basic) operators in relational algebra form the foundation upon which all other operations are built.

### 2.1 SELECT (σ) - Selection Operator

The Selection operator filters tuples (rows) from a relation based on a condition. It is a unary operator that returns a relation containing only those tuples that satisfy the specified predicate.

**Syntax:**
```
σ<condition>(RelationName)
```

**Properties:**
- The result has the same schema as the original relation
- Selectivity reduces the number of tuples
- Multiple conditions can be combined using AND (∧), OR (∨), and NOT (¬)
- Commutative: σ₁(σ₂(R)) = σ₂(σ₁(R))

**Example 1: Simple Selection**

Given the **STUDENT** relation:

| RollNo | Name | Age | Dept | CGPA |
|--------|------|-----|------|------|
| 101 | Amit | 20 | CS | 8.5 |
| 102 | Priya | 19 | CS | 9.2 |
| 103 | Rahul | 21 | IT | 7.8 |
| 104 | Sneha | 20 | CS | 8.9 |

Query: Find all students in the CS department
```
σDept='CS'(STUDENT)
```

**Result:**

| RollNo | Name | Age | Dept | CGPA |
|--------|------|-----|------|------|
| 101 | Amit | 20 | CS | 8.5 |
| 102 | Priya | 19 | CS | 9.2 |
| 104 | Sneha | 20 | CS | 8.9 |

**Example 2: Compound Condition**

Query: Find students with CGPA greater than 8.5 in CS department
```
σDept='CS' ∧ CGPA>8.5(STUDENT)
```

**Result:**

| RollNo | Name | Age | Dept | CGPA |
|--------|------|-----|------|------|
| 102 | Priya | 19 | CS | 9.2 |
| 104 | Sneha | 20 | CS | 8.9 |

---

### 2.2 PROJECT (π) - Projection Operator

The Projection operator selects specific columns (attributes) from a relation, effectively creating a vertical subset. It eliminates duplicate tuples in the result (by definition, relations are sets).

**Syntax:**
```
π<attribute1, attribute2, ...>(RelationName)
```

**Properties:**
- The result schema contains only the specified attributes
- Removes duplicate tuples (set property)
- Can reorder attributes in the output
- Commutative with itself but not generally with Selection

**Example 1: Simple Projection**

Query: Get names and CGPA of all students
```
πName, CGPA(STUDENT)
```

**Result:**

| Name | CGPA |
|------|------|
| Amit | 8.5 |
| Priya | 9.2 |
| Rahul | 7.8 |
| Sneha | 8.9 |

**Example 2: Combined Selection and Projection**

Query: Get names of CS students with CGPA > 8.0
```
πName(σDept='CS' ∧ CGPA>8.0(STUDENT))
```

**Result:**

| Name |
|------|
| Amit |
| Priya |
| Sneha |

---

### 2.3 UNION (∪) - Union Operator

The Union operator combines tuples from two relations that have the same schema (compatible relations). The result contains all tuples from both relations, with duplicates eliminated.

**Syntax:**
```
Relation1 ∪ Relation2
```

**Requirements for Union Compatibility:**
- Both relations must have the same number of attributes
- Corresponding attributes must have the same domain

**Properties:**
- Commutative: R ∪ S = S ∪ R
- Associative: (R ∪ S) ∪ T = R ∪ (S ∪ T)
- Idempotent: R ∪ R = R

**Example:**

Given **CS_STUDENTS** table:
| RollNo | Name |
|--------|------|
| 101 | Amit |
| 102 | Priya |

And **IT_STUDENTS** table:
| RollNo | Name |
|--------|------|
| 103 | Rahul |
| 101 | Amit |

Query: Find all students in either CS or IT
```
CS_STUDENTS ∪ IT_STUDENTS
```

**Result:**

| RollNo | Name |
|--------|------|
| 101 | Amit |
| 102 | Priya |
| 103 | Rahul |

*Note: RollNo 101 (Amit) appears only once due to set semantics*

---

### 2.4 SET DIFFERENCE (−) - Minus Operator

The Set Difference operator returns tuples that exist in the first relation but not in the second. It is essential for implementing "NOT IN" or "EXCEPT" operations.

**Syntax:**
```
Relation1 − Relation2
```

**Properties:**
- Not commutative: R − S ≠ S − R
- Not associative
- Requires union compatibility

**Example:**

Query: Find students in CS department but not in the honor roll (assume HONOR_ROLL contains RollNos of honor students)
```
πRollNo(σDept='CS'(STUDENT)) − HONOR_ROLL
```

**Result:** Returns RollNos of CS students who are NOT in the honor roll

---

### 2.5 CARTESIAN PRODUCT (×) - Cross Product

The Cartesian Product combines every tuple from the first relation with every tuple from the second relation. This creates a relation with all possible combinations.

**Syntax:**
```
Relation1 × Relation2
```

**Properties:**
- If Relation1 has n1 tuples and a1 attributes, and Relation2 has n2 tuples and a2 attributes, then:
  - Result has n1 × n2 tuples
  - Result has a1 + a2 attributes
- Not commutative but can be combined with Selection for meaningful results

**Example:**

**STUDENT** (n1=3, a1=3):
| ID | Name | DeptID |
|----|------|--------|
| 1 | Amit | D1 |
| 2 | Priya | D1 |
| 3 | Rahul | D2 |

**DEPARTMENT** (n2=2, a2=2):
| DeptID | DeptName |
|--------|----------|
| D1 | CS |
| D2 | IT |

Query:
```
STUDENT × DEPARTMENT
```

**Result (3 × 2 = 6 tuples):**

| ID | Name | DeptID | DeptID | DeptName |
|----|------|--------|--------|----------|
| 1 | Amit | D1 | D1 | CS |
| 1 | Amit | D1 | D2 | IT |
| 2 | Priya | D1 | D1 | CS |
| 2 | Priya | D1 | D2 | IT |
| 3 | Rahul | D2 | D1 | CS |
| 3 | Rahul | D2 | D2 | IT |

---

### 2.6 RENAME (ρ) - Rename Operator

The Rename operator is essential for avoiding naming conflicts and for referencing the same relation multiple times in a query. It allows us to assign new names to relations or their attributes.

**Syntax:**
```
ρnewName(RelationName)                          // Rename relation
ρnewName(attr1, attr2, ...)(RelationName)       // Rename relation and attributes
ρS(T)                                           // Rename T to S
```

**Properties:**
- Does not change the data, only the names
- Essential for self-joins and complex queries

**Example:**

Query: Find students who have the same department as student with RollNo 101
```
πS1.Name(σS1.DeptID=S2.DeptID ∧ S2.RollNo=101 (ρS1(STUDENT) × ρS2(STUDENT)))
```

This query uses the Rename operator to create two copies of STUDENT relation (S1 and S2) to compare departments.

---

## 3. Additional Relational Algebra Operators

These operators are derived from the fundamental operators but provide significant convenience.

### 3.1 INTERSECTION (∩)

Returns tuples common to both relations. Can be expressed using set difference:
```
R ∩ S = R − (R − S)
```

**Properties:**
- Commutative: R ∩ S = S ∩ R
- Requires union compatibility

**Example:**

Query: Find students who are both in CS department and on honor roll
```
πRollNo(σDept='CS'(STUDENT)) ∩ HONOR_ROLL
```

---

### 3.2 NATURAL JOIN (⋈)

The Natural Join automatically matches tuples based on **common attribute names** with the same values. It performs:
1. Cartesian Product
2. Selection on matching values of common attributes
3. Projection to remove duplicate common attributes

**Syntax:**
```
Relation1 ⋈ Relation2
```

**Properties:**
- Commutative (with some nuances): R ⋈ S ≈ S ⋈ R
- Associative: (R ⋈ S) ⋈ T = R ⋈ (S ⋈ T)

**Example:**

**ENROLLMENT**:
| StudID | CourseID | Grade |
|--------|----------|-------|
| 101 | C1 | A |
| 101 | C2 | B |
| 102 | C1 | A |

**COURSE**:
| CourseID | CourseName | Credits |
|----------|------------|---------|
| C1 | DBMS | 4 |
| C2 | OS | 3 |

Query:
```
ENROLLMENT ⋈ COURSE
```

**Result:**

| StudID | CourseID | Grade | CourseName | Credits |
|--------|----------|-------|------------|---------|
| 101 | C1 | A | DBMS | 4 |
| 101 | C2 | B | OS | 3 |
| 102 | C1 | A | DBMS | 4 |

---

### 3.3 THETA JOIN (⋈θ)

The Theta Join allows joining based on any condition (θ can be =, <, >, ≤, ≥, ≠).

**Syntax:**
```
Relation1 ⋈<condition> Relation2
```

This is equivalent to:
```
σ<condition>(Relation1 × Relation2)
```

**Example:**

Query: Find all student-course combinations where the student's ID is greater than the course credits
```
STUDENT ⋈ID>Credits COURSE
```

---

### 3.4 EQUI-JOIN

A specific case of Theta Join where the condition uses equality (=).

**Example:**
```
STUDENT ⋈ STUDENT.DeptID = DEPARTMENT.DeptID DEPARTMENT
```

---

### 3.5 OUTER JOINS

Outer joins preserve tuples that would be lost in a natural join by including NULL values for unmatched records.

#### 3.5.1 LEFT OUTER JOIN (⋈L)

Preserves all tuples from the left relation, filling NULL for unmatched right tuples.

#### 3.5.2 RIGHT OUTER JOIN (⋈R)

Preserves all tuples from the right relation.

#### 3.5.3 FULL OUTER JOIN (⋈F)

Preserves all tuples from both relations.

**Example:**

**STUDENT**:
| ID | Name |
|----|------|
| 1 | Amit |
| 2 | Priya |
| 3 | Rahul |

**ENROLLMENT**:
| StudID | Course |
|--------|--------|
| 1 | DBMS |
| 1 | OS |

**LEFT OUTER JOIN** (Student ⋈L Enrollment):

| ID | Name | StudID | Course |
|----|------|--------|--------|
| 1 | Amit | 1 | DBMS |
| 1 | Amit | 1 | OS |
| 2 | Priya | NULL | NULL |
| 3 | Rahul | NULL | NULL |

---

### 3.6 DIVISION (÷)

The Division operator is used for "for all" or "universal" queries. Given R(X, Y) and S(Y), R ÷ S returns tuples in X that are associated with **every** tuple in S.

**Syntax:**
```
R ÷ S
```

**Requirements:**
- Attributes of S must be a subset of attributes of R
- Result contains attributes of R not in S

**Example:**

**STUDENT_COURSE**:
| StudID | CourseID |
|--------|----------|
| S1 | C1 |
| S1 | C2 |
| S1 | C3 |
| S2 | C1 |
| S2 | C2 |

**REQUIRED_COURSES**:
| CourseID |
|----------|
| C1 |
| C2 |

Query: Find students who have enrolled in **all** required courses
```
STUDENT_COURSE ÷ REQUIRED_COURSES
```

**Result:**
| StudID |
|--------|
| S1 |
| S2 |

*S1 is included because they have both C1 and C2; S2 is also included for the same reason*

---

## 4. Extended Relational Algebra Operators

### 4.1 Aggregate Functions

Relational algebra can be extended to include aggregate functions that perform computations on sets of tuples.

**Syntax:**
```
G1, G2, ..., Gn ℑF1(A1), F2(A2), ..., Fm(Am)(R)
```

Where:
- G1, G2, ..., Gn are grouping attributes
- F1, F2, ..., Fm are aggregate functions (SUM, AVG, MIN, MAX, COUNT)
- A1, A2, ..., Am are attribute names

**Example:**

Query: Find the average CGPA for each department
```
Dept ℑAVG(CGPA)(STUDENT)
```

**Result:**
| Dept | AVG(CGPA) |
|------|-----------|
| CS | 8.87 |
| IT | 7.8 |

---

### 4.2 Generalized Projection

Extends projection with arithmetic operations.

**Example:**

Query: Calculate bonus (10% of CGPA) for all students
```
πName, CGPA, CGPA*0.10 AS Bonus(STUDENT)
```

---

## 5. Complex Query Examples

### Example 1: Multi-Table Query

Consider a University Database:
- **STUDENT**(RollNo, Name, DeptID, Age)
- **ENROLLMENT**(RollNo, CourseID, Grade)
- **COURSE**(CourseID, CourseName, Credits, DeptID)

**Query:** Find names of students enrolled in "Database Management Systems" offered by the CS department

**Step-by-step Relational Algebra:**

```
πName(
    STUDENT ⋈
    (πRollNo(σCourseName='Database Management Systems'(
        COURSE ⋈ 
        σDeptID='CS'(COURSE)
    )))
)
```

### Example 2: Division for Complex Queries

**Query:** Find courses that have been enrolled by all students in the CS department

```
(πRollNo, CourseID(ENROLLMENT) ÷ πRollNo(σDept='CS'(STUDENT))) ⋈ COURSE
```

---

## 6. Commutativity in Relational Algebra

Understanding commutativity is crucial for query optimization:

| Operator | Commutative? | Notes |
|----------|---------------|-------|
| Selection (σ) | Yes | σp(σq(R)) = σq(σp(R)) |
| Projection (π) | Yes (with self) | πA(πB(R)) = πA(R) if A ⊆ B |
| Union (∪) | Yes | R ∪ S = S ∪ R |
| Intersection (∩) | Yes | R ∩ S = S ∩ R |
| Cartesian Product (×) | Yes | R × S = S × R |
| Natural Join (⋈) | Yes* | R ⋈ S ≈ S ⋈ R (column ordering may differ) |
| Difference (−) | No | R − S ≠ S − R |
| Division (÷) | No | R ÷ S ≠ S ÷ R |
| Join (⋈θ) | No (generally) | Depends on θ |

---

## 7. Key Takeaways

1. **Six Fundamental Operators**: Select, Project, Union, Set Difference, Cartesian Product, and Rename form the foundation of all relational algebra operations.

2. **Selection (σ)**: Filters rows based on conditions; preserves all attributes; commutative with multiple selections.

3. **Projection (π)**: Selects specific columns; eliminates duplicates; can be combined with selection for efficient queries.

4. **Union Compatibility**: Union, Intersection, and Difference operations require both relations to have the same number of attributes with compatible domains.

5. **Join Operations**: Natural join automatically matches on common attributes; theta joins allow arbitrary conditions; outer joins preserve unmatched tuples.

6. **Division Operator**: Implements "for all" queries; essential for queries like "find students enrolled in ALL courses".

7. **Rename Operator**: Critical for self-joins and avoiding ambiguity in complex queries involving the same relation multiple times.

8. **Query Optimization Understanding**: Knowing commutativity properties helps understand how database optimizers reorder operations for efficiency.

9. **SQL Connection**: Every SQL query translates to relational algebra operations; understanding RA helps in writing better SQL and understanding query execution plans.

10. **Practical Application**: These operators are used internally by database management systems to process, optimize, and execute user queries efficiently.

---

## 8. Assessment Items (MCQs)

### Level 1: Basic Understanding

1. Which operator is used to filter rows in a relation?
   - A) Project (π)
   - B) Select (σ)
   - C) Union (∪)
   - D) Rename (ρ)
   - **Answer: B**

### Level 2: Intermediate Concepts

2. What is the result of the Cartesian product of two relations R and S where |R| = 100 tuples and |S| = 50 tuples?
   - A) 150 tuples
   - B) 50 tuples
   - C) 5000 tuples
   - D) 2 tuples
   - **Answer: C**

3. Which of the following is NOT a fundamental relational algebra operator?
   - A) Selection
   - B) Projection
   - C) Intersection
   - D) Rename
   - **Answer: C**

### Level 3: Advanced & Complex

4. Given relations R(A,B) and S(B), if R contains tuples {(1,2), (1,3), (2,2)} and S contains {2}, what is R ÷ S?
   - A) {(1,2), (1,3), (2,2)}
   - B) {(1), (2)}
   - C) {(1)}
   - D) {(2)}
   - **Answer: C** *(Only attribute A values associated with ALL values in S)*

5. Consider relations STUDENT(SID, Name, DeptID) and ENROLLMENT(SID, CourseID). To find students enrolled in at least one course, which expression is correct?
   - A) STUDENT − ENROLLMENT
   - B) πSID(STUDENT) ∩ πSID(ENROLLMENT)
   - C) STUDENT ⋈ ENROLLMENT
   - D) STUDENT ÷ ENROLLMENT
   - **Answer: B**

### Level 4: Commutativity & Properties

6. Which of the following statements is TRUE regarding commutativity?
   - A) Set Difference is commutative
   - B) Natural Join is commutative
   - C) Division is commutative
   - D) Cartesian Product is not commutative
   - **Answer: B** *(Natural Join is approximately commutative - result contains same tuples but column ordering may differ)*

7. The expression σp(σq(R)) = σq(σp(R)) demonstrates which property?
   - A) Associativity
   - B) Distributivity
   - C) Commutativity of Selection
   - D) Idempotence
   - **Answer: C**

### Level 5: Complex Expressions

8. For the relations R(A,B) and S(A,B), which expression correctly finds tuples in R that are NOT in S?
   - A) R ∩ S
   - B) R ∪ S
   - C) R − S
   - D) R × S
   - **Answer: C**

9. A query asks to "Find all courses enrolled by ALL students in BSc CS". This is an example of which type of query?
   - A) Simple selection
   - B) Join query
   - C) Division query
   - D) Aggregation query
   - **Answer: C**

### Level 6: Critical Thinking

10. Given the relations:
    - EMPLOYEE(EmpID, Name, DeptID)
    - DEPARTMENT(DeptID, DeptName)
    
    To find department names that have NO employees, which approach is CORRECT?
    
    A) πDeptName(DEPARTMENT) − πDeptName(EMPLOYEE ⋈ DEPARTMENT)
    
    B) πDeptName(DEPARTMENT) ∩ πDeptName(EMPLOYEE ⋈ DEPARTMENT)
    
    C) σCount=0(DeptID ℑCOUNT(EmpID)(EMPLOYEE ⋈ DEPARTMENT))
    
    D) All of the above
    
    **Answer: A** *(Finds departments in DEPARTMENT that don't appear in the join result)*

---

## References

- Database Management Systems, Raghu Ramakrishnan & Johannes Gehrke
- Database System Concepts, Silberschatz, Korth & Sudarshan
- Delhi University BSc (Hons) Computer Science Syllabus, NEP 2024 UGCF

---

*This study material is designed to help Delhi University students master Relational Algebra operators, providing both theoretical foundations and practical examples essential for database management system examinations.*