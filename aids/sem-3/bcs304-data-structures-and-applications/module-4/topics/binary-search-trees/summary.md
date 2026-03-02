# Binary Search Trees - Summary

## Key Definitions

- **Binary Search Tree (BST)**: A binary tree where each node's key is greater than all keys in its left subtree and less than all keys in its right subtree
- **Tree Height**: The number of edges on the longest path from a node to a leaf; empty tree height = -1
- **Node Successor**: The smallest key greater than the current node's key
- **Node Predecessor**: The largest key smaller than the current node's key
- **Balanced BST**: A BST where height is O(log n), ensuring O(log n) operations

## Important Formulas

- **Search Time**: T(n) = O(h), where h is tree height
- **Balanced Height**: h = Θ(log n)
- **Worst-case Height**: h = n - 1 (degenerate tree)
- **Expected Height**: O(log n) for randomly built BST
- **Inorder Successor**: Minimum node in right subtree OR lowest ancestor where current node is in left subtree

## Key Points

1. BST property enables binary search principle at O(log n) average time
2. Operations (search, insert, delete) all require O(h) time
3. Balanced trees maintain h = O(log n), achieving consistent performance
4. Inorder traversal always produces sorted output
5. Sorted input creates degenerate tree with O(n) performance - the critical vulnerability
6. Deletion with two children requires successor replacement
7. BSTs support order-statistic operations (find kth smallest) efficiently
8. Recursive implementations require O(h) stack space; iterative versions use O(1) space

## Common Mistakes

1. **Confusing tree height with node depth**: Height measures from node downward; depth measures from root upward
2. **Forgetting the two-child deletion case**: Simply removing the node corrupts tree structure
3. **Assuming O(log n) always**: Without balance enforcement, worst-case is O(n)
4. **Incorrect successor/predecessor logic**: When right/left subtree is empty, must traverse ancestors
5. **Off-by-one errors in height calculation**: Single node has height 0, empty tree has height -1 (or 0 depending on convention)
6. **Ignoring duplicate key handling**: BST definition must specify whether duplicates are allowed and where they go
