# Basis and Dimension

## Table of Contents

- [Basis and Dimension](#basis-and-dimension)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Linear Independence](#linear-independence)
  - [Spanning Set](#spanning-set)
  - [Definition of Basis](#definition-of-basis)
  - [Dimension](#dimension)
  - [Dimension of Subspaces](#dimension-of-subspaces)
  - [Basis Extension Theorem](#basis-extension-theorem)
  - [Finding Bases for Solution Spaces](#finding-bases-for-solution-spaces)
- [Examples](#examples)
  - [Example 1: Determining if a Set is a Basis](#example-1-determining-if-a-set-is-a-basis)
  - [Example 2: Finding Dimension and Basis of a Subspace](#example-2-finding-dimension-and-basis-of-a-subspace)
  - [Example 3: Basis for the Column Space of a Matrix](#example-3-basis-for-the-column-space-of-a-matrix)
- [Exam Tips](#exam-tips)

## Introduction

Basis and dimension are fundamental concepts in linear algebra that provide a framework for understanding the structure of vector spaces. These concepts are essential for solving systems of linear equations, performing linear transformations, and understanding the geometric properties of vectors in various spaces. In engineering and computer science applications, particularly in computer graphics, machine learning, and signal processing, the ability to characterize vector spaces through their bases and dimensions is crucial.

The concept of a basis allows us to represent any vector in a vector space as a unique linear combination of a set of special vectors called basis vectors. The dimension tells us how many such basis vectors are needed to span the entire space. Together, these concepts provide a complete description of the "size" and structure of a vector space, enabling us to work with infinite-dimensional spaces in a finite, systematic manner.

This topic builds upon the concepts of vector spaces, subspaces, linear independence, and span that were introduced earlier. Understanding basis and dimension is essential for advanced topics such as change of basis, coordinate systems, eigenvalues and eigenvectors, and linear transformations between vector spaces.

## Key Concepts

### Linear Independence

A set of vectors {v₁, v₂, ..., vₖ} in a vector space V is said to be linearly independent if the only scalars c₁, c₂, ..., cₖ satisfying c₁v₁ + c₂v₂ + ... + cₖvₖ = 0 are c₁ = c₂ = ... = cₖ = 0. In other words, no vector in the set can be expressed as a linear combination of the others.

If there exist scalars not all zero such that this linear combination equals the zero vector, the vectors are linearly dependent. Geometrically, in ℝ², two vectors are linearly independent if they do not lie on the same line through the origin. In ℝ³, three vectors are linearly independent if they do not all lie in the same plane through the origin.

**Example:** In ℝ³, the vectors e₁ = (1,0,0), e₂ = (0,1,0), and e₃ = (0,0,1) are linearly independent because if c₁(1,0,0) + c₂(0,1,0) + c₃(0,0,1) = (0,0,0), then c₁ = c₂ = c₃ = 0.

### Spanning Set

A set of vectors {v₁, v₂, ..., vₖ} in a vector space V is said to span V if every vector in V can be written as a linear combination of these vectors. That is, for every v ∈ V, there exist scalars c₁, c₂, ..., cₖ such that v = c₁v₁ + c₂v₂ + ... + cₖvₖ.

The span of a set of vectors is denoted as span{v₁, v₂, ..., vₖ} and represents the smallest subspace containing all these vectors. If span{S} = V, then S is called a spanning set or generating set for V.

**Example:** The set {(1,0), (0,1)} spans ℝ² because any vector (a,b) in ℝ² can be written as a(1,0) + b(0,1).

### Definition of Basis

A basis for a vector space V is a set of vectors that is both linearly independent and spans V. This means that every vector in V can be written uniquely as a linear combination of the basis vectors. The uniqueness property is crucial and distinguishes a basis from merely a spanning set.

**Standard Bases for Common Vector Spaces:**

1. **ℝⁿ:** The standard basis is {e₁, e₂, ..., eₙ} where eᵢ has 1 in the i-th position and 0 elsewhere. For ℝ², this is {(1,0), (0,1)}. For ℝ³, this is {(1,0,0), (0,1,0), (0,0,1)}.

2. **ℝ²:** Besides the standard basis, many other bases exist. For example, {(1,1), (1,-1)} is also a basis for ℝ².

3. **Pₙ (polynomials of degree ≤ n):** The standard basis is {1, x, x², ..., xⁿ}.

4. **M₂ₓ₂ (2×2 matrices):** A standard basis is {[1,0;0,0], [0,1;0,0], [0,0;1,0], [0,0;0,1]}.

### Dimension

The dimension of a vector space V, denoted as dim(V), is the number of vectors in any basis for V. A critical theorem in linear algebra states that all bases for a given vector space have the same number of elements, which justifies the term "dimension."

**Important Results:**

- If dim(V) = n, then any set of n linearly independent vectors in V is a basis.
- If dim(V) = n, then any set of n vectors that spans V is a basis.
- If a set has more than n vectors in an n-dimensional space, it must be linearly dependent.
- If a set has fewer than n vectors, it cannot span the space.

**Examples of Dimensions:**

- dim(ℝⁿ) = n
- dim(Pₙ) = n + 1
- dim(Mₘₓₙ) = m × n
- dim({0}) = 0 (the zero vector space has dimension 0)

### Dimension of Subspaces

If W is a subspace of V, then dim(W) ≤ dim(V). Furthermore, if dim(W) = dim(V) and W is a subspace of V, then W = V. This provides a useful tool for proving that a subspace equals the entire space.

**Example:** In ℝ³, consider the subspace W = {(a,b,0) : a,b ∈ ℝ}, which is the xy-plane. This subspace has dimension 2, while ℝ³ has dimension 3. The standard basis for W is {(1,0,0), (0,1,0)}.

### Basis Extension Theorem

The Basis Extension Theorem (or Steinitz Exchange Lemma) states that if a set S is linearly independent and T is a spanning set, then we can replace elements of T with elements of S to obtain a basis. This theorem guarantees that every linearly independent set can be extended to a basis, and every spanning set contains a basis.

### Finding Bases for Solution Spaces

Consider a homogeneous system of linear equations Ax = 0. The solution set forms a subspace of ℝⁿ called the null space or kernel of A. To find a basis for this space, we solve the system and express the solutions in parametric vector form. The vectors in this parametric representation form a basis for the null space.

## Examples

### Example 1: Determining if a Set is a Basis

**Problem:** Determine whether S = {(1,2,1), (2,1,0), (1,1,1)} is a basis for ℝ³.

**Solution:**

To be a basis for ℝ³, the set must satisfy two conditions:

1. The vectors must be linearly independent
2. The vectors must span ℝ³

Since ℝ³ has dimension 3, and we have 3 vectors, we only need to check one condition (if they are linearly independent, they automatically span, and vice versa).

Form a matrix with these vectors as rows or columns and find its determinant:

A = [1 2 1; 2 1 0; 1 1 1]

det(A) = 1(1×1 - 0×1) - 2(2×1 - 0×1) + 1(2×1 - 1×1)
= 1(1) - 2(2) + 1(2-1)
= 1 - 4 + 1
= -2 ≠ 0

Since the determinant is non-zero, the vectors are linearly independent and span ℝ³. Therefore, S is a basis for ℝ³.

### Example 2: Finding Dimension and Basis of a Subspace

**Problem:** Find the dimension and a basis for the subspace W = {(a,b,c,d) ∈ ℝ⁴ : a + b = 0, c - d = 0}.

**Solution:**

The conditions are:

- a + b = 0 ⇒ b = -a
- c - d = 0 ⇒ c = d

So any vector in W has the form (a, -a, d, d) = a(1,-1,0,0) + d(0,0,1,1).

These two vectors are linearly independent (neither is a scalar multiple of the other).

Therefore, dim(W) = 2, and a basis is {(1,-1,0,0), (0,0,1,1)}.

### Example 3: Basis for the Column Space of a Matrix

**Problem:** Find a basis for the column space of A = [1 1 2; 2 2 4; 1 1 2].

**Solution:**

First, find the column vectors:
C₁ = (1,2,1), C₂ = (1,2,1), C₃ = (2,4,2)

Notice that C₂ = C₁ and C₃ = 2C₁. So all columns are multiples of C₁.

The column space is span{(1,2,1)}.

Since (1,2,1) ≠ 0, it is linearly independent and forms a basis.

Thus, a basis for Col(A) is {(1,2,1)} and dim(Col(A)) = 1.

## Exam Tips

1. **Remember the definition:** A basis must satisfy BOTH conditions - linear independence AND spanning. Many exam errors occur when students check only one condition.

2. **Dimension of ℝⁿ is n:** This is fundamental. The standard basis has exactly n vectors, and any basis for ℝⁿ has exactly n vectors.

3. **Use the determinant test:** For sets of n vectors in ℝⁿ, if the determinant of the matrix formed by these vectors is non-zero, they form a basis.

4. **n linearly independent vectors ⇒ basis in n-dimensional space:** If you have n linearly independent vectors in an n-dimensional space, you automatically have a basis.

5. **Parametric form gives basis:** For solution spaces of homogeneous systems, writing the solution in parametric vector form directly gives a basis.

6. **Know the dimension formulas:** dim(Pₙ) = n+1, dim(Mₘₓₙ) = mn, dim({0}) = 0.

7. **Row space = Column space dimension:** The rank of a matrix equals the dimension of both its row space and column space. This is useful for finding bases of subspaces defined by matrices.

8. **Check linear independence systematically:** Use the definition - assume c₁v₁ + ... + cₖvₖ = 0 and show all cᵢ must be zero, or use row reduction to echelon form.

9. **Extend to basis when needed:** If you have a linearly independent set smaller than the dimension, you can extend it to a basis by adding appropriate vectors.

10. **Common subspaces to remember:** The span of column vectors, null space of a matrix, and coordinate subspaces like the xy-plane in ℝ³ all have predictable dimensions.
