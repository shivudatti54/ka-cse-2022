# Binary Trees and Traversals - Summary

## Key Definitions and Concepts

- **Binary Tree**: A hierarchical data structure where each node has at most two children (left and right)
- **Leaf Node**: A node with no children (external node)
- **Internal Node**: A node with at least one child
- **Height**: Longest path from root to a leaf; depth is the reverse (root to node)
- **Full Binary Tree**: Every node has 0 or 2 children (never 1)
- **Complete Binary Tree**: All levels filled except possibly last, nodes as far left as possible
- **Perfect Binary Tree**: All internal nodes have 2 children, all leaves at same level
- **Traversal**: Systematic visiting of all nodes in a tree

## Important Formulas and Theorems

- **Maximum nodes in tree of height h**: 2^(h+1) - 1
- **Minimum height for n nodes**: ⌊log₂n⌋
- **In a complete binary tree (array)**: Left child at 2i+1, Right child at 2i+2, Parent at ⌊(i-1)/2⌋
- **All traversals**: Time complexity = O(n), Space = O(h) where h = height
- **Balanced tree**: h = O(log n); Skewed tree: h = O(n)

## Key Points

1. **Inorder (LNR)**: Left → Root → Right → Produces sorted output for BSTs
2. **Preorder (NLR)**: Root → Left → Right → Useful for copying trees, prefix expressions
3. **Postorder (LRN)**: Left → Right → Root → Used for deleting trees, postfix expressions
4. **Level Order**: Level by level (Breadth-First) → Uses queue data structure
5. Recursive traversals use implicit call stack; iterative versions use explicit data structures
6. Inorder of BST always gives ascending order - used for validation
7. Two traversals (one must be inorder) are needed to uniquely construct a tree
8. Expression trees: Inorder gives infix, Preorder gives prefix, Postorder gives postfix notation

## Common Mistakes to Forget

1. **Confusing traversal orders**: Students often mix up when root is visited in preorder vs postorder
2. **Forgetting base case**: Recursive traversals must check for NULL/empty tree
3. **Stack overflow**: Recursive approaches can fail on skewed trees with large n
4. **Wrong child order**: Always process left before right (unless specified otherwise)
5. **Ignoring space complexity**: Only counting time, not stack/queue space

## Revision Tips

1. **Practice drawing**: For any traversal question, draw the tree first, then trace through
2. **Mnemonics help**: L-N-R (In), N-L-R (Pre), L-R-N (Post) - remember "L" comes before "N" comes before "R" in each
3. **Know the applications**: Link each traversal to its use case (BST sorted = inorder, delete tree = postorder)
4. **Master complexity analysis**: Be able to derive O(n) time and O(h) space for all traversals
5. **Solve previous year questions**: DU exams frequently ask traversal outputs and tree construction