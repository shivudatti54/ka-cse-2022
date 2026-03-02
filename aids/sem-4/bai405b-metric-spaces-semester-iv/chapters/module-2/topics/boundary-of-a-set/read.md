**Subject: METRIC SPACES | Semester: IV**
**Module: Module 2: Concepts in Metric Spaces**
**Topic: Boundary of a Set**

---

# Boundary of a Set in a Metric Space

### 1. Introduction

In the study of metric spaces, we often want to understand the "shape" and "edges" of a set. We have already encountered concepts like *interior points* (points completely surrounded by the set) and *limit points* (points arbitrarily close to the set). The **boundary** of a set is a fundamental concept that precisely defines its frontier or its "skin." It is the set of points that mark the absolute division between the set and its complement, where one can approach from both inside and outside.

---

### 2. Core Concepts

#### 2.1. Formal Definition

Let **(X, d)** be a metric space, and let **A** be any subset of **X**. A point **x ∈ X** is called a **boundary point** of **A** if **every open ball** (or neighbourhood) centered at **x** intersects **both** the set **A** and its complement **Aᶜ = X \ A**.

In other words, no matter how small you choose an ε > 0, the open ball **B(x, ε)** must contain **at least one point from A** and **at least one point not from A**.

The set of all boundary points of **A** is denoted by **∂A** (sometimes **bd(A)** or **fr(A)**).

**Mathematically:**
**∂A = { x ∈ X | ∀ ε > 0, B(x, ε) ∩ A ≠ ∅ and B(x, ε) ∩ Aᶜ ≠ ∅ }**

#### 2.2. Key Observations from the Definition

1.  **Neutrality:** A boundary point **x** does not need to be inside **A**. It can belong to **A** or to **Aᶜ**. The definition is concerned solely with the *proximity* of **x** to both **A** and its complement.
2.  **Closure and Interior:** The boundary can be defined using previously learned concepts:
    *   **∂A = \(\overline{A}\) \ A°**
    This means the boundary of **A** is the closure of **A** (all limit points of A) minus its interior (all interior points of A). This is a very useful characterization for proofs and visual understanding.
3.  **Relationship with other concepts:**
    *   Every boundary point of **A** is also a limit point of **A** and a limit point of **Aᶜ**. Therefore, **∂A ⊂ \(\overline{A}\)** and **∂A ⊂ \(\overline{Aᶜ}\)**.
    *   The closure of a set is the union of its interior and its boundary: **\(\overline{A}\) = A° ∪ ∂A**.

---

### 3. Examples

Let’s consider the metric space **(ℝ, d)**, where **d** is the standard Euclidean metric (**d(x,y) = |x-y|**).

**Example 1: An Interval**
Let **A = (0, 1]**, the half-open interval from 0 to 1.
*   **Interior (A°):** (0, 1)
*   **Closure (\(\overline{A}\)):** [0, 1]
*   **Boundary (∂A):** Using the formula ∂A = \(\overline{A}\) \ A° = [0,1] \ (0,1) = **{0, 1}**.
    *   **x = 0:** Every ball B(0, ε) = (-ε, ε) contains points *greater than 0* (which are in A) and points *less than 0* (which are in Aᶜ). So, 0 is a boundary point.
    *   **x = 1:** Similarly, B(1, ε) contains points in (1-ε, 1] (in A) and points in (1, 1+ε) (in Aᶜ). So, 1 is a boundary point.
    *   **x = 0.5:** You can find a small ball (e.g., B(0.5, 0.1)) that is entirely contained within A. Since it doesn't intersect Aᶜ, 0.5 is *not* a boundary point.

**Example 2: A Finite Set**
Let **A = {1, 2, 3}**.
*   **Interior (A°):** ∅. (No open interval around a single point can lie entirely within this finite set).
*   **Closure (\(\overline{A}\)):** A itself, since it's a finite set (all points are isolated).
*   **Boundary (∂A):** ∂A = \(\overline{A}\) \ A° = {1, 2, 3} \ ∅ = **{1, 2, 3}**. Every point in A is its own boundary. For example, take x=1. Any ball B(1, ε) will contain 1 (∈ A) and other points like 1 + ε/2 (∉ A, for small ε).

**Example 3: The Whole Space and Empty Set**
*   Let **A = X**. The complement **Aᶜ = ∅**.
    *   For any x ∈ X, B(x, ε) ∩ X ≠ ∅ and B(x, ε) ∩ ∅ = ∅. The second condition fails. Therefore, **∂X = ∅**.
*   Let **A = ∅**. Then **Aᶜ = X**.
    *   Similarly, for any x, B(x, ε) ∩ ∅ = ∅. The first condition fails. Therefore, **∂∅ = ∅**.

**Example 4: A Set in ℝ²**
Consider **(ℝ², d)** (standard distance metric) and let **A = {(x,y) | x² + y² < 1}**, the open unit disk.
*   **Interior (A°):** A itself.
*   **Closure (\(\overline{A}\)):** The closed disk {(x,y) | x² + y² ≤ 1}.
*   **Boundary (∂A):** The circle {(x,y) | x² + y² = 1}. Any point on this circle will have neighbourhoods that extend inside the disk (A) and outside the disk (Aᶜ).

---

### 4. Key Points & Summary

*   **Definition:** The boundary **∂A** of a set **A** in a metric space **(X, d)** is the set of all points **x ∈ X** such that every neighbourhood of **x** intersects both **A** and its complement **Aᶜ**.
*   **Membership:** A boundary point **x** can be either in **A** or not in **A**.
*   **Alternative Formula:** The boundary is the set difference between the closure of A and its interior: **∂A = \(\overline{A}\) \ A°**.
*   **Closure:** The closure of a set is the union of its interior and its boundary: **\(\overline{A}\) = A° ∪ ∂A**.
*   **Special Cases:**
    *   The boundary of the whole space **X** and the empty set **∅** is always empty (**∂X = ∂∅ = ∅**).
    *   For sets with no interior points (like finite sets or ℚ in ℝ), the boundary is equal to the closure.
*   **Visualization:** The boundary represents the "edge" or "frontier" of a set. In ℝ², think of it as the literal outline of a shape.