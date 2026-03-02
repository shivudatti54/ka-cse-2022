# Binary Tree Traversals - Summary

## Key Definitions and Concepts

- Binary tree traversal is the systematic process of visiting each node in a binary tree exactly once
- A binary tree consists of nodes with at most two children: left child and right child
- "Visiting" a node means performing an operation such as printing, updating, or checking its value

## Important Formulas and Theorems

- Time complexity for all traversals: O(n) where n is the number of nodes
- Space complexity for recursive traversals: O(h) where h is tree height
- Space complexity for level order: O(w) where w is maximum tree width
- In worst case (skewed tree): O(n) space for recursive; O(n) for level order if tree is complete

## Key Points

- INORDER (Left-Root-Right): Produces sorted output for Binary Search Trees; used for inorder successor operations
- PREORDER (Root-Left-Right): Ideal for tree copying, serializing tree structure, and prefix notation
- POSTORDER (Left-Right-Root): Essential for postfix evaluation, tree deletion, and computing aggregate child values
- LEVEL ORDER: Uses queue data structure; visits nodes level by level; required for breadth-first operations

## Common Mistakes to Avoid

- Confusing the order of operations in different traversals—students often mix up preorder and postorder sequences
- Forgetting the base case in recursive implementations, leading to infinite recursion
- Neglecting to handle empty trees (NULL root) in implementation questions
- Confusing when to process the root relative to its subtrees in recursive implementations

## Revision Tips

- Practice drawing at least 10 different trees and writing all four traversals for each
- Memorize the mnemonic "L R Root" for inorder, "Root L R" for preorder, "L R Root" for postorder
- Understand the stack operations in iterative inorder traversal thoroughly as it frequently appears in exams
- Focus on applications—knowing why each traversal exists helps remember the differences