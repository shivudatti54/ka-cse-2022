# Linear Transformations: Singular vs. Non-Singular

## 1. Introduction

In Linear Algebra, a **linear transformation** is a function `T: V → W` between two vector spaces that preserves the operations of vector addition and scalar multiplication. A fundamental question we ask about such a transformation is: "Does it have an inverse?" The answer to this question hinges on whether the transformation is singular or non-singular. Understanding this distinction is crucial for solving systems of linear equations, analyzing vector spaces, and applications in computer graphics, data science, and control systems.

## 2. Core Concepts

### Prerequisites: Kernel and Image

Before defining singularity, we must recall two key subspaces:

- **Kernel (or Null Space):** `Ker(T) = { v ∈ V | T(v) = 0 }`. It's the set of all vectors in `V` that map to the zero vector in `W`.
- **Image (or Range):** `Im(T) = { T(v) | v ∈ V }`. It's the set of all vectors in `W` that are the image of some vector in `V`.

### Non-Singular (Invertible) Linear Transformation

A linear transformation `T: V → W` is said to be **non-singular** or **invertible** if it satisfies the following equivalent conditions:

1.  `T` is one-to-one (injective).
2.  The kernel of `T` is trivial: `Ker(T) = {0}`.
3.  `T` maps linearly independent sets in `V` to linearly independent sets in `W`.
4.  An inverse transformation `T⁻¹: W → V` exists, which is also linear.

If `V` and `W` are finite-dimensional and `dim(V) = dim(W)`, non-singularity also implies that `T` is onto (surjective).

### Singular (Non-Invertible) Linear Transformation

A linear transformation `T: V → W` is **singular** if it is **not** non-singular. This means:

1.  `T` is not one-to-one. Multiple distinct vectors in `V` map to the same vector in `W`.
2.  The kernel is non-trivial: `Ker(T) ≠ {0}`. There exists at least one non-zero vector `v` such that `T(v) = 0`.
3.  `T` maps at least one linearly independent set to a linearly dependent set.

## 3. Examples

Let’s consider transformations `T: R² → R²`.

**Example 1: Non-Singular Transformation**
Let `T(x, y) = (2x + y, x - 3y)`. This can be represented by the matrix `A = [[2, 1], [1, -3]]`.

- **Kernel:** Solve `T(v) = 0`.
  `2x + y = 0`
  `x - 3y = 0`
  The only solution is `x = 0, y = 0`. Thus, `Ker(T) = {0}`.
- Since the kernel is trivial, `T` is one-to-one. Furthermore, `det(A) = (2)(-3) - (1)(1) = -7 ≠ 0`, confirming it's invertible. `T` is non-singular.

**Example 2: Singular Transformation**
Let `T(x, y) = (x + 2y, 2x + 4y)`. This can be represented by the matrix `B = [[1, 2], [2, 4]]`.

- **Kernel:** Solve `T(v) = 0`.
  `x + 2y = 0`
  `2x + 4y = 0`
  These equations are linearly dependent. The solutions are all vectors of the form `(-2t, t)`
  for any scalar `t`. Thus, `Ker(T) = span{(-2, 1)} ≠ {0}`.
- Since the kernel contains non-zero vectors (e.g., `(-2, 1)`), `T` is not one-to-one. Also, `det(B) = (1)(4) - (2)(2) = 0`. `T` is singular.

## 4. Key Points & Summary

| Feature                                    | Non-Singular Transformation (`T`)            | Singular Transformation (`T`)               |
| :----------------------------------------- | :------------------------------------------- | :------------------------------------------ |
| **One-to-One (Injective)**                 | **Yes**                                      | **No**                                      |
| **Kernel (`Ker(T)`)**                      | Trivial: `{0}`                               | **Non-trivial** (Contains non-zero vectors) |
| **Invertible**                             | **Yes** (`T⁻¹` exists)                       | **No** (`T⁻¹` does not exist)               |
| **Determinant** <br> (for square matrices) | `det(A) ≠ 0`                                 | `det(A) = 0`                                |
| **Effect on Independence**                 | Preserves linear independence                | **Does not** preserve linear independence   |
| **Rank** <br> (`dim(Im(T))`)               | `rank(T) = dim(V)` <br> (if `dim(V)=dim(W)`) | `rank(T) < dim(V)`                          |

**Summary:**

- The concepts of **singularity** and **non-singularity** classify linear transformations based on their invertibility.
- A transformation is **non-singular** if and only if its **kernel is trivial**. This makes it one-to-one and invertible.
- A **singular** transformation has a **non-trivial kernel**, meaning it "collapses" information by mapping an entire line of vectors to zero. This destroys invertibility.
- For a transformation represented by a square matrix `A`, the **determinant provides a quick test**: `det(A) = 0` implies singularity, while `det(A) ≠ 0` implies non-singularity.
