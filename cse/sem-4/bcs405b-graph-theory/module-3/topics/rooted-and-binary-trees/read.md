# Rooted and Binary Trees

## Table of Contents

- [Rooted and Binary Trees](#rooted-and-binary-trees)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Basic Tree Definitions](#1-basic-tree-definitions)
  - [2. Properties of Rooted Trees](#2-properties-of-rooted-trees)
  - [3. Binary Trees](#3-binary-trees)
  - [4. Binary Tree Traversals](#4-binary-tree-traversals)
  - [5. Spanning Trees](#5-spanning-trees)
  - [6. Binary Search Trees (BST)](#6-binary-search-trees-bst)
- [Examples](#examples)
  - [Example 1: Binary Tree Properties](#example-1-binary-tree-properties)
  - [Example 2: Tree Traversal](#example-2-tree-traversal)
  - [Example 3: Spanning Tree Count](#example-3-spanning-tree-count)
- [Exam Tips](#exam-tips)

## Introduction

Trees represent one of the most important non-linear data structures in discrete mathematics and computer science. Unlike linear data structures such as arrays or linked lists, trees organize data in a hierarchical manner, making them essential for representing relationships, managing hierarchical data, and enabling efficient searching and sorting operations. In the context of graph theory, a tree is defined as a connected acyclic graph, and when one vertex is distinguished as the root, it becomes a rooted tree.

Rooted trees provide a natural way to represent parent-child relationships, organizational hierarchies, and file system structures. Binary trees, a special type of rooted tree where each node has at most two children, form the foundation of many efficient algorithms including binary search trees, heap data structures, and expression parsing. Understanding the properties, traversals, and applications of rooted and binary trees is crucial for computer science students, as these concepts appear frequently in algorithm design, database systems, and compiler construction.

This module explores the fundamental concepts of rooted trees and binary trees, their properties, traversal methods, and practical applications. We will examine how these structures enable efficient data management and problem-solving in various computational domains.

## Key Concepts

### 1. Basic Tree Definitions

A **tree** is a connected undirected graph with no simple cycles. For a graph with n vertices, a tree contains exactly n-1 edges. Any connected graph without cycles is a tree, and any acyclic graph is a forest (a collection of trees).

A **rooted tree** is a tree in which one vertex is distinguished as the root. This distinction gives the tree a natural direction—from the root downward to the leaves. In a rooted tree:

- The root has no parent
- Every other node has exactly one parent
- Nodes with no children are called **leaves** or **terminal vertices**
- Nodes with children are called **internal nodes** or **branching vertices**

The **level** or **depth** of a node is the length of the path from the root to that node. The root is at level 0. The **height** of a tree is the maximum level of any node in the tree.

### 2. Properties of Rooted Trees

For a rooted tree with n vertices:

- Number of edges = n - 1
- If a node has degree d (including edge to parent), it has d - 1 children (except root which has d children)
- A rooted tree with branching factor b has at most b^h nodes at height h
- The number of leaves in a tree can be related to internal nodes with certain properties

**Theorem**: In any rooted tree, if internal nodes have at most b children, then with i internal nodes and L leaves, we have L ≤ (b - 1)i + 1.

### 3. Binary Trees

A **binary tree** is a rooted tree in which each node has at most two children. The two children are typically distinguished as the **left child** and **right child**. Binary trees are particularly important because:

- Each node has at most two children, simplifying operations
- They naturally represent binary decisions and expressions
- They enable O(log n) search times in balanced configurations

**Full Binary Tree**: A binary tree in which every node has either 0 or 2 children (no nodes with exactly 1 child).

**Complete Binary Tree**: A binary tree in which all levels except possibly the last are completely filled, and all nodes are as far left as possible.

**Perfect Binary Tree**: A binary tree in which all interior nodes have exactly two children and all leaves are at the same level.

### 4. Binary Tree Traversals

Tree traversal refers to the process of visiting each node in a tree exactly once in a systematic order. For binary trees, there are four common traversal methods:

**Inorder Traversal** (Left, Root, Right): Visit left subtree, then root, then right subtree. For binary search trees, inorder traversal produces nodes in sorted order.

**Preorder Traversal** (Root, Left, Right): Visit root first, then left subtree, then right subtree. Useful for creating copies of trees and prefix expressions.

**Postorder Traversal** (Left, Right, Root): Visit left subtree, then right subtree, then root. Useful for deleting trees and evaluating postfix expressions.

**Level Order Traversal**: Visit nodes level by level from top to bottom, left to right. Requires a queue data structure.

### 5. Spanning Trees

A **spanning tree** of a connected graph G is a subgraph that is a tree and contains all vertices of G. A connected graph with n vertices has at least one spanning tree with exactly n-1 edges.

**Properties of Spanning Trees**:

- A spanning tree is a minimal connected subgraph (removing any edge disconnects it)
- Every connected graph has at least one spanning tree
- A graph has a unique spanning tree if and only if it is a tree itself

**Minimum Spanning Tree (MST)**: For a weighted graph, a spanning tree with minimum total weight. Important algorithms include Prim's algorithm and Kruskal's algorithm.

### 6. Binary Search Trees (BST)

A binary search tree is a binary tree where for each node:

- All nodes in the left subtree have values less than the node's value
- All nodes in the right subtree have values greater than the node's value
- Both subtrees are also binary search trees

This property enables efficient searching, insertion, and deletion operations with average case O(log n) time complexity.

## Examples

### Example 1: Binary Tree Properties

Consider a complete binary tree with 15 nodes.

**Solution**:

- Height of tree = log₂(15) = 3 (since 2^4 = 16 > 15, height is 3)
- Maximum nodes at level 3 = 2^3 = 8 (leaves)
- Total nodes in levels 0, 1, 2 = 1 + 2 + 4 = 7 (internal nodes)
- For a complete binary tree with n nodes, the number of leaves is either n/2 or (n/2) + 1
- Here leaves = 8, which equals ceiling(15/2) = 8

### Example 2: Tree Traversal

Given a binary tree with root value A, left child B (with children D, E), and right child C (with child F), perform all traversals:

```
 A
 / \
 B C
 / \ \
 D E F
```

**Inorder (LNR)**: D → B → E → A → C → F

**Preorder (NLR)**: A → B → D → E → C → F

**Postorder (LRN)**: D → E → B → F → C → A

**Level Order**: A → B → C → D → E → F

### Example 3: Spanning Tree Count

How many spanning trees does a cycle graph C₄ have?

**Solution**:
For a cycle graph C₄ with 4 vertices:

- We can form spanning trees by removing any one edge from the cycle
- C₄ has 4 edges, so removing any 1 edge gives a spanning tree
- Number of spanning trees = 4 (one for each edge removal)

More generally, for a cycle graph Cₙ, the number of spanning trees is n.

## Exam Tips

1. **Remember the fundamental tree property**: A tree with n vertices has exactly n-1 edges. This is frequently tested in university exams.

2. **Binary tree formula**: For any binary tree with n nodes, maximum number of leaves is ceil(n/2), and minimum height is floor(log₂n).

3. **Traversal relationships**: If you know the traversal sequences, you can reconstruct the tree. Remember that preorder + inorder or postorder + inorder uniquely determines the tree structure.

4. **Complete vs Full vs Perfect**: Memorize the distinctions—complete fills left to right, full has 0 or 2 children, perfect has all levels filled with 2 children each.

5. **Spanning tree minimum edges**: A spanning tree of n vertices always has exactly n-1 edges. This is a key property for solving many exam problems.

6. **Height of complete binary tree**: For a complete binary tree with n nodes, height = floor(log₂n). This formula is essential for time complexity analysis.

7. **Binary search tree property**: Left subtree < root < right subtree. This ordering enables efficient O(log n) search in balanced BSTs.
