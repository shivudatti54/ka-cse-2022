Of course. Here is a comprehensive explanation on "The Gradient of Quadratic Cost" for  Engineering students, structured as requested.

# The Gradient of Quadratic Cost in Optimization

## 1. Introduction

In Module 2, we explore how the powerful tools of vector calculus, specifically the **gradient**, are directly applied to real-world engineering problems. A fundamental task in optimization is minimizing a cost function. Often, this cost function is **quadratic** (e.g., in Least Squares regression, control systems, signal processing). Understanding how to compute and interpret the gradient of such a function is the first crucial step towards finding its minimum point efficiently. This note explains the formulation of a quadratic cost function and demonstrates how its gradient leads us to the optimal solution.

## 2. Core Concepts

### What is a Quadratic Cost Function?

A quadratic cost function is a scalar function of a vector variable that takes the form:
$$ J(\mathbf{x}) = \frac{1}{2} \mathbf{x}^T \mathbf{A} \mathbf{x} - \mathbf{b}^T \mathbf{x} + c $$
where:
*   $\mathbf{x}$ is an $n$-dimensional vector representing the decision variables (e.g., parameters we want to optimize), $\mathbf{x} \in \mathbb{R}^n$.
*   $\mathbf{A}$ is an $n \times n$ symmetric, positive definite matrix ($\mathbf{A}^T = \mathbf{A}$). The positive definiteness ensures the function has a unique global minimum.
*   $\mathbf{b}$ is an $n$-dimensional vector, $\mathbf{b} \in \mathbb{R}^n$.
*   $c$ is a scalar constant.

The $\frac{1}{2}$ term is a convention that simplifies the derivative, as it will cancel out the factor of 2 that appears during differentiation.

### Why is the Gradient Important?

The **gradient**, $\nabla J(\mathbf{x})$, of a scalar function is a vector that points in the direction of the **steepest ascent**. Conversely, the negative gradient ($-\nabla J(\mathbf{x})$) points in the direction of the **steepest descent**. For minimization, we want to move in the direction where the function decreases the fastest. Therefore, the gradient is the fundamental guide for many iterative optimization algorithms (like Gradient Descent).

A necessary condition for a point $\mathbf{x}^*$ to be a local minimum is that the gradient at that point is zero:
$$ \nabla J(\mathbf{x}^*) = \mathbf{0} $$
This is known as the **first-order necessary condition**.

### Finding the Gradient of the Quadratic Cost

Our goal is to find the derivative of $J(\mathbf{x})$ with respect to the vector $\mathbf{x}$. We can break the function into parts and use known identities from vector calculus:

1.  **Quadratic Term:** $\frac{\partial}{\partial \mathbf{x}} (\mathbf{x}^T \mathbf{A} \mathbf{x}) = 2\mathbf{A}\mathbf{x}$ (This is analogous to $\frac{d}{dx}(ax^2) = 2ax$)
2.  **Linear Term:** $\frac{\partial}{\partial \mathbf{x}} (\mathbf{b}^T \mathbf{x}) = \mathbf{b}$
3.  **Constant Term:** $\frac{\partial}{\partial \mathbf{x}} (c) = \mathbf{0}$

Applying these identities to our cost function $J(\mathbf{x})$:
$$
\nabla J(\mathbf{x}) = \nabla \left( \frac{1}{2} \mathbf{x}^T \mathbf{A} \mathbf{x} - \mathbf{b}^T \mathbf{x} + c \right) = \frac{1}{2} \cdot 2\mathbf{A}\mathbf{x} - \mathbf{b} = \mathbf{A}\mathbf{x} - \mathbf{b}
$$

**The gradient of the quadratic cost function is:**
$$ \nabla J(\mathbf{x}) = \mathbf{A}\mathbf{x} - \mathbf{b} $$

## 3. Example: Finding the Minimum Analytically

Let's consider a simple 2D example with concrete values.

**Problem:** Minimize the cost function $J(\mathbf{x}) = \frac{1}{2} \mathbf{x}^T \mathbf{A} \mathbf{x} - \mathbf{b}^T \mathbf{x}$, where
$$
\mathbf{A} = \begin{bmatrix} 2 & 0 \\ 0 & 4 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
$$

**Step 1: Write the expanded form of $J(\mathbf{x})$.**
$$
J(x_1, x_2) = \frac{1}{2} \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} 2 & 0 \\ 0 & 4 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} - \begin{bmatrix} 2 & 4 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
$$
$$
= \frac{1}{2} (2x_1^2 + 4x_2^2) - (2x_1 + 4x_2) = x_1^2 + 2x_2^2 - 2x_1 - 4x_2
$$

**Step 2: Find the gradient $\nabla J(\mathbf{x})$.**
Using our formula:
$$
\nabla J(\mathbf{x}) = \mathbf{A}\mathbf{x} - \mathbf{b} = \begin{bmatrix} 2 & 0 \\ 0 & 4 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} - \begin{bmatrix} 2 \\ 4 \end{bmatrix} = \begin{bmatrix} 2x_1 - 2 \\ 4x_2 - 4 \end{bmatrix}
$$

**Step 3: Set the gradient to zero to find the critical point $\mathbf{x}^*$.**
$$
\nabla J(\mathbf{x}) = \mathbf{0} \implies \begin{bmatrix} 2x_1 - 2 \\ 4x_2 - 4 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$
Solving this system gives:
$2x_1 - 2 = 0 \implies x_1^* = 1$
$4x_2 - 4 = 0 \implies x_2^* = 1$

**Solution:** The minimum of the cost function is at $\mathbf{x}^* = (1, 1)^T$. We can verify that the Hessian matrix ($\mathbf{A}$) is positive definite, confirming this is indeed a minimum.

## 4. Key Points & Summary

*   **Foundation for Optimization:** The quadratic cost function, $J(\mathbf{x}) = \frac{1}{2} \mathbf{x}^T \mathbf{A} \mathbf{x} - \mathbf{b}^T \mathbf{x} + c$, is a cornerstone in optimization, especially in Least Squares problems.
*   **The Gradient is Key:** The gradient of this function, $\nabla J(\mathbf{x}) = \mathbf{A}\mathbf{x} - \mathbf{b}$, provides the direction of steepest ascent and is essential for iterative minimization algorithms like Gradient Descent.
*   **Optimality Condition:** The first-order necessary condition for a minimum is $\nabla J(\mathbf{x}) = \mathbf{0}$. For a quadratic function with a positive definite $\mathbf{A}$, this condition is both necessary and sufficient.
*   **Closed-Form Solution:** Unlike more complex functions, the minimum of a quadratic cost can often be found **analytically** by solving the system of linear equations $\mathbf{A}\mathbf{x} = \mathbf{b}$. This is a direct result of setting the gradient to zero.
*   **Beyond the Minimum:** This analysis is not just theoretical; it is the basis for algorithms in machine learning (linear regression), optimal control, and computer vision.

Understanding this derivation is crucial, as it forms the analytical backbone for the numerical optimization techniques you will encounter later in this course.