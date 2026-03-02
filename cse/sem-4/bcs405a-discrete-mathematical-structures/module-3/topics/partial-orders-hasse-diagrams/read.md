# Partial Orders and Hasse Diagrams

## Table of Contents

- [Partial Orders and Hasse Diagrams](#partial-orders-and-hasse-diagrams)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Partial Order Relation](#1-partial-order-relation)
  - [2. Comparable and Incomparable Elements](#2-comparable-and-incomparable-elements)
  - [3. Hasse Diagram](#3-hasse-diagram)
  - [4. Maximal and Minimal Elements](#4-maximal-and-minimal-elements)
  - [5. Greatest and Least Elements](#5-greatest-and-least-elements)
  - [6. Upper and Lower Bounds](#6-upper-and-lower-bounds)
  - [7. Lattice](#7-lattice)
  - [8. Topological Sorting](#8-topological-sorting)
- [Examples](#examples)
  - [Example 1: Divisibility Relation on {1, 2, 3, 4, 6, 12}](#example-1-divisibility-relation-on-1-2-3-4-6-12)
  - [Example 2: Subset Relation on Power Set](#example-2-subset-relation-on-power-set)
  - [Example 3: Topological Sort](#example-3-topological-sort)
- [Exam Tips](#exam-tips)

## Introduction

In discrete mathematics, relations play a fundamental role in understanding connections between elements of sets. Among various types of relations, **partial order relations** hold special significance in computer science, particularly in areas such as database systems, scheduling, file organizations, and dependency analysis. A partial order is a relation that organizes elements in a hierarchical manner based on some ordering criteria, allowing us to compare elements when comparison is possible while acknowledging that some elements may be incomparable.

The concept of partially ordered sets (posets) provides a mathematical framework for representing hierarchical structures that we encounter frequently in real-world applications. For instance, in project management, tasks may have dependencies where some tasks must be completed before others can begin, but tasks without direct dependencies can be executed in any order. Similarly, in software development, header files in C/C++ have include dependencies that form a partial order. The **Hasse diagram** serves as a powerful graphical tool to visualize these partial orders, making complex relationships easier to understand and analyze.

This topic is essential for the university's Discrete Mathematical Structures course and forms the foundation for understanding more advanced concepts like lattices, topological sorting, and algorithm analysis (particularly in understanding time complexity relationships).

## Key Concepts

### 1. Partial Order Relation

A relation R on a set A is called a **partial order** (or **partial ordering**) if it is:

- **Reflexive**: For all a ∈ A, (a, a) ∈ R
- **Antisymmetric**: If (a, b) ∈ R and (b, a) ∈ R, then a = b
- **Transitive**: If (a, b) ∈ R and (b, c) ∈ R, then (a, c) ∈ R

A set equipped with a partial order is called a **partially ordered set** or **poset**, denoted as (A, ≼).

**Examples:**

- (ℤ, ≤) - integers with less than or equal to relation
- (ℕ, |) - natural numbers with divisibility relation
- (P(S), ⊆) - power set of a set with subset relation

### 2. Comparable and Incomparable Elements

In a poset (A, ≼), two elements a and b are said to be **comparable** if either a ≼ b or b ≼ a holds. If neither a ≼ b nor b ≼ a holds, then a and b are **incomparable**, denoted as a || b.

**Example:** In the poset (P({a, b, c}), ⊆):

- {a} and {a, b} are comparable ({a} ⊆ {a, b})
- {a} and {b} are incomparable ({a} ⊄ {b} and {b} ⊄ {a})

### 3. Hasse Diagram

A **Hasse diagram** is a graphical representation of a finite poset where:

- Each element is represented as a vertex (node)
- If a ≼ b and a ≠ b, then a is placed below b
- A direct relation (covering relation) is shown as a line connecting a and b
- Transitive edges are omitted (they are implied)

The **covering relation** (or cover) is defined as: a covers b if a ≼ b, a ≠ b, and there is no element c such that a ≼ c ≼ b.

**Construction Rules:**

1. Place minimal elements at the bottom
2. Place maximal elements at the top
3. Draw lines only for covering relations
4. Smaller elements appear below larger elements

### 4. Maximal and Minimal Elements

In a poset (A, ≼):

- An element m ∈ A is **maximal** if there is no element a ∈ A such that m ≼ a and m ≠ a
- An element m ∈ A is **minimal** if there is no element a ∈ A such that a ≼ m and a ≠ m

**Important:** A poset can have multiple maximal or minimal elements, but at most one greatest and one least element.

### 5. Greatest and Least Elements

- An element g ∈ A is the **greatest element** (top) if for all a ∈ A, a ≼ g
- An element l ∈ A is the **least element** (bottom) if for all a ∈ A, l ≼ a

If they exist, the greatest and least elements are unique.

### 6. Upper and Lower Bounds

Let B be a subset of a poset (A, ≼):

- An element u ∈ A is an **upper bound** of B if b ≼ u for all b ∈ B
- An element l ∈ A is a **lower bound** of B if l ≼ b for all b ∈ B
- The **least upper bound** (supremum or join) is the smallest among all upper bounds
- The **greatest lower bound** (infimum or meet) is the largest among all lower bounds

### 7. Lattice

A poset in which every pair of elements has both a least upper bound and a greatest lower bound is called a **lattice**:

- **Join (∨)**: For a, b ∈ A, a ∨ b is the least upper bound
- **Meet (∧)**: For a, b ∈ A, a ∧ b is the greatest lower bound

### 8. Topological Sorting

A **topological order** or **topological sorting** of a poset is a linear arrangement of all elements such that if a ≼ b, then a appears before b in the sequence. Only **posets without cycles** (i.e., posets that are actually partial orders, not pre-orders) can have topological sorts.

## Examples

### Example 1: Divisibility Relation on {1, 2, 3, 4, 6, 12}

**Problem:** Consider the set A = {1, 2, 3, 4, 6, 12} with the divisibility relation |. Draw the Hasse diagram and identify maximal, minimal, greatest, and least elements.

**Solution:**

Step 1: Understand the relation

- 1|1, 2, 3, 4, 6, 12
- 2|2, 4, 6, 12
- 3|3, 6, 12
- 4|4, 12
- 6|6, 12
- 12|12

Step 2: Identify covering relations (immediate predecessors)

- 1 covers nothing (it's the minimum)
- 2 is covered by 1; 2 covers 4 and 6
- 3 is covered by 1; 3 covers 6
- 4 is covered by 2; 4 covers 12
- 6 is covered by 2 and 3; 6 covers 12
- 12 is covered by 4 and 6 (maximum)

Step 3: Draw Hasse diagram

```
 12
 / \
 4 6
 | / \
 2 3 (2 and 3 connected to 1 below)
 | |
 1
```

Step 4: Identify elements

- **Minimal elements:** 1 (no element divides 1 except itself)
- **Maximal elements:** 12 (12 is not covered by any other element)
- **Least element:** 1 (1 divides every element)
- **Greatest element:** 12 (12 is divisible by every element)

### Example 2: Subset Relation on Power Set

**Problem:** Let S = {a, b, c}. Consider the poset (P(S), ⊆). Draw the Hasse diagram and identify all bounds for subset B = {{a}, {b}}.

**Solution:**

Step 1: Power set elements: ∅, {a}, {b}, {c}, {a,b}, {a,c}, {b,c}, {a,b,c}

Step 2: Hasse diagram (arranged by cardinality)

```
 {a,b,c}
 / | \
 {a,b} {a,c} {b,c}
 | | |
 {a} {b} {c}
 \ | /
 ∅
```

Step 3: Find bounds for B = {{a}, {b}}

**Lower bounds:** Elements that are subsets of both {a} and {b}

- ∅ is a lower bound
- Is {a} a lower bound? No, {a} ⊄ {b}
- Is {b} a lower bound? No, {b} ⊄ {a}

**Greatest lower bound (meet):** Largest among lower bounds = ∅

**Upper bounds:** Elements that contain both {a} and {b}

- {a,b} contains both
- {a,b,c} contains both

**Least upper bound (join):** Smallest among upper bounds = {a,b}

**Answer:**

- Lower bounds: ∅
- Greatest lower bound: ∅
- Upper bounds: {a,b}, {a,b,c}
- Least upper bound: {a,b}

### Example 3: Topological Sort

**Problem:** Find a topological ordering for the poset whose Hasse diagram is:

```
 d
 |
 c
 / \
 a b
```

**Solution:**

Step 1: Identify the partial order from the diagram

- a ≼ c, b ≼ c, c ≼ d
- Therefore: a ≼ c ≼ d and b ≼ c ≼ d

Step 2: Find minimal elements (no predecessors)

- a and b are minimal (nothing comes before them)

Step 3: Build topological order

- Start with minimal elements: a, b (can be in either order)
- Then c (after both a and b)
- Then d (after c)

Step 4: Valid topological orders

- a, b, c, d
- b, a, c, d

Both satisfy: if x ≼ y, then x appears before y.

## Exam Tips

1. **Remember the three properties:** For a partial order, always verify reflexivity, antisymmetry, and transitivity. Common mistakes include confusing antisymmetry with asymmetry.

2. **Hasse diagram construction:** Always place minimal elements at the bottom and draw only covering relations. Don't draw transitive edges—they're implied.

3. **Distinguish maximal from greatest:** A poset can have multiple maximal elements but at most one greatest element. The greatest element must be comparable with all elements.

4. **Lattice verification:** To check if a poset is a lattice, verify that every pair of elements has both meet and join defined.

5. **Topological sort existence:** A poset can have topological ordering if and only if it has no cycles. Check for cycles before attempting topological sort.

6. **Divisibility poset:** For divisibility on {1, 2, ..., n}, remember 1 is always the least element and n is always the greatest element (if n is considered).

7. **Power set examples:** The power set with subset relation is a classic example—always remember the number of elements is 2^n and the structure forms a Boolean lattice.

8. **Notation clarity:** Use ≼ for general partial order, ≤ for numerical orders, | for divisibility, and ⊆ for subset relation. Don't mix them up in exam answers.
