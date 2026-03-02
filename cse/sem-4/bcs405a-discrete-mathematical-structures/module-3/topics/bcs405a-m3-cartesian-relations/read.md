# Cartesian Products and Relations

## Table of Contents

- [Cartesian Products and Relations](#cartesian-products-and-relations)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Cartesian Product](#cartesian-product)
  - [Relations](#relations)
  - [Domain and Range](#domain-and-range)
  - [Types of Relations](#types-of-relations)
  - [Properties of Relations on a Set](#properties-of-relations-on-a-set)
  - [Equivalence Relations](#equivalence-relations)
  - [Partial Orders](#partial-orders)
  - [Inverse Relation](#inverse-relation)
  - [Composition of Relations](#composition-of-relations)
- [Examples](#examples)
  - [Example 1: Computing Cartesian Products](#example-1-computing-cartesian-products)
  - [Example 2: Identifying Relation Properties](#example-2-identifying-relation-properties)
  - [Example 3: Composition of Relations](#example-3-composition-of-relations)
- [Exam Tips](#exam-tips)

## Introduction

Cartesian products and relations form the foundational building blocks of discrete mathematics and are essential for understanding more advanced topics in computer science, including database systems, graph theory, and formal language theory. The concept of a relation generalizes the familiar notion of a relationship between quantities, allowing us to formally describe how elements from one set connect to elements in another set or within the same set.

In the context of the university's Discrete Mathematical Structures course, understanding Cartesian products and relations is crucial because these concepts underpin many algorithms and data structures studied in later courses. Relations are extensively used in relational database management systems, where data is organized into tables with rows representing tuples and columns representing attributes. The mathematical foundations of these systems rely directly on the theory of Cartesian products and relations.

This topic explores how sets can be combined to form new sets through Cartesian products, how relationships between sets can be represented as subsets of Cartesian products, and the various properties and types of relations that are essential for both theoretical understanding and practical applications in computing.

## Key Concepts

### Cartesian Product

The Cartesian product of two sets A and B, denoted by A × B, is defined as the set of all ordered pairs (a, b) where a ∈ A and b ∈ B. Formally:

**A × B = {(a, b) : a ∈ A and b ∈ B}**

For example, if A = {1, 2} and B = {x, y}, then:
A × B = {(1, x), (1, y), (2, x), (2, y)}

The cardinality of the Cartesian product follows the formula: |A × B| = |A| × |B|. This property is particularly useful in counting problems and in understanding the complexity of potential relationships between sets.

The Cartesian product is not commutative, meaning A × B ≠ B × A in general (unless A = B or one of them is empty). It is also not associative in the strict sense, but (A × B) × C can be associated with A × (B × C) through a natural bijection.

For multiple sets, we extend the definition to n-ary Cartesian products. The Cartesian product of n sets A₁, A₂, ..., Aₙ is defined as:
**A₁ × A₂ × ... × Aₙ = {(a₁, a₂, ..., aₙ) : aᵢ ∈ Aᵢ for each i}**

### Relations

A relation R from set A to set B is a subset of the Cartesian product A × B. If (a, b) ∈ R, we say that "a is related to b" and denote this as aRb. When A = B, we say R is a relation on A.

For example, consider A = {1, 2, 3} and B = {1, 2, 3, 4}. The relation "divides" from A to B can be represented as:
R = {(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 3)}

### Domain and Range

The domain of a relation R ⊆ A × B is the set of all first components: dom(R) = {a ∈ A : ∃b ∈ B such that (a, b) ∈ R}

The range (or codomain image) of R is the set of all second components: ran(R) = {b ∈ B : ∃a ∈ A such that (a, b) ∈ R}

### Types of Relations

**Empty Relation**: The relation R = ∅, which contains no ordered pairs.

**Universal Relation**: R = A × A, where every element in A is related to every other element.

**Identity Relation**: Iₐ = {(a, a) : a ∈ A}, where each element is related only to itself.

### Properties of Relations on a Set

For a relation R on set A:

**Reflexive**: A relation R is reflexive if (a, a) ∈ R for every a ∈ A. The relation "is equal to" on real numbers is reflexive.

**Symmetric**: R is symmetric if whenever (a, b) ∈ R, then (b, a) ∈ R. The relation "is married to" is symmetric.

**Transitive**: R is transitive if whenever (a, b) ∈ R and (b, c) ∈ R, then (a, c) ∈ R. The relation "is an ancestor of" is transitive.

**Anti-symmetric**: R is anti-symmetric if whenever (a, b) ∈ R and (b, a) ∈ R, then a = b. The relation "is less than or equal to" (≤) is anti-symmetric.

### Equivalence Relations

A relation that is reflexive, symmetric, and transitive is called an equivalence relation. Equivalence relations partition a set into disjoint equivalence classes. For example, the relation "has the same remainder when divided by n" on integers is an equivalence relation.

### Partial Orders

A relation that is reflexive, anti-symmetric, and transitive is called a partial order. A set equipped with a partial order is called a poset (partially ordered set). The relation "is a subset of" (⊆) on the power set of a set is a partial order.

### Inverse Relation

Given a relation R from A to B, the inverse relation R⁻¹ from B to A is defined as:
**R⁻¹ = {(b, a) : (a, b) ∈ R}**

### Composition of Relations

Given R from A to B and S from B to C, the composition S ∘ R from A to C is defined as:
**S ∘ R = {(a, c) : ∃b ∈ B such that (a, b) ∈ R and (b, c) ∈ S}**

## Examples

### Example 1: Computing Cartesian Products

Let A = {a, b} and B = {1, 2, 3}. Find A × B and |A × B|.

**Solution:**
A × B = {(a, 1), (a, 2), (a, 3), (b, 1), (b, 2), (b, 3)}

|A × B| = |A| × |B| = 2 × 3 = 6 elements

### Example 2: Identifying Relation Properties

Consider the relation R on the set of integers Z defined by R = {(a, b) : a - b is even}. Determine whether R is reflexive, symmetric, and transitive.

**Solution:**

_Reflexive_: For any integer a, a - a = 0, which is even. So (a, a) ∈ R for all a ∈ Z. Therefore, R is reflexive.

_Symmetric_: If (a, b) ∈ R, then a - b is even. But -(a - b) = b - a is also even. Therefore (b, a) ∈ R. So R is symmetric.

_Transitive_: If (a, b) ∈ R and (b, c) ∈ R, then a - b is even and b - c is even. Adding: (a - b) + (b - c) = a - c is even. Therefore (a, c) ∈ R. So R is transitive.

Since R is reflexive, symmetric, and transitive, R is an equivalence relation.

### Example 3: Composition of Relations

Let A = {1, 2, 3}, B = {a, b}, C = {x, y}. Let R from A to B be R = {(1, a), (2, b), (3, a)} and S from B to C be S = {(a, x), (b, y)}. Find S ∘ R.

**Solution:**
S ∘ R = {(1, x), (2, y), (3, x)}

We find these pairs by checking: for each (a, b) ∈ R and each (b, c) ∈ S with matching middle element, we include (a, c) in the composition.

- From (1, a) ∈ R and (a, x) ∈ S: (1, x) ∈ S ∘ R
- From (2, b) ∈ R and (b, y) ∈ S: (2, y) ∈ S ∘ R
- From (3, a) ∈ R and (a, x) ∈ S: (3, x) ∈ S ∘ R

## Exam Tips

1. **Remember the Cartesian product definition**: The Cartesian product A × B is the set of all ordered pairs (a, b) where a ∈ A and b ∈ B. This is frequently tested in university exams.

2. **Cardinality formula**: Always remember |A × B| = |A| × |B|, which is essential for counting problems.

3. **Properties of relations**: Memorize the definitions of reflexive, symmetric, transitive, and anti-symmetric properties. Understand that equivalence relations require all three (reflexive, symmetric, transitive), while partial orders require reflexive, anti-symmetric, and transitive.

4. **Anti-symmetric vs Asymmetric**: Anti-symmetric allows (a, b) and (b, a) only when a = b, while asymmetric forbids both when a ≠ b. This is a common point of confusion.

5. **Composition notation**: Be careful with notation. S ∘ R means first apply R, then apply S. The order matters.

6. **Relation vs Function**: Every function is a relation, but not every relation is a function. A relation becomes a function only if each element in the domain has exactly one image in the range.

7. **Power set and relations**: If |A| = n, then |A × A| = n², and there are 2^(n²) possible relations on A. This is important for understanding the scope of possible relations.

8. **Inverse relation**: Remember that the inverse of a relation simply swaps each ordered pair. If R = {(1, 2), (3, 4)}, then R⁻¹ = {(2, 1), (4, 3)}.
