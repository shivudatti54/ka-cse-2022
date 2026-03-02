# Linear Independence, Basis & Dimension

## Introduction

These are fundamental concepts in linear algebra essential for computer science applications like machine learning, computer graphics, and data structures. As per the Delhi University NEP 2024 UGCF syllabus for BSc (Hons) Computer Science, understanding these concepts is crucial for solving systems of linear equations and vector space problems.

## Key Concepts

### Linear Independence

- A set of vectors {v₁, v₂, ..., vₙ} is **linearly independent** if no vector can be expressed as a linear combination of the others
- Formally: c₁v₁ + c₂v₂ + ... + cₙvₙ = 0 implies all scalars c₁, c₂, ..., cₙ = 0
- If at least one scalar is non-zero, the set is **linearly dependent**
- Geometrically in ℝ²: two vectors are independent if they are not parallel
- In ℝ³: three vectors are independent if they do not lie in the same plane
- **Key test**: Form a matrix with vectors as columns/rows and find its rank or determinant

### Span

- The **span** of a set of vectors {v₁, v₂, ..., vₙ} is the set of all linear combinations: c₁v₁ + c₂v₂ + ... + cₙvₙ where cᵢ are scalars
- Span represents all reachable points in the vector space using given vectors
- If span(S) = ℝⁿ, then set S spans ℝⁿ (covers entire n-dimensional space)
- **Theorem**: Any spanning set can be reduced to a basis by removing dependent vectors

### Basis

- A **basis** for a vector space V is a set of vectors that is:
  - **Linearly independent** (no redundancy)
  - **Spans V** (covers entire space)
- Every basis of a vector space has the same number of elements
- **Standard bases**:
  - ℝ²: {(1,0), (0,1)}
  - ℝ³: {(1,0,0), (0,1,0), (0,0,1)}
- Basis provides a unique representation for every vector in V as a linear combination of basis vectors
- Any set of n linearly independent vectors in ℝⁿ forms a basis for ℝⁿ

### Dimension

- **Dimension** of a vector space V is the number of vectors in any basis of V
- **Fundamental Theorem**: All bases of a vector space have the same number of elements
- Dimension(ℝⁿ) = n; Dimension of {0} = 0
- **Dimension formula** for subspaces: If W is a subspace of V, then dim(W) ≤ dim(V)
- **Extended basis theorem**: Any linearly independent set in an n-dimensional space can be extended to a basis
- **Relationship**: If basis has k vectors, dimension = k

## Applications in Computing

- Solving systems of linear equations (used in graphics transformations)
- Understanding data structures and algorithms (vector spaces in machine learning)
- Rank of matrices determines solution uniqueness in linear systems

## Conclusion

Linear independence, span, basis, and dimension are interconnected concepts forming the foundation of vector space theory. A basis provides a "coordinate system" for a vector space, while dimension tells us the minimum number of vectors needed to describe the entire space. These concepts are essential for advanced topics in computer science and must be mastered for exam success.