# Functions of Several Variables

## Table of Contents

- [Functions of Several Variables](#functions-of-several-variables)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Functions of Several Variables](#1-functions-of-several-variables)
  - [2. Partial Derivatives](#2-partial-derivatives)
  - [3. The Gradient Vector](#3-the-gradient-vector)
  - [4. Directional Derivatives](#4-directional-derivatives)
  - [5. Jacobian Matrix](#5-jacobian-matrix)
  - [6. Hessian Matrix](#6-hessian-matrix)
  - [7. Taylor's Theorem for Multivariable Functions](#7-taylors-theorem-for-multivariable-functions)
  - [8. Maxima and Minima of Multivariable Functions](#8-maxima-and-minima-of-multivariable-functions)
- [Examples](#examples)
  - [Example 1: Finding Critical Points and Classification](#example-1-finding-critical-points-and-classification)
  - [Example 2: Using Gradient for Optimization](#example-2-using-gradient-for-optimization)
  - [Example 3: Constrained Optimization Setup](#example-3-constrained-optimization-setup)
- [Exam Tips](#exam-tips)

## Introduction

Functions of several variables form the foundation of multivariable calculus and play a crucial role in optimization techniques. While single-variable calculus deals with functions that depend on one independent variable, real-world optimization problems typically involve multiple variables simultaneously. For instance, a company optimizing production might consider cost, quality, time, and resource allocation as multiple interdependent variables.

In engineering and computer science applications, functions of several variables appear frequently. Machine learning algorithms optimize loss functions with thousands of parameters, control systems optimize multiple performance metrics simultaneously, and resource allocation problems balance competing objectives. Understanding how to analyze such functions—finding their maxima, minima, and saddle points—is essential for solving these practical optimization problems.

This module introduces the mathematical tools required to analyze functions of several variables, including partial derivatives, the gradient vector, directional derivatives, and methods for finding extrema. These concepts provide the groundwork for understanding constrained optimization, Lagrange multipliers, and numerical optimization methods covered in subsequent modules.

## Key Concepts

### 1. Functions of Several Variables

A function of several variables maps tuples of real numbers to a real number. For example, f(x, y) = x² + y² represents a paraboloid surface in three-dimensional space. The domain of such functions is a subset of ℝⁿ, and the range is a subset of ℝ.

**Level Curves and Surfaces**: For f(x, y), level curves connect points with equal function values (like topographic maps). For three-variable functions, we use level surfaces. These visualizations help understand the behavior of multivariable functions.

### 2. Partial Derivatives

Partial derivatives measure the rate of change of a function with respect to one variable while holding other variables constant. For f(x, y), the partial derivative with respect to x is:

$$\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}$$

Similarly, ∂f/∂y measures change in the y-direction. Partial derivatives of higher order exist: fₓₓ = ∂²f/∂x², fₓᵧ = ∂²f/∂x∂y, and so on.

** Clairaut's Theorem (Equality of Mixed Partials)**: If partial derivatives are continuous in a neighborhood, mixed partials are equal: fₓᵧ = fᵧₓ.

### 3. The Gradient Vector

The gradient of f, denoted ∇f, is a vector containing all first-order partial derivatives:

$$\nabla f = \left(\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, ..., \frac{\partial f}{\partial x_n}\right)$$

The gradient has two critical properties:

- It points in the direction of steepest ascent (maximum increase)
- Its magnitude equals the maximum rate of change
- At any point, ∇f is perpendicular to the level curve/surface through that point

### 4. Directional Derivatives

The directional derivative in the direction of a unit vector u = (u₁, u₂, ..., uₙ) measures the rate of change of f in that direction:

$$D_u f = \nabla f \cdot u = \frac{\partial f}{\partial x_1}u_1 + \frac{\partial f}{\partial x_2}u_2 + ... + \frac{\partial f}{\partial x_n}u_n$$

This generalizes partial derivatives to any direction, not just coordinate axes.

### 5. Jacobian Matrix

For a vector-valued function F: ℝⁿ → ℝᵐ, the Jacobian matrix contains all first-order partial derivatives:

$$J_F = \begin{pmatrix} \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & ... & \frac{\partial f_1}{\partial x_n} \\ \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & ... & \frac{\partial f_2}{\partial x_n} \\ ... & ... & ... & ... \\ \frac{\partial f_m}{\partial x_1} & \frac{\partial f_m}{\partial x_2} & ... & \frac{\partial f_m}{\partial x_n} \end{pmatrix}$$

The Jacobian generalizes the derivative concept to vector-valued functions and appears in change-of-variables theorems and solving systems of equations.

### 6. Hessian Matrix

The Hessian matrix contains all second-order partial derivatives:

$$H_f = \begin{pmatrix} f_{x_1x_1} & f_{x_1x_2} & ... & f_{x_1x_n} \\ f_{x_2x_1} & f_{x_2x_2} & ... & f_{x_2x_n} \\ ... & ... & ... & ... \\ f_{x_nx_1} & f_{x_nx_2} & ... & f_{x_nx_n} \end{pmatrix}$$

The Hessian is symmetric if continuous second derivatives exist (Clairaut's theorem). It plays a crucial role in determining the nature of critical points.

### 7. Taylor's Theorem for Multivariable Functions

Taylor's expansion generalizes to multivariable functions. For f(x, y) near (a, b):

$$f(a+h, b+k) = f(a,b) + h f_x(a,b) + k f_y(a,b) + \frac{1}{2}(h^2 f_{xx} + 2hk f_{xy} + k^2 f_{yy}) + ...$$

This expansion is fundamental in numerical optimization methods, where we approximate functions locally by quadratic forms.

### 8. Maxima and Minima of Multivariable Functions

**Critical Points**: A point (a, b) is critical when ∇f(a, b) = 0 or ∇f doesn't exist. This means:
$$\frac{\partial f}{\partial x} = 0 \quad \text{and} \quad \frac{\partial f}{\partial y} = 0$$

**Classification using Hessian**: For f(x, y), at a critical point:

- If det(H) > 0 and fₓₓ > 0: local minimum
- If det(H) > 0 and fₓₓ < 0: local maximum
- If det(H) < 0: saddle point
- If det(H) = 0: test inconclusive (need higher derivatives)

Here, det(H) = fₓₓfᵧᵧ - (fₓᵧ)²

**Global Extrema**: For continuous functions on closed bounded domains, global extrema occur at critical points or boundaries. The Extreme Value Theorem guarantees existence of global maxima and minima.

## Examples

### Example 1: Finding Critical Points and Classification

Find and classify the critical points of f(x, y) = x³ + y³ - 3xy.

**Solution**:

**Step 1: Compute partial derivatives**

- fₓ = 3x² - 3y
- fᵧ = 3y² - 3x

**Step 2: Set partial derivatives to zero**

- 3x² - 3y = 0 ⇒ y = x²
- 3y² - 3x = 0 ⇒ x = y²

**Step 3: Solve the system**
Substituting y = x² into x = y²:
x = (x²)² = x⁴
x⁴ - x = 0
x(x³ - 1) = 0

So x = 0 or x = 1. When x = 0, y = 0² = 0. When x = 1, y = 1² = 1.
Critical points: (0, 0) and (1, 1)

**Step 4: Compute second derivatives**

- fₓₓ = 6x
- fᵧᵧ = 6y
- fₓᵧ = -3

**Step 5: Classify using Hessian**
At (0, 0): fₓₓ(0,0) = 0, fᵧᵧ(0,0) = 0, fₓᵧ = -3
det(H) = (0)(0) - (-3)² = -9 < 0 ⇒ Saddle point

At (1, 1): fₓₓ(1,1) = 6, fᵧᵧ(1,1) = 6, fₓᵧ = -3
det(H) = (6)(6) - (-3)² = 36 - 9 = 27 > 0
Since fₓₓ = 6 > 0, this is a local minimum.

### Example 2: Using Gradient for Optimization

Find the direction of steepest ascent for f(x, y) = xe^y at point (1, 0). Also find the maximum rate of change.

**Solution**:

**Step 1: Compute gradient**

- ∂f/∂x = e^y
- ∂f/∂y = xe^y
  ∇f = (e^y, xe^y)

**Step 2: Evaluate at (1, 0)**
∇f(1, 0) = (e^0, 1·e^0) = (1, 1)

**Step 3: Direction of steepest ascent**
The direction is given by the unit vector in the direction of ∇f:
||∇f|| = √(1² + 1²) = √2
Unit vector: (1/√2, 1/√2)

**Step 4: Maximum rate of change**
The maximum rate of change equals the magnitude of the gradient:
D_max = ||∇f(1,0)|| = √2

### Example 3: Constrained Optimization Setup

Find the point on the plane x + 2y + 3z = 6 closest to the origin using the method of Lagrange multipliers concept.

**Solution**:

We minimize the squared distance: f(x,y,z) = x² + y² + z²
Subject to constraint: g(x,y,z) = x + 2y + 3z - 6 = 0

**Setup Lagrange conditions**:
∇f = λ∇g
(2x, 2y, 2z) = λ(1, 2, 3)

This gives:
2x = λ ⇒ x = λ/2
2y = 2λ ⇒ y = λ
2z = 3λ ⇒ z = 3λ/2

Substitute into constraint:
(λ/2) + 2(λ) + 3(3λ/2) = 6
λ/2 + 2λ + 9λ/2 = 6
(λ + 4λ + 9λ)/2 = 6
14λ/2 = 6
7λ = 6
λ = 6/7

Thus:
x = 3/7, y = 6/7, z = 9/7

The closest point on the plane to the origin is (3/7, 6/7, 9/7).

## Exam Tips

1. **Remember the Hessian test for two variables**: For f(x,y), calculate Δ = fₓₓfᵧᵧ - (fₓᵧ)² at critical points. Positive with fₓₓ > 0 means minimum; positive with fₓₓ < 0 means maximum; negative means saddle point.

2. **Gradient points perpendicular to level curves**: This property helps verify gradient calculations and understand the geometric meaning of ∇f.

3. **For exam problems, check both critical points and boundary points**: Global extrema on closed domains require examining boundaries, not just interior critical points.

4. **Practice mixed partial derivative calculations**: Remember Clairaut's theorem for simplifying calculations when mixed partials are continuous.

5. **The Jacobian appears in change of variables**: For transformation (u,v) → (x,y), the area/scale factor is |∂(x,y)/∂(u,v)| = |det(J)|.

6. **Directional derivative formula D_u f = ∇f · u**: Always ensure u is a unit vector; if not, normalize it first.

7. **Lagrange multipliers setup**: For optimization with constraint g(x,y,z) = 0, solve ∇f = λ∇g along with the constraint equation.
