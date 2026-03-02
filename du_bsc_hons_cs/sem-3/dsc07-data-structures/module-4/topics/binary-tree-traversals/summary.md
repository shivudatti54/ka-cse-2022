# Binary Tree Traversals - Summary

## Key Definitions and Concepts

*   **Inorder Traversal**: Left subtree, current node, right subtree (left -> root -> right)
*   **Preorder Traversal**: Current node, left subtree, right subtree (root -> left -> right)
*   **Postorder Traversal**: Left subtree, right subtree, current node (left -> right -> root)
*   **Recursive Implementation**: Function calls itself to traverse the tree
*   **Iterative Implementation**: Uses a stack or queue to traverse the tree without function calls

## Important Formulas and Theorems

*   Time complexity: O(n), where n is the number of nodes in the tree
*   Space complexity:
    *   Recursive implementation: O(h), where h is the height of the tree
    *   Iterative implementation: O(1) for inorder and preorder traversals, O(h) for postorder traversal

## Key Points

*   Binary tree traversals visit each node in the tree exactly once
*   Inorder traversal visits nodes in ascending order
*   Preorder traversal visits the current node before its subtrees
*   Postorder traversal visits the subtrees before the current node
*   Recursive and iterative implementations have different trade-offs
*   Binary tree traversals have various applications in computer science
*   Understanding binary tree traversals is crucial for more advanced data structures and algorithms

## Common Mistakes to Avoid

*   Confusing the order of visitation for each traversal type
*   Not considering the time and space complexity of each implementation
*   Not practicing traversals on different binary tree structures
*   Not understanding the applications of binary tree traversals

## Revision Tips

*   Practice implementing binary tree traversals using both recursive and iterative approaches
*   Review the time and space complexity of each traversal type
*   Draw diagrams to visualize the traversal process
*   Try to identify the type of traversal used in a given algorithm or code snippet