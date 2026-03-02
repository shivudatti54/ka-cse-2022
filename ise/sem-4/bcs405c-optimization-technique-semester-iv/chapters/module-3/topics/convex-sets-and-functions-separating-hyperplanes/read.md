# Module 3: Convex Optimization-1 - Convex Sets, Functions, and Separating Hyperplanes

## Introduction

Convexity is the foundational bedrock of a vast portion of optimization theory. Unlike general non-linear problems, which can be riddled with local minima and complex landscapes, **convex optimization problems** have a special property: any local minimum is also a global minimum. This makes them reliably solvable with efficient algorithms. This module introduces the core concepts that define a convex problem: convex sets, convex functions, and the powerful geometric idea of a separating hyperplane.

## Core Concepts

### 1. Convex Sets

A set is convex if, for any two points within the set, the entire line segment connecting them also lies within the set.

**Mathematical Definition:**
A set \( C \subseteq \mathbb{R}^n \) is **convex** if for any points \( x_1, x_2 \in C \) and any scalar \( \theta \) with \( 0 \leq \theta \leq 1 \), we have:
\[
\theta x_1 + (1 - \theta) x_2 \in C
\]
The point \( \theta x_1 + (1 - \theta) x_2 \) is called a **convex combination** of \( x_1 \) and \( x_2 \).

**Examples:**

- **Convex:** A line segment, a hyperplane (\( \{x | a^Tx = b\} \)), a halfspace (\( \{x | a^Tx \leq b\} \)), a sphere, a polyhedron (like the feasible region of an LP).
- **Non-Convex:** A star-shaped set, a crescent moon shape, the set of integers.

### 2. Convex Functions

A function is convex if the line segment between any two points on its graph lies above or on the graph.

**Mathematical Definition:**
A function \( f: \mathbb{R}^n \rightarrow \mathbb{R} \) is **convex** if its domain is a convex set and for all \( x_1, x_2 \) in its domain and any \( \theta \) with \( 0 \leq \theta \leq 1 \), we have:
\[
f(\theta x_1 + (1 - \theta) x_2) \leq \theta f(x_1) + (1 - \theta) f(x_2)
\]
This is known as **Jensen's inequality**.

**Checking Convexity:**
For twice-differentiable functions, a powerful test is to check the Hessian matrix (\( \nabla^2f(x) \)). If the Hessian is **positive semidefinite** (\( \nabla^2f(x) \succeq 0 \)) for all \( x \) in the domain, then \( f \) is convex.

**Examples:**

- **Convex:** \( f(x) = x^2 \) (Hessian is 2, which is > 0), \( f(x) = e^x \), affine functions (\( f(x) = a^Tx + b \)), norms (\( ||x||\_p \)).
- **Non-Convex:** \( f(x) = \sin(x) \), \( f(x) = x^3 \) (for all \( x \)).

### 3. Separating Hyperplanes

The Separating Hyperplane Theorem is a fundamental result in convex analysis with profound implications for optimization, duality, and machine learning.

**Theorem:**
If \( C \) and \( D \) are two disjoint (non-intersecting) convex sets in \( \mathbb{R}^n \) (i.e., \( C \cap D = \emptyset \)), then there exists a hyperplane that separates them. This means there exists a non-zero vector \( a \in \mathbb{R}^n \) and a scalar \( b \) such that:
\[
a^Tx \leq b \quad \text{for all } x \in C \\
a^Tx \geq b \quad \text{for all } x \in D
\]
This defines the **separating hyperplane** \( \{x \, | \, a^Tx = b\} \).

**Application Example:**
Imagine two distinct, non-overlapping clusters of data points on a plane. The Separating Hyperplane Theorem guarantees that we can always draw at least one straight line (a hyperplane in 2D) such that all points of one cluster are on one side and all points of the other are on the opposite side. This is the very principle behind **Support Vector Machines (SVMs)** in machine learning.

**Special Case: Supporting Hyperplane**
For a convex set \( C \) and a point \( x_0 \) on its boundary (\( x_0 \in \text{boundary of } C \)), a **supporting hyperplane** at \( x_0 \) is a hyperplane \( \{x \, | \, a^Tx = a^Tx_0\} \) such that the entire set \( C \) lies in one of the associated halfspaces: \( a^Tx \leq a^Tx_0 \) for all \( x \in C \).

## Key Points & Summary

| Concept                   | Core Idea                                                                                    | Importance                                                                                                       |
| :------------------------ | :------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| **Convex Set**            | Contains all line segments between its points.                                               | Defines the feasible domain for a convex optimization problem.                                                   |
| **Convex Function**       | Graph lies below the line segment joining any two points.                                    | Guarantees that any local minimum is a **global minimum**.                                                       |
| **Separating Hyperplane** | A hyperplane that divides two disjoint convex sets.                                          | Foundational for proving duality (Farkas' lemma), optimality conditions, and classification algorithms like SVM. |
| **Supporting Hyperplane** | A hyperplane that touches a convex set at a boundary point and contains the set on one side. | Used to characterize optimal points and derive the Lagrangian dual.                                              |

**In summary:** Recognizing convex sets and functions allows us to identify problems that can be solved efficiently and globally. The Separating Hyperplane Theorem provides a powerful geometric tool to analyze these problems and prove fundamental theoretical results.
