# Representation of Binary Trees - Summary

## Key Definitions and Concepts

- **Binary Tree**: Hierarchical data structure where each node has ≤ 2 children (left & right).
- **Linked Representation**: Uses nodes with `data`, `left`, and `right` pointers (dynamic memory allocation).
- **Sequential Representation**: Stores nodes in arrays using index relationships (static allocation).
- **Complete Binary Tree**: All levels except last are full, nodes filled left-to-right (ideal for array storage).
- **Root Node**: Topmost node (index 0 in arrays).

## Important Formulas and Theorems

1. **Array Index Relationships**:
   ```python
   Parent(i) = (i-1)//2          # Floor division
   Left_Child(i) = 2*i + 1
   Right_Child(i) = 2*i + 2
   ```
2. **Space Complexity**:
   - Linked: O(n) + pointer overhead
   - Array: O(2^h) where h = tree height (wasteful for incomplete trees)
3. **Time Complexity**:
   - Insertion (linked): O(1) with parent reference
   - Traversal: O(n) for both representations

## Key Points

- **Linked Representation**:
  - Flexible for dynamic operations
  - Requires extra memory for pointers (4/8 bytes per node)
  - Used in BSTs, expression trees, and file systems
- **Array Representation**:
  - Efficient for complete trees (no wasted space)
  - Fast access via index calculations
  - Used in heaps/priority queues
- Preorder/Inorder/Postorder traversals use linked representation naturally
- Array storage for incomplete trees leads to memory fragmentation
- Root node is always at index 0 in array representation
- Height of tree with array size `n`: `h = log₂(n+1) - 1`
- Minimum array size for height `h`: `2^(h+1) - 1`

## Common Mistakes to Avoid

1. **Array Index Errors**: Using `2*i` instead of `2*i+1` for left child
2. **Null Pointer Handling**: Forgetting to set `left/right` to `NULL` in linked nodes
3. **Space Miscalculations**: Assuming array size = node count (valid only for complete trees)
4. **Traversal Confusion**: Attempting postorder traversal on array without recursion/stack

## Revision Tips

1. **Practice Index Calculations**: Convert the sample tree `A(B(D,E),C)` to array format:
   ```
   Index: 0 1 2 3 4
   Value: A B C D E
   ```
2. **Compare Representations**:
   - Draw linked vs array for tree `A(B,C(D))`
   - Calculate wasted array slots
3. **Memorize Formulas**:
   - Parent/child index relationships
   - Space complexity for both methods
4. **Implement Operations**:
   - Write pseudocode for linked insertion
   - Practice array-to-linked conversion
