Of course. Here is comprehensive educational content on "Functions – Plain and One-to-One" for  Engineering Students.

# Functions: Plain and One-to-One

## Introduction

In Discrete Mathematical Structures, after mastering relations, we move to a special, critically important type of relation called a **Function**. Functions are the backbone of computer science and engineering, modeling how inputs are transformed into outputs in algorithms, circuits, and software. This module focuses on understanding what a function is and a key property that defines its behavior: being **one-to-one**.

## Core Concepts

### 1. Plain Function (Definition)

A function is a relation with a specific constraint. Formally, a function `f` from a set `A` (domain) to a set `B` (codomain) is a relation such that **every element of `A` is related to exactly one element of `B`**.

This means two things:

1.  **Every input has an output:** For every `a ∈ A`, there exists some `b ∈ B` such that `(a, b) ∈ f`.
2.  **No input has multiple outputs:** If `(a, b) ∈ f` and `(a, c) ∈ f`, then `b = c`. An input cannot point to two different outputs.

We denote a function as `f: A → B`.

**Example:**
Let `A = {1, 2, 3}` and `B = {x, y, z}`.

- `f = {(1, x), (2, y), (3, x)}` is a function. Each input has exactly one output.
- `g = {(1, x), (1, y), (2, z)}` is **NOT** a function because the input `1` is related to two different outputs (`x` and `y`).
- `h = {(1, x), (2, y)}` is **NOT** a function from `A` to `B` because the input `3` has no output.

### 2. One-to-One Function (Injection)

A one-to-one (or injective) function is a function where **distinct inputs always produce distinct outputs**. No two different elements in the domain map to the same element in the codomain.

**Formal Definition:**
A function `f: A → B` is **one-to-one** (injective) if and only if:
`f(a₁) = f(a₂)` implies `a₁ = a₂` for all `a₁, a₂` in the domain `A`.
The contrapositive is often more intuitive: if `a₁ ≠ a₂`, then `f(a₁) ≠ f(a₂)`.

**Example 1: One-to-One**
Let `A = {1, 2, 3}`, `B = {w, x, y, z}`. Define `f: A → B` as:
`f(1) = w`, `f(2) = x`, `f(3) = y`
This is one-to-one. All outputs are unique.

**Example 2: Not One-to-One**
Let `A = {1, 2, 3}`, `B = {x, y, z}`. Define `g: A → B` as:
`g(1) = x`, `g(2) = y`, `g(3) = x`
This is a valid function, but it is **not** one-to-one. Two distinct inputs, `1` and `3`, both map to the same output `x`.

### Visualizing the Difference

The standard arrow diagrams make these concepts clear:

- **Function:** Every element in the domain has exactly one arrow starting from it.
- **One-to-One Function:** Every element in the domain has exactly one arrow starting from it, and every element in the codomain has **at most one** arrow ending at it.

## Key Points and Summary

| Concept                             | Definition                                                          | Key Rule                                                                              |
| :---------------------------------- | :------------------------------------------------------------------ | :------------------------------------------------------------------------------------ |
| **Function (Plain)**                | A relation from `A` to `B` where each input has exactly one output. | For every `a ∈ A`, there is **exactly one** `b ∈ B` with `(a, b) ∈ f`.                |
| **One-to-One (Injective) Function** | A function where distinct inputs map to distinct outputs.           | If `a₁ ≠ a₂`, then `f(a₁) ≠ f(a₂)`. Equivalently, if `f(a₁) = f(a₂)`, then `a₁ = a₂`. |

- **All one-to-one functions are functions,** but not all functions are one-to-one.
- The property of being one-to-one is crucial for concepts like **inverse functions** (which you will study later). A function must be one-to-one (and onto) to have a full inverse.
- In computer science, a **hash function** that is not one-to-one leads to _collisions_, where different inputs produce the same hash value, a critical consideration in data retrieval and cryptography.
- To prove a function is **one-to-one**, start with the assumption `f(a₁) = f(a₂)` and use algebraic manipulation to show that this forces `a₁ = a₂`.
