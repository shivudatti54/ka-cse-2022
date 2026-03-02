# Onto Functions (Surjective Functions)

## Table of Contents

- [Onto Functions (Surjective Functions)](#onto-functions-surjective-functions)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Function Terminology](#basic-function-terminology)
  - [Definition of Onto (Surjective) Functions](#definition-of-onto-surjective-functions)
  - [Visual Representation](#visual-representation)
  - [Onto vs One-to-One Functions](#onto-vs-one-to-one-functions)
  - [Examples of Onto Functions](#examples-of-onto-functions)
  - [Number of Onto Functions Between Finite Sets](#number-of-onto-functions-between-finite-sets)
  - [Composition and Onto Functions](#composition-and-onto-functions)
- [Examples](#examples)
  - [Worked Example 1: Proving a Function is Onto](#worked-example-1-proving-a-function-is-onto)
  - [Worked Example 2: Determining Function Type](#worked-example-2-determining-function-type)
  - [Worked Example 3: Creating Onto Functions](#worked-example-3-creating-onto-functions)
- [Exam Tips](#exam-tips)

## Introduction

In discrete mathematics, functions form a fundamental concept that establishes relationships between two sets. Among the various types of functions, **onto functions** (also known as **surjective functions**) play a crucial role in understanding mappings where every element in the codomain has at least one preimage in the domain. This concept is essential for computer science students as it underpins many algorithmic and theoretical foundations, including database theory, function composition, and cryptographic applications.

The study of onto functions extends our understanding of how elements from one set can be mapped to elements in another set comprehensively. Unlike one-to-one functions that ensure uniqueness in the mapping, onto functions guarantee completeness—every element in the target set is "covered" by some element from the source set. This property makes onto functions particularly valuable in scenarios where we need to ensure that all possible outputs are achievable through our mapping.

In this module, we will explore the formal definition of onto functions, examine their properties, work through detailed examples, and understand how they relate to other types of functions. Mastery of this topic is essential for success in discrete mathematics and provides a foundation for more advanced topics in computer science such as combinatorics, algorithm analysis, and formal language theory.

## Key Concepts

### Basic Function Terminology

Before diving into onto functions, let us establish the fundamental terminology:

- **Function (Mapping)**: A function f from set A to set B is a rule that assigns to each element in A exactly one element in B. We write f: A → B.
- **Domain**: The set A is called the domain of the function.
- **Codomain**: The set B is called the codomain (or target set) of the function.
- **Range (Image)**: The set of all actual outputs {f(a) : a ∈ A} is called the range or image of f. The range is always a subset of the codomain.

### Definition of Onto (Surjective) Functions

A function f: A → B is called **onto** (or **surjective**) if and only if for every element b in the codomain B, there exists at least one element a in the domain A such that f(a) = b.

**Formal Definition**: f: A → B is onto iff ∀b ∈ B, ∃a ∈ A such that f(a) = b.

In other words, the range of an onto function equals its codomain: Range(f) = B.

### Visual Representation

Consider the function f: {1, 2, 3} → {a, b, c} defined by f(1) = a, f(2) = b, f(3) = c. This function is onto because every element in the codomain {a, b, c} has at least one preimage in the domain.

Now consider g: {1, 2, 3} → {a, b, c} defined by g(1) = a, g(2) = a, g(3) = b. This function is NOT onto because c in the codomain has no preimage.

### Onto vs One-to-One Functions

Understanding the distinction between onto and one-to-one (injective) functions is crucial:

- **One-to-one (Injective)**: Different inputs produce different outputs. If f(a₁) = f(a₂), then a₁ = a₂.
- **Onto (Surjective)**: Every element in the codomain is an output for some input.

A function can be:

- One-to-one but not onto
- Onto but not one-to-one
- Both (bijective)
- Neither

### Examples of Onto Functions

**Example 1**: Let f: ℤ → ℤ be defined by f(x) = x + 1. Is this onto?

_Solution_: For any integer y in the codomain, we need to find x such that f(x) = y. Solving x + 1 = y gives x = y - 1, which is always an integer. Therefore, f is onto (and also one-to-one, making it bijective).

**Example 2**: Let f: ℝ → ℝ be defined by f(x) = x³. Is this onto?

_Solution_: For any real number y, we can take x = ∛y (cube root of y), which is always a real number. Since f(∛y) = (∛y)³ = y, every real number is in the range. Thus, f is onto (and also one-to-one).

**Example 3**: Let f: ℝ → ℝ be defined by f(x) = x². Is this onto?

_Solution_: No, this function is not onto because negative numbers in the codomain have no preimage. For example, there is no real x such that x² = -4. The range is [0, ∞), not all of ℝ.

### Number of Onto Functions Between Finite Sets

A common problem is determining how many onto functions exist from a set of size m to a set of size n (where m ≥ n).

**Formula**: The number of onto functions from an n-element set to an m-element set is:
$$m! \cdot S(n, m)$$

where S(n, m) denotes the Stirling numbers of the second kind (number of ways to partition n objects into m non-empty subsets).

Alternatively, using the inclusion-exclusion principle:
$$\text{Number of onto functions} = m^n - \binom{m}{1}(m-1)^n + \binom{m}{2}(m-2)^n - \cdots + (-1)^{m-1}\binom{m}{m-1}(1)^n$$

**Example**: How many onto functions are there from a set with 3 elements to a set with 2 elements?

_Solution_: Using the formula with n = 3 (domain size) and m = 2 (codomain size):
$$= 2^3 - \binom{2}{1} \cdot 1^3 = 8 - 2 = 6$$

Let the domain be {a, b, c} and codomain be {x, y}. The 6 onto functions are:

- f(a)=x, f(b)=x, f(c)=y
- f(a)=x, f(b)=y, f(c)=y
- f(a)=y, f(b)=x, f(c)=x
- f(a)=y, f(b)=y, f(c)=x
- f(a)=x, f(b)=y, f(c)=x
- f(a)=y, f(b)=x, f(c)=y

### Composition and Onto Functions

**Theorem**: If f: A → B is onto and g: B → C is onto, then g ∘ f: A → C is onto.

_Proof_: Let c be any element in C. Since g is onto, there exists b ∈ B such that g(b) = c. Since f is onto, there exists a ∈ A such that f(a) = b. Therefore, (g ∘ f)(a) = g(f(a)) = g(b) = c. Hence, every element in C has a preimage in A, so g ∘ f is onto.

**Note**: If g ∘ f is onto, it does not necessarily mean that f is onto.

## Examples

### Worked Example 1: Proving a Function is Onto

**Problem**: Let f: ℤ → ℤ be defined by f(x) = 5x - 3. Prove that f is onto.

**Solution**:

To prove f is onto, we need to show that for every integer y in the codomain, there exists an integer x in the domain such that f(x) = y.

Let y be an arbitrary integer. We need to find x such that:
5x - 3 = y
5x = y + 3
x = (y + 3)/5

For x to be an integer, y + 3 must be divisible by 5. But not every integer y satisfies this condition. Therefore, f is NOT onto.

For example, if y = 1, then x = (1 + 3)/5 = 4/5, which is not an integer. Thus, the function is not surjective over ℤ.

If we change the codomain to ℚ (rational numbers), then f would be onto because for any rational y, we can find x = (y + 3)/5, which is also rational.

### Worked Example 2: Determining Function Type

**Problem**: Consider the function f: {1, 2, 3, 4} → {a, b, c} defined by:
f(1) = a, f(2) = b, f(3) = c, f(4) = c

Determine if f is onto, one-to-one, both, or neither.

**Solution**:

**Onto check**: Check if every element in codomain {a, b, c} has a preimage.

- a: preimage is 1 ✓
- b: preimage is 2 ✓
- c: preimages are 3 and 4 ✓

All elements have at least one preimage, so f is ONTO.

**One-to-one check**: Check if different inputs produce different outputs.

- f(1) = a, f(2) = b, f(3) = c, f(4) = c
- Here, f(3) = f(4) = c, but 3 ≠ 4

Since two different domain elements map to the same codomain element, f is NOT one-to-one.

Therefore, f is onto but not one-to-one.

### Worked Example 3: Creating Onto Functions

**Problem**: Let A = {1, 2, 3, 4} and B = {w, x, y}. Find all onto functions from A to B.

**Solution**:

We need functions where every element of B appears as an output at least once. Since |A| = 4 and |B| = 3, by the pigeonhole principle, at least one element in B must be the image of more than one element in A.

We can systematically list these:

Type 1: One element appears 3 times, one appears once, one appears 0 times → NOT ONTO (all must appear)

Type 2: One element appears 2 times, another appears 2 times, third appears 0 times → NOT ONTO

Type 3: One element appears 2 times, the other two appear once each → ONTO

- Choose which element appears twice: 3 ways
- Choose which two domain elements map to this repeated element: C(4,2) = 6 ways
- Arrange the remaining 2 domain elements to the remaining 2 codomain elements: 2! = 2 ways

Total: 3 × 6 × 2 = 36 onto functions

Type 4: All three elements appear once each, and one element appears twice (same as Type 3)

Actually, the correct count using our formula: mⁿ - C(m,1)(m-1)ⁿ = 3⁴ - C(3,1)(2)⁴ = 81 - 3(16) = 81 - 48 = 33

Let us verify: Using the inclusion-exclusion approach:

- Total functions: 3⁴ = 81
- Subtract those missing at least one codomain element: C(3,1) × 2⁴ = 3 × 16 = 48
- Add back those missing at least two codomain elements: C(3,2) × 1⁴ = 3 × 1 = 3

81 - 48 + 3 = 36

So there are 36 onto functions from A to B.

## Exam Tips

1. **Memorize the definition**: f: A → B is onto iff ∀b ∈ B, ∃a ∈ A such that f(a) = b. This is the most fundamental concept.

2. **Range equals codomain**: For an onto function, Range(f) = B. Always check if the range covers the entire codomain.

3. **Use counterexamples**: To prove a function is NOT onto, find ONE element in the codomain with no preimage.

4. **Pigeonhole principle**: If |A| < |B|, an onto function is impossible. This is a quick check.

5. **Bijection requires both properties**: Remember that a function is bijective if and only if it is both one-to-one AND onto.

6. **Composition rules**: If f is onto and g is onto, then g ∘ f is onto. But g ∘ f being onto does NOT guarantee f is onto.

7. **Infinite sets**: Be careful with infinite domains/codomains. Use algebraic solving (like x = y - 1) to prove onto property.

8. **Notation awareness**: "Onto" and "surjective" mean the same thing. Some textbooks may use either term.

9. **Stirling numbers**: For counting onto functions between finite sets, remember the formula m! × S(n,m) or the inclusion-exclusion approach.

10. **Real-world interpretation**: Think of onto as "every possible output is achieved" — this helps in exam questions asking you to identify or create onto functions.
