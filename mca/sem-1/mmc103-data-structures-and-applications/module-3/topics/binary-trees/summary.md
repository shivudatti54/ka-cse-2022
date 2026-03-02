# Binary Trees - Summary

## Key Definitions

- **Binary Tree**: Hierarchical data structure with each node having at most two children (left and right)
- **Root**: Topmost node with no parent
- **Leaf Node**: Node with no children
- **Height**: Longest path from node to leaf (in edges) or number of levels minus one
- **Depth**: Number of edges from root to the node

## Important Formulas

- Maximum nodes in tree of height $h$: $2^{h+1} - 1$
- Maximum nodes at level $i$: $2^i$
- Minimum height for $n$ nodes: $\lfloor \log_2 n \rfloor$
- Full binary tree: Leaf nodes = Internal nodes + 1
- Array representation indices: Left = $2i+1$, Right = $2i+2$, Parent = $\lfloor (i-1)/2 \rfloor$

## Key Points

1. Binary trees are fundamental to understanding advanced tree structures like BST, AVL, and heaps
2. A full binary tree has nodes with either 0 or 2 children; a complete tree fills levels left-to-right
3. Perfect binary trees have all leaves at the same level with maximum nodes
4. Degenerate trees degrade to linked list performance (O(n) for all operations)
5. Linked representation allows dynamic size; array representation is memory-efficient for complete trees
6. Height and depth are often confused - height measures downward from node, depth measures upward from root
7. The root is conventionally at depth/level 0, not level 1

## Common Mistakes

1. Confusing height (edges) with level (nodes) - height of single node tree is 0, not 1
2. Using $2^h$ instead of $2^{h+1} - 1$ for maximum nodes formula
3. Forgetting that array representation wastes space for non-complete trees
4. Misidentifying tree type - a complete tree is not necessarily full
5. Calculating depth incorrectly by starting from 1 instead of 0
