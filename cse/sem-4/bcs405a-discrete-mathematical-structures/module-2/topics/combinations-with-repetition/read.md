# Combinations with Repetition

## Table of Contents

- [Combinations with Repetition](#combinations-with-repetition)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Combinations with Repetition](#definition-of-combinations-with-repetition)
  - [Stars and Bars Method](#stars-and-bars-method)
  - [Conditions for Applying Combinations with Repetition](#conditions-for-applying-combinations-with-repetition)
  - [Types of Problems](#types-of-problems)
  - [Relationship with Other Combinatorial Concepts](#relationship-with-other-combinatorial-concepts)
- [Examples](#examples)
  - [Example 1: Restaurant Order Problem](#example-1-restaurant-order-problem)
  - [Example 2: Committee Formation with Role Repetition](#example-2-committee-formation-with-role-repetition)
  - [Example 3: Integer Solutions Problem](#example-3-integer-solutions-problem)
- [Exam Tips](#exam-tips)

## Introduction

Combinations with repetition is a fundamental concept in combinatorics that deals with selecting items from a set where repetitions are allowed, but the order of selection does not matter. This is also known as "combinations with replacement" or the "stars and bars" method. In real-world scenarios, we frequently encounter situations where we need to choose items allowing duplicates - such as selecting fruits from a store where we can pick multiple apples, or distributing identical objects among distinct boxes.

The key distinction between regular combinations and combinations with repetition lies in whether we can select the same element more than once. In standard combinations (without repetition), each element can be chosen at most once. However, in combinations with repetition, elements can be selected multiple times. For instance, if we want to choose 3 fruits from 5 available types (apple, banana, orange, mango, grape), allowing repetition, we could select (apple, apple, banana), (orange, orange, orange), or (apple, banana, banana) - all valid selections where order doesn't matter.

This topic is essential for the university's Discrete Mathematical Structures course as it forms the foundation for solving various counting problems in computer science, including algorithm analysis, probability calculations, and combinatorial circuit design. Understanding when and how to apply combinations with repetition enables students to tackle complex problems in data structures, cryptography, and resource allocation algorithms.

## Key Concepts

### Definition of Combinations with Repetition

Combinations with repetition refers to the number of ways to select k items from n distinct items where:

- Repetitions are allowed (each item can be selected multiple times)
- Order does not matter (selections are combinations, not permutations)

The formula for combinations with repetition is given by:

**C(n + k - 1, k) = C(n + k - 1, n - 1) = (n + k - 1)! / (k! × (n - 1)!)**

This can also be written as: **((n + k - 1) choose k)**

Where:

- n = number of distinct types/items available
- k = number of items to be selected

### Stars and Bars Method

The "stars and bars" technique is an intuitive visualization for solving combinations with repetition problems. This method represents the selection using two symbols:

- **Stars (★)**: Represent the items being selected
- **Bars (|)**: Separate different types of items

For example, if we have n = 3 types of fruits (apple, banana, cherry) and want to select k = 5 fruits with repetition, we represent this as placing 5 stars (the selected fruits) into 3 bins (the types), separated by 2 bars.

The arrangement ★★|★★|★ represents: 2 apples, 2 bananas, 1 cherry
The arrangement ★|★★★|★ represents: 1 apple, 3 bananas, 1 cherry

The number of bars needed is always (n - 1), and the total symbols (stars + bars) is always (k + n - 1). We need to choose positions for either the k stars or the (n-1) bars from the total positions.

### Conditions for Applying Combinations with Repetition

The problem must satisfy these conditions:

1. **Homogeneous selections**: Items of the same type are indistinguishable
2. **Unordered selections**: The order of selection is irrelevant
3. **Repetition allowed**: Each type can be selected multiple times
4. **Fixed selection size**: We select exactly k items from n types

### Types of Problems

**Type 1: Selecting items with repetition**
Example: In how many ways can we select 4 balls from a box containing 3 different colors (allowing repetition)?

Using formula: C(3 + 4 - 1, 4) = C(6, 4) = 15 ways

**Type 2: Distributing identical objects**
Example: In how many ways can we distribute 7 identical candies among 4 children?

Here, n = 4 children, k = 7 candies
Using formula: C(4 + 7 - 1, 7) = C(10, 7) = C(10, 3) = 120 ways

**Type 3: Non-negative integer solutions**
Example: Find the number of non-negative integer solutions to x₁ + x₂ + x₃ + x₄ = 10

This is equivalent to distributing 10 identical items among 4 variables
Using formula: C(4 + 10 - 1, 10) = C(13, 10) = C(13, 3) = 286

### Relationship with Other Combinatorial Concepts

- **Permutations with repetition**: When order matters, use P(n + k - 1, k) = (n + k - 1)! / (n - 1)!
- **Combinations without repetition**: When repetition is not allowed, use C(n, k)
- **Generating functions**: Combinations with repetition can be studied using generating functions where each type contributes (1 + x + x² + ...)

## Examples

### Example 1: Restaurant Order Problem

**Problem**: A restaurant offers 6 different desserts. In how many ways can a customer order 4 desserts (of the same or different types)?

**Solution**:

- Here, n = 6 (types of desserts)
- k = 4 (desserts to be selected)
- Repetition is allowed, order doesn't matter

Using formula: C(n + k - 1, k) = C(6 + 4 - 1, 4) = C(9, 4)

C(9, 4) = 9! / (4! × 5!) = (9 × 8 × 7 × 6) / (4 × 3 × 2 × 1) = 3024 / 24 = 126

**Answer**: 126 ways

**Verification using stars and bars**:
We need to place 4 stars into 6 categories, requiring 5 bars.
Total positions = 4 + 5 = 9
Choose 4 positions for stars (or 5 for bars): C(9, 4) = C(9, 5) = 126 ✓

### Example 2: Committee Formation with Role Repetition

**Problem**: From a department with 5 senior professors and 4 junior professors, a committee of 6 members is to be formed. The committee must have at least 2 senior professors. In how many ways can this be done?

**Solution**:
This problem requires case analysis based on the number of senior professors:

Let x = number of senior professors (minimum 2)
Then (6 - x) = number of junior professors (must be non-negative, so x ≤ 6)

Possible values of x: 2, 3, 4, 5, 6

- Case 1: 2 seniors, 4 juniors → C(5, 2) × C(4, 4) = 10 × 1 = 10
- Case 2: 3 seniors, 3 juniors → C(5, 3) × C(4, 3) = 10 × 4 = 40
- Case 3: 4 seniors, 2 juniors → C(5, 4) × C(4, 2) = 5 × 6 = 30
- Case 4: 5 seniors, 1 junior → C(5, 5) × C(4, 1) = 1 × 4 = 4
- Case 5: 6 seniors, 0 juniors → C(5, 6) = 0 (not possible since only 5 seniors)

Total = 10 + 40 + 30 + 4 = 84

**Answer**: 84 ways

### Example 3: Integer Solutions Problem

**Problem**: Find the number of positive integer solutions to x₁ + x₂ + x₃ = 15 where each xᵢ ≥ 1.

**Solution**:
For positive integer solutions (each variable ≥ 1), we use a transformation:
Let yᵢ = xᵢ - 1, so yᵢ ≥ 0

Then: (y₁ + 1) + (y₂ + 1) + (y₃ + 1) = 15
y₁ + y₂ + y₃ = 12

Now this is a non-negative integer solution problem with n = 3, k = 12

Using formula: C(3 + 12 - 1, 12) = C(14, 12) = C(14, 2) = 91

**Answer**: 91 solutions

**Verification**:
The minimum sum for positive integers (1 + 1 + 1 = 3) leaves 12 to distribute among 3 variables, which matches our transformed problem.

## Exam Tips

1. **Identify the problem type**: Carefully determine if the problem involves combinations with repetition by checking three conditions: repetition allowed, order irrelevant, identical items of each type.

2. **Apply the correct formula**: Use C(n + k - 1, k) for combinations with repetition. Don't confuse it with C(n, k) for combinations without repetition or P(n, k) for permutations.

3. **Stars and bars visualization**: For problems involving distributing identical objects or finding non-negative integer solutions, draw the stars and bars representation to verify your answer.

4. **Transform positive to non-negative**: For positive integer solutions (xᵢ ≥ 1), use the transformation yᵢ = xᵢ - 1 to convert to non-negative solutions (yᵢ ≥ 0).

5. **Check boundary conditions**: Always verify that n ≥ 1, k ≥ 0, and that the selection is possible given constraints.

6. **Use symmetry property**: Remember that C(n + k - 1, k) = C(n + k - 1, n - 1). Choose the smaller number for easier calculation.

7. **Practice case analysis**: For problems with additional constraints (like "at least" or "at most" conditions), break the problem into cases and sum the results.

8. **Understand generating functions**: For advanced problems, recognize that combinations with repetition correspond to the coefficient of x^k in (1 + x + x² + ...)^n = 1/(1-x)^n.
