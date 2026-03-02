Of course. Here is a comprehensive educational module on Closed Sets in Metric Spaces, tailored for  Engineering students.

# Module 2: Concepts in Metric Spaces
## Topic: Closed Sets

### 1. Introduction

In the previous module, you were introduced to the fundamental concept of a **metric space**—a set where we can measure the distance between any two points. This structure allows us to extend intuitive geometric ideas from Euclidean space (like $\mathbb{R}^n$) to more abstract settings. A critical step in this journey is understanding special types of subsets, notably **open** and **closed sets**. While open sets generalize the idea of an "interior" without its boundary, closed sets are their natural counterpart, formalizing the concept of a set that **includes its entire boundary**. This concept is paramount for deeper topics in analysis, like continuity, convergence, and compactness.

### 2. Core Concepts

#### 2.1. Definition of a Closed Set

Let $(X, d)$ be a metric space. A subset $F \subseteq X$ is said to be **closed** if its **complement**, $F^c = X \setminus F$, is an open set.

This definition is elegant because it directly ties the new concept (closed sets) to a previously understood one (open sets). If you can identify that the complement of a set is open, you immediately know the set itself is closed.

#### 2.2. Limit Points and Closure

To understand closed sets more intuitively, we need the concept of a **limit point** (or an accumulation point).

*   **Definition:** A point $x \in X$ is a **limit point** of a set $A \subseteq X$ if **every open ball** $B(x, r)$ centered at $x$ contains **at least one point of $A$ different from $x$ itself**. That is, $B(x, r) \cap (A \setminus \{x\}) \ne \emptyset$ for all $r > 0$.

*   **Closed Set via Limit Points:** A set $F$ is closed **if and only if** it contains **all** of its limit points. This means there are no points "just outside" F that are arbitrarily close to points inside F; F has "closed" itself off by including all such boundary points.

*   **Closure of a Set:** The **closure** of any set $A$, denoted by $\overline{A}$, is the union of $A$ and the set of all its limit points. Therefore, $\overline{A}$ is always a closed set, and it is the **smallest closed set** containing $A$. A set $A$ is closed if and only if $A = \overline{A}$.

#### 2.3. Relationship with Convergent Sequences

There is a powerful and practical characterization of closed sets using sequences, which is often easier to apply.

*   **Theorem:** A subset $F$ of a metric space $(X, d)$ is closed **if and only if** for every sequence $(x_n)$ in $F$ that converges to a point $x \in X$, the limit $x$ also belongs to $F$.

In simpler terms, a closed set is "closed" under the operation of taking limits. If a sequence of points from a closed set converges, it cannot converge to a point outside the set.

### 3. Examples

Let's consider the metric space $(\mathbb{R}, d)$, where $d(x, y) = |x - y|$ (the standard Euclidean metric).

1.  **Closed Intervals:** The interval $F = [a, b]$ is closed.
    *   *Reason:* Its complement is $(-\infty, a) \cup (b, \infty)$, which is a union of two open sets (and hence open).
    *   *Limit Points:* Every point in $[a, b]$ is a limit point. The points $a$ and $b$ are also limit points (e.g., any ball around $a$ contains points greater than $a$ that are in $[a, b]$). Since $F$ contains all of them, it is closed.

2.  **Singleton Sets:** Any set containing a single point, $F = \{c\}$, is closed.
    *   *Reason:* Its complement is $(-\infty, c) \cup (c, \infty)$, which is open.
    *   *Limit Points:* Does $\{c\}$ have any limit points? Consider any point $x \ne c$. You can find an open ball around $x$ small enough that it doesn't include $c$ (e.g., $r < |x-c|$). The point $c$ itself is *not* a limit point because the definition requires a point *different* from $x$. Therefore, the set of limit points is empty. Since it contains all (zero) of its limit points, it is closed.

3.  **Finite Sets:** Any finite set $F = \{c_1, c_2, ..., c_n\}$ is closed. This is because it is a finite union of closed sets (singleton sets), and a finite union of closed sets is always closed.

4.  **The Whole Space and the Empty Set:** In any metric space $(X, d)$, the entire set $X$ and the empty set $\emptyset$ are both closed (and also open). This is a special case.
    *   $X$ is closed because its complement $\emptyset$ is open.
    *   $\emptyset$ is closed because its complement $X$ is open.

5.  **Open Intervals are NOT Closed:** The interval $A = (a, b)$ is **not closed**.
    *   *Reason:* Its complement is $(-\infty, a] \cup [b, \infty)$. The set $(-\infty, a]$ is not open because any open ball around $a$ will include points less than $a$ (which are in the complement) but also points greater than $a$ (which are not in the complement). Since the complement is not open, $A$ is not closed.
    *   *Limit Point:* The point $b$ is a limit point of $A$ but is not contained in $A$. This confirms that $A$ is not closed.

### 4. Key Points & Summary

*   **Definition:** A set $F$ in a metric space $(X, d)$ is **closed** if its complement $X \setminus F$ is **open**.
*   **Equivalent Characterization:** A set $F$ is closed **if and only if** it contains **all** of its limit points.
*   **Sequential Characterization:** A set $F$ is closed **if and only if** the limit of every convergent sequence in $F$ is also in $F$.
*   **Closure:** The **closure** $\overline{A}$ of a set $A$ is the smallest closed set containing $A$, formed by adding all limit points of $A$ to it.
*   **Important Properties:**
    *   The whole space $X$ and the empty set $\emptyset$ are always closed.
    *   Arbitrary **intersections** of closed sets are closed.
    *   Finite **unions** of closed sets are closed. (Infinite unions need not be closed).
*   **Not Mutually Exclusive:** A set can be both open and closed (like $X$ and $\emptyset$), or neither (like the interval $[0, 1)$ in $\mathbb{R}$).

Understanding closed sets is crucial as they form the building blocks for more advanced concepts like **compact sets** and **complete metric spaces**, which are foundational in engineering mathematics for optimization, solving differential equations, and numerical analysis.