# Insertion, Traversals, Searching, Copying a Tree

## Overview

Core binary tree operations include inserting nodes, traversing in different orders, searching for values, and creating tree copies. These operations demonstrate fundamental tree manipulation techniques and recursive algorithms.

## Key Points

- **Insertion**: Add new node at appropriate position maintaining tree structure
- **Traversals**: Preorder, inorder, postorder visit nodes in different sequences
- **Searching**: Locate node with specific value by traversing tree
- **Copying Tree**: Create duplicate tree preserving structure and data
- **Recursive Implementation**: Most operations naturally implemented using recursion
- **Time Complexity**: O(n) for traversal and copying, O(h) for search where h is height
- **Applications**: Each operation serves specific purposes in tree manipulation

## Important Concepts

- Insertion in general binary tree adds node at first available position
- Preorder: process root, traverse left, traverse right
- Inorder: traverse left, process root, traverse right
- Postorder: traverse left, traverse right, process root
- Tree copying uses preorder traversal creating new nodes
- Searching compares node values during traversal

## Notes

- Practice writing code for all operations recursively
- Understand base case and recursive case for each operation
- Know traversal output sequences for given trees
- Be able to trace copying operation step by step
- Remember copying creates entirely new tree with same structure