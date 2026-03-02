# Linearization and Multivariate Taylor Series

## Table of Contents

- [Linearization and Multivariate Taylor Series](#linearization-and-multivariate-taylor-series)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Multivariate Taylor Series Expansion](#multivariate-taylor-series-expansion)
  - [Gradient Vector](#gradient-vector)
  - [Hessian Matrix](#hessian-matrix)
  - [Remainder Term](#remainder-term)
  - [Second-Order Approximation](#second-order-approximation)
- [Examples](#examples)
  - [Example 1: Linearization of Two-Variable Function](#example-1-linearization-of-two-variable-function)
  - [Example 2: Second-Order Taylor Approximation](#example-2-second-order-taylor-approximation)
  - [Example 3: Using Taylor Series for Optimization](#example-3-using-taylor-series-for-optimization)
- [Exam Tips](#exam-tips)

## Introduction

Linearization and Multivariate Taylor Series form the mathematical foundation for many optimization techniques taught in engineering curricula. These concepts allow us to approximate complex nonlinear functions using simpler linear or polynomial representations, making them indispensable tools for solving real-world engineering problems.

In the context of optimization, we frequently encounter functions of multiple variables that are difficult to analyze directly. The multivariate Taylor series provides a systematic way to approximate such functions around a specific point, enabling us to understand local behavior, find critical points, and develop iterative optimization algorithms. Linearization, the simplest form of this approximation, replaces a nonlinear function with its first-order Taylor polynomial, which serves as the basis for gradient-based optimization methods like Newton's method and gradient descent.

This topic is particularly crucial for CSE students as it bridges mathematical theory with practical applications in machine learning, data science, and engineering optimization. Understanding these concepts enables students to grasp why gradient-based methods work and how to analyze their convergence properties.

## Key Concepts

### Multivariate Taylor Series Expansion

The multivariate Taylor series expands a function of several variables around a point in terms of its partial derivatives. For a function f(x₁, x₂, ..., xₙ) that has continuous partial derivatives up to order m at a point a = (a₁, a₂, ..., aₙ), the Taylor expansion is:

**f(x) = f(a) + ∇f(a)·(x-a) + ½(x-a)ᵀH(f)(a)(x-a) + ... + Rₘ**

Where:

- ∇f(a) is the gradient vector at point a
- H(f)(a) is the Hessian matrix at point a
- Rₘ is the remainder term

**First-Order Expansion (Linearization):**
f(x) ≈ f(a) + ∑ᵢ ∂f/∂xᵢ (a) · (xᵢ - aᵢ) = f(a) + ∇f(a)ᵀ(x - a)

This linear approximation is called the **linearization** of f at point a.

### Gradient Vector

The gradient of a function f(x₁, x₂, ..., xₙ) is a column vector of first-order partial derivatives:

∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]ᵀ

The gradient points in the direction of steepest ascent and is perpendicular to level curves/surfaces.

### Hessian Matrix

The Hessian matrix contains all second-order partial derivatives:

H(f) = [∂²f/∂xᵢ∂xⱼ] for i, j = 1 to n

For a function of two variables x and y:

```
H(f) = [ ∂²f/∂x² ∂²f/∂x∂y ]
 [ ∂²f/∂y∂x ∂²f/∂y² ]
```

The Hessian is symmetric if continuous second-order partial derivatives exist.

### Remainder Term

The Lagrange form of the remainder for multivariate case:
Rₖ = ∑|ᵅ|=k (f^(α)(c)/α!)(x-a)^α
where c lies between x and a, and |α| = k

For practical purposes, we use the big-O notation:
f(x) = f(a) + ∇f(a)ᵀ(x-a) + O(||x-a||²)

### Second-Order Approximation

f(x) ≈ f(a) + ∇f(a)ᵀ(x-a) + ½(x-a)ᵀH(f)(a)(x-a)

This quadratic approximation is crucial for Newton's method in optimization.

## Examples

### Example 1: Linearization of Two-Variable Function

**Problem:** Find the linearization of f(x,y) = x² + xy + y² at point (1,1). Use it to approximate f(1.1, 0.9).

**Solution:**

**Step 1: Compute function value at base point**
f(1,1) = 1² + 1·1 + 1² = 1 + 1 + 1 = 3

**Step 2: Compute partial derivatives**
∂f/∂x = 2x + y
∂f/∂y = x + 2y

**Step 3: Evaluate partial derivatives at (1,1)**
∂f/∂x(1,1) = 2(1) + 1 = 3
∂f/∂y(1,1) = 1 + 2(1) = 3

**Step 4: Form linearization**
L(x,y) = f(1,1) + ∂f/∂x(1,1)(x-1) + ∂f/∂y(1,1)(y-1)
L(x,y) = 3 + 3(x-1) + 3(y-1)
L(x,y) = 3 + 3x - 3 + 3y - 3
L(x,y) = 3x + 3y - 3

**Step 5: Approximate f(1.1, 0.9)**
L(1.1, 0.9) = 3(1.1) + 3(0.9) - 3 = 3.3 + 2.7 - 3 = 3.0

**Actual value:** f(1.1, 0.9) = (1.1)² + 1.1(0.9) + (0.9)² = 1.21 + 0.99 + 0.81 = 3.01

**Error:** |3.01 - 3.0| = 0.01 (very small approximation!)

### Example 2: Second-Order Taylor Approximation

**Problem:** Use second-order Taylor series to approximate f(0.1, 0.2) for f(x,y) = e^(x+y) at point (0,0).

**Solution:**

**Step 1: Function value at origin**
f(0,0) = e^0 = 1

**Step 2: First-order partial derivatives**
∂f/∂x = e^(x+y)
∂f/∂y = e^(x+y)

At (0,0): ∂f/∂x(0,0) = 1, ∂f/∂y(0,0) = 1

**Step 3: Second-order partial derivatives**
∂²f/∂x² = e^(x+y)
∂²f/∂y² = e^(x+y)
∂²f/∂x∂y = e^(x+y)

At (0,0): All equal to 1

**Step 4: Hessian matrix at origin**
H(f)(0,0) = [1 1]
[1 1]

**Step 5: Second-order approximation**
f(x,y) ≈ 1 + [1, 1]·[x, y]ᵀ + ½[x, y] [1 1][x]ᵀ
[1 1] [y]

f(x,y) ≈ 1 + x + y + ½(x² + 2xy + y²)
f(x,y) ≈ 1 + x + y + 0.5x² + xy + 0.5y²

**Step 6: Approximate at (0.1, 0.2)**
f(0.1, 0.2) ≈ 1 + 0.1 + 0.2 + 0.5(0.01) + 0.1(0.2) + 0.5(0.04)
≈ 1.3 + 0.005 + 0.02 + 0.02
≈ 1.345

**Actual value:** f(0.1, 0.2) = e^0.3 ≈ 1.34986

**Error:** Very small approximation error achieved!

### Example 3: Using Taylor Series for Optimization

**Problem:** Find critical points of f(x,y) = x³ - 3x - y² + 4y using Taylor series approach.

**Solution:**

**Step 1: Find gradient**
∇f = [∂f/∂x, ∂f/∂y] = [3x² - 3, -2y + 4]

**Step 2: Set gradient to zero for critical points**
3x² - 3 = 0 → x² = 1 → x = ±1
-2y + 4 = 0 → y = 2

Critical points: (1, 2) and (-1, 2)

**Step 3: Hessian matrix**
H(f) = [6x 0 ]
[0 -2 ]

**Step 4: Classify critical points using Hessian**
At (1, 2): H = [6 0] → Eigenvalues: 6, -2
[0 -2]
Since eigenvalues have opposite signs, (-1)ⁿ × (product) < 0: **Saddle Point**

At (-1, 2): H = [-6 0] → Eigenvalues: -6, -2
[0 -2]
Both eigenvalues negative: **Local Maximum**

**Step 5: Second-order Taylor test at (1,2)**
f(x,y) ≈ f(1,2) + ½ΔxᵀHΔx
For direction [1,0]: ½(1)(6)(1) = 3 > 0
For direction [0,1]: ½(1)(-2)(1) = -1 < 0
Confirms saddle point behavior.

## Exam Tips

1. **Remember the linearization formula:** L(x) = f(a) + ∇f(a)ᵀ(x-a) is the fundamental linearization formula - practice writing this from memory.

2. **Gradient and Hessian are essential:** Know how to compute gradient vectors and Hessian matrices for multivariable functions as they appear in almost every optimization problem.

3. **Symmetry of Hessian:** The Hessian matrix is always symmetric if second-order partial derivatives are continuous - use this property to verify your calculations.

4. **Taylor series application in optimization:** Second-order Taylor expansion is used in Newton's method: xₖ₊₁ = xₖ - H⁻¹∇f for finding optimum points.

5. **Classification using Hessian:** For critical points, if Hessian is positive definite → local minimum; negative definite → local maximum; indefinite → saddle point.

6. **Big-O notation:** Remember that the first-order approximation error is O(||x-a||²), meaning error decreases quadratically as we approach the expansion point.

7. **Common expansion point choices:** For optimization, we typically expand around critical points (where ∇f = 0) to analyze the nature of extrema.

8. **Practice two-variable problems thoroughly:** Most exam questions involve functions of two variables, so master ∂f/∂x, ∂f/∂y, and the 2×2 Hessian matrix.
