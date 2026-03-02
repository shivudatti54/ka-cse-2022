# Hessian Matrix

## Table of Contents

- [Hessian Matrix](#hessian-matrix)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of the Hessian Matrix](#definition-of-the-hessian-matrix)
  - [Relationship with Gradient and Jacobian](#relationship-with-gradient-and-jacobian)
  - [Second-Order Taylor Series Expansion](#second-order-taylor-series-expansion)
  - [Classification of Critical Points](#classification-of-critical-points)
  - [Sylvester's Criterion](#sylvesters-criterion)
  - [Eigenvalues and Quadratic Forms](#eigenvalues-and-quadratic-forms)
- [Examples](#examples)
  - [Example 1: Hessian of a Two-Variable Function](#example-1-hessian-of-a-two-variable-function)
  - [Example 2: Classifying a Critical Point](#example-2-classifying-a-critical-point)
  - [Example 3: Hessian with Saddle Point](#example-3-hessian-with-saddle-point)
- [Exam Tips](#exam-tips)

## Introduction

The Hessian Matrix is a fundamental concept in multivariable calculus and optimization theory that plays a crucial role in understanding the local curvature of scalar-valued functions. Named after the German mathematician Ludwig Otto Hesse, this matrix contains all the second-order partial derivatives of a function with multiple variables. In the context of the university's Linear Algebra course (BCS405D), the Hessian Matrix serves as a bridge between differential calculus and linear algebra, providing powerful tools for analyzing optimization problems, classifying critical points, and understanding the behavior of multivariable functions.

The importance of the Hessian Matrix extends far beyond theoretical mathematics. In computer science and engineering, particularly in machine learning and optimization algorithms, the Hessian Matrix is essential for understanding convergence properties of gradient descent methods, training neural networks, and solving constrained optimization problems. For university students, mastering this topic provides the mathematical foundation necessary for advanced courses in artificial intelligence, computer vision, and data science.

This module explores the theoretical foundations of the Hessian Matrix, its properties, computational methods, and applications in determining the nature of critical points in multivariable functions. Understanding this topic is essential for engineers who will work with optimization problems, numerical methods, and machine learning algorithms in their professional careers.

## Key Concepts

### Definition of the Hessian Matrix

Given a scalar-valued function f(x₁, x₂, ..., xₙ) = f(x) of n variables that has continuous second-order partial derivatives in a neighborhood of a point, the Hessian Matrix H at a point x = (x₁, x₂, ..., xₙ) is defined as the n × n matrix of second-order partial derivatives:

H(f)(x) = [∂²f/∂xᵢ∂xⱼ] =

```
| ∂²f/∂x₁² ∂²f/∂x₁∂x₂ ∂²f/∂x₁∂x₃ ... ∂²f/∂x₁∂xₙ |
| ∂²f/∂x₂∂x₁ ∂²f/∂x₂² ∂²f/∂x₂∂x₃ ... ∂²f/∂x₂∂xₙ |
| ∂²f/∂x₃∂x₁ ∂²f/∂x₃∂x₂ ∂²f/∂x₃² ... ∂²f/∂x₃∂xₙ |
| ... ... ... ... ... |
| ∂²f/∂xₙ∂x₁ ∂²f/∂xₙ∂x₂ ∂²f/∂xₙ∂x₃ ... ∂²f/∂xₙ² |
```

The (i, j)-th entry of the Hessian is the second-order partial derivative ∂²f/(∂xᵢ∂xⱼ). If the function has continuous second-order partial derivatives (which is the case for most functions encountered in engineering), then Clairaut's theorem applies, and the Hessian is symmetric: ∂²f/∂xᵢ∂xⱼ = ∂²f/∂xⱼ∂xᵢ.

### Relationship with Gradient and Jacobian

The Hessian Matrix is closely related to two other important mathematical constructs:

1. **Gradient (∇f)**: The gradient is a vector of first-order partial derivatives:
   ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]ᵀ

The Hessian is the matrix of derivatives of the gradient, i.e., H(f) = ∇(∇f)ᵀ.

2. **Jacobian Matrix**: For a vector-valued function f: ℝⁿ → ℝᵐ, the Jacobian is the matrix of first-order partial derivatives. The Hessian is essentially the Jacobian of the gradient.

### Second-Order Taylor Series Expansion

One of the most important applications of the Hessian Matrix is in the second-order Taylor series expansion of a function around a point a:

f(x) ≈ f(a) + ∇f(a)ᵀ(x - a) + ½(x - a)ᵀH(f)(a)(x - a) + higher-order terms

This quadratic approximation is crucial in optimization, where we use it to determine whether a critical point is a local minimum, maximum, or saddle point.

### Classification of Critical Points

Let f: ℝⁿ → ℝ be a twice continuously differentiable function, and let x* be a critical point where ∇f(x*) = 0. The Hessian at this point, H(x\*), determines the nature of the critical point:

1. **Positive Definite Hessian**: If H(x*) is positive definite, then x* is a strict local minimum. All eigenvalues of H are positive.

2. **Negative Definite Hessian**: If H(x*) is negative definite, then x* is a strict local maximum. All eigenvalues of H are negative.

3. **Indefinite Hessian**: If H(x*) has both positive and negative eigenvalues, then x* is a saddle point (neither minimum nor maximum).

4. **Positive/Negative Semidefinite Hessian**: If H(x\*) is positive semidefinite or negative semidefinite, the second-order test is inconclusive, and higher-order terms must be considered.

### Sylvester's Criterion

For determining definiteness of symmetric matrices (including Hessian matrices), Sylvester's criterion provides a convenient test:

- A symmetric matrix is **positive definite** if and only if all leading principal minors (determinants of upper-left k × k submatrices for k = 1, 2, ..., n) are positive.

- A symmetric matrix is **negative definite** if and only if the leading principal minors alternate in sign, with the first one being negative.

### Eigenvalues and Quadratic Forms

The Hessian Matrix being symmetric (for continuously differentiable functions) implies it has real eigenvalues and can be diagonalized. The definiteness of the Hessian can also be understood through quadratic forms:

- xᵀHx > 0 for all non-zero x ⇒ H is positive definite
- xᵀHx < 0 for all non-zero x ⇒ H is negative definite
- xᵀHx can be positive or negative ⇒ H is indefinite

## Examples

### Example 1: Hessian of a Two-Variable Function

Find the Hessian Matrix of f(x, y) = x³ + xy + y³ at the point (1, 2), and determine if the function has a local minimum or maximum at that point.

**Solution:**

First, compute all first-order partial derivatives:
∂f/∂x = 3x² + y
∂f/∂y = x + 3y²

Now compute all second-order partial derivatives:
∂²f/∂x² = 6x
∂²f/∂y² = 6y
∂²f/∂x∂y = ∂²f/∂y∂x = 1

The Hessian Matrix is:
H(x, y) = | 6x 1 |
| 1 6y |

At the point (1, 2):
H(1, 2) = | 6 1 |
| 1 12 |

Now, check if (1, 2) is a critical point:
∇f(1, 2) = [3(1)² + 2, 1 + 3(2)²] = [5, 13] ≠ (0, 0)

So (1, 2) is NOT a critical point. The Hessian classification is only valid at critical points. This example demonstrates the importance of first checking the gradient.

### Example 2: Classifying a Critical Point

Find and classify all critical points of f(x, y) = x² + y² - 4x - 6y.

**Solution:**

First, find the critical points by setting the gradient to zero:
∂f/∂x = 2x - 4 = 0 ⇒ x = 2
∂f/∂y = 2y - 6 = 0 ⇒ y = 3

The only critical point is (2, 3).

Now compute the Hessian:
∂²f/∂x² = 2
∂²f/∂y² = 2
∂²f/∂x∂y = 0

H(2, 3) = | 2 0 |
| 0 2 |

Using Sylvester's criterion:

- First leading principal minor: det([2]) = 2 > 0
- Determinant of full matrix: det(H) = (2)(2) - (0)(0) = 4 > 0

Since both leading principal minors are positive, H is positive definite.

Therefore, (2, 3) is a strict local minimum (and also the global minimum for this convex function).

The minimum value is f(2, 3) = 2² + 3² - 4(2) - 6(3) = 4 + 9 - 8 - 18 = -13.

### Example 3: Hessian with Saddle Point

Analyze the critical points of f(x, y) = x² - y².

**Solution:**

Find critical points:
∂f/∂x = 2x = 0 ⇒ x = 0
∂f/∂y = -2y = 0 ⇒ y = 0

Critical point: (0, 0)

Compute Hessian:
∂²f/∂x² = 2
∂²f/∂y² = -2
∂²f/∂x∂y = 0

H(0, 0) = | 2 0 |
| 0 -2 |

The eigenvalues are λ₁ = 2 and λ₂ = -2 (one positive, one negative).

Since the Hessian has both positive and negative eigenvalues, it is indefinite.

Therefore, (0, 0) is a saddle point. Indeed, along the x-axis, f(x, 0) = x² ≥ 0 (minimum behavior), while along the y-axis, f(0, y) = -y² ≤ 0 (maximum behavior).

## Exam Tips

1. **Always Check Critical Points First**: The Hessian classification is only valid at critical points where ∇f = 0. Finding critical points is the first step in optimization problems.

2. **Remember Symmetry**: For functions with continuous second-order partial derivatives, the Hessian is symmetric (Clairaut's theorem). This property is essential for applying Sylvester's criterion.

3. **Sylvester's Criterion Application**: For positive definiteness, all leading principal minors must be positive. For negative definiteness, they must alternate in sign starting with negative.

4. **Relationship Between Tests**: You can use either eigenvalues or leading principal minors to determine definiteness. For exam problems, Sylvester's criterion is usually faster for small matrices.

5. **Second-Order Taylor Series**: Remember the quadratic term formula: ½(x-a)ᵀH(x-a). This is frequently tested in examinations.

6. **Indefinite = Saddle Point**: If the Hessian has both positive and negative eigenvalues (or determinants of submatrices don't satisfy definiteness conditions), you have a saddle point.

7. **Semidefinite Cases**: When the Hessian is positive or negative semidefinite, the second derivative test is inconclusive. Higher-order derivatives must be examined, which is beyond the scope of most introductory courses.

8. **Practice Computation**: Be thorough in computing partial derivatives. Common errors include forgetting to apply the chain rule or making sign mistakes.
