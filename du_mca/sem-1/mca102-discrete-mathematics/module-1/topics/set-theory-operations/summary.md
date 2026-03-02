# Set Theory Operations — Quick Revision Summary

## Introduction
Set theory forms the foundational language of discrete mathematics, essential for understanding relations, functions, and combinatorial structures. As per the Delhi University MCA syllabus (Revised June 2024), this unit covers fundamental operations on sets that are crucial for problem-solving in computer science applications.

## Key Concepts

### Basic Set Operations
- **Union (∪)**: Combines all elements from two or more sets — A ∪ B = {x : x ∈ A or x ∈ B}
- **Intersection (∩)**: Contains only common elements — A ∩ B = {x : x ∈ A and x ∈ B}
- **Difference (−)**: Elements in one set but not in another — A − B = {x : x ∈ A and x ∉ B}
- **Complement (A')**: All elements in universal set U not in A

### Important Set Laws
- **Commutative**: A ∪ B = B ∪ A, A ∩ B = B ∩ A
- **Associative**: (A ∪ B) ∪ C = A ∪ (B ∪ C)
- **Distributive**: A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C); A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
- **De Morgan's Laws**: (A ∪ B)' = A' ∩ B'; (A ∩ B)' = A' ∪ B'
- **Idempotent**: A ∪ A = A; A ∩ A = A
- **Identity**: A ∪ ∅ = A; A ∩ U = A

### Cartesian Product
- **Definition**: A × B = {(a, b) : a ∈ A and b ∈ B}
- **Properties**: Not commutative; |A × B| = |A| × |B|

### Power Set
- **Definition**: P(A) = {S : S ⊆ A}
- **Property**: If |A| = n, then |P(A)| = 2ⁿ

### Venn Diagrams
- Visual representation of set operations using overlapping circles within a universal set rectangle

## Conclusion
Mastering these set operations and their algebraic properties is essential for MCA students, as they underpin logical reasoning, database theory, and algorithm design. Practice problems involving Venn diagrams and set identities to strengthen conceptual clarity before the examination.