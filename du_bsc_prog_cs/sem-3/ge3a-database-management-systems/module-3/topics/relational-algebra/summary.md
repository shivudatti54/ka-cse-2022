# Relational Algebra

## Introduction
Relational Algebra is a **procedural query language** for relational databases that provides a set of operations to manipulate and retrieve data. It forms the theoretical foundation for query processing and optimization in DBMS, directly influencing SQL and other query languages. For the Delhi University Ge3A Database Management Systems syllabus (NEP 2024), this topic is crucial for understanding how queries are executed and evaluated.

## Key Concepts
- **Definition**: A formal system that operates on relations (tables) using mathematical set operations to produce new relations.
- **Fundamental Operations** (6 basic operations):
  * **Selection (σ)**: Filters tuples (rows) based on a condition (e.g., σ_{dept='CS'}(Student)).
  * **Projection (π)**: Selects specific attributes (columns), eliminating duplicates (e.g., π_{name, age}(Student)).
  * **Union (∪)**: Combines results of two compatible relations (e.g., R ∪ S).
  * **Set Difference (−)**: Returns tuples in one relation but not in another (e.g., R − S).
  * **Cartesian Product (×)**: Generates all possible combinations of tuples from two relations (e.g., R × S).
  * **Rename (ρ)**: Renames relations or attributes to avoid ambiguity (e.g., ρ_{newName}(R)).
- **Additional Operations** (derived from fundamental):
  * **Intersection (∩)**: Common tuples (R ∩ S = R − (R − S)).
  * **Natural Join (⋈)**: Equi-join on common attributes, automatically eliminating duplicate columns.
  * **Theta Join (⋈_θ)**: Join with a specific condition (e.g., R ⋈_{R.id=S.id} S).
  * **Division (÷)**: Used for queries like "find all students who have enrolled in all courses" (e.g., Student ÷ Course).
- **Extended Operations**:
  * **Outer Joins**: Left (⟕), Right (⟖), Full (⟗) to preserve tuples with NULL values.
  * **Outer Union**: Combines partially compatible relations.
- **Query Examples**: Complex queries are built by combining operations (e.g., π_{name}(σ_{dept='CS'}(Student ⋈ Enroll))).
- **Query Optimization**: Relational algebra expressions are used by DBMS to optimize query execution through techniques like query parsing, planning, and cost estimation.

## Conclusion
Relational Algebra is essential for understanding database query processing. It provides a procedural approach to data manipulation, directly mapping to SQL and aiding in query optimization. For Delhi University exams, focus on writing queries using fundamental operations and understanding their properties (e.g., commutativity, associativity). Practice converting English queries to relational algebra expressions and vice versa for exam success.