Of course. Here is a comprehensive educational content piece on the Binomial Theorem for  Engineering students.

# Module 2: Combinations – The Binomial Theorem

**Subject:** Discrete Mathematical Structures (DMS) | **Semester:** IV

---

## 1. Introduction

In the previous modules, you learned about permutations and combinations, which are fundamental for counting arrangements and selections. The **Binomial Theorem** is a powerful algebraic extension of combinations (`C(n, r)`). It provides a formula for expanding expressions raised to any positive integer power, of the form `(x + y)^n`. Instead of multiplying `(x + y)` by itself `n` times, which is tedious, the theorem gives us a direct, elegant solution using combinatorial principles. It is indispensable in fields like computer science (algorithm analysis, probability), engineering mathematics, and cryptography.

## 2. Core Concepts

### 2.1. The Binomial Theorem Statement

For any positive integer `n` and any real numbers `x` and `y`:

**`(x + y)^n = Σ_{r=0}^{n} C(n, r) * x^{n-r} * y^r`**

Where:

- `Σ_{r=0}^{n}` means "the sum from `r = 0` to `r = n`".
- `C(n, r)` is the number of combinations of `n` items taken `r` at a time, also written as `\binom{n}{r}` and called a **binomial coefficient**.

The expanded form is:
`(x + y)^n = C(n,0)x^n y^0 + C(n,1)x^{n-1}y^1 + C(n,2)x^{n-2}y^2 + ... + C(n,n)x^0 y^n`

### 2.2. Understanding the Components

1.  **Binomial Coefficients (`C(n, r)` or `\binom{n}{r}`):** These are the numerical coefficients in the expansion. Notice how for each term, the value of `r` in `C(n, r)` corresponds to the power of `y`. The coefficients are symmetric: `C(n, r) = C(n, n-r)`.
2.  **Powers of `x` and `y`:** In each term, the sum of the exponents of `x` and `y` is always `n`. The exponent of `x` decreases from `n` to `0`, while the exponent of `y` increases from `0` to `n`.
3.  **The General Term:** Often, we need to find a specific term in the expansion. The `(r+1)^{th}` term (or `T_{r+1}`) is given by:
    **`T_{r+1} = C(n, r) * x^{n-r} * y^r`**
    This is extremely useful when you don't need the entire expansion.

### 2.3. Connection to Combinations

Why do combinations appear here? The coefficient `C(n, r)` represents the number of ways to choose `r` instances of the variable `y` from the `n` binomial factors `(x + y)`. For example, when expanding `(x + y)^3 = (x+y)(x+y)(x+y)`, the term `xy^2` is formed by choosing `y` from two of the three factors and `x` from the remaining one. There are exactly `C(3, 2) = 3` ways to do this: (1st factor `x`, 2nd & 3rd `y`), (2nd factor `x`, 1st & 3rd `y`), and (3rd factor `x`, 1st & 2nd `y`). Hence, the coefficient for `xy^2` is 3.

## 3. Examples

**Example 1: Expand `(x + 2y)^4`**

Here, `n=4`, `x` is `x`, and `y` is `2y`.
`(x + 2y)^4 = Σ_{r=0}^{4} C(4, r) * x^{4-r} * (2y)^r`

Let's calculate term-by-term:

- `r=0`: `C(4,0) * x^4 * (2y)^0 = 1 * x^4 * 1 = x^4`
- `r=1`: `C(4,1) * x^3 * (2y)^1 = 4 * x^3 * 2y = 8x^3y`
- `r=2`: `C(4,2) * x^2 * (2y)^2 = 6 * x^2 * 4y^2 = 24x^2y^2`
- `r=3`: `C(4,3) * x^1 * (2y)^3 = 4 * x * 8y^3 = 32xy^3`
- `r=4`: `C(4,4) * x^0 * (2y)^4 = 1 * 1 * 16y^4 = 16y^4`

**Therefore, `(x + 2y)^4 = x^4 + 8x^3y + 24x^2y^2 + 32xy^3 + 16y^4`**

**Example 2: Find the coefficient of `x^5` in the expansion of `(2x - 3)^7`.**

This is a job for the general term. We have `(2x + (-3))^7`, so `n=7`.
The general term is: `T_{r+1} = C(7, r) * (2x)^{7-r} * (-3)^r`

We need the term where the power of `x` is 5. Therefore, the exponent of `(2x)` must be 5, so `7 - r = 5`, which gives `r = 2`.

Now, plug `r=2` into the general term to find the _entire_ term and its coefficient:
`T_{3} = C(7, 2) * (2x)^{5} * (-3)^2`
`= 21 * (32x^5) * 9`
`= 21 * 32 * 9 * x^5`
`= 6048 x^5`

**Therefore, the coefficient of `x^5` is 6048.**

## 4. Key Points & Summary

- **Purpose:** The Binomial Theorem provides a formula to expand expressions of the form `(x + y)^n` efficiently without manual multiplication.
- **Formula:** `(x + y)^n = Σ_{r=0}^{n} C(n, r) * x^{n-r} * y^r`
- **Binomial Coefficients:** The coefficients `C(n, r)` are central to the theorem and demonstrate a direct application of combinations.
- **General Term:** The `(r+1)^{th}` term, `T_{r+1} = C(n, r) * x^{n-r} * y^r`, is used to find any specific term in the expansion.
- **Symmetry:** The coefficients are symmetric (`C(n, r) = C(n, n-r)`), and the expansion has `n+1` terms.
- ** Relevance:** This is a crucial topic for your DMS course. Mastery is essential for solving problems in exams and for its applications in more advanced topics like probability and generating functions.
