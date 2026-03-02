# Module 3: Convex Optimization-1 - Convex Sets, Functions, and Separating Hyperplanes

## Introduction

Convex Optimization is a powerful and elegant subfield of mathematical optimization where the objective function is convex, and the feasible set defined by the constraints is convex. The "convexity" property is the cornerstone that makes these problems fundamentally easier to solve than non-convex ones. For any local optimum found in a convex problem, we can be certain it is a **global optimum**. This module introduces the foundational concepts of convex sets and functions, which allow us to define convex optimization problems, and the concept of separating hyperplanes, a crucial tool for proving optimality and duality.

## Core Concepts

### 1. Convex Sets

A set $C$ in a vector space is called **convex** if the line segment between any two points in $C$ lies entirely within $C$.

**Mathematical Definition:**
A set $C \subseteq \mathbb{R}^n$ is convex if for any two points $x_1, x_2 \in C$ and any scalar $\theta$ with $0 \leq \theta \leq 1$, we have:
$$\theta x_1 + (1 - \theta)x_2 \in C$$
The point $\theta x_1 + (1 - \theta)x_2$ is called a **convex combination** of $x_1$ and $x_2$.

**Examples:**
*   **Convex:** A line segment, a circle (including its interior), a hypercube, a half-space (e.g., $\{x | a^Tx \leq b\}$), and the intersection of convex sets.
*   **Non-Convex:** A star shape, a crescent shape, the set of integers.

### 2. Convex Functions

A function $f: \mathbb{R}^n \rightarrow \mathbb{R}$ is **convex** if its domain is a convex set and if for any two points $x_1, x_2$ in its domain and any $\theta$ where $0 \leq \theta \leq 1$, the following inequality holds:
$$f(\theta x_1 + (1 - \theta)x_2) \leq \theta f(x_1) + (1 - \theta)f(x_2)$$
Graphically, this means the line segment between any two points on the function's graph lies **on or above** the graph itself. If the inequality is strict ($<$), the function is **strictly convex**.

**First-Order Condition (for differentiable functions):**
A differentiable function $f$ is convex if and only if:
$$f(y) \geq f(x) + \nabla f(x)^T (y - x) \quad \text{for all } x, y \in \text{dom } f$$
This states that the first-order Taylor approximation is a **global underestimator** of the function.

**Examples:**
*   **Convex:** $f(x) = x^2$, $f(x) = e^x$, $f(x_1, x_2) = x_1^2 + 2x_2^2$ (a parabola).
*   **Non-Convex:** $f(x) = \sin(x)$ (over most intervals), $f(x) = x^3$ (not on $\mathbb{R}$).

### 3. Separating Hyperplane Theorem

This is a fundamental result in convex analysis with profound implications for optimization and duality.

**Theorem:** Suppose you have two disjoint (non-overlapping) convex sets $C$ and $D$ (i.e., $C \cap D = \emptyset$). Then, there exists a hyperplane that separates them.

**Mathematical Formulation:**
There exists a non-zero vector $a \in \mathbb{R}^n$ and a scalar $b$ such that:
$$a^Tx \leq b \quad \text{for all } x \in C$$
$$a^Tx \geq b \quad \text{for all } x \in D$$
This hyperplane $\{x | a^Tx = b\}$ is called a **separating hyperplane**.

**Graphical Example:**
Imagine two circles on a plane that do not touch. You can always draw at least one straight line between them such that all points of one circle lie on one side of the line and all points of the other circle lie on the opposite side.

**Application in Optimization:**
This theorem is used to prove the existence of **dual variables** (Lagrange multipliers). In a constrained optimization problem, at an optimal point, the hyperplane separating the feasible set and the set of better points defines the optimality condition (KKT conditions).

## Key Points & Summary

*   **Convex Set:** A set where the line segment between any two points remains inside the set.
*   **Convex Function:** A function where the chord between any two points lies above the graph. Its epigraph is a convex set.
*   **Global Optimum:** For a convex optimization problem (minimizing a convex function over a convex set), any local minimum is automatically a global minimum. This is the primary reason convex problems are tractable.
*   **Separating Hyperplane Theorem:** Two disjoint convex sets can always be separated by a hyperplane. This is a foundational existence theorem.
*   **Why it Matters:** These concepts form the bedrock of convex optimization. Recognizing convexity in a problem allows you to apply powerful and efficient algorithms (like gradient descent, interior-point methods) guaranteed to find the global solution. The separating hyperplane theorem leads directly to the powerful concepts of duality and the Karush-Kuhn-Tucker (KKT) conditions.

**In your next module, you will see how these concepts combine to formally define a Convex Optimization Problem and how duality arises from separation.**