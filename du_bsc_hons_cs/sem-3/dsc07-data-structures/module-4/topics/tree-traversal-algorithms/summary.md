# Tree Traversal Algorithms - Summary

## Key Definitions and Concepts

- **Tree Traversal**: A method of visiting all nodes of a tree data structure exactly once in a systematic manner
- **Binary Tree**: A tree where each node has at most two children (left and right)
- **Depth-First Search (DFS)**: Traversals that explore as deep as possible along each branch before backtracking
- **Breadth-First Search (BFS)**: Traversals that explore level by level, visiting all nodes at current depth before moving deeper

## Important Formulas and Theorems

| Traversal Type | Order | Data Structure | Primary Use |
|---------------|-------|----------------|-------------|
| Preorder | Root → Left → Right | Stack | Directory serialization, prefix expression |
| Inorder | Left → Root → Right | Stack | BST sorted output, infix expression |
| Postorder | Left → Right → Root | Stack | Expression evaluation, tree deletion |
| Level Order | By levels, left to right | Queue | Shortest path, level-wise processing |

**Complexity**: Time O(n), Space O(h) where n = nodes, h = height

**BST Theorem**: Inorder traversal of a Binary Search Tree always produces elements in ascending order.

## Key Points

- Preorder: Root visited first—useful when root must be processed before children
- Inorder: Produces sorted output for BSTs—most common for binary search tree operations
- Postorder: Root visited last—essential for postfix expression evaluation and memory cleanup
- Level Order: Uses queue (FIFO) unlike DFS traversals which use stack (LIFO)
- Recursive traversals are elegant but use system call stack; iterative versions use explicit data structures
- Height of tree determines space complexity—O(log n) for balanced, O(n) for skewed trees

## Common Mistakes to Avoid

- Confusing the order of operations in different traversals—always verify before writing code
- Forgetting the base case (null check) in recursive implementations, causing infinite recursion
- Using stack for level order instead of queue—this produces incorrect (zigzag) order
- Assuming all traversals produce different outputs—some trees may produce identical sequences for different traversals

## Revision Tips

1. **Practice tracing**: Draw small trees (5-7 nodes) and manually trace each traversal type
2. **Mnemonic记忆**: Use "Root Left Right" for Preorder, "Left Root Right" for Inorder, "Left Right Root" for Postorder
3. **Compare implementations**: Study recursive vs iterative versions side-by-side to understand the stack mechanics
4. **Know applications**: Link each traversal to its real-world use case—expression trees, file systems, game AI