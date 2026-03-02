Of course. Here is a comprehensive educational note on "Connectedness" tailored for  Engineering students.

# Module 5: Connectedness - Semester-End Examination Guide

## Introduction

In calculus, we intuitively understand the idea of a "connected" set as one that is in a single piece. However, in the abstract world of metric spaces, this intuitive notion needs a rigorous mathematical definition. Connectedness is a fundamental topological property that helps classify metric spaces and understand the behavior of functions defined on them. It is crucial for proving important results, such as the Intermediate Value Theorem in higher dimensions.

## Core Concepts

### 1. Definition of Connectedness

A metric space $(X, d)$ is said to be **disconnected** if there exist two non-empty **open sets** $A$ and $B$ in $X$ such that:
1. $A \cap B = \emptyset$
2. $A \cup B = X$

If no such separation exists, the space $X$ is called **connected**.

**Explanation:** This means we can split the entire space into two disjoint, open pieces. A space is connected if it *cannot* be split in this way. It's important to remember that both sets $A$ and $B$ must be open in $X$.

### 2. Connected Subsets

A subset $S$ of a metric space $X$ is connected if it is connected in the **subspace topology**. This means we consider $S$ itself as a metric space with the same metric $d$ restricted to $S$.

### 3. Characterizations and Theorems

*   **Continuous Images of Connected Sets:** The most important theorem states: **"The continuous image of a connected set is connected."** Formally, if $f: (X, d_X) \to (Y, d_Y)$ is a continuous function and $X$ is connected, then $f(X)$ is a connected subset of $Y$. This is a powerful tool for proving sets are connected.

*   **Connectedness of Intervals:** In the real line $\mathbb{R}$ (with the standard Euclidean metric), a subset is connected **if and only if it is an interval** (e.g., $(a, b)$, $[a, b]$, $[a, \infty)$, etc.). This directly leads to the classic Intermediate Value Theorem.

*   **Path Connectedness:** A stronger notion is that of a **path-connected** space. A space $X$ is path-connected if for every pair of points $x, y \in X$, there exists a continuous function $f: [0,1] \to X$ (called a *path*) such that $f(0) = x$ and $f(1) = y$.
    *   **Key Fact:** Every path-connected space is connected. However, the converse is not always true. There exist connected spaces that are not path-connected (these are often complex and beyond the scope of this module).

## Examples

**Example 1: Connected Sets**
*   The real line $\mathbb{R}$ is connected.
*   Any interval, like $[0, 1]$ or $(2, 5)$, is connected in $\mathbb{R}$.
*   $\mathbb{R}^n$ (for $n \geq 2$) is connected. More generally, any **convex** subset of $\mathbb{R}^n$ (like a disk, a square, or the entire space) is path-connected and hence connected.

**Example 2: Disconnected Sets**
*   The set $X = [0, 1] \cup [2, 3]$ in $\mathbb{R}$ is disconnected. We can separate it using the open sets (in the subspace topology) $A = [0,1]$ and $B = [2,3]$. Note that $A$ is open in $X$ because $A = X \cap (-1, 1.5)$, and $(-1, 1.5)$ is open in $\mathbb{R}$.
*   The set of rational numbers $\mathbb{Q}$ is disconnected. For example, separate it into $\mathbb{Q} \cap (-\infty, \sqrt{2})$ and $\mathbb{Q} \cap (\sqrt{2}, \infty)$.

**Example 3: Application of the Theorem**
Consider the function $f: \mathbb{R} \to \mathbb{R}^2$ defined by $f(t) = (\cos t, \sin t)$. This function is continuous. The domain $\mathbb{R}$ is connected. Therefore, the image $f(\mathbb{R})$, which is the **unit circle**, is a connected subset of $\mathbb{R}^2$.

## Key Points & Summary

*   **Definition:** A space is **connected** if it cannot be written as the union of two disjoint, non-empty open sets.
*   **Separation:** A **disconnection** of $X$ is a pair of disjoint, non-empty open sets whose union is $X$.
*   **Main Theorem:** The continuous image of a connected set is connected. This is a vital tool for proofs.
*   **Intervals:** In $\mathbb{R}$, the connected subsets are precisely the intervals.
*   **Path-Connectedness:** A stronger property. All path-connected spaces are connected, but not all connected spaces are path-connected.
*   **Exam Focus:** Be prepared to:
    1.  Use the definition to prove a set is connected or disconnected.
    2.  Apply the theorem that the continuous image of a connected set is connected.
    3.  Identify connected and disconnected subsets of $\mathbb{R}$ and $\mathbb{R}^2$.
    4.  Understand the difference between connectedness and path-connectedness.

Understanding connectedness provides a deeper insight into the structure of metric spaces and is essential for advanced studies in analysis and topology.