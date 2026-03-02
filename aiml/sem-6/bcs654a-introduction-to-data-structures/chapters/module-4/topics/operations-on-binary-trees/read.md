# Module 4: Operations on Binary Trees

## Introduction

A Binary Tree is a fundamental hierarchical data structure where each node has at most two children, referred to as the left child and the right child. Understanding the operations that can be performed on this structure is crucial, as these operations form the backbone of more complex algorithms used in database systems, compilers, and search applications. This module explores the core traversal, insertion, and deletion operations.

## Core Concepts and Operations

### 1. Tree Traversals

Tree traversal is the process of visiting each node in a tree exactly once in a specific order. Unlike linear data structures, trees can be traversed in multiple ways.

*   **Inorder Traversal (Left-Root-Right):**
    1.  Traverse the left subtree recursively.
    2.  Visit the root node.
    3.  Traverse the right subtree recursively.
    *   **Result:** For a Binary Search Tree (BST), this traversal yields nodes in non-decreasing order.
    *   **Example:** For the tree `[A, B, C]` (where B is left child, C is right child), the inorder traversal is `B -> A -> C`.

*   **Preorder Traversal (Root-Left-Right):**
    1.  Visit the root node.
    2.  Traverse the left subtree recursively.
    3.  Traverse the right subtree recursively.
    *   **Use Case:** Often used to create a copy of the tree or to get a prefix expression of an expression tree.
    *   **Example:** For the tree `[A, B, C]`, the preorder traversal is `A -> B -> C`.

*   **Postorder Traversal (Left-Right-Root):**
    1.  Traverse the left subtree recursively.
    2.  Traverse the right subtree recursively.
    3.  Visit the root node.
    *   **Use Case:** Used to delete the tree (because you delete children before the parent) or to get a postfix expression.
    *   **Example:** For the tree `[A, B, C]`, the postorder traversal is `B -> C -> A`.

*   **Level Order Traversal:**
    This traversal visits nodes level by level, from top to bottom and left to right.
    *   **Implementation:** It uses a **Queue** data structure (FIFO) instead of recursion.
    *   **Steps:**
        1.  Enqueue the root node.
        2.  While the queue is not empty:
            *   Dequeue a node and visit it.
            *   Enqueue its left child (if exists).
            *   Enqueue its right child (if exists).

### 2. Insertion in a Binary Tree

Insertion is typically done in a level-order fashion to maintain a complete or nearly complete tree, ensuring minimal height.

**Algorithm (Level Order Insertion):**
1.  If the tree is empty, create the new node as the root.
2.  Else, perform a level order traversal until we find the first node that has an empty child spot (either left or right).
3.  Insert the new node at that empty spot.

**Example:**
Inserting `D` into the tree `[A, B, C]` (where `B` and `C` are children of `A`).
*   Start at root `A`. It has both children.
*   Move to next level, first node `B`. It has no left child. Insert `D` as the left child of `B`.
*   The new tree structure is `A (B (D, -), C)`.

### 3. Deletion in a Binary Tree

The goal is to delete a given node while preserving the tree's structure. The algorithm ensures the tree doesn't become fragmented.

**Algorithm:**
1.  Find the node to be deleted (e.g., `targetNode`).
2.  Find the deepest node in the tree (the last node in the level order traversal). Let's call it `deepestNode`.
3.  Replace the data in `targetNode` with the data in `deepestNode`.
4.  Delete the `deepestNode`.

This approach efficiently removes the desired node by replacing it with the deepest node, which can then be easily removed without affecting the rest of the tree's hierarchy.

**Example:**
Delete node `B` from the tree `A (B (D, E), C)`.
1.  `targetNode` is `B`.
2.  The deepest node is `E`.
3.  Replace `B`'s data with `E`'s data. The tree becomes `A (E (D, E), C)`.
4.  Now, delete the leaf node `E` that was the deepest node. The final tree is `A (E (D), C)`.

## Key Points / Summary

| Operation         | Key Idea                                                                                             | Common Method/Order                              |
| :---------------- | :--------------------------------------------------------------------------------------------------- | :----------------------------------------------- |
| **Traversal**     | Visiting every node in a specific sequence.                                                          | Inorder (LNR), Preorder (NLR), Postorder (LRN), Level Order |
| **Inorder**       | Processes nodes in a sorted order for BSTs.                                                          | Left -> Root -> Right                           |
| **Preorder**      | Useful for copying a tree's structure.                                                               | Root -> Left -> Right                           |
| **Postorder**     | Necessary for safe deletion (children first).                                                        | Left -> Right -> Root                           |
| **Level Order**   | Uses a Queue; visits nodes by depth level.                                                           | Breadth-First Search (BFS)                       |
| **Insertion**     | Adds a new node.                                                                                     | Typically inserted at the first available position in level order to keep the tree balanced. |
| **Deletion**      | Removes a node while maintaining tree continuity.                                                     | Replace target node with the deepest node, then delete the deepest node. |

Mastering these operations is essential for implementing efficient algorithms on tree-based data structures like Binary Search Trees, AVL Trees, and Heaps.