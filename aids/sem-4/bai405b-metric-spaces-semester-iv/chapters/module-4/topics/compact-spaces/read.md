Of course. Here is a comprehensive educational note on **Compact Spaces** for  Engineering Students, Semester IV.

# Module 4: Compactness - Compact Spaces

## 1. Introduction

In the study of metric spaces, we often need to generalize powerful properties of closed and bounded intervals in $\mathbb{R}$ (like the Heine-Borel Theorem) to more abstract spaces. **Compactness** is one of the most fundamental and important concepts in topology and analysis. It provides a precise way to say that a space is "small" or "finite" in a very useful topological sense, allowing us to extend local properties to global ones and guaranteeing the existence of maximum and minimum values for continuous functions. For engineers, this concept underpins many optimization and convergence theorems used in numerical methods and control theory.

## 2. Core Concepts

### 2.1. Open Covers and Finite Subcovers

The definition of compactness is built upon two key ideas:

*   **Open Cover:** Let $(X, d)$ be a metric space and let $A \subseteq X$. A collection $\mathcal{U} = \{U_i\}_{i \in I}$ of open subsets of $X$ is called an **open cover** of $A$ if $A \subseteq \bigcup_{i \in I} U_i$.
*   **Finite Subcover:** A **finite subcover** is a finite subcollection of $\mathcal{U}$, say $\{U_1, U_2, ..., U_n\} \subseteq \mathcal{U}$, that still covers $A$ (i.e., $A \subseteq U_1 \cup U_2 \cup ... \cup U_n$).

**Example:** Consider the set $A = (0, 1)$ in $\mathbb{R}$. One open cover is $\mathcal{U} = \{ (1/n, 1) : n \in \mathbb{N}, n \geq 2 \}$. Can we find a finite subcover? If we take a finite collection $\{(1/n_1, 1), (1/n_2, 1), ..., (1/n_k, 1)\}$, let $N = \max\{n_1, n_2, ..., n_k\}$. The union of these sets is just $(1/N, 1)$, which does not include points very close to 0 (e.g., $1/(N+1)$ is not covered). Therefore, *no* finite subcover exists for this particular cover.

### 2.2. Definition of a Compact Space

A metric space $(X, d)$ is said to be **compact** if **every** open cover of $X$ has a **finite subcover**.

A subset $A$ of a metric space $(X, d)$ is compact if it is compact as a subspace (i.e., with the metric $d$ restricted to $A$). This is equivalent to saying: for any collection of open sets in $X$ whose union contains $A$, there is a finite subcollection whose union still contains $A$.

### 2.3. Key Theorems and Properties

*   **Closed and Bounded in $\mathbb{R}^n$ (Heine-Borel Theorem):** A subset $A$ of $\mathbb{R}^n$ (with the usual Euclidean metric) is compact **if and only if** it is **closed and bounded**. This is the most familiar characterization for engineering students.
    *   $[a, b]$ is compact.
    *   $(a, b)$ is not compact (it is bounded but not closed).
    *   $\mathbb{R}$ is not compact (it is closed but not bounded).

*   **Continuous Images of Compact Sets:** If $f: (X, d) \to (Y, \rho)$ is a continuous function and $K \subseteq X$ is compact, then its image $f(K) \subseteq Y$ is also compact. This leads directly to the Extreme Value Theorem: a continuous real-valued function on a compact set attains its **maximum and minimum values**.

*   **Closed Subsets of Compact Sets:** Every **closed** subset of a **compact** set is itself compact.

*   **Sequential Compactness (Bolzano-Weierstrass Property):** In metric spaces (though not in general topological spaces), compactness is equivalent to **sequential compactness**. A set $K$ is sequentially compact if **every sequence** in $K$ has a **convergent subsequence** whose limit lies in $K$. This provides an intuitive way to think about compactness: a set is compact if you cannot "spread out" an infinite sequence—some points must necessarily cluster together.

## 3. Examples

1.  **Compact:** The interval $[0, 1]$ in $\mathbb{R}$ is compact (by Heine-Borel: closed and bounded). A sphere $\{(x,y,z) : x^2+y^2+z^2 = 1\}$ in $\mathbb{R}^3$ is compact.

2.  **Not Compact:**
    *   $\mathbb{R}$ itself is not compact. The open cover $\{ (-n, n) : n \in \mathbb{N} \}$ has no finite subcover.
    *   The set $\{1, 1/2, 1/3, ..., 1/n, ...\}$ in $\mathbb{R}$ is **not compact**. While it is bounded, it is not closed (because the limit point $0$ is not in the set). The sequence $(1/n)$ itself has no convergent subsequence whose limit is *inside* the set.
    *   The set $\{0\} \cup \{1, 1/2, 1/3, ..., 1/n, ...\}$ **is compact**. It is closed and bounded. Notice that the sequence $(1/n)$ now has a convergent subsequence (itself) whose limit $0$ is in the set.

## 4. Key Points & Summary

*   **Definition:** A space is compact if **every** open cover has a **finite subcover**.
*   **Main Characterization ($\mathbb{R}^n$):** In $\mathbb{R}^n$, compact = **closed + bounded** (Heine-Borel Theorem).
*   **Alternative View (Metric Spaces):** Compactness is equivalent to the **Bolzano-Weierstrass property**: every sequence has a convergent subsequence.
*   **Why it Matters:**
    *   **Extreme Value Theorem:** Guarantees max/min values for continuous functions on compact sets, crucial for optimization.
    *   **Uniform Continuity:** A continuous function on a compact metric space is automatically **uniformly continuous**.
    *   **Finite Dimension:** Many properties of finite-dimensional vector spaces (like $\mathbb{R}^n$) are linked to the compactness of their closed and bounded subsets.
*   **Non-Example Remember:** $(0, 1)$ is **not compact**. This is a common point of confusion. It is bounded but not closed, and we explicitly found an open cover with no finite subcover.

Understanding compactness is key to moving from the concrete setting of $\mathbb{R}$ and $\mathbb{R}^n$ to the more abstract and powerful world of metric spaces and functional analysis.