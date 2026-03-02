# Tree Definitions and Traversals - Summary

## Key Definitions and Concepts

- **Tree**: A hierarchical data structure with nodes connected by edges, having one root node (if non-empty)
- **Binary Tree**: A tree where each node has at most two children (left and right)
- **Node**: Contains data and pointers to left and right children
- **Leaf Node**: A node with no children
- **Height**: Maximum level of any node in the tree
- **Traversal**: Systematic way of visiting each node exactly once

## Important Formulas and Theorems

- **Maximum nodes in binary tree of height h**: 2^(h+1) - 1
- **Leaf node relationship**: n0 = n2 + 1 (where n0 = leaf nodes, n2 = nodes with degree 2)
- **Array representation**: Parent at (i-1)/2, Left child at 2i+1, Right child at 2i+2
- **Time Complexity**: O(n) for all traversals
- **Space Complexity**: O(h) for recursive, O(w) for level order

## Key Points

1. Preorder (Root-Left-Right): Root visited first - useful for tree copying
2. Inorder (Left-Root-Right): Root in middle - gives sorted output for BST
3. Postorder (Left-Right-Root): Root visited last - useful for deletion
4. Level Order: Uses queue, visits level by level
5. Complete binary tree: All levels filled except possibly last, nodes left-aligned
6. Perfect binary tree: All internal nodes have 2 children, all leaves at same level
7. Tree traversals are recursive by nature
8. Array representation is efficient only for complete binary trees

## Common Mistakes to Avoid

1. Confusing preorder with inorder - remember the position of root relative to subtrees
2. Forgetting the base case in recursive traversals (checking for NULL)
3. Using wrong data structure for level order (must use queue, not stack)
4. Incorrect array indexing for parent/child relationships
5. Not understanding that tree height can be defined as node count or edge count (be consistent)

## Revision Tips

1. Practice drawing trees from given traversal sequences - this is frequently tested in DU exams
2. Write traversal algorithms by hand multiple times to reinforce understanding
3. Memorize the relationship n0 = n2 + 1 - it appears in numerical problems
4. Understand that different traversals of the same tree produce different output sequences
5. Know that inorder + any other traversal can uniquely reconstruct a binary tree
6. Complete binary trees have efficient array representation - remember the indexing formulas