# Differentiation and Partial Differentials

## Table of Contents

- [Differentiation and Partial Differentials](#differentiation-and-partial-differentials)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Ordinary Differentiation](#1-ordinary-differentiation)
  - [2. Higher Order Derivatives](#2-higher-order-derivatives)
  - [3. Partial Differentiation](#3-partial-differentiation)
  - [4. Higher Order Partial Derivatives](#4-higher-order-partial-derivatives)
  - [5. Total Differentiation](#5-total-differentiation)
  - [6. Jacobian Matrix](#6-jacobian-matrix)
  - [7. Taylor Series Expansion](#7-taylor-series-expansion)
- [Examples](#examples)
  - [Example 1: Finding Critical Points using First and Second Derivatives](#example-1-finding-critical-points-using-first-and-second-derivatives)
  - [Example 2: Partial Differentiation](#example-2-partial-differentiation)
  - [Example 3: Total Differentiation with Constraint](#example-3-total-differentiation-with-constraint)
  - [Example 4: Taylor Series Expansion](#example-4-taylor-series-expansion)
- [Exam Tips](#exam-tips)

## Introduction

Differentiation and partial differentials form the mathematical foundation of optimization techniques in engineering. In the context of the BCS405C course, these concepts are essential for understanding how to find maximum and minimum values of functions, which is the core objective of any optimization problem. The ability to compute derivatives allows engineers to determine the rate of change of quantities with respect to variables, enabling them to analyze and design systems efficiently.

Partial differentiation extends the concept of derivatives to functions of multiple variables, where we examine how a function changes with respect to one variable while keeping other variables constant. This is particularly important in engineering optimization problems that typically involve multiple variables and constraints. For example, in designing an optimal container, we might need to minimize surface area while maximizing volume—two competing objectives that require partial differentiation to solve.

This module builds the necessary mathematical framework for subsequent topics in optimization, including single-variable and multi-variable optimization, Lagrange multipliers, and gradient descent methods. Mastery of these concepts is crucial for solving real-world engineering problems in areas such as design optimization, control systems, and resource allocation.

## Key Concepts

### 1. Ordinary Differentiation

Differentiation is the process of finding the derivative of a function, which represents the instantaneous rate of change of the function with respect to its variable. If y = f(x), the derivative is denoted as dy/dx or f'(x) and is defined as:

**f'(x) = lim[h→0] [f(x+h) - f(x)] / h**

The derivative has several geometric and physical interpretations. Geometrically, it represents the slope of the tangent line to the curve at a given point. Physically, it can represent velocity (rate of change of position with respect to time), acceleration (rate of change of velocity), or any instantaneous rate of change.

**Rules of Differentiation:**

- **Constant Rule:** d/dx(c) = 0, where c is a constant
- **Power Rule:** d/dx(xⁿ) = nxⁿ⁻¹
- **Sum/Difference Rule:** d/dx[f(x) ± g(x)] = f'(x) ± g'(x)
- **Product Rule:** d/dx[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)
- **Quotient Rule:** d/dx[f(x)/g(x)] = [f'(x)g(x) - f(x)g'(x)] / [g(x)]²
- **Chain Rule:** d/dx[f(g(x))] = f'(g(x)) × g'(x)

### 2. Higher Order Derivatives

The second derivative, denoted as f''(x) or d²y/dx², is the derivative of the first derivative. Higher order derivatives follow the same pattern. The second derivative is particularly important in optimization because it helps determine whether a critical point is a maximum or minimum:

- If f''(x) > 0 at a critical point, the function has a local minimum
- If f''(x) < 0 at a critical point, the function has a local maximum
- If f''(x) = 0, the test is inconclusive (could be inflection point)

### 3. Partial Differentiation

For functions of two or more variables, we use partial differentiation. If z = f(x, y), the partial derivative with respect to x treats y as a constant and differentiates with respect to x:

**∂f/∂x = lim[h→0] [f(x+h, y) - f(x, y)] / h**

Similarly, the partial derivative with respect to y treats x as constant:

**∂f/∂y = lim[h→0] [f(x, y+h) - f(x, y)] / h**

The partial derivatives ∂f/∂x and ∂f/∂y give the rate of change of f in the direction of the x-axis and y-axis respectively, holding the other variable constant.

### 4. Higher Order Partial Derivatives

Second-order partial derivatives include:

- **∂²f/∂x²**: Partial derivative with respect to x, twice
- **∂²f/∂y²**: Partial derivative with respect to y, twice
- **∂²f/∂x∂y**: Partial derivative first with respect to y, then x (mixed derivative)
- **∂²f/∂y∂x**: Partial derivative first with respect to x, then y

**Young's Theorem:** If the mixed partial derivatives are continuous, they are equal:
∂²f/∂x∂y = ∂²f/∂y∂x

### 5. Total Differentiation

For a function z = f(x, y), where both x and y are functions of a single variable t, the total derivative is:

**dz/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt)**

This concept is crucial in optimization when variables are related by constraints.

### 6. Jacobian Matrix

The Jacobian matrix is a matrix of all first-order partial derivatives of a vector-valued function. For f = (f₁, f₂, ..., fₘ) with variables (x₁, x₂, ..., xₙ):

**J = [∂fᵢ/∂xⱼ]** for i = 1 to m and j = 1 to n

The Jacobian determinant is used in coordinate transformations and in determining whether a system of equations can be solved using the implicit function theorem.

### 7. Taylor Series Expansion

The Taylor series provides a way to approximate functions using polynomials. For a single variable:

**f(x + h) = f(x) + hf'(x) + (h²/2!)f''(x) + (h³/3!)f'''(x) + ...**

For two variables (Maclaurin series expansion about origin):

**f(x, y) = f(0,0) + x∂f/∂x + y∂f/∂y + (x²/2)∂²f/∂x² + xy∂²f/∂x∂y + (y²/2)∂²f/∂y² + ...**

Taylor series is extensively used in optimization algorithms to find approximate solutions.

## Examples

### Example 1: Finding Critical Points using First and Second Derivatives

**Problem:** Find the local maxima and minima of f(x) = x³ - 3x² - 24x + 5

**Solution:**

**Step 1:** Find the first derivative
f'(x) = 3x² - 6x - 24

**Step 2:** Set f'(x) = 0 to find critical points
3x² - 6x - 24 = 0
Divide by 3: x² - 2x - 8 = 0
(x - 4)(x + 2) = 0
x = 4 or x = -2

**Step 3:** Find the second derivative
f''(x) = 6x - 6

**Step 4:** Evaluate second derivative at critical points
At x = 4: f''(4) = 6(4) - 6 = 18 > 0 → Local minimum
At x = -2: f''(-2) = 6(-2) - 6 = -18 < 0 → Local maximum

**Step 5:** Find function values at these points
f(4) = 4³ - 3(4)² - 24(4) + 5 = 64 - 48 - 96 + 5 = -75
f(-2) = (-2)³ - 3(-2)² - 24(-2) + 5 = -8 - 12 + 48 + 5 = 33

**Answer:** Local maximum at x = -2 with value 33, Local minimum at x = 4 with value -75

### Example 2: Partial Differentiation

**Problem:** If z = x³ + 2x²y - 3xy² + y³, find all first and second order partial derivatives.

**Solution:**

**First Order Partial Derivatives:**
∂z/∂x = 3x² + 4xy - 3y²
∂z/∂y = 2x² - 6xy + 3y²

**Second Order Partial Derivatives:**
∂²z/∂x² = ∂/∂x(3x² + 4xy - 3y²) = 6x + 4y
∂²z/∂y² = ∂/∂y(2x² - 6xy + 3y²) = -6x + 6y
∂²z/∂x∂y = ∂/∂y(3x² + 4xy - 3y²) = 4x - 6y
∂²z/∂y∂x = ∂/∂x(2x² - 6xy + 3y²) = 4x - 6y

Note: ∂²z/∂x∂y = ∂²z/∂y∂x (verified by Young's theorem)

### Example 3: Total Differentiation with Constraint

**Problem:** If z = x²y + xy², where x = t² and y = t + 1, find dz/dt at t = 1.

**Solution:**

**Step 1:** Find partial derivatives
∂z/∂x = 2xy + y²
∂z/∂y = x² + 2xy

**Step 2:** Find dx/dt and dy/dt
dx/dt = 2t
dy/dt = 1

**Step 3:** Apply total differentiation formula
dz/dt = (∂z/∂x)(dx/dt) + (∂z/∂y)(dy/dt)

**Step 4:** Evaluate at t = 1
At t = 1: x = 1² = 1, y = 1 + 1 = 2

∂z/∂x = 2(1)(2) + 2² = 4 + 4 = 8
∂z/∂y = 1² + 2(1)(2) = 1 + 4 = 5
dx/dt = 2(1) = 2
dy/dt = 1

dz/dt = (8)(2) + (5)(1) = 16 + 5 = 21

**Answer:** dz/dt at t = 1 is 21

### Example 4: Taylor Series Expansion

**Problem:** Find the Taylor series expansion of f(x) = eˣ about x = 0 up to the third term.

**Solution:**

For eˣ, we know that at x = 0, f(0) = 1, f'(0) = 1, f''(0) = 1, f'''(0) = 1

Using Taylor series: f(x) ≈ f(0) + xf'(0) + (x²/2!)f''(0) + (x³/3!)f'''(0)

f(x) ≈ 1 + x + (x²/2) + (x³/6)

This is the Maclaurin series for eˣ, which is actually infinite. The approximation becomes more accurate as we include more terms.

## Exam Tips

1. **Memorize all differentiation rules**: The product rule, quotient rule, and chain rule are frequently tested. Write these down immediately when solving problems to avoid mistakes.

2. **Understand the difference between ordinary and partial derivatives**: In exam questions, carefully identify whether you're dealing with a function of one variable or multiple variables.

3. **Second derivative test is crucial**: Always remember that f''(x) > 0 indicates minimum and f''(x) < 0 indicates maximum at critical points where f'(x) = 0.

4. **Check continuity of mixed partial derivatives**: When verifying Young's theorem (∂²f/∂x∂y = ∂²f/∂y∂x), remember this holds only when the derivatives are continuous.

5. **Practice total differentiation problems**: These often appear in exam questions involving parametric equations or related rates problems.

6. **Be careful with notation**: Understand that ∂z/∂x and dz/dx mean different things—the partial derivative holds other variables constant while the total derivative accounts for indirect dependence.

7. **Know how to find critical points**: Set first derivative(s) to zero and solve for the variable(s). These are candidates for maxima or minima.

8. **Taylor series applications**: Understand how to compute up to second-order terms for approximating functions near a point—this is foundational for understanding optimization algorithms.
