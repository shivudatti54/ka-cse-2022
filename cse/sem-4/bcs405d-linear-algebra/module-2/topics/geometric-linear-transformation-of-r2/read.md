# Geometric Linear Transformations of R²

## Introduction

Linear transformations form a fundamental concept in linear algebra with extensive applications in computer graphics, engineering, physics, and data science. A linear transformation is a mapping between vector spaces that preserves vector addition and scalar multiplication. When we restrict our attention to the Euclidean plane R² (the 2-dimensional real coordinate space), geometric linear transformations provide an intuitive way to understand how vectors are transformed through operations like rotation, scaling, shearing, reflection, and projection.

The study of geometric transformations in R² is particularly valuable because visual representations help build strong intuitions about abstract algebraic concepts. Each linear transformation in R² can be represented by a 2×2 matrix, and applying the transformation to any vector is simply matrix multiplication. This beautiful connection between geometry and algebra is central to understanding linear algebra and its applications.

In the context of the university's BCS405D Linear Algebra course, this topic appears in Module 2 and carries significant weightage in examinations. Understanding geometric transformations not only helps solve theoretical problems but also provides the foundation for more advanced topics like eigenvalues, eigenvectors, and diagonalization.

## Key Concepts

### Definition of Linear Transformation

A function T: R² → R² is called a linear transformation if it satisfies two properties for all vectors u, v in R² and all scalars c:

1. **Additivity**: T(u + v) = T(u) + T(v)
2. **Homogeneity**: T(cu) = cT(u)

An equivalent and often more useful definition states that T is linear if and only if T(au + bv) = aT(u) + bT(v) for all scalars a, b and vectors u, v.

A fundamental property of all linear transformations is that they map the origin to itself: T(0) = 0. This is immediately evident from homogeneity with c = 0.

### Standard Matrix Representation

Every linear transformation T: R² → R² can be represented by a unique 2×2 matrix A such that T(v) = Av for every vector v in R². To find this matrix, we apply T to the standard basis vectors e₁ = (1, 0) and e₂ = (0, 1):

- The first column of A is T(e₁)
- The second column of A is T(e₂)

If T(e₁) = (a, c) and T(e₂) = (b, d), then the matrix representation is A = [[a, b], [c, d]].

### Types of Geometric Transformations

**1. Rotation**

A rotation by an angle θ (counterclockwise positive) about the origin is represented by the matrix:

R(θ) = [[cos θ, -sin θ], [sin θ, cos θ]]

The determinant of this matrix is cos²θ + sin²θ = 1, indicating that rotation preserves area.

**2. Scaling**

A scaling transformation with scale factors a in the x-direction and b in the y-direction is represented by:

S(a, b) = [[a, 0], [0, b]]

- If a = b = k, it's a uniform scaling (dilation if k > 1, contraction if 0 < k < 1)
- If a = 1 and b = -1, it's a reflection across the x-axis

**3. Shear**

A horizontal shear (parallel to x-axis) with shear factor k is represented by:

Hₓ(k) = [[1, k], [0, 1]]

A vertical shear (parallel to y-axis) is:

Hᵧ(k) = [[1, 0], [k, 1]]

Shear transformations preserve area (determinant = 1) but distort angles.

**4. Reflection**

- Reflection across x-axis: [[1, 0], [0, -1]]
- Reflection across y-axis: [[-1, 0], [0, 1]]
- Reflection across the line y = x: [[0, 1], [1, 0]]
- Reflection across the line y = -x: [[0, -1], [-1, 0]]

**5. Projection**

Projection onto the x-axis: [[1, 0], [0, 0]]
Projection onto the y-axis: [[0, 0], [0, 1]]

Projections are linear transformations that map vectors onto subspaces. The projection matrix is idempotent: P² = P.

### Composition of Transformations

When two linear transformations are applied sequentially, the resulting transformation is represented by the product of their matrices. If T₁ has matrix A and T₂ has matrix B, then the composition T₁ ∘ T₂ (first apply T₂, then T₁) has matrix BA (note the order: rightmost matrix applies first).

### Inverse Transformations

A linear transformation is invertible if and only if its matrix representation is invertible (non-zero determinant). The inverse transformation T⁻¹ is represented by the inverse matrix A⁻¹, satisfying AA⁻¹ = A⁻¹A = I.

## Examples

### Example 1: Finding the Matrix of a Transformation

**Problem**: Find the matrix representation of the linear transformation T: R² → R² that rotates every vector by 45° counterclockwise and then reflects it across the x-axis.

**Solution**:

Step 1: Write the rotation matrix for θ = 45° = π/4
R(45°) = [[cos 45°, -sin 45°], [sin 45°, cos 45°]] = [[√2/2, -√2/2], [√2/2, √2/2]]

Step 2: Write the reflection matrix across x-axis
Fₓ = [[1, 0], [0, -1]]

Step 3: Composition (first rotate, then reflect)
The combined transformation matrix is Fₓ × R(45°)

= [[1, 0], [0, -1]] × [[√2/2, -√2/2], [√2/2, √2/2]]

= [[1 × √2/2 + 0 × √2/2, 1 × (-√2/2) + 0 × √2/2], [0 × √2/2 + (-1) × √2/2, 0 × (-√2/2) + (-1) × √2/2]]

= [[√2/2, -√2/2], [-√2/2, -√2/2]]

Therefore, T(v) = [[√2/2, -√2/2], [-√2/2, -√2/2]]v

### Example 2: Applying Transformation to a Vector

**Problem**: Find the image of the vector v = (2, 3) under the shear transformation with shear factor 2 in the x-direction.

**Solution**:

Step 1: Write the shear matrix
Hₓ(2) = [[1, 2], [0, 1]]

Step 2: Multiply the matrix by the vector
Hₓ(2) × (2, 3)ᵀ = [[1, 2], [0, 1]] × [[2], [3]] = [[1×2 + 2×3], [0×2 + 1×3]] = [[2 + 6], [3]] = [[8], [3]]

The image is the vector (8, 3).

Geometrically, the x-coordinate is shifted by 2 times the y-coordinate, which gives 2 × 3 = 6, resulting in 2 + 6 = 8.

### Example 3: Verifying Linearity and Finding Inverse

**Problem**: Verify that T(x, y) = (3x + y, x - 2y) is a linear transformation and find its inverse transformation if it exists.

**Solution**:

**Part 1: Verify Linearity**

Let u = (x₁, y₁), v = (x₂, y₂)

T(u + v) = T(x₁ + x₂, y₁ + y₂) = (3(x₁ + x₂) + (y₁ + y₂), (x₁ + x₂) - 2(y₁ + y₂))
= (3x₁ + 3x₂ + y₁ + y₂, x₁ + x₂ - 2y₁ - 2y₂)
= (3x₁ + y₁, x₁ - 2y₁) + (3x₂ + y₂, x₂ - 2y₂)
= T(u) + T(v) ✓

T(cu) = T(cx, cy) = (3cx + cy, cx - 2cy) = c(3x + y, x - 2y) = cT(u) ✓

Therefore, T is linear.

**Part 2: Find the matrix and inverse**

The matrix representation is A = [[3, 1], [1, -2]]

Find determinant: det(A) = (3)(-2) - (1)(1) = -6 - 1 = -7 ≠ 0

Since determinant is non-zero, inverse exists. Using formula for 2×2 inverse:
A⁻¹ = (1/det) × [[d, -b], [-c, a]] = (1/-7) × [[-2, -1], [-1, 3]]
= [[2/7, 1/7], [1/7, -3/7]]

Therefore, T⁻¹(x, y) = ((2x + y)/7, (x - 3y)/7)

## Exam Tips

1. **Remember the matrix forms**: Memorize standard transformation matrices for rotation, scaling, shear, reflection, and projection. These frequently appear in exam questions.

2. **Verify linearity quickly**: Check if T(0) = 0. If not, it's not linear. This simple test can save time in examination.

3. **Composition order matters**: Remember that matrix multiplication is not commutative. The rightmost matrix in the product applies first to the vector.

4. **Determinant indicates area change**: The absolute value of the determinant tells you how the area of regions changes. |det| = 1 means area is preserved.

5. **Inverse exists when det ≠ 0**: Always check the determinant first. If det = 0, the transformation is not invertible.

6. **Standard basis trick**: To find the matrix of any linear transformation, apply it to e₁ = (1, 0) and e₂ = (0, 1). The results form the columns of the matrix.

7. **Geometric interpretation helps**: When stuck, visualize what the transformation does to the unit square. This often clarifies the approach.

8. **Projection and reflection are idempotent**: For projections P and reflections R, we have P² = P and R² = I. Use this to verify your answers.
