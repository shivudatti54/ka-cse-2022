Of course. Here is a comprehensive explanation on Functions, focusing on Plain and One-to-One types, tailored for  Engineering students.

# Functions: Plain and One-to-One (Module 3)

## 1. Introduction

In Discrete Mathematical Structures, a **function** is a fundamental concept that formalizes a relationship between two sets where each input from the first set is connected to *exactly one* output in the second set. This is crucial in computer science for modeling tasks like hashing (where an input should always produce the same hash value), database operations, and defining algorithms. This note focuses on understanding general functions and a specific, important type: **one-to-one (injective)** functions.

---

## 2. Core Concepts

### What is a Function?

Let `A` and `B` be two non-empty sets. A function `f` from `A` to `B`, denoted `f: A → B`, is a rule that assigns to **each element** `a ∈ A` **exactly one element** `b ∈ B`.

*   The set `A` is called the **domain**.
*   The set `B` is called the **codomain**.
*   For an element `a ∈ A`, the assigned element `b ∈ B` is called the **image** of `a` under `f`, written `b = f(a)`.
*   The set of all images `{ f(a) | a ∈ A }` is called the **range** (or image) of `f`. Note: The range is always a **subset** of the codomain (`Range ⊆ Codomain`).

**Key Property:** A relation from A to B is a function only if **every element in the domain (A) must have exactly one arrow coming out of it.**

### Types of Functions: One-to-One (Injective)

A function `f: A → B` is said to be **one-to-one** (or **injective**) if distinct elements in the domain map to distinct elements in the codomain.

In simpler terms: **No two different inputs produce the same output.**

**Formal Definition:**
A function `f` is one-to-one if and only if for all `a₁, a₂ ∈ A`,
`if f(a₁) = f(a₂), then a₁ = a₂`.

The contrapositive is often more intuitive to use: `if a₁ ≠ a₂, then f(a₁) ≠ f(a₂)`.

**Visual Check (Arrow Diagram):** In a one-to-one function, **no two arrows from the domain should point to the same element in the codomain.** An element in the codomain can have *at most one* arrow pointing to it. It's okay if some codomain elements have no arrows.

---

## 3. Examples

Let `A = {1, 2, 3}` and `B = {a, b, c, d}`.

**Example 1: A Plain Function (Not One-to-One)**
Define `f: A → B` as:
`f(1) = a`, `f(2) = b`, `f(3) = a`

*   **Is it a function?** Yes. Every element in `A` has exactly one image in `B`.
*   **Is it one-to-one?** No. Because `f(1) = f(3) = a`, but `1 ≠ 3`. Two distinct inputs (`1` and `3`) map to the same output (`a`).

**Example 2: A One-to-One Function**
Define `g: A → B` as:
`g(1) = a`, `g(2) = c`, `g(3) = b`

*   **Is it a function?** Yes.
*   **Is it one-to-one?** Yes. All outputs `a`, `c`, and `b` are distinct. No two inputs share an output.

**Example 3: A Function that is Not Possible**
Define a relation `h: A → B` as:
`h(1) = a`, `h(2) = b`  ( element `3` in the domain is not assigned any image)
This is **NOT a function** because the element `3 ∈ A` has no image. It violates the rule that every domain element must have an assignment.

**Example 4: Relevant to CS - A Hashing Function**
Imagine a simple hashing function `h(n) = n mod 5`, where the domain is a set of student IDs `{100, 101, 102, 103, 104}` and the codomain is the set of hash buckets `{0, 1, 2, 3, 4}`.

*   `h(100) = 0`
*   `h(101) = 1`
*   `h(102) = 2`
*   `h(103) = 3`
*   `h(104) = 4`

This function **is one-to-one** for this specific domain, as each input produces a unique hash value (output). If two different IDs produced the same hash (e.g., `h(105)` would also be `0`), it would not be one-to-one, leading to a **hash collision**.

---

## 4. Key Points & Summary

| Feature | Description | Key Check |
| :--- | :--- | :--- |
| **Function (`f: A → B`)** | A rule assigning **every** element `a ∈ A` to **exactly one** element `b ∈ B`. | Does every element in the domain have **exactly one** arrow? |
| **Domain** | The set of all inputs (`A`). | |
| **Codomain** | The set of all possible outputs (`B`). | |
| **Range** | The set of all **actual** outputs `{f(a) for all a in A}`. | `Range ⊆ Codomain` |
| **One-to-One (Injective)** | A function where **distinct inputs have distinct outputs**. | Does `f(a₁)=f(a₂)` imply `a₁=a₂`? Do any two arrows hit the same codomain element? |

*   The property of being one-to-one is crucial for functions that must be **reversible** or where **uniqueness** is required.
*   A one-to-one function ensures that information from the domain is not "lost" or conflated when mapped to the codomain.
*   Remember: **All one-to-one functions are functions, but not all functions are one-to-one.**