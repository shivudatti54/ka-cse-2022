# Basic Concepts of Trees - Summary

## Key Definitions and Concepts

- **Tree**: A hierarchical data structure with one root node and n disjoint subtrees, where each node has exactly one parent (except root) and zero or more children
- **Root**: The topmost node with no parent
- **Leaf Node**: A node with no children (degree 0)
- **Internal Node**: A node with at least one child
- **Sibling Nodes**: Nodes sharing the same parent
- **Ancestors**: All nodes on the path from root to a given node
- **Descendants**: All nodes that have the given node as an ancestor
- **Subtree**: A node and all its descendants form a subtree

## Important Formulas and Theorems

- **Edge Count**: A tree with n nodes always has exactly (n-1) edges
- **Binary Tree Array Indexing**: For node at index i - Left child = 2i, Right child = 2i+1, Parent = floor(i/2)
- **Full Binary Tree Property**: If L = number of leaf nodes, then total nodes n = 2L - 1
- **Height Calculation**: Maximum possible height for n nodes = n - 1; Minimum height = log₂(n) + 1

## Key Points

1. Trees are non-linear data structures organizing data hierarchically
2. Every node except the root has exactly one parent; a node can have zero or more children
3. A tree with n nodes always has n-1 edges (this is a fundamental invariant)
4. Level/depth starts from the root - typically root is at level 1 in DU curriculum
5. Height of tree = maximum level of any node; height of single node tree = 1
6. Binary trees restrict each node to maximum 2 children (left and right)
7. Complete binary trees use efficient array representation with no wasted space
8. Perfect binary trees have all leaf nodes at same level and 2^k - 1 nodes for height k
9. Forest = collection of disjoint trees (formed by removing root from a tree)

## Common Mistakes to Avoid

1. Confusing height with depth - height measures from node to deepest leaf, depth measures from root to node
2. Forgetting that a leaf node has degree 0, not degree 1
3. Assuming tree height can be 0 - minimum tree height is 1 (for single node)
4. Confusing complete vs full vs perfect binary trees - they are different concepts

## Revision Tips

1. Draw various tree structures and label all components to reinforce terminology
2. Practice identifying relationships (parent-child, sibling, ancestor-descendant) on drawn trees
3. Memorize the key property: n nodes = n-1 edges always
4. Remember array representation formulas for binary trees - frequently tested
5. For exam, always draw the tree first before answering any questions about it