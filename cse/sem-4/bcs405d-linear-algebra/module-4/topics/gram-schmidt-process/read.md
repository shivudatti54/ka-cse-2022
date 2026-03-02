# Gram-Schmidt Orthogonalization Process

## Table of Contents

- [Gram-Schmidt Orthogonalization Process](#gram-schmidt-orthogonalization-process)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Inner Product](#inner-product)
  - [Norm of a Vector](#norm-of-a-vector)
  - [Orthogonal Vectors](#orthogonal-vectors)
  - [Orthonormal Vectors](#orthonormal-vectors)
  - [Projection of One Vector onto Another](#projection-of-one-vector-onto-another)
  - [The Gram-Schmidt Process](#the-gram-schmidt-process)
  - [Connection to QR Decomposition](#connection-to-qr-decomposition)
- [Examples](#examples)
  - [Example 1: Orthogonalization of Two Vectors in ℝ³](#example-1-orthogonalization-of-two-vectors-in-)
  - [Example 2: Complete Orthogonalization in ℝ³](#example-2-complete-orthogonalization-in-)
  - [Example 3: QR Decomposition](#example-3-qr-decomposition)
- [Exam Tips](#exam-tips)

## Introduction

The Gram-Schmidt orthogonalization process is a fundamental algorithm in linear algebra that transforms any set of linearly independent vectors into an orthogonal (or orthonormal) set spanning the same subspace. This process is Named after Jørgen Gram and Erhard Schmidt, who developed this technique independently in the late 19th century. The importance of this process in computational linear algebra cannot be overstated, as it serves as the backbone for numerous applications including QR decomposition, least squares problems, and solving systems of linear equations.

In the context of the university's Linear Algebra course (BCS405D), the Gram-Schmidt process represents one of the most practical topics as it connects theoretical concepts of orthogonality to real-world computational methods. Understanding this process is essential for students students as it appears frequently in signal processing, control systems, and numerical analysis applications. The process not only helps in creating orthogonal bases but also simplifies many matrix computations by working with orthonormal bases.

## Key Concepts

### Inner Product

The inner product (or dot product) of two vectors **u** = (u₁, u₂, ..., uₙ) and **v** = (v₁, v₂, ..., vₙ) in ℝⁿ is defined as:

⟨**u**, **v**⟩ = u₁v₁ + u₂v₂ + ... + uₙvₙ = **u**ᵀ**v**

The inner product satisfies the following properties:

- Commutativity: ⟨**u**, **v**⟩ = ⟨**v**, **u**⟩
- Distributivity: ⟨**u** + **v**, **w**⟩ = ⟨**u**, **w**⟩ + ⟨**v**, **w**⟩
- Scalar multiplication: ⟨c**u**, **v**⟩ = c⟨**u**, **v**⟩ where c is a scalar

### Norm of a Vector

The norm (or length) of a vector **v** is defined as:

||**v**|| = √⟨**v**, **v**⟩ = √(v₁² + v₂² + ... + vₙ²)

### Orthogonal Vectors

Two vectors **u** and **v** are orthogonal if their inner product is zero:

⟨**u**, **v**⟩ = 0

A set of vectors {**v₁**, **v₂**, ..., **vₖ**} is orthogonal if **vᵢ** ⊥ **vⱼ** for all i ≠ j.

### Orthonormal Vectors

A set of vectors is orthonormal if they are orthogonal and each vector has unit length:

⟨**vᵢ**, **vⱼ**⟩ = { 1 if i = j, 0 if i ≠ j }

If **u** is any vector and {**e₁**, **e₂**, ..., **eₙ**} is an orthonormal basis, then:

**u** = ⟨**u**, **e₁**⟩**e₁** + ⟨**u**, **e₂**⟩**e₂** + ... + ⟨**u**, **eₙ**⟩**eₙ**

### Projection of One Vector onto Another

The projection of vector **v** onto vector **u** (where **u** ≠ 0) is given by:

projᵤ(**v**) = (⟨**v**, **u**⟩ / ⟨**u**, **u**⟩) **u**

This projection represents the component of **v** in the direction of **u**.

### The Gram-Schmidt Process

Given a set of linearly independent vectors {**a₁**, **a₂**, ..., **aₙ**}, the Gram-Schmidt process produces an orthogonal set {**q₁**, **q₂**, ..., **qₙ**}.

**Step 1:** Start with **q₁** = **a₁**

**Step 2:** For k = 2 to n:

- Subtract from **aₖ** its projections onto all previously computed orthogonal vectors **q₁**, **q₂**, ..., **qₖ₋₁**
- **qₖ** = **aₖ** - Σⱼ₌₁ᵏ⁻¹ projᵠⱼ(**aₖ**)

The formula becomes:
**qₖ** = **aₖ** - (⟨**aₖ**, **q₁**⟩/⟨**q₁**, **q₁**⟩)**q₁** - (⟨**aₖ**, **q₂**⟩/⟨**q₂**, **q₂**⟩)**q₂** - ... - (⟨**aₖ**, **qₖ₋₁**⟩/⟨**qₖ₋₁**, **qₖ₋₁**⟩)**qₖ₋₁**

**Step 3 (Optional):** To obtain an orthonormal set, normalize each **qₖ**:

**eₖ** = **qₖ** / ||**qₖ**||

### Connection to QR Decomposition

The Gram-Schmidt process is directly used to compute the QR decomposition of a matrix A. If A = [a₁ a₂ ... aₙ] where aᵢ are linearly independent column vectors, then:

A = QR

where Q has orthonormal columns and R is an upper triangular matrix. The columns of Q are exactly the orthonormal vectors obtained from the Gram-Schmidt process, and R contains the coefficients used during orthogonalization.

## Examples

### Example 1: Orthogonalization of Two Vectors in ℝ³

**Problem:** Apply the Gram-Schmidt process to orthogonalize the vectors:
**a₁** = (1, 1, 0) and **a₂** = (1, 0, 1)

**Solution:**

**Step 1:** Set **q₁** = **a₁** = (1, 1, 0)

**Step 2:** Compute **q₂**:

- First, find the projection of **a₂** onto **q₁**:
  proj\_{q₁}(**a₂**) = (⟨**a₂**, **q₁**⟩/⟨**q₁**, **q₁**⟩) **q₁**

⟨**a₂**, **q₁**⟩ = (1)(1) + (0)(1) + (1)(0) = 1

⟨**q₁**, **q₁**⟩ = 1² + 1² + 0² = 2

proj\_{q₁}(**a₂**) = (1/2) **q₁** = (1/2, 1/2, 0)

- Now compute **q₂**:
  **q₂** = **a₂** - proj\_{q₁}(**a₂**)
  **q₂** = (1, 0, 1) - (1/2, 1/2, 0)
  **q₂** = (1 - 1/2, 0 - 1/2, 1 - 0)
  **q₂** = (1/2, -1/2, 1)

**Verification:** Check that **q₁** ⊥ **q₂**:
⟨**q₁**, **q₂**⟩ = (1)(1/2) + (1)(-1/2) + (0)(1) = 1/2 - 1/2 + 0 = 0 ✓

### Example 2: Complete Orthogonalization in ℝ³

**Problem:** Find an orthonormal basis for the subspace spanned by:
**a₁** = (1, 1, 1), **a₂** = (1, 0, 1), **a₃** = (1, 1, 2)

**Solution:**

**Step 1:** **q₁** = **a₁** = (1, 1, 1)

**Step 2:** Compute **q₂**:

- proj\_{q₁}(**a₂**) = (⟨**a₂**, **q₁**⟩/⟨**q₁**, **q₁**⟩) **q₁**
- ⟨**a₂**, **q₁**⟩ = 1 + 0 + 1 = 2
- ⟨**q₁**, **q₁**⟩ = 1 + 1 + 1 = 3
- proj = (2/3)(1, 1, 1) = (2/3, 2/3, 2/3)

- **q₂** = **a₂** - proj = (1, 0, 1) - (2/3, 2/3, 2/3) = (1/3, -2/3, 1/3)

**Step 3:** Compute **q₃**:

- **q₃** = **a₃** - proj*{q₁}(**a₃**) - proj*{q₂}(**a₃**)

- proj\_{q₁}(**a₃**): ⟨**a₃**, **q₁**⟩ = 1+1+2 = 4, so (4/3)(1,1,1) = (4/3,4/3,4/3)

- proj\_{q₂}(**a₃**): First find ⟨**a₃**, **q₂**⟩ and ⟨**q₂**, **q₂**⟩
- ⟨**a₃**, **q₂**⟩ = 1(1/3) + 1(-2/3) + 2(1/3) = 1/3 - 2/3 + 2/3 = 1/3
- ⟨**q₂**, **q₂**⟩ = (1/3)² + (-2/3)² + (1/3)² = 1/9 + 4/9 + 1/9 = 6/9 = 2/3
- proj\_{q₂}(**a₃**) = (1/3)/(2/3) × **q₂** = (1/2) × (1/3, -2/3, 1/3) = (1/6, -1/3, 1/6)

- **q₃** = (1, 1, 2) - (4/3, 4/3, 4/3) - (1/6, -1/3, 1/6)
  = (1 - 4/3 - 1/6, 1 - 4/3 + 1/3, 2 - 4/3 - 1/6)
  = ((6-8-1)/6, (6-8+2)/6, (12-8-1)/6)
  = (-3/6, 0/6, 3/6) = (-1/2, 0, 1/2)

**Step 4:** Normalize to get orthonormal basis:

- ||**q₁**|| = √3, so **e₁** = (1/√3, 1/√3, 1/√3)
- ||**q₂**|| = √(2/3) = √2/√3, so **e₂** = (1/√6, -2/√6, 1/√6)
- ||**q₃**|| = √(1/4 + 0 + 1/4) = √(1/2) = 1/√2, so **e₃** = (-1/√2, 0, 1/√2)

The orthonormal basis is: **{e₁, e₂, e₃}**

### Example 3: QR Decomposition

**Problem:** Find the QR decomposition of A = [[1, 1], [1, 0], [0, 1]]

**Solution:**

The columns are **a₁** = (1,1,0) and **a₂** = (1,0,1)

From Example 1: **q₁** = (1,1,0), **q₂** = (1/2, -1/2, 1)

Normalize:

- **e₁** = (1/√2, 1/√2, 0)
- **q₂** has norm √((1/2)² + (-1/2)² + 1²) = √(1/4 + 1/4 + 1) = √(1.5) = √(3/2)
- **e₂** = (1/√6, -1/√6, 2/√6)

So Q = [[1/√2, 1/√6], [1/√2, -1/√6], [0, 2/√6]]

To find R: R = QᵀA

- R₁₁ = ⟨**e₁**, **a₁**⟩ = (1/√2)(1) + (1/√2)(1) + (0)(0) = 2/√2 = √2
- R₁₂ = ⟨**e₁**, **a₂**⟩ = (1/√2)(1) + (1/√2)(0) + (0)(1) = 1/√2
- R₂₁ = ⟨**e₂**, **a₁**⟩ = (1/√6)(1) + (-1/√6)(1) + (2/√6)(0) = 0
- R₂₂ = ⟨**e₂**, **a₂**⟩ = (1/√6)(1) + (-1/√6)(0) + (2/√6)(1) = 3/√6 = √6/2

Thus, R = [[√2, 1/√2], [0, √6/2]]

Verification: Q × R = A ✓

## Exam Tips

1. **Remember the projection formula**: projᵤ(**v**) = (⟨**v**, **u**⟩/⟨**u**, **u**⟩)**u** is the most important formula in this topic.

2. **Always verify orthogonality**: After computing orthogonal vectors, verify that their dot products equal zero to check your answer.

3. **Don't forget normalization**: If the question asks for an orthonormal set, you must divide each orthogonal vector by its norm.

4. **Order matters**: The Gram-Schmidt process produces vectors in the same order as the input vectors. Changing the order changes the result.

5. **Connection to QR decomposition**: Remember that Gram-Schmidt orthogonalization directly gives the Q matrix in QR decomposition, and R is upper triangular with diagonal entries as norms.

6. **Handle numerical stability**: In practice, modified Gram-Schmidt is more numerically stable than classical Gram-Schmidt for computing QR decomposition.

7. **Linear independence requirement**: The input vectors must be linearly independent for Gram-Schmidt to work. If they're dependent, you'll get a zero vector during the process.
