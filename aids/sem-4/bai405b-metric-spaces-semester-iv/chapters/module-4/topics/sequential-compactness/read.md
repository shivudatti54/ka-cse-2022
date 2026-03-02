Of course. Here is a comprehensive educational module on Sequential Compactness, tailored for  engineering students.

***

### **Module 4: Compactness | Topic: Sequential Compactness**

**Subject:** METRIC SPACES
**Semester:** IV

---

#### **1. Introduction: What is Sequential Compactness?**

In the previous modules, we explored the general concept of a **compact set**—a set where every open cover has a finite subcover. While this definition is powerful, it can sometimes be abstract and difficult to apply directly.

**Sequential compactness** offers an alternative, often more intuitive, way to think about compactness, especially in the context of metric spaces (which include the familiar Euclidean spaces like `ℝⁿ`). It reframes the idea of "compactness" in terms of the behavior of *sequences*, a concept you are already well-acquainted with from calculus.

Simply put, a set is sequentially compact if every sequence you can possibly form within it has a subsequence that converges to a point *that is also inside the set*. This captures the essence of compactness: a set is "closed" enough to contain its limit points and "bounded" enough to prevent sequences from escaping to infinity.

---

#### **2. Core Concepts and Definition**

Let's break down the key ideas:

*   **Sequence:** An ordered list of points `(x₁, x₂, x₃, ..., xₙ)` in a metric space `(X, d)`.
*   **Convergence:** A sequence `(xₙ)` converges to a limit `L` if for every `ε > 0`, there exists an integer `N` such that for all `n ≥ N`, `d(xₙ, L) < ε`.
*   **Subsequence:** A sequence formed by selecting points from the original sequence in order. For example, if you have a sequence `(x₁, x₂, x₃, ...)`, then `(x₂, x₅, x₇, x₉, ...)` is a subsequence.

**Definition:**
A subset `K` of a metric space `(X, d)` is **sequentially compact** if **every sequence** in `K` has a **subsequence** that **converges to a point in `K`**.

Notice the crucial part: the limit point must be *inside* `K`. This is what differentiates a sequentially compact set from a merely bounded one.

**Example 1: A Closed and Bounded Interval**
Consider the set `K = [0, 1]` in `ℝ` with the standard metric.
*   Imagine any sequence of numbers within `[0, 1]`. For instance, `(1, 0.1, 0.01, 0.001, ...)`.
*   This sequence itself converges to `0`, which is in `[0, 1]`.
*   A more chaotic sequence, like `(0, 1, 0, 1, 0, 1, ...)`, does not converge. However, we can extract a subsequence, e.g., `(0, 0, 0, ...)` or `(1, 1, 1, ...)`, both of which converge to a point in `[0, 1]`.
This illustrates that `[0, 1]` is sequentially compact.

**Example 2: An Open Interval (Not Sequentially Compact)**
Now consider the set `U = (0, 1)`.
*   Take the sequence `(xₙ) = (1/2, 1/3, 1/4, ..., 1/n)`.
*   This sequence converges to `0`. However, `0` is **not** an element of the open set `(0, 1)`.
*   *Any* subsequence of `(xₙ)` will also converge to `0`. Since no subsequence converges to a point *inside* `(0, 1)`, the set is not sequentially compact.

---

#### **3. The Equivalence Theorem (Why This Matters)**

For metric spaces, the two notions of compactness are equivalent. This is a fundamental theorem.

**Theorem:** Let `(X, d)` be a metric space and `K ⊂ X`. The following are equivalent:
1.  `K` is **compact** (every open cover has a finite subcover).
2.  `K` is **sequentially compact** (every sequence has a convergent subsequence with limit in `K`).

This theorem is incredibly useful. It allows us to use the sequential definition (often easier to work with) to prove things about compact sets and vice-versa.

**Application: The Bolzano-Weierstrass Theorem**
You have likely seen this in calculus. It states: *"Every bounded sequence in `ℝⁿ` has a convergent subsequence."*
This is a direct consequence of the equivalence theorem. In `ℝⁿ`, a set is compact **if and only if** it is closed and bounded (Heine-Borel Theorem). Therefore, if a sequence is bounded, it is contained within some large closed ball, which is a compact set. By sequential compactness, a convergent subsequence must exist.

---

#### **4. Key Points & Summary**

| Key Point | Explanation |
| :--- | :--- |
| **Definition** | A set `K` is sequentially compact if **every** sequence in `K` has a **subsequence** converging to a point **in `K`**. |
| **Intuition** | No matter how a sequence "jumps around" inside the set, you can always find a pattern (a subsequence) that settles down to a point within the set. |
| **Equivalence** | In **metric spaces**, sequential compactness is **equivalent** to standard (open cover) compactness. This is a powerful tool. |
| **Relation to Closed & Bounded** | In `ℝⁿ` (and other finite-dimensional spaces), a set is sequentially compact **if and only if** it is **closed and bounded**. This is not true for all metric spaces. |
| **Why Engineers Care** | This concept is crucial for proving the existence of solutions (e.g., maxima/minima) in optimization problems and analyzing the convergence of numerical methods. |

**In a nutshell:** Sequential compactness provides an intuitive, sequence-based characterization of compactness in metric spaces. It ensures that limits of convergent subsequences remain trapped within the set, formalizing the ideas of "completeness" and "finiteness" that are central to analysis and its applications in engineering.