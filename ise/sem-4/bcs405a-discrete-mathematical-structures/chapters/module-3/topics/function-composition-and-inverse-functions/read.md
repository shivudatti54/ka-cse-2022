# Function Composition and Inverse Functions

=====================================================

## Introduction

---

In the study of discrete mathematical structures, functions play a crucial role in describing relationships between variables. Two fundamental concepts in function theory are function composition and inverse functions. This topic is essential for understanding how functions interact and can be used to solve problems in various fields.

## Definitions

---

### Function Composition

Given two functions `f` and `g`, the **function composition** is defined as `(f ∘ g)(x) = f(g(x))`. This means that the output of function `g` is used as the input for function `f`.

### Inverse Function

A **function** `f` is said to be **invertible** if it has an inverse function `f^(-1)`, denoted as `f^(-1)(x) = y`, such that `f(f^(-1)(x)) = f^(-1)(f(x)) = x`. The inverse function undoes the action of the original function.

## Properties of Function Composition

---

### Associativity

Function composition is associative, meaning that `(f ∘ g) ∘ h = f ∘ (g ∘ h)` for any functions `f`, `g`, and `h`.

### Identity Function

The **identity function** `i(x) = x` is an example of a function that acts as the identity for composition. When composed with any function, it leaves the input unchanged.

### Composition of Inverse Functions

If `f` is invertible, then the composition of `f` with its inverse is the identity function, i.e., `(f ∘ f^(-1))(x) = f(f^(-1)(x)) = x`.

## Examples

---

### Example 1: Function Composition

Let `f(x) = 2x` and `g(x) = x + 1`. Find `(f ∘ g)(x)`.

`(f ∘ g)(x) = f(g(x)) = f(x + 1) = 2(x + 1) = 2x + 2`

### Example 2: Inverse Function

Let `f(x) = x^2`. Find the inverse function `f^(-1)`.

To find the inverse of `f`, we need to solve the equation `y = x^2` for `x`. Taking the square root of both sides, we get `x = ±√y`. Since `f` is a function, we can assume that `x` is always non-negative, so `x = √y`. Therefore, `f^(-1)(y) = √y`.

## Key Concepts

---

- **Function composition**: `(f ∘ g)(x) = f(g(x))`
- **Inverse function**: `f^(-1)(x) = y` such that `f(f^(-1)(x)) = f^(-1)(f(x)) = x`
- **Associativity**: `(f ∘ g) ∘ h = f ∘ (g ∘ h)`
- **Identity function**: `i(x) = x`
- **Composition of inverse functions**: `(f ∘ f^(-1))(x) = x`

## Practice Problems

---

1.  Find `(f ∘ g)(x)` for `f(x) = 2x` and `g(x) = x + 1`.
2.  Find the inverse function `f^(-1)` for `f(x) = x^2`.
3.  Prove that `(f ∘ f^(-1))(x) = x` for any invertible function `f`.

By mastering these concepts and practicing with examples, you will gain a deeper understanding of function composition and inverse functions, which are essential tools for solving problems in discrete mathematical structures.
