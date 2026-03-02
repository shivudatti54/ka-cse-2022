# Counting Binary Trees


## Table of Contents

- [Counting Binary Trees](#counting-binary-trees)
- [Introduction](#introduction)
- [Theoretical Foundation](#theoretical-foundation)
  - [Catalan Numbers: Definition and Properties](#catalan-numbers-definition-and-properties)
  - [Combinatorial Proof of Closed-Form Formula](#combinatorial-proof-of-closed-form-formula)
  - [Types of Binary Trees and Their Enumeration](#types-of-binary-trees-and-their-enumeration)
- [Mathematical Formulation](#mathematical-formulation)
  - [General Binary Tree Count](#general-binary-tree-count)
  - [Root-Based Recurrence](#root-based-recurrence)
  - [Full Binary Tree Count](#full-binary-tree-count)
- [Worked Examples](#worked-examples)
  - [Example 1: BST Enumeration for 4 Keys](#example-1-bst-enumeration-for-4-keys)
  - [Example 2: Full Binary Tree with Internal Nodes](#example-2-full-binary-tree-with-internal-nodes)
  - [Example 3: Comparing General and Full Binary Trees](#example-3-comparing-general-and-full-binary-trees)
  - [Example 4: Application to Algorithm Analysis](#example-4-application-to-algorithm-analysis)
- [Common Errors and Misconceptions](#common-errors-and-misconceptions)
- [Summary](#summary)

## Introduction

The enumeration of binary trees constitutes a fundamental problem in combinatorial mathematics with profound applications in computer science. The study involves determining the number of distinct binary tree configurations possible for a given number of nodes, analyzing structural properties, and establishing relationships between tree counting and other combinatorial objects such as Dyck paths and monotonic lattice paths.

Binary trees serve as the foundational data structure for numerous computational paradigms, including binary search trees (BST), expression trees in compilers, heap-based priority queues, and Huffman coding trees. Understanding the combinatorial properties of binary trees enables computer scientists to analyze algorithmic complexity, predict memory utilization patterns, and design optimal tree-based algorithms. The mathematical framework underlying tree enumeration relies heavily on Catalan numbers, a sequence of integers that appears remarkably frequently in discrete mathematics and combinatorial theory.

The systematic study of tree enumeration dates to the 18th century, with significant contributions from mathematicians including Leonard Euler, who studied planar trees, and later Eugène Charles Catalan, after whom the Catalan numbers are named. Today, this knowledge is indispensable for computer science professionals working with hierarchical data structures, database indexing, network routing protocols, and compiler design.

## Theoretical Foundation

### Catalan Numbers: Definition and Properties

The sequence of numbers that enumerate binary trees are known as **Catalan numbers**, named after the Belgian mathematician Eugène Charles Catalan (1814-1894). The nth Catalan number is defined by the closed-form formula:

**C(n) = (2n)! / [(n+1)! × n!] = (1/(n+1)) × (2n choose n)**

This formula can also be expressed using binomial coefficients as C(n) = (1/(n+1)) × binomial(2n, n).

**Theorem 1: Catalan Number Recurrence**

The Catalan numbers satisfy the following nonlinear recurrence relation:

C(0) = 1

C(n+1) = Σ(i=0 to n) C(i) × C(n-i) for n ≥ 0

**Proof of Recurrence Relation:**

Consider constructing a binary tree with (n+1) nodes. Let the root have i nodes in its left subtree and (n-i) nodes in its right subtree, where 0 ≤ i ≤ n. The number of possible left subtrees is C(i) and the number of possible right subtrees is C(n-i). By the multiplication principle, there are C(i) × C(n-i) trees with exactly i nodes in the left subtree. Summing over all possible values of i yields the recurrence relation. ∎

The first ten Catalan numbers are: C(0)=1, C(1)=1, C(2)=2, C(3)=5, C(4)=14, C(5)=42, C(6)=132, C(7)=429, C(8)=1430, C(9)=4862.

### Combinatorial Proof of Closed-Form Formula

**Theorem 2: Closed-Form Derivation**

The number of binary trees with n nodes equals C(n) = (2n)! / [(n+1)! × n!].

**Proof using Ballot Problem:**

Consider the problem of counting monotonic lattice paths from (0,0) to (n,n) that never cross above the diagonal y=x. Each such path corresponds uniquely to a binary tree with n+1 nodes (or n edges). The total number of monotonic paths from (0,0) to (n,n) without restrictions is binomial(2n, n).

By the Ballot Theorem (also known as the André's reflection method), the number of paths that do not cross above the diagonal equals binomial(2n, n) - binomial(2n, n+1) = (1/(n+1)) × binomial(2n, n) = C(n).

The bijection between such lattice paths and binary trees is established by interpreting "up" moves as left child edges and "right" moves as right child edges, ensuring the prefix property required for valid trees. ∎

### Types of Binary Trees and Their Enumeration

**1. Rooted Binary Trees**

A rooted binary tree is a hierarchical structure where each node possesses at most two children, distinguished as left and right children. The enumeration of rooted binary trees with n nodes follows the Catalan number sequence, as established by Theorem 1.

**2. Full (Strict) Binary Trees**

A full binary tree (or strict binary tree) is defined as a binary tree in which each node possesses either zero or exactly two children. Let n represent the number of internal (non-leaf) nodes. The relationship between internal nodes and total nodes in a full binary tree is given by: total nodes = 2n + 1, with exactly n + 1 leaf nodes.

**Theorem 3: Full Binary Tree Enumeration**

The number of full binary trees with n internal nodes equals C(n).

**Proof:** Each full binary tree with n internal nodes corresponds uniquely to a general binary tree with n nodes through the correspondence of internal nodes to tree nodes. Therefore, the enumeration is identical: C(n). ∎

**3. Complete Binary Trees**

A complete binary tree satisfies the property that all levels except possibly the last are completely filled, and the last level's nodes are positioned as far left as possible. Unlike general binary trees, complete binary trees have a unique structure for each value of n, hence the count is always 1.

**4. Binary Search Trees (BST)**

A binary search tree is a binary tree with the ordering property: all nodes in the left subtree have values less than the root, and all nodes in the right subtree have values greater than the root. For n distinct keys, the number of possible BST structures equals C(n).

**Theorem 4: BST Enumeration**

The number of distinct binary search trees constructible from n distinct keys is C(n).

**Proof:** Select any key as the root. Keys smaller than the root form the left subtree, and keys larger form the right subtree. If i keys are placed in the left subtree, (n-i-1) keys occupy the right subtree. The number of BSTs with i keys in the left subtree is C(i) × C(n-i-1). Summing over all i from 0 to n-1 yields C(n) by the Catalan recurrence with appropriate index transformation. ∎

## Mathematical Formulation

### General Binary Tree Count

The number of different binary trees that can be formed with n distinct nodes (unlabeled) is given by:

**B(n) = C(n) = (2n)! / [(n+1)! × n!]**

### Root-Based Recurrence

Let T(n) denote the number of binary trees with n nodes, where T(0) = 1 (empty tree). The recurrence relation is:

**T(n) = Σ(i=1 to n) T(i-1) × T(n-i)**

This follows directly from selecting i-1 nodes for the left subtree and n-i nodes for the right subtree.

### Full Binary Tree Count

For full binary trees with n internal nodes:

**F(n) = C(n) = (2n)! / [(n+1)! × n!]**

The total number of nodes is 2n + 1, with n + 1 leaf nodes.

## Worked Examples

### Example 1: BST Enumeration for 4 Keys

**Problem:** Determine the number of distinct binary search trees that can be formed using the keys {1, 2, 3, 4}.

**Solution:**

Using the Catalan formula with n = 4:

C(4) = (2×4)! / [(4+1)! × 4!]
C(4) = 8! / [5! × 4!]
C(4) = 40320 / (120 × 24)
C(4) = 40320 / 2880 = 14

**Verification using recurrence:**

T(0) = 1
T(1) = T(0) × T(0) = 1
T(2) = T(0) × T(1) + T(1) × T(0) = 1 + 1 = 2
T(3) = T(0) × T(2) + T(1) × T(1) + T(2) × T(0) = 2 + 1 + 2 = 5
T(4) = T(0) × T(3) + T(1) × T(2) + T(2) × T(1) + T(3) × T(0) = 5 + 2 + 2 + 5 = 14

Thus, 14 distinct BSTs are possible.

### Example 2: Full Binary Tree with Internal Nodes

**Problem:** How many full binary trees exist with 5 internal nodes? Also determine the total number of nodes and leaf nodes.

**Solution:**

For full binary trees, n = 5 internal nodes.

C(5) = (2×5)! / [(5+1)! × 5!]
C(5) = 10! / [6! × 5!]
C(5) = 3628800 / (720 × 120)
C(5) = 3628800 / 86400 = 42

Total nodes = 2n + 1 = 2(5) + 1 = 11
Leaf nodes = n + 1 = 6

Therefore, 42 full binary trees are possible with 5 internal nodes, containing 11 total nodes and 6 leaf nodes.

### Example 3: Comparing General and Full Binary Trees

**Problem:** For n = 4 nodes, compare the number of general binary trees versus full binary trees.

**Solution:**

**General binary trees with 4 nodes:**
Using C(3) since formula uses n-1 for nodes count:
B(4) = C(3) = 5 trees

**Full binary trees with n internal nodes:**
For 4 nodes in a full binary tree, internal nodes = (4-1)/2 = 1.5 (not integer), so this is impossible.

For n = 3 internal nodes (total nodes = 7):
F(3) = C(3) = 5 trees

This illustrates that full binary trees require an odd number of total nodes (2n+1), while general binary trees can have any n ≥ 0.

### Example 4: Application to Algorithm Analysis

**Problem:** Analyze the average number of comparisons required to search for an element in a randomly constructed BST with n distinct keys.

**Solution:**

In a randomly constructed BST (where all C(n) permutations are equally likely), the expected search cost corresponds to the expected depth of a random node. It can be shown that the average number of comparisons for successful search is approximately 2 ln(n) - O(1), and for unsuccessful search is approximately √(πn).

This result follows from the analysis of the depth distribution in random binary search trees, where the total path length P(n) satisfies the recurrence P(n) = n + (1/n) × Σ(i=0 to n-1) [P(i) + P(n-1-i)], with asymptotic solution P(n) ~ 2n ln(n).

## Common Errors and Misconceptions

1. **Node Count vs Index:** Many students confuse the formula index. The formula C(n) gives trees with n+1 nodes or n edges. For n nodes, use C(n-1).

2. **Labeled vs Unlabeled:** The Catalan formula applies only to unlabeled (structural) trees. For labeled trees where node values matter, the count multiplies by n! for distinct values.

3. **Full vs Complete:** Full binary trees have the counting property C(n), while complete binary trees have exactly one structure per n.

4. **Base Case Understanding:** T(0) = 1 represents the empty tree, which is essential for recurrence computations.

## Summary

The enumeration of binary trees leads to the Catalan number sequence C(n) = (2n)! / [(n+1)!n!]. This fundamental result applies to rooted binary trees, binary search trees, and full binary trees (with n internal nodes). The recurrence relation C(n+1) = Σ(i=0 to n) C(i)C(n-i) provides an alternative computational method. Understanding these combinatorial foundations is essential for analyzing tree-based algorithms, predicting performance characteristics, and designing efficient data structures.
