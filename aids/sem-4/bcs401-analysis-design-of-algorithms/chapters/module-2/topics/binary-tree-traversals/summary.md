# Binary Tree Traversals - Summary

## Key Definitions and Concepts

- **Binary Tree:** A hierarchical data structure where each node has at most two children (left and right)
- **Root:** The topmost node of the tree with no parent
- **Leaf Node:** A node with no children
- **Subtree:** A tree consisting of a node and all its descendants
- **Depth-first Traversal:** Visits nodes by exploring as far as possible along each branch before backtracking
- **Breadth-first (Level-order) Traversal:** Visits nodes level by level from top to bottom

## Important Formulas and Theorems

- **Time Complexity:** O(n) for all traversals—each node is visited exactly once
- **Space Complexity (Recursive):** O(h) where h is tree height; O(log n) for balanced trees, O(n) for skewed trees
- **Space Complexity (Level-order):** O(w) where w is maximum width of tree
- **Maximum Width:** At most 2^h nodes at any level

## Key Points

- Pre-order (Root-Left-Right): Useful for tree copying, prefix expression evaluation
- In-order (Left-Root-Right): Produces sorted output for Binary Search Trees
- Post-order (Left-Right-Root): Used for deletion, postfix evaluation, directory size calculation
- Level-order: Uses queue data structure, visits level by level
- Recursive traversals are concise but use call stack; iterative versions use explicit data structures
- For n nodes, there are (2n)!/(n+1)! different binary tree shapes (Catalan number)

## Common Mistakes to Avoid

- Confusing traversal orders under exam pressure—always write the sequence step by step
- Forgetting that level-order requires a queue, not a stack
- Not handling empty trees (null) properly in implementations
- Confusing left and right subtree processing order in recursive calls

## Revision Tips

1. Practice drawing at least 5 different trees and writing all four traversal sequences
2. Memorize the recursive template: ROOT LEFT RIGHT for pre-order, LEFT ROOT RIGHT for in-order, LEFT RIGHT ROOT for post-order
3. For iterative traversals, remember: use stack for DFS, use queue for BFS
4. Solve previous year DU question papers to understand exam patterns
5. Focus on in-order traversal for BSTs—this is frequently tested