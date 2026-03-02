Of course. Here is a comprehensive educational note on "Open and Closed Spheres" for  Engineering students, structured as requested.

***

### **Module 2: Concepts in Metric Spaces**
### **Topic: Open and Closed Spheres**

#### **1. Introduction**
In the study of metric spaces, we move beyond simple Euclidean geometry to more abstract spaces where we can still measure "distance." The concepts of **open and closed spheres** (or balls) are fundamental building blocks. They form the basis for defining crucial topological ideas like open sets, closed sets, interior points, boundary points, convergence, and continuity. For engineering applications, these concepts underpin algorithms in computer graphics (e.g., collision detection), machine learning (e.g., clustering with k-NN), and signal processing.

#### **2. Core Concepts**

Let $(X, d)$ be a metric space, let $x_0 \in X$ be a fixed point (the "center"), and let $r > 0$ be a real number (the "radius").

##### **A. Open Sphere (or Open Ball)**
An **open sphere** $S(x_0, r)$ is the set of all points in $X$ whose distance from the center $x_0$ is *strictly less than* $r$.

**Mathematical Definition:**
$$S(x_0, r) = \{ x \in X \mid d(x, x_0) < r \}$$

**Interpretation:** It contains all points *inside* the sphere but explicitly *excludes* the boundary. Think of it as a "punctured" or "soft" boundary where you can get arbitrarily close to the radius $r$ but never quite reach it.

##### **B. Closed Sphere (or Closed Ball)**
A **closed sphere** $\overline{S}(x_0, r)$ is the set of all points in $X$ whose distance from the center $x_0$ is *less than or equal to* $r$.

**Mathematical Definition:**
$$\overline{S}(x_0, r) = \{ x \in X \mid d(x, x_0) \leq r \}$$

**Interpretation:** It contains all points *inside* the sphere *including* the boundary. This is the intuitive notion of a solid sphere.

#### **3. Examples in Different Metric Spaces**

The visual interpretation of these spheres depends heavily on the metric being used.

**Example 1: The Real Line $\mathbb{R}$ with usual metric ($d(x, y) = |x - y|$)**
*   **Open Sphere:** $S(a, r) = \{ x \in \mathbb{R} \mid |x - a| < r \} = (a - r, a + r)$. This is an open interval.
    *   $S(2, 1) = (1, 3)$
*   **Closed Sphere:** $\overline{S}(a, r) = \{ x \in \mathbb{R} \mid |x - a| \leq r \} = [a - r, a + r]$. This is a closed interval.
    *   $\overline{S}(2, 1) = [1, 3]$

**Example 2: The Plane $\mathbb{R}^2$ with Euclidean metric ($d((x_1,y_1), (x_2,y_2)) = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$)**
*   **Open Sphere:** All points *inside* a circle of radius $r$ centered at $(x_0, y_0)$, excluding the circular boundary itself.
*   **Closed Sphere:** All points *inside* the circle, including the boundary.

**Example 3: The Plane $\mathbb{R}^2$ with Manhattan metric ($d((x_1,y_1), (x_2,y_2)) = |x_2-x_1| + |y_2-y_1|$)**
The shape of the "sphere" changes dramatically.
*   **Open Sphere:** $S((0,0), 1)$ is the set of points $(x, y)$ such that $|x| + |y| < 1$. This forms a diamond-shaped region (a rotated square), excluding its boundary.
*   This highlights that these are abstract concepts not limited to circular shapes.

#### **4. Key Observations and Properties**

1.  **Relation:** For any $x_0$ and $r>0$, the open sphere is always a subset of its closed counterpart: $S(x_0, r) \subseteq \overline{S}(x_0, r)$.
2.  **Nesting:** If $r_1 < r_2$, then $S(x_0, r_1) \subseteq S(x_0, r_2)$ and $\overline{S}(x_0, r_1) \subseteq \overline{S}(x_0, r_2)$.
3.  **Terminology:** The terms "ball" and "sphere" are often used interchangeably in this context. Don't confuse them with the classical geometric definition of a "sphere" as just a hollow shell; here, a "sphere" refers to a solid ball.
4.  **Topological Role:** Open spheres are the fundamental building blocks used to define **open sets**. A set $A$ is open if, for every point $a \in A$, there exists some $r > 0$ such that the entire open sphere $S(a, r)$ is contained within $A$.

#### **5. Summary**

| Feature | Open Sphere $S(x_0, r)$ | Closed Sphere $\overline{S}(x_0, r)$ |
| :--- | :--- | :--- |
| **Definition** | $\{ x \in X \mid d(x, x_0) < r \}$ | $\{ x \in X \mid d(x, x_0) \leq r \}$ |
| **Includes Boundary?** | **No** | **Yes** |
| **Analogy in $\mathbb{R}$** | Open Interval $(a-r, a+r)$ | Closed Interval $[a-r, a+r]$ |
| **Analogy in $\mathbb{R}^2$ (Euclidean)** | Interior of a circle | A solid disk (interior + circle) |
| **Primary Use** | Defining **open sets**, **neighborhoods**, and **interior points**. | Defining **bounded sets** and **compact sets**. |

Understanding the precise distinction between these two objects, governed solely by the inequality sign ($<$ vs. $\leq$), is critical for progressing in the study of metric spaces and their applications.