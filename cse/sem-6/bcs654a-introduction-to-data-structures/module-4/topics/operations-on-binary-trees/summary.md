# Operations on Binary Trees

## Overview

Binary tree operations include insertion, deletion, traversal, searching, and manipulation functions. Traversal methods (preorder, inorder, postorder, level-order) are fundamental to processing tree data in specific orders.

## Key Points

- **Insertion**: Add nodes maintaining tree structure, typically at available position
- **Deletion**: Remove node and restructure tree preserving properties
- **Traversal Methods**: Preorder (Root-Left-Right), Inorder (Left-Root-Right), Postorder (Left-Right-Root)
- **Level-Order**: Visit nodes level by level using queue
- **Searching**: Find node by traversing tree comparing values
- **Height Calculation**: Recursive function finding maximum path to leaf
- **Node Counting**: Count total nodes, leaf nodes, or internal nodes

## Important Concepts

- Inorder traversal of BST produces sorted sequence
- Preorder useful for creating copy of tree
- Postorder used for deleting tree or postfix expression evaluation
- Level-order requires queue data structure
- All traversals can be implemented recursively or iteratively
- Time complexity O(n) for traversals visiting all n nodes

## Notes

- Practice all four traversal methods on sample trees
- Understand recursive nature of tree operations
- Know applications of each traversal type
- Be able to write traversal outputs for given trees
- Master both recursive and iterative implementations
