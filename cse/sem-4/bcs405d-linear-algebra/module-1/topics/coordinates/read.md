# Coordinates in Linear Algebra

## Table of Contents

- [Coordinates in Linear Algebra](#coordinates-in-linear-algebra)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Ordered Basis and Coordinate Vector](#1-ordered-basis-and-coordinate-vector)
  - [2. Coordinates in ℝⁿ](#2-coordinates-in-)
  - [3. Change of Basis](#3-change-of-basis)
  - [4. Transition Matrix Properties](#4-transition-matrix-properties)
  - [5. Standard Matrix Representation](#5-standard-matrix-representation)
  - [6. Coordinates in Different Coordinate Systems](#6-coordinates-in-different-coordinate-systems)
- [Examples](#examples)
  - [Example 1: Finding Coordinate Vector](#example-1-finding-coordinate-vector)
  - [Example 2: Transition Matrix](#example-2-transition-matrix)
  - [Example 3: Using Transition Matrix](#example-3-using-transition-matrix)
- [Exam Tips](#exam-tips)

## Introduction

Coordinates are fundamental to understanding vector spaces and linear transformations in linear algebra. In the context of the university's Linear Algebra course (BCS405D), coordinates represent how a vector can be expressed as a linear combination of basis vectors. This concept bridges the abstract theory of vector spaces with practical computational methods used in engineering applications.

The study of coordinates becomes essential when we need to work with different bases, transform vectors between coordinate systems, and perform computations efficiently. In computer science and engineering, coordinates play a crucial role in computer graphics, data science, machine learning, and solving systems of linear equations. Understanding how to represent vectors in different coordinate systems allows us to simplify complex problems and choose the most convenient representation for a given task.

This module covers the mathematical foundations of coordinates, including coordinate vectors, change of basis, and transition matrices. These concepts form the backbone of many advanced topics in linear algebra and its applications in engineering disciplines.

## Key Concepts

### 1. Ordered Basis and Coordinate Vector

A **basis** of a vector space V is a set of linearly independent vectors that span V. When we arrange the basis vectors in a specific order, we call it an **ordered basis**. For an n-dimensional vector space, an ordered basis B = {v₁, v₂, ..., vₙ} assigns each vector a unique position.

Given a vector v in V, if v = c₁v₁ + c₂v₂ + ... + cₙvₙ, then the **coordinate vector** of v with respect to the ordered basis B is:

[v]ᵦ = [c₁, c₂, ..., cₙ]ᵀ

The scalars c₁, c₂, ..., cₙ are called the **coordinates** of v relative to basis B. These coordinates are unique for each vector given a specific basis.

### 2. Coordinates in ℝⁿ

In the standard Euclidean space ℝⁿ, the **standard basis** is:

- For ℝ²: e₁ = (1, 0), e₂ = (0, 1)
- For ℝ³: e₁ = (1, 0, 0), e₂ = (0, 1, 0), e₃ = (0, 0, 1)

Any vector v = (x₁, x₂, ..., xₙ) in ℝⁿ can be written as v = x₁e₁ + x₂e₂ + ... + xₙeₙ, so its coordinate vector relative to the standard basis is [x₁, x₂, ..., xₙ]ᵀ.

### 3. Change of Basis

When we have two different bases for the same vector space, we need to find the relationship between the coordinates of a vector with respect to these bases. This leads to the **change of basis** problem.

If B = {v₁, v₂, ..., vₙ} and B' = {u₁, u₂, ..., uₙ} are two ordered bases of an n-dimensional vector space V, and if each vector in B' is expressed in terms of the basis B:

u₁ = a₁₁v₁ + a₂₁v₂ + ... + aₙ₁vₙ
u₂ = a₁₂v₁ + a₂₂v₂ + ... + aₙ₂vₙ
...
uₙ = a₁ₙv₁ + a₂ₙv₂ + ... + aₙₙvₙ

Then the **transition matrix** (or change of basis matrix) from B to B' is the n×n matrix P whose j-th column contains the coordinates of uⱼ relative to B:

P = [ [u₁]ᵦ [u₂]ᵦ ... [uₙ]ᵦ ]

### 4. Transition Matrix Properties

The transition matrix P from basis B to basis B' satisfies the following important relationships:

- If [v]ᵦ is the coordinate vector of v relative to B, then [v]ᵦ' = P[v]ᵦ gives the coordinates relative to B'.
- Conversely, [v]ᵦ = P⁻¹[v]ᵦ' converts coordinates from B' to B.
- The inverse of the transition matrix, P⁻¹, is the transition matrix from B' to B.

### 5. Standard Matrix Representation

For linear transformations, the matrix representation depends on the chosen bases. If T: V → V is a linear transformation, and B is an ordered basis for V, then the **matrix of T relative to basis B** is:

[T]ᵦ = [[T(v₁)]ᵦ [T(v₂)]ᵦ ... [T(vₙ)]ᵦ]

This matrix allows us to compute T(v) in coordinates using [T(v)]ᵦ = [T]ᵦ[v]ᵦ.

### 6. Coordinates in Different Coordinate Systems

In geometry and engineering applications, we often work with various coordinate systems:

- **Cartesian coordinates**: The standard rectangular coordinate system
- **Polar coordinates** (in ℝ²): Points are represented as (r, θ) where r is the distance from origin and θ is the angle from positive x-axis
- **Cylindrical coordinates** (in ℝ³): (r, θ, z)
- **Spherical coordinates** (in ℝ³): (ρ, θ, φ)

The conversion between these coordinate systems involves specific transformation formulas.

## Examples

### Example 1: Finding Coordinate Vector

**Problem**: In ℝ³, let B = {(1,0,0), (0,1,0), (0,0,1)} be the standard basis and B' = {(1,1,0), (0,1,1), (1,0,1)}. Find the coordinate vector of v = (3, 2, 1) relative to basis B'.

**Solution**:

**Step 1**: Express v as a linear combination of B' vectors
Let v = a(1,1,0) + b(0,1,1) + c(1,0,1) = (a+c, a+b, b+c)

**Step 2**: Set up the system of equations
a + c = 3
a + b = 2
b + c = 1

**Step 3**: Solve the system
From a + b = 2, we have b = 2 - a
From b + c = 1, substitute b: (2 - a) + c = 1 ⇒ c = a - 1
From a + c = 3: a + (a - 1) = 3 ⇒ 2a = 4 ⇒ a = 2

Then b = 2 - 2 = 0, and c = 2 - 1 = 1

**Step 4**: Write the coordinate vector
[v]ᵦ' = [2, 0, 1]ᵀ

**Verification**: 2(1,1,0) + 0(0,1,1) + 1(1,0,1) = (2+1, 2+0, 0+1) = (3, 2, 1) ✓

### Example 2: Transition Matrix

**Problem**: Given bases B = {(1,0), (0,1)} and B' = {(1,2), (3,4)} in ℝ², find the transition matrix from B to B'.

**Solution**:

**Step 1**: Express each B' vector in terms of B coordinates
(1,2) = 1(1,0) + 2(0,1) → coordinates: [1, 2]ᵀ
(3,4) = 3(1,0) + 4(0,1) → coordinates: [3, 4]ᵀ

**Step 2**: Form the transition matrix P with these as columns
P = [ [1, 3]ᵀ [2, 4]ᵀ ] = ⎡ 1 3 ⎤
⎣ 2 4 ⎦

**Step 3**: For any vector v = (x, y) in B coordinates, the B' coordinates are:
[v]ᵦ' = P[v]ᵦ = ⎡ 1 3 ⎤ [x]
⎣ 2 4 ⎦ [y]

### Example 3: Using Transition Matrix

**Problem**: Using the transition matrix from Example 2, find the coordinates of v = (5, 7) relative to basis B'.

**Solution**:

**Step 1**: Write v in B coordinates
[v]ᵦ = [5, 7]ᵀ

**Step 2**: Apply the transition matrix
[v]ᵦ' = P[v]ᵦ = ⎡ 1 3 ⎤ [5] = [1(5) + 3(7)] = [5 + 21] = [26]
⎣ 2 4 ⎦ [7] [2(5) + 4(7)] [10 + 28] [38]

**Step 3**: Verify
26(1,2) + 38(3,4) = (26 + 114, 52 + 152) = (140, 204)
This doesn't match (5, 7)! There's an error.

**Correction**: The transition matrix should be P⁻¹. Let's find it:
det(P) = 1(4) - 3(2) = 4 - 6 = -2
P⁻¹ = (1/-2) ⎡ 4 -3 ⎤ = ⎡ -2 1.5 ⎤
⎣ -2 1 ⎦ ⎣ 1 -0.5 ⎦

Now [v]ᵦ' = P⁻¹[v]ᵦ = ⎡ -2 1.5 ⎤ [5] = [(-2)(5) + 1.5(7)] = [-10 + 10.5] = [0.5]
⎣ 1 -0.5 ⎦ [7] [1(5) + (-0.5)(7)] [5 - 3.5] [1.5]

**Verification**: 0.5(1,2) + 1.5(3,4) = (0.5 + 4.5, 1 + 6) = (5, 7) ✓

So [v]ᵦ' = [0.5, 1.5]ᵀ

## Exam Tips

1. **Understand the definition**: Remember that coordinates of a vector v relative to basis B are the scalars c₁, c₂, ..., cₙ such that v = c₁v₁ + c₂v₂ + ... + cₙvₙ.

2. **Transition matrix direction**: The transition matrix P from basis B to B' transforms B-coordinates to B'-coordinates: [v]ᵦ' = P[v]ᵦ. Pay attention to which direction the transformation goes.

3. **Finding transition matrix**: To find P from B to B', write each vector of B' as a linear combination of B vectors and use these coordinates as columns.

4. **Inverse relationship**: If P is the transition matrix from B to B', then P⁻¹ is the transition matrix from B' to B.

5. **Standard basis coordinates**: In ℝⁿ with the standard basis, the coordinate vector of (x₁, x₂, ..., xₙ) is simply [x₁, x₂, ..., xₙ]ᵀ.

6. **Matrix representation of linear transformations**: For a linear transformation T with matrix A in the standard basis, and bases B and B', we have [T]ᵦ' = P⁻¹AP where P is the transition matrix from B to B'.

7. **Verification always helps**: Always verify your answer by reconstructing the original vector from the coordinates to catch calculation errors.

8. **Polar coordinates conversion**: Remember the formulas: x = r cos θ, y = r sin θ, and r = √(x² + y²), θ = arctan(y/x).
