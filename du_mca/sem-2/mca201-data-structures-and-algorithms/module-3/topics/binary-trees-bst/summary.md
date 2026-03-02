# Binary Trees and Binary Search Trees - Summary

## Key Definitions and Concepts

- **Binary Tree**: A hierarchical structure where each node has at most two children (left and right)
- **Binary Search Tree (BST)**: A binary tree with ordering property - left subtree contains smaller values, right subtree contains larger values
- **Tree Height**: Longest path from root to leaf (single node has height 1)
- **Complete Binary Tree**: All levels filled except possibly last, nodes left-aligned
- **Full Binary Tree**: Every node has 0 or 2 children
- **Inorder Successor**: Smallest value in right subtree (used in deletion)
- **Inorder Predecessor**: Largest value in left subtree (alternative for deletion)

## Important Formulas and Theorems

- Maximum nodes in tree of height h: 2^h - 1 (full binary tree)
- Minimum nodes in tree of height h: h (skewed tree)
- Minimum height with n nodes: ⌊log₂(n)⌋ + 1
- BST Search/Insert/Delete: O(h) where h = height
- Balanced BST: O(log n), Skewed BST: O(n)
- Traversal time complexity: O(n)

## Key Points

- Inorder traversal of BST produces sorted ascending order
- Preorder: Root → Left → Right (useful for copying trees, prefix expressions)
- Postorder: Left → Right → Root (useful for deletion, postfix evaluation)
- Level order: Uses queue, visits level by level (left to right)
- BST deletion: Case 1 (leaf) - remove directly; Case 2 (1 child) - bypass node; Case 3 (2 children) - replace with inorder successor, delete successor
- Sequential representation: For node at index i, left child = 2i+1, right child = 2i+2 (0-based indexing)
- Recursive traversals use O(h) space due to call stack

## Common Mistakes to Avoid

- Confusing tree height (edges) with number of nodes - be consistent with definitions
- Forgetting that BST requires unique keys - duplicate handling must be specified
- Not handling null/base cases in recursive functions
- In deletion case 3, forgetting to delete the inorder successor node after replacing value
- Assuming O(log n) for BST operations - only true for balanced trees

## Revision Tips

1. Practice constructing BSTs from sequences - this is the most frequently tested concept
2. Memorize traversal outputs for given trees - can be verified by tracing algorithm
3. For deletion, draw the tree at each step - visual understanding prevents errors
4. Remember that height affects space complexity in recursive solutions
5. Solve at least 5-10 previous year exam questions on tree traversals and BST operations