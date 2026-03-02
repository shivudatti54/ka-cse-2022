# Length and Orthogonality

## Introduction

Length and orthogonality are fundamental concepts in linear algebra that form the backbone of many advanced topics in mathematics, physics, and computer science. These concepts extend the geometric intuition of length and perpendicularity from two and three-dimensional spaces to higher-dimensional vector spaces. In the context of the university's Linear Algebra course, understanding these concepts is crucial for solving problems related to vector spaces, inner product spaces, and orthogonal projections.

The concept of length, also known as the norm of a vector, provides a way to measure the "size" or "magnitude" of a vector. This is essential in various applications such as data normalization, machine learning algorithms, and solving systems of linear equations. Orthogonality, on the other hand, generalizes the notion of perpendicularity and plays a vital role in optimization problems, least squares approximations, and Fourier analysis. Together, these concepts enable us to work with geometrically meaningful structures in abstract vector spaces.

## Key Concepts

### 1. Inner Product and Dot Product

The **inner product** is a binary operation that takes two vectors and returns a scalar, satisfying specific axioms. For vectors in ℝⁿ, the standard inner product is the **dot product**, defined as:

For **u** = (u₁, u₂, ..., uₙ) and **v** = (v₁, v₂, ..., vₙ):
**u** · **v** = u₁v₁ + u₂v₂ + ... + uₙvₙ

The inner product satisfies the following properties:

- **Commutativity**: **u** · **v** = **v** · **u**
- **Distributivity**: **u** · (**v** + **w**) = **u** · **v** + **u** · **w**
- **Scalar multiplication**: (c**u**) · **v** = c(**u** · **v**)
- **Positivity**: **v** · **v** ≥ 0, and **v** · **v** = 0 if and only if **v** = **0**

### 2. Length (Norm) of a Vector

The **length** or **norm** of a vector **v** in ℝⁿ is defined as:

‖**v**‖ = √(**v** · **v**) = √(v₁² + v₂² + ... + vₙ²)

**Properties of Norm:**

- **Positivity**: ‖**v**‖ ≥ 0 for all **v**, and ‖**v**‖ = 0 if and only if **v** = **0**
- **Absolute homogeneity**: ‖c**v**‖ = |c| ‖**v**‖ for any scalar c
- **Triangle inequality**: ‖**u** + **v**‖ ≤ ‖**u**‖ + ‖**v**‖

A **unit vector** is a vector with length 1. To normalize a vector **v** (≠ **0**), we compute **v**/‖**v**‖.

### 3. Distance Between Vectors

The **distance** between two vectors **u** and **v** in ℝⁿ is defined as:

d(**u**, **v**) = ‖**u** - **v**‖

This definition satisfies the distance axioms:

- d(**u**, **v**) ≥ 0
- d(**u**, **v**) = 0 if and only if **u** = **v**
- Symmetry: d(**u**, **v**) = d(**v**, **u**)
- Triangle inequality: d(**u**, **w**) ≤ d(**u**, **v**) + d(**v**, **w**)

### 4. Angle Between Vectors

The **angle θ** between two non-zero vectors **u** and **v** in ℝⁿ is given by:

cos θ = (**u** · **v**) / (‖**u**‖ ‖**v**‖), where 0 ≤ θ ≤ π

### 5. Orthogonal Vectors

Two vectors **u** and **v** are **orthogonal** (perpendicular) if their dot product is zero:

**u** · **v** = 0

We denote orthogonal vectors as **u** ⊥ **v**. The zero vector is orthogonal to every vector.

**Pythagorean Theorem for Vectors**: If **u** and **v** are orthogonal, then:
‖**u** + **v**‖² = ‖**u**‖² + ‖**v**‖²

### 6. Cauchy-Schwarz Inequality

For any vectors **u** and **v** in ℝⁿ:
|**u** · **v**| ≤ ‖**u**‖ ‖**v**‖

Equality holds if and only if **u** and **v** are linearly dependent (one is a scalar multiple of the other).

### 7. Orthogonal Complements

If **v** is orthogonal to every vector in a subspace W, then **v** is in the **orthogonal complement** of W, denoted W⊥.

Properties of orthogonal complements:

- W⊥ is a subspace of ℝⁿ
- (W⊥)⊥ = W
- dim(W) + dim(W⊥) = n

### 8. Orthogonal Sets and Bases

A set of non-zero vectors {**v₁**, **v₂**, ..., **vₖ**} is **orthogonal** if every pair of distinct vectors is orthogonal:
**vᵢ** · **vⱼ** = 0 for i ≠ j

If additionally each vector has unit length (‖**vᵢ**‖ = 1), the set is **orthonormal**.

**Key Theorem**: If {**v₁**, **v₂**, ..., **vₖ**} is an orthogonal set of non-zero vectors, then these vectors are linearly independent.

An **orthogonal basis** is a basis that forms an orthogonal set. An **orthonormal basis** is an orthogonal basis where all vectors are unit vectors.

### 9. Gram-Schmidt Orthogonalization Process

The Gram-Schmidt process converts any set of linearly independent vectors into an orthogonal (or orthonormal) set. Given linearly independent vectors {**x₁**, **x₂**, ..., **xₙ**}:

**Step 1**: Let **v₁** = **x₁**

**Step 2**: **v₂** = **x₂** - proj\_{**v₁**}(**x₂**) = **x₂** - ((**x₂** · **v₁**)/(**v₁** · **v₁**))**v₁**

**Step 3**: **v₃** = **x₃** - proj*{**v₁**}(**x₃**) - proj*{**v₂**}(**x₃**)

Continue this process. To get an orthonormal set, normalize each **vᵢ**:
**uᵢ** = **vᵢ**/‖**vᵢ**‖

## Examples

### Example 1: Computing Length and Distance

Given **u** = (1, -2, 3, -1) and **v** = (2, 0, -1, 4) in ℝ⁴:

**Solution:**

Length of **u**:
‖**u**‖ = √(1² + (-2)² + 3² + (-1)²) = √(1 + 4 + 9 + 1) = √15 ≈ 3.87

Length of **v**:
‖**v**‖ = √(2² + 0² + (-1)² + 4²) = √(4 + 0 + 1 + 16) = √21 ≈ 4.58

Distance between **u** and **v**:
**u** - **v** = (1-2, -2-0, 3-(-1), -1-4) = (-1, -2, 4, -5)
‖**u** - **v**‖ = √((-1)² + (-2)² + 4² + (-5)²) = √(1 + 4 + 16 + 25) = √46 ≈ 6.78

### Example 2: Verifying Orthogonality and Pythagorean Theorem

Verify that **u** = (3, 4) and **v** = (4, -3) are orthogonal, and verify the Pythagorean theorem.

**Solution:**

**u** · **v** = 3(4) + 4(-3) = 12 - 12 = 0

Since the dot product is zero, **u** ⊥ **v**.

Now verify Pythagorean theorem:
‖**u** + **v**‖² = ‖(3+4, 4+(-3))‖² = ‖(7, 1)‖² = 7² + 1² = 49 + 1 = 50

‖**u**‖² + ‖**v**‖² = (3² + 4²) + (4² + (-3)²) = (9 + 16) + (16 + 9) = 25 + 25 = 50

Thus, ‖**u** + **v**‖² = ‖**u**‖² + ‖**v**‖², confirming the Pythagorean theorem.

### Example 3: Applying Gram-Schmidt Process

Given **x₁** = (1, 1, 0) and **x₂** = (1, 0, 1) in ℝ³, find an orthogonal basis.

**Solution:**

**Step 1**: **v₁** = **x₁** = (1, 1, 0)

**Step 2**: **v₂** = **x₂** - proj\_{**v₁**}(**x₂**)

Compute projection:
**x₂** · **v₁** = 1(1) + 0(1) + 1(0) = 1
**v₁** · **v₁** = 1² + 1² + 0² = 2

proj\_{**v₁**}(**x₂**) = (1/2) **v₁** = (1/2, 1/2, 0)

**v₂** = (1, 0, 1) - (1/2, 1/2, 0) = (1 - 1/2, 0 - 1/2, 1 - 0) = (1/2, -1/2, 1)

Verify orthogonality:
**v₁** · **v₂** = 1(1/2) + 1(-1/2) + 0(1) = 1/2 - 1/2 + 0 = 0

Thus, {**v₁**, **v₂**} = {(1,1,0), (1/2,-1/2,1)} is an orthogonal set.

## Exam Tips

1. **Remember the norm formula**: ‖**v**‖ = √(**v** · **v**) is the key formula for computing vector length.

2. **Cauchy-Schwarz inequality**: |**u** · **v**| ≤ ‖**u**‖‖**v**‖ is frequently tested—memorize it along with its equality condition.

3. **Triangle inequality**: ‖**u** + **v**‖ ≤ ‖**u**‖ + ‖**v**‖ is essential for proving various properties.

4. **Orthogonality test**: Two vectors are orthogonal if and only if their dot product equals zero—this is the most direct test.

5. **Gram-Schmidt process**: Be thorough with the projection formula: proj\_{**v**}(**x**) = ((**x** · **v**)/(**v** · **v**))**v**.

6. **Unit vector normalization**: To convert any non-zero vector to a unit vector, divide by its norm: **v**/‖**v**‖.

7. **Pythagorean theorem**: Remember that ‖**u** + **v**‖² = ‖**u**‖² + ‖**v**‖² holds only when **u** ⊥ **v**.

8. **Orthogonal complement properties**: Know that W⊥ is always a subspace and dim(W) + dim(W⊥) = n for subspaces of ℝⁿ.
