# Kernel and Image of a Linear Transformation

## Introduction

Linear transformations are fundamental structures in linear algebra that map vectors from one vector space to another while preserving vector addition and scalar multiplication. Understanding the behavior of these transformations requires analyzing two critical subsets: the kernel (also called the null space) and the image (also called the range or column space). These concepts form the backbone of many applications in computer science, engineering, and mathematics.

The kernel of a linear transformation consists of all vectors that get mapped to the zero vector - essentially measuring how much "information" is lost during the transformation. The image, on the other hand, represents all possible output vectors that can be obtained from the transformation. Together, these two subspaces provide complete information about whether a linear transformation is invertible, one-to-one, or onto. The celebrated Rank-Nullity Theorem establishes a fundamental relationship between their dimensions, making these concepts essential for understanding the structure of linear transformations.

## Key Concepts

### 1. Linear Transformation

A function T: V → W between two vector spaces V and W is called a linear transformation if for all vectors u, v in V and scalar c:

- T(u + v) = T(u) + T(v)
- T(cu) = cT(u)

Every linear transformation can be represented by a matrix A such that T(x) = Ax, where A is an m×n matrix when T: ℝⁿ → ℝᵐ.

### 2. Kernel (Null Space)

The kernel (or null space) of a linear transformation T: V → W is defined as:

**Ker(T) = {v ∈ V : T(v) = 0}**

The kernel is always a subspace of the domain V. It contains all vectors that "collapse" to the zero vector under the transformation. In matrix terms, for T(x) = Ax, the kernel is the set of all solutions to Ax = 0, also called the null space of matrix A, denoted as N(A) or Null(A).

**Properties of Kernel:**

- Ker(T) always contains the zero vector (since T(0) = 0)
- If u, v ∈ Ker(T), then u + v ∈ Ker(T)
- If v ∈ Ker(T), then cv ∈ Ker(T) for any scalar c
- T is one-to-one (injective) if and only if Ker(T) = {0}

### 3. Image (Range)

The image (or range) of a linear transformation T: V → W is defined as:

**Im(T) = {w ∈ W : w = T(v) for some v ∈ V}**

The image is always a subspace of the codomain W. It represents all possible outputs of the transformation. In matrix terms, for T(x) = Ax, the image is the column space of A, denoted as Col(A), consisting of all linear combinations of the columns of A.

**Properties of Image:**

- Im(T) always contains the zero vector (since T(0) = 0)
- If w₁, w₂ ∈ Im(T), then w₁ + w₂ ∈ Im(T)
- If w ∈ Im(T), then cw ∈ Im(T) for any scalar c
- T is onto (surjective) if and only if Im(T) = W

### 4. Rank-Nullity Theorem

The Rank-Nullity Theorem is a fundamental result that relates the dimensions of the kernel and image:

**dim(Ker(T)) + dim(Im(T)) = dim(V)**

Where:

- dim(Ker(T)) is called the **nullity** of T
- dim(Im(T)) is called the **rank** of T

For an m×n matrix A:

- Rank(A) = dim(Col(A)) = dimension of the column space
- Nullity(A) = dim(Null(A)) = dimension of the null space
- Rank(A) + Nullity(A) = n (number of columns)

### 5. One-to-One and Onto Transformations

**One-to-One (Injective):** A linear transformation T: V → W is one-to-one if different inputs produce different outputs, i.e., T(u) = T(v) implies u = v. This is equivalent to Ker(T) = {0}.

**Onto (Surjective):** A linear transformation T: V → W is onto if every element in W is the image of some element in V, i.e., Im(T) = W.

**Key Relationships:**

- T is one-to-one ⇔ Ker(T) = {0} ⇔ Nullity(T) = 0
- T is onto ⇔ Im(T) = W ⇔ Rank(T) = dim(W)
- For T: ℝⁿ → ℝᵐ, if Rank(T) = n, then T is one-to-one
- For T: ℝⁿ → ℝᵐ, if Rank(T) = m, then T is onto

### 6. Finding Kernel and Image from Matrix

**To find Kernel of T(x) = Ax:**

1. Solve the homogeneous system Ax = 0
2. Express the solution in parametric vector form
3. The set of all parameter vectors forms the kernel

**To find Image of T(x) = Ax:**

1. Find the column space of A
2. Reduce A to row echelon form
3. The pivot columns in the original matrix span the image

## Examples

### Example 1: Finding Kernel and Image

Let T: ℝ³ → ℝ² be defined by T(x, y, z) = (x + y, y + z). Find Ker(T) and Im(T).

**Solution:**

The transformation can be written as T(x) = Ax where A = [[1, 1, 0], [0, 1, 1]]

**Finding Kernel (Null Space):**
Solve Ax = 0:

```
[1 1 0 | 0]
[0 1 1 | 0]
```

Row 2: y + z = 0 ⇒ y = -z
Row 1: x + y = 0 ⇒ x = -y = z

Let z = t (free variable):

- x = t, y = -t, z = t
- Solution: (t, -t, t) = t(1, -1, 1)

Therefore, Ker(T) = {t(1, -1, 1) : t ∈ ℝ} = span{(1, -1, 1)}

**Finding Image (Column Space):**
The columns of A are: c₁ = (1, 0), c₂ = (1, 1), c₃ = (0, 1)

These vectors in ℝ² span the image. Are they linearly independent?

- (1, 0) and (1, 1) are linearly independent
- (0, 1) = (1, 1) - (1, 0)

So Im(T) = span{(1, 0), (1, 1)} = ℝ² (since two linearly independent vectors span ℝ²)

**Verification with Rank-Nullity:**

- dim(Ker(T)) = 1 (nullity = 1)
- dim(Im(T)) = 2 (rank = 2)
- dim(V) = 3
- 1 + 2 = 3 ✓

### Example 2: Determining if Transformation is One-to-One or Onto

Let T: ℝ⁴ → ℝ³ be defined by T(x) = Ax where A = [[1, 2, 0, 1], [1, 1, 1, 0], [2, 3, 1, 1]]. Determine if T is one-to-one and/or onto.

**Solution:**

First, find the rank of A by row reduction:

```
[1 2 0 1]
[1 1 1 0]
[2 3 1 1]
```

R₂ → R₂ - R₁: [0, -1, 1, -1]
R₃ → R₃ - 2R₁: [0, -1, 1, -1]

R₂ → -R₂: [0, 1, -1, 1]
R₃ → R₃ - R₂: [0, 0, 0, 0]

The rank is 2 (two pivots in rows 1 and 2).

**Analysis:**

- dim(V) = 4
- Rank(T) = 2
- Nullity(T) = 4 - 2 = 2

Since nullity > 0, Ker(T) ≠ {0}, so T is **not one-to-one**.

For T: ℝ⁴ → ℝ³, to be onto, we need rank = 3 (dimension of codomain). Here rank = 2 < 3, so T is **not onto**.

### Example 3: Using Rank-Nullity Theorem

If T: ℝ⁵ → ℝ³ has nullity 2, find the rank of T and determine if T can be one-to-one.

**Solution:**

Given:

- dim(V) = 5
- Nullity = dim(Ker(T)) = 2

By Rank-Nullity Theorem:
Rank(T) = dim(V) - Nullity = 5 - 2 = 3

Since rank = 3 equals the dimension of the codomain ℝ³, T is **onto** (but not one-to-one).

For T to be one-to-one, we need nullity = 0. Here nullity = 2 > 0, so T cannot be one-to-one.

## Exam Tips

1. **Remember the Rank-Nullity Theorem**: dim(Ker) + dim(Im) = dim(domain) is the most important formula. Almost every problem involving kernel and image can be solved using this.

2. **Kernel = {0} means One-to-One**: If you're asked whether T is injective, find the kernel. If it contains only the zero vector, T is one-to-one.

3. **Image = Codomain means Onto**: To check surjectivity, compare the dimension of the image with the dimension of the codomain.

4. **Finding Kernel**: Always solve Ax = 0. Write the solution in parametric form to express the kernel as a span of basis vectors.

5. **Finding Image**: For matrix transformations, the image is spanned by the columns of the matrix. Find the pivot columns after row reduction to get a basis.

6. **Quick Rank Check**: For T: ℝⁿ → ℝᵐ, if rank = n, T is one-to-one; if rank = m, T is onto.

7. **Understand the Geometry**: The kernel represents vectors that get "crushed" to zero. A larger kernel means more information is lost in the transformation.

8. **Practice Matrix Reduction**: Become proficient in finding rank and nullity through Gaussian elimination as this is the most common examination approach.
