# Linear Dependence and Independence

## Introduction

Linear dependence and independence are fundamental concepts in linear algebra that form the backbone of vector space theory and are essential for understanding more advanced topics such as basis, dimension, linear transformations, and eigenvalues. These concepts help us determine whether a set of vectors contains redundant information or whether each vector contributes unique directional information to the space they span.

In practical applications, linear dependence arises in numerous real-world scenarios. For instance, in data science, when multiple features in a dataset are highly correlated, they become linearly dependent, leading to multicollinearity problems in regression analysis. In engineering, analyzing forces in a structure requires understanding whether certain force vectors are linearly dependent, which determines whether the structure is stable or has redundant components. In computer graphics, determining whether a set of transformation vectors are linearly independent helps optimize computations and avoid redundant operations.

This topic is crucial for the university examination as it typically carries significant weightage. Understanding these concepts enables students to solve problems related to determining whether a given set of vectors forms a basis, checking the linear independence of rows or columns of matrices (which is essential for understanding rank), and solving systems of linear equations through various methods.

## Key Concepts

### 1. Linear Combination

A **linear combination** of vectors v₁, v₂, ..., vₙ is an expression of the form:

c₁v₁ + c₂v₂ + ... + cₙvₙ

where c₁, c₂, ..., cₙ are scalars (real numbers in most contexts). The scalars c₁, c₂, ..., cₙ are called the **coefficients** of the linear combination.

For example, in ℝ³, if v₁ = (1, 0, 0), v₂ = (0, 1, 0), and v₃ = (0, 0, 1), then the vector (3, 4, 5) can be written as the linear combination: 3v₁ + 4v₂ + 5v₃.

### 2. Linear Dependence

A set of vectors {v₁, v₂, ..., vₙ} in a vector space is said to be **linearly dependent** if there exist scalars c₁, c₂, ..., cₙ, not all zero, such that:

c₁v₁ + c₂v₂ + ... + cₙvₙ = 0

This means at least one vector in the set can be expressed as a linear combination of the other vectors. The scalars c₁, c₂, ..., cₙ are called the **dependence coefficients**.

**Geometric Interpretation**: In ℝ² and ℝ³, vectors are linearly dependent if they lie on the same line (in ℝ²) or the same plane (in ℝ³). Two vectors are linearly dependent if and only if one is a scalar multiple of the other.

### 3. Linear Independence

A set of vectors {v₁, v₂, ..., vₙ} is said to be **linearly independent** if the only scalars that satisfy c₁v₁ + c₂v₂ + ... + cₙvₙ = 0 are c₁ = c₂ = ... = cₙ = 0.

In other words, no vector in the set can be expressed as a linear combination of the other vectors. This means each vector contributes new directional information that cannot be obtained from the others.

**Important Property**: A set containing the zero vector is always linearly dependent because we can write 1·0 = 0 with a non-zero coefficient.

### 4. Theorems and Properties

**Theorem 1**: A set of two vectors {v₁, v₂} is linearly dependent if and only if one is a scalar multiple of the other.

**Theorem 2**: If a set contains more vectors than the dimension of the vector space, it must be linearly dependent. For example, any set of 4 or more vectors in ℝ³ is linearly dependent.

**Theorem 3**: A set of vectors is linearly independent if and only if the matrix formed by taking these vectors as columns has a non-zero determinant (for square matrices) or full rank.

**Theorem 4**: Any set of vectors containing the zero vector is linearly dependent.

**Theorem 5**: If a set {v₁, v₂, ..., vₙ} is linearly independent, then each vector can be expressed uniquely as a linear combination of any basis of the space.

### 5. Spanning and Relationship

The concepts of linear dependence/independence are closely related to spanning:

- A set of vectors **spans** a subspace if every vector in that subspace can be expressed as a linear combination of the set.
- A **basis** is a set of vectors that is both linearly independent and spans the entire space.
- The number of vectors in any basis of a finite-dimensional vector space is constant (this is the dimension of the space).

### 6. Testing Linear Independence

To test whether a set of vectors is linearly independent, we typically:

1. **Form a matrix** with the given vectors as rows or columns
2. **Reduce to echelon form** using row operations
3. **Check for pivot positions**: If every column (or row) has a pivot position, the vectors are linearly independent; otherwise, they are dependent.

## Examples

### Example 1: Basic Linear Independence Test in ℝ³

Determine whether the vectors v₁ = (1, 2, 3), v₂ = (4, 5, 6), and v₃ = (7, 8, 9) are linearly independent or dependent.

**Solution**:

We need to check if the equation c₁v₁ + c₂v₂ + c₃v₃ = 0 has only the trivial solution.

Let us form the matrix with these vectors as columns:

A = [1 4 7; 2 5 8; 3 6 9]

We need to find the determinant or reduce to echelon form:

Using row operations:
R₂ → R₂ - 2R₁: [1 4 7; 0 -3 -6; 3 6 9]
R₃ → R₃ - 3R₁: [1 4 7; 0 -3 -6; 0 -6 -12]

R₃ → R₃ - 2R₂: [1 4 7; 0 -3 -6; 0 0 0]

The matrix has rank 2 (only 2 non-zero rows), which is less than the number of vectors (3). Therefore, the vectors are **linearly dependent**.

We can verify: Notice that v₃ - 2v₂ = (7, 8, 9) - 2(4, 5, 6) = (7-8, 8-10, 9-12) = (-1, -2, -3) = -v₁
So: v₁ + 2v₂ - v₃ = 0, confirming dependence.

### Example 2: Finding Dependence Relationship

Given vectors v₁ = (1, -1, 2) and v₂ = (2, 1, 3) in ℝ³, determine if they are linearly independent. Then check if v₃ = (4, 1, 8) can be expressed as a linear combination.

**Solution**:

For two vectors in ℝ³, they are linearly dependent only if one is a scalar multiple of the other. Since (1, -1, 2) is not a scalar multiple of (2, 1, 3), these two vectors are **linearly independent**.

Now, to check if v₃ can be written as a linear combination:
We need scalars a and b such that a(1, -1, 2) + b(2, 1, 3) = (4, 1, 8)

This gives us:
a + 2b = 4
-a + b = 1
2a + 3b = 8

Solving: From the second equation, b = 1 + a
Substituting in first: a + 2(1 + a) = 4 → a + 2 + 2a = 4 → 3a = 2 → a = 2/3
Then b = 1 + 2/3 = 5/3

Check third equation: 2(2/3) + 3(5/3) = 4/3 + 15/3 = 19/3 ≠ 8

Since no solution exists, v₃ cannot be expressed as a linear combination of v₁ and v₂. Therefore, {v₁, v₂, v₃} is linearly independent.

### Example 3: Using Matrix Rank

Determine whether the following vectors in ℝ⁴ are linearly independent:
v₁ = (1, 2, 0, 1), v₂ = (2, 1, 1, 0), v₃ = (1, 1, 1, 1), v₄ = (0, 1, 2, 3)

**Solution**:

Form matrix A with these as rows:

A = [1 2 0 1; 2 1 1 0; 1 1 1 1; 0 1 2 3]

Reduce to row echelon form:

R₂ → R₂ - 2R₁: [1 2 0 1; 0 -3 1 -2; 1 1 1 1; 0 1 2 3]
R₃ → R₃ - R₁: [1 2 0 1; 0 -3 1 -2; 0 -1 1 0; 0 1 2 3]

R₂ ↔ R₃: [1 2 0 1; 0 -1 1 0; 0 -3 1 -2; 0 1 2 3]

R₃ → R₃ - 3R₂: [1 2 0 1; 0 -1 1 0; 0 0 -2 -2; 0 1 2 3]
R₄ → R₄ + R₂: [1 2 0 1; 0 -1 1 0; 0 0 -2 -2; 0 0 3 3]

R₄ → R₄ + (3/2)R₃: [1 2 0 1; 0 -1 1 0; 0 0 -2 -2; 0 0 0 0]

We have 3 non-zero rows, so rank = 3. Since rank (3) < number of vectors (4), the vectors are **linearly dependent**.

The dependence relationship can be found by solving the homogeneous system.

## Exam Tips

1. **Remember the definition**: A set is linearly dependent if there exist scalars, not all zero, such that c₁v₁ + ... + cₙvₙ = 0. For independence, only trivial solution exists.

2. **Quick test for two vectors**: Two vectors are dependent if and only if one is a scalar multiple of the other. Check ratios of corresponding components.

3. **Zero vector rule**: Any set containing the zero vector is always linearly dependent. This is a frequently tested point.

4. **Dimension rule**: In ℝⁿ, any set of more than n vectors is linearly dependent. For example, in ℝ³, any set of 4 or more vectors is dependent.

5. **Matrix method**: Form a matrix with vectors as rows/columns, reduce to echelon form, and count pivots. Number of pivots equals the number of linearly independent vectors.

6. **Determinant test**: For n vectors in ℝⁿ, form an n×n matrix and find its determinant. Non-zero determinant implies linear independence.

7. **Understanding "not all zero"**: Remember that for dependence, at least one scalar must be non-zero. The trivial solution always works for any set, but we need non-trivial solutions for dependence.

8. **Practice spanning problems**: Questions often ask to determine if a set spans ℝⁿ or is a basis. This requires understanding both spanning and linear independence.
