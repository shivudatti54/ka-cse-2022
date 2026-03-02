Of course. Here is a comprehensive educational note on the Bolzano-Weierstrass property for  Engineering students.

# **Module 4: Compactness - The Bolzano-Weierstrass Property**

**Semester: IV | Subject: Metric Spaces**

---

## **1. Introduction**

In the study of metric spaces, we often deal with infinite sets and sequences. A fundamental question arises: when can we guarantee that an infinite set or a sequence has a "well-behaved" limit point? The Bolzano-Weierstrass property provides a crucial answer to this question. It is a fundamental characteristic of a special class of metric spaces known as **compact spaces**. This property generalizes a classic result from real analysis (the Bolzano-Weierstrass Theorem) to the broader setting of metric spaces.

## **2. Core Concepts**

### **2.1. What is the Bolzano-Weierstrass Property?**

A metric space $(X, d)$ is said to have the **Bolzano-Weierstrass property** if **every infinite subset of $X$ has a limit point in $X$**.

Let's break this down:
*   **Infinite Subset:** We consider any subset $A \subseteq X$ that contains infinitely many points.
*   **Limit Point:** A point $x \in X$ is a limit point of $A$ if every open ball $B(x, \epsilon)$ (for any $\epsilon > 0$) contains at least one point of $A$ different from $x$ itself. This means points of $A$ get arbitrarily close to $x$.
*   **In $X$:** This is crucial. The limit point must lie within the space $X$ itself.

In essence, this property guarantees that no matter how you choose an infinite collection of points in $X,$ you cannot "spread them out" everywhere; they must inevitably cluster or accumulate around at least one point within the space.

### **2.2. Connection to Compactness**

The Bolzano-Weierstrass property is not just a standalone idea; it is fundamentally linked to the concept of compactness. One of the key theorems in metric spaces states:

**"A metric space $(X, d)$ is compact if and only if it has the Bolzano-Weierstrass property."**

This means the following statements are equivalent for a metric space:
1.  $X$ is compact (every open cover has a finite subcover).
2.  Every infinite subset of $X$ has a limit point in $X$ (the Bolzano-Weierstrass property).
3.  Every sequence in $X$ has a convergent subsequence (this is another common and equivalent formulation).

This equivalence is a powerful tool. It allows us to prove a space is compact by showing that any infinite set within it must have a cluster point, which is often more intuitive than working with open covers.

### **2.3. The Classic Example: $[a, b] \subset \mathbb{R}$**

The closed and bounded interval $[a, b]$ is a compact subset of $\mathbb{R}$ with the usual metric. The **Bolzano-Weierstrass Theorem** from real analysis states: *"Every bounded infinite subset of $\mathbb{R}$ has a limit point in $\mathbb{R}$."* Since $[a, b]$ is bounded and also closed (meaning it contains all its limit points), any infinite subset of it is bounded and therefore must have a limit point, which will necessarily lie within $[a, b]$. This perfectly illustrates the property.

**Counterexample:** The space $(0, 1)$ with the usual metric is **not** compact. Consider the infinite subset $A = \{1/n : n \in \mathbb{N}\}$. This set has a limit point, which is $0$. However, $0 \notin (0, 1)$. Since the limit point of this infinite set is not in the space, $(0, 1)$ fails the Bolzano-Weierstrass property and is therefore not compact.

### **2.4. Example in a Different Metric Space**

Consider the metric space $X = \{1/n : n \in \mathbb{N}\} \cup \{0\}$ with the standard metric inherited from $\mathbb{R}$.

*   Is this space compact? Let's check the Bolzano-Weierstrass property.
*   Take any infinite subset $A \subseteq X$. There are two possibilities:
    1.  If $A$ contains the point $0$, then $0$ is trivially a limit point of $A$ (and is in $X$).
    2.  If $A$ does not contain $0$, then $A$ is an infinite subset of $\{1/n\}$. The only possible limit point for such a set is $0$. Since the points $1/n$ get arbitrarily close to $0$, every open ball around $0$ will contain infinitely many points from $A$. Therefore, $0$ is a limit point, and it is in $X$.

Since every infinite subset has a limit point (specifically, $0$) in $X$, the space satisfies the Bolzano-Weierstrass property and is thus compact.

## **3. Key Points & Summary**

| **Key Point** | **Description** |
| :--- | :--- |
| **Definition** | A metric space $(X, d)$ has the Bolzano-Weierstrass property if **every infinite subset of $X$ has a limit point in $X$**. |
| **Equivalence** | For metric spaces, the Bolzano-Weierstrass property is **equivalent to compactness**. This is a central theorem. |
| **Utility** | It provides an intuitive way to understand compactness: in a compact space, infinite points cannot be "spread out"; they must cluster around at least one point within the space. |
| **Classic Case** | The Bolzano-Weierstrass Theorem for $\mathbb{R}$ ($[a,b]$ is compact) is a specific instance of this general property. |
| **Application** | To prove a space is **not compact**, find an infinite subset with no limit point (or whose limit point lies outside the space). |

**In summary, the Bolzano-Weierstrass property is an essential feature of compact metric spaces, stating that confinement of infinite sets guarantees the existence of limit points, thereby providing a powerful tool for analysis and proof.**