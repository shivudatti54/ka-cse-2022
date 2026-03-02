# Functions - Plain and One-to-One

## Table of Contents

- [Functions - Plain and One-to-One](#functions---plain-and-one-to-one)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Definition of a Function](#1-definition-of-a-function)
  - [2. Domain, Codomain, and Range](#2-domain-codomain-and-range)
  - [3. One-to-One Functions (Injective Functions)](#3-one-to-one-functions-injective-functions)
  - [4. Methods to Verify One-to-One](#4-methods-to-verify-one-to-one)
  - [5. Onto Functions (Surjective Functions)](#5-onto-functions-surjective-functions)
  - [6. Bijective Functions](#6-bijective-functions)
  - [7. Composition of Functions](#7-composition-of-functions)
  - [8. Inverse Functions](#8-inverse-functions)
- [Examples](#examples)
  - [Example 1: Proving a Function is One-to-One](#example-1-proving-a-function-is-one-to-one)
  - [Example 2: Proving a Function is NOT One-to-One](#example-2-proving-a-function-is-not-one-to-one)
  - [Example 3: Composition and One-to-One](#example-3-composition-and-one-to-one)
- [Exam Tips](#exam-tips)

## Introduction

Functions form one of the most fundamental concepts in discrete mathematics and serve as the building block for understanding more complex mathematical structures. A function is a special type of relation that associates each element from one set (called the domain) with exactly one element in another set (called the codomain). This concept is pervasive in computer science, particularly in algorithm analysis, database systems, programming language theory, and cryptography.

In this module, we focus on understanding the nature of functions, with special emphasis on **one-to-one functions** (also called injective functions or "plain" functions in some textbooks). The study of one-to-one functions is crucial because they guarantee that no two different input values produce the same output, a property that ensures data integrity and enables the construction of inverse functions. Understanding when a function is one-to-one, how to verify this property, and how one-to-one functions behave under composition are essential skills for any computer science engineer.

## Key Concepts

### 1. Definition of a Function

A function f from set A (domain) to set B (codomain) is a relation such that every element in A is associated with exactly one element in B. We denote this as f: A → B.

For a relation to be a function, it must satisfy two conditions:

- **Every element in A must have an image**: ∀a ∈ A, ∃b ∈ B such that (a, b) ∈ f
- **Each element in A has exactly one image**: If (a, b₁) ∈ f and (a, b₂) ∈ f, then b₁ = b₂

**Example**: Let f: {1, 2, 3} → {a, b, c} be defined by f(1) = a, f(2) = b, f(3) = c. This is a function.

**Counter-example**: Let g: {1, 2} → {a, b} be defined by g(1) = a and g(1) = b. This is NOT a function because 1 has two images.

### 2. Domain, Codomain, and Range

- **Domain (Dom(f))**: The set of all possible input values (first coordinates of ordered pairs)
- **Codomain**: The set into which all outputs of the function must fall
- **Range (Range(f) or Image)**: The set of all actual outputs; Range(f) = {f(x) : x ∈ Dom(f)}

**Important**: Range ⊆ Codomain. The range is always a subset of the codomain.

### 3. One-to-One Functions (Injective Functions)

A function f: A → B is called **one-to-one** (injective or plain) if different elements in the domain map to different elements in the codomain.

**Formal Definition**: f is one-to-one if ∀a₁, a₂ ∈ A, if f(a₁) = f(a₂), then a₁ = a₂.

**Contrapositive form** (often easier to prove): f is one-to-one if ∀a₁, a₂ ∈ A, if a₁ ≠ a₂, then f(a₁) ≠ f(a₂).

**Key Insight**: No two distinct domain elements produce the same codomain element.

### 4. Methods to Verify One-to-One

**Method 1: Horizontal Line Test**
A function is one-to-one if and only if every horizontal line intersects its graph at most once. This is the visual test.

**Method 2: Algebraic Test**
Assume f(a₁) = f(a₂) and prove that a₁ = a₂.

**Method 3: Counterexample Method**
To show a function is NOT one-to-one, find two distinct elements a₁ ≠ a₂ such that f(a₁) = f(a₂).

### 5. Onto Functions (Surjective Functions)

A function f: A → B is **onto** (surjective) if every element in the codomain has at least one preimage.

**Formal Definition**: f is onto if ∀b ∈ B, ∃a ∈ A such that f(a) = b.

**Range = Codomain** for onto functions.

### 6. Bijective Functions

A function that is both one-to-one AND onto is called **bijective**. Bijective functions have inverses.

### 7. Composition of Functions

If f: A → B and g: B → C, then the composition g∘f: A → C is defined by (g∘f)(a) = g(f(a)).

**Important Theorem**: If f and g are both one-to-one, then g∘f is also one-to-one.

**Proof**: Assume (g∘f)(a₁) = (g∘f)(a₂)
→ g(f(a₁)) = g(f(a₂))
→ Since g is one-to-one, f(a₁) = f(a₂)
→ Since f is one-to-one, a₁ = a₂
→ Therefore, g∘f is one-to-one.

### 8. Inverse Functions

A function f has an inverse f⁻¹ if and only if f is bijective.

The inverse function reverses the mapping: f⁻¹(y) = x if and only if f(x) = y.

**Condition for inverse existence**: f must be one-to-one (injective) to be invertible.

## Examples

### Example 1: Proving a Function is One-to-One

Let f: ℝ → ℝ be defined by f(x) = 3x + 5. Prove that f is one-to-one.

**Solution**:

**Method 1: Algebraic approach**
Assume f(a₁) = f(a₂)
→ 3a₁ + 5 = 3a₂ + 5
→ 3a₁ = 3a₂
→ a₁ = a₂

Therefore, f is one-to-one.

**Method 2: Using the contrapositive**
Assume a₁ ≠ a₂
→ 3a₁ ≠ 3a₂
→ 3a₁ + 5 ≠ 3a₂ + 5
→ f(a₁) ≠ f(a₂)

Since distinct inputs produce distinct outputs, f is one-to-one.

### Example 2: Proving a Function is NOT One-to-One

Let f: ℤ → ℤ be defined by f(x) = x². Prove that f is not one-to-one.

**Solution**:

To show f is not one-to-one, we need to find two distinct elements with the same image.

Let a₁ = 2 and a₂ = -2 (clearly a₁ ≠ a₂)

f(2) = 2² = 4
f(-2) = (-2)² = 4

Since f(2) = f(-2) = 4, but 2 ≠ -2, the function is NOT one-to-one.

This demonstrates that f(x) = x² is not injective over ℤ (or ℝ). However, if we restricted the domain to ℝ⁺ (positive reals), it would be one-to-one.

### Example 3: Composition and One-to-One

Let f: {1, 2, 3} → {a, b, c} be defined by f(1) = a, f(2) = b, f(3) = c.
Let g: {a, b, c} → {1, 2, 3, 4} be defined by g(a) = 1, g(b) = 2, g(c) = 3.

Determine if g∘f is one-to-one.

**Solution**:

First, compute g∘f:
(g∘f)(1) = g(f(1)) = g(a) = 1
(g∘f)(2) = g(f(2)) = g(b) = 2
(g∘f)(3) = g(f(3)) = g(c) = 3

Since f is one-to-one (each element maps to a unique element) and g is also one-to-one (each of a, b, c maps to different values 1, 2, 3), the composition g∘f is one-to-one.

We can verify algebraically:
(g∘f)(1) = 1, (g∘f)(2) = 2, (g∘f)(3) = 3
All outputs are distinct, so g∘f is injective.

## Exam Tips

1. **Remember the formal definition**: For one-to-one functions, always start with "Assume f(a₁) = f(a₂)" and conclude "Therefore, a₁ = a₂."

2. **Know the contrapositive form**: If asked to prove one-to-one, using a₁ ≠ a₂ → f(a₁) ≠ f(a₂) is often cleaner.

3. **Distinguish domain and range**: In university exams, students often lose marks by confusing domain with codomain or range.

4. **One-to-one + Onto = Bijective**: This is a frequently tested concept. Know that bijective functions are the only functions with true inverses.

5. **Composition preserves injectivity**: Remember the theorem—if both f and g are one-to-one, then g∘f is also one-to-one.

6. **Common counterexamples**: f(x) = x² over ℤ is not one-to-one (2 and -2 map to 4). f(x) = sin(x) over ℝ is not one-to-one.

7. **Visual test**: For functions over ℝ, the horizontal line test quickly determines injectivity.

8. **Inverse exists only for bijective functions**: This is crucial—know that one-to-one alone is not sufficient; the function must also be onto for an inverse to exist.

9. **Restricting domain**: When a function is not one-to-one over its entire domain, consider restricting the domain to make it one-to-one.

10. **Notation matters**: Use f: A → B notation correctly and understand all symbols including ∈, ∀, ∃, ∘.
