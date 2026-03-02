# Binary Search Tree Operations and Complexity - Summary

## Key Definitions and Concepts
- **Binary Search Tree (BST)**: A binary tree where left subtree contains smaller values, right subtree contains larger values
- **Tree Height**: Number of edges from root to deepest leaf
- **Balance Factor**: height(left) - height(right) for each node
- **In-order Successor**: Smallest value in the right subtree (used in deletion)
- **In-order Predecessor**: Largest value in the left subtree (alternative for deletion)

## Important Formulas and Theorems

| Operation | Best Case | Average Case | Worst Case |
|-----------|-----------|---------------|------------|
| Search    | O(1)      | O(log n)      | O(n)       |
| Insert    | O(1)      | O(log n)      | O(n)       |
| Delete    | O(1)      | O(log n)      | O(n)       |
| Traversal | O(n)      | O(n)          | O(n)       |

- **Space Complexity**: O(n) for storage, O(h) auxiliary for recursion
- **Recurrence**: T(n) = T(n/2) + O(1) → O(log n) for balanced trees

## Key Points
- BST maintains sorted data, enabling efficient ordered operations
- Insertion always creates a new leaf node
- Deletion with two children requires finding in-order successor
- Tree shape depends on insertion order; sorted input creates degenerate tree
- Balanced BSTs (AVL, Red-Black) guarantee O(log n) worst case
- In-order traversal always produces sorted output
- Search efficiency depends on tree height, not number of nodes

## Common Mistakes to Avoid
- Confusing BST with binary tree (ordering property is key)
- Forgetting that deletion with two children replaces value then deletes successor
- Assuming O(log n) always applies (worst case is O(n) for skewed trees)
- Not considering how insertion order affects performance
- Confusing space complexity of traversal (recursive uses O(h) stack space)

## Revision Tips
1. Practice drawing trees for different insertion sequences
2. Memorize the three deletion cases with visual examples
3. Remember: average case assumes balanced tree, worst case assumes degenerate
4. Know why sorted input is the worst-case scenario for BSTs
5. Review the relationship between height and number of nodes: log₂(n+1) ≤ h ≤ n