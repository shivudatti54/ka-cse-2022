# Module 4: Operations on Binary Trees

## Introduction

A Binary Tree is a fundamental hierarchical data structure where each node has at most two children, referred to as the **left child** and the **right child**. Understanding how to manipulate these trees is crucial for solving complex problems in computer science, such as expression parsing, data compression, and efficient searching/sorting. This module covers the core operations performed on binary trees.

## Core Operations & Concepts

The operations on a binary tree can be broadly classified into two categories: **traversal** (visiting every node) and **modification** (changing the tree's structure or contents).

### 1. Traversal Operations

Traversal is the process of visiting each node in the tree exactly once in a specific order. The order of visitation defines the type of traversal. There are three fundamental depth-first traversals (DFT):

#### a) Preorder Traversal (Root -> Left -> Right)

The root node is visited first, followed by the left subtree, and then the right subtree. This order is useful for creating a copy of the tree or for generating a prefix expression.

**Algorithm:**

1. Visit the root.
2. Traverse the left subtree (recursively).
3. Traverse the right subtree (recursively).

**Example:** For the tree above, Preorder traversal yields: `A, B, D, E, C, F`.

#### b) Inorder Traversal (Left -> Root -> Right)

The left subtree is traversed first, then the root node, and finally the right subtree. When performed on a Binary Search Tree (BST), it visits nodes in ascending order.

**Algorithm:**

1. Traverse the left subtree (recursively).
2. Visit the root.
3. Traverse the right subtree (recursively).

**Example:** For the tree above, Inorder traversal yields: `D, B, E, A, F, C`.

#### c) Postorder Traversal (Left -> Right -> Root)

The left subtree is traversed first, then the right subtree, and finally the root node. This is useful for deleting the tree or for evaluating postfix expressions.

**Algorithm:**

1. Traverse the left subtree (recursively).
2. Traverse the right subtree (recursively).
3. Visit the root.

**Example:** For the tree above, Postorder traversal yields: `D, E, B, F, C, A`.

#### d) Level Order Traversal (Breadth-First)

Nodes are visited level by level, from left to right. This requires a queue data structure to keep track of the nodes at the next level.

**Algorithm:**

1. Enqueue the root node.
2. While the queue is not empty:

- Dequeue a node and visit it.
- Enqueue its left child (if exists).
- Enqueue its right child (if exists).

**Example:** For the tree above, Level Order traversal yields: `A, B, C, D, E, F`.

### 2. Modification Operations

These operations change the structure or content of the tree.

#### a) Insertion

Adds a new node to the tree. In a general binary tree without specific ordering rules, insertion is often done using level order to maintain balance, placing the new node in the first available spot. In a **Binary Search Tree (BST)**, insertion follows specific rules to maintain the BST property (`left child < root < right child`).

#### b) Deletion

Removes a node from the tree. This is more complex than insertion. The strategy depends on the node to be deleted:

- **Node with no children (Leaf):** Simply remove it.
- **Node with one child:** Replace the node with its only child.
- **Node with two children:** Find the node's **inorder successor** (or predecessor), copy its value to the current node, and then recursively delete the successor node.

#### c) Searching

Finding a node with a given value. In a general tree, this requires a full traversal (e.g., preorder). In a **BST**, the search is highly efficient (`O(log n)` on average), as it compares the value with the root and recursively searches the left or right subtree accordingly.

## Key Points / Summary

| Operation                 | Description                    | Key Use Case                                     |
| :------------------------ | :----------------------------- | :----------------------------------------------- |
| **Preorder Traversal**    | Root -> Left -> Right          | Copying a tree, prefix expressions               |
| **Inorder Traversal**     | Left -> Root -> Right          | Getting sorted order from a BST                  |
| **Postorder Traversal**   | Left -> Right -> Root          | Deleting a tree, postfix expressions             |
| **Level Order Traversal** | Level by Level (Breadth-First) | Finding the shortest path, level-wise operations |
| **Insertion/Deletion**    | Modifies the tree structure    | Building and maintaining a tree                  |
| **Searching**             | Finding a specific node        | Data retrieval, a fundamental operation          |

- Traversal is the basis for most other complex operations on trees.
- The choice of traversal depends entirely on the application (e.g., `Inorder` for BSTs, `Postorder` for deletion).
- Insertion and deletion algorithms must preserve any inherent properties of the tree (e.g., the ordering property of a BST).
- Understanding these operations is a prerequisite for more advanced trees like AVL Trees, Heaps, and B-Trees.
