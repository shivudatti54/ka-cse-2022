Of course. Here is a comprehensive educational guide on the "Diameter of a Set" for  Engineering students, formatted in Markdown.

# **Diameter of a Set in Metric Spaces**

**Subject:** Metric Spaces
**Semester:** IV
**Module:** Module 2: Concepts in Metric Spaces

---

## **1. Introduction**

In Module 1, we learned that a metric space is a set equipped with a function (a metric) that defines the distance between any two of its elements. This allows us to analyze sets not just as collections of points, but as geometric objects with shape and size. The **diameter** of a set is a fundamental concept that quantifies the overall "spread" or "size" of a set within a metric space. It is a direct extension of the intuitive idea of the diameter of a circle in the Euclidean plane to any abstract metric space.

## **2. Core Concept & Definition**

Let $(X, d)$ be a metric space.

**Definition:** The **diameter** of a non-empty subset $A$ of $X$ (denoted by $diam(A)$) is defined as the least upper bound (supremum) of the set of all distances between pairs of points in $A$.

Mathematically, it is expressed as:
$$
diam(A) = \sup \{ d(x, y) : x, y \in A \}
$$

In simpler terms, the diameter is the **largest possible distance** that can exist between any two points in the set $A$. It's crucial to note the use of the **supremum** ($\sup$) instead of the maximum ($\max$). This is because for some sets, the largest distance might not be achieved by any two specific points, but we can still find distances arbitrarily close to a certain upper bound.

### **Key Implications:**

*   **Non-Negativity:** Since $d(x, y) \geq 0$ for all $x, y$, it follows that $diam(A) \geq 0$.
*   **A Singleton Set:** If $A = \{a\}$, a set with only one point, then there are no two distinct points to measure a distance. The only distance is $d(a, a) = 0$. Therefore, $diam(\{a\}) = 0$.
*   **Boundedness:** A set $A$ in a metric space is said to be **bounded** if it has a finite diameter, i.e., $diam(A) < \infty$. Conversely, if $diam(A) = \infty$, the set is **unbounded**.

## **3. Examples**

Let's explore this concept with examples in different metric spaces.

**Example 1: In $\mathbb{R}$ with the standard metric ($d(x, y) = |x - y|$)**

*   Let $A = (1, 5)$, an open interval.
    *   The farthest two points are 1 and 5. The distance between them is $|5-1| = 4$.
    *   Can we find a pair with a distance greater than 4? No. Even though 1 and 5 are not included in the open set, we can find pairs like 1.001 and 4.999 whose distance is arbitrarily close to 4.
    *   Therefore, $diam(A) = \sup\{ |x-y| : x, y \in (1, 5) \} = 4$.
*   Let $B = \{2, 7, 9, 11\}$, a finite set.
    *   We simply find the maximum of all pairwise distances: $d(2, 11) = 9$ is the largest.
    *   Here, the supremum is achieved (it's a maximum), so $diam(B) = 9$.

**Example 2: In $\mathbb{R}^2$ with the Euclidean metric ($d((x_1,y_1), (x_2,y_2)) = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$)**

*   Let $A = \{ (x, y) \in \mathbb{R}^2 : x^2 + y^2 < 9 \}$, an open disk of radius 3 centered at the origin.
    *   The farthest two points lie on the boundary. The maximum distance is the length of the diameter of the circle, which is $2 \times radius = 6$.
    *   Since the set is open, no two points *inside* the disk actually achieve this distance, but we can get infinitely close to it.
    *   Therefore, $diam(A) = 6$.

**Example 3: An Unbounded Set**

*   Let $A = \mathbb{N}$, the set of natural numbers, in $\mathbb{R}$ with the standard metric.
    *   The distance between points can be arbitrarily large (e.g., $d(1, 1000) = 999$, $d(1, 10^6) = 999999$, ...).
    *   There is no finite upper bound on these distances.
    *   Therefore, $diam(\mathbb{N}) = \infty$, and $\mathbb{N}$ is an unbounded set.

## **4. Key Properties and Summary**

| Property | Description |
| :--- | :--- |
| **Definition** | $diam(A) = \sup \{ d(x, y) : x, y \in A \}$ |
| **Singleton Set** | $diam(\{a\}) = 0$ |
| **Relation to Boundedness** | A set $A$ is **bounded** **if and only if** $diam(A) < \infty$. |
| **Nested Sets** | If $A \subseteq B$, then $diam(A) \leq diam(B)$. The diameter of a subset cannot be larger than the diameter of the set containing it. |
| **Triangle Inequality** | For any $x, y, z \in A$, $d(x, y) \leq d(x, z) + d(z, y) \leq diam(A) + diam(A) = 2 \cdot diam(A)$. This is often useful in proofs. |

### **Summary**

*   The **diameter** is a measure of the maximum possible distance between any two points in a set.
*   It is defined using the **supremum** to account for sets where the maximum distance is not attained (e.g., open intervals).
*   A set is **bounded** if its diameter is finite.
*   Understanding the diameter is crucial for later topics in analysis, such as the **Nested Set Theorem** and concepts in **topology** (e.g., total boundedness).

This concept provides a powerful tool to characterize and compare the "size" of subsets within any metric space, forming a foundational block for more advanced analysis in engineering mathematics.