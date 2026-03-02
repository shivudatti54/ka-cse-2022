Of course. Here is a comprehensive educational note on Sequential Search methods for  Engineering students, specifically covering 3-Point and Fibonacci Search.

# Module 3: Sequential Search Methods - 3-Point & Fibonacci Search

## 1. Introduction

In single-variable unconstrained optimization, our goal is to find the minimum (or maximum) of a function `f(x)` within a given interval `[a, b]`, often called the interval of uncertainty. **Sequential search methods** are iterative techniques that systematically reduce this interval of uncertainty by evaluating the function at specific points within the interval. This note covers two classic methods: the simple **3-Point Search** and the highly efficient **Fibonacci Search** method.

## 2. Core Concepts & Explanation

### 2.1. 3-Point Search (Equal-Interval Search)

This is one of the simplest sequential search techniques. The core idea is to divide the initial interval `[a, b]` into four equal parts using three interior points, compare their function values, and discard the portion of the interval that cannot contain the minimum.

**Algorithm Steps:**

1.  **Initialization:** Start with the initial interval of uncertainty `[a₁, b₁]` and set iteration counter `k = 1`.
2.  **Point Selection:** Choose two interior points `x₁` and `x₂` such that they divide the interval into three equal segments.
    `x₁ = a_k + (b_k - a_k)/4`
    `x₂ = b_k - (b_k - a_k)/4 = a_k + 3*(b_k - a_k)/4`
3.  **Function Evaluation:** Compute `f(x₁)` and `f(x₂)`.
4.  **Interval Reduction:**
    - If `f(x₁) < f(x₂)`, then the minimum must lie in the subinterval `[a_k, x₂]`. Set `a_{k+1} = a_k` and `b_{k+1} = x₂`.
    - If `f(x₁) > f(x₂)`, then the minimum must lie in the subinterval `[x₁, b_k]`. Set `a_{k+1} = x₁` and `b_{k+1} = b_k`.
    - If `f(x₁) = f(x₂)`, the minimum lies in `[x₁, x₂]`. Set `a_{k+1} = x₁` and `b_{k+1} = x₂`.
5.  **Termination:** Check if the new interval length `(b_{k+1} - a_{k+1})` is small enough (less than a predefined tolerance `ϵ`). If yes, stop. The midpoint is the approximate optimum. If not, set `k = k+1` and go back to Step 2.

**Example:**
Minimize `f(x) = x²` over `[−2, 2]` with `ϵ = 0.4`.
_Iteration 1:_ `a₁=-2, b₁=2`. `x₁ = -2 + 4/4 = -1`, `x₂ = 2 - 4/4 = 1`.
`f(-1)=1`, `f(1)=1`. Since they are equal, new interval is `[-1, 1]`. Length = 2.
_Iteration 2:_ `a₂=-1, b₂=1`. `x₁ = -1 + 2/4 = -0.5`, `x₂ = 1 - 2/4 = 0.5`.
`f(-0.5)=0.25`, `f(0.5)=0.25`. New interval `[-0.5, 0.5]`. Length = 1.
_Iteration 3:_ Length (1) > `ϵ` (0.4), continue.
This process continues until the interval is sufficiently reduced.

### 2.2. Fibonacci Search Method

The Fibonacci method is an optimal sequential search technique that uses the famous Fibonacci sequence to determine the most efficient placement of evaluation points, minimizing the number of function evaluations required to reduce the interval to a given length.

The Fibonacci sequence is defined as:
`F₀ = 0, F₁ = 1, F_n = F_{n-1} + F_{n-2}` for `n >= 2` (i.e., 0, 1, 1, 2, 3, 5, 8, 13, ...).

**Algorithm Steps:**

1.  **Initialization:** Specify the final interval length `L` (or tolerance `ϵ`) and find the smallest `n` such that `F_n > (b₁ - a₁)/L`. This `n` determines the number of iterations/function evaluations needed.
2.  **Point Selection:** For iteration `k`, place two interior points symmetrically.
    `x₁ = a_k + (F_{n-k}/F_{n-k+1}) * (b_k - a_k)`
    `x₂ = a_k + (F_{n-k+1}/F_{n-k+2}) * (b_k - a_k) = b_k - (F_{n-k}/F_{n-k+2})*(b_k - a_k)`
    (Note: The ratios `F_{n-k}/F_{n-k+1}` and `F_{n-k+1}/F_{n-k+2}` are precomputed).
3.  **Function Evaluation & Reduction:** Compute `f(x₁)` and `f(x₂)`.
    - If `f(x₁) < f(x₂)`, set `b_{k+1} = x₂`.
    - If `f(x₁) > f(x₂)`, set `a_{k+1} = x₁`.
    - If they are equal, handle as in 3-point search.
4.  **Iterate:** Set `k = k+1`. For the next iteration, one of the points (`x₁` or `x₂`) is reused, and only one new function evaluation is needed. This is key to its efficiency.
5.  **Termination:** The process continues until `k = n-1`. The final interval will have length `(b₁ - a₁)/F_n`.

**Why it's Efficient:** The ratio of the interval reduction is `F_{n-k}/F_{n-k+1}`, which approaches the golden ratio. This method guarantees the smallest possible interval of uncertainty for a fixed number of function evaluations, making it optimal.

## 3. Key Points & Summary

| Feature                  | 3-Point Search                                                                                   | Fibonacci Search                                                    |
| :----------------------- | :----------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| **Principle**            | Divides interval into four equal segments.                                                       | Uses Fibonacci sequence for optimal point placement.                |
| **Efficiency**           | Less efficient. Reduces interval by a constant factor (~0.5) per iteration.                      | Highly efficient. Optimal method for a fixed number of evaluations. |
| **Function Evaluations** | Requires 2 new evaluations per iteration.                                                        | Requires only **1** new evaluation per iteration after the first.   |
| **Applications**         | Simple to understand and implement for quick, rough estimates.                                   | Preferred when function evaluations are computationally expensive.  |
| **Unimodality**          | **Both methods assume the function is unimodal** within `[a, b]` (has a single minimum/maximum). |

**Summary:**

- **Sequential search methods** iteratively reduce the interval of uncertainty to find the optimum of a unimodal function.
- The **3-Point Search** is a straightforward method using equally spaced points but is not optimal in terms of the number of required function evaluations.
- The **Fibonacci Search** is an optimal technique that minimizes the number of function calls for a desired interval reduction by leveraging the properties of the Fibonacci sequence. Its efficiency makes it superior for complex objective functions.
