# Properties of Relations

## Table of Contents

- [Properties of Relations](#properties-of-relations)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Definitions](#basic-definitions)
  - [Reflexive Relations](#reflexive-relations)
  - [Symmetric Relations](#symmetric-relations)
  - [Transitive Relations](#transitive-relations)
  - [Composite Relations](#composite-relations)
  - [Inverse Relations](#inverse-relations)
  - [Closure Operations](#closure-operations)
- [Examples](#examples)
  - [Example 1: Classifying Relation Properties](#example-1-classifying-relation-properties)
  - [Example 2: Proving Transitive Closure](#example-2-proving-transitive-closure)
  - [Example 3: Equivalence Relation Verification](#example-3-equivalence-relation-verification)
- [Exam Tips](#exam-tips)

## Introduction

Relations are fundamental constructs in discrete mathematics that describe connections between elements of sets. A relation from set A to set B is essentially a subset of the Cartesian product A × B. When we say "properties of relations," we refer to the special characteristics that certain relations possess, such as reflexivity, symmetry, transitivity, and antisymmetry. These properties are crucial because they help classify relations and determine their behavior in mathematical structures and applications.

In computer science, relations play a vital role in database theory (where they represent table relationships), formal language theory (defining grammar productions), software engineering (modeling dependencies), and many other areas. Understanding relation properties enables us to analyze algorithms, design data structures, and construct mathematical proofs more effectively. This module explores these properties in depth, providing the theoretical foundation necessary for advanced topics like equivalence classes, partial orders, and graph theory.

## Key Concepts

### Basic Definitions

A **relation R** from set A to set B is a subset of A × B, written as R ⊆ A × B. If (a, b) ∈ R, we say "a is related to b" and write aRb. When A = B, we say R is a relation on A.

**Domain** of R: {a ∈ A | ∃b ∈ B such that (a, b) ∈ R}
**Range** of R: {b ∈ B | ∃a ∈ A such that (a, b) ∈ R}

### Reflexive Relations

A relation R on set A is **reflexive** if for every element a ∈ A, (a, a) ∈ R. In other words, every element is related to itself. The identity relation I_A = {(a, a) | a ∈ A} is the smallest reflexive relation on A.

**Examples:**

- "is equal to" (=) on any set of numbers is reflexive
- "is divisible by" on positive integers is reflexive
- "is a subset of" (⊆) on power sets is reflexive

A relation is **irreflexive** if for no element a ∈ A, (a, a) ∈ R. The "is father of" relation is irreflexive since no one is their own father.

### Symmetric Relations

A relation R on set A is **symmetric** if whenever aRb, then bRa for all a, b ∈ A. The relationship "is married to" is symmetric because if person A is married to person B, then person B is married to person A.

A relation is **asymmetric** if whenever aRb, then bRa is never true (for distinct elements). The "is father of" relation is asymmetric.

A relation is **antisymmetric** if whenever aRb and bRa, then a = b. The relation "≤" on real numbers is antisymmetric because if a ≤ b and b ≤ a, then a = b.

### Transitive Relations

A relation R on set A is **transitive** if whenever aRb and bRc, then aRc for all a, b, c ∈ A. The relation "is ancestor of" is transitive—if A is ancestor of B and B is ancestor of C, then A is ancestor of C.

A relation that is reflexive, symmetric, and transitive is an **equivalence relation**. Equality (=) on any set is the classic example. Equivalence relations partition sets into disjoint equivalence classes.

### Composite Relations

Given relations R from A to B and S from B to C, the **composite relation** S ∘ R from A to C is defined as:
S ∘ R = {(a, c) | ∃b ∈ B such that (a, b) ∈ R and (b, c) ∈ S}

For a relation R on set A, we define R^n (n-th power) recursively:

- R^1 = R
- R^(n+1) = R^n ∘ R

R is transitive if and only if R^n ⊆ R for all n ≥ 1.

### Inverse Relations

For a relation R from A to B, the **inverse relation** R^(-1) from B to A is:
R^(-1) = {(b, a) | (a, b) ∈ R}

Properties: If R is reflexive, symmetric, or transitive, then R^(-1) inherits the same property.

### Closure Operations

The **reflexive closure** of R is R ∪ I_A (adds all missing self-pairs).
The **symmetric closure** of R is R ∪ R^(-1) (adds reverse of each pair).
The **transitive closure** of R is R^\* = R ∪ R^2 ∪ R^3 ∪ ...

The transitive closure can be computed using Warshall's algorithm in O(n³) time.

## Examples

### Example 1: Classifying Relation Properties

Let A = {1, 2, 3} and R = {(1,1), (1,2), (2,2), (2,3), (3,3)}. Determine which properties R satisfies.

**Solution:**

1. **Reflexive?** Check (1,1), (2,2), (3,3) ∈ R

- (1,1) ∈ R ✓
- (2,2) ∈ R ✓
- (3,3) ∈ R ✓
- **R is reflexive**

2. **Symmetric?** For every (a,b) ∈ R, check if (b,a) ∈ R

- (1,2) ∈ R but (2,1) ∉ R
- **R is not symmetric**

3. **Antisymmetric?** If aRb and bRa, then a = b

- We never have aRb and bRa for a ≠ b
- **R is antisymmetric** (vacuously true)

4. **Transitive?** If aRb and bRc, check aRc

- (1,1) and (1,2): need (1,2) — present ✓
- (1,2) and (2,3): need (1,3) — not present
- **R is not transitive**

### Example 2: Proving Transitive Closure

Let R = {(1,2), (2,3)} on A = {1,2,3}. Find the transitive closure R\*.

**Solution:**

Compute successive powers:

- R¹ = {(1,2), (2,3)}
- R² = R ∘ R = {(1,3)} [1R2 and 2R3 gives 1R3]
- R³ = R² ∘ R = ∅ [no path of length 3 possible]

R\* = R ∪ R² ∪ R³ = {(1,2), (2,3), (1,3)}

The transitive closure adds (1,3) because 1→2→3 creates a path.

### Example 3: Equivalence Relation Verification

Define relation R on integers Z as aRb if a - b is divisible by 3. Show R is an equivalence relation.

**Solution:**

1. **Reflexive:** a - a = 0, divisible by 3. So aRa. ✓

2. **Symmetric:** If aRb, then a - b = 3k for some k ∈ Z
   Then b - a = -3k = 3(-k), divisible by 3
   So bRa. ✓

3. **Transitive:** If aRb and bRc:
   a - b = 3k and b - c = 3m
   Then a - c = (a - b) + (b - c) = 3(k + m)
   So aRc. ✓

Since R is reflexive, symmetric, and transitive, R is an equivalence relation. The equivalence classes are [0], [1], [2] (integers congruent modulo 3).

## Exam Tips

1. **Remember definitions precisely**: For reflexive: (a,a) ∈ R for all a; for symmetric: aRb implies bRa; for transitive: aRb and bRc implies aRc.

2. **Antisymmetric vs Asymmetric**: Antisymmetric allows aRb and bRa only when a = b; asymmetric never allows both for distinct elements.

3. **Empty set edge cases**: The empty relation on a nonempty set is irreflexive, symmetric, antisymmetric, and transitive—but not reflexive.

4. **Universal relation U = A × A**: This is reflexive (unless A is empty), symmetric, transitive, and antisymmetric (only when |A| ≤ 1).

5. **Testing transitivity efficiently**: Check only pairs where first component matches second component of another pair.

6. **Equivalence relations create partitions**: They divide the set into disjoint equivalence classes; remember this for proof questions.

7. **Transitive closure formula**: R\* = R ∪ R² ∪ R³ ∪ ... ∪ R^n for finite set of size n.

8. **Warshall's algorithm**: For computing transitive closure, remember the iterative update rule: W[k][i][j] = W[k-1][i][j] OR (W[k-1][i][k] AND W[k-1][k][j]).

9. **Inverse properties**: If R has a property, R^(-1) retains it—except irreflexive and asymmetric don't necessarily invert.

10. **Identify common relations**: Equality (=) is equivalence; ≤ is partial order; "is friend with" is often symmetric but not transitive.
