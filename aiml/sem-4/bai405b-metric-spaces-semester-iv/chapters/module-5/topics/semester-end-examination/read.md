Of course. Here is a comprehensive educational note on Connectedness in Metric Spaces, tailored for  Engineering students.

# Module 5: Connectedness - A Primer for Semester-End Examination

## Introduction

In the study of metric spaces, we often want to understand the "structure" or "shape" of a space. **Connectedness** is a fundamental topological property that formalizes the intuitive idea of a space being "in one piece." A space is disconnected if it can be split into two separate, non-overlapping open sets. Conversely, it is connected if no such split is possible. This concept has crucial applications in analysis, such as proving the Intermediate Value Theorem and understanding the behavior of continuous functions.

## Core Concepts Explained

### 1. Definition of Connectedness

A metric space $(X, d)$ is said to be **connected** if it **cannot** be represented as the union of two non-empty disjoint open sets.
That is, there do not exist two non-empty open sets $U$ and $V$ such that:
*   $U \cup V = X$
*   $U \cap V = \emptyset$

If such sets *do* exist, then $X$ is **disconnected**. The pair $(U, V)$ is called a **separation** of $X$.

**Key Insight:** Think of "open sets" in this definition as the tools we use to break the space apart. If the space can be broken into two open pieces that don't touch each other, it's disconnected.

### 2. Connected Subsets

A subset $A$ of a metric space $(X, d)$ is called connected if it is connected under the **subspace metric**. This means we consider $A$ itself as a metric space and look at open sets *within* $A$.

**Example:** The interval $[0, 1] \cup [2, 3]$ is a subset of $\mathbb{R}$ (with the usual metric). It is disconnected because we can find two open sets *in $\mathbb{R}$* (e.g., $(-1, 1.5)$ and $(1.5, 4)$) whose intersections with the subset form a separation.
$U_A = A \cap (-1, 1.5) = [0, 1]$ and $V_A = A \cap (1.5, 4) = [2, 3]$. Since $[0,1]$ and $[2,3]$ are disjoint and their union is $A$, the subset is disconnected.

### 3. Important Theorem: Connectedness of Intervals in $\mathbb{R}$

A crucial result for real analysis states: **A subset of $\mathbb{R}$ is connected if and only if it is an interval.**

An interval can be any set $I \subseteq \mathbb{R}$ such that for any $a, b \in I$ with $a < b$, every $x$ satisfying $a < x < b$ also belongs to $I$. This includes $(a,b)$, $[a,b]$, $(a, \infty)$, $(-\infty, b]$, and $\mathbb{R}$ itself.

This theorem is the foundation for the Intermediate Value Theorem.

### 4. Continuous Functions Preserve Connectedness

This is one of the most important properties for engineering applications.

**Theorem:** Let $f: (X, d_X) \to (Y, d_Y)$ be a continuous function. If $A \subseteq X$ is a connected set, then its image $f(A) \subseteq Y$ is also a connected set.

**Proof Outline (for understanding):** Assume $f(A)$ is disconnected. Then you can "pull back" the separation into $A$ using the continuity of $f$, which would imply $A$ is also disconnected—a contradiction.

**Application - The Intermediate Value Theorem (IVT):** This is a direct consequence. Let $f: [a, b] \to \mathbb{R}$ be continuous. Since $[a,b]$ is connected, $f([a,b])$ must also be a connected subset of $\mathbb{R}$, i.e., it is an interval. Therefore, $f$ must attain every value between $f(a)$ and $f(b)$.

### 5. Path-Connectedness (A Stronger Form)

A metric space $(X, d)$ is **path-connected** if for every pair of points $x, y \in X$, there exists a continuous function $f: [0,1] \to X$ (called a **path**) such that $f(0) = x$ and $f(1) = y$.

**Important Fact:** Every path-connected space is connected. However, the converse is **not always true**.

**Classic Counterexample:** The **Topologist's Sine Curve** is a connected space that is not path-connected. It consists of the graph of $y = \sin(1/x)$ for $x > 0$ and the point $(0,0)$. You cannot draw a continuous path from a point on the curve to the point $(0,0)$.

## Key Points & Summary

*   **Definition:** A space is **connected** if it cannot be divided into two non-empty, disjoint open sets.
*   **Subsets:** A subset is connected if it is connected in its subspace topology.
*   **Intervals:** In $\mathbb{R}$, the connected sets are precisely the intervals.
*   **Preservation:** The continuous image of a connected set is connected. This is a powerful tool for proving properties like the IVT.
*   **Path-Connectedness:** A stronger, more intuitive property (if you can draw a path between any two points, the space is connected). All path-connected spaces are connected, but not all connected spaces are path-connected.
*   **Exam Focus:** Be prepared to:
    *   Use the definition to prove whether a given set (like $[0,1] \cup [2,3]$) is connected or disconnected.
    *   State and apply the theorem that continuous functions map connected sets to connected sets.
    *   Understand the difference between connectedness and path-connectedness.
    *   Know the result about intervals in $\mathbb{R}$.