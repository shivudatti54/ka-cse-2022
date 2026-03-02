# Linear Mappings (Linear Transformations)

## Table of Contents

- [Linear Mappings (Linear Transformations)](#linear-mappings-linear-transformations)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Linear Mapping](#definition-of-linear-mapping)
  - [Zero Transformation and Identity Transformation](#zero-transformation-and-identity-transformation)
  - [Kernel (Null Space)](#kernel-null-space)
  - [Range (Image)](#range-image)
  - [Rank-Nullity Theorem](#rank-nullity-theorem)
  - [Matrix Representation of Linear Transformations](#matrix-representation-of-linear-transformations)
  - [Types of Linear Transformations in R²](#types-of-linear-transformations-in-r)
  - [Composition of Linear Transformations](#composition-of-linear-transformations)
  - [One-to-One and Onto Transformations](#one-to-one-and-onto-transformations)
- [Examples](#examples)
  - [Example 1: Verifying Linearity](#example-1-verifying-linearity)
  - [Example 2: Finding Kernel and Range](#example-2-finding-kernel-and-range)
  - [Example 3: Matrix Representation](#example-3-matrix-representation)
- [Exam Tips](#exam-tips)

## Introduction

A linear mapping, also known as a linear transformation, is one of the most fundamental concepts in linear algebra. It serves as a bridge between abstract vector spaces and the concrete world of matrices and computations. In simple terms, a linear mapping is a function that preserves the operations of vector addition and scalar multiplication between two vector spaces.

The importance of linear mappings in computer science and engineering cannot be overstated. In computer graphics, linear transformations are used for rotation, scaling, and reflection of objects. In machine learning and data science, linear transformations form the foundation of dimensionality reduction techniques like Principal Component Analysis (PCA). In solving systems of linear equations, understanding the behavior of linear transformations helps determine whether solutions exist and are unique. For students pursuing computer science, linear transformations are essential for understanding neural networks, image processing, and various algorithms that rely on linear algebraic operations.

This topic builds directly on the concepts of vector spaces and subspaces studied in Module 1. We will explore the definition, properties, kernel and range, rank-nullity theorem, and matrix representation of linear transformations, along with practical examples that frequently appear in university examinations.

## Key Concepts

### Definition of Linear Mapping

A function T: V → W between two vector spaces V and W over a field F is called a linear transformation (or linear mapping) if for all u, v ∈ V and all scalars c ∈ F:

1. **Additivity**: T(u + v) = T(u) + T(v)
2. **Homogeneity**: T(cu) = cT(u)

These two properties can be combined into a single condition: T(cu + dv) = cT(u) + dT(v) for all u, v ∈ V and all scalars c, d ∈ F.

The vector space V is called the domain, and W is called the codomain of the transformation.

### Zero Transformation and Identity Transformation

- **Zero Transformation**: The transformation T: V → W defined by T(v) = 0 for all v ∈ V is linear. It maps every vector to the zero vector.
- **Identity Transformation**: The transformation I: V → V defined by I(v) = v for all v ∈ V is linear. It maps each vector to itself.

### Kernel (Null Space)

The kernel (or null space) of a linear transformation T: V → W is the set of all vectors in V that map to the zero vector in W:

Ker(T) = {v ∈ V : T(v) = 0}

The kernel is always a subspace of V. It represents the "information lost" during the transformation.

### Range (Image)

The range (or image) of a linear transformation T: V → W is the set of all vectors in W that are obtained by applying T to vectors in V:

Range(T) = {T(v) : v ∈ V}

The range is always a subspace of W. It represents the "result space" of the transformation.

### Rank-Nullity Theorem

One of the most important theorems in linear algebra relates the dimensions of the kernel and range:

**Rank-Nullity Theorem**: For a linear transformation T: V → W where V is finite-dimensional:

dim(Ker(T)) + dim(Range(T)) = dim(V)

Here, dim(Ker(T)) is called the **nullity** of T, and dim(Range(T)) is called the **rank** of T.

### Matrix Representation of Linear Transformations

If V and W are finite-dimensional vector spaces with ordered bases B*V and B_W respectively, every linear transformation T: V → W can be represented by a matrix [T]*{B_W}^{B_V}. To find this matrix:

1. Apply T to each basis vector of V
2. Express each resulting vector in terms of the basis of W
3. The columns of the matrix are the coordinates of these results

For standard bases in Fⁿ and Fᵐ, the matrix representation is particularly simple: if T(x) = Ax for some m×n matrix A, then A is the matrix representation of T.

### Types of Linear Transformations in R²

Several important linear transformations in the plane include:

- **Rotation**: T(x, y) = (x cos θ - y sin θ, x sin θ + y cos θ) rotates vectors by angle θ
- **Scaling**: T(x, y) = (ax, by) scales in x-direction by a and y-direction by b
- **Reflection**: T(x, y) = (x, -y) reflects across the x-axis; T(x, y) = (-x, y) reflects across the y-axis
- **Projection**: T(x, y) = (x, 0) projects onto the x-axis; T(x, y) = (0, y) projects onto the y-axis
- **Shear**: T(x, y) = (x + ky, y) is a horizontal shear

### Composition of Linear Transformations

If T: U → V and S: V → W are linear transformations, then the composition S ∘ T: U → W defined by (S ∘ T)(u) = S(T(u)) is also linear. The matrix representation satisfies: [S ∘ T] = [S][T].

### One-to-One and Onto Transformations

- T is **one-to-one** (injective) if T(u) = T(v) implies u = v, or equivalently, Ker(T) = {0}
- T is **onto** (surjective) if Range(T) = W
- T is **bijective** if it is both one-to-one and onto

## Examples

### Example 1: Verifying Linearity

Determine whether the transformation T: R² → R² defined by T(x, y) = (x + 1, y) is linear.

**Solution:**

To check if T is linear, we must verify additivity and homogeneity.

Let u = (x₁, y₁) and v = (x₂, y₂). Then:

**Additivity Check:**
T(u + v) = T(x₁ + x₂, y₁ + y₂) = (x₁ + x₂ + 1, y₁ + y₂)
T(u) + T(v) = (x₁ + 1, y₁) + (x₂ + 1, y₂) = (x₁ + x₂ + 2, y₁ + y₂)

Since T(u + v) ≠ T(u) + T(v), the additivity property fails.

**Conclusion:** T is NOT a linear transformation. The extra "+1" breaks the linearity. Only transformations that pass through the origin (map zero to zero) can be linear.

### Example 2: Finding Kernel and Range

Let T: R³ → R² be defined by T(x, y, z) = (x + y, y + z). Find the kernel and range of T.

**Solution:**

**Finding Kernel(T):**
We need all (x, y, z) such that T(x, y, z) = (0, 0):
x + y = 0 → x = -y
y + z = 0 → z = -y

So, Kernel(T) = {(-y, y, -y) : y ∈ R} = {y(-1, 1, -1) : y ∈ R}
The kernel is spanned by (-1, 1, -1), so dim(Ker(T)) = 1.

**Finding Range(T):**
Let T(x, y, z) = (x + y, y + z) = x(1, 0) + y(1, 1) + z(0, 1)

The vectors (1, 0), (1, 1), and (0, 1) span the range. These are linearly dependent (since (1, 1) = (1, 0) + (0, 1)), so the range is spanned by (1, 0) and (0, 1), which form the standard basis of R².

Therefore, Range(T) = R², and dim(Range(T)) = 2.

**Verification using Rank-Nullity:**
dim(V) = 3
dim(Ker(T)) + dim(Range(T)) = 1 + 2 = 3 = dim(V) ✓

### Example 3: Matrix Representation

Find the matrix representation of the linear transformation T: R³ → R² defined by T(x, y, z) = (2x + y - z, x - 3y) with respect to the standard bases.

**Solution:**

For the standard bases, we apply T to each standard basis vector of R³ and write the results as columns:

T(1, 0, 0) = (2, 1) → Column 1 = [2, 1]ᵀ
T(0, 1, 0) = (1, -3) → Column 2 = [1, -3]ᵀ
T(0, 0, 1) = (-1, 0) → Column 3 = [-1, 0]ᵀ

Therefore, the matrix representation is:
A = [[2, 1, -1], [1, -3, 0]]

We can verify: A[x, y, z]ᵀ = [2x + y - z, x - 3y]ᵀ, which matches T(x, y, z).

## Exam Tips

1. **Always verify the two properties**: When asked to show a transformation is linear, explicitly verify additivity T(u+v) = T(u) + T(v) and homogeneity T(cv) = cT(v).

2. **Check if T(0) = 0**: A necessary condition for linearity is that the zero vector maps to zero. If T(0) ≠ 0, it's definitely not linear—this is a quick elimination technique.

3. **Kernel is a subspace**: Remember that Kernel(T) is always a subspace of the domain, and Range(T) is always a subspace of the codomain.

4. **Rank-Nullity is examinable**: The theorem dim(Ker(T)) + dim(Range(T)) = dim(V) frequently appears in exams. Know how to apply it to find missing dimensions.

5. **Matrix of transformation**: For standard bases, simply apply T to each basis vector and collect the results as columns—the resulting matrix is your answer.

6. **Types of transformations**: Be able to identify and give examples of rotation, scaling, reflection, projection, and shear transformations in R².

7. **One-to-one test**: T is one-to-one if and only if Ker(T) = {0}. Use this to verify injectivity quickly.
