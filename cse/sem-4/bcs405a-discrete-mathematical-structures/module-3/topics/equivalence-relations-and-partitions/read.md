# Equivalence Relations and Partitions

## Table of Contents

- [Equivalence Relations and Partitions](#equivalence-relations-and-partitions)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Relation Basics](#1-relation-basics)
  - [2. Equivalence Relation Definition](#2-equivalence-relation-definition)
  - [3. Equivalence Classes](#3-equivalence-classes)
  - [4. Partitions](#4-partitions)
  - [5. The Fundamental Theorem](#5-the-fundamental-theorem)
  - [6. Quotient Set](#6-quotient-set)
  - [7. Congruence Modulo n](#7-congruence-modulo-n)
- [Examples](#examples)
  - [Example 1: Proving an Equivalence Relation](#example-1-proving-an-equivalence-relation)
  - [Example 2: Finding Equivalence Classes](#example-2-finding-equivalence-classes)
  - [Example 3: From Partition to Equivalence Relation](#example-3-from-partition-to-equivalence-relation)
  - [Example 4: Modular Arithmetic Application](#example-4-modular-arithmetic-application)
- [Exam Tips](#exam-tips)

## Introduction

In discrete mathematics, relations form the backbone of many computational structures and algorithms. Among the various types of relations, equivalence relations hold a special place due to their ability to group together elements that share common properties. This concept is fundamental in computer science, appearing in areas such as database systems (functional dependencies), programming languages (type equivalence), cryptography (modular arithmetic), and algorithm design (partitioning problems).

An equivalence relation formalizes the intuitive notion of "sameness" or compatibility between elements of a set. When we say two elements are equivalent, we mean they belong to the same category according to some defined criteria. The power of equivalence relations lies in their ability to partition a set into disjoint subsets called equivalence classes, creating a structured way to organize and analyze complex systems.

This topic connects deeply with the concept of partitions, establishing a beautiful correspondence: every equivalence relation induces a partition of the set, and conversely, every partition defines a unique equivalence relation. This duality is known as the Fundamental Theorem of Equivalence Relations and is essential for understanding many advanced topics in discrete mathematics and its applications.

## Key Concepts

### 1. Relation Basics

A relation R from set A to set B is a subset of the Cartesian product A × B. When A = B, we say R is a relation on A. For a relation R on set A, we write aRb to denote (a, b) ∈ R.

The three fundamental properties that relations can possess are:

- **Reflexive**: For all a ∈ A, aRa
- **Symmetric**: For all a, b ∈ A, if aRb then bRa
- **Transitive**: For all a, b, c ∈ A, if aRb and bRc then aRc

### 2. Equivalence Relation Definition

A relation R on a set A is called an **equivalence relation** if it is reflexive, symmetric, and transitive.

**Examples of Equivalence Relations:**

- Equality (=) on any set
- Congruence modulo n on integers: a ≡ b (mod n) if n divides (a - b)
- Similarity of triangles in geometry
- "Has the same remainder when divided by k" on integers

### 3. Equivalence Classes

Given an equivalence relation R on set A, the **equivalence class** of an element a ∈ A is the set of all elements related to a:

[a] = {x ∈ A | xRa}

The element a is called a **representative** or **canonical element** of its equivalence class.

**Theorem 1**: For an equivalence relation R on A:

1. Each element belongs to exactly one equivalence class
2. Two elements are related (aRb) if and only if [a] = [b]
3. The equivalence classes form a partition of A

### 4. Partitions

A **partition** of a set A is a collection of non-empty subsets {A₁, A₂, A₃, ...} such that:

1. The subsets are pairwise disjoint: Aᵢ ∩ Aⱼ = ∅ for i ≠ j
2. The union of all subsets equals A: ⋃Aᵢ = A

Each subset in a partition is called a **block** or **cell**.

### 5. The Fundamental Theorem

**Theorem 2 (Fundamental Theorem of Equivalence Relations)**: Let R be an equivalence relation on set A. Then the set of equivalence classes {[a] | a ∈ A} forms a partition of A.

**Theorem 3 (Converse)**: Let {A₁, A₂, ...} be a partition of set A. Define relation R by: aRb if and only if a and b belong to the same block of the partition. Then R is an equivalence relation on A.

This establishes a **bijection** between equivalence relations on A and partitions of A.

### 6. Quotient Set

The set of all equivalence classes under relation R on A is called the **quotient set** or **factor set**, denoted A/R:

A/R = {[a] | a ∈ A}

### 7. Congruence Modulo n

The most important example in computer science is congruence modulo n. For n ∈ ℕ (n > 1):

Define a ≡ b (mod n) if and only if n divides (a - b), or equivalently, a and b have the same remainder when divided by n.

This is an equivalence relation on ℤ with exactly n equivalence classes:

- [0] = {..., -2n, -n, 0, n, 2n, ...}
- [1] = {..., -2n+1, -n+1, 1, n+1, 2n+1, ...}
- ...
- [n-1] = {..., -n-1, -1, n-1, 2n-1, 3n-1, ...}

The quotient set ℤ/nℤ = {[0], [1], [2], ..., [n-1]} forms the foundation of modular arithmetic used in cryptography and hash functions.

## Examples

### Example 1: Proving an Equivalence Relation

**Problem**: Let R be the relation on ℤ (integers) defined by aRb if and only if a + b is even. Prove that R is an equivalence relation.

**Solution**:

We need to prove R is reflexive, symmetric, and transitive.

**Reflexive**: For any a ∈ ℤ, a + a = 2a is even. Therefore aRa. R is reflexive.

**Symmetric**: For any a, b ∈ ℤ, if aRb (i.e., a + b is even), then b + a = a + b is also even. Hence bRa. R is symmetric.

**Transitive**: Suppose aRb and bRc, meaning a + b is even and b + c is even.

- Even + Even = Even
- (a + b) + (b + c) = a + 2b + c is even
- Since 2b is even, a + c must be even (even - even = even)
- Therefore a + c is even, so aRc. R is transitive.

Since R is reflexive, symmetric, and transitive, R is an equivalence relation.

### Example 2: Finding Equivalence Classes

**Problem**: For the relation in Example 1, find all equivalence classes.

**Solution**:

The equivalence relation partitions ℤ into two classes:

- **[0]**: All even numbers (since 0 + even = even)
- [0] = {..., -4, -2, 0, 2, 4, ...}

- **[1]**: All odd numbers (since 1 + odd = even)
- [1] = {..., -3, -1, 1, 3, 5, ...}

These two classes are disjoint and their union is ℤ, forming a partition.

### Example 3: From Partition to Equivalence Relation

**Problem**: Let A = {1, 2, 3, 4, 5, 6} with partition P = {{1, 4}, {2, 5}, {3, 6}}. Find the equivalence relation R induced by this partition.

**Solution**:

For each block, all elements within that block are related to each other:

- Block {1, 4}: 1R1, 1R4, 4R1, 4R4
- Block {2, 5}: 2R2, 2R5, 5R2, 5R5
- Block {3, 6}: 3R3, 3R6, 6R3, 6R6

R = {(1,1), (1,4), (4,1), (4,4), (2,2), (2,5), (5,2), (5,5), (3,3), (3,6), (6,3), (6,6)}

This relation is reflexive (all diagonal elements present), symmetric (whenever (a,b) is present, (b,a) is too), and transitive.

### Example 4: Modular Arithmetic Application

**Problem**: In ℤ/7ℤ, find [3] + [5] and [4] × [6].

**Solution**:

For addition: [3] + [5] = [3 + 5] = [8] = [1] (since 8 mod 7 = 1)

For multiplication: [4] × [6] = [4 × 6] = [24] = [3] (since 24 mod 7 = 3)

This demonstrates how the quotient set ℤ/7ℤ forms a complete algebraic system.

## Exam Tips

1. **Know the Three Properties**: For proving an equivalence relation, always verify reflexive, symmetric, and transitive properties. Many exam questions ask you to prove or disprove equivalence relations.

2. **Partition Checklist**: Remember that a partition must have: (i) no empty sets, (ii) pairwise disjoint sets, (iii) union equals the original set.

3. **Bijection Between Relations and Partitions**: This is a favorite exam topic. Remember the two-way correspondence: Equivalence Relation ↔ Partition.

4. **Finding Equivalence Classes**: To find [a], apply the defining condition to find all x such that xRa. The representative is arbitrary—[a] = [b] if aRb.

5. **Modular Arithmetic**: Congruence modulo n is the most common example. Remember: a ≡ b (mod n) means n | (a - b), not that a/b gives remainder n.

6. **Quotient Set Notation**: A/R represents the set of all equivalence classes. Its cardinality equals the number of equivalence classes.

7. **Transitivity Trap**: When checking transitivity, ensure the "middle element" is actually in the relation. Many students incorrectly conclude transitivity from seemingly related pairs.

8. **Applications**: Understand practical applications like hash functions (partitioning data) and database normalization (functional dependencies as equivalence relations).
