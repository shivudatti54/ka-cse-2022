Of course. Here is a comprehensive educational note on "Open and Closed Spheres" for  Engineering students, structured as requested.

***

### **Module 2: Concepts in Metric Spaces**
#### **Topic: Open Spheres and Closed Spheres**

---

#### **1. Introduction**

In the previous module, we defined a **metric space** as a set `X` equipped with a function `d` (the metric) that measures the distance between any two points. This simple concept of "distance" allows us to generalize fundamental ideas like convergence, continuity, and limits from calculus to vastly more abstract spaces. The building blocks for these ideas are **open spheres** and **closed spheres**. Think of them as the generalized, rigorous versions of "open balls" and "closed balls" you know from 2D or 3D space.

---

#### **2. Core Concepts**

##### **2.1. Open Sphere (or Open Ball)**

An open sphere is the set of all points inside a certain distance from a central point, *excluding* the boundary itself.

*   **Formal Definition:** Let `(X, d)` be a metric space. For a point `a ∈ X` and a real number `r > 0`, the **open sphere** (or open ball) centered at `a` with radius `r` is defined as:
    `S(a, r) = { x ∈ X | d(x, a) < r }`

*   **Interpretation:** It contains all points `x` in the space `X` whose distance from the center `a` is *strictly less than* `r`. The boundary, where `d(x, a) = r`, is not included.

##### **2.2. Closed Sphere (or Closed Ball)**

A closed sphere is the set of all points inside a certain distance from a central point, *including* the boundary.

*   **Formal Definition:** For a point `a ∈ X` and a real number `r > 0`, the **closed sphere** (or closed ball) centered at `a` with radius `r` is defined as:
    `S[a, r] = { x ∈ X | d(x, a) ≤ r }`

*   **Interpretation:** It contains all points `x` in the space `X` whose distance from the center `a` is *less than or equal to* `r`.

**Key Difference:** The crucial distinction lies in the inequality: `<` for open, `≤` for closed. This seemingly minor difference has profound implications for concepts like open sets, closed sets, and limit points later on.

---

#### **3. Examples**

Let's visualize these concepts in different metric spaces.

**Example 1: The Real Line (ℝ with usual metric)**
Consider the metric space `(ℝ, d)` where `d(x, y) = |x - y|`.

*   **Open Sphere:** `S(5, 2) = { x ∈ ℝ | |x - 5| < 2 } = (3, 7)`
    This is an open interval on the number line, from 3 to 7, *not including* the endpoints 3 and 7.

*   **Closed Sphere:** `S[5, 2] = { x ∈ ℝ | |x - 5| ≤ 2 } = [3, 7]`
    This is a closed interval, which *includes* the endpoints 3 and 7.

**Example 2: The Plane (ℝ² with Euclidean metric)**
Consider `(ℝ², d)` where `d((x₁,y₁), (x₂,y₂)) = √[(x₂-x₁)² + (y₂-y₁)²]`.

*   **Open Sphere:** `S( (0,0), 1 )` is the set of all points *inside* the circle `x² + y² = 1`. The circle itself (the boundary) is not part of this set.
*   **Closed Sphere:** `S[ (0,0), 1 ]` is the set of all points *inside and on* the circle `x² + y² = 1`.

**Example 3: A Discrete Metric Space**
Let `X` be any non-empty set with the discrete metric:
`d(x, y) = { 0 if x = y, 1 if x ≠ y }`

*   **Open Sphere:** `S(a, 1) = { x ∈ X | d(x, a) < 1 } = {a}`. Since the metric only gives values 0 or 1, the only point with distance < 1 is the center `a` itself.
*   **Closed Sphere:** `S[a, 1] = { x ∈ X | d(x, a) ≤ 1 } = X`. Every point in `X` is either the center (distance 0) or a different point (distance 1, which is ≤ 1).

This example shows how these concepts can behave very differently in non-standard metric spaces.

---

#### **4. Key Points & Summary**

| Feature | Open Sphere `S(a, r)` | Closed Sphere `S[a, r]` |
| :--- | :--- | :--- |
| **Definition** | `{ x ∈ X | d(x, a) < r }` | `{ x ∈ X | d(x, a) ≤ r }` |
| **Boundary** | **Excluded** | **Included** |
| **Notation** | Parentheses `S( , )` | Square Brackets `S[ , ]` |
| **Analogy** | Interior of a circle/sphere | A solid ball including its skin |
| **Purpose** | Fundamental building block for defining **open sets**. | Used to define **closed sets** and **bounded sets**. |

*   **Why is this important?** These spheres are the "neighborhoods" that allow us to define:
    *   **Interior Point:** A point `a` is an interior point of a set `M` if there *exists* some open sphere `S(a, r)` entirely contained within `M`.
    *   **Open Set:** A set `M` is open if *every* point in `M` is an interior point. (e.g., an open sphere is itself an open set).
    *   **Closed Set:** A set is closed if its complement is open. Closed spheres are classic examples of closed sets.

Understanding open and closed spheres is the crucial first step toward grasping the topology of metric spaces, which is essential for advanced engineering mathematics, optimization, and numerical analysis.