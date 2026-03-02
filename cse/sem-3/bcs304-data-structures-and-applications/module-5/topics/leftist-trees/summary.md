# Leftist Trees - Summary

## Key Definitions

- **Leftist Tree**: A binary tree that satisfies the heap property and the leftist property (NPL(left) ≥ NPL(right) for every node)

- **Null Path Length (NPL)**: The length of the shortest path from a node to a null pointer; NPL(null) = -1, and for any node: NPL(x) = min(NPL(left), NPL(right)) + 1

- **Meldable Heap**: A priority queue that supports efficient merge (meld) operations in O(log n) time

- **Min-Leftist Tree**: A leftist tree where each node's key is less than or equal to the keys of its children (heap order)

## Important Formulas

- **NPL Computation**: NPL(x) = min(NPL(left child), NPL(right child)) + 1
- **Leftist Property**: NPL(left child) ≥ NPL(right child)
- **Path Length Bound**: A leftist tree with n nodes has at most ⌊log₂(n+1)⌋ nodes on any right path

## Key Points

1. Leftist trees support merge in O(log n) time, making them ideal for applications requiring frequent merging

2. All operations (insert, delete-min, merge) have O(log n) time complexity; find-min is O(1)

3. The leftist property ensures the right subtree is always shallower, guaranteeing logarithmic height

4. The merge operation recursively merges the root with the right subtree of the tree with larger root

5. After merging, children may need to be swapped to maintain the leftist property

6. Leftist trees are simpler to implement than Fibonacci heaps but have slightly worse amortized bounds

7. The structure maintains balance through the NPL values rather than explicit rotation operations

8. Both min and max variants exist, following the same principles with appropriate heap ordering

## Common Mistakes

1. Setting NPL(null) = 0 instead of -1 leads to incorrect calculations and property violations

2. Forgetting to update NPL values after merge operations

3. Merging with the left subtree instead of the right subtree during the merge algorithm

4. Not checking and maintaining the leftist property after merge operations (child swapping)

5. Confusing leftist trees with left-leaning trees (a different balanced binary search tree variant)