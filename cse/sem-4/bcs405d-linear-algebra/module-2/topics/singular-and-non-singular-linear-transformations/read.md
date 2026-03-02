# Singular and Non-Singular Linear Transformations

## Introduction

Linear transformations form one of the most fundamental concepts in linear algebra, serving as the bridge between abstract vector spaces and practical applications in engineering, computer science, and physics. A linear transformation is a mapping between two vector spaces that preserves the operations of vector addition and scalar multiplication. Understanding whether a linear transformation is singular or non-singular is crucial because it determines whether the transformation can be inverted and what properties the transformation possesses.

In the context of the university's Linear Algebra course (BCS405D), this topic holds significant weight as it appears frequently in examinations. A singular linear transformation (also called degenerate or non-invertible) maps multiple vectors to the same output, causing a "loss of information." Conversely, a non-singular linear transformation (also called invertible or non-degenerate) preserves the distinctness of vectors and can be reversed. This distinction has profound implications in solving systems of linear equations, computer graphics, and engineering applications such as signal processing and control systems.

This module builds upon the concepts of vector spaces, bases, and matrices studied in Module 1. We will explore the criteria that determine whether a linear transformation is singular or non-singular, examine the relationship with rank and nullity, and develop problem-solving techniques essential for university examinations.

## Key Concepts

### 1. Definition of Linear Transformation

A function T: V → W between two vector spaces V and W is called a linear transformation if for all u, v ∈ V and scalar α ∈ F:

- T(u + v) = T(u) + T(v) [Additivity]
- T(αv) = αT(v) [Homogeneity]

The vector space V is called the domain, and W is called the codomain.

### 2. Singular Linear Transformation

A linear transformation T: V → W is said to be **singular** (or degenerate/non-invertible) if it is not one-to-one. This means there exist distinct vectors u, v ∈ V such that T(u) = T(v) but u ≠ v. Geometrically, singular transformations "collapse" the domain onto a lower-dimensional subspace of the codomain.

**Key Characteristics of Singular Transformations:**

- The kernel (null space) of T contains non-zero vectors: ker(T) ≠ {0}
- The rank of T is less than the dimension of the domain
- T cannot be inverted; no inverse transformation exists
- Determinant of the matrix representation equals zero

### 3. Non-Singular Linear Transformation

A linear transformation T: V → W is said to be **non-singular** (or invertible/non-degenerate) if it is one-to-one. This means T(u) = T(v) implies u = v for all u, v ∈ V. Non-singular transformations preserve the dimensional structure of the vector space.

**Key Characteristics of Non-Singular Transformations:**

- The kernel contains only the zero vector: ker(T) = {0}
- The rank of T equals the dimension of the domain (for finite-dimensional spaces)
- An inverse transformation T⁻¹ exists such that T⁻¹(T(v)) = v for all v ∈ V
- Determinant of the matrix representation is non-zero

### 4. Rank and Nullity Theorem (Fundamental Theorem of Linear Transformations)

For a linear transformation T: V → W where V is finite-dimensional:

**Rank(T) + Nullity(T) = dim(V)**

Where:

- Rank(T) = dim(Range(T)) = dimension of the image
- Nullity(T) = dim(Ker(T)) = dimension of the kernel

This theorem is extremely important for university examinations and is used to determine whether a transformation is singular or non-singular.

### 5. One-to-One and Onto Properties

**One-to-One (Injective):** T is one-to-one if each element of the range has a unique pre-image. For linear transformations, this is equivalent to ker(T) = {0}.

**Onto (Surjective):** T is onto if every element of the codomain has at least one pre-image, i.e., Range(T) = W.

For linear transformations between vector spaces of equal finite dimension:

- T is one-to-one ⇔ T is onto ⇔ T is non-singular

### 6. Matrix Representation and Determinant

If T: ℝⁿ → ℝⁿ is a linear transformation represented by an n×n matrix A, then:

- T is non-singular ⇔ A is invertible ⇔ det(A) ≠ 0
- T is singular ⇔ A is singular ⇔ det(A) = 0

### 7. Inverse Linear Transformation

If T: V → W is non-singular, then T⁻¹: W → V exists and is also a linear transformation. The matrix representation of T⁻¹ is A⁻¹, the inverse matrix of A.

Properties:

- (T⁻¹)⁻¹ = T
- (ST)⁻¹ = T⁻¹S⁻¹ (when S and T are non-singular)

## Examples

### Example 1: Identifying a Singular Transformation

Consider T: ℝ³ → ℝ³ defined by T(x, y, z) = (x + y, y + z, x + y + z).

**Solution:**

Step 1: Find the kernel (null space)
T(x, y, z) = (0, 0, 0) gives:
x + y = 0 → x = -y
y + z = 0 → z = -y
x + y + z = 0 → substituting: (-y) + y + (-y) = -y = 0 → y = 0

Therefore, x = 0, y = 0, z = 0. The kernel appears to be {0}.

Step 2: Find the matrix representation
A = [[1, 1, 0], [0, 1, 1], [1, 1, 1]]

Step 3: Calculate the determinant
det(A) = 1(1×1 - 1×1) - 1(0×1 - 1×1) + 0(0×1 - 1×1)
= 1(1-1) - 1(0-1) + 0
= 0 - 1(-1) + 0
= 1 ≠ 0

Wait, let me recalculate using proper expansion:
det(A) = 1×(1×1 - 1×1) - 1×(0×1 - 1×1) + 0×(0×1 - 1×1)
= 1×(1-1) - 1×(0-1) + 0
= 0 + 1 + 0 = 1 ≠ 0

Since det(A) ≠ 0, this transformation is **non-singular**.

### Example 2: Identifying a Singular Transformation

Consider T: ℝ³ → ℝ³ defined by T(x, y, z) = (x + y, x + y, x + y).

**Solution:**

Step 1: Find the kernel
T(x, y, z) = (0, 0, 0) gives x + y = 0, so y = -x.
The kernel contains all vectors of the form (x, -x, z) where x, z ∈ ℝ.
Since kernel contains non-zero vectors, T is singular.

Step 2: Verify using matrix approach
A = [[1, 1, 0], [1, 1, 0], [1, 1, 0]]

det(A) = 1×(1×0 - 0×1) - 1×(1×0 - 0×1) + 0 = 0 - 0 + 0 = 0

Since det(A) = 0, T is **singular**.

Step 3: Find rank and nullity
Rank(A) = 1 (only one linearly independent row)
Nullity = 3 - 1 = 2 (consistent with rank-nullity theorem)

### Example 3: Verifying Non-Singularity Using Rank

Consider T: ℝ² → ℝ³ defined by T(x, y) = (x, x+y, 2x-y).

**Solution:**

Step 1: Represent T as a matrix (3×2 matrix since domain is ℝ², codomain is ℝ³)
A = [[1, 0], [1, 1], [2, -1]]

Step 2: Find the rank
The matrix has 2 columns, so maximum possible rank is 2.
Check if columns are linearly independent:
c₁ = (1, 1, 2), c₂ = (0, 1, -1)
These are linearly independent (not scalar multiples), so rank = 2.

Step 3: Determine singularity
Since rank(A) = 2 = dim(domain), the transformation is **non-singular**.

Note: For T: ℝⁿ → ℝᵐ where m > n, T can still be non-singular (one-to-one) if rank = n.

## Exam Tips

1. **Quick Test for Non-Singularity:** For a linear transformation T: ℝⁿ → ℝⁿ, calculate det(A). If det(A) ≠ 0, T is non-singular; if det(A) = 0, T is singular.

2. **Kernel Test:** To check if T is non-singular, solve T(v) = 0. If the only solution is v = 0, then T is non-singular (one-to-one).

3. **Rank-Nullity is Essential:** Always apply the Rank-Nullity theorem: Rank + Nullity = Dimension of Domain. This helps verify your answers.

4. **Dimension Equality:** Remember: For T: V → W where dim(V) = dim(W) = n, T is one-to-one if and only if T is onto if and only if T is non-singular.

5. **Matrix Inverse:** If asked to find the inverse of a linear transformation, find the inverse matrix A⁻¹ and use it to compute T⁻¹(v).

6. **Common Singular Transformations:** Projections (onto a subspace), contractions, and any transformation that "collapses" dimensions are typically singular.

7. **Practice Previous Year Questions:** university frequently asks to determine whether given transformations are singular or non-singular using both kernel and determinant methods.

8. **Understanding the Question:** When a transformation maps between different spaces (like ℝ³ → ℝ²), "non-singular" typically means one-to-one (injective), not necessarily onto.
