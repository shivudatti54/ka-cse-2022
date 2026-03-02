# Newton and Quasi-Newton Methods

## Introduction to Second-Order Methods

In unconstrained optimization, we aim to minimize a function \( f(\mathbf{x}) \) where \( \mathbf{x} \in \mathbb{R}^n \). While first-order methods like Gradient Descent use only gradient information (\( \nabla f \)), **second-order methods** leverage additional curvature information from the **Hessian matrix** (\( \nabla^2 f \)) to achieve faster convergence. This chapter covers two powerful families of second-order methods: the classical Newton's Method and its practical approximations, the Quasi-Newton Methods.

## Newton's Method

### Conceptual Foundation

Newton's Method is derived from the second-order Taylor series approximation of the function \( f \) around the current point \( \mathbf{x}\_k \):

\[
f(\mathbf{x}\_k + \mathbf{p}) \approx f(\mathbf{x}\_k) + \nabla f(\mathbf{x}\_k)^T \mathbf{p} + \frac{1}{2} \mathbf{p}^T \nabla^2 f(\mathbf{x}\_k) \mathbf{p}
\]

where \( \mathbf{p} \) is the step we wish to take. To find a minimizer, we differentiate this quadratic approximation with respect to \( \mathbf{p} \) and set it to zero:

\[
\nabla f(\mathbf{x}\_k) + \nabla^2 f(\mathbf{x}\_k) \mathbf{p} = 0
\]

Solving for \( \mathbf{p} \) gives the **Newton step**:

\[
\mathbf{p}\_k = - [\nabla^2 f(\mathbf{x}_k)]^{-1} \nabla f(\mathbf{x}\_k)
\]

The update formula for the next iterate is:

\[
\mathbf{x}\_{k+1} = \mathbf{x}\_k + \mathbf{p}\_k = \mathbf{x}\_k - [\nabla^2 f(\mathbf{x}_k)]^{-1} \nabla f(\mathbf{x}\_k)
\]

### Algorithm Steps

1.  **Initialize:** Choose a starting point \( \mathbf{x}\_0 \), and set \( k = 0 \).
2.  **Check Termination:** If \( \|\| \nabla f(\mathbf{x}\_k) \|\| < \epsilon \), stop.
3.  **Compute Step:** Evaluate the gradient \( \mathbf{g}\_k = \nabla f(\mathbf{x}\_k) \) and the Hessian \( \mathbf{H}\_k = \nabla^2 f(\mathbf{x}\_k) \). Solve the linear system \( \mathbf{H}\_k \mathbf{p}\_k = -\mathbf{g}\_k \) for \( \mathbf{p}\_k \).
4.  **Update:** Set \( \mathbf{x}\_{k+1} = \mathbf{x}\_k + \mathbf{p}\_k \).
5.  **Increment:** Set \( k = k + 1 \) and go to Step 2.

### Example: Minimizing a Quadratic Function

Consider minimizing the function \( f(x) = 2x^2 - 8x + 10 \).

- Gradient: \( f'(x) = 4x - 8 \)
- Hessian: \( f''(x) = 4 \) (a constant)

Let's start from \( x_0 = 0 \).

**Iteration 1:**
\( f'(0) = 4(0) - 8 = -8 \)
\( f''(0) = 4 \)
Newton Step: \( p_0 = - [4]^{-1} _ (-8) = - (0.25) _ (-8) = 2 \)
\( x_1 = 0 + 2 = 2 \)

**Iteration 2:**
\( f'(2) = 4(2) - 8 = 0 \)
Since the gradient is zero, the algorithm terminates. The optimum is \( x^\* = 2 \).

This demonstrates Newton's method's ability to converge in a single step for a quadratic function.

### Convergence Properties

Newton's method exhibits **quadratic convergence** near a local minimum under certain conditions:

- The Hessian matrix \( \nabla^2 f(\mathbf{x}) \) must be **positive definite** at the solution \( \mathbf{x}^\* \).
- The Hessian must be **Lipschitz continuous** near \( \mathbf{x}^\* \).

This means the error decreases quadratically:
\[
\|\| \mathbf{x}_{k+1} - \mathbf{x}^\* \|\| \leq C \|\| \mathbf{x}_{k} - \mathbf{x}^\* \|\|^2
\]
for some constant \( C > 0 \). This is significantly faster than the linear convergence of gradient descent.

### Limitations and Drawbacks

1.  **Hessian Computation:** Calculating the full Hessian matrix (\( O(n^2) \) operations) and solving the linear system (\( O(n^3) \) operations) can be computationally expensive for large \( n \).
2.  **Hessian Inversion:** The method requires the Hessian to be invertible. If it's singular, the Newton step is undefined.
3.  **Not Always a Descent Direction:** If the Hessian is not positive definite (e.g., at a saddle point or far from the optimum), the Newton step \( \mathbf{p}\_k \) might not be a descent direction (\( \nabla f(\mathbf{x}\_k)^T \mathbf{p}\_k > 0 \)), causing the algorithm to diverge.
4.  **Global Convergence:** The pure Newton method is not globally convergent. It needs modifications (like a line search or trust region) to ensure it converges from an arbitrary starting point.

## Quasi-Newton Methods

### The Core Idea

Quasi-Newton methods address the computational burden of Newton's method. They avoid explicitly calculating the Hessian. Instead, they build an **approximation** to the Hessian (or its inverse) iteratively using only gradient information.

The update step becomes:
\[
\mathbf{x}_{k+1} = \mathbf{x}\_k - \alpha_k \mathbf{B}\_k^{-1} \nabla f(\mathbf{x}\_k)
\]
where \( \mathbf{B}\_k \approx \nabla^2 f(\mathbf{x}\_k) \) is the Hessian approximation, and \( \alpha_k \) is a step length found via line search. Alternatively, some methods approximate the inverse Hessian directly (\( \mathbf{H}\_k \approx [\nabla^2 f(\mathbf{x}_k)]^{-1} \)), leading to an update without solving a linear system:
\[
\mathbf{x}_{k+1} = \mathbf{x}\_k - \alpha_k \mathbf{H}\_k \nabla f(\mathbf{x}\_k)
\]

### The Secant Condition

The key to building these approximations is the **Secant Condition** (or Quasi-Newton Equation). Let’s define:

- \( \mathbf{s}_k = \mathbf{x}_{k+1} - \mathbf{x}\_k \) (the step)
- \( \mathbf{y}_k = \nabla f(\mathbf{x}_{k+1}) - \nabla f(\mathbf{x}\_k) \) (the change in gradient)

A Taylor expansion shows that the Hessian satisfies \( \nabla^2 f(\mathbf{x}_k) \mathbf{s}\_k \approx \mathbf{y}\_k \). Therefore, we require our approximation \( \mathbf{B}_{k+1} \) to satisfy:
\[
\mathbf{B}_{k+1} \mathbf{s}\_k = \mathbf{y}\_k
\]
This is the secant condition. For the inverse Hessian approximation \( \mathbf{H}_{k+1} \), the condition is:
\[
\mathbf{H}\_{k+1} \mathbf{y}\_k = \mathbf{s}\_k
\]

### The BFGS Algorithm

The **Broyden–Fletcher–Goldfarb–Shanno (BFGS)** method is the most popular Quasi-Newton algorithm. It updates the inverse Hessian approximation \( \mathbf{H}\_k \) directly.

**BFGS Update Formula:**
\[
\mathbf{H}\_{k+1} = \left ( \mathbf{I} - \frac{\mathbf{s}\_k \mathbf{y}\_k^T}{\mathbf{y}\_k^T \mathbf{s}\_k} \right ) \mathbf{H}\_k \left ( \mathbf{I} - \frac{\mathbf{y}\_k \mathbf{s}\_k^T}{\mathbf{y}\_k^T \mathbf{s}\_k} \right ) + \frac{\mathbf{s}\_k \mathbf{s}\_k^T}{\mathbf{y}\_k^T \mathbf{s}\_k}
\]

This update ensures that \( \mathbf{H}\_{k+1} \) remains symmetric and positive definite if \( \mathbf{H}\_k \) is positive definite and \( \mathbf{y}\_k^T \mathbf{s}\_k > 0 \) (which is guaranteed by a Wolfe line search).

**BFGS Algorithm Steps:**

1.  Initialize \( \mathbf{x}\_0 \), choose initial \( \mathbf{H}\_0 \) (often \( \mathbf{I} \)), set \( k = 0 \).
2.  Compute search direction: \( \mathbf{p}\_k = -\mathbf{H}\_k \nabla f(\mathbf{x}\_k) \).
3.  Perform line search: find \( \alpha_k > 0 \) satisfying Wolfe conditions.
4.  Update: \( \mathbf{x}\_{k+1} = \mathbf{x}\_k + \alpha_k \mathbf{p}\_k \).
5.  Compute \( \mathbf{s}_k = \alpha_k \mathbf{p}\_k \) and \( \mathbf{y}\_k = \nabla f(\mathbf{x}_{k+1}) - \nabla f(\mathbf{x}\_k) \).
6.  Apply BFGS update to get \( \mathbf{H}\_{k+1} \).
7.  Set \( k = k + 1 \), go to Step 2.

### The DFP Algorithm

The **Davidon–Fletcher–Powell (DFP)** method is historically significant and updates an approximation to the Hessian itself (\( \mathbf{B}\_k \)).

**DFP Update Formula:**
\[
\mathbf{B}\_{k+1} = \left ( \mathbf{I} - \frac{\mathbf{y}\_k \mathbf{s}\_k^T}{\mathbf{y}\_k^T \mathbf{s}\_k} \right ) \mathbf{B}\_k \left ( \mathbf{I} - \frac{\mathbf{s}\_k \mathbf{y}\_k^T}{\mathbf{y}\_k^T \mathbf{s}\_k} \right ) + \frac{\mathbf{y}\_k \mathbf{y}\_k^T}{\mathbf{y}\_k^T \mathbf{s}\_k}
\]

BFGS is generally considered superior to DFP and is more widely used in practice.

### Limited-Memory BFGS (L-BFGS)

For very high-dimensional problems (large \( n \)), storing the dense \( n \times n \) matrix \( \mathbf{H}\_k \) becomes prohibitive. **L-BFGS** solves this by not storing the matrix explicitly. Instead, it stores a limited history of the last \( m \) pairs of vectors \( \{ \mathbf{s}\_i, \mathbf{y}\_i \} \). The product \( \mathbf{H}\_k \nabla f(\mathbf{x}\_k) \) is computed recursively using this history, requiring storage of only \( O(mn) \) floats instead of \( O(n^2) \).

## Comparison of Methods

| Feature                  | Gradient Descent        | Newton's Method                | Quasi-Newton (BFGS)                       |
| :----------------------- | :---------------------- | :----------------------------- | :---------------------------------------- |
| **Order of Convergence** | Linear (Q-linear)       | Quadratic (Q-quadratic)        | Superlinear (Q-superlinear)               |
| **Cost per Iteration**   | \( O(n) \)              | \( O(n^3) \) (Hessian + Solve) | \( O(n^2) \) (BFGS), \( O(mn) \) (L-BFGS) |
| **Uses Hessian?**        | No                      | Yes, explicit calculation      | No, approximated from gradients           |
| **Robustness**           | Good (with line search) | Poor (requires modifications)  | Very Good                                 |
| **Storage**              | \( O(n) \)              | \( O(n^2) \)                   | \( O(n^2) \) (BFGS), \( O(mn) \) (L-BFGS) |

## Practical Considerations and Exam Tips

- **Line Search is Crucial:** Pure Newton and Quasi-Newton methods are almost always used with a line search (e.g., satisfying Wolfe conditions) to ensure global convergence and stability.
- **Initialization:** For Quasi-Newton methods, the initial inverse Hessian approximation \( \mathbf{H}\_0 \) is typically set to the identity matrix, making the first step equivalent to gradient descent.
- **Hessian Modification:** If the pure Newton method encounters a non-positive definite Hessian, a standard fix is to use **Hessian Modification**: add a multiple of the identity matrix \( \lambda \mathbf{I} \) until \( \nabla^2 f(\mathbf{x}\_k) + \lambda \mathbf{I} \) becomes positive definite. This is closely related to trust region methods.
- **Exam Focus:** Be prepared to **derive the Newton step** from the Taylor series, **perform one iteration** of Newton's method on a simple function, **explain the secant condition**, and **compare and contrast** the properties (cost, convergence, storage) of Gradient Descent, Newton, and BFGS.
- **Remember the Acronyms:** BFGS and DFP are fundamental. Remember what they stand for and that BFGS is the preferred choice.
- **Think L-BFGS for Big Problems:** The answer to "what do you use for a large-scale unconstrained problem?" is almost always **L-BFGS**.
