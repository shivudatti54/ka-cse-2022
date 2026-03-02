# **Trees: Introduction, Binary Trees, Binary Tree Traversals, Threaded Binary Trees**

## **Introduction**

- Definition: A tree is a non-linear data structure consisting of nodes with at most one edge connecting them.
- Types of Trees:
  - Simple Tree
  - Connected Tree
  - Disconnected Tree
  - Weighted Tree

## **Binary Trees**

- Definition: A binary tree is a tree in which each node has at most two children (left child and right child).
- Properties:
  - Each node has a unique key (or value).
  - Each node has at most two children.
- Types of Binary Trees:
  - Full Binary Tree
  - Empty Binary Tree
  - Balanced Binary Tree
  - Unbalanced Binary Tree

## **Binary Tree Traversals**

- Definition: The process of visiting each node in a binary tree in a specific order.
- Types of Traversals:
  - Inorder Traversal (Left-Root-Right)
  - Preorder Traversal (Root-Left-Right)
  - Postorder Traversal (Left-Right-Root)
- Formulas:
  - Inorder Traversal: `T(x) = L(x) + R(x)`
  - Preorder Traversal: `T(x) = x + L(x) + R(x)`
  - Postorder Traversal: `T(x) = L(x) + R(x) + x`

## **Threaded Binary Trees**

- Definition: A binary tree with two types of edges: regular edges and threaded edges.
- Properties:
  - Each node has a unique key (or value).
  - Each node has at most two children (left child and right child).
  - Each node has a threaded edge (either regular or threaded).
- Types of Threaded Binary Trees:
  - Threaded Binary Tree
  - Unthreaded Binary Tree

## **Important Formulas and Definitions**

- Definition: A tree is said to be **balanced** if the height of the left subtree and the right subtree of every node differ by at most one.
- Definition: A tree is said to be **complete** if every level of the tree is fully occupied except possibly the last level, which is occupied from left to right.
- Theorem: A binary tree with n nodes has at most log2(n + 1) levels.
