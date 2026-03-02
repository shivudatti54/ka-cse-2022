# Examples of Queries in Relational Algebra

## Table of Contents

- [Examples of Queries in Relational Algebra](#examples-of-queries-in-relational-algebra)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Operators](#basic-operators)
  - [Advanced Operators](#advanced-operators)
  - [Aggregate Functions](#aggregate-functions)
- [Examples](#examples)
  - [Example 1: Employee Database](#example-1-employee-database)
  - [Example 2: Student and Course Database](#example-2-student-and-course-database)
  - [Example 3: Complex Query with Set Operations](#example-3-complex-query-with-set-operations)
  - [Example 4: Left Outer Join](#example-4-left-outer-join)
- [Exam Tips](#exam-tips)

## Introduction

Relational Algebra is a theoretical foundation of relational database management systems (RDBMS). It provides a set of mathematical operations that can be applied to relations (tables) to retrieve, manipulate, and transform data. Understanding relational algebra is crucial for database students as it forms the basis for writing SQL queries and helps develop a deeper understanding of how databases process requests internally.

In this topic, we explore various examples of relational algebra queries, ranging from simple selection and projection operations to complex joins and division operations. These examples demonstrate how to combine different operators to extract meaningful information from multiple related tables. The knowledge of relational algebra is essential for database design, query optimization, and understanding the theoretical limitations and capabilities of relational databases.

## Key Concepts

### Basic Operators

**Selection (σ)**: The selection operator filters tuples (rows) from a relation based on a condition. It returns all tuples that satisfy the specified condition. The condition can involve comparison operators (=, ≠, <, ≤, >, ≥) and logical operators (AND, OR, NOT).

**Projection (π)**: The projection operator selects specific columns (attributes) from a relation, eliminating duplicate tuples in the result. It essentially performs vertical partitioning of a table.

**Union (∪)**: The union operation combines tuples from two relations that have the same schema (compatible relations). It eliminates duplicate tuples automatically.

**Set Difference (-)**: The set difference operation returns tuples that exist in the first relation but not in the second relation. Both relations must have the same schema.

**Cartesian Product (×)**: The Cartesian product combines every tuple from the first relation with every tuple from the second relation, creating all possible combinations.

**Rename (ρ)**: The rename operator is used to rename relations or attributes, which is particularly useful when performing self-joins or when we need to distinguish between attributes with the same name.

### Advanced Operators

**Natural Join (⋈)**: The natural join combines two relations based on common attribute names. It performs an equijoin on all attributes with the same name and then removes duplicate common attributes.

**Theta Join (⋈θ)**: The theta join combines tuples from two relations based on a join condition (theta). It is essentially a Cartesian product followed by a selection.

**Equijoin**: A special case of theta join where the condition uses only equality (=) operator.

**Outer Joins**: Extended joins that preserve tuples that do not have matching values. Includes left outer join, right outer join, and full outer join.

**Intersection (∩)**: Returns tuples that exist in both relations. Can be expressed using set difference: R ∩ S = R - (R - S).

**Division (÷)**: The division operation returns tuples from the first relation that match all tuples in the second relation. It is used for queries involving "for all" or "such that" conditions.

### Aggregate Functions

Relational algebra can be extended with aggregate functions like SUM, AVG, COUNT, MIN, and MAX. These operations group tuples and compute aggregate values.

## Examples

### Example 1: Employee Database

Consider the following relations for a company database:

**EMPLOYEE** (Emp_ID, Emp_Name, Dept_ID, Salary)

- E1, Alice, D1, 50000
- E2, Bob, D1, 60000
- E3, Charlie, D2, 55000
- E4, David, D2, 45000
- E5, Eve, D3, 70000

**DEPARTMENT** (Dept_ID, Dept_Name, Manager_ID)

- D1, IT, E1
- D2, HR, E3
- D3, Finance, E5

**Query 1**: Find names of all employees earning more than 50000

**Solution**:
π_Emp_Name(σ_Salary > 50000(EMPLOYEE))

Step-by-step:

1. σ_Salary > 50000(EMPLOYEE) → Select employees with salary > 50000

- E1, Alice, D1, 50000 (No, not > 50000)
- E2, Bob, D1, 60000 (Yes)
- E3, Charlie, D2, 55000 (Yes)
- E4, David, D2, 45000 (No)
- E5, Eve, D3, 70000 (Yes)
  Result: {E2, E3, E5}

2. π_Emp_Name({E2, E3, E5}) → Project only Emp_Name
   Result: {Bob, Charlie, Eve}

**Query 2**: Find department names for employees in IT department

**Solution**:
π_Dept_Name(EMPLOYEE ⋈ DEPARTMENT)

Step-by-step:

1. Natural join EMPLOYEE ⋈ DEPARTMENT on Dept_ID

- E1, Alice, D1, 50000 ⋈ D1, IT, E1 → E1, Alice, D1, 50000, IT, E1
- E2, Bob, D1, 60000 ⋈ D1, IT, E1 → E2, Bob, D1, 60000, IT, E1
- E3, Charlie, D2, 55000 ⋈ D2, HR, E3 → E3, Charlie, D2, 55000, HR, E3
- E4, David, D2, 45000 ⋈ D2, HR, E3 → E4, David, D2, 45000, HR, E3
- E5, Eve, D3, 70000 ⋈ D3, Finance, E5 → E5, Eve, D3, 70000, Finance, E5

2. π_Dept_Name(Result)
   Result: {IT, IT, HR, HR, Finance} → After removing duplicates: {IT, HR, Finance}

### Example 2: Student and Course Database

Consider:
**STUDENT** (Stud_ID, Name, Major, GPA)

- S1, John, CS, 3.8
- S2, Mary, CS, 3.5
- S3, Tom, Math, 3.2
- S4, Lucy, Physics, 3.9

**ENROLLMENT** (Stud_ID, Course_ID, Grade)

- S1, C1, A
- S1, C2, B
- S2, C1, A
- S3, C1, B
- S3, C2, A

**COURSE** (Course_ID, Course_Name, Credits)

- C1, Database, 4
- C2, Algorithms, 3

**Query 3**: Find names of students enrolled in Database course

**Solution**:
π_Name(σ_Course_Name = 'Database'(STUDENT ⋈ ENROLLMENT ⋈ COURSE))

Step-by-step:

1. STUDENT ⋈ ENROLLMENT on Stud_ID
2. Result ⋈ COURSE on Course_ID
3. σ_Course_Name = 'Database'(Result) → Select Database courses
4. π_Name(Result) → Project student names

**Query 4**: Find students who have taken all courses

**Solution**:
This requires division operation:
π_Stud_ID, Course_ID(ENROLLMENT) ÷ π_Course_ID(COURSE)

The result gives Stud_ID of students enrolled in all courses.

### Example 3: Complex Query with Set Operations

**Query 5**: Find employees who work in IT or have salary > 55000

**Solution**:
(π_Emp_ID, Emp_Name, Dept_ID, Salary(σ_Dept_ID = 'D1'(EMPLOYEE))) ∪ (π_Emp_ID, Emp_Name, Dept_ID, Salary(σ_Salary > 55000(EMPLOYEE)))

Step-by-step:

1. σ_Dept_ID = 'D1'(EMPLOYEE) → E1, Alice and E2, Bob
2. σ_Salary > 55000(EMPLOYEE) → E3, Charlie and E5, Eve
3. Union removes duplicates: {E1, E2, E3, E5}

### Example 4: Left Outer Join

**Query 6**: List all departments with their employees (including departments with no employees)

**Solution**:
EMPLOYEE ⟕ DEPARTMENT

This returns all departments even if no employee is assigned.

## Exam Tips

1. **Understand operator precedence**: Selection (σ) and projection (π) have higher precedence than join (⋈), union (∪), and set difference (-).

2. **Practice tree notation**: Learn to draw expression trees for complex queries as this helps in understanding query structure and evaluation order.

3. **Remember set operations require schema compatibility**: Union, intersection, and difference operations only work on relations with the same number of attributes and compatible domains.

4. **Natural join removes duplicate common attributes**: After natural join, the common attributes appear only once in the result.

5. **Division is the inverse of Cartesian product**: If R ÷ S = T, then T × S is a subset of R.

6. **Theta join = Cartesian product + Selection**: R ⋈θ S = σθ(R × S)

7. **Outer joins preserve non-matching tuples**: Left outer join keeps all tuples from the left relation; right outer join keeps all from the right; full outer join keeps all from both.
