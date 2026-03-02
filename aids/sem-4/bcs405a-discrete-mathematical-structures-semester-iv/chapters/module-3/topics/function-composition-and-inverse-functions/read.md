Of course. Here is a comprehensive educational guide on Function Composition and Inverse Functions, tailored for  engineering students.

# Module 3: Relations and Functions
## Function Composition and Inverse Functions

### 1. Introduction

In Discrete Mathematical Structures, functions are fundamental tools for modeling relationships between sets, which is crucial in computer science for areas like algorithm design, database theory, and automata. Simply knowing individual functions is often not enough. We need to combine them to create more complex relationships and, crucially, we need to be able to "reverse" their effects. This brings us to two core operations: **function composition** and finding **inverse functions**.

---

### 2. Core Concepts

#### Function Composition

Function composition is the process of applying one function to the results of another. Think of it like a factory assembly line, where the output of one machine becomes the input for the next.

**Definition:**
Let `f: A → B` and `g: B → C` be two functions. The composition of `g` and `f`, denoted by `g ∘ f` (read as "g composed with f" or "g of f"), is a function from `A` to `C` defined as:
`(g ∘ f)(x) = g(f(x))` for all `x` in `A`.

**Key Points:**
*   **Order Matters:** Composition is not commutative. `g ∘ f` is **not** the same as `f ∘ g`. In fact, `f ∘ g` may not even be defined unless the codomain of `g` is a subset of the domain of `f`.
*   **Domain & Codomain:** For `g ∘ f` to be defined, the codomain of `f` must be a subset of (or equal to) the domain of `g`.

**Example 1:**
Let `f: ℝ → ℝ` be defined by `f(x) = x + 1`
Let `g: ℝ → ℝ` be defined by `g(x) = x²`

Find `(g ∘ f)(x)` and `(f ∘ g)(x)`.

*   `(g ∘ f)(x) = g(f(x)) = g(x + 1) = (x + 1)²`
*   `(f ∘ g)(x) = f(g(x)) = f(x²) = x² + 1`

Clearly, `(x + 1)² ≠ x² + 1`, proving `g ∘ f ≠ f ∘ g`.

#### Inverse Functions

An inverse function essentially "undoes" the action of the original function. If a function `f` maps an element `a` to an element `b`, its inverse `f⁻¹` maps `b` back to `a`.

**Definition:**
A function `f: A → B` is **invertible** if there exists a function `f⁻¹: B → A` such that:
1.  `f⁻¹ ∘ f = I_A` (the identity function on A, meaning `f⁻¹(f(x)) = x` for all `x ∈ A`)
2.  `f ∘ f⁻¹ = I_B` (the identity function on B, meaning `f(f⁻¹(y)) = y` for all `y ∈ B`)

**Condition for Invertibility:**
A function is invertible **if and only if it is bijective** (both one-to-one/injective and onto/surjective).

*   **One-to-One (Injective):** Ensures that the inverse will be a function (every input has only one output).
*   **Onto (Surjective):** Ensures the inverse is defined for every element in the codomain.

**How to Find the Inverse:**
If a function `y = f(x)` is bijective, its inverse can be found by:
1.  Set `y = f(x)`.
2.  Solve this equation for `x` in terms of `y`.
3.  Swap `x` and `y`. The resulting `y` is `f⁻¹(x)`.

**Example 2:**
Show that `f: ℝ → ℝ` defined by `f(x) = 2x + 3` is invertible and find its inverse.

1.  **Check if bijective:**
    *   *One-to-one?* Assume `f(a) = f(b)`. Then `2a+3 = 2b+3 => 2a=2b => a=b`. ∴ It is injective.
    *   *Onto?* For any `y ∈ ℝ`, we can find `x = (y-3)/2` such that `f(x)=y`. ∴ It is surjective.
    Since it's bijective, it is invertible.

2.  **Find the inverse:**
    *   Set `y = 2x + 3`
    *   Solve for `x`: `y - 3 = 2x => x = (y - 3)/2`
    *   Swap `x` and `y`: `y = (x - 3)/2`
    *   Therefore, the inverse function is **`f⁻¹(x) = (x - 3)/2`**.

**Verification:**
*   `f⁻¹(f(x)) = f⁻¹(2x+3) = ((2x+3) - 3)/2 = (2x)/2 = x` ✔️
*   `f(f⁻¹(x)) = f((x-3)/2) = 2*((x-3)/2) + 3 = (x-3) + 3 = x` ✔️

---

### 3. Key Points & Summary

| Concept | Definition | Key Condition | Notation & Formula |
| :--- | :--- | :--- | :--- |
| **Composition** | Applying one function to the result of another. | `codomain(f)` ⊆ `domain(g)` | `(g ∘ f)(x) = g(f(x))` |
| **Inverse Function** | A function that reverses the mapping of `f`. | `f` must be **bijective** (one-to-one and onto). | `f⁻¹(f(x)) = x` and `f(f⁻¹(y)) = y` |

*   **Composition is Associative:** `(h ∘ g) ∘ f = h ∘ (g ∘ f)`, provided the compositions are defined.
*   The inverse of a composition follows the "socks-and-shoes" property: `(g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹`. You must undo the last function first.
*   These concepts are vital in cryptography (encryption/decryption functions), computer graphics (coordinate transformations), and software engineering (function chaining).