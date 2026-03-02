# Relational Algebra (Module 2: Database Management Systems)

## Introduction

Relational Algebra is a **procedural query language** that forms the mathematical foundation for relational databases and SQL. It provides a set of operations that take one or more relations (tables) as input and produce a new relation as output. For  engineering students, understanding these operations is crucial as they are the building blocks upon which complex SQL queries are internally executed by the Database Management System (DBMS).

---

## Core Concepts & Operations

Relational Algebra operations can be broadly classified into two categories:

### 1. Fundamental Operations (Primitive Operations)

These are the core operations from which all other operations can be derived.

*   **Select (σ - sigma):** The select operation is used to choose a subset of tuples (rows) from a relation that satisfies a given predicate (condition). It acts as a horizontal filter.
    *   **Notation:** σ`<predicate>`(R)
    *   **Example:** Select all students from the 'CS' branch.
        `σ`<sub>Branch='CS'</sub>`(Student)`

*   **Project (∏ - pi):** The project operation is used to select specific attributes (columns) from a relation. It removes duplicate values in the result, ensuring the output is also a relation (a set). It acts as a vertical filter.
    *   **Notation:** ∏`<attribute list>`(R)
    *   **Example:** Get only the names and roll numbers of all students.
        `∏`<sub>Name, RollNo</sub>`(Student)`

*   **Union (∪):** The union operation combines tuples from two relations of the same schema (same number of attributes and compatible domains). Like mathematical sets, it returns all distinct tuples present in either relation.
    *   **Notation:** R ∪ S
    *   **Prerequisite:** R and S must be **union-compatible**.

*   **Set Difference (-):** The set difference operation finds tuples that are in one relation but not in another. The result contains tuples present in R but absent in S.
    *   **Notation:** R - S
    *   **Prerequisite:** R and S must be **union-compatible**.

*   **Cartesian Product (×):** This operation combines every tuple from relation R with every tuple from relation S. If R has 'm' tuples and S has 'n' tuples, the result will have m*n tuples. It is the fundamental operation for joining data from multiple tables.
    *   **Notation:** R × S

*   **Rename (ρ - rho):** The rename operation is used to assign a new name to a relation or its attributes. This is useful for disambiguating names, especially after operations like Cartesian Product.
    *   **Notation:** ρ`<new_name>(<old_name>)` or ρ`<new_name>(attribute1, attribute2)>(<old_name>)`

### 2. Additional Useful Operations

These operations can be expressed in terms of the fundamental operations but are used frequently for convenience.

*   **Set Intersection (∩):** Returns tuples that are common to both relations R and S.
    *   **Derivation:** R ∩ S = R - (R - S)
    *   **Notation:** R ∩ S

*   **Natural Join (⋈):** One of the most important operations. It performs a Cartesian Product followed by a Select operation that enforces equality on attributes with the same name. It automatically removes duplicate attributes.
    *   **Derivation:** R ⋈ S = σ`<condition>`(R × S)  // where condition matches common attributes
    *   **Notation:** R ⋈ S
    *   **Example:** Join `Student` and `Enrollment` tables on the common `StudentID` attribute to get a list of students and their enrolled courses.

*   **Theta Join (⋈`θ`):** A generalized join where the condition `θ` can be any comparison operator (like =, <, >, ≠), not just equality.
    *   **Derivation:** It is essentially a Cartesian Product followed by a Select: σ`θ`(R × S)

*   **Division (÷):** A useful operation for queries involving "for all" conditions. For example, "find students who have enrolled in all courses offered by the CS department."
    *   **Notation:** R ÷ S

---

## Example Query in Relational Algebra

Let's use a simple database with two relations:
*   **Student**(RollNo, Name, Branch)
*   **Enrollment**(RollNo, CourseID)

**Query:** Find the names of all 'CS' branch students who are enrolled in the course 'DBMS'.

This can be broken down into a sequence of relational algebra operations:

1.  Get all CS students: `CS_Students ← σ`<sub>Branch='CS'</sub>`(Student)`
2.  Get all enrollments for the 'DBMS' course: `DBMS_Enrollments ← σ`<sub>CourseID='DBMS'</sub>`(Enrollment)`
3.  Join these two intermediate results on the common `RollNo` attribute to find which CS students are in the DBMS enrollment list: `Result1 ← CS_Students ⋈ DBMS_Enrollments`
4.  Finally, project only the `Name` attribute: `Final_Result ← ∏`<sub>Name</sub>`(Result1)`

This can be written as a single nested expression:
`∏`<sub>Name</sub>`( (σ`<sub>Branch='CS'</sub>`(Student)) ⋈ (σ`<sub>CourseID='DBMS'</sub>`(Enrollment)) )`

---

## Key Points / Summary

*   **Procedural Language:** Relational Algebra specifies *how* to retrieve data (the step-by-step procedure), unlike SQL which is largely declarative (*what* to retrieve).
*   **Closure Property:** The output of every operation is another relation. This allows operations to be nested to form complex expressions.
*   **Foundation for SQL:** SQL queries are ultimately converted into a tree of relational algebra operations for execution by the query optimizer.
*   **Operators:** The core operators are **Select (σ)**, **Project (∏)**, **Union (∪)**, **Set Difference (-)**, **Cartesian Product (×)**, and **Rename (ρ)**.
*   **Joins are Derived:** Crucial operations like **Natural Join (⋈)** and **Theta Join** are derived from the fundamental Cartesian Product and Select operations.
*   **Purpose:** It provides a formal framework for query optimization and processing within a DBMS.