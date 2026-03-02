Of course. Here is a comprehensive educational module on the "Diameter of a Set," tailored for  engineering students.

# Module 2: Concepts in Metric Spaces
## Topic: Diameter of a Set

### 1. Introduction

In the study of metric spaces, we are often interested in the "size" or "spread" of a subset. While concepts like distance between two points are fundamental, the **diameter** of a set provides a single number that quantifies the maximum possible distance between any two points within that set. It is a crucial concept for understanding boundedness, convergence, and the geometry of sets within a metric space.

### 2. Core Concept: Definition

Let $(X, d)$ be a metric space, and let $A$ be a non-empty subset of $X$.

The **diameter** of the set $A$ is defined as the least upper bound (supremum) of the distances between all possible pairs of points in $A$. Mathematically, it is denoted and defined as:

$$
\text{diam}(A) = \sup \{ d(x, y) : x, y \in A \}
$$

In simpler terms, the diameter represents the greatest distance that can exist between any two points in the set $A$. If $A$ contains only one point, by convention, its diameter is $0$.

**Important Note:** The diameter is always a non-negative real number. However, if the set is unbounded (meaning the distances between points can grow infinitely large), the diameter is defined to be **infinity** ($\infty$).

### 3. Visualizing the Diameter

Think of the set $A$ as a cluster of points. The diameter is the length of the longest possible "chord" you can draw through this cluster. It's important to note that the points forming this maximum distance must both lie *within* the set $A$.

For a circle in the Euclidean plane $\mathbb{R}^2$ (with the standard metric $d((x_1, y_1), (x_2, y_2)) = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$), the diameter in the geometric sense (the longest chord through the center) coincides perfectly with the metric space definition of diameter.

### 4. Key Properties and Theorems

1.  **Relation to Boundedness:** A set $A$ in a metric space is called **bounded** if it has a finite diameter. Conversely, if $\text{diam}(A) = \infty$, the set is unbounded.
    *   *Example:* The set $A = \{1, 1/2, 1/3, 1/4, ...\}$ in $\mathbb{R}$ is bounded ($\text{diam}(A) = 1 - 0 = 1$).
    *   *Example:* The set $\mathbb{N}$ (natural numbers) in $\mathbb{R}$ is unbounded ($\text{diam}(\mathbb{N}) = \infty$).

2.  **Nested Sets Property:** If $A \subseteq B$, then $\text{diam}(A) \leq \text{diam}(B)$. A subset cannot be "wider" than the set that contains it.

3.  **Triangle Inequality for Diameter:** For any two non-empty subsets $A$ and $B$ of $X$, the following holds:
    $$
    \text{diam}(A \cup B) \leq \text{diam}(A) + \text{diam}(B) + d(A, B)
    $$
    where $d(A, B) = \inf \{d(a, b) : a \in A, b \in B\}$ is the distance between the sets $A$ and $B$. This is a powerful tool for estimating the diameter of a union.

### 5. Worked Examples

**Example 1: Finite Set in $\mathbb{R}$**
Consider the set $A = \{ -3, 0, 5, 2 \}$ in $\mathbb{R}$ with the standard metric $d(x, y) = |x - y|$.
*   The distances between all pairs are: $|{-3-0}|=3$, $|{-3-5}|=8$, $|{-3-2}|=5$, $|{0-5}|=5$, $|{0-2}|=2$, $|{5-2}|=3$.
*   The supremum of these distances is $8$.
*   Therefore, $\text{diam}(A) = 8$.

**Example 2: Open and Closed Balls**
Consider the metric space $\mathbb{R}^2$ with the standard Euclidean metric.
*   Let $B = \{ (x, y) : x^2 + y^2 < 9 \}$ be an open ball of radius $3$.
    *   Its diameter is $6$. Note that no two points inside the ball actually achieve this distance, but we can get arbitrarily close to it. The supremum is still $6$.
*   Let $\overline{B} = \{ (x, y) : x^2 + y^2 \leq 9 \}$ be the corresponding closed ball.
    *   Its diameter is also $6$, and in this case, there exist points (e.g., $(3,0)$ and $(-3,0)$) for which $d(x, y) = 6$.

**Example 3: A Different Metric**
Consider $\mathbb{R}^2$ with the **taxicab metric**: $d((x_1, y_1), (x_2, y_2)) = |x_2 - x_1| + |y_2 - y_1|$.
*   The set $A = \{ (x, y) : |x| + |y| \leq 1 \}$ (a diamond shape).
*   What is its diameter? The points $(1, 0)$ and $(-1, 0)$ are in $A$. The distance between them is $|{-1-1}| + |{0-0}| = 2$.
*   Can we find a pair with a larger distance? Try $(0,1)$ and $(0,-1)$: distance = $|0-0| + |{-1-1}| = 2$. This is the maximum.
*   Therefore, $\text{diam}(A) = 2$.

### 6. Summary and Key Points

*   **Definition:** The diameter of a non-empty set $A$ in a metric space $(X, d)$ is $\text{diam}(A) = \sup \{ d(x, y) : x, y \in A \}$.
*   **Boundedness:** A set is **bounded** if and only if its diameter is finite.
*   **Supremum vs. Maximum:** The diameter is a *supremum*, not necessarily a maximum. The greatest distance may not be achieved by any two points in the set (e.g., in an open ball).
*   **Metric-Dependent:** The value of the diameter depends on the metric being used. A set can have different diameters in different metric spaces.
*   **Application:** This concept is fundamental in analysis for defining totally bounded sets and is a key step in proving important theorems like the **Heine-Borel Theorem**.

Understanding the diameter provides a powerful tool for analyzing the "size" and shape of sets in the abstract world of metric spaces, with direct applications in numerical analysis, optimization, and computer graphics.