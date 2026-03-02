# Vector Space And Subspaces

## Introduction

Vector spaces form a fundamental concept in linear algebra, essential for computer science applications including computer graphics, machine learning, and data structures. This topic covers the algebraic structure of vectors and their properties under addition and scalar multiplication.

---

## Key Concepts

### Vector Space Definition
- A **vector space** V over a field F is a set equipped with two operations:
  - **Vector addition**: V × V → V
  - **Scalar multiplication**: F × V → V
- Must satisfy ten axioms: closure, commutativity, associativity, identity, inverses (addition); distributivity (two types), compatibility, identity (scalar multiplication)

### Important Properties
- **Zero vector** (0) exists such that v + 0 = v
- Every vector v has an additive inverse (-v) where v + (-v) = 0
- Scalar multiplication distributes over vector addition and field addition

### Examples of Vector Spaces
- **Rⁿ**: n-tuples of real numbers (most common in computing)
- **Rᵐˣⁿ**: Set of all m×n matrices
- **Pₙ**: polynomials of degree ≤ n
- **C[a,b]**: continuous functions on interval [a,b]

### Subspaces
- A **subspace** W of vector space V is a subset that is itself a vector space under the same operations
- **Trivial subspaces**: {0} and V itself
- **Proper subspace**: W ≠ V

### Subspace Criteria (Theorems)
A non-empty subset W of V is a subspace if and only if:
1. **Closed under addition**: u, v ∈ W ⇒ u + v ∈ W
2. **Closed under scalar multiplication**: c ∈ F, v ∈ W ⇒ cv ∈ W

### Span and Linear Combinations
- **Linear combination**: cv₁ + cv₂ + ... + cvₙ where cᵢ are scalars
- **Span(W)**: Set of all linear combinations of vectors in W
- W spans V if span(W) = V

### Linear Independence
- **Linearly independent**: No vector can be expressed as a combination of others
- **Linearly dependent**: At least one vector is a linear combination of others

### Basis and Dimension
- **Basis**: Linearly independent set that spans the space
- **Dimension**: Number of vectors in any basis (consistent for all bases)
- Standard basis for Rⁿ: e₁, e₂, ..., eₙ

---

## Conclusion

Understanding vector spaces and subspaces is crucial for computing applications. The concepts of span, linear independence, and basis form the foundation for solving systems of linear equations, transformations, and multidimensional data representations—all essential for algorithms and computational thinking.

**Key Reference**: Delhi University BSc (Hons) CS - Mathematics for Computing (UGCF NEP 2024)