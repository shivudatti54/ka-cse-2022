Of course. Here is a comprehensive educational note on Sequential Search methods, specifically the 3-Point Search and Fibonacci Search, tailored for  Engineering students.

# Module 3: Sequential Search Methods - 3-Point & Fibonacci Search

## 1. Introduction

In single-variable unconstrained optimization, our goal is to find the minimum (or maximum) of a function `f(x)` within a given interval `[a, b]` where the function is **unimodal** (has only one optimum). Sequential search methods are iterative techniques that systematically reduce this interval of uncertainty until it becomes sufficiently small, pinpointing the location of the optimum. This note covers two such powerful methods: the 3-Point Search and the highly efficient Fibonacci Search.

## 2. Core Concepts

### Unimodality: The Fundamental Assumption
Both methods require the function to be unimodal on `[a, b]`. This means the function has a single minimum (or maximum), and it is strictly decreasing on one side of this point and strictly increasing on the other. This property allows us to eliminate portions of the interval after each evaluation.

### The General Principle
The algorithms start with the initial interval `[a, b]`. They select one or more interior points, evaluate the function at these points, and compare the values. Based on this comparison, a portion of the interval is discarded because the optimum cannot lie there. The remaining, smaller interval is then used for the next iteration. This process repeats until the interval size is less than a predefined tolerance (`ε`).

---

## 3. 3-Point Search (Equal-Interval Search)

This is a straightforward, robust method where the initial interval is divided into four equal parts using three symmetrically placed interior points.

### Algorithm Steps:
1.  **Initialization:** Start with the initial interval `[a, b]`. Set the tolerance `ε`.
2.  **Calculate Points:** Compute the two intermediate points that divide the interval into four equal parts:
    *   `x₁ = a + (b - a)/4`
    *   `x_m = (a + b)/2` (midpoint)
    *   `x₂ = b - (b - a)/4`
3.  **Evaluate & Compare:** Calculate `f₁ = f(x₁)`, `f_m = f(x_m)`, and `f₂ = f(x₂)`.
4.  **Eliminate Interval:**
    *   If `f₁ < f_m`, the minimum must lie in `[a, x_m]`. Set `b = x_m`.
    *   If `f_m < f₁` and `f_m < f₂`, the minimum is in `[x₁, x₂]`. Set `a = x₁` and `b = x₂`.
    *   If `f₂ < f_m`, the minimum must lie in `[x_m, b]`. Set `a = x_m`.
5.  **Check Tolerance:** Calculate the new interval length. If `(b - a) < ε`, stop. The optimum is approximately at the center of the final interval. Otherwise, go back to Step 2.

**Example:** For `f(x) = x²` on `[-2, 2]`:
*   `x₁ = -1`, `x_m = 0`, `x₂ = 1`. `f(1)=1`, `f(0)=0`, `f(1)=1`.
*   Since `f_m < f₁` and `f_m < f₂`, the new interval becomes `[-1, 1]`.
*   The next iteration would evaluate points at `-0.5`, `0`, and `0.5`, and again shrink the interval.

---

## 4. Fibonacci Search

This is the most efficient sequential search method in terms of the number of function evaluations required to achieve a desired reduction in the interval size. It uses the famous Fibonacci sequence to determine the optimal location of the interior points, minimizing the worst-case scenario interval length.

### Fibonacci Sequence:
Defined by `F₀ = 0`, `F₁ = 1`, and `Fₙ = Fₙ₋₁ + Fₙ₋₂` for `n >= 2`. The sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

### Algorithm Steps:
1.  **Initialization:** Specify the final interval length `L` (or tolerance `ε`) and determine the number of iterations `n` such that `Fₙ > (b₀ - a₀)/L`.
2.  **Set Initial Points:** For the first iteration (`k=1`), set:
    *   `x₁ = a₀ + (Fₙ₋₂ / Fₙ) * (b₀ - a₀)`
    *   `x₂ = a₀ + (Fₙ₋₁ / Fₙ) * (b₀ - a₀)`
3.  **Evaluate & Compare:** Calculate `f(x₁)` and `f(x₂)`.
    *   If `f(x₁) < f(x₂)`, eliminate the interval `[x₂, b]`. Set `b = x₂`.
    *   If `f(x₁) > f(x₂)`, eliminate the interval `[a, x₁]`. Set `a = x₁`.
4.  **Update for Next Iteration:** Set `k = k+1`. For the next iteration, only one new point needs to be calculated. The ratio of Fibonacci numbers changes for each step. The new point is placed at a distance of `(Fₙ₋ₖ₋₁ / Fₙ₋ₖ₊₁) * (new_interval_length)` from one end.
5.  **Terminate:** After `n-1` iterations, the interval is reduced to the required length. The optimum lies within this final interval.

**Why it's Efficient:** The placement of points ensures that the worst-case reduction ratio is maximized each time. After `n` evaluations, the initial interval is reduced by a factor of `1/Fₙ`, which is the best possible reduction.

---

## 5. Key Points & Summary

| Feature | 3-Point Search | Fibonacci Search |
| :--- | :--- | :--- |
| **Concept** | Divides interval into 4 equal parts using 3 points. | Uses Fibonacci sequence to optimally place points. |
| **Efficiency** | Good and simple. Reduces interval by ~1/2 per iteration. | **Most efficient.** Minimizes the number of function evaluations for a given reduction. |
| **Function Evaluations per Iteration** | 3 (but reuses one, so effectively 2 new ones after 1st iter). | 1 new evaluation per iteration after the first. |
| **Best For** | Simple implementation and understanding. | Problems where each function evaluation is computationally expensive. |
| **Requirement** | Function must be unimodal on `[a, b]`. | Function must be unimodal on `[a, b]`. |

**Summary:**
*   Both are **interval reduction** methods for finding the optimum of a **unimodal function**.
*   The **3-Point Search** is intuitive and easy to code, making it a good introductory method.
*   The **Fibonacci Search** is the optimal strategy in terms of minimizing the number of required function evaluations to achieve a specific interval reduction. It is the preferred choice when evaluating the function `f(x)` is computationally costly.
*   The final interval after `n` iterations in Fibonacci search is `(b₀ - a₀) / Fₙ`.