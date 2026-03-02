Of course. Here is a comprehensive educational note on "Bounded Sets" in Metric Spaces, tailored for  Engineering students.

# **Bounded Sets in Metric Spaces**

## **1. Introduction**

In engineering mathematics, we often deal with sets of numbers, vectors, or functions. A fundamental question is: "How 'big' is this set?" or "Does the set extend to infinity?" The concept of a **bounded set** provides a precise mathematical answer to this question. In the context of metric spaces, boundedness is defined using the underlying distance function (the metric). This concept is crucial for later topics in analysis, such as convergence, continuity, and compactness, which are vital for solving engineering problems involving approximations and optimizations.

---

## **2. Core Concepts**

### **Definition of a Bounded Set**

Let **(X, d)** be a metric space. A subset **A ⊆ X** is said to be **bounded** if there exists a real number **M > 0** and a fixed point **a₀ ∈ X** such that for every point **x ∈ A**, the distance from **x** to **a₀** is less than or equal to **M**.

In mathematical terms:
**A is bounded if ∃ a₀ ∈ X and ∃ M > 0 such that d(x, a₀) ≤ M for all x ∈ A.**

*   The point **a₀** is often called the **center**.
*   The smallest such **M** can be thought of as the "radius" that encloses the entire set **A**.

### **An Equivalent (and Often More Useful) Definition**

An equivalent way to define a bounded set is by using the concept of **diameter**. The **diameter of a set A** is defined as:
**diam(A) = sup{ d(x, y) : x, y ∈ A }**
This represents the supremum (least upper bound) of all possible distances between pairs of points in A.

A set **A** is bounded **if and only if its diameter is finite**, i.e., **diam(A) < ∞**.

This definition is often more practical because it doesn't require choosing an arbitrary center point.

---

## **3. Examples**

Let's explore these definitions with examples in different metric spaces.

### **Example 1: Bounded Sets in ℝ (Real Line) with usual metric**

The standard metric on ℝ is **d(x, y) = |x - y|**.

*   **Bounded Set:** The interval **A = (2, 5)** is bounded.
    *   *Using first definition:* Choose center **a₀ = 3.5** and **M = 1.5**. For any x ∈ (2, 5), |x - 3.5| < 1.5.
    *   *Using diameter:* The farthest two points in A are nearly 2 and 5. diam(A) = |5 - 2| = 3, which is finite.
*   **Unbounded Set:** The set of natural numbers **ℕ = {1, 2, 3, ...}** is unbounded.
    *   For any proposed center **a₀** and radius **M**, we can always find a natural number **n** such that **d(n, a₀) > M**. Its diameter is infinite.

### **Example 2: Bounded Sets in ℝ² (Plane) with Euclidean metric**

The metric is **d( (x₁, y₁), (x₂, y₂) ) = √[(x₂ - x₁)² + (y₂ - y₁)² ]**.

*   **Bounded Set:** A circle (including its interior) is bounded. Its diameter is simply the length of its diameter.
*   **Bounded Set:** Any finite set of points is bounded.
*   **Unbounded Set:** The entire plane **ℝ²** is unbounded. A line (e.g., the x-axis) is also an unbounded subset of ℝ².

### **Example 3: Importance of the Metric**

Consider the set **A = {1, 2, 3, ...}** (the natural numbers). Is it bounded?
*   With the **usual metric d(x, y) = |x - y|**: **Unbounded**, as shown in Example 1.
*   With the **discrete metric**:
    **d(x, y) = { 0 if x = y; 1 if x ≠ y }**
    In this metric, **A is bounded**!
    *   *Why?* Choose center **a₀ = 1** and **M = 1**. For any other natural number **n**, **d(n, 1) = 1 ≤ 1**. The distance between *any* two distinct points is always 1, so **diam(A) = 1**, which is finite.

**This example highlights a critical point: Boundedness is not an inherent property of the set alone; it depends on the metric we use to define distance.**

---

## **4. Key Points and Summary**

| **Key Point** | **Description** |
| :--- | :--- |
| **Definition** | A set **A** in a metric space **(X, d)** is bounded if it can be enclosed in a ball of finite radius. Formally, ∃ a₀ ∈ X, M > 0 such that **d(x, a₀) ≤ M** for all x ∈ A. |
| **Equivalent Definition** | A set is bounded **iff** its **diameter**, diam(A) = sup{d(x,y) : x,y ∈ A}, is **finite**. |
| **Dependence on Metric** | Boundedness is a **metric-dependent property**. The same underlying set can be bounded under one metric and unbounded under another. |
| **Simple Examples** | Intervals like [a, b], circles, spheres, and any finite set are bounded in their standard metrics. |
| **Non-Examples** | The real line ℝ, lines/planes in ℝⁿ, and the set of natural numbers (under the usual metric) are unbounded. |

**Why is this important for engineers?**
Understanding boundedness is a prerequisite for more advanced concepts. For instance, in optimization, we often search for maxima/minima within a bounded, closed set (which leads to the Extreme Value Theorem). In signal processing, we deal with bounded functions (signals with finite energy). In computer science, algorithms often require working within a bounded region of a search space. Grasping this fundamental concept in metric spaces provides the groundwork for these applications.