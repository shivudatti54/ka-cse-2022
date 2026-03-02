# First Order Linear Recurrence Relation

## Table of Contents

- [First Order Linear Recurrence Relation](#first-order-linear-recurrence-relation)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Recurrence Relation](#definition-of-recurrence-relation)
  - [First Order Linear Recurrence Relation](#first-order-linear-recurrence-relation)
  - [Homogeneous vs Non-Homogeneous Recurrence Relations](#homogeneous-vs-non-homogeneous-recurrence-relations)
  - [Method of Solving First Order Linear Recurrence Relations](#method-of-solving-first-order-linear-recurrence-relations)
  - [Particular Solution for Non-Homogeneous Relations](#particular-solution-for-non-homogeneous-relations)
  - [General Solution Formula](#general-solution-formula)
  - [Solving with Initial Condition a₁](#solving-with-initial-condition-a)
- [Examples](#examples)
  - [Example 1: Population Growth Model](#example-1-population-growth-model)
  - [Example 2: Compound Interest](#example-2-compound-interest)
  - [Example 3: Non-Homogeneous Recurrence](#example-3-non-homogeneous-recurrence)
  - [Example 4: Arithmetic Progression Case](#example-4-arithmetic-progression-case)
- [Exam Tips](#exam-tips)

## Introduction

Recurrence relations are fundamental mathematical tools used to describe sequences where each term is defined in terms of previous terms. They appear extensively in computer science for analyzing algorithm complexity, in physics for modeling population dynamics, and in finance for predicting economic trends. A first-order linear recurrence relation is the simplest form of recurrence relation where each term depends directly on only the immediately preceding term.

In the context of the university 2022 Scheme for Discrete Mathematical Structures, understanding first-order linear recurrence relations is crucial because they form the foundation for solving more complex recurrence relations of higher orders. These relations are extensively used in counting problems, analyzing recursive algorithms, and solving real-world problems involving exponential growth and decay.

This module covers the theory and applications of first-order linear recurrence relations, including both homogeneous and non-homogeneous cases. Students will learn various methods to solve these relations, understand their characteristics, and apply them to practical problems commonly appearing in university examinations.

## Key Concepts

### Definition of Recurrence Relation

A recurrence relation is an equation that defines a sequence recursively by expressing each term as a function of one or more preceding terms. The general form for a first-order recurrence relation is:

**aₙ = f(aₙ₋₁)** or **aₙ = f(aₙ₋₁, n)**

where aₙ represents the nth term of the sequence, and a₀ (or a₁) serves as the initial condition that starts the sequence.

### First Order Linear Recurrence Relation

A first-order linear recurrence relation has the general form:

**aₙ = c × aₙ₋₁ + d** for n ≥ 1

where:

- c is a constant coefficient (c ≠ 0)
- d is a constant term
- aₙ is the nth term
- aₙ₋₁ is the (n-1)th term

This is called "linear" because each term is expressed as a linear combination of the previous term and a constant. The term "first-order" refers to the fact that only aₙ₋₁ appears on the right-hand side.

### Homogeneous vs Non-Homogeneous Recurrence Relations

**Homogeneous First-Order Linear Recurrence Relation:**
When d = 0, the relation becomes:
**aₙ = c × aₙ₋₁**

This is called homogeneous because all terms contain the unknown aₙ. The solution is straightforward: aₙ = a₀ × cⁿ

**Non-Homogeneous First-Order Linear Recurrence Relation:**
When d ≠ 0, the relation becomes:
**aₙ = c × aₙ₋₁ + d**

This requires finding a particular solution plus the homogeneous solution.

### Method of Solving First Order Linear Recurrence Relations

#### Method 1: Iteration (Substitution Method)

This method involves repeatedly substituting the recurrence relation to find a pattern.

**Example: Solve aₙ = 3aₙ₋₁ with a₀ = 2**

- a₁ = 3a₀ = 3(2) = 6
- a₂ = 3a₁ = 3(6) = 18
- a₃ = 3a₂ = 3(18) = 54

Pattern: aₙ = 2 × 3ⁿ

#### Method 2: Iteration to Closed Form

For non-homogeneous relations, iterate and factor out the pattern:

**Example: Solve aₙ = 3aₙ₋₁ + 5 with a₀ = 1**

a₁ = 3(1) + 5 = 8
a₂ = 3(8) + 5 = 29
a₃ = 3(29) + 5 = 92

General formula: aₙ = a₀cⁿ + d(cⁿ - 1)/(c - 1)

Substituting: aₙ = 1 × 3ⁿ + 5(3ⁿ - 1)/(3 - 1) = 3ⁿ + (5/2)(3ⁿ - 1)

#### Method 3: Characteristic Equation Method

For homogeneous relations aₙ = c × aₙ₋₁:

- Characteristic equation: r - c = 0
- Solution: r = c
- General solution: aₙ = A × cⁿ where A is determined by initial condition

### Particular Solution for Non-Homogeneous Relations

When the non-homogeneous term (d) is a constant, we look for a particular solution of the form P (constant). Substituting:

P = cP + d
P - cP = d
P(1 - c) = d
P = d/(1 - c), provided c ≠ 1

**Special Case: When c = 1**
If c = 1, the recurrence becomes aₙ = aₙ₋₁ + d, which is an arithmetic progression:
aₙ = a₀ + nd

### General Solution Formula

For aₙ = caₙ₋₁ + d with a₀ = a:

**When c ≠ 1:**
aₙ = a × cⁿ + d(cⁿ - 1)/(c - 1)

**When c = 1:**
aₙ = a + nd

### Solving with Initial Condition a₁

Sometimes the recurrence is defined for n ≥ 2 with a₁ as initial condition:

aₙ = caₙ₋₁ + d for n ≥ 2

Then: aₙ = a₁cⁿ⁻¹ + d(cⁿ⁻¹ - 1)/(c - 1) for c ≠ 1

## Examples

### Example 1: Population Growth Model

A bacteria population doubles every hour. If initially there are 100 bacteria, find the population after 6 hours.

**Solution:**

The recurrence relation: aₙ = 2aₙ₋₁ with a₀ = 100

This is homogeneous with c = 2, d = 0

Using formula: aₙ = a₀ × cⁿ = 100 × 2ⁿ

For n = 6: a₆ = 100 × 2⁶ = 100 × 64 = 6400 bacteria

### Example 2: Compound Interest

A bank account has $1000 earning 5% interest per year. Find the amount after 10 years.

**Solution:**

Interest adds 5% => multiply by 1.05 each year

Recurrence: aₙ = 1.05aₙ₋₁ with a₀ = 1000

aₙ = 1000 × (1.05)ⁿ

For n = 10: a₁₀ = 1000 × (1.05)¹⁰ ≈ 1000 × 1.6289 = $1628.89

### Example 3: Non-Homogeneous Recurrence

Solve the recurrence relation aₙ = 3aₙ₋₁ + 7 with initial condition a₀ = 2.

**Solution:**

Using the formula for c ≠ 1:

aₙ = a₀cⁿ + d(cⁿ - 1)/(c - 1)
aₙ = 2 × 3ⁿ + 7(3ⁿ - 1)/(3 - 1)
aₙ = 2 × 3ⁿ + (7/2)(3ⁿ - 1)
aₙ = 2 × 3ⁿ + (7/2) × 3ⁿ - (7/2)
aₙ = (11/2) × 3ⁿ - (7/2)

Verification:

- a₀ = (11/2) × 1 - (7/2) = (11-7)/2 = 2 ✓
- a₁ = (11/2) × 3 - (7/2) = (33-7)/2 = 13
- Using recurrence: a₁ = 3(2) + 7 = 13 ✓

### Example 4: Arithmetic Progression Case

Solve aₙ = aₙ₋₁ + 5 with a₀ = 3.

**Solution:**

Here c = 1, so we use the special formula: aₙ = a₀ + nd

aₙ = 3 + 5n

Verification:

- a₀ = 3 ✓
- a₁ = 3 + 5 = 8; using recurrence: a₁ = 3 + 5 = 8 ✓
- a₂ = 3 + 10 = 13; using recurrence: a₂ = 8 + 5 = 13 ✓

## Exam Tips

1. **Identify the type correctly**: Determine whether the recurrence is homogeneous (d = 0) or non-homogeneous (d ≠ 0) first.

2. **Check the value of c**: If c = 1, use the arithmetic progression formula aₙ = a₀ + nd; otherwise use the geometric progression based formula.

3. **Initial condition matters**: Note whether the initial condition is given as a₀ or a₁ and adjust your formula accordingly.

4. **Verify your solution**: Always substitute n = 0 (or 1) and n = 1 to verify your closed-form solution against the recurrence.

5. **Common mistake to avoid**: Students often forget to subtract 1 from cⁿ in the numerator when applying the formula for non-homogeneous cases.

6. **Step-by-step iteration**: If stuck, write out first 3-4 terms to identify the pattern before applying formulas.

7. **Applications**: Be prepared for word problems involving population, compound interest, and depreciating values - these are favorites in university exams.

8. **Practice all cases**: Ensure practice with c > 1, 0 < c < 1, c < 0, and c = 1 to handle all possibilities.
