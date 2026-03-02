# Basis and Dimension

## Introduction to Basis and Dimension

In linear algebra, the concepts of **basis** and **dimension** are fundamental to understanding the structure of vector spaces. These concepts help us describe vector spaces in a precise and efficient manner, allowing us to represent any vector in the space uniquely through a minimal set of vectors.

A basis provides a coordinate system for a vector space, while dimension tells us how many "degrees of freedom" or independent directions exist within that space. Together, they form the foundation for many advanced topics in linear algebra and its applications.

## What is a Basis?

### Formal Definition

A **basis** for a vector space V is a set of vectors that is:

1. **Linearly independent**
2. **Spans** the entire vector space V

In other words, a basis is a minimal spanning set or a maximal linearly independent set.

### Key Properties of a Basis

- **Uniqueness of representation**: Every vector in V can be expressed as a unique linear combination of the basis vectors
- **Minimality**: No proper subset of a basis can span V
- **Maximal independence**: Adding any other vector to a basis makes the set linearly dependent

### Standard Basis Examples

**R² (2D plane)**:
The standard basis is { (1,0), (0,1) }
Any vector (a,b) can be written as: a(1,0) + b(0,1)

**R³ (3D space)**:
The standard basis is { (1,0,0), (0,1,0), (0,0,1) }
Any vector (a,b,c) can be written as: a(1,0,0) + b(0,1,0) + c(0,0,1)

```
Visualization of standard basis in R³:

     z
     ↑
     |   (0,0,1)
     |    /
     |   /
     |  /
     | /
(0,1,0)---→ y
    /
   /
 x ← (1,0,0)
```

## What is Dimension?

### Formal Definition

The **dimension** of a vector space V is the number of vectors in any basis for V. This number is well-defined because all bases for a given vector space have the same number of elements.

### Properties of Dimension

- dim(V) = n, where n is the number of vectors in any basis
- If W is a subspace of V, then dim(W) ≤ dim(V)
- The zero vector space {0} has dimension 0

### Examples of Dimension

- dim(Rⁿ) = n
- dim(Pⁿ) = n+1 (where Pⁿ is the space of polynomials of degree ≤ n)
- dim(M\_{m×n}) = m×n (space of m×n matrices)

## Finding a Basis

### From a Spanning Set

Given a set S that spans V, we can find a basis by eliminating redundant vectors (those that are linear combinations of others).

**Procedure**:

1. Write the vectors as columns of a matrix
2. Reduce to row echelon form
3. The pivot columns correspond to the basis vectors

**Example**: Find a basis for the span of {(1,2,3), (2,4,6), (1,1,1), (0,1,2)}

```
Matrix:
[1  2  1  0]
[2  4  1  1]
[3  6  1  2]

Row reduction:
[1  2  0 -1]
[0  0  1  1]
[0  0  0  0]

Pivot columns: 1 and 3
Basis: {(1,2,3), (1,1,1)}
```

### From a Linearly Independent Set

Given a linearly independent set in V, we can extend it to a basis for V by adding vectors that are not in the span of the current set.

## Coordinate Vectors

Once we have a basis B = {v₁, v₂, ..., vₙ} for V, every vector v ∈ V can be written uniquely as:
v = c₁v₁ + c₂v₂ + ... + cₙvₙ

The **coordinate vector** of v with respect to B is:
[v]ₑ = (c₁, c₂, ..., cₙ)

**Example**: Let B = {(1,1), (1,-1)} be a basis for R². Find the coordinates of (3,1).

```
Solve: (3,1) = a(1,1) + b(1,-1)
System:
a + b = 3
a - b = 1

Solution: a = 2, b = 1
Coordinate vector: (2,1)
```

## Dimension Theorems

### Fundamental Theorem

For any vector space V:

- Any linearly independent set has at most dim(V) vectors
- Any spanning set has at least dim(V) vectors
- Any set with exactly dim(V) vectors that is either linearly independent or spans V is a basis

### Rank-Nullity Theorem

For a linear transformation T: V → W:
dim(ker(T)) + dim(im(T)) = dim(V)

This is also expressed for matrices as:
nullity(A) + rank(A) = number of columns

## Comparing Basis Concepts

| Concept                  | Definition                                        | Example in R³                        |
| ------------------------ | ------------------------------------------------- | ------------------------------------ |
| Spanning Set             | Set whose linear combinations generate all of V   | {(1,0,0), (0,1,0), (0,0,1), (1,1,1)} |
| Linearly Independent Set | No vector can be written as combination of others | {(1,0,0), (0,1,0), (0,0,1)}          |
| Basis                    | Both spanning and linearly independent            | {(1,0,0), (0,1,0), (0,0,1)}          |

## Advanced Examples

### Polynomial Space Basis

The space P₂ of polynomials of degree ≤ 2 has dimension 3.
A standard basis is {1, x, x²}

Any polynomial ax² + bx + c can be written as:
a(x²) + b(x) + c(1)

### Matrix Space Basis

The space M₂₂ of 2×2 matrices has dimension 4.
A standard basis is:

```
{[1 0]  [0 1]  [0 0]  [0 0]}
{[0 0], [0 0], [1 0], [0 1]}
```

## Exam Tips

1. **Basis verification**: To check if a set is a basis, verify both linear independence and spanning
2. **Dimension clues**: If you find n linearly independent vectors in an n-dimensional space, they form a basis
3. **Row reduction**: Use row reduction to find bases from spanning sets or to check independence
4. **Coordinate vectors**: Remember that coordinates depend on the chosen basis
5. **Theorems**: Know the fundamental theorems about basis and dimension
6. **Practice**: Work with different vector spaces (Rⁿ, polynomials, matrices)
7. **Visualization**: For R² and R³, draw diagrams to understand geometric interpretation
