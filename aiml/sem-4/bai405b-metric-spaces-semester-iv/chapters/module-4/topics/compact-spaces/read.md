Of course. Here is a comprehensive educational note on **Compact Spaces** for  Engineering Students, Semester IV, following your specified structure.

# Module 4: Compactness - Compact Spaces

## 1. Introduction

In the study of metric spaces, we often want to understand the behavior of sequences, functions, and sets under various conditions. **Compactness** is a fundamental topological concept that generalizes the idea of "closed and bounded" sets from Euclidean space (like $\mathbb{R}^n$) to more abstract metric spaces. It is an extremely powerful property because it often allows us to pass from *local* properties (things that are true near each point) to *global* properties (things that are true for the entire set). This has profound implications in analysis, optimization, and numerical methods.

## 2. Core Concepts

### 2.1. Open Covers and Finite Subcovers

The formal definition of compactness is based on the idea of "covers."

*   **Open Cover:** Let $(X, d)$ be a metric space and let $A \subseteq X$. An **open cover** for $A$ is a collection $\{G_\alpha\}$ of open subsets of $X$ such that $A \subseteq \bigcup_\alpha G_\alpha$.
*   **Finite Subcover:** A **finite subcover** is a finite subcollection of the open cover $\{G_\alpha\}$ that still covers $A$.

### 2.2. Definition of Compactness

A subset $K$ of a metric space $(X, d)$ is said to be **compact** if **every open cover** of $K$ has a **finite subcover**.

This is often called the **Heine-Borel** property. In simpler terms, no matter how you try to "cover" the set $K$ with open sets (even an infinite number of them), you can always find a finite number of those open sets that do the job.

### 2.3. Key Theorems and Properties

*   **Compactness in $\mathbb{R}^n$ (Heine-Borel Theorem):** A subset $K$ of $\mathbb{R}^n$ (with the usual Euclidean metric) is compact **if and only if** it is **closed and bounded**. This is the most intuitive and important example for engineers. The closed interval $[a, b]$ is compact in $\mathbb{R}$.
*   **Continuous Functions on Compact Sets:** If $f: X \rightarrow Y$ is a **continuous function** and $K \subseteq X$ is **compact**, then its image $f(K)$ is also compact in $Y$. Furthermore, if $f$ is a real-valued function ($Y = \mathbb{R}$), then $f$ **attains its maximum and minimum** on $K$. This is crucial for optimization problems.
*   **Closed subsets:** Every closed subset of a compact space is itself compact.
*   **Bolzano-Weierstrass Property:** In a compact metric space, **every sequence has a convergent subsequence** that converges to a point *within the set*. This is often an easier way to prove or disprove compactness.

### 2.4. Examples

**Example 1: Compact Set**
The set $K = \{ x \in \mathbb{R} \;|\; x^2 + y^2 \leq 1 \}$ (the closed unit disk) in $\mathbb{R}^2$ is compact. It is closed and bounded.

**Example 2: Non-Compact Sets**
1.  $\mathbb{R}$ itself is **not compact**. The open cover $\{ (-n, n) \;|\; n \in \mathbb{N} \}$ has no finite subcover.
2.  The open interval $(0, 1)$ in $\mathbb{R}$ is **not compact**. Consider the open cover $\{ (1/n, 1) \;|\; n \in \mathbb{N}, n \geq 2 \}$. No finite subcollection can cover all points arbitrarily close to 0.
3.  An infinite set $X$ with the discrete metric ($d(x,y)=1$ if $x \neq y$) is **not compact** if $X$ is infinite. The open cover of all singleton sets $\{\{x\} \;|\; x \in X\}$ has no finite subcover.

**Example 3: Sequential Compactness**
Consider the sequence $x_n = \frac{1}{n}$ in the metric space $(0, 1]$. This sequence converges to $0$, but $0$ is not in the set $(0, 1]$. Therefore, while the sequence has a convergent subsequence (itself), the limit point is outside the set. This is a manifestation of the set *not* being compact (which we also saw in Example 2.2). In the compact set $[0, 1]$, the same sequence converges to $0$, which *is* in the set.

## 3. Key Points & Summary

*   **Definition:** A set $K$ is compact if every open cover has a finite subcover.
*   **Heine-Borel Theorem:** In $\mathbb{R}^n$, compact = closed + bounded. This is the most practical test.
*   **Sequential Compactness:** In metric spaces (though not in general topological spaces), compactness is equivalent to the Bolzano-Weierstrass property: every sequence has a convergent subsequence with a limit *in the set*.
*   **Why it matters:**
    *   **Guarantees Extrema:** A continuous real-valued function on a compact set **must** attain a maximum and a minimum value.
    *   **Enables Global Conclusions:** Local properties can often be extended to the whole compact set.
    *   **Fundamental in Analysis:** Essential for proving important results in analysis, such as the uniform continuity of continuous functions on compact sets.

**In essence, compactness is a "finiteness" property that allows us to tame infinite sets and processes, making them manageable for analysis and application.**