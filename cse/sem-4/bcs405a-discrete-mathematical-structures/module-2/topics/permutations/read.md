# Permutations

## Table of Contents

- [Permutations](#permutations)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Fundamental Principle of Counting (Multiplication Rule)](#fundamental-principle-of-counting-multiplication-rule)
  - [Definition of Permutation](#definition-of-permutation)
  - [Permutations of n Objects Taken r at a Time](#permutations-of-n-objects-taken-r-at-a-time)
  - [Permutations with Repetition](#permutations-with-repetition)
  - [Circular Permutations](#circular-permutations)
  - [Derangements (Subfactorial)](#derangements-subfactorial)
- [Examples](#examples)
  - [Example 1: Basic Permutation](#example-1-basic-permutation)
  - [Example 2: Word Arrangement with Repeated Letters](#example-2-word-arrangement-with-repeated-letters)
  - [Example 3: Circular Arrangement](#example-3-circular-arrangement)
- [Exam Tips](#exam-tips)

## Introduction

Permutations form a fundamental concept in discrete mathematics and counting theory. In simple terms, a permutation refers to an arrangement of objects in a specific order, where the order of arrangement matters significantly. Unlike combinations where the order is irrelevant, permutations consider every different ordering of the same set of objects as distinct.

The study of permutations is crucial for computer science students as it forms the foundation for algorithm analysis, particularly in understanding the time complexity of sorting algorithms, combinatorial optimization, and various recursive algorithms. Permutations also play a vital role in probability theory, cryptography, and network communications. In the context of the university's Discrete Mathematical Structures course, mastering permutations is essential as it frequently appears in examination questions and forms the basis for more advanced topics like permutations and combinations, generating functions, and graph theory.

Understanding permutations enables us to solve real-world problems such as scheduling tasks, arranging seats, forming teams with specific roles, and. The concept extends from simple arrangements of a few objects to complex scenarios involving repetitions and circular arrangements, making it a versatile tool in the mathematician's toolkit.

## Key Concepts

### Fundamental Principle of Counting (Multiplication Rule)

Before diving into permutations, it is essential to understand the fundamental principle of counting, which states: "If a task can be performed in m ways and a second task can be performed in n ways after the first task, then the total number of ways to perform both tasks is m × n ways."

This principle extends to multiple tasks: if task 1 can be done in n₁ ways, task 2 in n₂ ways, task 3 in n₃ ways, and so on up to task k in nₖ ways, then all k tasks can be performed in n₁ × n₂ × n₃ × ... × nₖ ways.

### Definition of Permutation

A permutation is an ordered arrangement of r distinct objects selected from n distinct objects. The notation P(n, r) or nPr represents the number of permutations of n objects taken r at a time.

**Formula:** P(n, r) = n! / (n - r)!, where n! (n factorial) = n × (n-1) × (n-2) × ... × 2 × 1

**Special Cases:**

- When r = n: P(n, n) = n! (arranging all n objects)
- When r = 1: P(n, 1) = n (choosing 1 object from n)

### Permutations of n Objects Taken r at a Time

The number of ways to arrange r objects selected from n distinct objects is given by:

**P(n, r) = n(n-1)(n-2)...(n-r+1) = n! / (n-r)!**

This formula can be derived using the fundamental principle of counting: for the first position, we have n choices; for the second position, we have (n-1) choices (since one object is already used); for the third position, we have (n-2) choices; and so on until we place r objects, giving us (n-r+1) choices for the rth position.

### Permutations with Repetition

When some objects are identical (repetition allowed), the formula changes. If there are n objects with repetitions of types: n₁ objects of type 1, n₂ objects of type 2, ..., nk objects of type k, where n₁ + n₂ + ... + nk = n, then the number of distinct permutations is:

**P = n! / (n₁! × n₂! × ... × nk!)**

For example, the letters in the word "BANANA" can be arranged in 6!/(3!×2!×1!) = 720/(6×2×1) = 60 ways.

### Circular Permutations

When arranging objects in a circle, the number of distinct permutations changes because arrangements that can be rotated into each other are considered identical. The number of ways to arrange n distinct objects in a circle is:

**(n-1)!**

This is derived from the fact that for n linear arrangements, there are n starting positions that lead to the same circular arrangement, so we divide n! by n.

**Important Note:** If clockwise and counterclockwise arrangements are considered the same (as in a necklace or bracelet problem), we divide by 2: (n-1)!/2

### Derangements (Subfactorial)

A derangement is a permutation where no element appears in its original position. The number of derangements of n objects is denoted by !n or Dₙ.

**Formula:** !n = n! × Σ(-1)ᵏ/ₖ! for k from 0 to n

This can be computed using the recursive formula: Dₙ = (n-1) × (Dₙ₋₁ + Dₙ₋₂), with D₁ = 0 and D₂ = 1

Values: D₁ = 0, D₂ = 1, D₃ = 2, D₄ = 9, D₅ = 44, D₆ = 265

## Examples

### Example 1: Basic Permutation

**Problem:** In how many ways can 3 students be seated in a row of 5 chairs?

**Solution:**
We need to select 3 chairs from 5 and arrange 3 students in them.
Using P(5, 3) = 5!/(5-3)! = 5!/2! = 120/2 = 60

Alternatively, using the multiplication principle:

- First position: 5 choices
- Second position: 4 choices
- Third position: 3 choices
- Total: 5 × 4 × 3 = 60 ways

**Answer:** 60 ways

### Example 2: Word Arrangement with Repeated Letters

**Problem:** How many distinct arrangements can be made from the letters of the word "STATISTICS"?

**Solution:**
The word "STATISTICS" has 10 letters: S appears 3 times, T appears 3 times, A appears 1 time, I appears 2 times, C appears 1 time.

Total permutations = 10!/(3! × 3! × 2! × 1! × 1!)
= 3,628,800/(6 × 6 × 2)
= 3,628,800/72
= 50,400

**Answer:** 50,400 distinct arrangements

### Example 3: Circular Arrangement

**Problem:** In how many ways can 6 friends be seated around a circular table such that two particular friends always sit together?

**Solution:**
Step 1: Treat the two particular friends as a single unit. Now we have 5 units to arrange in a circle.
Step 2: Number of circular arrangements of 5 units = (5-1)! = 4! = 24
Step 3: The two particular friends can be arranged among themselves in 2! = 2 ways.

Total ways = 24 × 2 = 48

**Answer:** 48 ways

## Exam Tips

1. **Understand the difference between permutations and combinations:** Remember that permutations consider order (arrangements) while combinations consider selection (groups). In permutations, "AB" and "BA" are different; in combinations, they are the same.

2. **Memorize key formulas:** P(n,r) = n!/(n-r)!, permutations with repetition = n!/(n₁!n₂!...), circular permutations = (n-1)!, derangements = !n.

3. **Check for repetition in objects:** Always identify if the objects are distinct or if there are repeated elements before applying the appropriate formula.

4. **For circular arrangements, remember to divide by n:** Unless specified otherwise (necklace problem), always use (n-1)! for circular permutations of n distinct objects.

5. **Apply inclusion-exclusion for derangement problems:** When solving "at least one object in original position" type problems, use inclusion-exclusion principle rather than direct counting.

6. **Read questions carefully:** Determine whether the problem asks for "arrangement" (permutation) or "selection" (combination), as this determines which formula to use.

7. **Practice with previous year questions:** Many university exam questions follow similar patterns, especially those involving arrangements of letters in words and seating arrangements.
