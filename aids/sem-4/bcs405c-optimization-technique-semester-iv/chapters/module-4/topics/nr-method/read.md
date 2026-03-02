Of course. Here is a comprehensive educational note on the Newton-Raphson (NR) Method for  Engineering students, tailored for the Optimization Techniques curriculum.

# **Module 4: Convex Optimization-2 | Topic: Newton-Raphson (NR) Method**

## **1. Introduction**

In optimization, our goal is to find the minimum or maximum of a function, which corresponds to points where its first derivative (or gradient) is zero. The Newton-Raphson (NR) Method is a powerful iterative technique originally developed for finding roots of equations. In the context of optimization, it is repurposed to find the **stationary points** (where ∇f(x) = 0) of a twice-differentiable function. It is renowned for its fast convergence properties, especially when started near the optimum, making it a cornerstone algorithm in convex optimization.

---

## **2. Core Concepts**

### **A. From Root-Finding to Optimization**

The standard NR method finds the root of a function g(x) (i.e., x such that g(x)=0). The iterative formula is:
`x_{k+1} = x_k - [g(x_k) / g'(x_k)]`

In optimization, we don't want to find the root of the function `f(x)` itself, but the root of its derivative `f'(x)`. Therefore, we set `g(x) = f'(x)`. Substituting into the root-finding formula:
`x_{k+1} = x_k - [f'(x_k) / f''(x_k)]`

This is the **Newton-Raphson Method for 1-D Unconstrained Optimization**.

### **B. The Multivariate Case (For n Variables)**

For a function `f(x)` where `x` is an n-dimensional vector (`x ∈ R^n`), we extend the concept using vectors and matrices.

*   The first derivative is replaced by the **Gradient vector**, `∇f(x)`.
*   The second derivative is replaced by the **Hessian matrix**, `H(x)` or `∇²f(x)`, which contains all the second-order partial derivatives.

The iterative step becomes:
**`x_{k+1} = x_k - [H(x_k)]^{-1} ∇f(x_k)`**

Where:
*   `x_k` is the current point (vector).
*   `x_{k+1}` is the next, hopefully better, estimate.
*   `[H(x_k)]^{-1}` is the inverse of the Hessian matrix evaluated at `x_k`.
*   `∇f(x_k)` is the gradient vector evaluated at `x_k`.

### **C. Interpretation and Intuition**

The NR step can be understood as a two-part process:
1.  **Model the Function:** At each point `x_k`, we approximate the function `f(x)` by its second-order Taylor series expansion. This creates a local quadratic model of the function.
2.  **Minimize the Model:** The NR step `(x_{k+1} = x_k - H^{-1}∇f)` is the exact minimizer of this local quadratic model (provided the Hessian `H` is positive definite). Essentially, it jumps directly to the minimum of this approximated quadratic "bowl."

---

## **3. Algorithm Steps**

The procedure for implementing the NR method is straightforward:

1.  **Initialize:** Choose a starting point `x_0`. Set iteration counter `k = 0`. Select a tolerance `ϵ > 0`.
2.  **Compute Gradient and Hessian:** Calculate the gradient `∇f(x_k)` and the Hessian matrix `H(x_k)`.
3.  **Solve the Linear System:** Solve for the search direction `d_k` in the system:
    `H(x_k) d_k = -∇f(x_k)`
    (This is computationally more stable than explicitly inverting the Hessian).
4.  **Update the Point:** `x_{k+1} = x_k + d_k`
5.  **Check for Convergence:** If the norm of the gradient `||∇f(x_{k+1})||` is less than the tolerance `ϵ`, stop. The point `x_{k+1}` is a stationary point.
6.  **Iterate:** Else, set `k = k + 1` and go back to step 2.

---

## **4. Example (1-Dimensional)**

Let's find the minimum of the convex function:
**`f(x) = x^2 + 5x + 6`**

1.  First and second derivatives:
    `f'(x) = 2x + 5`
    `f''(x) = 2` (constant, positive -> function is convex)

2.  Apply the NR update formula:
    `x_{k+1} = x_k - [f'(x_k) / f''(x_k)] = x_k - [(2x_k + 5) / 2]`

3.  **Iteration 1:** Let's start with `x_0 = 0`
    `x_1 = 0 - [(2*0 + 5)/2] = 0 - (5/2) = -2.5`

4.  **Iteration 2:** `x_1 = -2.5`
    `f'(-2.5) = 2*(-2.5) + 5 = 0`
    Since the gradient is zero, we have converged.

The algorithm found the minimum at `x = -2.5` in just one iteration. This is expected because NR exactly minimizes a quadratic function. For non-quadratic functions, it will take more iterations.

---

## **5. Key Points & Summary**

| **Aspect** | **Description** |
| :--- | :--- |
| **Purpose** | To find stationary points (where ∇f(x)=0) for smooth, twice-differentiable functions. |
| **Key Formula** | `x_{k+1} = x_k - [H(x_k)]^{-1} ∇f(x_k)` |
| **Strength** | **Quadratic Convergence Rate:** Very fast if started near the solution. The number of correct digits roughly doubles per iteration. |
| **Weaknesses** | 1. **Computational Cost:** Requires computation and inversion of the Hessian matrix (O(n³) operations per iteration). <br> 2. **Not Globally Convergent:** May diverge if the starting point is far from the optimum or if the Hessian is not positive definite. <br> 3. **Requires Hessian:** The function must be twice differentiable, and the Hessian must be computed. |
| **Convexity** | For convex problems where the Hessian is always positive definite, the NR method is extremely effective and reliable. |
| ** Focus** | Understand the derivation from the root-finding method, the intuition behind the update step, and its advantages/disadvantages compared to methods like Steepest Descent. |