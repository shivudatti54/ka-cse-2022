# Module 3: Complete Metric Spaces and Continuous Functions

**Subject:** Metric Spaces
**Semester:** IV

---

## 1. Introduction

Welcome to Module 3. In our previous modules, we defined a metric space as a set equipped with a distance function (`d(x, y)`) satisfying positivity, symmetry, and the triangle inequality. Now, we delve deeper into the analysis of these spaces. A fundamental question arises: **Do all sequences that "should" converge actually have a limit point within our space?** The answer defines the crucial property of *completeness*. Furthermore, we will explore how the structure of a metric space allows us to rigorously define and analyze *continuous functions*, bridging the gap between metric spaces and calculus.

## 2. Core Concepts

### 2.1 Cauchy Sequences

Before we can define a complete space, we need a way to describe sequences that are "trying" to converge.

*   **Definition:** A sequence `(x_n)` in a metric space `(X, d)` is called a **Cauchy sequence** if for every `ε > 0`, there exists a positive integer `N` (depending on `ε`) such that for all `m, n ≥ N`, we have `d(x_m, x_n) < ε`.
*   **Intuition:** The terms of the sequence get arbitrarily close to *each other* as the sequence progresses. This is a stronger condition than just consecutive terms getting close; it requires *all* subsequent terms to cluster together.

**Example:** Consider the sequence `x_n = 1/n` in the metric space `(R, d_std)`. Is it Cauchy?
For `m, n ≥ N`, `d(1/m, 1/n) = |1/m - 1/n| ≤ |1/m| + |1/n| ≤ 1/N + 1/N = 2/N`. For any `ε > 0`, choose `N > 2/ε`. Then for all `m, n ≥ N`, `d(x_m, x_n) < ε`. So, yes, it is Cauchy.

**Key Fact:** **Every convergent sequence is Cauchy.** However, the converse is not always true.

### 2.2 Complete Metric Spaces

This brings us to the central concept of this module.

*   **Definition:** A metric space `(X, d)` is called **complete** if every Cauchy sequence in `X` converges to a limit that is also in `X`.
*   **Intuition:** A complete space has no "holes" or "missing points" that Cauchy sequences might try to converge to. All sequences that behave like they are converging actually have a destination within the space.

**Examples and Non-Examples:**

1.  **`(R, d_std)` is complete.** This is a fundamental result from real analysis (the Cauchy Convergence Criterion).
2.  **`(Q, d_std)` is NOT complete.** Consider the sequence of rational numbers `(1, 1.4, 1.41, 1.414, ...)` converging to `√2`. This is a Cauchy sequence in `Q`, but its limit `√2` is *irrational* and hence not in `Q`. Therefore, `Q` is incomplete.
3.  **`(R^n, d_ Euclidean)` is complete.** This is a generalization of the completeness of `R`.

### 2.3 Continuous Functions in Metric Spaces

We can now generalize the `ε-δ` definition of continuity from calculus to any metric space.

*   **Definition:** Let `f: (X, d_X) → (Y, d_Y)` be a function between two metric spaces. Let `a ∈ X`.
    *   We say `f` is **continuous at a** if for every `ε > 0`, there exists a `δ > 0` such that:
        `if d_X(x, a) < δ then d_Y(f(x), f(a)) < ε`.
    *   We say `f` is **continuous on X** if it is continuous at every point `a ∈ X`.
*   **Sequential Characterization:** A function `f` is continuous at `a` **if and only if** for every sequence `(x_n)` in `X` that converges to `a` (i.e., `x_n → a`), the image sequence converges to `f(a)` in `Y` (i.e., `f(x_n) → f(a)`).
    This equivalent definition is often much easier to use for proofs.

**Example:** Let `f: (R^2, d_2) → (R, d_std)` be defined by `f(x, y) = 2x + y`. Prove it's continuous.
*Proof (using ε-δ):* Let `ε > 0` and `a = (a1, a2) ∈ R^2`. Choose `δ = ε / 3`. If `d((x,y), (a1,a2)) = sqrt((x-a1)^2 + (y-a2)^2) < δ`, then `|x-a1| < δ` and `|y-a2| < δ`.
Now, `|f(x,y) - f(a1,a2)| = |(2x+y) - (2a1+a2)| ≤ 2|x-a1| + |y-a2| < 2δ + δ = 3δ = ε`. ∎

## 3. Key Points & Summary

*   **Cauchy Sequence:** A sequence where terms get arbitrarily close to each other (`d(x_m, x_n) → 0` as `m,n → ∞`).
*   **Complete Metric Space:** A space where every Cauchy sequence has a limit *within the space*. It has no "missing" points.
*   **Continuity:** A function `f: X → Y` is continuous if it preserves limits: `x_n → a` implies `f(x_n) → f(a)`.
*   **Why it matters:** Completeness is a vital property for performing calculus and analysis. Key theorems like the Banach Fixed-Point Theorem (used in solving equations numerically) and the Weierstrass Maximum Value Theorem require the underlying space to be complete. Continuity is the foundational concept for connecting the structures of different metric spaces.