Of course. Here is comprehensive educational content on the Bolzano-Weierstrass property for  Engineering Mathematics students, structured as requested.

### **Module 4: Compactness - The Bolzano-Weierstrass Property**

**Subject:** METRIC SPACES
**Semester:** IV

---

#### **1. Introduction**

In the study of metric spaces, we often grapple with infinite sets. A fundamental question arises: when does an infinite set have a "limit point" or a point that other points get arbitrarily close to? The **Bolzano-Weierstrass Property** provides a powerful and elegant answer to this question. It is a cornerstone of mathematical analysis, deeply connected to the crucial concept of **compactness**. For engineering students, this isn't just abstract math; it underpins convergence proofs in numerical methods, optimization algorithms, and signal processing, where finding a convergent subsequence is often the key to a solution.

#### **2. Core Concepts**

Let's break down the property step-by-step.

**a) Sequential Compactness**
A subset \( K \) of a metric space \( (X, d) \) is said to be **sequentially compact** if **every sequence** in \( K \) has a **convergent subsequence** whose limit is also *in* \( K \).

**b) The Bolzano-Weierstrass Theorem (for \( \mathbb{R}^n \))**
The classic theorem states:
> Every **bounded** sequence in \( \mathbb{R}^n \) has a **convergent subsequence**.

This is the property you likely encountered in first-year calculus. It tells us that in \( \mathbb{R} \) and \( \mathbb{R}^n \), boundedness is the key to finding a limit point.

**c) The Bolzano-Weierstrass Property (General Metric Space)**
We generalize this idea to any metric space. A metric space \( (X, d) \) is said to have the **Bolzano-Weierstrass Property** if every infinite subset of \( X \) has a **limit point**.

*   **Limit Point (Recall):** A point \( x \in X \) is a limit point of a set \( S \subseteq X \) if every open ball \( B(x, \epsilon) \) contains a point of \( S \) different from \( x \) itself.

**d) The Crucial Link: Equivalence to Compactness**
In metric spaces, several important properties are equivalent. The most significant takeaway for this module is:

> For a metric space \( (X, d) \), the following are equivalent:
> 1.  \( X \) is **compact** (every open cover has a finite subcover).
> 2.  \( X \) is **sequentially compact**.
> 3.  \( X \) has the **Bolzano-Weierstrass Property**.

This means that in metric spaces, **compactness**, **sequential compactness**, and the **Bolzano-Weierstrass property** are three different ways of describing the same fundamental concept. If a set has one of these properties, it automatically has the other two.

#### **3. Examples & Non-Examples**

Let's solidify these ideas with examples.

*   **Example 1: A Closed and Bounded Interval**
    Consider \( K = [0, 1] \subset \mathbb{R} \). This set is compact (by the Heine-Borel Theorem).
    - Take *any* sequence \( (x_n) \) in \([0, 1]\). The Bolzano-Weierstrass Theorem guarantees a convergent subsequence \( (x_{n_k}) \). Since \([0, 1]\) is closed, the limit of this subsequence must also lie in \([0, 1]\). Thus, \([0, 1]\) is sequentially compact and possesses the Bolzano-Weierstrass property.

*   **Example 2: An Open Interval**
    Consider \( S = (0, 1) \subset \mathbb{R} \). This set is **not** compact.
    - Take the sequence \( x_n = \frac{1}{n} \) for \( n = 2, 3, 4, ... \). All points are in \( (0, 1) \). This sequence itself converges to \( 0 \), but \( 0 \notin (0, 1) \). While there *is* a convergent subsequence (the sequence itself), its limit is **not in the set** \( S \). Therefore, \( S \) is **not** sequentially compact and does **not** have the Bolzano-Weierstrass property.

*   **Non-Example: An Infinite-Dimensional Space**
    In the space \( \ell^2 \) (the space of square-summable sequences), the set \( \{e_1, e_2, e_3, ...\} \), where \( e_k \) is the sequence with 1 in the k-th position and 0 elsewhere, is bounded. However, the distance between any two distinct elements is \( \sqrt{2} \). No subsequence can be Cauchy, hence none can converge. This shows that in infinite-dimensional spaces, boundedness alone is **not** sufficient for the Bolzano-Weierstrass property; this is a key difference from \( \mathbb{R}^n \).

#### **4. Key Points & Summary**

| Concept | Definition | Key Insight |
| :--- | :--- | :--- |
| **Sequential Compactness** | Every sequence has a convergent subsequence (limit in the set). | The "sequence" version of compactness. |
| **Bolzano-Weierstrass Property** | Every infinite subset has a limit point. | The "set" version of compactness. |
| **Compactness** | Every open cover has a finite subcover. | The standard topological definition. |

**Summary:**
*   The **Bolzano-Weierstrass Property** states that every infinite subset of a space must have a limit point.
*   In \( \mathbb{R}^n \), this is equivalent to a set being **closed and bounded** (Heine-Borel Theorem).
*   In a **general metric space**, this property is **equivalent** to compactness and sequential compactness.
*   This property is vital as it guarantees the existence of limits or convergent processes, which is essential for stability and convergence analysis in engineering applications.
*   **Remember:** For metric spaces, **Compactness \( \equiv \) Sequential Compactness \( \equiv \) Bolzano-Weierstrass Property**.