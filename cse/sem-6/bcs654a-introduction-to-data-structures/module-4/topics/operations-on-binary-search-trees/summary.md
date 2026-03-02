# Operations on Binary Search Trees

## Overview

BST operations leverage the ordering property for efficient data manipulation including search, insertion, deletion, and finding minimum/maximum values. All operations maintain the BST property that left < root < right.

## Key Points

- **Search**: Compare target with node, go left if smaller, right if larger, O(h) time
- **Insertion**: Find appropriate position using search, insert as leaf node, O(h)
- **Deletion**: Three cases based on children count (0, 1, or 2 children)
- **Find Minimum**: Traverse leftmost path from root
- **Find Maximum**: Traverse rightmost path from root
- **BST Property Maintenance**: All operations must preserve left < root < right ordering
- **Height Dependency**: All operations take O(h) where h is tree height

## Important Concepts

- Search terminates when value found or NULL reached
- Insertion always adds new node as leaf
- Delete leaf: simply remove node
- Delete with one child: replace node with its child
- Delete with two children: replace with inorder successor, then delete successor
- Inorder successor is minimum value in right subtree
- Balanced tree ensures h = O(log n) for all operations

## Notes

- Practice all three deletion cases thoroughly
- Understand recursive and iterative implementations
- Know how to find inorder successor and predecessor
- Be able to trace operations showing tree changes
- Remember to maintain BST property after modifications
