# Module 3: Convex Optimization-1 - Convex Sets, Functions & Separating Hyperplanes

## Introduction

Convex optimization forms the backbone of numerous engineering applications, from optimal power flow in electrical engineering to machine learning model training and resource allocation. Its power lies in the guarantee that if a problem is convex, any local minimum is also a global minimum, making it solvable efficiently. This foundation is built upon three core concepts: convex sets, convex functions, and the powerful geometric idea of separating hyperplanes.

## Core Concepts Explained

### 1. Convex Sets

A set `C` in a vector space is called **convex** if, for any two points `x₁` and `x₂` within `C`, the entire line segment connecting them also lies within `C`. Mathematically, this is expressed as:

`θx₁ + (1 - θ)x₂ ∈ C` for all `x₁, x₂ ∈ C` and `0 ≤ θ ≤ 1`.

**Examples:**
*   **Convex:** A line segment, a circle (and its interior), a triangle, a cube, a hyperplane (`{x | aᵀx = b}`), a halfspace (`{x | aᵀx ≤ b}`).
*   **Non-Convex:** A star shape, a crescent moon, a donut (annulus). The line segment connecting two points in different arms of a star will pass outside the set.

### 2. Convex Functions

A function `f: ℝⁿ → ℝ` is **convex** if its domain is a convex set and if the line segment between any two points on the graph of the function lies on or above the graph itself. The mathematical condition is:

`f(θx₁ + (1 - θ)x₂) ≤ θf(x₁) + (1 - θ)f(x₂)` for all `x₁, x₂ ∈ dom f` and `0 ≤ θ ≤ 1`.

This is known as the **Jensen's inequality**.

**Visualization:** The graph of a convex function is a bowl-shaped curve. For a twice-differentiable function, you can check for convexity by verifying its Hessian matrix (`∇²f(x)`) is positive semidefinite (`∇²f(x) ≽ 0`) for all `x` in the domain.

**Examples:**
*   **Convex:** `f(x) = x²`, `f(x) = e^x`, `f(x) = |x|` (on `ℝ`), `f(x) = x log(x)` (for `x > 0`).
*   **Non-Convex:** `f(x) = sin(x)` (over an interval larger than `π`), `f(x) = -x²`.

### 3. Separating Hyperplanes

The Separating Hyperplane Theorem is a fundamental result in convex analysis with profound implications for optimization, duality, and classification (e.g., Support Vector Machines).

**Theorem:** If two convex sets `C` and `D` are disjoint (i.e., `C ∩ D = ∅`), then there exists a hyperplane that separates them. This means there exists a non-zero vector `a` and a scalar `b` such that:

`aᵀx ≤ b` for all `x ∈ C`
`aᵀx ≥ b` for all `x ∈ D`

This defines the hyperplane `{x | aᵀx = b}` which lies between the two sets.

**Strong Separation:** If the sets are closed and at least one is compact (closed and bounded), a *strong separation* exists where the inequality can be strict: `aᵀx < b` for all `x ∈ C` and `aᵀx > b` for all `x ∈ D`.

**Application Example:** In a binary classification problem, where data points from two classes are linearly separable (i.e., two convex sets), the separating hyperplane is the decision boundary that maximizes the margin between the classes.

## Key Points & Summary

*   **Convex Set:** A set where the line segment between any two points remains inside the set. This property is crucial for defining the domain of convex problems.
*   **Convex Function:** A function that satisfies Jensen's inequality. Its "bowl-shaped" geometry ensures that any local minimum is a global minimum, which is the key reason convex optimization problems are tractable.
*   **Separating Hyperplane Theorem:** A powerful geometric tool stating that any two disjoint convex sets can be separated by a hyperplane. This is foundational for proving duality theorems (like Farkas' Lemma) and designing algorithms.
*   **Why it Matters:** Identifying convexity in sets and functions allows you to formulate problems as convex optimization problems. Once in this form, you can confidently apply specialized algorithms (like Interior-Point Methods) that are efficient and guaranteed to find the global optimal solution.
*   **Engineering Insight:** These are not just abstract mathematical concepts. They are the principles that enable robust design, optimal control, and efficient resource management in complex engineering systems.