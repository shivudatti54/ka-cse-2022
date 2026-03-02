# Binary Search Trees (BST)

## Overview

A Binary Search Tree is a binary tree where for each node, all values in left subtree are smaller and all values in right subtree are larger. This ordering property enables efficient O(log n) search, insert, and delete operations when tree is balanced.

## Key Points

- **BST Property**: For every node, left subtree values < node value < right subtree values
- **Search Efficiency**: O(log n) average case, O(h) where h is tree height
- **Insertion**: Compare with nodes starting from root, insert at appropriate leaf position
- **Deletion Cases**: Leaf node (simple), one child (replace with child), two children (replace with successor/predecessor)
- **Inorder Traversal**: Produces sorted sequence of values
- **Balanced BST**: Height remains O(log n) ensuring efficient operations
- **Degenerate Case**: Skewed tree behaves like linked list with O(n) operations

## Important Concepts

- BST property must be maintained after every insertion and deletion
- Search follows left or right based on comparison with node value
- Inorder successor is leftmost node in right subtree
- Inorder predecessor is rightmost node in left subtree
- Deleting node with two children requires finding and replacing with successor
- Self-balancing BSTs (AVL, Red-Black) prevent degeneration

## Notes

- Practice inserting and deleting with all three cases
- Understand why inorder traversal gives sorted output
- Know how to find min (leftmost) and max (rightmost) nodes
- Be able to trace search path through BST
- Remember worst case occurs with sorted input creating skewed tree
