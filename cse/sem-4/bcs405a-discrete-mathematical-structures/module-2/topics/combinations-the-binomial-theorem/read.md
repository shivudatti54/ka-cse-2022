# Combinations and the Binomial Theorem

## Table of Contents

- [Combinations and the Binomial Theorem](#combinations-and-the-binomial-theorem)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Combinations](#1-combinations)
  - [2. Binomial Theorem](#2-binomial-theorem)
  - [3. Pascal's Triangle](#3-pascals-triangle)
  - [4. Multinomial Theorem](#4-multinomial-theorem)
- [Examples](#examples)
  - [Example 1: Combination Calculation](#example-1-combination-calculation)
  - [Example 2: Binomial Expansion](#example-2-binomial-expansion)
  - [Example 3: Using Pascal's Identity](#example-3-using-pascals-identity)
- [Exam Tips](#exam-tips)

## Introduction

Combinations and the Binomial Theorem form fundamental concepts in discrete mathematics with extensive applications in computer science, probability theory, and combinatorial analysis. Combinations deal with selecting objects from a set without considering the order of selection, which is crucial in problems involving arrangements, selections, and counting techniques. The Binomial Theorem provides a powerful method for expanding powers of binomials and has deep connections to combinatorial mathematics.

In the context of the university's Discrete Mathematical Structures course, these concepts serve as building blocks for more advanced topics like probability distributions, algorithm analysis, and graph theory. Understanding combinations is essential for solving problems related to password generation, network configurations, and various algorithmic complexity calculations. The Binomial Theorem, with its elegant relationship to Pascal's Triangle, demonstrates the beautiful symmetry in mathematical structures and provides efficient methods for computing coefficients in polynomial expansions.

## Key Concepts

### 1. Combinations

A combination refers to the selection of objects from a set where the order of selection does not matter. The number of ways to choose r objects from a set of n distinct objects is denoted by C(n, r) or nCr, also read as "n choose r."

**Formula:** C(n, r) = n! / (r!(n-r)!)

**Key Properties:**

- C(n, 0) = 1 and C(n, n) = 1
- C(n, r) = C(n, n-r) (symmetry property)
- C(n, r) + C(n, r-1) = C(n+1, r) (Pascal's identity)

**Conditions for using combinations:**

- Order does not matter
- Objects are distinct (without repetition)
- Selection is made from a single set

### 2. Binomial Theorem

The Binomial Theorem provides a formula for expanding any power of a binomial expression (a + b)^n.

**Theorem:** For any non-negative integer n,
(a + b)^n = Σ C(n, r) a^(n-r) b^r, where r ranges from 0 to n

This expands to:
(a + b)^n = C(n, 0)a^n + C(n, 1)a^(n-1)b + C(n, 2)a^(n-2)b^2 + ... + C(n, n)b^n

**The General Term:** The (r+1)th term is given by T(r+1) = C(n, r)a^(n-r)b^r

**Key Properties:**

- There are n+1 terms in the expansion
- The coefficients C(n, 0), C(n, 1), ..., C(n, n) are called binomial coefficients
- The sum of all coefficients in (a + b)^n is 2^n (by setting a = 1, b = 1)
- The alternating sum is 0 (by setting a = 1, b = -1)

### 3. Pascal's Triangle

Pascal's Triangle is a geometric arrangement of binomial coefficients that provides an intuitive way to compute combinations.

**Structure:**

- Row 0: 1
- Row 1: 1 1
- Row 2: 1 2 1
- Row 3: 1 3 3 1
- Row 4: 1 4 6 4 1
- Row n: C(n, 0), C(n, 1), ..., C(n, n)

**Properties:**

- Each entry is the sum of the two entries directly above it
- The rth element in nth row is C(n-1, r-1)
- Each row is symmetric

### 4. Multinomial Theorem

An extension of the binomial theorem for more than two terms:

(x₁ + x₂ + ... + x_k)^n = Σ (n! / (n₁! n₂! ... n_k!)) x₁^n₁ x₂^n₂ ... x_k^n_k

Where the sum is over all nonnegative integers n₁, n₂, ..., n_k such that n₁ + n₂ + ... + n_k = n.

The coefficient n! / (n₁! n₂! ... n_k!) is called the multinomial coefficient.

## Examples

### Example 1: Combination Calculation

**Problem:** In how many ways can a committee of 3 men and 2 women be formed from a group of 6 men and 5 women?

**Solution:**

Step 1: Select 3 men from 6 men
C(6, 3) = 6! / (3! × 3!) = (720) / (6 × 6) = 720 / 36 = 20

Step 2: Select 2 women from 5 women
C(5, 2) = 5! / (2! × 3!) = (120) / (2 × 6) = 120 / 12 = 10

Step 3: Since these selections are independent, multiply the results
Total ways = C(6, 3) × C(5, 2) = 20 × 10 = 200 ways

### Example 2: Binomial Expansion

**Problem:** Find the coefficient of x⁴ in the expansion of (2x - 3)⁷

**Solution:**

Using the general term: T(r+1) = C(7, r) (2x)^(7-r) (-3)^r

We need the term containing x⁴, so:
(2x)^(7-r) should give x⁴
This means 7-r = 4, so r = 3

Now substitute r = 3:
Coefficient = C(7, 3) × 2^(7-3) × (-3)³
= C(7, 3) × 2⁴ × (-27)
= 35 × 16 × (-27)
= 35 × (-432)
= -15,120

Therefore, the coefficient of x⁴ is -15,120

### Example 3: Using Pascal's Identity

**Problem:** Prove that C(7, 3) = C(6, 2) + C(6, 3)

**Solution:**

Using Pascal's Identity: C(n, r) = C(n-1, r-1) + C(n-1, r)

For n = 7, r = 3:
C(7, 3) = C(6, 2) + C(6, 3)

Now compute each side:
C(7, 3) = 7! / (3! × 4!) = 5040 / (6 × 24) = 5040 / 144 = 35
C(6, 2) = 6! / (2! × 4!) = 720 / (2 × 24) = 720 / 48 = 15
C(6, 3) = 6! / (3! × 3!) = 720 / (6 × 6) = 720 / 36 = 20

Left side: 35
Right side: 15 + 20 = 35

Thus, C(7, 3) = C(6, 2) + C(6, 3) is verified.

## Exam Tips

1. **Memorize the combination formula:** C(n, r) = n!/(r!(n-r)!) - This is the foundation for solving most combination problems.

2. **Apply the symmetry property:** When n is large, use C(n, r) = C(n, n-r) to simplify calculations. For example, C(100, 97) = C(100, 3).

3. **For binomial expansion problems:** Always identify the general term T(r+1) = C(n, r)a^(n-r)b^r first, then determine which value of r gives the required term.

4. **Remember Pascal's identity:** C(n, r) + C(n, r-1) = C(n+1, r) is frequently used in proofs and simplifications.

5. **Use special cases:** Setting a = 1, b = 1 gives sum of coefficients = 2^n. Setting a = 1, b = -1 gives alternating sum = 0.

6. **For multinomial problems:** Identify the exponent requirements first, then compute the multinomial coefficient using n!/(n₁!n₂!...).

7. **Practice with Pascal's Triangle:** Understand how to quickly generate and use Pascal's Triangle for small values of n.

8. **Check your answer's reasonableness:** In combination problems, answer should not exceed the total possible selections.
