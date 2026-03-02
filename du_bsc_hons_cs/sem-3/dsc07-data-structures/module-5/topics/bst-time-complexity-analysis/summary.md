# Binary Search Tree (BST) - Time Complexity Analysis - Summary

## Key Definitions and Concepts

- **Binary Search Tree (BST)**: A binary tree where each node has at most two children, with the property that all left subtree nodes have keys less than the root, and all right subtree nodes have keys greater.

- **Tree Height (h)**: The length of the longest path from root to leaf, determining the worst-case number of operations.

- **Balanced BST**: A BST where the height is approximately log₂n, ensuring O(log n) operations.

- **Skewed BST**: A degenerate tree where each node has only one child, resulting in O(n) operations.

## Important Formulas and Theorems

- **Search/Insert/Delete Time**: T(n) = O(h)
  - Best Case: O(log n) - balanced tree
  - Average Case: O(log n) - random insertions
  - Worst Case: O(n) - skewed tree

- **Height-Node Relationship**:
  - Balanced: h ≈ log₂n
  - Skewed: h = n-1

- **Traversal Time**: O(n) - visits every node once
- **Space Complexity**: O(n) for storage, O(h) for recursion stack

## Key Points

- All basic operations (search, insert, delete) depend on tree height h
- Average case assumes roughly balanced distribution of keys
- Worst case occurs with sorted/nearly-sorted data insertions
- Deletion with two children requires finding in-order successor (O(h) additional)
- Perfect/complete BST provides guaranteed O(log n) performance
- Self-balancing trees (AVL, Red-Black) maintain O(log n) even with worst-case input

## Common Mistakes to Avoid

- Confusing O(log n) with O(1)—BST operations are never constant time
- Forgetting that traversal is always O(n), regardless of tree balance
- Assuming worst case won't happen—sorted input produces worst case
- Mixing up space and time complexity in analysis

## Revision Tips

1. Practice tracing search/insert/delete operations on small trees (5-7 nodes)
2. Draw both balanced and skewed trees for the same data to compare operations
3. Memorize the three deletion cases and practice each with examples
4. Remember: height determines complexity, balance determines height
5. Solve previous year DU exam questions on BST complexity analysis