# Subspaces

## Table of Contents

- [Subspaces](#subspaces)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of a Subspace](#definition-of-a-subspace)
  - [The Zero Subspace](#the-zero-subspace)
  - [Trivial and Proper Subspaces](#trivial-and-proper-subspaces)
  - [The Span as a Subspace](#the-span-as-a-subspace)
  - [Operations on Subspaces](#operations-on-subspaces)
  - [Direct Sum](#direct-sum)
  - [Basis and Dimension of Subspaces](#basis-and-dimension-of-subspaces)
- [Examples](#examples)
  - [Example 1: Subspaces in R²](#example-1-subspaces-in-r)
  - [Example 2: Subspaces in R³](#example-2-subspaces-in-r)
  - [Example 3: Direct Sum in R³](#example-3-direct-sum-in-r)
- [Exam Tips](#exam-tips)

## Introduction

In linear algebra, the concept of subspaces is fundamental to understanding the structure of vector spaces. A subspace is essentially a subset of a vector space that itself forms a vector space under the same operations of addition and scalar multiplication. This notion allows us to break down complex vector spaces into smaller, more manageable components that retain all the essential properties of the larger space.

The study of subspaces is crucial in numerous applications across engineering and computer science. In computer graphics, subspaces help in understanding transformations and projections. In machine learning, subspaces are used in dimensionality reduction techniques like Principal Component Analysis (PCA). In data science, the concept of subspace approximation underlies many algorithms. For CSE students, mastering subspaces provides the foundation for understanding more advanced topics such as linear transformations, eigenvalues, and eigenvectors, which are essential in areas like image processing, network analysis, and optimization problems.

This module explores the definition, characterization, and properties of subspaces, along with important operations and relationships between subspaces. Understanding these concepts is essential for solving problems in linear algebra and applying them to real-world engineering problems.

## Key Concepts

### Definition of a Subspace

A subset W of a vector space V (over a field F) is called a subspace of V if W itself is a vector space under the operations defined on V. This means W must satisfy the following conditions:

1. **Non-empty**: W contains the zero vector (0 ∈ W)
2. **Closed under addition**: If u and v are in W, then u + v is in W
3. **Closed under scalar multiplication**: If v is in W and c is any scalar in F, then cv is in W

These three conditions are collectively known as the **subspace test**. If a subset satisfies all three conditions, it is guaranteed to be a subspace of V.

### The Zero Subspace

Every vector space V has at least two subspaces: the zero subspace {0} (also denoted as {0} or O) and the space V itself. The zero subspace contains only the zero vector and is sometimes called the trivial subspace. This subspace satisfies all vector space axioms trivially since it contains only one element.

### Trivial and Proper Subspaces

A subspace W of V is called a **trivial subspace** if W = {0} or W = V. Any subspace that is neither {0} nor V is called a **proper subspace**. For example, in R³, any line through the origin or any plane through the origin is a proper subspace.

### The Span as a Subspace

Given any set of vectors S = {v₁, v₂, ..., vₖ} in a vector space V, the span of S, denoted as span(S) or span{v₁, v₂, ..., vₖ}, is the set of all linear combinations of these vectors. A fundamental theorem states that **the span of any set of vectors is always a subspace of V**. This is because:

- The zero vector can be written as 0·v₁ + 0·v₂ + ... + 0·vₖ
- If u and v are in span(S), then u = a₁v₁ + ... + aₖvₖ and v = b₁v₁ + ... + bₖvₖ, so u + v = (a₁+b₁)v₁ + ... + (aₖ+bₖvₖ) ∈ span(S)
- If v ∈ span(S) and c is a scalar, then cv = (ca₁)v₁ + ... + (caₖ)vₖ ∈ span(S)

### Operations on Subspaces

**Intersection of Subspaces**: If W₁ and W₂ are subspaces of V, then their intersection W₁ ∩ W₂ is also a subspace of V. This is because:

- The zero vector is in both W₁ and W₂, so it's in their intersection
- If u, v ∈ W₁ ∩ W₂, then u, v ∈ W₁ and u, v ∈ W₂, so u + v ∈ W₁ and u + v ∈ W₂, hence u + v ∈ W₁ ∩ W₂
- Similar reasoning applies for scalar multiplication

**Union of Subspaces**: The union of two subspaces is generally NOT a subspace unless one is contained in the other. For example, in R², the union of the x-axis and y-axis is not a subspace because it doesn't contain vectors like (1,1).

**Sum of Subspaces**: The sum of subspaces W₁ + W₂ is defined as {w₁ + w₂ : w₁ ∈ W₁, w₂ ∈ W₂}. This is always a subspace and contains both W₁ and W₂.

### Direct Sum

If W₁ and W₂ are subspaces of V such that W₁ ∩ W₂ = {0}, then the sum W₁ + W₂ is called the **direct sum** and is denoted as W₁ ⊕ W₂. In this case, every vector in W₁ ⊕ W₂ can be uniquely written as w₁ + w₂ where w₁ ∈ W₁ and w₂ ∈ W₂.

### Basis and Dimension of Subspaces

A basis of a subspace W is a linearly independent set that spans W. The dimension of W, denoted as dim(W), is the number of vectors in any basis of W. For subspaces of Rⁿ, we have important relationships:

- If W is a subspace of Rⁿ, then dim(W) ≤ n
- If dim(W) = n, then W = Rⁿ

## Examples

### Example 1: Subspaces in R²

Determine which of the following subsets of R² are subspaces:

(a) W₁ = {(x, y) : x ≥ 0, y ≥ 0} (First quadrant including axes)

(b) W₂ = {(x, y) : x + y = 0}

(c) W₃ = {(x, y) : x = 1}

**Solution:**

(a) W₁ is NOT a subspace. While it contains the zero vector (0,0), it fails closure under scalar multiplication. For example, (1, 1) ∈ W₁, but (-1)(1, 1) = (-1, -1) ∉ W₁ since -1 < 0.

(b) W₂ IS a subspace. Check:

- Zero vector: (0, 0) satisfies 0 + 0 = 0, so (0, 0) ∈ W₂
- Closure under addition: If (x₁, y₁), (x₂, y₂) ∈ W₂, then x₁ + y₁ = 0 and x₂ + y₂ = 0. Then (x₁+x₂) + (y₁+y₂) = (x₁+y₁) + (x₂+y₂) = 0 + 0 = 0, so (x₁+x₂, y₁+y₂) ∈ W₂
- Closure under scalar multiplication: If (x, y) ∈ W₂ and c is a scalar, then x + y = 0, so (cx) + (cy) = c(x+y) = c(0) = 0, hence c(x, y) ∈ W₂

This is the line y = -x through the origin.

(c) W₃ is NOT a subspace. It does not contain the zero vector (0, 0) because 0 ≠ 1. Also, it's not closed under addition or scalar multiplication.

### Example 2: Subspaces in R³

Let W = {(a, b, c) ∈ R³ : a - 2b + c = 0}. Show that W is a subspace of R³ and find its dimension.

**Solution:**

First, verify W is a subspace using the subspace test:

1. Check zero vector: (0, 0, 0) satisfies 0 - 2(0) + 0 = 0, so (0, 0, 0) ∈ W ✓

2. Closure under addition: Let u = (a₁, b₁, c₁) and v = (a₂, b₂, c₂) be in W.
   Then a₁ - 2b₁ + c₁ = 0 and a₂ - 2b₂ + c₂ = 0.
   For u + v = (a₁+a₂, b₁+b₂, c₁+c₂):
   (a₁+a₂) - 2(b₁+b₂) + (c₁+c₂) = (a₁-2b₁+c₁) + (a₂-2b₂+c₂) = 0 + 0 = 0
   So u + v ∈ W ✓

3. Closure under scalar multiplication: Let u = (a, b, c) ∈ W and c be a scalar.
   Then a - 2b + c = 0.
   For cu = (ca, cb, cc):
   ca - 2(cb) + cc = c(a - 2b + c) = c(0) = 0
   So cu ∈ W ✓

Since all three conditions are satisfied, W is a subspace.

To find the dimension, we need a basis. The condition a - 2b + c = 0 gives us a = 2b - c.
So any vector in W can be written as:
(2b - c, b, c) = b(2, 1, 0) + c(-1, 0, 1)

The set {(2, 1, 0), (-1, 0, 1)} spans W and is linearly independent. So it's a basis, and dim(W) = 2.

### Example 3: Direct Sum in R³

In R³, let W₁ = {(x, y, 0) : x, y ∈ R} (the xy-plane) and W₂ = {(0, 0, z) : z ∈ R} (the z-axis). Show that R³ = W₁ ⊕ W₂.

**Solution:**

First, show that W₁ ∩ W₂ = {0}:
If v ∈ W₁ ∩ W₂, then v = (x, y, 0) = (0, 0, z) for some x, y, z.
This gives x = 0, y = 0, and z = 0, so v = (0, 0, 0).

Now show that any vector in R³ can be written as a sum of vectors from W₁ and W₂:
For any (x, y, z) ∈ R³, we can write:
(x, y, z) = (x, y, 0) + (0, 0, z)
where (x, y, 0) ∈ W₁ and (0, 0, z) ∈ W₂.

Since every vector can be uniquely written as such a sum (the representation is unique because W₁ ∩ W₂ = {0}), we have R³ = W₁ ⊕ W₂.

## Exam Tips

1. **Always check the zero vector first**: If a set doesn't contain the zero vector, it's not a subspace. This is the quickest way to eliminate incorrect options in multiple-choice questions.

2. **Use the subspace test systematically**: For any subset, verify all three conditions: non-empty (zero vector), closed under addition, and closed under scalar multiplication.

3. **Remember that spans are always subspaces**: If you're given a set of vectors and asked to show something is a subspace, try to express it as the span of those vectors.

4. **Intersection of subspaces is always a subspace**: But union is not. Remember this distinction when solving problems about operations on subspaces.

5. **Direct sum requires intersection to be trivial**: For W₁ ⊕ W₂, you must verify both W₁ + W₂ spans the space AND W₁ ∩ W₂ = {0}.

6. **Find basis by solving equations**: When a subspace is defined by equations (like a - 2b + c = 0), express one variable in terms of others and identify the spanning vectors.

7. **Dimension formula for direct sum**: If W = W₁ ⊕ W₂, then dim(W) = dim(W₁) + dim(W₂). This is useful for verification.

8. **Visualize geometric subspaces**: In R², subspaces are either {0}, lines through origin, or R² itself. In R³, they are {0}, lines through origin, planes through origin, or R³ itself.
