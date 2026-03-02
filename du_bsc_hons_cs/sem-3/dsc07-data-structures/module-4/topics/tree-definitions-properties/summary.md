# Tree Definitions and Properties - Summary

## Key Definitions and Concepts

- **Tree**: A hierarchical data structure consisting of nodes connected by edges, with exactly one root and no cycles
- **Node**: An element containing data and pointers to its children
- **Root**: The topmost node with no parent
- **Leaf Node**: A node with no children (degree 0)
- **Internal Node**: A node with at least one child
- **Parent/Child**: A node above another node is its parent; nodes below are children
- **Sibling**: Nodes sharing the same parent
- **Ancestor/Descendant**: Any node on the path from root to a node is its ancestor; any node in its subtree is a descendant

## Important Formulas and Theorems

- **Edges in a tree**: For n nodes, edges = n - 1
- **Maximum nodes at level L**: 2^L (for binary tree, root at level 0)
- **Maximum nodes in tree of height H**: 2^(H+1) - 1
- **Leaf-Internal Node Relationship**: For non-empty binary tree: Leaf nodes = Internal nodes with 2 children + 1

## Key Points

1. Trees are non-linear data structures representing hierarchical relationships
2. A tree with n nodes always has exactly n-1 edges (no cycles)
3. Height measures from node downward; depth measures from root upward
4. Binary tree: each node has at most 2 children
5. Full binary tree: every node has 0 or 2 children (never 1)
6. Complete binary tree: all levels filled except possibly last, nodes left-justified
7. Perfect binary tree: all internal nodes have 2 children, all leaves at same level
8. Complete binary trees are efficiently represented using arrays
9. There is exactly one path between any two nodes in a tree

## Common Mistakes to Avoid

1. Confusing height with depth—height goes downward from node, depth goes upward from root
2. Confusing full binary tree with complete binary tree—they are different definitions
3. Forgetting that a single node tree has height 0 (or 1 depending on convention) but 0 edges
4. Not understanding that a tree must be acyclic—any cycle makes it a graph, not a tree
5. Incorrectly counting leaf nodes—only nodes with zero children are leaves

## Revision Tips

1. Draw different tree types and label all components to reinforce terminology
2. Practice calculating height, depth, and edges from tree diagrams
3. Memorize the relationship: n nodes → n-1 edges
4. Remember: perfect → full + all leaves same level → complete
5. Solve previous year DU questions on tree properties for exam pattern