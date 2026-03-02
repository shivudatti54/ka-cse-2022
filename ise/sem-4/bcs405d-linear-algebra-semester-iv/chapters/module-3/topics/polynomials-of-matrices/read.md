Of course. Here is comprehensive educational content on "Polynomials of Matrices" tailored for  Engineering students.

# Polynomials of Matrices

**Subject:** Linear Algebra | **Semester:** IV | **Module:** 3 (Eigenvalues and Eigenvectors)

---

## 1. Introduction

In algebra, we often work with polynomial functions of a variable, like `p(x) = 2x² - 3x + 5`. A natural question arises in linear algebra: can we evaluate such a polynomial when `x` is replaced by a square matrix `A`? The answer is yes. Evaluating polynomials for matrices is not just a theoretical exercise; it is a fundamental tool with critical applications in solving systems of differential equations, computer graphics (rotations and scaling), stability analysis in control systems, and more advanced matrix functions like `e^A` (matrix exponential).

## 2. Core Concepts

### 2.1. Definition of a Matrix Polynomial

Let `p(t)` be a polynomial in a variable `t` defined as:
`p(t) = aₙtⁿ + aₙ₋₁tⁿ⁻¹ + ... + a₁t + a₀`
where `a₀, a₁, ..., aₙ` are scalars.

If `A` is an `n x n` square matrix, then the matrix polynomial `p(A)` is defined as:
`p(A) = aₙAⁿ + aₙ₋₁Aⁿ⁻¹ + ... + a₁A + a₀I`

**Crucial Point:** The constant term `a₀` becomes `a₀` multiplied by the **identity matrix `I`** of the same order as `A`. This is necessary for the addition of matrices to be defined.

### 2.2. How to Compute `p(A)`

The computation is straightforward:

1.  Compute the powers of the matrix `A` (`A²`, `A³`, ..., `Aⁿ`).
2.  Multiply each matrix power by its corresponding scalar coefficient.
3.  Sum all the resulting matrices together, including the `a₀I` term.

### 2.3. The Connection to Eigenvalues (The Spectral Mapping Theorem)

This is the most important property of matrix polynomials and directly links this topic to Module 3. It states:

> If `λ` is an eigenvalue of a matrix `A` with corresponding eigenvector `x`, then for the polynomial `p(A)`, the eigenvalue is `p(λ)` and the eigenvector remains the same `x`.

**Proof:**
We know `A x = λ x`.
Let's compute `p(A)x`:
`p(A)x = (aₙAⁿ + aₙ₋₁Aⁿ⁻¹ + ... + a₁A + a₀I)x`
`= aₙAⁿx + aₙ₋₁Aⁿ⁻¹x + ... + a₁A x + a₀I x`

Since `Aᵏx = λᵏx` (because `A²x = A(Ax) = A(λx) = λ(Ax) = λ²x`, and so on), we can substitute:
`= aₙλⁿx + aₙ₋₁λⁿ⁻¹x + ... + a₁λ x + a₀x`
`= (aₙλⁿ + aₙ₋₁λⁿ⁻¹ + ... + a₁λ + a₀)x`
`= p(λ)x`

Therefore, `p(A)x = p(λ)x`, proving that `p(λ)` is an eigenvalue of `p(A)` with the same eigenvector `x`.

## 3. Example

Let `A = [[2, 1], [0, 3]]` and consider the polynomial `p(t) = t² - 5t + 3`. Let's find `p(A)`.

**Step 1: Compute the necessary powers of A.**

- `A² = A * A = [[2,1],[0,3]] * [[2,1],[0,3]] = [[4,5],[0,9]]`
- (We need `A²` and `A`. The `I` for the constant term is implied).

**Step 2: Apply the polynomial.**
`p(A) = A² - 5A + 3I`
`= [[4, 5], [0, 9]] - 5 * [[2, 1], [0, 3]] + 3 * [[1, 0], [0, 1]]`
`= [[4, 5], [0, 9]] + [[-10, -5], [0, -15]] + [[3, 0], [0, 3]]`
`= [[4 -10 + 3, 5 -5 + 0], [0 + 0 + 0, 9 -15 + 3]]`
`= [[-3, 0], [0, -3]]`

**Step 3: Verify using eigenvalues.**
First, find the eigenvalues `λ` of `A`:
The characteristic equation is `(2-λ)(3-λ) = 0`, so eigenvalues are `λ₁ = 2` and `λ₂ = 3`.

Now, apply the polynomial `p(t)` to these eigenvalues:

- `p(λ₁) = p(2) = (2)² - 5*(2) + 3 = 4 - 10 + 3 = -3`
- `p(λ₂) = p(3) = (3)² - 5*(3) + 3 = 9 - 15 + 3 = -3`

According to the Spectral Mapping Theorem, the eigenvalues of `p(A)` should be `-3` and `-3`. The matrix we computed, `p(A) = [[-3, 0], [0, -3]] = -3I`, indeed has a single eigenvalue `-3` with multiplicity 2. This confirms our result.

## 4. Key Points & Summary

- A **matrix polynomial** `p(A)` is defined for a square matrix `A` as `p(A) = aₙAⁿ + ... + a₁A + a₀I`.
- The constant term in the polynomial must be replaced with the scalar multiplied by the **identity matrix `I`**.
- Computation involves calculating matrix powers, scalar multiplication, and matrix addition.
- **Spectral Mapping Theorem:** If `λ` is an eigenvalue of `A`, then `p(λ)` is an eigenvalue of `p(A)`. The eigenvectors of `A` remain eigenvectors of `p(A)`.
- This theorem provides a powerful shortcut to find the eigenvalues of `p(A)` without performing the full matrix computation, and is fundamental to understanding how functions act on linear transformations.
- This concept is a building block for defining more complex matrix functions (e.g., `e^A`, `sin(A)`) using their power series expansions.
