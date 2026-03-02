Of course. Here is a comprehensive educational note on Sequential Search Methods (3-Point and Fibonacci) for  Engineering students.

# Module 3: Convex Optimization-1
## Sequential Search Methods: 3-Point & Fibonacci Search

### 1. Introduction

In single-variable unconstrained optimization, our goal is to find the minimum (or maximum) of a unimodal function `f(x)` over an interval `[a, b]`. A function is **unimodal** if it has a single optimum (one valley) within the interval. Sequential search methods are iterative techniques that systematically reduce the interval of uncertainty (the range where the optimum is known to lie) by evaluating the function at specific points within the interval. Two classic and efficient methods are the **3-Point Search** (a specific implementation of the Golden Section Search) and the **Fibonacci Search**.

---

### 2. Core Concepts

#### The Principle of Interval Reduction

Both methods work on a fundamental principle:
1.  Start with an initial interval of uncertainty, `I₀ = [a, b]`.
2.  Choose two *interior points*, `x₁` and `x₂` (`x₁ < x₂`), within this interval.
3.  Evaluate `f(x₁)` and `f(x₂)`.
4.  Based on the function values, eliminate a portion of the interval:
    *   If `f(x₁) > f(x₂)`, the minimum cannot lie in `[a, x₁]`, so the new interval becomes `[x₁, b]`.
    *   If `f(x₁) < f(x₂)`, the minimum cannot lie in `[x₂, b]`, so the new interval becomes `[a, x₂]`.
5.  The process is repeated on the new, smaller interval until it is smaller than a predefined tolerance `ε`.

The key difference between the methods is *how* these interior points are chosen to maximize efficiency.

#### 3-Point Search (Golden Section Search)

This method chooses the two interior points such that one of them can be **reused** in the next iteration, drastically reducing the number of function evaluations required. The points are chosen according to the golden ratio, `τ ≈ 0.618`.

*   **Initial Points:**
    `x₁ = b - τ(b - a)`
    `x₂ = a + τ(b - a)`

*   **Why it's efficient:** After each iteration, the interval is reduced to `τ ≈ 61.8%` of its previous length. More importantly, one of the points from the previous iteration becomes a new interior point for the next iteration, meaning only **one new function evaluation** is needed per iteration.

#### Fibonacci Search

This method uses the Fibonacci number sequence to determine the interior points. The Fibonacci sequence is defined as `F₀=0, F₁=1, Fₙ = Fₙ₋₁ + Fₙ₋₂`. This method is optimal in the sense that it minimizes the maximum number of function evaluations needed to achieve a desired interval reduction.

*   **How it works:** The number of iterations `n` is decided upfront based on the final desired interval length `ε` and the initial interval length `L₀ = (b-a)`. The ratio of interval reduction in each step `k` is determined by Fibonacci numbers: `ρₖ = 1 - (Fₙ₋ₖ / Fₙ₋ₖ₊₁)`.

*   **Initial Points for iteration 1:**
    `x₁ = a + (Fₙ₋₂ / Fₙ)(b - a)`
    `x₂ = a + (Fₙ₋₁ / Fₙ)(b - a)`

*   **Why it's efficient:** It provides the smallest possible interval of uncertainty for a *fixed number of function evaluations*. However, unlike the 3-point search, the reduction ratio changes each iteration, and the number of iterations must be fixed in advance.

---

### 3. Example: 3-Point Search Iteration

Let's minimize `f(x) = x² + 2x` over the initial interval `[-3, 5]` with a tolerance. The exact minimum is at `x = -1`.

**Iteration 1:**
*   `a = -3`, `b = 5`
*   `τ = (√5 - 1)/2 ≈ 0.618`
*   `x₁ = b - τ(b - a) = 5 - 0.618*(8) = 0.056`
*   `x₂ = a + τ(b - a) = -3 + 0.618*(8) = 1.944`
*   `f(x₁) = (0.056)² + 2*(0.056) ≈ 0.115`
*   `f(x₂) = (1.944)² + 2*(1.944) ≈ 7.667`
*   Since `f(x₁) < f(x₂)`, the minimum must lie in `[a, x₂] = [-3, 1.944]`. We discard `[x₂, 5]`.
*   **Note:** `x₁ (0.056)` becomes the new `x₂` for the next iteration, so we only need to calculate one new point.

**Iteration 2:**
*   New interval: `a = -3`, `b = 1.944`
*   Reuse `x₂ (old x₁) = 0.056`
*   Calculate new `x₁ = b - τ(b - a) = 1.944 - 0.618*(4.944) ≈ -1.112`
*   `f(new x₁) = (-1.112)² + 2*(-1.112) ≈ -1.111`
*   `f(x₂) = f(0.056) ≈ 0.115`
*   Since `f(x₁) < f(x₂)`, the new interval becomes `[a, x₂] = [-3, 0.056]`.

This process continues until `(b - a) < ε`.

---

### 4. Key Points & Summary

| Feature | 3-Point (Golden Section) Search | Fibonacci Search |
| :--- | :--- | :--- |
| **Basis** | Uses the constant golden ratio (`τ ≈ 0.618`). | Uses the Fibonacci number sequence. |
| **Iterations** | Can run until a tolerance is met. | Number of iterations `n` must be pre-defined. |
| **Efficiency** | Very efficient, requires only 1 new evaluation per iteration. | Theoretically **most efficient** for a fixed `n`, minimizes worst-case uncertainty. |
| **Interval Reduction** | Fixed ratio: each iteration reduces interval to ~61.8% of previous size. | Variable ratio: reduction ratio changes each iteration. |
| **Application** | Excellent general-purpose method. Best when the number of evaluations is unknown. | Best when the cost of evaluation is very high and a fixed precision is required. |
| **Requirement** | Function must be **unimodal** over `[a, b]`. | Function must be **unimodal** over `[a, b]`. |

**Summary:**
Both 3-Point and Fibonacci searches are powerful, derivative-free methods for finding the optimum of a unimodal function. The 3-Point search is simpler to implement as it uses a constant reduction factor and does not require pre-defining the number of iterations. Fibonacci search is optimal for a fixed budget of function evaluations. For most practical purposes in engineering optimization, the 3-Point (Golden Section) search is widely used due to its robustness and simplicity.