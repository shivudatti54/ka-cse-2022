**Subject: METRIC SPACES | Semester: IV**
**Module: Module 2: Concepts in Metric Spaces**
**Topic: Exterior and Boundary Points**

---

### **1. Introduction**

In the study of metric spaces, understanding the "position" of a point relative to a subset is crucial. We have already explored interior points, which lie "deep inside" a set. Now, we extend these ideas to define two other fundamental types of points: **exterior points** and **boundary points**. These concepts are essential for analyzing the structure of sets, defining limits, continuity, and eventually, more advanced topics like topology on metric spaces.

---

### **2. Core Concepts**

Let $(X, d)$ be a metric space, and let $A$ be a subset of $X$.

#### **a) Exterior Point**

An element $x \in X$ is called an **exterior point** of the set $A$ if there exists an open ball centered at $x$ that is completely contained in the **complement** of $A$, denoted $A^c$.

*   **Formal Definition:** $x \in X$ is an exterior point of $A$ if $\exists \ r > 0$ such that $B(x, r) \subseteq A^c$.
*   **Simple Interpretation:** The point $x$ is "well outside" the set $A". It has a neighborhood of points that also do not belong to $A$.
*   **The Exterior:** The set of all exterior points of $A$ is called the **exterior** of $A$ and is often denoted as $\text{ext}(A)$.

#### **b) Boundary Point**

An element $x \in X$ is called a **boundary point** of the set $A$ if **every** open ball centered at $x$ intersects **both** the set $A$ and its complement $A^c$.

*   **Formal Definition:** $x \in X$ is a boundary point of $A$ if $\forall \ r > 0$, the open ball $B(x, r)$ satisfies both $B(x, r) \cap A \neq \emptyset$ and $B(x, r) \cap A^c \neq \emptyset$.
*   **Simple Interpretation:** The point $x$ is on the "edge" or "frontier" of $A$. No matter how closely you look around $x$, you will always find points that are in $A$ and points that are not in $A$.
*   **The Boundary:** The set of all boundary points of $A$ is called the **boundary** (or frontier) of $A$ and is denoted by $\partial A$.

---

### **3. Examples**

Let's consider the metric space $(\mathbb{R}^2, d)$ with the usual Euclidean metric and a subset $A = \{(x, y) \in \mathbb{R}^2 : x^2 + y^2 < 1\}$, the open unit disk.

*   **Interior Point:** The point $(0, 0.5)$ is an **interior point**. You can find a small ball around it that stays entirely inside the disk.
*   **Exterior Point:** The point $(2, 2)$ is an **exterior point**. You can find a ball (e.g., of radius $0.5$) around $(2,2)$ that does not contain *any* points from the disk $A$.
*   **Boundary Point:** The point $(1, 0)$ is a **boundary point**. No matter how small a radius $r$ you choose, the ball $B((1,0), r)$ will always contain:
    *   Points *inside* the disk (e.g., points just to the left of $(1,0)$).
    *   Points *outside* the disk (e.g., points just to the right of $(1,0)$).
    The entire circle defined by $x^2 + y^2 = 1$ is the boundary $\partial A$.

**Another Example in $(\mathbb{R}, d)$:**
Let $A = (0, 1]$, a half-open interval.
*   **Interior Points:** Points like $0.5$ are interior. ($B(0.5, 0.1) \subset A$).
*   **Exterior Points:** Points like $-1$ or $2$ are exterior.
*   **Boundary Points:** The points $x=0$ and $x=1$ are boundary points.
    *   For $x=0$: *Every* ball $B(0, r) = (-r, r)$ contains negative numbers (outside $A$) and positive numbers (inside $A$).
    *   For $x=1$: *Every* ball $B(1, r)$ contains numbers less than 1 (inside $A$) and numbers greater than 1 (outside $A$).

---

### **4. Key Relationships and Summary**

| Concept | Definition | Key Idea |
| :--- | :--- | :--- |
| **Interior Point** | $\exists r > 0$ such that $B(x, r) \subseteq A$ | A point "deep inside" A. |
| **Exterior Point** | $\exists r > 0$ such that $B(x, r) \subseteq A^c$ | A point "well outside" A. |
| **Boundary Point** | $\forall r > 0$, $B(x, r) \cap A \neq \emptyset$ **and** $B(x, r) \cap A^c \neq \emptyset$ | A point on the "edge" of A. |

**Key Takeaways:**

1.  **Mutual Exclusivity:** For a given set $A$, any point $x \in X$ must be **exactly one** of the following: an interior point of $A$, an exterior point of $A$, or a boundary point of $A$. These three sets form a partition of the entire metric space $X$.
    > $X = \text{int}(A) \ \cup \ \text{ext}(A) \ \cup \ \partial A$

2.  **Closure:** The **closure** of a set $\overline{A}$, which is the union of $A$ and its limit points, can also be expressed as $\overline{A} = A \cup \partial A$. The boundary is the part you add to a set to make it closed.

3.  **Complement Relation:** The exterior of a set $A$ is simply the interior of its complement: $\text{ext}(A) = \text{int}(A^c)$.

4.  **Visualization:** Always try to visualize these concepts in familiar metric spaces like $\mathbb{R}^2$. This builds the intuition necessary to handle more abstract spaces.

Understanding these point types is foundational for grasping subsequent concepts like **open sets** ($A = \text{int}(A)$), **closed sets** ($\partial A \subseteq A$), and **compact sets**.