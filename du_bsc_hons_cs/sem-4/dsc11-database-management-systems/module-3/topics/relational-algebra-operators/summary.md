# Relational Algebra Operators

## Database Management Systems — BSc (Hons) Computer Science
### Delhi University (NEP 2024 UGCF)

---

## Introduction

Relational Algebra is a procedural query language that forms the theoretical foundation of relational DBMS. It provides a set of mathematical operations to manipulate relations (tables) and produce new relations as output. Understanding these operators is essential for query processing, optimization, and database design — core components of the Delhi University BSc (Hons) Computer Science syllabus.

---

## Fundamental Operators

- **Select (σ)**: Filters rows/tuples based on a condition
  - Notation: σ_condition(Relation)
  - Example: σSalary>50000(Employee)

- **Project (π)**: Selects specific columns/attributes
  - Notation: πattribute_list(Relation)
  - Example: πName, Dept(Employee)

- **Union (∪)**: Combines results of two compatible relations, removes duplicates
  - Example: R ∪ S

- **Set Difference (−)**: Returns tuples in first relation but not in second
  - Example: R − S

- **Cartesian Product (×)**: Produces all possible combinations of tuples from two relations
  - Notation: R × S

- **Rename (ρ)**: Renames relations or attributes for clarity
  - Notation: ρnew_name(Relation)

---

## Additional Operators

- **Intersection (∩)**: Returns common tuples from two relations
  - Derived: R ∩ S = R − (R − S)

- **Natural Join (⋈)**: Equi-join on common attributes; automatically eliminates duplicate columns

- **Theta Join (⋈θ)**: Join based on a specified condition (θ)
  - Notation: R ⋈θ S = σθ(R × S)

- **Division (÷)**: Returns attributes from first relation that match all tuples in second relation
  - Used for "forall" type queries

---

## Extended Operators

- **Outer Joins**: Preserve unmatched tuples
  - **Left Outer Join (⟕)**: Keep all tuples from left relation
  - **Right Outer Join (⟖)**: Keep all tuples from right relation
  - **Full Outer Join (⟗)**: Keep all tuples from both relations

- **Assignment (←)**: Stores intermediate results in temporary relations

---

## Conclusion

Relational Algebra operators provide a formal framework for querying relational databases. The fundamental operators (select, project, union, difference, cartesian product, rename) form the basis, while additional and extended operators enable complex queries. These concepts are crucial for understanding query optimization and form a significant portion of the Database Management Systems paper in Delhi University's NEP 2024 UGCF curriculum.