# **Local Connectedness and Arc-Wise Connectedness**

## **Introduction**

In metric spaces, connectedness is a fundamental concept that describes the properties of a space that allow us to travel from one point to another without leaving the space. There are two types of connectedness: local connectedness and arc-wise connectedness. In this study material, we will explore these concepts, their definitions, and examples.

## **Local Connectedness**

### Definition

A point $x$ in a metric space $(X, d)$ is said to be locally connected at $x$ if for every open set $U$ containing $x$, there exists an open neighborhood $V$ of $x$ such that $V \subseteq U$.

### Explanation

Local connectedness is a weaker form of connectedness. A space is locally connected if every point has a neighborhood that is fully contained in an open set. This means that if we are in a neighborhood of a point, we can always find a larger open set that includes that neighborhood.

### Example

Consider the space $\mathbb{R}$ with the standard metric. The point $x=0$ is locally connected because for every open set $U$ containing $0$, we can find an open neighborhood $V$ of $0$ such that $V \subseteq U$. For instance, if $U=(-1, 1)$, we can take $V=(-\frac{1}{2}, \frac{1}{2})$.

### Key Concepts

- A space is locally connected if every point is a local minimum of the distance function $d(x, \cdot)$.
- The open mapping theorem states that a continuous function from a locally connected space to a locally connected space is open.

### Arc-Wise Connectedness

---

### Definition

A subset $A$ of a metric space $(X, d)$ is said to be arc-wise connected if for every two points $x, y \in A$, there exists a continuous function $f: [0, 1] \to A$ such that $f(0) = x$ and $f(1) = y$.

### Explanation

Arc-wise connectedness is a stronger form of connectedness. A space is arc-wise connected if we can travel from one point to another by following a continuous path within the space. This means that if we start at one point and move to another, we can do so by following a continuous function that stays within the subset.

### Example

Consider the space $[0, 1]$ with the standard metric. The subset $[0, \frac{1}{2}]$ is arc-wise connected because for every two points $x, y \in [0, \frac{1}{2}]$, we can find a continuous function $f: [0, 1] \to [0, \frac{1}{2}]$ such that $f(0) = x$ and $f(1) = y$. For instance, we can take $f(t) = 2t$.

### Key Concepts

- A space is arc-wise connected if and only if it is path-connected and locally connected.
- The space is also arc-wise connected if and only if it is locally arc-wise connected.

### Comparison

---

Local connectedness and arc-wise connectedness are related but distinct concepts.

- Local connectedness is a weaker form of connectedness that only concerns neighborhoods of points.
- Arc-wise connectedness is a stronger form of connectedness that concerns paths between points.

In summary, local connectedness ensures that every point has a neighborhood that is fully contained in an open set, while arc-wise connectedness ensures that we can travel from one point to another by following a continuous path within the space.

### Conclusion

---

In conclusion, local connectedness and arc-wise connectedness are fundamental concepts in metric spaces that describe the properties of connectedness. Understanding these concepts is essential for studying connectedness in metric spaces.
