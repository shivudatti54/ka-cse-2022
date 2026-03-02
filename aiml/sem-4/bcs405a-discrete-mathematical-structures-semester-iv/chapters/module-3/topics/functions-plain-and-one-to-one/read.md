Of course. Here is comprehensive educational content on Functions, Plain and One-to-One, tailored for  Engineering students.

# Functions: Plain and One-to-One

## Introduction

In Discrete Mathematical Structures, after mastering relations, we move to a special and fundamental type of relation: the **Function**. Functions are the cornerstone of not only mathematics but also computer science and engineering. They are used to model inputs and outputs of algorithms, define sequences, and describe relationships where each input has a single, unambiguous output. This note focuses on understanding plain functions and a specific, important category: one-to-one functions.

## Core Concepts

### 1. What is a Function?

A function is a relation from a set `A` (domain) to a set `B` (codomain) with a crucial restriction: **every element of `A` must be related to exactly one element in `B`**.

**Formal Definition:**
A function `f` from set `A` to set `B` (denoted `f: A → B`) is a relation such that:
1.  **For every** `a ∈ A`, there exists **at least one** `b ∈ B` such that `(a, b) ∈ f`. (This is the **domain condition**).
2.  If `(a, b) ∈ f` and `(a, c) ∈ f`, then `b = c`. (This is the **uniqueness condition**).

The element `b` associated with `a` is called the **image** of `a` under `f` and is written `b = f(a)`. The set of all images `{f(a) | a ∈ A}` is called the **range** of `f`. Note that the range is a subset of the codomain (`Range ⊆ Codomain B`).

**Example 1:**
Let `A = {1, 2, 3}` and `B = {x, y, z}`.
The relation `f = {(1, x), (2, y), (3, x)}` **is a function**. Each element in `A` has a single, defined image.
*   Domain: `{1, 2, 3}`
*   Codomain: `{x, y, z}`
*   Range: `{x, y}`

**Example 2:**
The relation `g = {(1, x), (1, y), (2, z)}` is **NOT a function** because the element `1 ∈ A` is related to two different elements (`x` and `y`), violating the uniqueness condition.

### 2. Types of Functions: One-to-One (Injectivity)

A key way to classify functions is by how they map elements from the domain to the codomain. A **One-to-One (Injective) Function** is one where distinct inputs always map to distinct outputs.

**Formal Definition:**
A function `f: A → B` is said to be **one-to-one (or injective)** if and only if:
`f(a₁) = f(a₂)` implies `a₁ = a₂` for all `a₁, a₂` in the domain `A`.
In other words, **different inputs must produce different outputs**.

**How to Prove Injectivity:**
To prove a function is one-to-one, you assume `f(a) = f(b)` and then show that this assumption logically forces `a = b`.

**Example 3 (One-to-One):**
Let `f: Z → Z` be defined by `f(x) = 2x + 3`.
*   Assume `f(a) = f(b)`. This means `2a + 3 = 2b + 3`.
*   Subtracting 3 from both sides: `2a = 2b`.
*   Dividing by 2: `a = b`.
Since `f(a) = f(b)` implies `a = b`, the function `f` is **one-to-one**.

**Example 4 (Not One-to-One):**
Let `g: R → R` be defined by `g(x) = x²`.
*   Check: Is `g(a) = g(b)`?
    *   Let `a = 2` and `b = -2`.
    *   `g(2) = 4` and `g(-2) = 4`.
    *   So, `g(2) = g(-2)` but `2 ≠ -2`.
Since we found two distinct inputs that produce the same output, the function `g` is **not one-to-one**.

**The Horizontal Line Test (Conceptual):**
For functions with real-number inputs and outputs, a function is one-to-one if no horizontal line intersects its graph more than once. The function in Example 3 (a line) passes this test. The function in Example 4 (a parabola) fails it.

## Key Points & Summary

| Concept | Definition | Key Idea |
| :--- | :--- | :--- |
| **Function (`f: A → B`)** | A relation where **every element** in `A` is related to **exactly one element** in `B`. | For every input, there is one and only one output. |
| **Domain** | The set of all starting points (inputs), Set `A`. | All possible `a` values for which `f(a)` is defined. |
| **Codomain** | The set `B` that contains all possible outputs. | The "type" or "set" of the outputs. |
| **Range** | The set of all actual outputs, `{f(a) \| a ∈ A}`. | A subset of the codomain. |
| **One-to-One (Injective)** | If `f(a) = f(b)` then it must be that `a = b`. | **Distinct inputs map to distinct outputs.** No two different inputs share the same output. |

*   A function must be defined for **every element** in its domain.
*   The **range** can be smaller than the **codomain**, but never larger.
*   Injectivity (one-to-one) is about the **uniqueness of mappings forward**. It ensures the function never "collapses" two different inputs into the same output, which is a critical property in cryptography, hashing, and invertibility of functions.
*   Not all functions are one-to-one. A function that is not one-to-one is often called "many-to-one".