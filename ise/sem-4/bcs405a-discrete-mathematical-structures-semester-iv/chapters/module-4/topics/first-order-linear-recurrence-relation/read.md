Of course. Here is educational content on "First Order Linear Recurrence Relations" tailored for  Engineering students.

---

# Module 4: First Order Linear Recurrence Relations

### **Introduction**

In Discrete Mathematical Structures, recurrence relations are powerful tools for modeling problems where the state of a system depends on its previous states. They are fundamental in computer science for analyzing algorithms (e.g., calculating time complexity in recursive functions like binary search), in engineering for signal processing, and in operations research. A **First Order Linear Recurrence Relation** is the simplest type, where the next term depends _linearly_ on _exactly one_ previous term.

---

### **Core Concepts**

A first order linear recurrence relation has the form:

$$
a_n = c \cdot a_{n-1} + f(n)
$$

where:

- $a_n$ is the term we want to find.
- $a_{n-1}$ is the previous term.
- $c$ is a constant coefficient.
- $f(n)$ is a function of $n$ (called the _non-homogeneous part_). If $f(n) = 0$, the relation is called **homogeneous**.

To solve such a relation means to find a **closed-form solution**—a non-recursive formula that calculates $a_n$ directly without needing to compute all previous terms.

#### **1. Solving Homogeneous Relations ($f(n) = 0$)**

The relation simplifies to:

$$
a_n = c \cdot a_{n-1}
$$

This is a simple geometric progression. The solution is found by iterating backwards until we reach the initial condition $a_0$:

$$
a_n = c \cdot a_{n-1} = c \cdot (c \cdot a_{n-2}) = c^2 \cdot a_{n-2} = ... = c^n \cdot a_0
$$

**Closed-form solution:** $a_n = a_0 \cdot c^n$

#### **2. Solving Non-Homogeneous Relations ($f(n) \neq 0$)**

The general form $a_n = c \cdot a_{n-1} + f(n)$ requires a more systematic method. The most straightforward technique is **iteration (unfolding)**.

**Steps for Solution by Iteration:**

1.  Start with the recurrence relation.
2.  Repeatedly substitute the formula for $a_{n-1}$, then $a_{n-2}$, and so on, until you detect a pattern that allows you to reach the initial term $a_0$.
3.  Express the final pattern as a summation.
4.  Simplify the summation to obtain the closed-form solution.

---

### **Example**

**Problem:** Solve the recurrence relation $a_n = 3a_{n-1} + 2$, for $n \geq 1$, with initial condition $a_0 = 1$.

**Solution by Iteration:**

1.  **Start and Substitute:**
    $a_n = 3a_{n-1} + 2$

2.  **Substitute for $a_{n-1}$:** Notice $a_{n-1} = 3a_{n-2} + 2$. Plug this in:
    $a_n = 3(3a_{n-2} + 2) + 2 = 3^2 a_{n-2} + 3 \cdot 2 + 2$

3.  **Substitute for $a_{n-2}$:** $a_{n-2} = 3a_{n-3} + 2$. Plug in again:
    $a_n = 3^2 (3a_{n-3} + 2) + 3 \cdot 2 + 2 = 3^3 a_{n-3} + 3^2 \cdot 2 + 3 \cdot 2 + 2$

4.  **Identify the Pattern:** After $k$ iterations, we see:
    $a_n = 3^k a_{n-k} + 2(3^{k-1} + 3^{k-2} + ... + 3 + 1)$

5.  **Reach the Initial Condition:** We continue until the subscript matches our initial condition. Let $k = n$. Then $n-k = 0$:
    $a_n = 3^n a_{0} + 2(3^{n-1} + 3^{n-2} + ... + 3^1 + 3^0)$

6.  **Write as a Summation:**
    $a_n = 3^n \cdot (1) + 2 \sum_{i=0}^{n-1} 3^i$

7.  **Simplify the Summation:** The sum $\sum_{i=0}^{n-1} 3^i$ is a geometric series.
    $\sum_{i=0}^{n-1} r^i = \frac{r^n - 1}{r - 1}$ for $r \neq 1$.
    Therefore, $\sum_{i=0}^{n-1} 3^i = \frac{3^n - 1}{3 - 1} = \frac{3^n - 1}{2}$

8.  **Final Closed-Form Solution:**
    $a_n = 3^n + 2 \cdot \left( \frac{3^n - 1}{2} \right)$
    $a_n = 3^n + (3^n - 1)$
    $\boxed{a_n = 2 \cdot 3^n - 1}$

You can verify this solution by checking for a small value of `n`. E.g., for $n=1$: $a_1 = 3(1) + 2 = 5$. The closed form gives $2 \cdot 3^1 - 1 = 6 - 1 = 5$. ✅

---

### **Key Points & Summary**

| Concept               | Description                                                                                                                                                                    |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Definition**        | A recurrence of the form $a_n = c \cdot a_{n-1} + f(n)$. "First order" means it depends on one previous term. "Linear" means the dependence is linear.                         |
| **Homogeneous Case**  | When $f(n)=0$. The solution is always a geometric sequence: $a_n = a_0 \cdot c^n$.                                                                                             |
| **Solution Method**   | **Iteration (Unfolding)** is a primary method. Substitute the relation into itself repeatedly until you reach the initial condition and can express the result as a summation. |
| **Initial Condition** | A closed-form solution **must** be expressed in terms of the initial condition $a_0$ (or another given base case).                                                             |
| **Application**       | Crucial for analyzing the time complexity of algorithms (e.g., $T(n) = T(n-1) + n$ has complexity $O(n^2)$) and modeling real-world sequential processes.                      |

**Why is this important for engineers?** Understanding how to move from a recursive model (a recurrence) to a closed-form formula is essential for efficient computation and deep analysis of system behavior, which is a core skill in computer science, control systems, and optimization.
