# Inner Product Spaces

## Table of Contents

- [Inner Product Spaces](#inner-product-spaces)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Definition of Inner Product](#1-definition-of-inner-product)
  - [2. Standard Inner Products](#2-standard-inner-products)
  - [3. Norm Induced by Inner Product](#3-norm-induced-by-inner-product)
  - [4. Cauchy-Schwarz Inequality](#4-cauchy-schwarz-inequality)
  - [5. Triangle Inequality](#5-triangle-inequality)
  - [6. Orthogonal and Orthonormal Vectors](#6-orthogonal-and-orthonormal-vectors)
  - [7. Gram-Schmidt Orthogonalization Process](#7-gram-schmidt-orthogonalization-process)
  - [8. Orthogonal Complement](#8-orthogonal-complement)
  - [9. Best Approximation Theorem](#9-best-approximation-theorem)
- [Examples](#examples)
  - [Example 1: Verifying Inner Product in ℝ²](#example-1-verifying-inner-product-in-)
  - [Example 2: Applying Cauchy-Schwarz Inequality](#example-2-applying-cauchy-schwarz-inequality)
  - [Example 3: Gram-Schmidt Process](#example-3-gram-schmidt-process)
- [Exam Tips](#exam-tips)

## Introduction

Inner Product Spaces are fundamental structures in linear algebra that extend the familiar dot product from Euclidean geometry to more abstract vector spaces. While a vector space provides the framework for adding and scaling vectors, an inner product space adds the crucial concept of "length" and "angle" between vectors, enabling geometric intuition in higher-dimensional spaces. This generalization is essential for numerous applications in engineering, physics, computer science, and applied mathematics.

In this module, we explore how inner products transform abstract vector spaces into metric spaces where concepts like distance, orthogonality, and projection become meaningful. The Cauchy-Schwarz inequality and Gram-Schmidt orthogonalization process are among the most important tools we develop, forming the foundation for topics in functional analysis, quantum mechanics, least-squares approximations, and signal processing.

## Key Concepts

### 1. Definition of Inner Product

An inner product on a vector space V over field F (where F is ℝ or ℂ) is a function that maps each ordered pair of vectors (u, v) to a scalar ⟨u, v⟩, satisfying the following axioms for all u, v, w ∈ V and all scalars α:

**Inner Product Axioms:**

1. **Conjugate Symmetry (Hermitian property):** ⟨u, v⟩ =\overline{⟨v, u⟩}

- For real vector spaces: ⟨u, v⟩ = ⟨v, u⟩
- For complex vector spaces: inner product of a vector with itself equals conjugate

2. **Linearity in the first argument:** ⟨αu + v, w⟩ = α⟨u, w⟩ + ⟨v, w⟩

3. **Positive-definiteness:** ⟨v, v⟩ ≥ 0, and ⟨v, v⟩ = 0 if and only if v = 0

A vector space equipped with an inner product is called an **inner product space**.

### 2. Standard Inner Products

**In ℝⁿ (Real n-dimensional space):**
The standard (Euclidean) inner product is:
⟨u, v⟩ = u₁v₁ + u₂v₂ + ... + uₙvₙ = uᵀv

where u = (u₁, u₂, ..., uₙ) and v = (v₁, v₂, ..., vₙ)

**In ℂⁿ (Complex n-dimensional space):**
⟨u, v⟩ = u₁\overline{v₁} + u₂\overline{v₂} + ... + uₙ\overline{vₙ}

**For matrices (Fᵐˣⁿ):**
⟨A, B⟩ = trace(BᵀA) = ΣᵢΣⱼ AᵢⱼBᵢⱼ

**For continuous functions on [a, b]:**
⟨f, g⟩ = ∫ₐᵇ f(x)g(x)dx

### 3. Norm Induced by Inner Product

The **norm** (or length) of a vector v in an inner product space is defined as:
‖v‖ = √⟨v, v⟩

This satisfies the norm axioms:

- ‖v‖ ≥ 0, and ‖v‖ = 0 iff v = 0
- ‖αv‖ = |α|·‖v‖
- ‖u + v‖ ≤ ‖u‖ + ‖v‖ (Triangle Inequality)

### 4. Cauchy-Schwarz Inequality

For any vectors u, v in an inner product space:
|⟨u, v⟩| ≤ ‖u‖ · ‖v‖

Equality holds if and only if u and v are linearly dependent (one is a scalar multiple of the other).

**Proof sketch:** Consider the quadratic polynomial P(t) = ‖u - tv‖² ≥ 0. This leads to a quadratic in t whose discriminant must be non-positive, yielding the inequality.

### 5. Triangle Inequality

‖u + v‖ ≤ ‖u‖ + ‖v‖

This follows directly from the Cauchy-Schwarz inequality.

### 6. Orthogonal and Orthonormal Vectors

Two vectors u and v are **orthogonal** (perpendicular) if:
⟨u, v⟩ = 0

A set of vectors {v₁, v₂, ..., vₖ} is **orthogonal** if ⟨vᵢ, vⱼ⟩ = 0 for all i ≠ j.

A set is **orthonormal** if it is orthogonal and each vector has unit norm:
⟨vᵢ, vⱼ⟩ = δᵢⱼ (Kronecker delta)

### 7. Gram-Schmidt Orthogonalization Process

This process converts any set of linearly independent vectors into an orthogonal (or orthonormal) set spanning the same subspace.

**Algorithm:**
Given linearly independent vectors {w₁, w₂, ..., wₙ}:

**Step 1:** v₁ = w₁

**Step 2:** v₂ = w₂ - proj\_{v₁}(w₂) = w₂ - (⟨w₂, v₁⟩/⟨v₁, v₁⟩)v₁

**Step 3:** v₃ = w₃ - proj*{v₁}(w₃) - proj*{v₂}(w₃)
= w₃ - (⟨w₃, v₁⟩/⟨v₁, v₁⟩)v₁ - (⟨w₃, v₂⟩/⟨v₂, v₂⟩)v₂

**General step k:**
vₖ = wₖ - Σᵢ₌₁ᵏ⁻¹ (⟨wₖ, vᵢ⟩/⟨vᵢ, vᵢ⟩)vᵢ

For orthonormal set: uᵢ = vᵢ/‖vᵢ‖

### 8. Orthogonal Complement

For a subspace W of an inner product space V, the **orthogonal complement** W⊥ is defined as:
W⊥ = {v ∈ V : ⟨v, w⟩ = 0 for all w ∈ W}

**Properties:**

- W⊥ is a subspace of V
- W ∩ W⊥ = {0}
- dim(W) + dim(W⊥) = dim(V)
- (W⊥)⊥ = W (for finite-dimensional spaces)

### 9. Best Approximation Theorem

Let W be a finite-dimensional subspace of an inner product space V, and let v ∈ V. The vector w₀ ∈ W that minimizes ‖v - w‖ is the **orthogonal projection** of v onto W, denoted proj_W(v).

The error v - proj_W(v) is orthogonal to every vector in W.

## Examples

### Example 1: Verifying Inner Product in ℝ²

**Problem:** Show that ⟨(x₁, y₁), (x₂, y₂)⟩ = 2x₁x₂ + 3y₁y₂ defines an inner product on ℝ².

**Solution:**

We verify the three axioms:

**1. Symmetry:**
⟨u, v⟩ = 2x₁x₂ + 3y₁y₂ = 2x₂x₁ + 3y₂y₁ = ⟨v, u⟩ ✓

**2. Linearity:**
⟨αu + v, w⟩ = ⟨(αx₁ + x₂, αy₁ + y₂), (x₃, y₃)⟩
= 2(αx₁ + x₂)x₃ + 3(αy₁ + y₂)y₃
= α(2x₁x₃ + 3y₁y₃) + (2x₂x₃ + 3y₂y₃)
= α⟨u, w⟩ + ⟨v, w⟩ ✓

**3. Positive-definiteness:**
⟨(x, y), (x, y)⟩ = 2x² + 3y² ≥ 0
And 2x² + 3y² = 0 implies x = 0 and y = 0, so (x, y) = (0, 0) ✓

All axioms satisfied. This is a valid inner product.

### Example 2: Applying Cauchy-Schwarz Inequality

**Problem:** Verify Cauchy-Schwarz inequality for u = (1, 2, 2) and v = (1, 0, 1) in ℝ³ with standard inner product.

**Solution:**

**Compute ‖u‖:**
⟨u, u⟩ = 1² + 2² + 2² = 1 + 4 + 4 = 9
‖u‖ = √9 = 3

**Compute ‖v‖:**
⟨v, v⟩ = 1² + 0² + 1² = 1 + 0 + 1 = 2
‖v‖ = √2

**Compute ⟨u, v⟩:**
⟨u, v⟩ = 1×1 + 2×0 + 2×1 = 1 + 0 + 2 = 3

**Verify inequality:**
|⟨u, v⟩| = 3
‖u‖·‖v‖ = 3 × √2 ≈ 4.24

Since 3 ≤ 3√2, the inequality holds.

### Example 3: Gram-Schmidt Process

**Problem:** Apply Gram-Schmidt to transform basis {(1, 1, 0), (1, 0, 1), (0, 1, 1)} into an orthogonal basis.

**Solution:**

Let w₁ = (1, 1, 0), w₂ = (1, 0, 1), w₃ = (0, 1, 1)

**Step 1:** v₁ = w₁ = (1, 1, 0)

**Step 2:**
proj\_{v₁}(w₂) = (⟨w₂, v₁⟩/⟨v₁, v₁⟩)v₁
⟨w₂, v₁⟩ = 1×1 + 0×1 + 1×0 = 1
⟨v₁, v₁⟩ = 1² + 1² + 0² = 2
proj = (1/2)(1, 1, 0) = (1/2, 1/2, 0)

v₂ = w₂ - proj = (1, 0, 1) - (1/2, 1/2, 0) = (1/2, -1/2, 1)

**Step 3:**
proj onto v₁: ⟨w₃, v₁⟩ = 0×1 + 1×1 + 1×0 = 1
(⟨w₃, v₁⟩/⟨v₁, v₁⟩)v₁ = (1/2)(1, 1, 0) = (1/2, 1/2, 0)

proj onto v₂: ⟨w₃, v₂⟩ = 0×(1/2) + 1×(-1/2) + 1×1 = -1/2 + 1 = 1/2
⟨v₂, v₂⟩ = (1/2)² + (-1/2)² + 1² = 1/4 + 1/4 + 1 = 1.5 = 3/2
(⟨w₃, v₂⟩/⟨v₂, v₂⟩)v₂ = (1/2)/(3/2) × (1/2, -1/2, 1) = (1/3)(1/2, -1/2, 1)
= (1/6, -1/6, 1/3)

v₃ = w₃ - proj₁ - proj₂ = (0, 1, 1) - (1/2, 1/2, 0) - (1/6, -1/6, 1/3)
= (0 - 1/2 - 1/6, 1 - 1/2 + 1/6, 1 - 0 - 1/3)
= (-2/3, 2/3, 2/3)

**Orthogonal basis:** {(1, 1, 0), (1/2, -1/2, 1), (-2/3, 2/3, 2/3)}

**Normalized (orthonormal):**
u₁ = (1/√2, 1/√2, 0)
u₂ = (1/√6, -1/√6, 2/√6)
u₃ = (-1/√6, 1/√6, 1/√6)

## Exam Tips

1. **Remember the inner product axioms:** For any exam question on verifying inner products, you must prove all three properties: symmetry, linearity, and positive-definiteness.

2. **Cauchy-Schwarz is frequently tested:** Be prepared to apply |⟨u, v⟩| ≤ ‖u‖·‖v‖ with both real and complex inner products. Remember that equality indicates linear dependence.

3. **Gram-Schmidt is a computation-heavy topic:** Practice the process thoroughly. The projection formula proj_v(w) = (⟨w, v⟩/⟨v, v⟩)v must be memorized and applied carefully.

4. **Orthogonal complements properties:** Know that W ⊕ W⊥ = V for finite-dimensional spaces, and remember the dimension relationship: dim(W) + dim(W⊥) = dim(V).

5. **Best approximation theorem:** Understand that the projection onto a subspace gives the closest point in that subspace—this is fundamental for least-squares problems.

6. **Complex inner products:** Remember the conjugate in the second argument: ⟨u, v⟩ = ū₁v₁ + ū₂v₂ + ... + ūₙvₙ. This is a common source of errors.

7. **Work with the standard inner product first:** In exam problems, unless specified otherwise, use the standard Euclidean inner product ⟨u, v⟩ = uᵀv.

8. **Orthogonal matrices:** If Q is an orthogonal matrix (QᵀQ = I), then its columns form an orthonormal basis of ℝⁿ. This is a useful connection to remember.
