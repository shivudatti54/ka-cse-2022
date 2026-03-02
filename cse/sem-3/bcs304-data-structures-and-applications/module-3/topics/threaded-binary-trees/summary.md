# Threaded Binary Trees

## Overview

Threaded binary trees replace NULL pointers with threads (pointers to inorder predecessor/successor) to optimize memory usage and traversal. This data structure is useful when frequent inorder traversal is needed.

## Key Points

- A binary tree with n nodes has n + 1 NULL pointers, which can be replaced by threads.
- Threads are pointers to the inorder predecessor or successor of a node.
- There are three types of threaded binary trees: right-threaded, left-threaded, and fully threaded.
- A header node is used to handle boundary cases (leftmost and rightmost nodes).
- Inorder traversal of a threaded binary tree can be done without a stack or recursion.
- Insertion and deletion in a threaded binary tree are more complex due to thread maintenance.

## Important Definitions

- **Thread**: A pointer to the inorder predecessor or successor of a node.
- **Header Node**: A sentinel node used to handle boundary cases in a threaded binary tree.
- **Right-Threaded Binary Tree**: A threaded binary tree where right child pointers are replaced by threads.
- **Left-Threaded Binary Tree**: A threaded binary tree where left child pointers are replaced by threads.
- **Fully Threaded Binary Tree**: A threaded binary tree where both left and right child pointers are replaced by threads.

## Key Formulas / Syntax

- Total pointer fields in a binary tree with n nodes: 2n
- NULL pointers in a binary tree with n nodes: n + 1
- Node structure in C: `typedef struct ThreadedNode { int data; struct ThreadedNode *left; struct ThreadedNode *right; int lthread; int rthread; } ThreadedNode;`

## Comparisons

| Feature                   | Regular Binary Tree      | Threaded Binary Tree     |
| ------------------------- | ------------------------ | ------------------------ |
| NULL pointers             | n + 1                    | 0                        |
| Inorder traversal         | Needs stack or recursion | Uses threads, O(1) space |
| Finding inorder successor | O(h)                     | O(1) if rthread == 1     |
| Node structure            | 3 fields                 | 5 fields                 |
| Insertion complexity      | O(h)                     | O(h) but more code       |

## Exam Tips

- Be prepared to prove the NULL pointer count formula.
- Practice drawing threaded binary trees and labeling threads.
- Know the node structure and inorder traversal algorithm by heart.
- Understand the purpose of the header node and how to insert new nodes while maintaining thread correctness.
- Be familiar with the advantages and disadvantages of threaded binary trees.
