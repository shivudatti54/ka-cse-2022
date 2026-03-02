# Leftist Trees - Summary

## Key Definitions

- **Leftist Tree**: A binary tree that satisfies both the heap property (keys in parent ≤ keys in children for min-heap) and the leftist property (NPL(left child) ≥ NPL(right child) for every node).

- **Null Path Length (NPL)**: The length of the shortest path from a node to a null pointer in its subtree. Formally, NPL(x) = 0 if x has null children, else NPL(x) = 1 + min(NPL(left), NPL(right)).

- **Leftist Property**: The condition that NPL(left_child) ≥ NPL(right_child) for every node in the tree.

- **Right Spine**: The path from the root following only right child pointers to a leaf node.

## Important Formulas

- NPL(x) = 0 if x is a leaf or has null children
- NPL(x) = 1 + min(NPL(left_child), NPL(right_child)) otherwise
- Updated NPL after swap: NPL(x) = NPL(right_child) + 1

## Key Points

1. Leftist trees are meldable priority queues that support efficient merge in O(log n) time.

2. The leftist property ensures that the right spine contains at most log₂(n+1) nodes, guaranteeing logarithmic merge complexity.

3. Merge is the fundamental operation—insert and delete-min are implemented using merge.

4. The merge algorithm always works on the right spine, never requiring traversal of the entire tree.

5. After each merge, the children may need to be swapped to restore the leftist property.

6. Find-min is O(1) since the minimum is always at the root (heap property).

7. Build-heap from n elements takes O(n) time using pairwise merging.

8. Leftist trees differ from binary heaps primarily in their ability to merge efficiently.

## Common Mistakes

1. Confusing the heap property with the leftist property—both must hold but serve different purposes.

2. Forgetting to update NPL values after swapping children during merge.

3. Attempting to merge into the left subtree instead of the right subtree (merge always proceeds via right spines).

4. Not handling the base case when one of the trees is null during merge.

5. Assuming leftist trees support decrease-key efficiently—they do not; this is a limitation compared to other structures like Fibonacci heaps.
