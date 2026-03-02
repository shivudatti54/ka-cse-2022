# Combinations with Repetition

## Introduction

In Module 2: Properties of the Integers, we explore various combinatorial principles that are fundamental to Discrete Mathematical Structures. A common combinatorial problem is selecting items from a set where the order does not matter—a *combination*. However, standard combinations (C(n, r)) assume we select items without replacement. What happens when we are allowed to select the same item more than once? This scenario, such as ordering multiple identical donuts from a shop or dealing with indistinguishable items, is solved using the concept of **Combinations with Repetition**.

## Core Concepts

A **combination with repetition** (or *multiset combination*) is an unordered selection of items from a set where each item may be chosen more than once. The order of selection is still irrelevant.

The central question is: **How many ways can we choose `r` objects from `n` different types of objects, with repetition allowed?**

### The "Stars and Bars" Theorem

The most powerful method for solving these problems is the **Stars and Bars** combinatorial principle.

*   **Stars (`*`)**: Represent the `r` items we want to select. Since the items are indistinguishable in the selection (we care about *how many* of each type, not their identity), we depict them as identical stars.
*   **Bars (`|`)**: Represent the `n` categories or types of objects available. We use `(n - 1)` bars to create partitions between these categories.

The theorem states that the number of non-negative integer solutions to the equation:
`x₁ + x₂ + ... + xₙ = r` (where each `x_i` represents the number of times the i-th type is chosen)
is equal to the number of ways to arrange `r` stars and `(n - 1)` bars in a sequence.

The formula for the number of combinations with repetition is given by:
$$ \binom{r + n - 1}{r} = \binom{r + n - 1}{n - 1} $$
This is read as "`r + n - 1` choose `r`".

### Why This Formula Works?

Imagine we have `r = 6` stars (items) and `n = 4` types (so we need `n - 1 = 3` bars to create 4 bins).

One possible arrangement is: `** | * | | ***`
This sequence corresponds to the solution:
*   `x₁ = 2` (stars before the first bar)
*   `x₂ = 1` (stars between the first and second bar)
*   `x₃ = 0` (stars between the second and third bar)
*   `x₄ = 3` (stars after the third bar)

We are simply choosing `r` positions out of the total `(r + n - 1)` positions to place the stars (the remaining positions will be filled by bars), or equivalently, choosing `(n - 1)` positions for the bars. Hence, the total number of combinations is `\binom{r + n - 1}{r}`.

## Examples

**Example 1: The Donut Shop**
A shop has 4 types of donuts (n=4). How many ways can you select a box of 6 donuts (r=6)?

Here, the order doesn't matter, and you can choose more than one of the same type. This is a classic combinations with repetition problem.
$$ \text{Number of ways} = \binom{6 + 4 - 1}{6} = \binom{9}{6} = \binom{9}{3} = 84 $$

**Example 2: Integer Solutions**
Find the number of non-negative integer solutions to `x₁ + x₂ + x₃ = 8`.

This equation directly asks: in how many ways can we distribute 8 indistinguishable units (stars) into 3 distinct variables (bins created by `3-1=2` bars)?
$$ \text{Number of solutions} = \binom{8 + 3 - 1}{8} = \binom{10}{8} = \binom{10}{2} = 45 $$

**Example 3: Lower Bound Constraints**
How many solutions exist for `x₁ + x₂ + x₃ = 11`, where `x₁ >= 1`, `x₂ >= 2`, and `x₃ >= 3`?

We can transform this into a standard stars and bars problem by handling the constraints first. Define new variables:
*   Let `y₁ = x₁ - 1` (so `y₁ >= 0`)
*   Let `y₂ = x₂ - 2` (so `y₂ >= 0`)
*   Let `y₃ = x₃ - 3` (so `y₃ >= 0`)

Substitute into the original equation:
`(y₁ + 1) + (y₂ + 2) + (y₃ + 3) = 11 => y₁ + y₂ + y₃ = 5`

Now we find the number of non-negative integer solutions for the new equation.
$$ \binom{5 + 3 - 1}{5} = \binom{7}{5} = \binom{7}{2} = 21 $$

## Key Points & Summary

*   **Purpose**: Counts the number of ways to choose `r` items from `n` types **with repetition allowed** and **order not mattering**.
*   **Common Applications**: Counting donut orders, integer solutions to equations (`x₁ + x₂ + ... + xₙ = r`), placing indistinguishable items into distinct bins.
*   **Core Formula**: The number of such combinations is `\binom{r + n - 1}{r} = \binom{r + n - 1}{n - 1}`.
*   **Visual Method**: The "Stars and Bars" method provides an intuitive way to understand the problem. We arrange `r` stars and `(n-1)` bars.
*   **Constraints**: For problems with lower bounds (e.g., `x_i >= k`), use variable substitution to transform them into the standard non-negative integer solution form.
*   **Contrast**: This differs fundamentally from standard combinations `\binom{n}{r}`, which is used for selection **without replacement**.