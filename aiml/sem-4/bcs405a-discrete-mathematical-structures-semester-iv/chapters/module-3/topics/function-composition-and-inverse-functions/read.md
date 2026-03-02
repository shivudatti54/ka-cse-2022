Of course. Here is comprehensive educational content on Function Composition and Inverse Functions, tailored for  Engineering students.

# Function Composition and Inverse Functions

## Introduction

In Discrete Mathematical Structures, functions are fundamental tools for modeling relationships between sets, especially in computer science for tasks like hashing, algorithm analysis, and state machine design. Building upon the basic definition of a function, this module explores how to combine functions through **composition** and how to reverse their effect through **inverse functions**. These concepts are crucial for understanding complex transformations and solving a wide range of computational problems.

## Core Concepts

### 1. Function Composition

Function composition is the process of applying one function to the results of another. It creates a new, combined function from two existing functions.

**Definition:** Let `f: A → B` and `g: B → C` be two functions. The composition of `g` with `f`, denoted as `g ∘ f` (read "g of f" or "g circle f"), is a function from `A` to `C` defined by:
`(g ∘ f)(x) = g(f(x))` for all `x` in `A`.

![Function Composition Diagram](https://via.placeholder.com/350x150?text=A+-f+->+B+-g+->+C)

**Key Requirements:**
*   The **codomain** of the first function (`f`) must be a **subset** of the **domain** of the second function (`g`). In other words, `f`'s output must be a valid input for `g`.
*   The order of application is **vital**. `g ∘ f` means `f` is applied first, then `g`. The composition `f ∘ g` is often a different function or may not even be defined.

**Example 1:**
Let `f: ℝ → ℝ` be defined by `f(x) = x + 2`.
Let `g: ℝ → ℝ` be defined by `g(x) = 3x`.

Find `(g ∘ f)(x)` and `(f ∘ g)(x)`.

**Solution:**
*   `(g ∘ f)(x) = g(f(x)) = g(x + 2) = 3(x + 2) = 3x + 6`
*   `(f ∘ g)(x) = f(g(x)) = f(3x) = (3x) + 2 = 3x + 2`

Clearly, `g ∘ f ≠ f ∘ g`, demonstrating that composition is **not commutative**.

### 2. Inverse Functions

An inverse function essentially "undoes" the operation of the original function. For a function to have an inverse, each input must map to a *unique* output, and each output must come from a *unique* input. This leads to the requirement that the function must be **bijective** (both one-to-one and onto).

**Definition:** Let `f: A → B` be a bijective function. The inverse function of `f`, denoted `f⁻¹: B → A`, is defined such that:
`f⁻¹(y) = x` if and only if `f(x) = y`.

This leads to the fundamental properties:
1.  `f⁻¹(f(x)) = x` for every `x` in `A`.  (Applying `f` and then its inverse returns the original input).
2.  `f(f⁻¹(y)) = y` for every `y` in `B`. (Applying the inverse and then `f` returns the original input).

**Finding the Inverse of a Function:**
For a function `f(x)` defined by a formula, the inverse can often be found algebraically:
1.  Replace `f(x)` with `y`.
2.  Solve the equation for `x` in terms of `y`.
3.  Swap the variables `x` and `y` (to conform to the notation `f⁻¹(x)`).
4.  The resulting expression is `y = f⁻¹(x)`.

**Example 2:**
Find the inverse of the bijective function `f: ℝ → ℝ` defined by `f(x) = 4x - 7`.

**Solution:**
1.  `y = 4x - 7`
2.  Solve for `x`: `y + 7 = 4x` --> `x = (y + 7)/4`
3.  Swap `x` and `y`: `y = (x + 7)/4`
4.  Therefore, `f⁻¹(x) = (x + 7)/4`

**Verification:**
*   `f⁻¹(f(x)) = f⁻¹(4x - 7) = ((4x - 7) + 7)/4 = (4x)/4 = x` ✅
*   `f(f⁻¹(x)) = f((x + 7)/4) = 4 * ((x + 7)/4) - 7 = (x + 7) - 7 = x` ✅

## Key Points & Summary

| Concept | Definition | Key Requirement | Notation & Example |
| :--- | :--- | :--- | :--- |
| **Composition** | Combining two functions: the output of the first is the input of the second. | `Codomain(f) ⊆ Domain(g)` | `(g ∘ f)(x) = g(f(x))` <br> e.g., `f(x)=x+2`, `g(x)=3x` → `(g ∘ f)(x)=3x+6` |
| **Inverse Function** | A function that reverses the mapping of the original function. | `f` must be **bijective** (one-to-one and onto). | `f⁻¹(y)=x` iff `f(x)=y` <br> e.g., `f(x)=4x-7` → `f⁻¹(x)=(x+7)/4` |

*   **Composition is Associative:** For functions `f, g, h`, `(h ∘ g) ∘ f = h ∘ (g ∘ f)`, provided the compositions are defined.
*   **Identity Function:** The function `I: A → A` defined by `I(x) = x` acts as the identity element for composition. For any function `f: A → B`, `f ∘ I_A = f` and `I_B ∘ f = f`.
*   **Relationship:** For bijective functions `f` and `g`, the inverse of their composition is `(g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹`. Notice the order reverses.

Understanding these operations is essential for later topics like permutations, cryptographic algorithms, and defining complex relations in software systems.