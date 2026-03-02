# Additive Group of Integers Modulo n

## Table of Contents

- [Additive Group of Integers Modulo n](#additive-group-of-integers-modulo-n)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Definition of Integers Modulo n](#1-definition-of-integers-modulo-n)
  - [2. Addition Modulo n](#2-addition-modulo-n)
  - [3. Properties of (Zₙ, +) as a Group](#3-properties-of-z--as-a-group)
  - [4. Cyclic Nature of Zₙ](#4-cyclic-nature-of-z)
  - [5. Order of Elements in Zₙ](#5-order-of-elements-in-z)
  - [6. Subgroups of Zₙ](#6-subgroups-of-z)
  - [7. Euler's Phi Function φ(n)](#7-eulers-phi-function-n)
  - [8. Isomorphism with Cyclic Groups](#8-isomorphism-with-cyclic-groups)
  - [9. Structure of Zₙ\*](#9-structure-of-z)
- [Examples](#examples)
  - [Example 1: Verifying Group Properties in Z₈](#example-1-verifying-group-properties-in-z)
  - [Example 2: Finding Order of Elements in Z₁₅](#example-2-finding-order-of-elements-in-z)
  - [Example 3: Finding Generators of Z₁₂](#example-3-finding-generators-of-z)
- [Exam Tips](#exam-tips)

## Introduction

The study of algebraic structures forms a fundamental pillar in discrete mathematics, with groups being one of the most important algebraic systems. The **additive group of integers modulo n**, denoted as **Zₙ** or **(Z/nZ, +)**, is a central concept in abstract algebra with extensive applications in computer science, cryptography, coding theory, and number theory.

The integers modulo n emerge naturally when we consider the remainders when integers are divided by a positive integer n. This construction leads to a finite group structure that exhibits fascinating properties and serves as the foundation for understanding more complex algebraic systems. The additive group Zₙ is particularly significant because it represents the prototype of all finite cyclic groups and provides concrete examples of group theoretic concepts such as generators, subgroups, and isomorphism.

In this module, we explore the structure, properties, and applications of Zₙ as a group under addition modulo n. Understanding this topic is essential for CSE students as it forms the basis for studying modular arithmetic, which is fundamental to cryptographic algorithms like RSA, and to understanding error-correcting codes.

## Key Concepts

### 1. Definition of Integers Modulo n

The set Zₙ is defined as the set of congruence classes modulo n:

**Zₙ = {0, 1, 2, 3, ..., n-1}**

where two integers a and b are considered equivalent if they differ by a multiple of n, denoted as a ≡ b (mod n). This means that n divides (a - b), or equivalently, a and b leave the same remainder when divided by n.

For example, Z₅ = {0, 1, 2, 3, 4}. Here, the elements represent the five possible remainders when dividing by 5.

### 2. Addition Modulo n

The binary operation of addition modulo n is defined as:

**a ⊕ b = (a + b) mod n**

This means we add the two integers and then take the remainder when dividing by n. For instance, in Z₇:

- 3 ⊕ 5 = 8 mod 7 = 1
- 6 ⊕ 4 = 10 mod 7 = 3

### 3. Properties of (Zₙ, +) as a Group

The structure (Zₙ, +) satisfies all group axioms:

**Closure**: For any a, b ∈ Zₙ, (a + b) mod n ∈ Zₙ

**Associativity**: For any a, b, c ∈ Zₙ, (a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)

**Identity Element**: The element 0 ∈ Zₙ serves as the identity since a ⊕ 0 = (a + 0) mod n = a

**Inverse Element**: For each a ∈ Zₙ, there exists an element b ∈ Zₙ such that a ⊕ b = 0. The inverse of a is (n - a) mod n, except for 0 which is its own inverse.

- Inverse of 3 in Z₇ is (7 - 3) = 4, since 3 ⊕ 4 = 7 mod 7 = 0

**Commutativity**: For any a, b ∈ Zₙ, a ⊕ b = b ⊕ a, making it an abelian group

Therefore, (Zₙ, +) forms an **abelian group** of order n.

### 4. Cyclic Nature of Zₙ

A group G is called **cyclic** if there exists an element g ∈ G such that every element of G can be expressed as g^k for some integer k (in additive notation, ka). The element g is called a **generator** of the group.

**Theorem**: (Zₙ, +) is always a cyclic group.

The generators of Zₙ are precisely those elements that are **coprime to n**, i.e., gcd(a, n) = 1. These are called **primitive elements** or generators.

For example:

- In Z₆: Generators are 1 and 5 (since gcd(1,6) = 1 and gcd(5,6) = 1)
- In Z₇: Generators are 1, 2, 3, 4, 5, 6 (all elements except 0, since 7 is prime)

The element 1 always generates Zₙ because:
1·0 = 0, 1·1 = 1, 1·2 = 2, ..., 1·(n-1) = n-1 (mod n)

### 5. Order of Elements in Zₙ

The **order** of an element a in Zₙ is the smallest positive integer k such that k·a ≡ 0 (mod n), denoted as ord(a).

**Formula**: The order of element a in Zₙ is given by **ord(a) = n / gcd(a, n)**

For example:

- In Z₁₂: ord(3) = 12/gcd(3,12) = 12/3 = 4
  Indeed, 3·4 = 12 ≡ 0 (mod 12), and no smaller positive multiple works
- In Z₁₂: ord(8) = 12/gcd(8,12) = 12/4 = 3

### 6. Subgroups of Zₙ

Since Zₙ is a cyclic group, every subgroup of Zₙ is also cyclic. The subgroups correspond to the divisors of n.

**Theorem**: For each divisor d of n, there exists a unique subgroup of order d, given by:
**H_d = {k·(n/d) | k = 0, 1, 2, ..., d-1}**

This subgroup has order d and is generated by n/d.

For example, in Z₁₂:

- Divisors of 12: 1, 2, 3, 4, 6, 12
- Subgroups:
- H₁ = {0} (order 1)
- H₂ = {0, 6} (order 2)
- H₃ = {0, 4, 8} (order 3)
- H₄ = {0, 3, 6, 9} (order 4)
- H₆ = {0, 2, 4, 6, 8, 10} (order 6)
- H₁₂ = Z₁₂ (order 12)

### 7. Euler's Phi Function φ(n)

Euler's totient function φ(n) counts the number of positive integers less than n that are coprime to n. These are precisely the generators of Zₙ.

Properties:

- If p is prime: φ(p) = p - 1
- If p and q are distinct primes: φ(pq) = (p-1)(q-1)
- For prime power: φ(p^k) = p^k - p^(k-1)
- Generally: φ(n) = n × ∏(1 - 1/p) for all prime divisors p of n

For example:

- φ(12) = 12 × (1 - 1/2) × (1 - 1/3) = 12 × 1/2 × 2/3 = 4
- The four generators of Z₁₂ are {1, 5, 7, 11}

### 8. Isomorphism with Cyclic Groups

All cyclic groups of order n are isomorphic to (Zₙ, +). This is a fundamental result in group theory. If G is a cyclic group of order n generated by g, then the map:

**f: Zₙ → G defined by f(k) = g^k**

is a group isomorphism.

### 9. Structure of Zₙ\*

The set of units (invertible elements) in Zₙ, denoted Zₙ*, forms a multiplicative group:
\*\*Zₙ* = {a ∈ Zₙ | gcd(a, n) = 1}\*\*

The order of this group is φ(n).

For example:

- Z₇\* = {1, 2, 3, 4, 5, 6} with φ(7) = 6
- Z₈\* = {1, 3, 5, 7} with φ(8) = 4
- Z₁₂\* = {1, 5, 7, 11} with φ(12) = 4

This multiplicative group is central to public-key cryptography (RSA algorithm).

## Examples

### Example 1: Verifying Group Properties in Z₈

**Problem**: Verify that (Z₈, +) forms an abelian group.

**Solution**:

**Step 1: Check Closure**
Take any two elements from Z₈ = {0, 1, 2, 3, 4, 5, 6, 7}

- 5 ⊕ 6 = (5 + 6) mod 8 = 11 mod 8 = 3 ∈ Z₈
- 7 ⊕ 7 = 14 mod 8 = 6 ∈ Z₈
  Since all possible sums reduce to values between 0 and 7, closure holds.

**Step 2: Check Associativity**
For any a, b, c ∈ Z₈:
(a ⊕ b) ⊕ c = ((a + b) mod 8 + c) mod 8 = (a + b + c) mod 8
a ⊕ (b ⊕ c) = (a + (b + c) mod 8) mod 8 = (a + b + c) mod 8
Since regular addition is associative, modular addition is also associative.

**Step 3: Find Identity**
0 ⊕ a = (0 + a) mod 8 = a mod 8 = a
So 0 is the identity element.

**Step 4: Find Inverses**

- Inverse of 0: 0 ⊕ 0 = 0
- Inverse of 1: 1 ⊕ 7 = 8 mod 8 = 0
- Inverse of 2: 2 ⊕ 6 = 8 mod 8 = 0
- Inverse of 3: 3 ⊕ 5 = 8 mod 8 = 0
- Inverse of 4: 4 ⊕ 4 = 8 mod 8 = 0

**Step 5: Check Commutativity**
a ⊕ b = (a + b) mod 8 = (b + a) mod 8 = b ⊕ a

Since all group axioms are satisfied, (Z₈, +) is an abelian group.

### Example 2: Finding Order of Elements in Z₁₅

**Problem**: Find the orders of elements 6 and 10 in Z₁₅.

**Solution**:

**For element 6 in Z₁₅:**
Using formula: ord(6) = 15 / gcd(6, 15)
gcd(6, 15) = 3
Therefore, ord(6) = 15/3 = 5

Verification:

- 1·6 = 6 mod 15 ≠ 0
- 2·6 = 12 mod 15 ≠ 0
- 3·6 = 18 mod 15 = 3 ≠ 0
- 4·6 = 24 mod 15 = 9 ≠ 0
- 5·6 = 30 mod 15 = 0 ✓

**For element 10 in Z₁₅:**
Using formula: ord(10) = 15 / gcd(10, 15)
gcd(10, 15) = 5
Therefore, ord(10) = 15/5 = 3

Verification:

- 1·10 = 10 mod 15 ≠ 0
- 2·10 = 20 mod 15 = 5 ≠ 0
- 3·10 = 30 mod 15 = 0 ✓

**Answer**: The order of 6 is 5, and the order of 10 is 3.

### Example 3: Finding Generators of Z₁₂

**Problem**: Find all generators of the group Z₁₂.

**Solution**:

The generators of Zₙ are elements a such that gcd(a, n) = 1.

For n = 12, we need to find all a in {1, 2, 3, ..., 11} with gcd(a, 12) = 1.

- gcd(1, 12) = 1 ✓ → Generator
- gcd(2, 12) = 2 ✗
- gcd(3, 12) = 3 ✗
- gcd(4, 12) = 4 ✗
- gcd(5, 12) = 1 ✓ → Generator
- gcd(6, 12) = 6 ✗
- gcd(7, 12) = 1 ✓ → Generator
- gcd(8, 12) = 4 ✗
- gcd(9, 12) = 3 ✗
- gcd(10, 12) = 2 ✗
- gcd(11, 12) = 1 ✓ → Generator

The generators are {1, 5, 7, 11}.

Verification that 5 generates Z₁₂:

- 1·5 = 5
- 2·5 = 10
- 3·5 = 15 ≡ 3
- 4·5 = 20 ≡ 8
- 5·5 = 25 ≡ 1
- 6·5 = 30 ≡ 6
- 7·5 = 35 ≡ 11
- 8·5 = 40 ≡ 4
- 9·5 = 45 ≡ 9
- 10·5 = 50 ≡ 2
- 11·5 = 55 ≡ 7
- 12·5 = 60 ≡ 0

All 12 elements appear, so 5 is indeed a generator.

**Answer**: The generators of Z₁₂ are {1, 5, 7, 11}.

## Exam Tips

1. **Remember the closure operation**: When adding in Zₙ, always reduce the result modulo n. For example, in Z₉, 7 ⊕ 8 = 15 mod 9 = 6, not 15.

2. **The identity is always 0**: In the additive group (Zₙ, +), 0 is always the identity element. Don't confuse it with 1, which is the identity in multiplicative groups.

3. **Finding inverses quickly**: The additive inverse of a in Zₙ is (n - a) mod n. For instance, inverse of 3 in Z₁₁ is 11 - 3 = 8.

4. **Generators and φ(n)**: The number of generators of Zₙ equals φ(n). Remember to check gcd(a, n) = 1 for generators.

5. **Order formula application**: For element a in Zₙ, remember ord(a) = n / gcd(a, n). This is frequently tested in exams.

6. **Subgroups and divisors**: Every subgroup of Zₙ has order dividing n, and for each divisor d of n, there exists exactly one subgroup of order d (which is cyclic).

7. **Prime modulus**: When n is prime, Zₙ is a field, and every non-zero element is a generator. This is crucial for understanding finite fields.

8. **Distinguish Zₙ as additive vs Zₙ\* as multiplicative**: (Zₙ, +) is always a cyclic group, while (Zₙ\*, ×) is a multiplicative group whose structure depends on n.

9. **Euler's theorem application**: For cryptography problems, remember a^φ(n) ≡ 1 (mod n) when gcd(a, n) = 1.

10. **Isomorphism recognition**: Any cyclic group of order n is isomorphic to (Zₙ, +). This is a fundamental theorem worth remembering.
