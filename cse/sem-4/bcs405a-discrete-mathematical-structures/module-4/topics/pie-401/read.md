# The Principle of Inclusion and Exclusion

## Table of Contents

- [The Principle of Inclusion and Exclusion](#the-principle-of-inclusion-and-exclusion)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Principle for Two Sets](#basic-principle-for-two-sets)
  - [Extension to Three Sets](#extension-to-three-sets)
  - [General Formulation](#general-formulation)
  - [Derangements (Subfactorial)](#derangements-subfactorial)
- [Examples](#examples)
  - [Example 1: Counting Integers Divisible by 2, 3, or 5](#example-1-counting-integers-divisible-by-2-3-or-5)
  - [Example 2: Counting Numbers Not Divisible by 2, 3, or 5](#example-2-counting-numbers-not-divisible-by-2-3-or-5)
  - [Example 3: Derangements Problem](#example-3-derangements-problem)
- [Exam Tips](#exam-tips)

## Introduction

The Principle of Inclusion and Exclusion (PIE) is a fundamental combinatorial technique used to count the number of elements in the union of multiple sets while accounting for overlapping elements. This principle is essential in discrete mathematics as it provides a systematic method for solving counting problems where direct enumeration is impractical due to multiple overlapping conditions.

In real-world scenarios, we often encounter situations where we need to count objects that satisfy at least one of several properties. For instance, consider counting the number of students who passed in Mathematics OR Physics OR Chemistry. A student might have passed in multiple subjects, and simply adding the counts of students passing each subject would lead to double-counting. The Principle of Inclusion and Exclusion elegantly handles such scenarios by systematically adding and subtracting the counts of intersections.

This topic is crucial for CSE students as it forms the foundation for understanding more advanced combinatorial concepts like derangements, the Euler's phi function, and combinatorial identities. The principle finds applications in probability theory, number theory, and algorithm analysis, making it an indispensable tool in a computer scientist's mathematical arsenal.

## Key Concepts

### Basic Principle for Two Sets

For any two finite sets A and B, the number of elements in their union is given by:

|A ∪ B| = |A| + |B| - |A ∩ B|

This formula accounts for the fact that elements in the intersection have been counted twice (once in A and once in B), so we subtract once to get the correct count.

**Proof:** The union A ∪ B can be partitioned into three disjoint parts: elements only in A, elements only in B, and elements in both A and B. When we add |A| + |B|, we count elements in A ∩ B twice. Subtracting |A ∩ B| once corrects this overcounting.

### Extension to Three Sets

For three sets A, B, and C:

|A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C|

The pattern follows: add the sizes of individual sets, subtract the sizes of all pairwise intersections, then add back the triple intersection.

### General Formulation

For n sets A₁, A₂, ..., Aₙ, the Principle of Inclusion and Exclusion states:

|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| - Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| - ... + (-1)ⁿ⁻¹|A₁ ∩ A₂ ∩ ... ∩ Aₙ|

Where:

- The first sum is over all single sets
- The second sum is over all pairs of sets
- The third sum is over all triples of sets
- And so on, alternating signs

### Derangements (Subfactorial)

A derangement is a permutation of n objects where no object remains in its original position. The number of derangements, denoted D(n) or !n, is given by:

D(n) = n! × Σ(-1)ᵏ/ᵏ! for k from 0 to n

This can be approximated as D(n) = ⌊n!/e + 1/2⌋

Derangements are a classic application of PIE. To count permutations where no element is in its original position:

- Total permutations: n!
- Subtract permutations where at least one element is fixed
- Apply PIE to account for overcounting

The formula simplifies to: D(n) = n! × (1 - 1/1! + 1/2! - 1/3! + ... + (-1)ⁿ/n!)

## Examples

### Example 1: Counting Integers Divisible by 2, 3, or 5

**Problem:** How many integers from 1 to 100 are divisible by 2, 3, or 5?

**Solution:**

Let:

- A = multiples of 2 from 1 to 100
- B = multiples of 3 from 1 to 100
- C = multiples of 5 from 1 to 100

Calculate individual counts:

- |A| = ⌊100/2⌋ = 50
- |B| = ⌊100/3⌋ = 33
- |C| = ⌊100/5⌋ = 20

Calculate pairwise intersections:

- |A ∩ B| = multiples of LCM(2,3) = 6: ⌊100/6⌋ = 16
- |A ∩ C| = multiples of LCM(2,5) = 10: ⌊100/10⌋ = 10
- |B ∩ C| = multiples of LCM(3,5) = 15: ⌊100/15⌋ = 6

Calculate triple intersection:

- |A ∩ B ∩ C| = multiples of LCM(2,3,5) = 30: ⌊100/30⌋ = 3

Apply PIE:
|A ∪ B ∪ C| = 50 + 33 + 20 - 16 - 10 - 6 + 3 = 74

**Answer:** 74 integers

### Example 2: Counting Numbers Not Divisible by 2, 3, or 5

**Problem:** How many integers from 1 to 100 are NOT divisible by 2, 3, or 5?

**Solution:**

We already calculated |A ∪ B ∪ C| = 74 (numbers divisible by at least one of 2, 3, or 5)

Total numbers from 1 to 100 = 100

Numbers NOT divisible by any of these = 100 - 74 = 26

**Answer:** 26 numbers

### Example 3: Derangements Problem

**Problem:** In how many ways can 4 distinct books be arranged on a shelf such that no book is in its original position?

**Solution:**

Using the derangement formula: D(4) = 4! × (1 - 1/1! + 1/2! - 1/3! + 1/4!)

D(4) = 24 × (1 - 1 + 1/2 - 1/6 + 1/24)
D(4) = 24 × (0 + 0.5 - 0.1667 + 0.0417)
D(4) = 24 × 0.375 = 9

Alternatively, using the recurrence D(n) = (n-1)[D(n-1) + D(n-2)]:

- D(1) = 0, D(2) = 1
- D(3) = 2 × (1 + 0) = 2
- D(4) = 3 × (2 + 1) = 9

**Answer:** 9 ways

## Exam Tips

1. **Identify the sets clearly**: Before applying PIE, clearly define what each set represents and what properties they represent.

2. **Remember the alternating sign pattern**: Start with addition for single sets, subtraction for intersections of two sets, addition for three-way intersections, and so on.

3. **Use complements when convenient**: For "at least one" problems, sometimes it's easier to count the complement (none of the properties) and subtract from the total.

4. **For derangements, memorize the recurrence**: D(n) = (n-1)[D(n-1) + D(n-2)] is often easier to compute than the factorial formula in exams.

5. **Check divisibility problems with LCM**: Always use the Least Common Multiple to find intersections of sets defined by divisibility.

6. **Verify your answer**: If possible, check with small values or by alternative reasoning to ensure the answer is reasonable.

7. **Time management**: For n > 3 sets, be careful about the number of terms. For 4 sets, there are 2⁴ = 16 terms—prioritize the most significant ones.
