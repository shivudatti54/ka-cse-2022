Of course. Here is a comprehensive educational module on Connectedness in Metric Spaces, tailored for  Engineering students.

***

### **Module 5: Connectedness**
**Subject:** Metric Spaces | **Semester:** IV | **Topic:** Continuous Internal Evaluation

---

#### **1. Introduction to Connectedness**

In our journey through metric spaces, we've studied concepts like open sets, closed sets, and convergence, which help us understand the "local" behavior of spaces and functions. **Connectedness** is a **global property** that describes whether a space is in "one piece" or can be split into disjoint, non-empty open parts. Intuitively, a connected space is a single, unbroken entity. This concept is crucial for understanding the behavior of continuous functions, especially the **Intermediate Value Theorem**, which you may recall from calculus.

---

#### **2. Core Concepts & Definitions**

Let $(X, d)$ be a metric space.

**a) Separated Sets:**
Two non-empty subsets $A$ and $B$ of $X$ are called **separated** if:
1.  $A \cap \overline{B} = \emptyset$ (The closure of $B$ does not intersect $A),$ and
2.  $\overline{A} \cap B = \emptyset$ (The closure of $A$ does not intersect $B).$

This is a stronger condition than just being disjoint. It means the sets are not arbitrarily "close" to each other; there is a gap between them.

**b) Connected Set (Formal Definition):**
A metric space $(X, d)$ is said to be **connected** if it **cannot** be expressed as the union of two non-empty separated sets.

In simpler terms, there is no way to split $X$ into two disjoint, non-empty open sets that are also closed in their relative topology. If such a split is possible, the space is **disconnected**.

**c) Useful Criterion:**
A more practical way to check for connectedness is this: **$X$ is disconnected if and only if there exist two non-empty, disjoint open sets $U$ and $V$ such that $X = U \cup V$.**

---

#### **3. Examples & Non-Examples**

Let's solidify these definitions with concrete examples.

**Example 1: A Connected Set**
*   The real line $\mathbb{R}$ with the usual metric is **connected**. You cannot split the entire number line into two disjoint open sets. Any attempt to do so (e.g., $(-\infty, a)$ and $(a, \infty)$) will miss the point $a$ itself, violating the condition that the union must be the whole space.

**Example 2: A Disconnected Set**
*   Consider the set $X = (0, 1) \cup (2, 3)$ as a subspace of $\mathbb{R}$.
    *   Let $U = (0, 1)$ and $V = (2, 3)$.
    *   Both $U$ and $V$ are open *in the subspace topology* of $X$.
    *   They are non-empty, disjoint, and their union is $X$.
    *   Therefore, $X$ is **disconnected**. It is clearly in two separate pieces.

**Example 3: A Surprising Case (The Rationals are Disconnected)**
*   Consider $\mathbb{Q}$, the set of rational numbers, with the usual metric.
*   Let $U = \{q \in \mathbb{Q} : q^2 < 2\}$ (rationals less than $\sqrt{2}$) and $V = \{q \in \mathbb{Q} : q^2 > 2\}$ (rationals greater than $\sqrt{2}$).
*   $U$ and $V$ are both open in $\mathbb{Q}$, disjoint, non-empty, and their union is $\mathbb{Q}$.
*   Thus, $\mathbb{Q}$ is **disconnected**. Even though it seems dense, the "gap" at the irrational number $\sqrt{2}$ is enough to separate it.

---

#### **4. Key Results and Theorems**

**a) Continuous Image of a Connected Set is Connected:**
If $f: (X, d_x) \to (Y, d_y)$ is a **continuous** function and $X$ is connected, then its image $f(X)$ is also connected in $Y$.

This is a powerful theorem. It means connectedness is a **topological property** preserved under continuous mappings.

**b) The Intermediate Value Theorem (Generalized):**
The classic IVT is a direct consequence of connectedness.
*   **Theorem:** Let $f: [a, b] \to \mathbb{R}$ be continuous. If $f(a) < k < f(b)$ (or $f(b) < k < f(a)$), then there exists some $c \in (a, b)$ such that $f(c) = k$.
*   **Why?** The interval $[a, b]$ is connected (it is a *connected subset* of $\mathbb{R}$). Therefore, its image under the continuous function $f$ must also be a connected subset of $\mathbb{R}$, which is an interval. This connected interval must contain all values between $f(a)$ and $f(b)$.

---

#### **5. Summary & Key Takeaways**

| **Concept** | **Description** | **Key Point** |
| :--- | :--- | :--- |
| **Connected Space** | A space that cannot be divided into two non-empty, disjoint open sets. | It is "one piece." |
| **Disconnected Space** | A space that can be written as $X = U \cup V$, where $U$ and $V$ are non-empty, disjoint, and open. | It is "multiple pieces." |
| **Separated Sets** | Sets that are not arbitrarily close to each other ($A \cap \overline{B} = \emptyset$ and $\overline{A} \cap B = \emptyset$). | Stronger than just being disjoint. |
| **Main Theorem** | The continuous image of a connected set is connected. | Preserved under continuity. |
| **IVT Link** | Connectedness of $[a, b]$ guarantees that a continuous function takes on every value between $f(a)$ and $f(b)$. | Fundamental for solving equations. |

**In essence, connectedness is a fundamental topological property that helps us understand the structure of a space and the behavior of functions defined on it, forming the bedrock for more advanced concepts in analysis.**