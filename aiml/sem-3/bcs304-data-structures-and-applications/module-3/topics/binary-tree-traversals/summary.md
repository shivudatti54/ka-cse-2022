# Binary Tree Traversals - Summary

## Key Definitions

- **Binary Tree**: A finite set of nodes that is either empty or consists of a root node and two disjoint binary trees called left and right subtrees
- **Traversal**: A systematic procedure for visiting all nodes in a binary tree exactly once, producing a linear sequence
- **Preorder (DLR)**: Visit root, traverse left subtree, traverse right subtree
- **Inorder (LDR)**: Traverse left subtree, visit root, traverse right subtree
- **Postorder (LRD)**: Traverse left subtree, traverse right subtree, visit root
- **Level-order**: Visit all nodes at depth d before visiting nodes at depth d+1

## Important Formulas

- **Time Complexity** (all traversals): Θ(n) where n = number of nodes
- **Space Complexity** (recursive): O(h) where h = height of tree
- **Space Complexity** (Morris): O(1)
- **Space Complexity** (Level-order): O(w) where w = maximum width
- **Edges in binary tree**: n-1 edges for n nodes

## Key Points

1. Tree traversals visit each node exactly once, giving Θ(n) time complexity
2. Recursive traversals use system call stack; iterative versions use explicit stacks
3. Inorder traversal of BST yields sorted sequence - fundamental property
4. Postorder is essential for expression evaluation and tree deletion operations
5. Level-order requires queue data structure; useful for finding shortest path in unweighted tree
6. Morris traversal achieves O(1) space by creating temporary threaded links
7. Height of balanced tree: O(log n); Height of skewed tree: O(n)
8. Maximum width of tree is at most n/2 (complete binary tree)

## Common Mistakes

1. Confusing traversal orders - writing preorder when inorder is required
2. Forgetting base case (null check) in recursive implementations, causing segmentation faults
3. Incorrectly implementing iterative postorder - the two-stack method is recommended
4. Assuming tree height equals number of nodes - height is number of edges on longest path
5. Mixing up when to process root vs. children in postorder (children must be processed first)
