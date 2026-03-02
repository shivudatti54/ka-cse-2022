# Binary Tree Traversals - Summary

## Key Definitions

- **Binary Tree:** A hierarchical data structure where each node has at most two children (left child and right child).

- **Traversal:** A systematic procedure to visit all nodes in a binary tree exactly once, applying an operation at each node.

- **Preorder (DFS):** Visit root, traverse left subtree, traverse right subtree - order: Root-Left-Right.

- **Inorder (DFS):** Traverse left subtree, visit root, traverse right subtree - order: Left-Root-Right.

- **Postorder (DFS):** Traverse left subtree, traverse right subtree, visit root - order: Left-Right-Root.

- **Level-order (BFS):** Visit all nodes at depth d before visiting nodes at depth d+1, using a queue.

## Important Formulas

- **Time Complexity (all traversals):** T(n) = Θ(n) - each of the n nodes is visited exactly once

- **Space Complexity (recursive):** S(n) = O(h) where h is tree height; worst case O(n) for skewed tree, O(log n) for balanced tree

- **Space Complexity (Morris traversal):** S(n) = O(1) - constant extra space

- **Tree Height:** For complete binary tree: h = ⌊log₂n⌋; For skewed tree: h = n

## Key Points

1. Preorder, inorder, and postorder are depth-first traversals using recursion (stack), while level-order is breadth-first using a queue.

2. Recursive traversals have O(h) space complexity where h is height; for balanced trees this is O(log n), for skewed trees O(n).

3. Morris traversal achieves O(1) space by temporarily creating threaded links to predecessors.

4. Inorder traversal of BST produces sorted ascending order of values.

5. Postorder is used for tree deletion and postfix expression evaluation.

6. Any two traversals (preorder+inorder or postorder+inorder) can uniquely reconstruct a binary tree with distinct node values.

7. Level-order traversal processes level by level, essential for finding tree width and shortest path in unweighted trees.

## Common Mistakes

1. Confusing the order of operations in recursive traversals - remember the position of "visit(root)" determines the traversal type.

2. Forgetting that recursive space complexity depends on tree height, not number of nodes - always consider the worst-case tree shape.

3. Assuming Morris traversal breaks the tree structure - it temporarily modifies but fully restores the original tree.

4. Using level-order (queue) when a depth-first approach is needed, or vice versa, for specific algorithmic problems.

5. Attempting to reconstruct a tree from preorder alone - you need inorder along with either preorder or postorder for unique reconstruction.