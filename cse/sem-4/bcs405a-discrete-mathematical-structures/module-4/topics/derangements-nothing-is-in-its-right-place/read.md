# Derangements - Nothing is in its Right Place

## Table of Contents

- [Derangements - Nothing is in its Right Place](#derangements---nothing-is-in-its-right-place)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Derangement](#definition-of-derangement)
  - [Derangement Formula (Inclusion-Exclusion Principle)](#derangement-formula-inclusion-exclusion-principle)
  - [Alternative Formulas for Derangements](#alternative-formulas-for-derangements)
  - [Initial Values of Derangements](#initial-values-of-derangements)
  - [Properties of Derangements](#properties-of-derangements)
- [Examples](#examples)
  - [Example 1: Computing D₅ using the Formula](#example-1-computing-d-using-the-formula)
  - [Example 2: Hat Check Problem](#example-2-hat-check-problem)
  - [Example 3: Probability in Random Permutation](#example-3-probability-in-random-permutation)
- [Exam Tips](#exam-tips)

## Introduction

Derangements represent a fascinating combinatorial concept that addresses the question: "In how many ways can we permute n objects such that no object remains in its original position?" This problem, famously known as the "matching problem" or "problème des ménages," has intrigued mathematicians since the 18th century. The Swiss mathematician Jacob Bernoulli is credited with first studying this problem, though L. Euler and N. Bernoulli also contributed significantly to its development.

In practical terms, derangements appear in numerous real-world scenarios. Consider a scenario where n guests arrive at a party and check their hats at the door. When leaving, each guest randomly picks a hat. The number of ways where nobody gets their own hat back is given by the derangement count. Similarly, in a classroom setting where answer papers are randomly distributed to students, the number of ways to ensure no student receives their own paper corresponds to a derangement. These applications make derangements an essential topic in discrete mathematics, particularly for computer science students studying algorithms, cryptography, and probability theory.

The concept of derangements, denoted as Dₙ or !n (read as "n subfactorial"), serves as a fundamental building block in combinatorics. It bridges the gap between permutations and combinations, introducing students to advanced counting techniques including the inclusion-exclusion principle, which is the primary method for deriving the derangement formula.

## Key Concepts

### Definition of Derangement

A derangement is a permutation of n distinct objects in which no object appears in its original position. In other words, it is a "permutation with no fixed points." If we have a set {1, 2, 3, ..., n} and we create permutations of this set, a derangement is a permutation where σ(i) ≠ i for all i, where σ represents the permutation function.

**Notation:** The number of derangements of n objects is denoted by Dₙ or !n, often read as "subfactorial n."

### Derangement Formula (Inclusion-Exclusion Principle)

The formula for counting derangements is derived using the inclusion-exclusion principle:

**Dₙ = n! × (1 - 1/1! + 1/2! - 1/3! + 1/4! - ... + (-1)ⁿ/n!)**

This can be written as:
**Dₙ = n! × Σ(k=0 to n) [(-1)ᵏ/k!]**

Or equivalently:
**Dₙ = n! × (1 - 1/1! + 1/2! - 1/3! + ... + (-1)ⁿ/n!)**

### Alternative Formulas for Derangements

There are several equivalent formulas to compute derangements:

1. **Recursive Formula:** Dₙ = (n - 1) × (Dₙ₋₁ + Dₙ₋₂), with base cases D₁ = 0 and D₂ = 1

2. **Iterative Formula:** Dₙ = ⌊n!/e + 1/2⌋ (the nearest integer to n!/e)

3. **Summation Formula:** Dₙ = Σ(k=0 to n) [(-1)ᵏ × n!/(k!)]

### Initial Values of Derangements

- D₀ = 1 (by convention, the empty permutation)
- D₁ = 0
- D₂ = 1
- D₃ = 2
- D₄ = 9
- D₅ = 44
- D₆ = 265
- D₇ = 1854
- D₈ = 14833
- D₉ = 133496
- D₁₀ = 1334961

### Properties of Derangements

1. **Asymptotic Behavior:** As n approaches infinity, Dₙ/n! approaches 1/e ≈ 0.3679, meaning approximately 36.79% of all permutations are derangements.

2. **Relation to Subfactorial:** The notation !n emphasizes that derangements are related to factorials but with alternating signs in their computation.

3. **Probability Interpretation:** The probability that a random permutation of n objects is a derangement approaches 1/e as n becomes large.

4. **Recurrence Proof:** Using the recurrence Dₙ = (n-1)(Dₙ₋₁ + Dₙ₋₂), we can derive this by considering where element 1 goes in a derangement of {1, 2, ..., n}.

## Examples

### Example 1: Computing D₅ using the Formula

**Problem:** Find the number of derangements of 5 objects using the formula.

**Solution:**

Using Dₙ = n! × (1 - 1/1! + 1/2! - 1/3! + 1/4! - 1/5!)

For n = 5:

- n! = 5! = 120

The series: 1 - 1/1! + 1/2! - 1/3! + 1/4! - 1/5!
= 1 - 1 + 1/2 - 1/6 + 1/24 - 1/120
= 0 + 0.5 - 0.1667 + 0.0417 - 0.0083
= 0.3667 (approximately)

D₅ = 120 × 0.3667 = 44

**Answer:** 44 derangements

**Verification using recurrence:**

- D₁ = 0
- D₂ = 1
- D₃ = 2
- D₄ = 9
- D₅ = 4 × (D₄ + D₃) = 4 × (9 + 2) = 4 × 11 = 44 ✓

### Example 2: Hat Check Problem

**Problem:** Five people check their hats at a theater. In how many ways can the hats be returned such that nobody receives their own hat?

**Solution:**

This is exactly the derangement problem with n = 5.

Using the recurrence formula:
D₅ = (5-1) × (D₄ + D₃)

We know D₃ = 2
D₄ = 3 × (D₃ + D₂) = 3 × (2 + 1) = 3 × 3 = 9

Therefore, D₅ = 4 × (9 + 2) = 4 × 11 = 44

**Answer:** 44 ways

### Example 3: Probability in Random Permutation

**Problem:** If the 10 letters A, B, C, D, E, F, G, H, I, J are randomly arranged, find the probability that no letter remains in its original alphabetical position.

**Solution:**

This is a derangement problem with n = 10.

Total number of permutations = 10! = 3,628,800

Number of derangements D₁₀ = !10

Using recurrence:
D₈ = 14833
D₉ = 9 × (D₈ + D₇) = 9 × (14833 + 1854) = 9 × 16687 = 150183
D₁₀ = 10 × (D₉ + D₈) = 10 × (150183 + 14833) = 10 × 165016 = 1,650,160

Alternatively, using formula:
D₁₀ = 10! × (1 - 1/1! + 1/2! - 1/3! + ... - 1/10!)
= 3,628,800 × 0.3678794...
≈ 1,333,961

Probability = D₁₀ / 10! = 1,333,961 / 3,628,800 ≈ 0.3679

This approaches 1/e ≈ 0.367879

**Answer:** Probability ≈ 0.3679 or about 36.79%

## Exam Tips

1. **Remember the Base Cases:** For university exams, always remember D₀ = 1, D₁ = 0, and D₂ = 1 as foundation values for solving problems.

2. **Master the Formula:** The primary formula Dₙ = n! × (1 - 1/1! + 1/2! - 1/3! + ... + (-1)ⁿ/n!) is most important and frequently tested.

3. **Use Recurrence for Computation:** The recurrence Dₙ = (n-1)(Dₙ₋₁ + Dₙ₋₂) is easier for manual calculation and is commonly asked in exams.

4. **Understand Inclusion-Exclusion:** Be prepared to derive the derangement formula using the inclusion-exclusion principle, as this demonstrates conceptual understanding.

5. **Approximation Application:** Remember that Dₙ ≈ n!/e, and the probability approaches 1/e ≈ 0.3679 as n increases.

6. **Notation Awareness:** Know that derangements are denoted by Dₙ, !n, or sometimes d(n) — all represent the same concept.

7. **Real-World Context:** Connect derangements to practical scenarios like hat-checking problems, letter distribution, or exam paper shuffling for better retention.

8. **Verify Your Answers:** For small values (n ≤ 5), you can verify using the recurrence or direct enumeration. D₃ = 2, D₄ = 9, D₅ = 44 are commonly used for verification.
