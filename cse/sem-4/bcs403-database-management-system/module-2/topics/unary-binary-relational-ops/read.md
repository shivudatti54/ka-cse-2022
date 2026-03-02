# Unary and Binary Relational Operations

## Table of Contents

- [Unary and Binary Relational Operations](#unary-and-binary-relational-operations)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Fundamental Relational Operations](#1-fundamental-relational-operations)
  - [2. Unary Relational Operations](#2-unary-relational-operations)
  - [3. Binary Relational Operations](#3-binary-relational-operations)
  - [4. Set Operations vs. Relational Operations](#4-set-operations-vs-relational-operations)
- [Examples](#examples)
  - [Example 1: Combined Operations](#example-1-combined-operations)
  - [Example 2: Set Operations](#example-2-set-operations)
  - [Example 3: Cartesian Product with Selection](#example-3-cartesian-product-with-selection)
- [Exam Tips](#exam-tips)

## Introduction

Relational Algebra forms the theoretical foundation of database management systems, providing a set of mathematical operations that work on relations (tables) to produce new relations. Developed by E.F. Codd in 1970, relational algebra provides a declarative way to query and manipulate data in relational databases. Understanding these operations is essential for any database professional, as they form the basis for SQL query optimization and database theory.

The operations in relational algebra are broadly categorized into two types: **Unary Operations** and **Binary Operations**. Unary operations work on a single relation, while binary operations combine two relations to produce a new relation. These operations are fundamental to data manipulation and form the backbone of SQL, the standard language for relational database management systems.

In this topic, we will explore each operation in detail with comprehensive examples, understand their properties, and learn how to apply them effectively in database queries. Mastery of these operations is crucial for database design, query optimization, and understanding how database systems process user requests.

## Key Concepts

### 1. Fundamental Relational Operations

The relational algebra operations can be divided into basic operations (Select, Project, Union, Set Difference, Cartesian Product, Rename) and additional operations (Intersection, Division, Join, etc.). For this module, we focus specifically on unary and binary operations.

### 2. Unary Relational Operations

#### 2.1 SELECT Operation (σ)

The SELECT operation (denoted by σ) extracts rows from a relation that satisfy a specified condition. It acts as a horizontal filter, reducing the number of tuples based on a predicate.

**Notation:** σ<sub>condition</sub>(R)

**Properties:**

- The result of SELECT has the same schema as the original relation
- SELECT is commutative: σ<sub>c1</sub>(σ<sub>c2</sub>(R)) = σ<sub>c2</sub>(σ<sub>c1</sub>(R))
- SELECT can be combined with logical operators: AND (∧), OR (∨), NOT (¬)
- The degree (number of attributes) remains unchanged

**Example:** Consider a relation EMPLOYEE(EmpID, Name, Dept, Salary):

```
EMPLOYEE
EmpID | Name | Dept | Salary
------|---------|-------|--------
E01 | Alice | IT | 50000
E02 | Bob | HR | 45000
E03 | Charlie | IT | 55000
E04 | Diana | Sales | 40000
```

σ<sub>Dept='IT'</sub>(EMPLOYEE) returns:

```
EmpID | Name | Dept | Salary
------|---------|-------|--------
E01 | Alice | IT | 50000
E03 | Charlie | IT | 55000
```

σ<sub>Salary>45000 ∧ Dept='IT'</sub>(EMPLOYEE) returns:

```
EmpID | Name | Dept | Salary
------|---------|-------|--------
E03 | Charlie | IT | 55000
```

#### 2.2 PROJECT Operation (π)

The PROJECT operation (denoted by π) extracts specified columns (attributes) from a relation. It acts as a vertical filter, selecting specific attributes while discarding others.

**Notation:** π<sub>attribute1, attribute2, ...</sub>(R)

**Properties:**

- The result contains only the specified attributes
- Duplicate tuples are eliminated (set semantics)
- The number of tuples may be reduced due to duplicate elimination
- PROJECT is not commutative: π<sub>A</sub>(π<sub>AB</sub>(R)) ≠ π<sub>AB</sub>(R)

**Example:** Using the EMPLOYEE relation:
π<sub>Name, Dept</sub>(EMPLOYEE) returns:

```
Name | Dept
--------|-------
Alice | IT
Bob | HR
Charlie | IT
Diana | Sales
```

π<sub>Dept</sub>(EMPLOYEE) returns (duplicates removed):

```
Dept
-----
IT
HR
Sales
```

#### 2.3 RENAME Operation (ρ)

The RENAME operation (denoted by ρ) is used to rename either the relation or its attributes. It is essential when performing operations that produce relations needing further manipulation.

**Notation:**

- ρ<sub>S</sub>(R) - Renames relation R to S
- ρ<sub>S(A1,A2,...,An)</sub>(R) - Renames relation R to S with new attribute names A1, A2, ..., An

**Properties:**

- Does not change the content of the relation
- Essential for self-joins and nested queries
- Helps avoid ambiguity in complex queries

**Example:** ρ<sub>EMP</sub>(EMPLOYEE) renames the relation to EMP.
ρ<sub>EMP(ID, Name, Department, Pay)</sub>(EMPLOYEE) renames both the relation and attributes.

### 3. Binary Relational Operations

Binary operations combine two relations. They are based on set theory and require both relations to be **union-compatible** (same number of attributes with compatible domains).

#### 3.1 UNION Operation (∪)

The UNION operation combines all tuples from two relations, eliminating duplicates.

**Notation:** R ∪ S

**Requirements (Union Compatibility):**

- Both relations must have the same number of attributes
- Corresponding attributes must have compatible domains

**Properties:**

- Union is commutative: R ∪ S = S ∪ R
- Union is associative: (R ∪ S) ∪ T = R ∪ (S ∪ T)
- Result contains no duplicate tuples

**Example:** Consider two relations:

```
STUDENT_CS STUDENT_IT
Name | Grade Name | Grade
--------|------- --------|-------
Alice | A Bob | A
Bob | A Charlie | B
Charlie | B David | A
```

STUDENT_CS ∪ STUDENT_IT:

```
Name | Grade
--------|-------
Alice | A
Bob | A
Charlie | B
David | A
```

#### 3.2 SET DIFFERENCE Operation (−)

The SET DIFFERENCE operation returns tuples that exist in the first relation but not in the second.

**Notation:** R − S

**Properties:**

- Set difference is not commutative: R − S ≠ S − R
- Requires union compatibility
- Order of operands matters

**Example:** Using the STUDENT relations above:
STUDENT_CS − STUDENT_IT:

```
Name | Grade
--------|-------
Alice | A
```

(Bob and Charlie are in STUDENT_IT)

#### 3.3 INTERSECTION Operation (∩)

The INTERSECTION operation returns tuples that exist in both relations.

**Notation:** R ∩ S

**Properties:**

- Intersection is commutative: R ∩ S = S ∩ R
- Can be expressed as: R ∩ S = R − (R − S)
- Requires union compatibility

**Example:** STUDENT_CS ∩ STUDENT_IT:

```
Name | Grade
--------|-------
Bob | A
Charlie | B
```

#### 3.4 CARTESIAN PRODUCT Operation (×)

The CARTESIAN PRODUCT (also called CROSS PRODUCT) combines every tuple from the first relation with every tuple from the second relation.

**Notation:** R × S

**Properties:**

- Result degree = degree(R) + degree(S)
- Result cardinality = |R| × |S|
- Not commutative (though R × S has same structure as S × R)
- Often followed by SELECT to form meaningful joins

**Example:**

```
R(A,B) S(C,D)
A | B C | D
-----|---- -----|----
a1 | b1 c1 | d1
a2 | b2 c2 | d2

R × S:
A | B | C | D
-----|-----|-----|-----
a1 | b1 | c1 | d1
a1 | b1 | c2 | d2
a2 | b2 | c1 | d1
a2 | b2 | c2 | d2
```

### 4. Set Operations vs. Relational Operations

It's important to distinguish between:

| Operation Type                | Operations                         | Description                        |
| ----------------------------- | ---------------------------------- | ---------------------------------- |
| Traditional Set Operations    | Union, Intersection, Difference    | Require union compatibility        |
| Special Relational Operations | Select, Project, Cartesian Product | Do not require union compatibility |
| Additional Operations         | Join, Division                     | Built from fundamental operations  |

## Examples

### Example 1: Combined Operations

Given relation EMPLOYEE(EmpID, Name, Dept, Salary, Experience):

```
EmpID | Name | Dept | Salary | Experience
------|---------|-------|--------|------------
E01 | Alice | IT | 50000 | 3
E02 | Bob | HR | 45000 | 5
E03 | Charlie | IT | 55000 | 7
E04 | Diana | Sales | 40000 | 2
E05 | Edward | HR | 48000 | 4
```

**Query:** Find names of employees in IT department with salary > 50000

**Solution:**
π<sub>Name</sub>(σ<sub>Dept='IT' ∧ Salary>50000</sub>(EMPLOYEE))

**Step-by-step:**

1. σ<sub>Dept='IT' ∧ Salary>50000</sub>(EMPLOYEE):

```
EmpID | Name | Dept | Salary | Experience
------|---------|-------|--------|------------
E03 | Charlie | IT | 55000 | 7
```

2. π<sub>Name</sub>(Result):

```
Name
--------
Charlie
```

### Example 2: Set Operations

Given relations:

```
MALE_WORKERS(WID, Name, Dept) FEMALE_WORKERS(WID, Name, Dept)
WID | Name | Dept WID | Name | Dept
----|---------|----- ----|---------|-----
W1 | Alice | IT W4 | Diana | HR
W2 | Bob | IT W5 | Eve | Sales
W3 | Charlie | HR
```

**Query 1:** Find all workers (both male and female)
MALE_WORKERS ∪ FEMALE_WORKERS

Result:

```
WID | Name | Dept
----|---------|-----
W1 | Alice | IT
W2 | Bob | IT
W3 | Charlie | HR
W4 | Diana | HR
W5 | Eve | Sales
```

**Query 2:** Find male workers who are not female workers
MALE_WORKERS − FEMALE_WORKERS

Result:

```
WID | Name | Dept
----|---------|-----
W1 | Alice | IT
W2 | Bob | IT
W3 | Charlie | HR
```

### Example 3: Cartesian Product with Selection

Given relations:

```
DEPT(DeptID, DeptName) EMPLOYEE(EmpID, Name, DeptID)
DeptID | DeptName EmpID | Name | DeptID
-------|-------- ------|---------|-------
D1 | IT E1 | Alice | D1
D2 | HR E2 | Bob | D2
D3 | Sales E3 | Charlie | D1
```

**Query:** Find employees with their department names

**Solution:** π<sub>EmpID, Name, DeptName</sub>(σ<sub>DEPT.DeptID = EMPLOYEE.DeptID</sub>(DEPT × EMPLOYEE))

**Step-by-step:**

1. DEPT × EMPLOYEE:

```
DEPT.DeptID | DeptName | EMPLOYEE.EmpID | Name | EMPLOYEE.DeptID
------------|----------|----------------|---------|-----------------
D1 | IT | E1 | Alice | D1
D1 | IT | E2 | Bob | D2
D1 | IT | E3 | Charlie | D1
D2 | HR | E1 | Alice | D1
D2 | HR | E2 | Bob | D2
D2 | HR | E3 | Charlie | D1
D3 | Sales | E1 | Alice | D1
D3 | Sales | E2 | Bob | D2
D3 | Sales | E3 | Charlie | D1
```

2. σ<sub>DEPT.DeptID = EMPLOYEE.DeptID</sub>(Result) - Natural join condition:

```
DEPT.DeptID | DeptName | EMPLOYEE.EmpID | Name | EMPLOYEE.DeptID
------------|----------|----------------|---------|-----------------
D1 | IT | E1 | Alice | D1
D1 | IT | E3 | Charlie | D1
D2 | HR | E2 | Bob | D2
```

3. π<sub>EmpID, Name, DeptName</sub>(Result):

```
EmpID | Name | DeptName
------|---------|----------
E1 | Alice | IT
E2 | Bob | HR
E3 | Charlie | IT
```

## Exam Tips

1. **Understanding Notation:** Know the symbols: σ (SELECT), π (PROJECT), ρ (RENAME), ∪ (UNION), − (DIFFERENCE), ∩ (INTERSECTION), × (CARTESIAN PRODUCT)

2. **Union Compatibility:** Remember that UNION, INTERSECTION, and SET DIFFERENCE require both relations to have the same number of attributes with compatible domains.

3. **SELECT vs PROJECT:** SELECT filters rows (horizontal), PROJECT filters columns (vertical). Don't confuse them in exams.

4. **Duplicate Elimination:** Remember that both PROJECT and UNION eliminate duplicate tuples. This is different from SQL which uses DISTINCT.

5. **Commutative Properties:** UNION and INTERSECTION are commutative; SET DIFFERENCE is not. This is important for query simplification.

6. **Degree and Cardinality:** For CARTESIAN PRODUCT, remember that degree = r1 + r2 and cardinality = n1 × n2.

7. **Operator Precedence:** In relational algebra, SELECT (σ) has highest priority, followed by PROJECT (π), then CARTESIAN PRODUCT (×), then UNION (∪) and DIFFERENCE (−).

8. **Practical Approach:** When solving query problems, break down complex queries into smaller steps using intermediate relations.

9. **Rename Operation Usage:** Use RENAME when you need to refer to the same relation multiple times or when attribute names conflict.

10. **Real-world Applications:** Connect these operations to their SQL equivalents: SELECT → σ, PROJECT → π attribute list, UNION → UNION, etc.
