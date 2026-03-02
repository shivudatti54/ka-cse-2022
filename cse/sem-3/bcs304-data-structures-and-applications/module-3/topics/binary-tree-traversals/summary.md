# Binary Tree Traversals

## Overview

Binary tree traversals visit all nodes exactly once, categorized into Depth-First Traversal (DFS) and Breadth-First Traversal (BFS). DFS includes Inorder, Preorder, and Postorder, while BFS includes Level Order. Each traversal has a specific order and use case.

## Key Points

- Inorder Traversal (LNR): Left → Node → Right, used for sorted output in BST.
- Preorder Traversal (NLR): Node → Left → Right, used to create a copy of the tree.
- Postorder Traversal (LRN): Left → Right → Node, used to delete a tree.
- Level Order Traversal: visits nodes level by level, left to right, using a Queue.
- DFS uses Stack (implicit in recursion), while BFS uses Queue.
- Inorder of BST gives sorted order.
- Preorder root is always first, Postorder root is always last.

## Important Definitions

- **Traversal**: visiting all nodes of a tree exactly once.
- **Depth-First Traversal (DFS)**: traverses the tree depth-first, includes Inorder, Preorder, and Postorder.
- **Breadth-First Traversal (BFS)**: traverses the tree level by level, includes Level Order.

## Key Formulas / Syntax

- Inorder: `inorder(root) { inorder(root->left); print(root->data); inorder(root->right); }`
- Preorder: `preorder(root) { print(root->data); preorder(root->left); preorder(root->right); }`
- Postorder: `postorder(root) { postorder(root->left); postorder(root->right); print(root->data); }`

## Comparisons

| Traversal   | Order      | Use Case                  | Data Structure |
| ----------- | ---------- | ------------------------- | -------------- |
| Inorder     | L-N-R      | Sorted output (BST)       | Stack          |
| Preorder    | N-L-R      | Copy tree, prefix expr    | Stack          |
| Postorder   | L-R-N      | Delete tree, postfix expr | Stack          |
| Level Order | Level-wise | BFS, shortest path        | Queue          |

## Exam Tips

- Focus on the order and use case of each traversal.
- Understand the difference between DFS and BFS.
- Practice constructing a tree from traversals (Preorder + Inorder, Postorder + Inorder).
- Be familiar with the time and space complexity of each traversal.
