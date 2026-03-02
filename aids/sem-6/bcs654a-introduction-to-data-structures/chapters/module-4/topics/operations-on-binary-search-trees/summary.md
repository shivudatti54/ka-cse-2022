# Operations on Binary Search Trees - Summary

## Key Definitions and Concepts

- BINARY SEARCH TREE (BST): A binary tree where each node has at most two children, with the property that all nodes in the left subtree have values less than the root, and all nodes in the right subtree have values greater than the root

- BST PROPERTY: For every node, left child value < parent value < right child value

- NODE: Contains three components - data field, left pointer, and right pointer

- TREE HEIGHT: The length of the longest path from root to leaf

## Important Formulas and Theorems

- Insertion Time Complexity: O(h) where h is tree height
- Search Time Complexity: O(h)
- Find Minimum: O(h) - traverse left until null
- Find Maximum: O(h) - traverse right until null
- Count Nodes: O(n) - must visit every node
- In a balanced BST: h = log₂n, so operations are O(log n)
- In worst case (skewed tree): h = n, so operations are O(n)

## Key Points

- The BST property enables efficient searching by eliminating half the tree at each step
- Insertion always happens at a leaf position; internal node values remain unchanged
- Minimum value is always at the leftmost node (keep moving LEFT)
- Maximum value is always at the rightmost node (keep moving RIGHT)
- The order of insertion determines the final tree shape
- Recursive implementations are preferred for clarity in exams
- Tree height directly impacts operation efficiency - balance is crucial
- Inorder traversal of BST produces sorted output

## Common Mistakes to Avoid

- Forgetting to check for null/empty tree before operations
- Not handling duplicate values according to specified convention
- Confusing the direction of traversal (left for smaller, right for larger)
- Assuming O(log n) always - must consider tree balance
- Mixing up minimum/maximum traversal directions

## Revision Tips

- Practice drawing BSTs from insertion sequences multiple times
- Memorize the recursive formulas for search, count, min, and max
- Remember: LEFT = SMALLER, RIGHT = LARGER
- Practice time complexity analysis for all operations
- Review the relationship between tree height and operation efficiency