# Linear Spans

## Table of Contents

- [Linear Spans](#linear-spans)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Linear Combinations](#1-linear-combinations)
  - [2. Definition of Linear Span](#2-definition-of-linear-span)
  - [3. Geometric Interpretation](#3-geometric-interpretation)
  - [4. Spanning Sets](#4-spanning-sets)
  - [5. Span of Two Vectors in ℝ³](#5-span-of-two-vectors-in-)
  - [6. Determining if a Vector Lies in the Span](#6-determining-if-a-vector-lies-in-the-span)
- [Examples](#examples)
  - [Example 1: Finding the Span of Two Vectors in ℝ²](#example-1-finding-the-span-of-two-vectors-in-)
  - [Example 2: Span of a Single Vector](#example-2-span-of-a-single-vector)
  - [Example 3: Checking if Vectors Span ℝ³](#example-3-checking-if-vectors-span-)
  - [Example 4: Vectors That Do Not Span ℝ³](#example-4-vectors-that-do-not-span-)
- [Exam Tips](#exam-tips)

## Introduction

Linear algebra forms the foundation of modern computing, and among its most fundamental concepts is the **linear span**. The linear span describes all possible vectors that can be created by taking linear combinations of a given set of vectors. This concept is crucial in understanding vector spaces, solving systems of linear equations, and performing transformations in computer graphics, machine learning, and data science.

In this module, we explore how to generate entire subspaces using just a finite set of vectors. The linear span answers the question: "What is the set of all vectors that can be written as combinations of these given vectors?" This notion becomes the building block for understanding bases, dimensions, and ultimately, the structure of vector spaces—concepts that are essential for any computer science engineer.

## Key Concepts

### 1. Linear Combinations

A **linear combination** of vectors v₁, v₂, ..., vₖ from a vector space V (over a field F) is an expression of the form:

**c₁v₁ + c₂v₂ + ... + cₖvₖ**

where c₁, c₂, ..., cₖ are scalars (real or complex numbers) belonging to the field F.

For example, in ℝ³, the vector (7, 8, 9) can be written as a linear combination of (1, 0, 0), (0, 1, 0), and (0, 0, 1) as:
7(1, 0, 0) + 8(0, 1, 0) + 9(0, 0, 1) = (7, 8, 9)

Every vector in ℝ³ can be expressed as a linear combination of the standard basis vectors i, j, and k.

### 2. Definition of Linear Span

The **linear span** (or simply **span**) of a set of vectors S = {v₁, v₂, ..., vₖ} in a vector space V is defined as:

**Span(S) = {c₁v₁ + c₂v₂ + ... + cₖvₖ : c₁, c₂, ..., cₖ ∈ F}**

In other words, Span(S) is the set of all possible linear combinations of vectors in S. This set is always a subspace of V.

**Properties of Linear Span:**

- Span(S) always contains the zero vector (by choosing all scalars as 0)
- Span(S) is the smallest subspace containing S
- If S is empty, then Span(S) = {0} (the zero subspace)
- S ⊆ Span(S) always holds

### 3. Geometric Interpretation

In ℝ², the span of a single non-zero vector is a line through the origin. In ℝ³, the span of one non-zero vector is a line through the origin; the span of two linearly independent vectors is a plane through the origin; and three linearly independent vectors span the entire ℝ³ space.

This geometric intuition helps visualize why some sets of vectors can "generate" more of the space than others.

### 4. Spanning Sets

A set S of vectors in a vector space V is called a **spanning set** or **generating set** of V if:

**Span(S) = V**

This means every vector in V can be expressed as a linear combination of vectors in S.

**Important Theorems:**

1. **Standard Spanning Set for ℝⁿ:** The set S = {e₁, e₂, ..., eₙ} where e₁ = (1, 0, ..., 0), e₂ = (0, 1, ..., 0), ..., eₙ = (0, 0, ..., 1) spans ℝⁿ. These are called the standard basis vectors.

2. **Spanning Set for ℝ²:** Any two non-collinear vectors (linearly independent) in ℝ² form a spanning set for ℝ².

3. **Spanning Set for ℝ³:** Any three vectors in ℝ³ that are not coplanar (linearly independent) form a spanning set for ℝ³.

### 5. Span of Two Vectors in ℝ³

Given two vectors v₁ and v₂ in ℝ³:

- If v₁ and v₂ are linearly dependent (one is a scalar multiple of the other), their span is a line through the origin.
- If v₁ and v₂ are linearly independent, their span is a plane through the origin.

### 6. Determining if a Vector Lies in the Span

To determine whether a vector b belongs to Span{v₁, v₂, ..., vₖ}, we solve the vector equation:

**c₁v₁ + c₂v₂ + ... + cₖvₖ = b**

This is equivalent to solving a system of linear equations. If a solution exists, b is in the span; otherwise, it is not.

## Examples

### Example 1: Finding the Span of Two Vectors in ℝ²

**Problem:** Find the span of S = {(1, 2), (3, 4)} in ℝ² and determine if the vector (5, 6) belongs to this span.

**Solution:**

Any vector in Span(S) has the form:
c₁(1, 2) + c₂(3, 4) = (c₁ + 3c₂, 2c₁ + 4c₂)

Let (5, 6) belong to the span. Then:
c₁ + 3c₂ = 5
2c₁ + 4c₂ = 6

Solving the system:
From first equation: c₁ = 5 - 3c₂
Substituting in second: 2(5 - 3c₂) + 4c₂ = 6
10 - 6c₂ + 4c₂ = 6
10 - 2c₂ = 6
-2c₂ = -4
c₂ = 2, then c₁ = 5 - 3(2) = -1

Since we found scalars c₁ = -1 and c₂ = 2, (5, 6) ∈ Span(S).

Since the two given vectors are linearly independent (neither is a scalar multiple of the other), their span is the entire ℝ² space.

### Example 2: Span of a Single Vector

**Problem:** Describe the span of S = {(2, 4, 6)} in ℝ³.

**Solution:**

Span{(2, 4, 6)} = {c(2, 4, 6) : c ∈ ℝ} = {(2c, 4c, 6c) : c ∈ ℝ}

This is a line through the origin in the direction of the vector (2, 4, 6). We can write this as:
{(x, y, z) : y = 2x and z = 3x} or equivalently, the line spanned by (1, 2, 3).

Note: (2, 4, 6) = 2(1, 2, 3), so Span{(2, 4, 6)} = Span{(1, 2, 3)}.

### Example 3: Checking if Vectors Span ℝ³

**Problem:** Does the set S = {(1, 1, 0), (1, 0, 1), (0, 1, 1)} span ℝ³?

**Solution:**

To check if S spans ℝ³, we need to verify if any arbitrary vector (a, b, c) in ℝ³ can be written as a linear combination:
c₁(1, 1, 0) + c₂(1, 0, 1) + c₃(0, 1, 1) = (a, b, c)

This gives the system:
c₁ + c₂ = a
c₁ + c₃ = b
c₂ + c₃ = c

Adding all three equations:
2(c₁ + c₂ + c₃) = a + b + c
c₁ + c₂ + c₃ = (a + b + c)/2

Solving for individual variables:
c₁ = (a + b - c)/2
c₂ = (a - b + c)/2
c₃ = (-a + b + c)/2

Since we can always find scalars for any (a, b, c), S spans ℝ³. Alternatively, we can check that the determinant of the coefficient matrix is non-zero, confirming linear independence and hence spanning.

### Example 4: Vectors That Do Not Span ℝ³

**Problem:** Show that S = {(1, 0, 0), (0, 1, 0)} does not span ℝ³.

**Solution:**

Any vector in Span(S) has the form:
c₁(1, 0, 0) + c₂(0, 1, 0) = (c₁, c₂, 0)

The third component is always 0. Therefore, vectors like (0, 0, 1) or (1, 1, 1) cannot be expressed as linear combinations of vectors in S.

Thus, Span(S) = {(x, y, 0) : x, y ∈ ℝ}, which is the xy-plane in ℝ³, not the entire ℝ³.

## Exam Tips

1. **Understanding the Definition:** Memorize the formal definition of linear span and be able to write it mathematically. This is frequently tested in university exams.

2. **Span Always Contains Zero Vector:** Remember that Span(S) always contains the zero vector regardless of S. This is a key property used in many proofs.

3. **Geometric Interpretation:** For ℝ² and ℝ³, visualize spans as lines or planes through the origin. Understand when a span equals the entire space.

4. **Checking if Vector is in Span:** To check if vector b is in Span{v₁, v₂, ..., vₖ}, set up the equation c₁v₁ + c₂v₂ + ... + cₖvₖ = b and solve for the scalars using Gaussian elimination or substitution.

5. **Linear Independence and Spanning:** Remember that n linearly independent vectors in ℝⁿ always span ℝⁿ. Conversely, if n vectors span ℝⁿ, they must be linearly independent.

6. **Standard Basis:** The standard basis vectors e₁, e₂, ..., eₙ always span ℝⁿ. This is a fundamental example to remember.

7. **Span of Two Vectors in ℝ³:** Two linearly independent vectors in ℝ³ span a plane; two dependent vectors span a line through the origin.

8. **Minimal Spanning Sets:** A spanning set can often be reduced. If one vector can be written as a linear combination of others, removing it doesn't change the span—this is key to understanding bases.

9. **Solving Systems:** The problem of determining if a vector lies in a span reduces to solving a system of linear equations. Be proficient in Gaussian elimination.

10. **Applications:** In computer graphics, spans determine the subspace (plane/line) on which transformations occur. In machine learning, spans help understand feature spaces.
