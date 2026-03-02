# Orthogonal Sets and Bases

## Table of Contents

- [Orthogonal Sets and Bases](#orthogonal-sets-and-bases)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Orthogonal Vectors](#orthogonal-vectors)
  - [Orthogonal Sets](#orthogonal-sets)
  - [Orthonormal Sets](#orthonormal-sets)
  - [Orthogonal Basis and Orthonormal Basis](#orthogonal-basis-and-orthonormal-basis)
  - [Gram-Schmidt Orthogonalization Process](#gram-schmidt-orthogonalization-process)
  - [QR Decomposition](#qr-decomposition)
- [Examples](#examples)
  - [Example 1: Verifying Orthogonal Sets](#example-1-verifying-orthogonal-sets)
  - [Example 2: Gram-Schmidt Orthogonalization](#example-2-gram-schmidt-orthogonalization)
  - [Example 3: Coordinates Relative to Orthogonal Basis](#example-3-coordinates-relative-to-orthogonal-basis)
- [Exam Tips](#exam-tips)

## Introduction

Orthogonal sets and bases form a fundamental concept in linear algebra with extensive applications in engineering, physics, computer science, and statistics. In the context of the university's Linear Algebra course, understanding orthogonal vectors, orthogonal sets, and orthonormal bases is crucial for solving systems of linear equations, performing dimension reduction in data science, and understanding spectral methods in signal processing.

The concept of orthogonality generalizes the notion of perpendicularity from Euclidean geometry to abstract vector spaces. When vectors are orthogonal, they possess special properties that simplify computations and provide elegant solutions to complex problems. For instance, in computer graphics, orthogonal bases enable efficient rendering and transformation of 3D objects. In machine learning, orthonormal bases underlie Principal Component Analysis (PCA), a widely used dimensionality reduction technique.

This module explores the theory of orthogonal sets, their properties, construction methods using the Gram-Schmidt process, and applications in finding solutions to least squares problems. Mastery of these concepts is essential for engineers as they form the foundation for Fourier series, signal processing, and solving differential equations.

## Key Concepts

### Orthogonal Vectors

Two vectors **u** and **v** in ℝⁿ are said to be orthogonal if their dot product is zero. Mathematically, **u** · **v** = 0. The zero vector is orthogonal to every vector in the space. Geometrically, orthogonal vectors meet at a right angle (90 degrees), which is why the term "perpendicular" is sometimes used interchangeably with orthogonal in Euclidean spaces.

The orthogonality condition can be extended to consider the concept of orthogonal complements. If **u** is orthogonal to every vector in a subspace W, then **u** belongs to the orthogonal complement of W, denoted as W⊥. This concept is particularly useful in solving systems of linear equations and in understanding the fundamental theorem of linear algebra.

### Orthogonal Sets

A set of non-zero vectors {**v**₁, **v**₂, ..., **v**ₖ} in ℝⁿ is called an orthogonal set if every pair of distinct vectors is orthogonal. That is, **v**ᵢ · **v**ⱼ = 0 for i ≠ j. The remarkable property of orthogonal sets is that the vectors are linearly independent. This can be proven by showing that if a linear combination equals zero, taking the dot product with each vector forces all coefficients to be zero.

For example, the set {**v**₁ = (1, 1, 0), **v**₂ = (1, -1, 0), **v**₃ = (0, 0, 1)} forms an orthogonal set in ℝ³, as **v**₁ · **v**₂ = 1(1) + 1(-1) + 0(0) = 0, **v**₁ · **v**₃ = 0, and **v**₂ · **v**₃ = 0.

### Orthonormal Sets

An orthonormal set is an orthogonal set where each vector has unit length (norm equal to 1). In other words, a set {**u**₁, **u**₂, ..., **u**ₖ} is orthonormal if **u**ᵢ · **u**ⱼ = 0 for i ≠ j, and ||**u**ᵢ|| = 1 for all i. Equivalently, we can write the condition as **u**ᵢ · **u**ⱼ = δᵢⱼ, where δᵢⱼ is the Kronecker delta (δᵢⱼ = 1 if i = j, and 0 otherwise).

The standard basis {**e**₁, **e**₂, ..., **e**ₙ} in ℝⁿ is a classic example of an orthonormal basis. The process of converting an orthogonal set to an orthonormal set involves normalizing each vector by dividing it by its norm.

### Orthogonal Basis and Orthonormal Basis

An orthogonal basis for a subspace W is a basis consisting of orthogonal vectors. An orthonormal basis is an orthogonal basis where all basis vectors have unit length. The standard basis in ℝⁿ is an orthonormal basis. Orthogonal and orthonormal bases are particularly useful because they simplify coordinate representation and projection operations.

Given an orthogonal basis {**v**₁, **v**₂, ..., **v**ₙ} for ℝⁿ, any vector **x** can be expressed as a linear combination **x** = c₁**v**₁ + c₂**v**₂ + ... + cₙ**v**ₙ, where the coefficients can be computed using the formula cᵢ = (**x** · **v**ᵢ)/(**v**ᵢ · **v**ᵢ). This formula is remarkably simple compared to solving a system of equations, making orthogonal bases extremely valuable for computations.

For an orthonormal basis {**u**₁, **u**₂, ..., **u**ₙ}, the coefficients become even simpler: cᵢ = **x** · **u**ᵢ. This is because the denominator becomes 1 when the basis vectors are normalized.

### Gram-Schmidt Orthogonalization Process

The Gram-Schmidt process is an algorithm that constructs an orthogonal (or orthonormal) basis from any set of linearly independent vectors. This is one of the most important algorithms in linear algebra and numerical analysis.

Given linearly independent vectors {**x**₁, **x**₂, ..., **x**ₙ}, the Gram-Schmidt process produces orthogonal vectors {**v**₁, **v**₂, ..., **v**ₙ} as follows:

**Step 1:** Set **v**₁ = **x**₁

**Step 2:** For j = 2 to n:
**v**ⱼ = **x**ⱼ - Σᵢ₌₁^(j-1) [(**x**ⱼ · **v**ᵢ)/(**v**ᵢ · **v**ᵢ)] **v**ᵢ

The subtraction removes the components of **x**ⱼ in the directions of previously computed orthogonal vectors **v**₁, **v**₂, ..., **v**ⱼ₋₁.

To obtain an orthonormal basis, normalize each **v**ⱼ by computing **u**ⱼ = **v**ⱼ/||**v**ⱼ||.

### QR Decomposition

The Gram-Schmidt process leads directly to the QR decomposition of a matrix. If A is an m×n matrix with linearly independent columns, then A = QR, where Q is an m×n matrix with orthonormal columns and R is an n×n upper triangular matrix with positive diagonal entries. The columns of Q form an orthonormal basis for the column space of A, and R contains the coefficients relating the original columns to the orthonormal columns.

## Examples

### Example 1: Verifying Orthogonal Sets

**Problem:** Determine whether the set S = {(1, 2, 2), (2, 1, -2), (2, -2, 1)} is orthogonal.

**Solution:**
To verify orthogonality, we compute dot products between all pairs of distinct vectors.

**v**₁ · **v**₂ = 1(2) + 2(1) + 2(-2) = 2 + 2 - 4 = 0

**v**₁ · **v**₃ = 1(2) + 2(-2) + 2(1) = 2 - 4 + 2 = 0

**v**₂ · **v**₃ = 2(2) + 1(-2) + (-2)(1) = 4 - 2 - 2 = 0

Since all pairwise dot products equal zero, the set S is orthogonal. Furthermore, since we have three non-zero orthogonal vectors in ℝ³, they form a basis for ℝ³.

### Example 2: Gram-Schmidt Orthogonalization

**Problem:** Apply the Gram-Schmidt process to transform the linearly independent vectors **x**₁ = (1, 1, 0), **x**₂ = (1, 0, 1), and **x**₃ = (0, 1, 1) into an orthogonal set.

**Solution:**

**Step 1:** **v**₁ = **x**₁ = (1, 1, 0)

**Step 2:** Compute **v**₂:

- Projection of **x**₂ onto **v**₁: proj\_{v₁}(**x**₂) = [(**x**₂ · **v**₁)/(**v**₁ · **v**₁)] **v**₁
- **x**₂ · **v**₁ = 1(1) + 0(1) + 1(0) = 1
- **v**₁ · **v**₁ = 1² + 1² + 0² = 2
- proj = (1/2) **v**₁ = (1/2, 1/2, 0)
- **v**₂ = **x**₂ - proj = (1, 0, 1) - (1/2, 1/2, 0) = (1/2, -1/2, 1)

**Step 3:** Compute **v**₃:

- We need to subtract projections onto both **v**₁ and **v**₂
- proj\_{v₁}(**x**₃) = [(**x**₃ · **v**₁)/(**v**₁ · **v**₁)] **v**₁
- **x**₃ · **v**₁ = 0(1) + 1(1) + 1(0) = 1
- proj = (1/2) **v**₁ = (1/2, 1/2, 0)
- proj\_{v₂}(**x**₃) = [(**x**₃ · **v**₂)/(**v**₂ · **v**₂)] **v**₂
- **x**₃ · **v**₂ = 0(1/2) + 1(-1/2) + 1(1) = 1/2
- **v**₂ · **v**₂ = (1/2)² + (-1/2)² + 1² = 1/4 + 1/4 + 1 = 1.5 = 3/2
- proj = (1/2)/(3/2) **v**₂ = (1/3) **v**₂ = (1/6, -1/6, 1/3)
- **v**₃ = **x**₃ - proj*{v₁} - proj*{v₂} = (0, 1, 1) - (1/2, 1/2, 0) - (1/6, -1/6, 1/3)
  = (-2/3, 2/3, 2/3)

Therefore, the orthogonal set is {**v**₁ = (1, 1, 0), **v**₂ = (1/2, -1/2, 1), **v**₃ = (-2/3, 2/3, 2/3)}.

### Example 3: Coordinates Relative to Orthogonal Basis

**Problem:** Given the orthogonal basis {**v**₁ = (2, 0, 0), **v**₂ = (0, 3, 0), **v**₃ = (0, 0, 4)} for ℝ³, find the coordinates of **x** = (4, 6, 8) relative to this basis.

**Solution:**

Since we have an orthogonal basis, we use the formula cᵢ = (**x** · **v**ᵢ)/(**v**ᵢ · **v**ᵢ):

c₁ = **x** · **v**₁ / (**v**₁ · **v**₁) = (4, 6, 8) · (2, 0, 0) / (2² + 0 + 0) = 8/4 = 2

c₂ = **x** · **v**₂ / (**v**₂ · **v**₂) = (4, 6, 8) · (0, 3, 0) / (0 + 3² + 0) = 18/9 = 2

c₃ = **x** · **v**₃ / (**v**₃ · **v**₃) = (4, 6, 8) · (0, 0, 4) / (0 + 0 + 4²) = 32/16 = 2

Thus, **x** = 2**v**₁ + 2**v**₂ + 2**v**₃ = (4, 0, 0) + (0, 6, 0) + (0, 0, 8), and the coordinate vector is [2, 2, 2].

## Exam Tips

1. **Remember the orthogonality condition**: For vectors **u** and **v** in ℝⁿ, they are orthogonal if and only if **u** · **v** = 0. Always compute dot products to verify orthogonality.

2. **Orthogonal sets are linearly independent**: This is a key theorem frequently tested in university exams. If you can verify a set is orthogonal (and non-zero), you can conclude it's linearly independent.

3. **Gram-Schmidt formula mastery**: The formula for the j-th orthogonal vector is **v**ⱼ = **x**ⱼ - Σᵢ₌₁^(j-1) proj\_{vᵢ}(**x**ⱼ). Practice this formula with at least 3-4 examples.

4. **Normalize for orthonormal bases**: After Gram-Schmidt, divide each vector by its norm to get an orthonormal set. This step is often tested in problem papers.

5. **Coordinate computation shortcut**: With orthogonal bases, coordinates are computed as cᵢ = (**x** · **v**ᵢ)/(**v**ᵢ · **v**ᵢ). With orthonormal bases, it's simply cᵢ = **x** · **u**ᵢ. Remember this distinction.

6. **Orthogonal complement properties**: For any subspace W, (W⊥)⊥ = W. Also, dim(W) + dim(W⊥) = n for subspaces of ℝⁿ. These results are frequently tested.

7. **QR decomposition understanding**: Know that Q has orthonormal columns and R is upper triangular with positive diagonal elements. This connects Gram-Schmidt to matrix factorization.

8. **Application-based questions**: Be prepared for questions on least squares solutions, as orthogonal bases simplify these computations significantly.
