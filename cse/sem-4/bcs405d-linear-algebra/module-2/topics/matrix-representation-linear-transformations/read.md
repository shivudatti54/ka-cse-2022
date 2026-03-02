# Matrix Representation of Linear Transformations

## Table of Contents

- [Matrix Representation of Linear Transformations](#matrix-representation-of-linear-transformations)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Linear Transformation](#definition-of-linear-transformation)
  - [Matrix Representation](#matrix-representation)
  - [Finding the Matrix of a Linear Transformation](#finding-the-matrix-of-a-linear-transformation)
  - [Standard Matrix Representations](#standard-matrix-representations)
  - [Composition of Linear Transformations](#composition-of-linear-transformations)
  - [Change of Basis](#change-of-basis)
- [Examples](#examples)
  - [Example 1: Finding Matrix Representation](#example-1-finding-matrix-representation)
  - [Example 2: Transformation in ℝ³](#example-2-transformation-in-)
  - [Example 3: Composition of Transformations](#example-3-composition-of-transformations)
- [Exam Tips](#exam-tips)

## Introduction

Matrix representation of linear transformations is a fundamental concept in linear algebra that bridges the abstract notion of linear transformations with concrete computational methods. A linear transformation T: V → W between vector spaces can be completely described by a matrix, once bases are chosen for both vector spaces. This representation allows us to perform computations, analyze properties, and solve problems using the well-developed theory of matrices.

The importance of this concept in computer science and engineering cannot be overstated. In computer graphics, linear transformations represent rotations, scaling, and shearing operations on images and 3D objects. In machine learning and data science, matrices represent linear models and transformations between feature spaces. In engineering applications, state transitions, control systems, and signal processing all rely on matrix representations of linear transformations. Understanding this concept is essential for any CSE student pursuing advanced courses in computer graphics, machine learning, numerical methods, or any field involving linear algebraic computations.

## Key Concepts

### Definition of Linear Transformation

A function T: V → W between two vector spaces V and W is called a linear transformation if for all vectors u, v in V and all scalars c:

- T(u + v) = T(u) + T(v) (additivity)
- T(cu) = cT(u) (homogeneity)

Equivalently, T(cu + dv) = cT(u) + dT(v) for all scalars c, d and vectors u, v.

### Matrix Representation

Let V and W be finite-dimensional vector spaces with dimensions n and m respectively. Let B_V = {v₁, v₂, ..., vₙ} be an ordered basis for V and B_W = {w₁, w₂, ..., wₘ} be an ordered basis for W.

For any linear transformation T: V → W, there exists a unique m × n matrix A such that for any vector v in V:
[T(v)]_{B_W} = A[v]_{B_V}

The columns of matrix A are the coordinate vectors of T(vᵢ) with respect to basis B*W:
A = [[T(v₁)]*{B*W} | [T(v₂)]*{B*W} | ... | [T(vₙ)]*{B_W}]

This matrix A is called the matrix representation of T with respect to bases B*V and B_W, denoted as [T]*{B_W}^{B_V} or simply [T] when bases are understood.

### Finding the Matrix of a Linear Transformation

**Step 1**: Identify the domain basis B_V and codomain basis B_W.
**Step 2**: Apply the transformation T to each basis vector of V.
**Step 3**: Express each transformed vector in terms of the codomain basis.
**Step 4**: Form the matrix using these coordinate vectors as columns.

### Standard Matrix Representations

When V = ℝⁿ and W = ℝᵐ with standard bases, the matrix representation is called the standard matrix. For T: ℝⁿ → ℝᵐ, the standard matrix A has T(eᵢ) as its i-th column, where eᵢ are the standard basis vectors.

Common transformations and their standard matrices:

- **Rotation by angle θ** (counterclockwise): [[cos θ, -sin θ], [sin θ, cos θ]]
- **Reflection across x-axis**: [[1, 0], [0, -1]]
- **Scaling by factor k**: [[k, 0], [0, k]]
- **Projection onto x-axis**: [[1, 0], [0, 0]]
- **Shear in x-direction**: [[1, k], [0, 1]]

### Composition of Linear Transformations

If S: U → V and T: V → W are linear transformations with matrices A and B respectively (with respect to appropriate bases), then the composition T∘S: U → W has matrix AB.

The matrix of the composition is the product of the individual matrices, with proper attention to the order (matrix multiplication is not commutative).

### Change of Basis

The matrix representation of a linear transformation changes when we change the basis. If P is the change-of-basis matrix from old basis to new basis in the domain, and Q is the change-of-basis matrix in the codomain, then:
[T]\_{new} = Q^{-1}AP

where A is the matrix in the old basis.

## Examples

### Example 1: Finding Matrix Representation

**Problem**: Let T: ℝ² → ℝ² be defined by T(x, y) = (2x + y, x - 3y). Find the matrix representation of T with respect to the standard basis.

**Solution**:

Step 1: Apply T to standard basis vectors e₁ = (1, 0) and e₂ = (0, 1).

- T(1, 0) = (2(1) + 0, 1 - 3(0)) = (2, 1)
- T(0, 1) = (2(0) + 1, 0 - 3(1)) = (1, -3)

Step 2: Express these as coordinate vectors in ℝ² (which are the same as the vectors themselves):

- [T(e₁)] = [2, 1]ᵀ
- [T(e₂)] = [1, -3]ᵀ

Step 3: Form the matrix with these as columns:
A = [[2, 1], [1, -3]]

**Verification**: For any vector v = (x, y), we can check:
Av = [[2, 1], [1, -3]] [x, y]ᵀ = [2x + y, x - 3y]ᵀ = T(x, y) ✓

### Example 2: Transformation in ℝ³

**Problem**: Let T: ℝ³ → ℝ² be defined by T(x, y, z) = (x + y, y - z). Find the matrix representation with respect to standard bases.

**Solution**:

Step 1: Apply T to basis vectors:

- T(1, 0, 0) = (1 + 0, 0 - 0) = (1, 0)
- T(0, 1, 0) = (0 + 1, 1 - 0) = (1, 1)
- T(0, 0, 1) = (0 + 0, 0 - 1) = (0, -1)

Step 2: Express as coordinate vectors:

- [T(e₁)] = [1, 0]ᵀ
- [T(e₂)] = [1, 1]ᵀ
- [T(e₃)] = [0, -1]ᵀ

Step 3: Form the 2 × 3 matrix:
A = [[1, 1, 0], [0, 1, -1]]

### Example 3: Composition of Transformations

**Problem**: Let S: ℝ² → ℝ² be rotation by 90° counterclockwise, and T: ℝ² → ℝ² be scaling by factor 2. Find the matrix representing T∘S.

**Solution**:

Step 1: Find matrices:

- S = [[cos 90°, -sin 90°], [sin 90°, cos 90°]] = [[0, -1], [1, 0]]
- T = [[2, 0], [0, 2]] = 2I

Step 2: Compute T∘S:
(T∘S) matrix = T × S = [[2, 0], [0, 2]] × [[0, -1], [1, 0]]
= [[2×0 + 0×1, 2×(-1) + 0×0], [0×0 + 2×1, 0×(-1) + 2×0]]
= [[0, -2], [2, 0]]

This represents rotation by 90° followed by scaling by 2.

## Exam Tips

1. **Always identify bases first**: Before finding the matrix representation, clearly state the bases being used for domain and codomain.

2. **Standard basis problems are most common**: In university exams, most problems use standard bases, so focus on finding standard matrices.

3. **Verify linearity before proceeding**: Check if the given transformation is linear; if not, matrix representation doesn't apply.

4. **Matrix-vector multiplication**: Remember that A[v] gives T(v), where v is the coordinate vector in the domain basis.

5. **Order matters in composition**: T∘S corresponds to matrix AB, not BA (apply S first, then T).

6. **Dimension compatibility**: The number of columns of the matrix equals the dimension of the domain; number of rows equals dimension of codomain.

7. **Special transformations**: Memorize standard matrices for rotation, reflection, scaling, projection, and shear transformations.

8. **Change of basis problems**: When bases change, use similarity transformation: [T]\_new = P^{-1}[T]\_old P.

9. **Practice with ℝ² and ℝ³**: Most exam problems involve 2D or 3D spaces, so practice extensively in these dimensions.

10. **Show all working**: In exams, clearly show each step: applying T to basis vectors, finding coordinates, forming the matrix.
