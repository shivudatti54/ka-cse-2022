# Binary Trees: Definition & Properties

**Data Structures | BSc (Hons) Computer Science | Delhi University (NEP 2024 UGCF)**

## Introduction

A binary tree is a fundamental non-linear hierarchical data structure in which each node has at most two children, referred to as the left child and right child. It serves as the foundation for more complex data structures like binary search trees, heaps, and AVL trees, and is extensively used in searching, sorting, and expression evaluation algorithms.

## Definition

A binary tree is a finite set of nodes that is either:
- **Empty** (null tree, no nodes), or
- **Non-empty** — consists of a root node with two distinct binary subtrees: the left subtree and the right subtree.

### Key Terminology
- **Root**: The topmost node of the tree
- **Parent**: A node with one or more child nodes
- **Child**: A node descended from a parent node
- **Siblings**: Nodes sharing the same parent
- **Leaf Node**: A node with no children (degree 0)
- **Internal Node**: A node with at least one child
- **Level**: The root is at level 0; each subsequent level = parent's level + 1
- **Height**: The maximum level of any node in the tree (root to deepest leaf)
- **Depth**: The length of the path from root to a given node

## Important Properties

- **Maximum Nodes at Level i**: At most 2^i nodes exist at level *i* (root at i=0)
- **Maximum Nodes in Tree of Height h**: A binary tree of height *h* can have at most (2^(h+1) - 1) nodes
- **Relationship between Nodes and Edges**: For any non-empty binary tree with *n* nodes, there are exactly *(n-1)* edges
- **Leaf vs Internal Nodes**: In a binary tree, if *L* = number of leaf nodes and *I* = number of internal nodes (with degree 2), then **L = I + 1**
- **Minimum Height**: For *n* nodes, the minimum possible height is ⌊log₂(n)⌋
- **Maximum Height**: A skewed tree (like a linked list) can have height *(n-1)*

## Types of Binary Trees

- **Full Binary Tree**: Every node has 0 or 2 children (no node has exactly 1 child)
- **Complete Binary Tree**: All levels except possibly the last are completely filled, and nodes are left-aligned
- **Perfect Binary Tree**: All internal nodes have 2 children and all leaf nodes are at the same level
- **Balanced Binary Tree**: Height difference between left and right subtrees is at most 1 for every node
- **Binary Search Tree (BST)**: Left child contains smaller values; right child contains larger values

## Conclusion

Binary trees form an essential topic in the Delhi University Data Structures syllabus (UGCF NEP 2024). Understanding their definitions, properties, and types is crucial for solving tree-related problems and mastering advanced data structures. The logarithmic relationship between nodes and height makes binary trees efficient for operations like searching, insertion, and deletion — making them indispensable in computer science applications.