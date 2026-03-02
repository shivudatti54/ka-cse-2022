# Selection Trees - Summary

## Key Definitions

- **Selection Tree**: A binary tree data structure used to efficiently select the minimum or maximum element from multiple sorted sequences
- **Winner Tree (Min Selection Tree)**: A complete binary tree where each internal node stores the smaller (winner) of its two children
- **Loser Tree (Max Selection Tree)**: A complete binary tree where each internal node stores the larger (loser) of its two children
- **K-way Merge**: The operation of merging k sorted runs or sequences into a single sorted output

## Important Formulas

- **Tree Height**: h = ⌈log₂k⌉ for k leaves
- **Array Size**: 2k - 1 nodes (or 2k with 1-based indexing)
- **Construction Time**: O(k)
- **Finding Winner**: O(1)
- **Update Time**: O(log k) = O(h)
- **Total comparisons for n outputs**: O(k + n log k)

## Key Points

1. Selection Trees are complete binary trees ideal for k-way merge operations in external sorting
2. Winner trees store minimum values at internal nodes; the root always contains the global minimum
3. Array representation provides O(1) access and excellent cache locality
4. Construction involves placing first elements of each run at leaves and building upward
5. After removing a winner, only the path from that leaf to the root needs updating
6. Selection trees reduce comparisons from O(k) per element to O(log k) per element
7. Loser trees store the losing element at each internal node, useful when tracking alternatives
8. The tree must be reconstructed when any run becomes empty and needs to be handled specially

## Common Mistakes

1. Confusing winner trees with loser trees - remember winner trees find minimums, loser trees track maximums as "losers"
2. Forgetting that leaves represent sorted runs, not individual elements
3. Not updating the leaf node correctly when advancing to the next element in a run
4. Using 0-based indexing incorrectly when implementing array-based trees
5. Attempting to update only the root after removing an element instead of propagating changes up the tree path