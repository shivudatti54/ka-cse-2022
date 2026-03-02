# Rooted and Binary Trees - Summary

## Key Definitions and Concepts

- **Tree**: A connected acyclic graph with n vertices and n-1 edges
- **Rooted Tree**: A tree with a distinguished root vertex giving hierarchical direction
- **Binary Tree**: A rooted tree where each node has at most two children (left and right)
- **Leaf Node**: A node with no children
- **Internal Node**: A node with at least one child
- **Level/Depth**: Distance from root to a node (root at level 0)
- **Height**: Maximum level of any node in the tree

## Important Formulas and Theorems

- **Tree edge count**: For n vertices, edges = n - 1
- **Complete binary tree height**: h = floor(log₂n)
- **Maximum nodes at level h**: 2^h
- **Maximum nodes in tree of height h**: 2^(h+1) - 1
- **Leaves in complete binary tree**: ceil(n/2)
- **Spanning tree edges**: n - 1 (for n vertices)
- **Cycle graph Cₙ spanning trees**: n

## Key Points

- Binary trees enable O(log n) search in balanced configurations
- Full binary tree: every node has 0 or 2 children
- Complete binary tree: filled left to right, enables array representation
- Perfect binary tree: all levels filled, all leaves at same level
- Inorder traversal of BST produces sorted sequence
- Preorder: root first (useful for copying trees)
- Postorder: root last (useful for deleting trees)
- Level order uses queue data structure

## Common Mistakes to Confuse

- Confusing complete with full binary trees (they are different)
- Forgetting that tree height may be defined as number of edges or nodes from root to deepest leaf
- Confusing preorder (root-first) with inorder (root in middle)
- Not remembering that binary search tree requires left < root < right property

## Revision Tips

- Practice drawing trees from traversal sequences
- Memorize the traversal algorithms and their use cases
- Remember: tree with n vertices = n-1 edges = connected + acyclic
- For exam problems, always start with the fundamental property: n vertices → n-1 edges
- Work through previous year university questions on tree traversals and properties
