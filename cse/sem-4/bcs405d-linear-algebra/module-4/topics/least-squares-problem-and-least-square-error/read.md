# Least Squares Problem and Least Square Error

## Table of Contents

- [Least Squares Problem and Least Square Error](#least-squares-problem-and-least-square-error)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. The Least Squares Problem](#1-the-least-squares-problem)
  - [2. Geometric Interpretation](#2-geometric-interpretation)
  - [3. Existence and Uniqueness](#3-existence-and-uniqueness)
  - [4. Methods for Solving Least Squares](#4-methods-for-solving-least-squares)
  - [5. Least Square Error](#5-least-square-error)
  - [6. Pseudoinverse](#6-pseudoinverse)
  - [7. Weighted Least Squares](#7-weighted-least-squares)
  - [8. Linear Regression Connection](#8-linear-regression-connection)
- [Examples](#examples)
  - [Example 1: Solving via Normal Equations](#example-1-solving-via-normal-equations)
  - [Example 2: Fitting a Straight Line](#example-2-fitting-a-straight-line)
  - [Example 3: Using QR Decomposition](#example-3-using-qr-decomposition)
- [Exam Tips](#exam-tips)

## Introduction

The least squares problem is one of the most fundamental concepts in numerical linear algebra and applied mathematics. It arises when we have a system of linear equations Ax = b where no exact solution exists, typically when the system is overdetermined (more equations than unknowns). In such cases, we seek an approximate solution that minimizes the total error between the observed data and the model predictions.

This topic is crucial for CSE students as it has extensive applications in data fitting, curve fitting, signal processing, machine learning, and engineering problems. The method of least squares provides a systematic approach to finding the "best fit" solution that minimizes the sum of squared residuals, making it invaluable for analyzing experimental data and building predictive models.

The mathematical foundation of least squares lies in the concept of orthogonal projections and the four fundamental subspaces of a matrix. Understanding this topic equips students with powerful tools for solving real-world optimization problems where exact solutions are impossible or unnecessary.

## Key Concepts

### 1. The Least Squares Problem

Given an m×n matrix A (with m ≥ n) and a vector b ∈ ℝᵐ, the least squares problem seeks a vector x ∈ ℝⁿ such that Ax ≈ b in the sense of minimizing the Euclidean norm of the residual vector r = b - Ax.

**Mathematical Formulation:**
Find x that minimizes ‖b - Ax‖²

The solution satisfies the **normal equations**: AᵀAx = Aᵀb

### 2. Geometric Interpretation

The least squares solution x̂ corresponds to the orthogonal projection of b onto the column space of A. The residual vector r = b - Ax̂ is orthogonal to every column of A (and hence to Col(A)). This geometric interpretation is key to understanding why the normal equations work.

### 3. Existence and Uniqueness

- If rank(A) = n (full column rank), a unique least squares solution exists
- If rank(A) < n (rank deficient), infinitely many solutions exist; we typically find the minimum norm solution
- The matrix AᵀA is invertible if and only if rank(A) = n

### 4. Methods for Solving Least Squares

**Method 1: Normal Equations**
x̂ = (AᵀA)⁻¹Aᵀb

**Method 2: QR Decomposition**
If A = QR where Q has orthonormal columns and R is upper triangular, then:
x̂ = R⁻¹Qᵀb (since QᵀQ = I)

**Method 3: Singular Value Decomposition (SVD)**
If A = UΣVᵀ, then:
x̂ = VΣ⁺Uᵀb
where Σ⁺ is the pseudoinverse (reciprocals of non-zero singular values)

### 5. Least Square Error

The least square error (LSE) or residual error is given by:
‖r‖² = ‖b - Ax̂‖²

This represents the sum of squared differences between observed and predicted values. The minimum value of this error quantifies how well the model fits the data.

### 6. Pseudoinverse

The Moore-Penrose pseudoinverse A⁺ provides a general solution:

- If Ax = b has a solution, A⁺b gives the unique solution
- If no solution exists, A⁺b gives the least squares solution
- A⁺ = (AᵀA)⁻¹Aᵀ when A has full column rank

### 7. Weighted Least Squares

When observations have different reliability levels, we minimize:
‖W¹ᐟ²(b - Ax)‖² where W is a diagonal weight matrix

### 8. Linear Regression Connection

In statistics, least squares is the basis for linear regression. For data points (xᵢ, yᵢ), fitting y = β₀ + β₁x involves:

- Design matrix A with columns [1, xᵢ]
- Response vector b = yᵢ
- Coefficients β = (AᵀA)⁻¹Aᵀb

## Examples

### Example 1: Solving via Normal Equations

**Problem:** Find the least squares solution for A = [[1, 1], [1, 2], [1, 3]] and b = [1, 2, 3]ᵀ

**Solution:**

Step 1: Compute AᵀA
AᵀA = [[1, 1, 1], [1, 2, 3]]ᵀ × [[1, 1], [1, 2], [1, 3]]
= [[3, 6], [6, 14]]

Step 2: Compute Aᵀb
Aᵀb = [[1, 1, 1], [1, 2, 3]]ᵀ × [1, 2, 3]ᵀ
= [6, 14]ᵀ

Step 3: Solve normal equations AᵀAx = Aᵀb
[[3, 6], [6, 14]][x₁, x₂]ᵀ = [6, 14]ᵀ

Using Cramer's rule or substitution:
3x₁ + 6x₂ = 6 → x₁ + 2x₂ = 2
6x₁ + 14x₂ = 14 → 3x₁ + 7x₂ = 7

From first: x₁ = 2 - 2x₂
Substitute: 3(2 - 2x₂) + 7x₂ = 7
6 - 6x₂ + 7x₂ = 7
6 + x₂ = 7
x₂ = 1, x₁ = 0

**Answer:** x̂ = [0, 1]ᵀ

### Example 2: Fitting a Straight Line

**Problem:** Fit a straight line y = mx + c to data points (1, 1), (2, 2), (3, 2.5)

**Solution:**

A = [[1, 1], [1, 2], [1, 3]], b = [1, 2, 2.5]ᵀ

AᵀA = [[3, 6], [6, 14]], Aᵀb = [5.5, 14]ᵀ

Solve: [[3, 6], [6, 6]][m, c]ᵀ = [5.5, 14]ᵀ

3m + 6c = 5.5 → m + 2c = 1.833
6m + 14c = 14 → 3m + 7c = 7

From first: m = 1.833 - 2c
3(1.833 - 2c) + 7c = 7
5.5 - 6c + 7c = 7
5.5 + c = 7
c = 1.5, m = 1.833 - 3 = -1.167

**Answer:** y = -1.167x + 1.5

### Example 3: Using QR Decomposition

**Problem:** Solve least squares using QR for A = [[1, 0], [1, 1], [0, 1]], b = [1, 2, 1]ᵀ

**Solution:**

Given A has orthonormal columns after QR factorization:
Let Q = [[1/√2, 0], [1/√2, 1/√2], [0, 1/√2]]
R = [[√2, 1/√2], [0, 1/√2]]

Then x̂ = R⁻¹Qᵀb
Qᵀb = [ (1+2)/√2, (2+1)/√2 ]ᵀ = [3/√2, 3/√2]ᵀ
R⁻¹ = [[1/√2, -1], [0, √2]]

x̂ = [ (3/√2)(1/√2) + 3/√2(-1), (3/√2)(0) + (3/√2)(√2) ]ᵀ
= [ 3/2 - 3/√2, 3 ]ᵀ
≈ [-0.621, 3]ᵀ

**Answer:** x̂ ≈ [-0.621, 3]ᵀ

## Exam Tips

1. **Remember the normal equations:** AᵀAx̂ = Aᵀb is the cornerstone equation for all least squares problems in university exams.

2. **Check rank conditions:** Always verify if A has full column rank before claiming uniqueness of the solution.

3. **Geometric interpretation matters:** The residual vector is orthogonal to Col(A)—this is frequently tested in exams.

4. **Know when to use each method:** Normal equations for small problems, QR for numerical stability, SVD for rank-deficient cases.

5. **Pseudoinverse shortcut:** For full rank matrices, A⁺ = (AᵀA)⁻¹Aᵀ—memorize this formula.

6. **Error calculation:** The minimum squared error equals ‖b‖² - ‖Ax̂‖² = ‖b‖² - (x̂ᵀAᵀAx̂).

7. **Connection to projections:** The projection matrix P = A(AᵀA)⁻¹Aᵀ projects b onto the column space; always remember this.

8. **Practice matrix operations:** Most errors in exams come from matrix multiplication mistakes—practice AᵀA and Aᵀb calculations thoroughly.
