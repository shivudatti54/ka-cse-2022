# Gradients of Vector-Valued Functions

## Introduction

In the study of optimization techniques, understanding how to work with functions that map multiple input variables to multiple output variables is essential. Vector-valued functions represent a crucial generalization of scalar functions, where instead of producing a single scalar output, the function produces a vector output. The gradient of a vector-valued function extends the concept of derivatives to multivariable contexts and plays a fundamental role in optimization algorithms, particularly in gradient descent methods and Newton's method for multivariate optimization.

The gradient essentially captures the rate of change of a function with respect to each of its input variables. For scalar functions, the gradient is a vector pointing in the direction of steepest ascent. For vector-valued functions, we deal with Jacobian matrices that contain all first-order partial derivatives. This mathematical framework is indispensable for solving constrained and unconstrained optimization problems in engineering, economics, machine learning, and scientific computing.

In the context of the university's Optimization Techniques course, mastering gradients of vector-valued functions enables students to understand advanced optimization algorithms, sensitivity analysis, and the mathematical foundations of machine learning algorithms like gradient descent and backpropagation.

## Key Concepts

### 1. Vector-Valued Functions

A vector-valued function f: ℝⁿ → ℝᵐ maps each point x ∈ ℝⁿ to a vector f(x) ∈ ℝᵐ. We can write:

f(x) = [f₁(x), f₂(x), ..., fₘ(x)]ᵀ

where each fᵢ: ℝⁿ → ℝ is a scalar function called the ith component function. The domain is ℝⁿ and the codomain is ℝᵐ.

**Example:** f: ℝ² → ℝ³ defined by f(x₁, x₂) = [x₁² + x₂, sin(x₁), x₁x₂]ᵀ

Here, f₁(x) = x₁² + x₂, f₂(x) = sin(x₁), f₃(x) = x₁x₂

### 2. Jacobian Matrix

The Jacobian matrix is the matrix of all first-order partial derivatives of a vector-valued function. For f: ℝⁿ → ℝᵐ, the Jacobian J ∈ ℝᵐˣⁿ is defined as:

J(f)(x) = ∂f/∂x = [∂fᵢ/∂xⱼ] for i = 1, 2, ..., m and j = 1, 2, ..., n

The Jacobian matrix has m rows (one for each output component) and n columns (one for each input variable):

```
J = | ∂f₁/∂x₁ ∂f₁/∂x₂ ... ∂f₁/∂xₙ |
 | ∂f₂/∂x₁ ∂f₂/∂x₂ ... ∂f₂/∂xₙ |
 | ... |
 | ∂fₘ/∂x₁ ∂fₘ/∂x₂ ... ∂fₘ/∂xₙ |
```

### 3. Gradient of Scalar Functions (Special Case)

When m = 1 (single output), the vector-valued function becomes a scalar function f: ℝⁿ → ℝ. In this case, the Jacobian reduces to a single row, which is the transpose of the gradient:

∇f(x) = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]ᵀ

The gradient has the following properties:

- Points in the direction of steepest ascent
- Is orthogonal to level curves (in 2D) or level surfaces (in higher dimensions)
- The directional derivative in direction u is ∇f · u

### 4. Chain Rule for Vector-Valued Functions

If we have composition of functions: h(x) = g(f(x)), where f: ℝⁿ → ℝᵐ and g: ℝᵐ → ℝᵖ, the Jacobian of h is the matrix product of the Jacobians:

J(h)(x) = J(g)(f(x)) · J(f)(x)

This is crucial for backpropagation in neural networks and sensitivity analysis.

### 5. Hessian Matrix

For twice-differentiability, we consider second-order derivatives. The Hessian matrix of a scalar function f: ℝⁿ → ℝ is an n×n symmetric matrix:

H(f)(x) = ∇²f(x) = [∂²f/∂xᵢ∂xⱼ]

The Hessian captures curvature information and is essential for Newton's method:

- If H is positive definite at a point, the function is locally convex
- Newton's update: xₖ₊₁ = xₖ - H⁻¹∇f(xₖ)

### 6. Matrix-Vector Products with Jacobian

For computational efficiency, we often need to compute J·v where J is the Jacobian and v is a vector. This can be done without explicitly computing all partial derivatives using directional derivatives:

(J·v)ᵢ = lim(h→0) [fᵢ(x + hv) - fᵢ(x)]/h

This is called the Jacobian-vector product and is computationally efficient.

## Examples

### Example 1: Computing the Jacobian Matrix

**Problem:** Find the Jacobian matrix for f: ℝ³ → ℝ² defined by:
f(x₁, x₂, x₃) = [x₁x₂ + x₃², sin(x₁) + cos(x₂)]ᵀ

**Solution:**

Step 1: Identify the component functions

- f₁(x) = x₁x₂ + x₃²
- f₂(x) = sin(x₁) + cos(x₂)

Step 2: Compute all partial derivatives

For f₁:

- ∂f₁/∂x₁ = x₂
- ∂f₁/∂x₂ = x₁
- ∂f₁/∂x₃ = 2x₃

For f₂:

- ∂f₂/∂x₁ = cos(x₁)
- ∂f₂/∂x₂ = -sin(x₂)
- ∂f₂/∂x₃ = 0

Step 3: Form the Jacobian matrix

```
J = | x₂ x₁ 2x₃ |
 | cos(x₁) -sin(x₂) 0 |
```

This is the complete Jacobian matrix.

### Example 2: Gradient Descent Using Gradient Computation

**Problem:** Find the minimum of f(x₁, x₂) = x₁² + 2x₂² - 4x₁ - 4x₂ using gradient descent with starting point (3, 3) and learning rate α = 0.1. Perform 3 iterations.

**Solution:**

Step 1: Compute the gradient ∇f(x₁, x₂)

- ∂f/∂x₁ = 2x₁ - 4
- ∂f/∂x₂ = 4x₂ - 4

So, ∇f(x) = [2x₁ - 4, 4x₂ - 4]ᵀ

Step 2: Iteration 1 (x⁰ = [3, 3]ᵀ)

- ∇f(x⁰) = [2(3)-4, 4(3)-4]ᵀ = [2, 8]ᵀ
- x¹ = x⁰ - α∇f(x⁰) = [3, 3]ᵀ - 0.1[2, 8]ᵀ = [3-0.2, 3-0.8]ᵀ = [2.8, 2.2]ᵀ

Step 3: Iteration 2 (x¹ = [2.8, 2.2]ᵀ)

- ∇f(x¹) = [2(2.8)-4, 4(2.2)-4]ᵀ = [1.6, 4.8]ᵀ
- x² = [2.8, 2.2]ᵀ - 0.1[1.6, 4.8]ᵀ = [2.8-0.16, 2.2-0.48]ᵀ = [2.64, 1.72]ᵀ

Step 4: Iteration 3 (x² = [2.64, 1.72]ᵀ)

- ∇f(x²) = [2(2.64)-4, 4(1.72)-4]ᵀ = [1.28, 2.88]ᵀ
- x³ = [2.64, 1.72]ᵀ - 0.1[1.28, 2.88]ᵀ = [2.64-0.128, 1.72-0.288]ᵀ = [2.512, 1.432]ᵀ

After 3 iterations, we approach the minimum at (2, 1) where ∇f = [0, 0]ᵀ.

### Example 3: Chain Rule Application

**Problem:** Let g: ℝ² → ℝ be defined by g(u₁, u₂) = u₁² + u₂², and u = f(x) where f: ℝ → ℝ² is f(x) = [x, x²]ᵀ. Find the derivative of h(x) = g(f(x)) using the chain rule.

**Solution:**

Step 1: Identify the functions

- f(x) = [x, x²]ᵀ → f₁(x) = x, f₂(x) = x²
- g(u₁, u₂) = u₁² + u₂²

Step 2: Compute individual Jacobians

- J(f)(x) = [df₁/dx, df₂/dx] = [1, 2x] (1×2 matrix)
- ∇g(u) = [∂g/∂u₁, ∂g/∂u₂] = [2u₁, 2u₂]

Step 3: Apply chain rule
h'(x) = ∇g(f(x)) · f'(x) = [2x, 2x²] · [1, 2x] = 2x(1) + 2x²(2x) = 2x + 4x³

Step 4: Verify by direct computation
h(x) = g(f(x)) = g(x, x²) = x² + (x²)² = x² + x⁴
h'(x) = 2x + 4x³ ✓

## Exam Tips

1. **Remember the Jacobian structure**: The Jacobian matrix has m rows (outputs) and n columns (inputs). Students often confuse the orientation; always verify dimensions before writing.

2. **Gradient is the transpose of Jacobian for scalar functions**: When dealing with f: ℝⁿ → ℝ, remember that ∇f = (∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ)ᵀ, which is Jᵀ.

3. **Chain rule requires matrix multiplication**: For compositions, J(h) = J(g) × J(f), not element-wise multiplication. Check dimension compatibility.

4. ** Hessian is symmetric for scalar functions**: The Hessian matrix Hᵢⱼ = ∂²f/∂xᵢ∂xⱼ is symmetric if second-order partial derivatives are continuous (Clairaut's theorem).

5. **Use Jacobian-vector products for efficiency**: In exams, if asked about computational complexity, remember that computing J·v can be done with O(m) function evaluations rather than O(mn) partial derivatives.

6. **Gradient descent updates**: For minimization, xₖ₊₁ = xₖ - α∇f(xₖ). The learning rate α must be chosen appropriately; too large causes divergence, too small causes slow convergence.

7. **Optimality condition**: For unconstrained optimization, a necessary condition for a local minimum is ∇f(x\*) = 0. The second-order condition involves positive definiteness of the Hessian.
