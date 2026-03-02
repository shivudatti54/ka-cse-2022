# Module 2: Unary and Binary Relational Operations in DBMS

## Introduction

The Relational Algebra is a theoretical, procedural query language that forms the foundation for most commercial database query languages like SQL. Its operations take one or more relations (tables) as input and produce a new relation as output. These operations are broadly classified as **Unary** (operate on a single relation) and **Binary** (operate on two relations). Understanding these core operations is crucial for comprehending how complex SQL queries are executed internally by the database system.

## Core Concepts and Operations

### Unary Relational Operations

Unary operations require only a single relation to perform the query.

#### 1. SELECT (σ)

The SELECT operation, denoted by the sigma symbol (σ), is used to choose a subset of tuples (rows) from a relation that satisfy a given predicate (condition). It filters rows horizontally.

*   **Notation:** σ_predicate_(R)
*   **Where:**
    *   `R` is the relation/table name.
    *   `predicate` is a logical condition (e.g., Age > 20, Dept = 'CSE').

**Example:**
Consider a `Students` relation:

| SID | Name  | Dept | Age |
| :-- | :---- | :--- | :-- |
| 101 | Alice | CSE  | 20  |
| 102 | Bob   | ECE  | 22  |
| 103 | Carol | CSE  | 19  |

Query: "Get all students from the 'CSE' department."
**Operation:** σ_Dept='CSE'_(Students)
**Result:**

| SID | Name  | Dept | Age |
| :-- | :---- | :--- | :-- |
| 101 | Alice | CSE  | 20  |
| 103 | Carol | CSE  | 19  |

#### 2. PROJECT (π)

The PROJECT operation, denoted by the pi symbol (π), is used to select specific attributes (columns) from a relation. It returns a vertical subset of the relation, eliminating duplicate tuples in the result.

*   **Notation:** π_attribute_list_(R)
*   **Where:** `attribute_list` is the list of desired column names.

**Example:**
Using the same `Students` table.
Query: "Get the names and departments of all students."
**Operation:** π_Name, Dept_(Students)
**Result:**

| Name  | Dept |
| :---- | :--- |
| Alice | CSE  |
| Bob   | ECE  |
| Carol | CSE  |

### Binary Relational Operations

Binary operations combine data from two different relations.

#### 1. UNION (∪)

The UNION operation combines tuples from two relations. For R ∪ S to be valid, both relations must be **union-compatible** (i.e., have the same number of attributes with corresponding domains). The result includes all distinct tuples that are in R, or in S, or in both.

*   **Notation:** R ∪ S

**Example:**
Let's have two relations, `CSE_Students` and `ECE_Students`, both with the same structure as the `Students` table.
Query: "Get a list of all unique student names from both CSE and ECE departments."
**Operation:** π_Name(CSE_Students) ∪ π_Name(ECE_Students)

#### 2. SET DIFFERENCE (–)

The SET DIFFERENCE operation, denoted by a minus sign (–), finds tuples that are in the first relation but not in the second. The relations must be union-compatible.

*   **Notation:** R – S
*   **Result:** Contains all tuples present in R but not in S.

**Example:**
Query: "Find students who are in CSE but not in ECE." (This example is conceptual, assuming both relations have the same attributes).
**Operation:** CSE_Students – ECE_Students

#### 3. CARTESIAN PRODUCT (×)

The CARTESIAN PRODUCT operation combines each tuple from the first relation with every tuple from the second relation. If relation R has `m` tuples and S has `n` tuples, R × S will have `m * n` tuples. It is the foundation for the JOIN operation.

*   **Notation:** R × S

**Example:**
If R has 2 tuples and S has 3 tuples, R × S will be a new relation with 6 tuples, combining every row from R with every row from S.

#### 4. RENAME (ρ)

The RENAME operation, denoted by the rho symbol (ρ), is used to assign a new name to a relation or its attributes. This is especially useful when dealing with Cartesian Products or self-joins to avoid ambiguity.

*   **Notation:** ρ_new_name_(R) or ρ_new_name(attribute_list)_(R)

---

## Key Points & Summary

| Operation      | Symbol | Type  | Description                                                                                          |
| :------------- | :----- | :---- | :--------------------------------------------------------------------------------------------------- |
| **SELECT**     | σ      | Unary | Filters **rows** based on a condition.                                                                |
| **PROJECT**    | π      | Unary | Selects specific **columns** and removes duplicates.                                                  |
| **UNION**      | ∪      | Binary | Combines all **distinct** tuples from two union-compatible relations.                                |
| **SET DIFFERENCE** | –   | Binary | Finds tuples in the first relation **not present** in the second (must be union-compatible).          |
| **CARTESIAN PRODUCT** | × | Binary | Combines **every tuple** of one relation with every tuple of another. Results in `m * n` tuples.  |
| **RENAME**     | ρ      | Unary | Assigns a new name to a relation or its attributes to resolve ambiguity.                             |

*   **Union-Compatible:** A fundamental requirement for UNION, INTERSECTION, and SET DIFFERENCE operations. It means the two relations must have the same number of attributes, and the domains of the corresponding attributes must be compatible (e.g., same data type).
*   These operations are the **building blocks of SQL**. A complex SQL `SELECT` query with `WHERE`, `JOIN`, and `SELECT` clauses is internally broken down into a sequence of these relational algebra operations for execution.
*   The result of any operation is always another **relation**, adhering to the closure property of relational algebra. This allows operations to be nested to form complex expressions.