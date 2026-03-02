# Vector Spaces

## Table of Contents

- [Vector Spaces](#vector-spaces)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of a Vector Space](#definition-of-a-vector-space)
  - [Examples of Vector Spaces](#examples-of-vector-spaces)
  - [Subspaces](#subspaces)
  - [Linear Combinations](#linear-combinations)
  - [Linear Dependence and Independence](#linear-dependence-and-independence)
  - [Basis and Dimension](#basis-and-dimension)
- [Examples](#examples)
  - [Example 1: Verifying a Vector Space](#example-1-verifying-a-vector-space)
  - [Example 2: Checking Linear Independence](#example-2-checking-linear-independence)
  - [Example 3: Finding Basis and Dimension](#example-3-finding-basis-and-dimension)
- [Exam Tips](#exam-tips)

## Introduction

Vector spaces form the foundational structure in linear algebra and are essential for understanding advanced mathematical concepts used in computer science, engineering, and physics. A vector space (also called a linear space) is a collection of vectors that can be added together and multiplied by scalars (numbers) while satisfying specific axioms. This abstract concept generalizes the familiar three-dimensional Euclidean space to arbitrary dimensions, making it a powerful tool for solving systems of linear equations, performing transformations, and analyzing data in higher dimensions.

In the context of computer science, vector spaces play a crucial role in machine learning algorithms, computer graphics, cryptography, and data science. Understanding vector spaces enables engineers to work with multidimensional data, perform linear transformations, and apply mathematical reasoning to complex computational problems. This topic is particularly important for the university's linear algebra course as it establishes the groundwork for understanding matrices, linear transformations, and eigenvalues.

## Key Concepts

### Definition of a Vector Space

A **vector space** V over a field F (typically the real numbers ℝ or complex numbers ℂ) is a set equipped with two operations:

1. **Vector addition**: For any u, v ∈ V, there exists u + v ∈ V
2. **Scalar multiplication**: For any c ∈ F and v ∈ V, there exists cv ∈ V

These operations must satisfy the following ten axioms for all u, v, w ∈ V and all scalars a, b ∈ F:

1. **Closure under addition**: u + v ∈ V
2. **Closure under scalar multiplication**: av ∈ V
3. **Commutativity**: u + v = v + u
4. **Associativity**: (u + v) + w = u + (v + w)
5. **Additive identity**: There exists 0 ∈ V such that v + 0 = v
6. **Additive inverse**: For each v ∈ V, there exists -v ∈ V such that v + (-v) = 0
7. **Multiplicative identity**: 1v = v
8. **Distributivity of scalar multiplication over vector addition**: a(u + v) = au + av
9. **Distributivity of scalar multiplication over field addition**: (a + b)v = av + bv
10. **Associativity of scalar multiplication**: a(bv) = (ab)v

### Examples of Vector Spaces

**Example 1: Euclidean Space ℝⁿ**
The set of all n-tuples of real numbers ℝⁿ = {(x₁, x₂, ..., xₙ) : xᵢ ∈ ℝ} forms a vector space with the usual operations of component-wise addition and scalar multiplication.

**Example 2: Space of Matrices Mₘₙ(ℝ)**
The set of all m × n matrices with real entries is a vector space under matrix addition and scalar multiplication.

**Example 3: Polynomial Space Pₙ**
The set of all polynomials of degree at most n with real coefficients, denoted Pₙ, forms a vector space.

**Example 4: Function Space**
The set of all real-valued functions defined on ℝ forms an infinite-dimensional vector space.

**Non-example:** The set of all 2×2 matrices with determinant equal to 1 is NOT a vector space, as it fails to contain the zero matrix.

### Subspaces

A **subspace** W of a vector space V is a subset of V that is itself a vector space under the same operations as V. The necessary and sufficient conditions for W to be a subspace are:

1. W is non-empty (contains zero vector)
2. For any u, v ∈ W, u + v ∈ W (closure under addition)
3. For any c ∈ F and v ∈ W, cv ∈ W (closure under scalar multiplication)

**Example:** In ℝ³, the set W = {(x, y, 0) : x, y ∈ ℝ} (the xy-plane) is a subspace of ℝ³.

### Linear Combinations

A vector v in V is a **linear combination** of vectors v₁, v₂, ..., vₖ if there exist scalars c₁, c₂, ..., cₖ such that:
v = c₁v₁ + c₂v₂ + ... + cₖvₖ

The set of all linear combinations of v₁, v₂, ..., vₖ is called the **span** of these vectors, denoted as Span{v₁, v₂, ..., vₖ}.

### Linear Dependence and Independence

Vectors v₁, v₂, ..., vₖ are **linearly dependent** if there exist scalars c₁, c₂, ..., cₖ, not all zero, such that:
c₁v₁ + c₂v₂ + ... + cₖvₖ = 0

If the only solution is c₁ = c₂ = ... = cₖ = 0, the vectors are **linearly independent**.

**Key Theorem:** A set of vectors is linearly dependent if and only if at least one vector can be expressed as a linear combination of the others.

### Basis and Dimension

A **basis** of a vector space V is a set of linearly independent vectors that span V. Every basis of a vector space has the same number of elements, called the **dimension** of V, denoted dim(V).

**Standard Basis Examples:**

- ℝⁿ has standard basis {(1,0,...,0), (0,1,...,0), ..., (0,0,...,1)}
- Pₙ has standard basis {1, x, x², ..., xⁿ}
- M₂ₓ₂(ℝ) has standard basis of four matrices

## Examples

### Example 1: Verifying a Vector Space

**Problem:** Show that the set V = {(x, y, x+y) : x, y ∈ ℝ} is a subspace of ℝ³.

**Solution:**

**Step 1:** Check if zero vector is in V.
When x = 0, y = 0, we get (0, 0, 0). Since 0 + 0 = 0, (0, 0, 0) ∈ V. ✓

**Step 2:** Check closure under addition.
Let u = (x₁, y₁, x₁+y₁) and v = (x₂, y₂, x₂+y₂) be in V.
u + v = (x₁+x₂, y₁+y₂, (x₁+y₁)+(x₂+y₂))
= (x₁+x₂, y₁+y₂, (x₁+x₂)+(y₁+y₂))
Since x₁+x₂, y₁+y₂ ∈ ℝ, the sum is in V. ✓

**Step 3:** Check closure under scalar multiplication.
Let c ∈ ℝ and v = (x, y, x+y) ∈ V.
cv = (cx, cy, c(x+y)) = (cx, cy, cx+cy)
Since cx, cy ∈ ℝ, cv ∈ V. ✓

Therefore, V is a subspace of ℝ³.

### Example 2: Checking Linear Independence

**Problem:** Determine whether the vectors v₁ = (1, 2, 3), v₂ = (4, 5, 6), and v₃ = (7, 8, 9) in ℝ³ are linearly independent.

**Solution:**

**Step 1:** Set up the linear combination equation.
c₁v₁ + c₂v₂ + c₃v₃ = 0

c₁(1, 2, 3) + c₂(4, 5, 6) + c₃(7, 8, 9) = (0, 0, 0)

**Step 2:** Write the system of equations.
c₁ + 4c₂ + 7c₃ = 0
2c₁ + 5c₂ + 8c₃ = 0
3c₁ + 6c₂ + 9c₃ = 0

**Step 3:** Solve the system.
Subtract 2×(equation 1) from equation 2:
2c₁ + 5c₂ + 8c₃ - 2c₁ - 8c₂ - 14c₃ = 0
-3c₂ - 6c₃ = 0 ⇒ c₂ = -2c₃

Subtract 3×(equation 1) from equation 3:
3c₁ + 6c₂ + 9c₃ - 3c₁ - 12c₂ - 21c₃ = 0
-6c₂ - 12c₃ = 0 ⇒ c₂ = -2c₃

**Step 4:** Express c₁ in terms of c₃.
From equation 1: c₁ + 4(-2c₃) + 7c₃ = 0
c₁ - 8c₃ + 7c₃ = 0
c₁ = c₃

**Step 5:** Conclusion.
We have non-trivial solutions: c₁ = t, c₂ = -2t, c₃ = t for any t ∈ ℝ.
Since there exist scalars not all zero satisfying the equation, the vectors are **linearly dependent**.

### Example 3: Finding Basis and Dimension

**Problem:** Find a basis and dimension for the subspace W = {(x, y, z, w) ∈ ℝ⁴ : x + y = 0, z - w = 0} of ℝ⁴.

**Solution:**

**Step 1:** Express the constraints.
x + y = 0 ⇒ y = -x
z - w = 0 ⇒ z = w

**Step 2:** Write general element of W.
(x, y, z, w) = (x, -x, z, z) = x(1, -1, 0, 0) + z(0, 0, 1, 1)

**Step 3:** Verify linear independence.
Let c₁(1, -1, 0, 0) + c₂(0, 0, 1, 1) = (0, 0, 0, 0)
This gives: c₁ = 0, -c₁ = 0, c₂ = 0, c₂ = 0
Thus c₁ = 0, c₂ = 0. They are linearly independent.

**Step 4:** Conclude basis and dimension.
Basis: {(1, -1, 0, 0), (0, 0, 1, 1)}
Dimension: 2

## Exam Tips

1. **Memorize the ten vector space axioms** - Questions often ask you to verify if a given set forms a vector space by checking these axioms.

2. **Zero vector test for subspaces** - Always check if the zero vector belongs to the set first; if not, it's not a subspace.

3. **Quick test for linear dependence** - If you have more vectors than dimensions (e.g., 4 vectors in ℝ³), they are automatically linearly dependent.

4. **Span interpretation** - Span{v₁, v₂} represents all vectors that can be written as linear combinations; it always contains the zero vector.

5. **Basis uniqueness** - A vector space can have many bases, but all bases have the same number of elements (dimension).

6. **Standard basis remember** - For ℝⁿ, the standard basis vectors are the columns of the n×n identity matrix.

7. **Subspace verification shortcut** - For W to be a subspace, if u, v ∈ W then u + v ∈ W and cu ∈ W must hold for all scalars c.

8. **Matrix as vector space** - The space of m×n matrices has dimension mn; basis consists of matrices with 1 in one position and 0 elsewhere.
