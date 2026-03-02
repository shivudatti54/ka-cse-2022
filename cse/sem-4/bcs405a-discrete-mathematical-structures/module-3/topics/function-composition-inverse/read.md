# Function Composition and Inverse Functions

## Table of Contents

- [Function Composition and Inverse Functions](#function-composition-and-inverse-functions)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Functions - Basic Definitions](#1-functions---basic-definitions)
  - [2. Function Composition](#2-function-composition)
  - [3. Inverse Functions](#3-inverse-functions)
  - [4. Permutations as Functions](#4-permutations-as-functions)
- [Examples](#examples)
  - [Example 1: Computing Function Composition](#example-1-computing-function-composition)
  - [Example 2: Verifying Inverse Functions](#example-2-verifying-inverse-functions)
  - [Example 3: Inverse of Composite Function](#example-3-inverse-of-composite-function)
- [Exam Tips](#exam-tips)

## Introduction

Function composition and inverse functions are fundamental concepts in discrete mathematics that form the backbone of many computational processes and algorithmic thinking. In the context of the university's Discrete Mathematical Structures course, understanding these concepts is essential for solving problems related to algorithmic complexity, recursive definitions, and cryptographic applications.

A function maps elements from one set (domain) to another set (codomain), establishing a precise relationship between input and output values. When we combine two or more functions, we create composite functions that perform sequential transformations. Inverse functions, on the other hand, allow us to "undo" the operation performed by a function, restoring the original input from the output. These concepts find extensive applications in computer science, particularly in algorithm design, data structures, and cryptography.

This module explores the theory and practical applications of function composition and inverse functions, providing you with the mathematical foundation necessary for advanced studies in computer science and engineering.

## Key Concepts

### 1. Functions - Basic Definitions

A function f from set A (domain) to set B (codomain) is denoted as f: A → B. For every element a ∈ A, there exists exactly one element b ∈ B such that f(a) = b. The set of all output values {f(a) : a ∈ A} is called the range or image of f.

**Types of Functions:**

- **Injective (One-to-One) Function:** A function f: A → B is injective if f(a₁) = f(a₂) implies a₁ = a₂ for all a₁, a₂ ∈ A. In other words, distinct inputs always produce distinct outputs.
- **Surjective (Onto) Function:** A function f: A → B is surjective if for every b ∈ B, there exists at least one a ∈ A such that f(a) = b. The range equals the codomain.
- **Bijective Function:** A function that is both injective and surjective. Bijective functions have inverses.

### 2. Function Composition

Given two functions f: A → B and g: B → C, the composition of g with f, denoted as g ∘ f, is a function from A to C defined by (g ∘ f)(a) = g(f(a)) for all a ∈ A.

**Key Properties of Function Composition:**

- **Associativity:** For functions f: A → B, g: B → C, and h: C → D, we have h ∘ (g ∘ f) = (h ∘ g) ∘ f. Composition is always associative.

- **Identity Function:** For any function f: A → B, there exists an identity function Iₐ: A → A such that Iₐ ∘ f = f ∘ Iₐ = f.

- **Composition of Injective Functions:** If f and g are both injective, then g ∘ f is also injective.

- **Composition of Surjective Functions:** If f and g are both surjective, then g ∘ f is also surjective.

- **Composition of Bijective Functions:** If f and g are both bijective, then g ∘ f is also bijective.

### 3. Inverse Functions

Let f: A → B be a bijective function. The inverse function f⁻¹: B → A is defined such that f⁻¹(b) = a if and only if f(a) = b. The inverse function "undoes" what f does.

**Fundamental Property:** For a bijective function f: A → B, f⁻¹ ∘ f = Iₐ and f ∘ f⁻¹ = Iᵦ, where Iₐ and Iᵦ are identity functions on A and B respectively.

**Conditions for Inverse Existence:**

- A function must be bijective (both one-to-one and onto) to have an inverse.
- If f is injective but not surjective, we can define an inverse on the range of f.

**Inverse of Composition:** (g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹, provided f and g are invertible.

### 4. Permutations as Functions

A permutation is a bijective function from a finite set to itself. The set of all permutations of n elements forms the symmetric group Sₙ under composition. Permutations are particularly important in:

- Cryptography (substitution ciphers)
- Sorting algorithms
- Combinatorics

## Examples

### Example 1: Computing Function Composition

Let f: ℝ → ℝ be defined by f(x) = 2x + 3, and g: ℝ → ℝ be defined by g(x) = x². Find (g ∘ f)(x) and (f ∘ g)(x).

**Solution:**

For (g ∘ f)(x):

- First apply f: f(x) = 2x + 3
- Then apply g to the result: g(f(x)) = g(2x + 3) = (2x + 3)² = 4x² + 12x + 9
- Therefore, (g ∘ f)(x) = 4x² + 12x + 9

For (f ∘ g)(x):

- First apply g: g(x) = x²
- Then apply f to the result: f(g(x)) = f(x²) = 2(x²) + 3 = 2x² + 3
- Therefore, (f ∘ g)(x) = 2x² + 3

**Key Observation:** Note that (g ∘ f)(x) ≠ (f ∘ g)(x) in general. Function composition is not commutative.

### Example 2: Verifying Inverse Functions

Let f: ℝ → ℝ be defined by f(x) = 3x - 5. Show that f is bijective and find its inverse.

**Solution:**

**Step 1: Prove injectivity**
Assume f(x₁) = f(x₂)
⇒ 3x₁ - 5 = 3x₂ - 5
⇒ 3x₁ = 3x₂
⇒ x₁ = x₂
Therefore, f is injective.

**Step 2: Prove surjectivity**
For any y ∈ ℝ, we need to find x ∈ ℝ such that f(x) = y
3x - 5 = y
3x = y + 5
x = (y + 5)/3
Since (y + 5)/3 ∈ ℝ for every y ∈ ℝ, f is surjective.

Since f is both injective and surjective, it is bijective.

**Step 3: Find the inverse**
Set y = f(x) = 3x - 5
Solve for x: x = (y + 5)/3
Therefore, f⁻¹(y) = (y + 5)/3
Replacing y with x: f⁻¹(x) = (x + 5)/3

**Verification:**

- (f ∘ f⁻¹)(x) = f(f⁻¹(x)) = f((x + 5)/3) = 3((x + 5)/3) - 5 = x + 5 - 5 = x ✓
- (f⁻¹ ∘ f)(x) = f⁻¹(f(x)) = f⁻¹(3x - 5) = ((3x - 5) + 5)/3 = 3x/3 = x ✓

### Example 3: Inverse of Composite Function

Let f: {1,2,3} → {1,2,3} be defined by f(1)=2, f(2)=3, f(3)=1.
Let g: {1,2,3} → {1,2,3} be defined by g(1)=3, g(2)=1, g(3)=2.
Find (g ∘ f)⁻¹.

**Solution:**

**Step 1: Find g ∘ f**

- (g ∘ f)(1) = g(f(1)) = g(2) = 1
- (g ∘ f)(2) = g(f(2)) = g(3) = 2
- (g ∘ f)(3) = g(f(3)) = g(1) = 3

So g ∘ f is the identity function: (g ∘ f)(x) = x for all x.

**Step 2: Find inverse**
Since g ∘ f is the identity function, its inverse is itself:
(g ∘ f)⁻¹(1) = 1, (g ∘ f)⁻¹(2) = 2, (g ∘ f)⁻¹(3) = 3

**Alternative using formula:** (g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹
First find f⁻¹: f⁻¹(1)=3, f⁻¹(2)=1, f⁻¹(3)=2
Find g⁻¹: g⁻¹(1)=2, g⁻¹(2)=3, g⁻¹(3)=1
Then (f⁻¹ ∘ g⁻¹)(1) = f⁻¹(g⁻¹(1)) = f⁻¹(2) = 1
(f⁻¹ ∘ g⁻¹)(2) = f⁻¹(g⁻¹(2)) = f⁻¹(3) = 2
(f⁻¹ ∘ g⁻¹)(3) = f⁻¹(g⁻¹(3)) = f⁻¹(1) = 3

Both methods give the same result.

## Exam Tips

1. **Remember the definition of injectivity:** When proving a function is injective, always start with f(x₁) = f(x₂) and show that this implies x₁ = x₂. This is a common university exam question.

2. **Inverse exists only for bijective functions:** Before attempting to find an inverse, first verify that the function is both one-to-one and onto. Many students lose marks by assuming all functions have inverses.

3. **Composition is not commutative:** Always remember that f ∘ g ≠ g ∘ f in general. This is frequently tested in exams.

4. **Use the horizontal line test for injectivity:** A function is injective if and only if no horizontal line intersects its graph more than once.

5. **Inverse of composition formula:** Remember (g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹. The order reverses when taking inverses of composite functions.

6. **Verify your inverse:** Always check that f(f⁻¹(x)) = x and f⁻¹(f(x)) = x. This verification is often expected in exam solutions.

7. **Domain and codomain matter:** When describing functions, always specify the domain and codomain. A function with different codomains can have different properties (surjective vs non-surjective).

8. **Practice with discrete sets:** university exams often include functions on finite sets (represented as mapping tables). Be comfortable working with such representations.
