# **TREES: Introduction, Binary Trees, Binary Tree Traversals, Threaded Binary Trees**

### Introduction

- A tree is a non-linear data structure consisting of nodes with a value and zero or more child nodes.
- Trees are used to represent hierarchical relationships between data elements.

### Binary Trees

- A binary tree is a tree in which each node has at most two children (i.e., left child and right child).
- Definition: A set of nodes where each node has a value and either zero or two children (left child and right child).
- Types of binary trees:
  - Full binary tree: Every node has two children.
  - Empty binary tree: No nodes.
  - Complete binary tree: All levels are fully occupied except possibly the last level.

### Binary Tree Traversals

- Traversal is the process of visiting each node in a tree.
- Types of traversals:
  - Inorder traversal: Left subtree, current node, right subtree.
  - Preorder traversal: Current node, left subtree, right subtree.
  - Postorder traversal: Left subtree, right subtree, current node.

### Threaded Binary Trees

- Threading is the process of adding additional data to the nodes of a binary tree.
- Types of threading:
  - Left child pointer (LC)
  - Right child pointer (RC)
  - Thread (T)
  - Next pointer (N)
  - Previous pointer (P)

### Important Formulas and Definitions

- Height of a binary tree (h): h = max depth of left and right subtrees.
- Depth of a binary tree (d): d = max number of edges between leaf nodes and root.
- Breadth-first search (BFS): Traversing a tree level by level from left to right.
- Depth-first search (DFS): Traversing a tree by visiting a node and then visiting its children.

### Important Theorems

- Theorem 1: A binary tree with n nodes has at most log2(n+1) levels.
- Theorem 2: A binary tree with n nodes has at most 2h-1 edges, where h is the height of the tree.

### Quick Revision Key Points

- Definition of a tree: A non-linear data structure with nodes and edges.
- Types of binary trees: Full, empty, complete binary trees.
- Types of binary tree traversals: Inorder, preorder, postorder traversals.
- Types of threading: Left child pointer, right child pointer, thread, next pointer, previous pointer.
