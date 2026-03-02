**Subject: METRIC SPACES | Semester: IV**
**Module: Module 2: Concepts in Metric Spaces**
**Topic: Exterior and Boundary Points**

***

### 1. Introduction

In the study of metric spaces, we often want to describe the "position" of a point relative to a given set. We have already encountered **interior points**, which lie deep inside a set with some neighbourhood entirely contained within it. Now, we will define two other fundamental classifications: **exterior points** and **boundary points**. These concepts are crucial for understanding the structure of sets, defining limits, continuity, and eventually, closed and open sets.

---

### 2. Core Concepts

Let \((X, d)\) be a metric space, and let \(A \subseteq X\). The definitions of exterior and boundary points are built upon the concept of an **open ball**, \(B_r(x) = \{ y \in X \mid d(x, y) < r \}\).

#### a) Exterior Point

A point \(x \in X\) is called an **exterior point** of the set \(A\) if there exists an open ball centered at \(x\) that is completely contained in the **complement** of \(A\), denoted \(A^c\).

*   **Formal Definition:** \(x \in X\) is an exterior point of \(A\) if \(\exists \ r > 0\) such that \(B_r(x) \subseteq A^c\).
*   **Interpretation:** An exterior point is "well outside" the set \(A\). It has a neighbourhood that doesn't touch \(A\) at all. It is, in fact, an **interior point of the complement set** \(A^c\).

The set of all exterior points of \(A\) is called the **exterior** of \(A\) and is often denoted by \(\text{ext}(A)\).

#### b) Boundary Point

A point \(x \in X\) is called a **boundary point** of the set \(A\) if **every** open ball centered at \(x\) intersects **both** the set \(A\) and its complement \(A^c\).

*   **Formal Definition:** \(x \in X\) is a boundary point of \(A\) if for every \(r > 0\), \(B_r(x) \cap A \neq \emptyset\) **and** \(B_r(x) \cap A^c \neq \emptyset\).
*   **Interpretation:** A boundary point is on the "edge" of the set \(A\). No matter how small a neighbourhood you take around it, you will always find points that are inside \(A\) and points that are outside \(A\). It is the dividing line between the set and its complement.

The set of all boundary points of \(A\) is called the **boundary** (or frontier) of \(A\) and is denoted by \(\partial A\).

---

### 3. Examples

Let's consider the metric space \((\mathbb{R}^2, d)\), where \(d\) is the standard Euclidean distance (the usual distance in a plane). Let our set be the **closed unit disk**:
\[
A = \{ (x, y) \in \mathbb{R}^2 \mid x^2 + y^2 \leq 1 \}
\]

*   **Exterior Point Example:** Consider the point \(P = (2, 0)\).
    *   Let's take an open ball of radius \(r = 0.5\): \(B_{0.5}(P)\).
    *   Every point in this ball will be at a distance greater than 1 from the origin \((0,0)\). For instance, the closest point in this ball to the origin is at a distance of \(2 - 0.5 = 1.5\).
    *   Therefore, \(B_{0.5}(P) \cap A = \emptyset\), meaning \(B_{0.5}(P) \subseteq A^c\).
    *   **Conclusion:** \(P\) is an **exterior point** of \(A\). All points where \(x^2 + y^2 > 1\) are exterior points.

*   **Boundary Point Example:** Consider the point \(Q = (1, 0)\).
    *   Now, take *any* open ball around \(Q\), no matter how small the radius \(r > 0\).
    *   The ball \(B_r(Q)\) will always contain points *inside* \(A\) (e.g., points slightly to the left of \((1,0)\) along the x-axis) and points *outside* \(A\) (e.g., points slightly to the right of \((1,0)\)).
    *   **Conclusion:** \(Q\) is a **boundary point** of \(A\). The entire unit circle \(x^2 + y^2 = 1\) forms the boundary \(\partial A\) of the disk.

*   **Another Example:** Consider the set of rational numbers \(\mathbb{Q}\) in the metric space \((\mathbb{R}, d)\), with the standard metric \(d(x, y) = |x - y|\).
    *   **What is the boundary of \(\mathbb{Q}\)?**
    *   Take any point \(x \in \mathbb{R}\) and any \(r > 0\). The interval \((x-r, x+r)\) will always contain both rational *and* irrational numbers.
    *   Therefore, **every** real number \(x\) is a boundary point of \(\mathbb{Q}\).
    *   **Conclusion:** \(\partial \mathbb{Q} = \mathbb{R}\). This shows that a set can be dense in the space, and its boundary can be the entire space.

---

### 4. Key Points & Summary

| Concept | Definition | Key Idea |
| :--- | :--- | :--- |
| **Exterior Point** | \(\exists r > 0\) such that \(B_r(x) \subseteq A^c\) | A point with a neighbourhood **completely outside** the set \(A\). It is an interior point of \(A^c\). |
| **Boundary Point** | \(\forall r > 0\), \(B_r(x) \cap A \neq \emptyset\) **and** \(B_r(x) \cap A^c \neq \emptyset\) | A point on the "edge". **Every** neighbourhood intersects **both** \(A\) and its complement. |

*   **Mutually Exclusive & Exhaustive:** For a given set \(A\) in a metric space, any point \(x \in X\) must be exactly one of the following:
    1.  An interior point of \(A\)
    2.  An exterior point of \(A\) (i.e., an interior point of \(A^c\))
    3.  A boundary point of \(A\)

*   **Relation to Closed/Open Sets:** The boundary is a key concept for defining closed sets. A set \(A\) is **closed** if and only if it contains all of its boundary points (\(\partial A \subseteq A\)). A set is **open** if and only if it contains **none** of its boundary points. The boundary itself is always a closed set.

Understanding these point classifications is essential for delving deeper into the topology of metric spaces, including the study of closure, limit points, and connectedness.