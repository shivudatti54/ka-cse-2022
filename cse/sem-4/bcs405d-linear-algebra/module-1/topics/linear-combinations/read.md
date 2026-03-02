# Linear Combinations

## Table of Contents

- [Linear Combinations](#linear-combinations)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Linear Combination](#definition-of-linear-combination)
  - [Span of a Set of Vectors](#span-of-a-set-of-vectors)
  - [Linear Combination as a System of Equations](#linear-combination-as-a-system-of-equations)
  - [Geometric Interpretation](#geometric-interpretation)
  - [Linear Dependence and Independence](#linear-dependence-and-independence)
  - [Conditions for Linear Combination Existence](#conditions-for-linear-combination-existence)
- [Examples](#examples)
  - [Example 1: Basic Linear Combination in ℝ²](#example-1-basic-linear-combination-in-)
  - [Example 2: Determining if Vector is in Span](#example-2-determining-if-vector-is-in-span)
  - [Example 3: Geometric Interpretation](#example-3-geometric-interpretation)
- [Exam Tips](#exam-tips)

## Introduction

Linear combinations constitute one of the most fundamental concepts in linear algebra, serving as the cornerstone for understanding vector spaces, spanning sets, linear independence, and linear transformations. A linear combination is an expression formed by multiplying each vector in a given set by a scalar (coefficient) and then adding all the resulting products together. This seemingly simple operation unlocks the door to understanding how vectors interact with each other and form the structural framework of multidimensional spaces.

The concept of linear combinations is incredibly versatile and finds applications across numerous fields including physics, engineering, computer science, and economics. In computer graphics, linear combinations are used to create smooth animations and transformations. In machine learning, they form the basis of neural networks and regression analysis. In quantum mechanics, state vectors are combined linearly to represent quantum states. Understanding linear combinations thoroughly is therefore essential for any students, as it provides the mathematical foundation for solving systems of linear equations, performing dimensional analysis, and understanding the behavior of linear systems.

This module explores linear combinations in depth, examining their properties, geometric interpretations, and applications. We will learn how to determine whether a vector can be expressed as a linear combination of other vectors, how to find the coefficients when such an expression exists, and how to interpret these combinations geometrically in two and three-dimensional spaces.

## Key Concepts

### Definition of Linear Combination

Given a set of vectors {v₁, v₂, ..., vₙ} in a vector space V and scalars c₁, c₂, ..., cₙ (typically real numbers), a **linear combination** of these vectors is defined as:

**c₁v₁ + c₂v₂ + ... + cₙvₙ**

The scalars c₁, c₂, ..., cₙ are called the **coefficients** or **weights** of the linear combination. When all coefficients are zero, we obtain the **trivial linear combination**, which always results in the zero vector.

### Span of a Set of Vectors

The **span** of a set of vectors {v₁, v₂, ..., vₙ}, denoted as span{v₁, v₂, ..., vₙ}, is the set of ALL possible linear combinations of these vectors. Mathematically:

**span{v₁, v₂, ..., vₙ} = {c₁v₁ + c₂v₂ + ... + cₙvₙ : c₁, c₂, ..., cₙ ∈ ℝ}**

The span represents the smallest subspace containing all the given vectors. It tells us the complete "reach" or "coverage" of the given set of vectors.

### Linear Combination as a System of Equations

Expressing a vector b as a linear combination of vectors v₁, v₂, ..., vₙ is equivalent to solving the vector equation:

**c₁v₁ + c₂v₂ + ... + cₙvₙ = b**

This can be rewritten as a system of linear equations in matrix form:

**Ac = b**

where A is the matrix whose columns are v₁, v₂, ..., vₙ, c is the column vector of coefficients, and b is the target vector.

### Geometric Interpretation

In ℝ² (2D space):

- A single non-zero vector v spans a line through the origin in the direction of v
- Two non-collinear vectors span the entire ℝ² plane
- The coefficients tell us how much of each direction to include

In ℝ³ (3D space):

- One vector spans a line through the origin
- Two non-parallel, non-collinear vectors span a plane through the origin
- Three non-coplanar vectors span the entire ℝ³ space

### Linear Dependence and Independence

Vectors v₁, v₂, ..., vₙ are **linearly dependent** if there exists a non-trivial linear combination (not all coefficients zero) that equals the zero vector. Otherwise, they are **linearly independent**.

Key theorem: Vectors are linearly dependent if and only if one of them can be expressed as a linear combination of the others.

### Conditions for Linear Combination Existence

The vector b is a linear combination of {v₁, v₂, ..., vₙ} if and only if the system Ac = b is consistent (has at least one solution). This occurs when:

- The augmented matrix [A|b] has the same rank as A
- b belongs to the column space of A

## Examples

### Example 1: Basic Linear Combination in ℝ²

**Problem:** Express the vector b = (7, 11) as a linear combination of v₁ = (1, 2) and v₂ = (3, 4).

**Solution:**

We need to find scalars c₁ and c₂ such that:
c₁(1, 2) + c₂(3, 4) = (7, 11)

This gives us the system:

- c₁ + 3c₂ = 7
- 2c₁ + 4c₂ = 11

From the first equation: c₁ = 7 - 3c₂

Substituting into the second:
2(7 - 3c₂) + 4c₂ = 11
14 - 6c₂ + 4c₂ = 11
14 - 2c₂ = 11
-2c₂ = -3
c₂ = 3/2

Then: c₁ = 7 - 3(3/2) = 7 - 9/2 = 14/2 - 9/2 = 5/2

**Verification:** (5/2)(1, 2) + (3/2)(3, 4) = (5/2 + 9/2, 5 + 6) = (14/2, 11) = (7, 11) ✓

Therefore, b = (5/2)v₁ + (3/2)v₂

### Example 2: Determining if Vector is in Span

**Problem:** Determine whether the vector b = (2, 5, 4) is in the span of v₁ = (1, 2, 1), v₂ = (2, 5, 3), and v₃ = (1, 1, 2).

**Solution:**

We need to solve c₁(1,2,1) + c₂(2,5,3) + c₃(1,1,2) = (2,5,4)

Writing as a system:

- c₁ + 2c₂ + c₃ = 2
- 2c₁ + 5c₂ + c₃ = 5
- c₁ + 3c₂ + 2c₃ = 4

Forming the augmented matrix and row reducing:

| 1 2 1 | 2 |
| 2 5 1 | 5 |
| 1 3 2 | 4 |

R₂ → R₂ - 2R₁: | 1 2 1 | 2 | → | 1 2 1 | 2 |
| 0 1 -1 | 1 | | 0 1 -1 | 1 |
| 1 3 2 | 4 | | 0 1 1 | 2 |

R₃ → R₃ - R₁: | 1 2 1 | 2 |
| 0 1 -1 | 1 |
| 0 1 1 | 2 |

R₃ → R₃ - R₂: | 1 2 1 | 2 |
| 0 1 -1 | 1 |
| 0 0 2 | 1 |

From the last row: 2c₃ = 1, so c₃ = 1/2

From second row: c₂ - c₃ = 1 → c₂ = 1 + c₃ = 1 + 1/2 = 3/2

From first row: c₁ + 2c₂ + c₃ = 2 → c₁ = 2 - 2(3/2) - 1/2 = 2 - 3 - 1/2 = -3/2

**Solution:** c₁ = -3/2, c₂ = 3/2, c₃ = 1/2

Since a solution exists, b is in the span of {v₁, v₂, v₃}.

### Example 3: Geometric Interpretation

**Problem:** In ℝ³, the vectors v₁ = (1, 0, 0) and v₂ = (0, 1, 0) span the xy-plane. What linear combination produces the vector w = (3, 4, 0)?

**Solution:**

Since w lies in the xy-plane (z = 0), it can definitely be expressed as a linear combination of v₁ and v₂.

We need c₁(1, 0, 0) + c₂(0, 1, 0) = (3, 4, 0)

This directly gives us:

- c₁ = 3
- c₂ = 4
- 0 = 0 (satisfied)

Therefore, w = 3v₁ + 4v₂

Geometrically, this means w is obtained by moving 3 units in the x-direction and 4 units in the y-direction from the origin.

## Exam Tips

1. **Understand the definition thoroughly**: Remember that a linear combination involves multiplying each vector by a scalar and summing the results. This is the foundation for all subsequent concepts.

2. **Matrix method is reliable**: For determining if a vector is a linear combination, always set up the augmented matrix [A|b] and perform row reduction. This systematic approach avoids errors.

3. **Span represents ALL possible combinations**: When asked to find the span of a set of vectors, remember it's the set of all possible linear combinations—write this in set notation.

4. **Connection to rank**: A vector b is in the span of columns of A if and only if rank(A) = rank([A|b]). This is a key theorem that frequently appears in exams.

5. **Geometric interpretation matters**: Understand how linear combinations correspond to lines, planes, and entire spaces in ℝ² and ℝ³. This provides intuition and helps solve problems.

6. **Linear dependence test**: To check if vectors are linearly dependent, set up the equation c₁v₁ + c₂v₂ + ... + cₙvₙ = 0 and see if non-trivial solutions exist.

7. **Practice coefficient finding**: Be thorough with solving systems of equations—whether by substitution, elimination, or matrix methods—to find coefficients in linear combinations.

8. **Watch for special cases**: Remember that the zero vector is always a linear combination (trivial case), and any set containing the zero vector is automatically linearly dependent.
