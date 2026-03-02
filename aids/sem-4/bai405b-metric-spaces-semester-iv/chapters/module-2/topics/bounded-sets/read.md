Of course. Here is a comprehensive educational note on **Bounded Sets in Metric Spaces** for  Engineering students, formatted as requested.

# Bounded Sets in Metric Spaces

## 1. Introduction

In the study of metric spaces, we often need to describe the "size" or "spread" of a set. The concept of **boundedness** is a fundamental geometric property that generalizes the intuitive idea of a set being of finite extent. For engineering applications, such as in signal processing (where signals are bounded functions) or optimization (searching for minima/maxima within a confined region), understanding bounded sets is crucial. This module defines bounded sets and explores their key properties within a general metric space.

## 2. Core Concepts

### 2.1. Definition of a Bounded Set

Let $(X, d)$ be a metric space. A non-empty subset $A \subseteq X$ is said to be a **bounded set** if its real-world intuition holds true: the distance between any two points in $A$ is not infinite. Formally, we define it using the concept of diameter.

The **diameter** of a set $A$ is defined as:
$$\text{diam}(A) = \sup \{ d(x, y) : x, y \in A \}$$
This represents the least upper bound of all possible distances between points in $A$.

A set $A$ is called **bounded** if its diameter is finite.
$$\text{A is bounded} \iff \text{diam}(A) < \infty$$

### 2.2. Equivalent Definition (Using a Fixed Point)

An equivalent and often more practical way to define boundedness is by "pinning" one point. A set $A$ is bounded if it can be entirely enclosed within a ball of finite radius around some fixed point (often an arbitrary point in $X$, or a specific point like the origin $0$ in $\mathbb{R}^n$).

Formally, $A \subseteq X$ is bounded **if and only if** there exists a point $x_0 \in X$ and a real number $R > 0$ such that:
$$A \subseteq B(x_0, R)$$
which means for every $a \in A$, we have $d(a, x_0) < R$.

It is important to note that the choice of $x_0$ does not matter. If a set can be enclosed in a ball centered at one point, it can be enclosed in a (possibly larger) ball centered at any other point.

## 3. Examples

Let's solidify these definitions with examples in familiar metric spaces.

**Example 1: Bounded Sets in $\mathbb{R}$ (with usual metric $d(x, y) = |x-y|$)**
*   The open interval $A = (2, 5)$ is bounded.
    *   *Reason:* $\text{diam}(A) = 3$ (since $\sup |x-y| = 5-2=3$). Equivalently, $A \subseteq B(3.5, 2)$ since for any $x \in (2,5)$, $|x - 3.5| < 1.5$.
*   The set $A = \{\frac{1}{n} : n \in \mathbb{N}\} = \{1, \frac{1}{2}, \frac{1}{3}, ...\}$ is bounded.
    *   *Reason:* All points lie in the interval $(0, 1]$. $\text{diam}(A) = 1$. It is contained in $B(0, 2)$.
*   The set $\mathbb{N}$ (natural numbers) is **NOT** bounded in $\mathbb{R}$.
    *   *Reason:* $\text{diam}(\mathbb{N})$ is not finite, as the distance between, say, $1$ and $N$ can be made arbitrarily large by choosing a large $N$.

**Example 2: Bounded Sets in $\mathbb{R}^2$ (with Euclidean metric $d_2$)**
*   The unit disk $A = \{(x,y) : x^2 + y^2 \leq 1\}$ is bounded. Its diameter is $2$.
*   Any finite set of points is bounded.
*   The entire plane $\mathbb{R}^2$ is **unbounded**.

**Example 3: A seemingly large but bounded set**
Consider the metric space $(C[0, 1], d_\infty)$ of continuous functions on $[0,1]$ with the sup-metric: $d_\infty(f, g) = \sup_{x \in [0,1]} |f(x) - g(x)|$.

Let $A$ be the set of all functions $f$ such that $|f(x)| < 5$ for all $x \in [0,1]$. This set is bounded.
*   *Reason:* For any two functions $f, g \in A$, the distance $d_\infty(f, g) = \sup |f(x)-g(x)| \leq \sup (|f(x)| + |g(x)|) < 5 + 5 = 10$. Therefore, $\text{diam}(A) \leq 10$, which is finite. Equivalently, if we take the zero function $z(x)=0$ as our center, $A \subseteq B(z, 6)$.

## 4. Key Points & Summary

*   **Definition:** A set $A$ in a metric space $(X, d)$ is **bounded** if $\text{diam}(A) = \sup \{ d(x, y) : x, y \in A \} < \infty$.
*   **Equivalent Definition:** $A$ is bounded if there exists some $x_0 \in X$ and $R > 0$ such that $A \subseteq B(x_0, R)$.
*   **Finite Sets are Always Bounded:** Any finite collection of points has a finite maximum distance between them, hence a finite diameter.
*   **Subsets of Bounded Sets:** If $A$ is bounded and $B \subseteq A$, then $B$ is also bounded.
*   **Union of Bounded Sets:** The union of a **finite** number of bounded sets is also bounded.
*   **Unboundedness:** Common examples of unbounded sets include the entire space $X$ (if $X$ is not a finite set itself), $\mathbb{N}$ and $\mathbb{Z}$ in $\mathbb{R}$, and infinite lines/planes in $\mathbb{R}^n$.
*   **Not a Topological Property:** Boundedness depends on the specific metric. A set can be bounded under one metric but unbounded under another. It is a **metric property**, not a topological one.

Understanding boundedness is a prerequisite for more advanced topics in analysis, such as compactness, completeness, and the study of continuous functions on metric spaces.