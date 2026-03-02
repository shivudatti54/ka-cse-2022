# Functional Dependencies: Comprehensive Study Material

## Database Management Systems — BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

### What are Functional Dependencies?

A **Functional Dependency (FD)** is a fundamental concept in relational database design that describes the relationship between attributes in a relation. In simpler terms, a functional dependency represents a constraint between two sets of attributes in a database relation. It states that if we know the value of one set of attributes (the determinant), we can uniquely determine the value of another set of attributes (the dependent).

### Real-World Relevance

Functional dependencies are crucial in modern database systems for several reasons:

1. **Data Integrity**: FDs help maintain data consistency by ensuring that relationships between data elements are properly enforced.
2. **Database Design**: They are the foundation of **normalization**, a process used to organize database tables to reduce redundancy and improve data integrity.
3. **Query Optimization**: Database query optimizers use functional dependencies to determine efficient query execution plans.
4. **Schema Design**: Understanding FDs helps database designers create robust schemas that accurately represent real-world entities and relationships.

### Importance in Delhi University Syllabus

The topic of Functional Dependencies is a core component of the Database Management Systems paper in the BSc (Hons) Computer Science curriculum under NEP 2024 UGCF. This chapter carries significant weight in both theoretical examinations and practical sessions.

---

## 2. Fundamentals of Functional Dependencies

### Formal Definition

Let R be a relation schema, and let X and Y be subsets of R. A **functional dependency** X → Y holds on R if and only if for every possible relation r(R), for all tuples t1 and t2 in r:

```
If t1[X] = t2[X], then t1[Y] = t2[Y]
```

This means: "Y is functionally dependent on X" or "X functionally determines Y."

### Notation

- **X → Y**: X determines Y (X is the left-hand side, Y is the right-hand side)
- **X → Y** is read as "X arrow Y" or "X determines Y"
- X and Y are sets of attributes

### Types of Functional Dependencies

#### 1. Trivial Functional Dependency

A functional dependency X → Y is **trivial** if Y is a subset of X.

```
Example: {A, B} → {A} is trivial because {A} ⊆ {A, B}
Example: {StudentID, Name} → {StudentID} is trivial
```

#### 2. Non-Trivial Functional Dependency

A functional dependency X → Y is **non-trivial** if Y is not a subset of X.

```
Example: {StudentID} → {StudentName, Address} is non-trivial
Example: {EmpID} → {DeptID} is non-trivial (assuming one employee per department)
```

#### 3. Completely Non-Trivial Functional Dependency

A functional dependency X → Y is **completely non-trivial** if X ∩ Y = ∅ (X and Y share no common attributes).

```
Example: {StudentID} → {CourseID} is completely non-trivial
```

---

## 3. Armstrong's Axioms

Armstrong's axioms are a set of inference rules used to derive all functional dependencies from a given set of functional dependencies. These axioms were formulated by William Armstrong in 1974.

### Primary Axioms

#### 1. Reflexivity (Axiom of Irrelevance)

If Y ⊆ X, then X → Y

```
Example: If we have {A, B}, then {A, B} → {A}
Example: {StudentID, Name} → {StudentID}
```

#### 2. Augmentation (Axiom of Augmentation)

If X → Y, then XZ → YZ for any Z

```
Example: If {StudentID} → {StudentName}, then {StudentID, Course} → {StudentName, Course}
Informal: You can add the same attributes to both sides of an FD
```

#### 3. Transitivity (Axiom of Transitivity)

If X → Y and Y → Z, then X → Z

```
Example: If {StudentID} → {DepartmentID} and {DepartmentID} → {DepartmentHead},
         then {StudentID} → {DepartmentHead}
```

### Derived Rules (Secondary Axioms)

These rules can be derived from the primary axioms:

#### 1. Union (Additive Rule)

If X → Y and X → Z, then X → YZ

```
Proof: X → Y (given)
       X → Z (given)
       X → XY (augmentation of X → Y with X)
       XY → YZ (augmentation of Y → Z with X)
       Therefore, X → Z (transitivity)
```

#### 2. Decomposition (Projective Rule)

If X → YZ, then X → Y and X → Z

```
Example: If {StudentID} → {Name, Address}, then {StudentID} → {Name}
```

#### 3. Pseudotransitivity

If X → Y and WY → Z, then WX → Z

```
Example: If {DeptID} → {DeptName} and {ManagerID, DeptName} → {ProjectID},
         then {ManagerID, DeptID} → {ProjectID}
```

#### 4. Composition

If X → Y and W → Z, then XW → YZ

---

## 4. Attribute Closure

### Definition

The **attribute closure** of a set of attributes X (denoted as X⁺ or X⁺) is the set of all attributes that can be functionally determined by X using Armstrong's axioms.

### Algorithm to Compute Attribute Closure

```
Algorithm: Compute Attribute Closure (X⁺)
Input: Set of attributes X, Set of FDs F
Output: Closure of X (X⁺)

1. Initialize X⁺ = X
2. Repeat:
   a. For each FD Y → Z in F:
      If Y ⊆ X⁺, then add Z to X⁺
   b. Until no new attributes are added to X⁺
3. Return X⁺
```

### Example: Computing Attribute Closure

**Given:**
- Relation: R(A, B, C, D, E, F)
- FDs: {A → B}, {B → C}, {A, E → F}, {C, D → E}

**Problem:** Find (A, D)⁺

**Solution:**

| Iteration | Attributes in X⁺ | FDs Applied | New Attributes Added |
|-----------|-------------------|-------------|----------------------|
| Initial   | {A, D}            | -           | -                    |
| 1         | {A, D, B}         | A → B       | B                    |
| 2         | {A, D, B, C}      | B → C       | C                    |
| 3         | {A, D, B, C, E}   | C, D → E    | E                    |
| 4         | {A, D, B, C, E, F}| A, E → F    | F                    |

**Final Result:** (A, D)⁺ = {A, B, C, D, E, F}

### Applications of Attribute Closure

1. **Determining Keys**: If X⁺ = all attributes of the relation, then X is a superkey
2. **Checking FDs**: To verify if an FD X → Y follows from a set F, check if Y ⊆ X⁺
3. **Computing Canonical Cover**: Essential step in finding minimal covers

---

## 5. Keys and Superkeys

### Superkey

A **superkey** is a set of attributes K of relation R such that for every possible relation r(R), no two tuples can have the same values for all attributes in K. In other words, K uniquely identifies tuples in the relation.

**Formal Definition:** K is a superkey of R if K → all attributes of R (K⁺ = R)

### Candidate Key

A **candidate key** is a minimal superkey — it is a superkey but no proper subset of it is a superkey.

**Properties:**
- Uniquely identifies each tuple
- Minimal (no proper subset is a superkey)
- There can be multiple candidate keys

### Primary Key

The **primary key** is the candidate key selected by the database designer to uniquely identify tuples. One candidate key is chosen as the primary key; others become alternate keys.

### Prime and Non-Prime Attributes

- **Prime Attributes**: Attributes that are part of any candidate key
- **Non-Prime Attributes**: Attributes that are not part of any candidate key

### Example: Identifying Keys

**Given:**
- Relation: R(A, B, C, D)
- FDs: {A → B}, {B → C}, {C → D}

**Solution:**

1. Compute closures:
   - A⁺ = {A, B, C, D} ✓ (A is a candidate key)
   - B⁺ = {B, C, D} ✗
   - C⁺ = {C, D} ✗
   - AB⁺ = {A, B, C, D} ✓ (AB is a superkey but not minimal)
   - AC⁺ = {A, C, B, D} ✓ (AC is a superkey but not minimal)

2. **Candidate Keys**: {A}
3. **Prime Attributes**: {A}
4. **Non-Prime Attributes**: {B, C, D}

---

## 6. Canonical Cover (Minimal Cover)

### Definition

The **canonical cover** (or minimal cover) of a set of functional dependencies F is a minimal set of functional dependencies that is equivalent to F. A canonical cover has no redundant FDs and no extraneous attributes in any FD.

### Properties of Canonical Cover

1. **No redundant FDs**: No FD in the cover can be inferred from the other FDs
2. **No extraneous attributes**: No attribute on the left-hand side can be removed without changing the closure
3. **Right-hand side is single-valued**: Each FD has a single attribute on the right-hand side

### Algorithm to Find Canonical Cover

```
Algorithm: Find Canonical Cover
Input: Set of FDs F
Output: Canonical Cover Fc

1. Split FDs so RHS is single attribute
2. Remove extraneous attributes from LHS
3. Remove redundant FDs
4. Return the result
```

### Example: Computing Canonical Cover

**Given:**
- Relation: R(A, B, C, D)
- FDs: {A → BC}, {B → C}, {AB → D}

**Step 1: Split FDs**
- F₁: {A → B}
- F₂: {A → C}
- F₃: {B → C}
- F₄: {A → D}

**Step 2: Remove Extraneous Attributes**

Check F₄: {A → D}
- Is A extraneous in AB → D? Check if A⁺ using {A → B, A → C, B → C} gives D
- A⁺ = {A, B, C} (doesn't include D)
- A is NOT extraneous

**Step 3: Remove Redundant FDs**

Check F₁: {A → B}
- Compute closure of LHS using remaining FDs: {A → C, B → C, A → D}
- A⁺ = {A, C, D}
- B is NOT in A⁺, so F₁ is NOT redundant

Check F₂: {A → C}
- Using {A → B, B → C, A → D}
- A⁺ = {A, B, C, D}
- C is in A⁺, so F₂ is REDUNDANT → Remove it

**Final Canonical Cover:**
- {A → B}
- {B → C}
- {A → D}

---

## 7. Normal Forms and Functional Dependencies

Normal forms define the level of normalization of a database schema based on functional dependencies.

### First Normal Form (1NF)

A relation is in 1NF if it contains only atomic (indivisible) values — no repeating groups or arrays.

```
❌ Not in 1NF: StudentCourses = {StudentID, Courses[]}  // Courses is multi-valued
✓ In 1NF: StudentCourse = {StudentID, CourseName}  // Atomic values
```

### Second Normal Form (2NF)

A relation is in 2NF if:
1. It is in 1NF
2. No non-prime attribute is partially dependent on a candidate key (no partial dependency)

```
Example of partial dependency (NOT in 2NF):
Relation: R(StudentID, CourseID, StudentName, CourseFee)
FDs: {StudentID, CourseID} → {StudentName, CourseFee}
     {StudentID} → {StudentName}

Problem: StudentName is partially dependent on {StudentID, CourseID}
Solution: Decompose into:
  - R1(StudentID, StudentName)
  - R2(StudentID, CourseID, CourseFee)
```

### Third Normal Form (3NF)

A relation R is in 3NF if for every FD X → A in F:
1. X is a superkey, OR
2. Each attribute A (not in X) is prime

```
Example: 
Relation: R(StudentID, DeptID, DeptName, Location)
FDs: {StudentID} → {DeptID}
     {DeptID} → {DeptName, Location}

Violation: DeptID → DeptName violates 3NF (DeptID is not a superkey, 
DeptName is not prime)
Solution: Decompose into:
  - R1(StudentID, DeptID)
  - R2(DeptID, DeptName, Location)
```

### Boyce-Codd Normal Form (BCNF)

A relation R is in BCNF if for every FD X → A in F, X is a superkey.

```
Example:
Relation: R(StudentID, AdvisorID)
FDs: {StudentID} → {AdvisorID}
     {AdvisorID} → {StudentID}

This is in BCNF because both StudentID and AdvisorID are superkeys
```

### Comparison of Normal Forms

| Normal Form | Requirement | Redundancy | Decomposition |
|-------------|-------------|-------------|---------------|
| 1NF | Atomic values | High | None |
| 2NF | 1NF + no partial dependencies | Medium | Required |
| 3NF | 1NF + no transitive dependencies | Low | Required |
| BCNF | 1NF + X must be superkey | Very Low | May lose dependencies |

---

## 8. Practical Examples with SQL Context

### Example 1: Employee-Department Database

Consider a relation **Employee(EmpID, EmpName, DeptID, DeptName, Location)**

```
FDs:
- EmpID → EmpName, DeptID
- DeptID → DeptName, Location

Analysis:
- Candidate Key: {EmpID}
- Prime Attributes: {EmpID}
- Non-Prime Attributes: {EmpName, DeptID, DeptName, Location}

Normalization:
- Decompose to:
  - Employee1(EmpID, EmpName, DeptID)
  - Department(DeptID, DeptName, Location)
```

**SQL DDL Representation:**

```sql
-- Normalized Tables
CREATE TABLE Department (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50) NOT NULL,
    Location VARCHAR(100) NOT NULL
);

CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(100) NOT NULL,
    DeptID INT NOT NULL,
    FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
);
```

### Example 2: Course Enrollment System

Consider a relation **Enrollment(StudentID, CourseID, Grade, StudentName, CourseName, InstructorID)**

```
FDs:
- StudentID → StudentName
- CourseID → CourseName, InstructorID
- StudentID, CourseID → Grade

Analysis:
- Candidate Keys: {StudentID, CourseID}
- Prime Attributes: {StudentID, CourseID}
- Non-Prime Attributes: {Grade, StudentName, CourseName, InstructorID}

This relation has partial dependencies (StudentName depends only on StudentID)
and transitive dependencies.

Decomposition to 3NF:
- Student(StudentID, StudentName)
- Course(CourseID, CourseName, InstructorID)
- Enrollment(StudentID, CourseID, Grade)
```

---

## 9. Multiple Choice Questions

### Level 1: Basic Concepts

**Q1. A functional dependency X → Y is trivial if:**
- a) X and Y have common attributes
- b) Y is a subset of X ✓
- c) X is a subset of Y
- d) X and Y are disjoint

**Q2. Armstrong's axioms include:**
- a) Reflexivity, Augmentation, Transitivity ✓
- b) Union, Decomposition, Composition
- c) Associativity, Commutativity, Distributivity
- d) Selection, Projection, Join

**Q3. If A → B and B → C, then by transitivity:**
- a) A → C ✓
- b) B → A
- c) C → A
- d) A → B → C

### Level 2: Intermediate

**Q4. The closure of attribute set X is denoted as:**
- a) X*
- b) X⁺ ✓
- c) X°
- d) X'

**Q5. A candidate key is a:**
- a) Superkey with maximum attributes
- b) Minimal superkey ✓
- c) Primary key with alternate names
- d) Foreign key in another relation

**Q6. The canonical cover of FDs must have:**
- a) Multiple attributes on RHS
- b) No redundant FDs ✓
- c) All possible FDs
- d) Composite keys only

**Q7. In 3NF, for FD X → A, which condition is NOT required?**
- a) X is a superkey
- b) A is prime
- c) X must be a candidate key ✓
- d) None of the above

### Level 3: Advanced

**Q8. Given FDs: A → B, B → C, the closure of {A} is:**
- a) {A}
- b) {A, B}
- c) {A, B, C} ✓
- d) {A, C}

**Q9. A relation is in BCNF if for every FD:**
- a) X → Y, X must be a superkey ✓
- b) X → Y, Y must be prime
- c) X → Y, X can be any attribute
- d) None of the above

**Q10. Which normal form eliminates transitive dependencies?**
- a) 1NF
- b) 2NF
- c) 3NF ✓
- d) BCNF

**Q11. If X → Y and X → Z, then by union rule we can infer:**
- a) X → YZ ✓
- b) X → Y and X → Z separately
- c) XY → Z
- d) YX → Z

**Q12. The process of removing redundant FDs is part of finding:**
- a) Attribute closure
- b) Canonical cover ✓
- c) Superkey
- d) Normal form

**Q13. In the relation R(A, B, C, D) with FDs A → B, B → C, C → D, the candidate key is:**
- a) A
- b) B
- c) C
- d) {A} ✓

**Q14. A relation is in 2NF if it is in 1NF and:**
- a) No non-prime attribute depends on part of a candidate key ✓
- b) No prime attribute depends on part of a candidate key
- c) All attributes are prime
- d) All FDs are trivial

**Q15. Given FD: AB → C and A → D, attribute D is:**
- a) Extraneous in AB
- b) Not extraneous in AB
- c) Part of the key
- d) Cannot be determined ✓

---

## 10. Flashcards

### Flashcard Set 1: Key Definitions

| # | Term | Definition |
|---|------|------------|
| 1 | Functional Dependency | A constraint X → Y where knowing X uniquely determines Y |
| 2 | Trivial FD | FD where RHS ⊆ LHS |
| 3 | Non-Trivial FD | FD where RHS ⊄ LHS |
| 4 | Armstrong's Axioms | Reflexivity, Augmentation, Transitivity |
| 5 | Attribute Closure X⁺ | Set of all attributes functionally determined by X |

### Flashcard Set 2: Keys and Normal Forms

| # | Term | Definition |
|---|------|------------|
| 6 | Superkey | Set of attributes that uniquely identifies tuples |
| 7 | Candidate Key | Minimal superkey |
| 8 | Prime Attribute | Attribute part of any candidate key |
| 9 | 2NF | 1NF + no partial dependencies |
| 10 | 3NF | 1NF + no transitive dependencies (X→Y: X superkey OR Y prime) |
| 11 | BCNF | 1NF + for all X→Y, X must be a superkey |

### Flashcard Set 3: Armstrong's Axioms (Derivations)

| # | Rule | Description | Example |
|---|------|-------------|---------|
| 12 | Reflexivity | If Y ⊆ X, then X → Y | {A,B} → {A} |
| 13 | Augmentation | If X → Y, then XZ → YZ | A→B implies AC→BC |
| 14 | Transitivity | If X→Y and Y→Z, then X→Z | A→B, B→C implies A→C |
| 15 | Union | If X→Y and X→Z, then X→YZ | A→B, A→C implies A→BC |
| 16 | Decomposition | If X→YZ, then X→Y and X→Z | A→BC implies A→B |
| 17 | Pseudotransitivity | If X→Y and WY→Z, then WX→Z | A→B, BC→D implies AC→D |

---

## 11. Key Takeaways

### Core Concepts to Remember

1. **Functional Dependencies** define constraints: knowing X determines Y (X → Y)
2. **Armstrong's Axioms** (Reflexivity, Augmentation, Transitivity) are the foundation for deriving all FDs from a given set
3. **Attribute Closure (X⁺)** is computed iteratively by applying FDs until no new attributes are found
4. **Keys**: A superkey's closure must equal all attributes; a candidate key is a minimal superkey
5. **Canonical Cover** eliminates redundant FDs and extraneous attributes

### Normalization Summary

- **1NF**: Atomic values only
- **2NF**: Eliminate partial dependencies (from 1NF)
- **3NF**: Eliminate transitive dependencies (from 2NF)
- **BCNF**: Stricter version of 3NF

### Exam Tips

- Always compute attribute closure using the iterative algorithm
- Remember: BCNF ⊆ 3NF ⊆ 2NF ⊆ 1NF
- For 3NF, the "or prime attribute" clause distinguishes it from BCNF
- Armstrong's axioms and their derivations are frequently tested
- Practice computing canonical covers — this is a common exam question

### Delhi University Syllabus Alignment

This study material covers all topics specified in the NEP 2024 UGCF syllabus for Database Management Systems, including:
- Functional dependency and Armstrong's axioms
- Attribute closure computation
- Keys, superkeys, and canonical cover
- Normal forms (1NF through BCNF)

---

*Prepared for BSc (Hons) Computer Science, Delhi University*