# Useful Identities for Computing Gradients

## Table of Contents

- [Useful Identities for Computing Gradients](#useful-identities-for-computing-gradients)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Gradient of a Scalar Function](#1-gradient-of-a-scalar-function)
  - [2. Product Rule for Gradients](#2-product-rule-for-gradients)
  - [3. Chain Rule for Gradients](#3-chain-rule-for-gradients)
  - [4. Gradient of Quadratic Forms](#4-gradient-of-quadratic-forms)
  - [5. Gradient of Vector-Norm Functions](#5-gradient-of-vector-norm-functions)
  - [6. Jacobian Matrix](#6-jacobian-matrix)
  - [7. Hessian Matrix](#7-hessian-matrix)
  - [8. Useful Vector Calculus Identities](#8-useful-vector-calculus-identities)
  - [9. Directional Derivative](#9-directional-derivative)
  - [10. Matrix-Vector Gradient Identities](#10-matrix-vector-gradient-identities)
- [Examples](#examples)
  - [Example 1: Gradient of a Quadratic Function](#example-1-gradient-of-a-quadratic-function)
  - [Example 2: Gradient Descent Update Using Identities](#example-2-gradient-descent-update-using-identities)
  - [Example 3: Gradient of Composite Function](#example-3-gradient-of-composite-function)
- [Exam Tips](#exam-tips)

## Introduction

In the field of optimization techniques, gradients play a fundamental role in understanding how functions change and in developing algorithms to find optimal solutions. The gradient of a function points in the direction of the steepest ascent, and its magnitude indicates the rate of change. Computing gradients accurately and efficiently is essential for various optimization methods, particularly gradient descent algorithms used in machine learning and numerical optimization.

This topic covers the essential mathematical identities and techniques used to compute gradients of scalar and vector functions. These identities simplify complex differentiation problems and provide systematic approaches to finding partial derivatives. Understanding these identities is crucial for solving optimization problems, as they form the foundation for analyzing multidimensional functions and their behavior near critical points.

The study of gradient identities is particularly important for CSE students because optimization techniques are extensively used in algorithms, data science, and computational mathematics. These mathematical tools enable engineers to develop efficient algorithms and analyze the convergence properties of optimization methods.

## Key Concepts

### 1. Gradient of a Scalar Function

The gradient of a scalar function f(x₁, x₂, ..., xₙ) with respect to the vector x = [x₁, x₂, ..., xₙ]ᵀ is defined as:

∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]ᵀ

The gradient operator ∇ (del operator) in n-dimensional space is:
∇ = [∂/∂x₁, ∂/∂x₂, ..., ∂/∂xₙ]ᵀ

### 2. Product Rule for Gradients

For two scalar functions f(x) and g(x):
∇(fg) = f∇g + g∇f

For vector-valued functions, if F(x) and G(x) are vector functions:
∇(F·G) = F × (∇ × G) + G × (∇ × F) + (F · ∇)G + (G · ∇)F

### 3. Chain Rule for Gradients

If y = f(u) and u = g(x), then:
∇ₓf(g(x)) = f'(u) · ∇ₓu

For composite vector functions:
∇ₓ(f ∘ g)(x) = ∇u f(u) · ∇ₓg(x)

### 4. Gradient of Quadratic Forms

For a symmetric matrix A and vector x:
∇(xᵀAx) = (A + Aᵀ)x = 2Ax (when A is symmetric)

This identity is extensively used in quadratic optimization problems.

### 5. Gradient of Vector-Norm Functions

- ∇(‖x‖²) = ∇(xᵀx) = 2x
- ∇(‖x‖) = x/‖x‖ for x ≠ 0
- ∇(1/‖x‖) = -x/‖x‖³ for x ≠ 0

### 6. Jacobian Matrix

For a vector function F(x) = [f₁(x), f₂(x), ..., fₘ(x)]ᵀ mapping from ℝⁿ to ℝᵐ, the Jacobian matrix J is:
J = ∂F/∂x = [[∂f₁/∂x₁, ..., ∂f₁/∂xₙ], ..., [∂fₘ/∂x₁, ..., ∂fₘ/∂xₙ]]

### 7. Hessian Matrix

The Hessian of a scalar function f(x) is the matrix of second-order partial derivatives:
H = ∇²f = ∂²f/∂xᵢ∂xⱼ

For twice-differentiable functions, the Hessian is symmetric if continuous second derivatives exist.

### 8. Useful Vector Calculus Identities

- ∇(a · x) = a (where a is constant vector)
- ∇(x · a) = a
- ∇(‖x - a‖²) = 2(x - a)
- ∇ᵤ(xᵀu) = x (with respect to u, treating x as constant)

### 9. Directional Derivative

The directional derivative of f at point x in direction d (unit vector) is:
Dₐf = ∇f · a

This represents the rate of change of f in the direction a.

### 10. Matrix-Vector Gradient Identities

For matrix A (constant), vector x:

- ∇ₓ(bᵀx) = b
- ∇ₓ(xᵀb) = b
- ∇ₓ(xᵀAx) = (A + Aᵀ)x

## Examples

### Example 1: Gradient of a Quadratic Function

Find the gradient of f(x) = xᵀQx + cᵀx + d, where Q is a symmetric n×n matrix, c is an n×1 vector, and d is a scalar constant.

**Solution:**

We need to find ∇f(x).

Using the identities:

- ∇(d) = 0 (gradient of constant is zero)
- ∇(cᵀx) = c (gradient of linear term)
- ∇(xᵀQx) = 2Qx (since Q is symmetric)

Therefore:
∇f(x) = 2Qx + c

This is the gradient of a quadratic function commonly used in optimization.

### Example 2: Gradient Descent Update Using Identities

Given f(x₁, x₂) = x₁² + 2x₂² - 2x₁x₂ + x₁ - 3x₂, find the gradient and perform one iteration of gradient descent starting from x₀ = [1, 1]ᵀ with learning rate α = 0.1.

**Solution:**

First, compute partial derivatives:
∂f/∂x₁ = 2x₁ - 2x₂ + 1
∂f/∂x₂ = 4x₂ - 2x₁ - 3

At x₀ = [1, 1]ᵀ:
∂f/∂x₁ = 2(1) - 2(1) + 1 = 1
∂f/∂x₂ = 4(1) - 2(1) - 3 = -1

So ∇f(x₀) = [1, -1]ᵀ

Gradient descent update:
x₁ = x₀ - α∇f(x₀)
x₁ = [1, 1]ᵀ - 0.1 × [1, -1]ᵀ
x₁ = [1 - 0.1, 1 + 0.1]ᵀ
x₁ = [0.9, 1.1]ᵀ

### Example 3: Gradient of Composite Function

Find ∇f(x) where f(x) = exp(-‖x‖²/2) (Gaussian function)

**Solution:**

Let g(x) = ‖x‖² = xᵀx
Let h(u) = exp(-u/2)

We have f(x) = h(g(x))

Using chain rule:
∇f(x) = h'(g(x)) · ∇g(x)

Now:
h'(u) = -1/2 × exp(-u/2) = -1/2 × h(u)
∇g(x) = ∇(xᵀx) = 2x

Therefore:
∇f(x) = (-1/2) × exp(-‖x‖²/2) × 2x
∇f(x) = -x × exp(-‖x‖²/2)
∇f(x) = -x · f(x)

This shows that the gradient of the Gaussian points radially inward, proportional to the function value.

## Exam Tips

1. **Remember the gradient definition**: ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]ᵀ is the first thing to write when solving gradient problems.

2. **Quadratic form gradient**: For xᵀAx, always check if A is symmetric. If A is symmetric, ∇(xᵀAx) = 2Ax; otherwise, use (A + Aᵀ)x.

3. **Chain rule application**: When dealing with composite functions, identify the inner and outer functions clearly before applying the chain rule.

4. **Matrix dimensions**: Always verify that your gradient dimensions match your variable dimensions. A gradient with respect to an n-dimensional vector should be n×1.

5. **Hessian symmetry**: For continuous second derivatives, the Hessian matrix is symmetric (Clairaut's theorem). Use this property to verify your second-order partial derivatives.

6. **Directional derivative**: Remember Dₐf = ∇f · a gives the rate of change in direction a. This is frequently tested in exams.

7. **Learning rate in gradient descent**: When asked to perform gradient descent iterations, show all steps clearly and use the update formula xₖ₊₁ = xₖ - α∇f(xₖ).

8. **Common functions to memorize**: Gradients of ‖x‖², 1/‖x‖, exp(x), log(x) frequently appear in optimization problems.

9. **Critical points**: Set ∇f = 0 to find critical points. These are candidates for local minima, maxima, or saddle points.

10. **Practice partial derivatives**: Many gradient computation errors come from mistakes in basic partial differentiation. Practice computing ∂f/∂xᵢ for various functions.
