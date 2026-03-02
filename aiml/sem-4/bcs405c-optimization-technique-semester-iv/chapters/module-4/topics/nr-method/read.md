Of course. Here is a comprehensive educational note on the Newton-Raphson (NR) Method for  Engineering students, structured as requested.

# **Optimization Technique - Module 4: Newton-Raphson (NR) Method**

**Subject:** Optimization Technique
**Semester:** IV
**Module:** Module 4: Convex Optimization-2
**Topic:** NR Method

---

## 1. Introduction

The Newton-Raphson (NR) Method is a powerful and widely-used iterative algorithm for finding successively better approximations to the roots (or zeros) of a real-valued function. In the context of **convex optimization**, its primary application is to solve the necessary condition for an unconstrained minimizer: finding the point where the gradient of the objective function is zero, i.e., ∇f(**x**) = **0**. It is a second-order method because it utilizes both the first and second derivatives (the Hessian matrix) of the function, which allows for remarkably fast convergence rates near the optimum.

## 2. Core Concepts

### A. The Fundamental Idea

While we use the method to find where ∇f(**x**) = **0**, the core idea is easiest to understand in one dimension for finding the root of a function `g(x) = 0`.

1.  Start with an initial guess `x₀`.
2.  Draw a tangent to the curve `g(x)` at the point `(x₀, g(x₀))`.
3.  The point where this tangent crosses the x-axis (`x₁`) is a new, hopefully better, approximation of the root.
4.  Repeat the process until the solution converges.

This process is described by the iterative formula:
**xₖ₊₁ = xₖ - g(xₖ)/g'(xₖ)**

### B. Extension to Optimization (Multivariable Case)

For an unconstrained optimization problem `min f(x)`, the optimum occurs where the gradient vector is zero. We can think of `g(x)` as the gradient vector `∇f(x)`. Therefore, to find the root of `∇f(x) = 0`, the Newton-Raphson formula becomes:

**xₖ₊₁ = xₖ - [∇²f(xₖ)]⁻¹ ∇f(xₖ)**

Where:
*   `xₖ` is the current point (a vector).
*   `∇f(xₖ)` is the **gradient vector** (first derivative) of `f` at `xₖ`.
*   `∇²f(xₖ)` is the **Hessian matrix** (matrix of second derivatives) of `f` at `xₖ`.
*   `[ ]⁻¹` denotes the inverse of the Hessian matrix.

### C. Geometric Interpretation and Intuition

The NR method can be interpreted as minimizing a quadratic approximation of the function `f` at each step. At point `xₖ`, we form a quadratic model (Taylor series expansion up to the second order):

**f(x) ≈ f(xₖ) + ∇f(xₖ)ᵀ(x - xₖ) + ½ (x - xₖ)ᵀ ∇²f(xₖ) (x - xₖ)**

The NR update step `xₖ₊₁` is exactly the point that minimizes this quadratic approximation. If the function `f` is quadratic and convex, the method converges to the global minimum in a single step.

### D. Algorithm Steps

1.  **Initialization:** Choose an initial point `x₀` and a tolerance `ε > 0`. Set `k = 0`.
2.  **Compute Gradient and Hessian:** Calculate the gradient vector `∇f(xₖ)` and the Hessian matrix `H(xₖ) = ∇²f(xₖ)`.
3.  **Solve the Linear System:** Solve the system of linear equations for the step direction `dₖ`:
    **H(xₖ) dₖ = -∇f(xₖ)**
    (This is more efficient and numerically stable than explicitly inverting the Hessian).
4.  **Update the Point:** Set `xₖ₊₁ = xₖ + dₖ`.
5.  **Check for Convergence:** If the norm of the step `||dₖ||` or the norm of the gradient `||∇f(xₖ)||` is less than `ε`, stop. `xₖ₊₁` is the optimal solution.
6.  **Iterate:** Set `k = k + 1` and go back to Step 2.

## 3. Example (One Variable)

Let's minimize the convex function: **f(x) = x⁴ - 3x³ + 2**

*   **Gradient:** g(x) = f'(x) = 4x³ - 9x²
*   **Hessian:** H(x) = f''(x) = 12x² - 18x

We want to find `x` such that `f'(x) = 0`.

**Iteration 1 (k=0):** Let’s start with `x₀ = 4`.
*   f'(4) = 4(64) - 9(16) = 256 - 144 = 112
*   f''(4) = 12(16) - 18(4) = 192 - 72 = 120
*   The Newton step: `d₀ = -f'(x₀)/f''(x₀) = -112/120 ≈ -0.933`
*   **x₁ = x₀ + d₀ = 4 - 0.933 = 3.067**

**Iteration 2 (k=1):** `x₁ = 3.067`
*   f'(3.067) ≈ 4(28.85) - 9(9.40) ≈ 115.4 - 84.6 = 30.8
*   f''(3.067) ≈ 12(9.40) - 18(3.067) ≈ 112.8 - 55.2 = 57.6
*   `d₁ = -30.8/57.6 ≈ -0.534`
*   **x₂ = 3.067 - 0.534 = 2.533**

**Iteration 3 (k=2):** `x₂ = 2.533`
*   f'(2.533) ≈ 4(16.26) - 9(6.414) ≈ 65.0 - 57.7 = 7.3
*   f''(2.533) ≈ 12(6.414) - 18(2.533) ≈ 76.97 - 45.59 = 31.38
*   `d₂ = -7.3/31.38 ≈ -0.233`
*   **x₃ = 2.533 - 0.233 = 2.300**

The method is clearly converging towards the true minimum, which is at `x = 2.25` (where `f'(x) = 0`). Subsequent iterations will get closer to this value.

## 4. Key Points & Summary

*   **Purpose:** A second-order iterative method to find where ∇f(**x**) = **0**, used for solving unconstrained optimization problems.
*   **Strength:** Very **fast convergence rate** (quadratic convergence) near the optimum if the initial guess is good.
*   **Requirements:**
    *   The function must be **twice differentiable**.
    *   The **Hessian matrix must be invertible** at each step.
*   **Drawbacks:**
    *   **Computationally expensive:** Requires computing and inverting/solving the Hessian at every iteration (O(n³) complexity).
    *   **Not globally convergent:** If the initial point is not close to the solution, or if the Hessian is not positive definite, the method may diverge. Modifications like using a **damped Newton step** (line search) are often needed to ensure global convergence.
*   **Ideal for:** Well-behaved, convex functions where a good initial guess is available and the cost of computing the Hessian is manageable. It is the foundation for more advanced algorithms like **Barrier Methods** in interior-point programming.