# Binary Trees

## Overview

A binary tree is a hierarchical data structure where each node has at most two children, referred to as the left child and the right child. Binary trees are used in many computational problems due to their strict limitation on the number of children per node. They can be empty or consist of a root node with exactly two subtrees.

## Key Points

- A binary tree is either empty or consists of a root node with left and right subtrees.
- Each node in a binary tree has at most two children (left child and right child).
- Types of binary trees include Full, Complete, Perfect, Degenerate, and Balanced trees.
- Binary tree traversals include Depth-First Traversals (Pre-order, In-order, Post-order) and Breadth-First Traversal (Level Order).
- A binary search tree (BST) is a binary tree where the left subtree of a node contains only nodes with keys less than the node's key, and the right subtree contains only nodes with keys greater than the node's key.
- Operations on BST include search, insertion, and deletion with O(h) time complexity.

## Important Definitions

- **Root**: The topmost node in the tree.
- **Parent**: A node that has one or more children.
- **Child**: Nodes directly connected below a parent node.
- **Leaf**: A node with no children.
- **Internal node**: A node with at least one child.
- **Depth**: The number of edges from the root to the node.
- **Height**: The number of edges on the longest path from the node to a leaf.
- **Level**: All nodes at the same depth.

## Key Formulas / Syntax

- Maximum number of nodes at level i: 2^i
- Maximum number of nodes in a tree of height h: 2^(h+1)-1
- Minimum height for n nodes: ⌈log₂(n+1)⌉-1
- Node structure: `struct Node { int data; struct Node* left; struct Node* right; };`

## Comparisons

| Type of Tree                   | Description                                                                        | Example                    |
| ------------------------------ | ---------------------------------------------------------------------------------- | -------------------------- |
| Full Binary Tree               | Every node has either 0 or 2 children.                                             | A binary tree with 3 nodes |
| Complete Binary Tree           | All levels are completely filled except possibly the last level.                   | A binary tree with 4 nodes |
| Perfect Binary Tree            | All internal nodes have exactly two children and all leaves are at the same level. | A binary tree with 7 nodes |
| Degenerate (Pathological) Tree | Each parent node has only one associated child node.                               | A linked list              |
| Balanced Binary Tree           | The height of the left and right subtrees of any node differ by at most 1.         | A binary tree with 5 nodes |

## Exam Tips

- Remember traversal orders: NLR (Pre-order), LNR (In-order), LRN (Post-order)
- Verify BST properties: left child < parent < right child for all nodes
- Calculate height for a complete binary tree with n nodes: ⌊log₂n⌋
- Practice drawing trees from traversal sequences
- Remember time complexity: balanced trees have O(log n) operations while degenerate trees have O(n) operations
- Be prepared to explain real-world uses of binary trees with specific examples
