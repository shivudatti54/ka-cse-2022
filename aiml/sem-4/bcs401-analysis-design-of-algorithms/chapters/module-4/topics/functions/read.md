# Functions and Types

## Introduction to Functions

In discrete mathematics, a **function** is a fundamental concept that describes a relationship between two sets where each element of the first set (called the domain) is associated with exactly one element of the second set (called the codomain). Functions are crucial in computer science for modeling relationships between data, defining algorithms, and structuring programs.

Formally, a function `f` from set `A` to set `B` (denoted `f: A → B`) is a rule that assigns to each element `a ∈ A` exactly one element `b ∈ B`. We write `f(a) = b` to indicate that `b` is the value of the function at `a`, or the image of `a` under `f`.

## Basic Terminology

- **Domain**: The set of all possible inputs for the function (set A)
- **Codomain**: The set of all possible outputs (set B)
- **Range/Image**: The set of all actual outputs produced by the function
- **Pre-image**: For any `b ∈ B`, the set of all `a ∈ A` such that `f(a) = b`

```
Domain (A)    Function f     Codomain (B)
   a₁  ------------------->     b₁
   a₂  ------------------->     b₂
   a₃  ------------------->     b₃
   a₄  ------------------->     b₄
```

## Types of Functions

### 1. Injective Functions (One-to-One)

A function `f: A → B` is **injective** (or one-to-one) if distinct elements in the domain map to distinct elements in the codomain. That is, for any `a₁, a₂ ∈ A`, if `a₁ ≠ a₂`, then `f(a₁) ≠ f(a₂)`.

**Example**: `f(x) = 2x` from ℝ to ℝ is injective because if `x₁ ≠ x₂`, then `2x₁ ≠ 2x₂`.

```
Injective Function:
A: {1, 2, 3}    →    B: {a, b, c, d}
1 → a
2 → b
3 → c
```

### 2. Surjective Functions (Onto)

A function `f: A → B` is **surjective** (or onto) if every element in the codomain has at least one pre-image in the domain. That is, for every `b ∈ B`, there exists some `a ∈ A` such that `f(a) = b`.

**Example**: `f(x) = x²` from ℝ to ℝ⁺ (non-negative reals) is surjective because every non-negative number has a real square root.

```
Surjective Function:
A: {1, 2, 3, 4}    →    B: {a, b, c}
1 → a
2 → b
3 → c
4 → c
```

### 3. Bijective Functions (One-to-One Correspondence)

A function `f: A → B` is **bijective** if it is both injective and surjective. This means there's a perfect pairing between elements of the domain and codomain.

**Example**: `f(x) = x + 1` from ℤ to ℤ is bijective.

```
Bijective Function:
A: {1, 2, 3}    →    B: {a, b, c}
1 → a
2 → b
3 → c
```

### 4. Constant Functions

A function `f: A → B` is **constant** if there exists some `c ∈ B` such that `f(a) = c` for all `a ∈ A`.

**Example**: `f(x) = 5` for all `x ∈ ℝ`.

### 5. Identity Functions

The **identity function** on a set `A` is the function `idₐ: A → A` defined by `idₐ(a) = a` for all `a ∈ A`.

## Function Composition

Given two functions `f: A → B` and `g: B → C`, the **composition** of `g` with `f` is the function `g∘f: A → C` defined by `(g∘f)(a) = g(f(a))` for all `a ∈ A`.

**Example**: If `f(x) = x²` and `g(x) = x + 1`, then `(g∘f)(x) = x² + 1`.

```
Composition Diagram:
A → f → B → g → C
```

## Special Functions in Computer Science

### 1. Floor and Ceiling Functions

- **Floor function**: `⌊x⌋` = greatest integer ≤ x
- **Ceiling function**: `⌈x⌉` = smallest integer ≥ x

**Examples**: `⌊3.7⌋ = 3`, `⌈3.2⌉ = 4`, `⌊-2.3⌋ = -3`

### 2. Boolean Functions

Functions where the domain and codomain are Boolean values (true/false or 1/0). Essential in logic circuits and programming.

### 3. Hash Functions

Functions that map data of arbitrary size to fixed-size values. Used in data structures like hash tables.

## Inverse Functions

If `f: A → B` is bijective, then there exists an **inverse function** `f⁻¹: B → A` such that:

- `f⁻¹(f(a)) = a` for all `a ∈ A`
- `f(f⁻¹(b)) = b` for all `b ∈ B`

**Example**: If `f(x) = 2x + 3`, then `f⁻¹(x) = (x - 3)/2`.

## Comparing Function Types

| Function Type | Injective? | Surjective? | Bijective? | Has Inverse?            |
| ------------- | ---------- | ----------- | ---------- | ----------------------- |
| Injective     | Yes        | Maybe       | Maybe      | Only if also surjective |
| Surjective    | Maybe      | Yes         | Maybe      | Only if also injective  |
| Bijective     | Yes        | Yes         | Yes        | Yes                     |
| Constant      | No\*       | Maybe       | No         | No                      |
| Identity      | Yes        | Yes         | Yes        | Yes                     |

\*Constant functions are injective only if the domain has exactly one element.

## Function Cardinality

The number of possible functions from set A to set B is `|B|^|A|`.

**Example**: If A has 3 elements and B has 2 elements, there are 2³ = 8 possible functions.

## Exam Tips

1. **Identify function types**: Always check both injectivity and surjectivity separately when determining if a function is bijective.
2. **Composition order**: Remember that `(g∘f)(x) = g(f(x))` - the function on the right is applied first.
3. **Inverse existence**: Only bijective functions have inverses. If asked to find an inverse, first verify the function is bijective.
4. **Floor/ceiling**: Remember that floor always rounds down, ceiling always rounds up, even for negative numbers.
5. **Function notation**: Use proper notation: `f: A → B` indicates domain A and codomain B.
6. **Practice**: Work through many examples with different domains (finite sets, integers, real numbers) to build intuition.
