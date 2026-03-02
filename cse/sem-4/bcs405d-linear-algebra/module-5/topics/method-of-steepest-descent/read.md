# Method of Steepest Descent

## Table of Contents

- [Method of Steepest Descent](#method-of-steepest-descent)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Relationship Between Linear Systems and Optimization](#1-relationship-between-linear-systems-and-optimization)
  - [2. The Gradient and Steepest Descent Direction](#2-the-gradient-and-steepest-descent-direction)
  - [3. The Iteration Formula](#3-the-iteration-formula)
  - [4. Optimal Step Size Derivation](#4-optimal-step-size-derivation)
  - [5. Convergence Analysis](#5-convergence-analysis)
  - [6. Algorithm Summary](#6-algorithm-summary)
- [Examples](#examples)
  - [Example 1: Solving a 2×2 System](#example-1-solving-a-22-system)
  - [Example 2: Finding Minimum of Quadratic Function](#example-2-finding-minimum-of-quadratic-function)
- [Exam Tips](#exam-tips)

## Introduction

The Method of Steepest Descent is a fundamental iterative optimization technique used to find the minimum of a function, particularly quadratic functions. In the context of Linear Algebra, this method serves as an important numerical technique for solving systems of linear equations where the coefficient matrix is symmetric and positive definite. The method derives its name from the fact that at each iteration, the search direction is chosen as the direction of steepest descent—that is, the direction in which the function decreases most rapidly.

The significance of the steepest descent method in engineering mathematics cannot be overstated. It forms the foundation for more advanced iterative methods like the Conjugate Gradient method, which is widely used in scientific computing and engineering applications. For students studying Linear Algebra, understanding this method is crucial as it provides insight into numerical linear algebra, optimization theory, and the solution of large sparse systems of equations that arise in practical engineering problems.

The method is particularly valuable because it transforms the problem of solving a linear system Ax = b into an equivalent optimization problem of minimizing a quadratic function. This transformation allows us to leverage the elegant mathematics of convex optimization to develop efficient numerical solution techniques.

## Key Concepts

### 1. Relationship Between Linear Systems and Optimization

For a symmetric positive definite (SPD) matrix A and a vector b, we define the quadratic function:

f(x) = (1/2)x^T A x - b^T x

This function has a unique minimum, and at this minimum point, the gradient equals zero, which gives us:

∇f(x) = Ax - b = 0

Thus, solving Ax = b is equivalent to minimizing f(x).

### 2. The Gradient and Steepest Descent Direction

The gradient of f(x) is given by:
∇f(x) = Ax - b

At any point x_k, the direction of steepest descent is given by the negative gradient:
d_k = -∇f(x_k) = b - Ax_k

This residual vector r_k = b - Ax_k represents how far we are from satisfying the linear system.

### 3. The Iteration Formula

Starting from an initial guess x_0, the steepest descent method generates a sequence of iterates:

x\_{k+1} = x_k + α_k d_k

where α_k is the step size (learning rate) chosen to minimize f(x_k + α d_k).

### 4. Optimal Step Size Derivation

To find the optimal step size, we minimize f(x_k + α d_k) with respect to α:

f(x_k + α d_k) = f(x_k + α(b - Ax_k))

Taking derivative with respect to α and setting it to zero:

d/dα [f(x_k + α d_k)] = d_k^T (Ax_k + αAd_k - b) = 0

Solving for α_k:
α_k = (d_k^T d_k) / (d_k^T A d_k) = (r_k^T r_k) / (r_k^T A r_k)

### 5. Convergence Analysis

The method exhibits linear convergence. The convergence rate depends on the condition number κ(A) of the matrix A:

||x*k - x^*||\_A ≤ (κ(A) - 1)/(κ(A) + 1))^k ||x*0 - x^*||\_A

where the A-norm is defined as ||x||\_A = sqrt(x^T A x).

For well-conditioned matrices (small κ(A)), convergence is rapid, but for ill-conditioned matrices, convergence can be very slow.

### 6. Algorithm Summary

1. Choose initial guess x_0
2. Compute initial residual r_0 = b - Ax_0
3. For k = 0, 1, 2, ... until convergence:

- Compute step size: α_k = (r_k^T r_k) / (r_k^T A r_k)
- Update solution: x\_{k+1} = x_k + α_k r_k
- Compute new residual: r\_{k+1} = r_k - α_k A r_k

## Examples

### Example 1: Solving a 2×2 System

Solve the system Ax = b using the method of steepest descent, where:
A = [[4, 1], [1, 3]] and b = [1, 2]

**Solution:**

**Step 1:** Define f(x) = (1/2)x^T A x - b^T x

**Step 2:** Start with initial guess x_0 = [0, 0]^T

**Step 3:** Compute initial residual:
r_0 = b - Ax_0 = [1, 2] - [[4, 1], [1, 3]][0, 0] = [1, 2]

**Iteration 1:**
α_0 = (r_0^T r_0) / (r_0^T A r_0) = ([1, 2] · [1, 2]) / ([1, 2] · A · [1, 2])

r_0^T r_0 = 1 + 4 = 5

A r_0 = [[4, 1], [1, 3]][1, 2] = [6, 7]

r_0^T A r_0 = [1, 2] · [6, 7] = 6 + 14 = 20

α_0 = 5/20 = 0.25

x_1 = x_0 + α_0 r_0 = [0, 0] + 0.25[1, 2] = [0.25, 0.5]

**Iteration 2:**
r_1 = b - Ax_1 = [1, 2] - [[4, 1], [1, 3]][0.25, 0.5] = [1, 2] - [1.5, 1.75] = [-0.5, 0.25]

α_1 = (r_1^T r_1) / (r_1^T A r_1) = (0.25 + 0.0625) / ([-0.5, 0.25] · A · [-0.5, 0.25])

r_1^T r_1 = 0.3125

A r_1 = [[4, 1], [1, 3]][-0.5, 0.25] = [-1.75, 0.25]

r_1^T A r_1 = [-0.5, 0.25] · [-1.75, 0.25] = 0.875 + 0.0625 = 0.9375

α_1 = 0.3125/0.9375 ≈ 0.3333

x_2 = x_1 + α_1 r_1 = [0.25, 0.5] + 0.3333[-0.5, 0.25] = [0.0833, 0.5833]

Continuing this process converges to the solution x ≈ [0.0714, 0.5714].

### Example 2: Finding Minimum of Quadratic Function

Find the minimum of f(x_1, x_2) = 2x_1² + x_2² - x_1x_2 - x_1 - x_2

**Solution:**

Write in matrix form: A = [[2, -1], [-1, 1]], b = [1, 1]

Note: f(x) = (1/2)x^T A x - b^T x

Starting with x_0 = [0, 0]:

r_0 = b - Ax_0 = [1, 1]

α_0 = (r_0^T r_0)/(r_0^T A r_0) = 2/( [1,1] · [[1,0],[0,1]] · [1,1] ) = 2/2 = 1

x_1 = x_0 + α_0 r_0 = [1, 1]

r_1 = b - Ax_1 = [1, 1] - [[2, -1], [-1, 1]][1, 1] = [1, 1] - [1, 0] = [0, 1]

α_1 = (r_1^T r_1)/(r_1^T A r_1) = 1/( [0,1] · [[2, -1], [-1, 1]] · [0,1] ) = 1/1 = 1

x_2 = x_1 + α_1 r_1 = [1, 1] + [0, 1] = [1, 2]

r_2 = b - Ax_2 = [1, 1] - [[2, -1], [-1, 1]][1, 2] = [1, 1] - [0, 1] = [1, 0]

The method oscillates between residuals [1, 0] and [0, 1], converging slowly due to the condition number of A.

## Exam Tips

1. **Remember the key equivalence**: Solving Ax = b (with SPD A) is equivalent to minimizing f(x) = (1/2)x^T Ax - b^T x.

2. **Always compute the step size using the formula**: α_k = (r_k^T r_k)/(r_k^T A r_k), not arbitrary values.

3. **The search direction is the negative gradient**: d_k = -∇f(x_k) = b - Ax_k = r_k (the residual).

4. **Know the convergence formula**: The error in A-norm reduces by factor (κ-1)/(κ+1) each iteration, where κ is the condition number.

5. **Understand when to use this method**: It works best for well-conditioned SPD systems; for ill-conditioned systems, consider preconditioning or other methods.

6. **The residual update formula**: r\_{k+1} = r_k - α_k A r_k can be used instead of recomputing to save operations.

7. **Convergence criterion**: Check if ||r_k|| < ε or when the change in solution becomes small.

8. **Connection to Conjugate Gradient**: The Method of Steepest Descent uses orthogonal search directions, while Conjugate Gradient uses A-conjugate directions for faster convergence.
