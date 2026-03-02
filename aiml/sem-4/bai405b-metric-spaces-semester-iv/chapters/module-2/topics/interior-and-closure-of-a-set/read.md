Of course. Here is a comprehensive educational guide on Metric Spaces for  Engineering students, focusing on the interior and closure of a set.

***

### **Interior and Closure of a Set in Metric Spaces**

In the study of metric spaces, two fundamental concepts that help us characterize the "structure" of a subset are its **interior** and its **closure**. These concepts are built upon the idea of neighborhoods (open balls) and provide a precise way to talk about points that are "deep inside" a set and points that are "arbitrarily close" to a set.

#### **1. Interior of a Set**

The interior of a set consists of all points that have some "breathing room" within the set. Formally:

**Definition:** Let $(X, d)$ be a metric space and let $A \subseteq X$. A point $x \in X$ is called an **interior point** of $A$ if there exists an open ball centered at $x$ that is entirely contained within $A$. That is,
$$\exists \epsilon > 0 \quad \text{such that} \quad B(x, \epsilon) \subseteq A.$$

The set of all interior points of $A$ is called the **interior** of $A$ and is denoted by $A^\circ$ or $\text{Int}(A)$.

**Key Properties:**
*   $A^\circ \subseteq A$.
*   $A^\circ$ is the **largest open set** contained in $A$.
*   A set $A$ is **open** if and only if every point of $A$ is an interior point, i.e., $A = A^\circ$.

**Example:** Consider the set $A = \{ (x, y) \in \mathbb{R}^2 \mid 1 \leq x^2 + y^2 < 4 \}$ in $\mathbb{R}^2$ with the standard Euclidean metric.
*   A point like $(1.5, 0)$ is an interior point. We can find a small ball around it that stays entirely within the annulus (e.g., $\epsilon = 0.4$).
*   A point like $(1, 0)$, which lies on the inner boundary, is **not** an interior point. *Any* open ball around $(1,0)$ will contain points whose distance from the origin is less than 1 (like $(0.99, 0)$), which are outside $A$.
*   Therefore, $\text{Int}(A) = \{ (x, y) \in \mathbb{R}^2 \mid 1 < x^2 + y^2 < 4 \}$.

#### **2. Closure of a Set**

The closure of a set consists of all points that are either in the set or are "limit points" of the set. There are two equivalent ways to define it.

**a) Using Limit Points:**
A point $x \in X$ is a **limit point** (or an accumulation point) of $A$ if every open ball centered at $x$ contains at least one point of $A$ different from $x$ itself.
$$ \forall \epsilon > 0, \quad B(x, \epsilon) \cap (A \setminus \{x\}) \neq \emptyset. $$

The **closure** of $A$, denoted by $\overline{A}$, is the union of $A$ and the set of all its limit points.
$$\overline{A} = A \cup \{\text{all limit points of } A\}.$$

**b) Using Closed Sets:**
The closure of $A$ is the **smallest closed set** containing $A$.

**Key Properties:**
*   $A \subseteq \overline{A}$.
*   $\overline{A}$ is always a **closed set**.
*   A set $A$ is **closed** if and only if it contains all its limit points, i.e., $A = \overline{A}$.

**Example:** Consider the same set $A = \{ (x, y) \in \mathbb{R}^2 \mid 1 \leq x^2 + y^2 < 4 \}$.
*   The point $(1, 0)$ is a limit point of $A$. Any ball around it contains points from $A$ (points just outside the circle of radius 1 are inside $A$).
*   The point $(2, 0)$ is also a limit point of $A$. Any ball around it will contain points from $A$ (points just inside the circle of radius 2).
*   The point $(0,0)$ is **not** a limit point, as a ball of radius $0.5$ contains no points of $A$.
*   Therefore, $\overline{A} = \{ (x, y) \in \mathbb{R}^2 \mid 1 \leq x^2 + y^2 \leq 4 \}$.

#### **Relationship between Interior and Closure**

The interior and closure of a set are dual concepts. The interior is the largest open set inside $A$, while the closure is the smallest closed set containing $A$. Their relationship is often expressed using the complement and the boundary.

The **boundary** of a set $A$, denoted by $\partial A$, is defined as $\partial A = \overline{A} \setminus A^\circ$. It consists of all points that are in the closure of $A$ but not in its interior. In our example, $\partial A = \{ (x, y) \mid x^2 + y^2 = 1 \text{ or } x^2 + y^2 = 4 \}$.

**Key Summary**
| Concept | Notation | Definition | Key Property |
| :--- | :--- | :--- | :--- |
| **Interior** | $A^\circ$, $\text{Int}(A)$ | Points with a neighborhood entirely in $A$. | Largest open subset of $A$. |
| **Closure** | $\overline{A}$ | $A$ union all its limit points. | Smallest closed set containing $A$. |
| **Boundary** | $\partial A$ | $\overline{A} \setminus A^\circ$ | Points arbitrarily close to both $A$ and its complement. |

Understanding these concepts is crucial for analyzing convergence, continuity, and compactness in metric spaces, which are foundational for many areas of engineering mathematics, including optimization and numerical analysis.