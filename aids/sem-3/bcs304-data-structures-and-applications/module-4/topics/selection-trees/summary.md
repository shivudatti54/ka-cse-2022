# Selection Trees - Summary

## Key Definitions

- **Selection Tree**: A complete binary tree used for k-way merging where leaves represent current elements from k sorted sequences and internal nodes store comparison winners (or losers)
- **Winner Tree (Min Selection Tree)**: Internal nodes store the minimum of children; root contains global minimum
- **Loser Tree (Max Selection Tree)**: Internal nodes store the maximum (loser) of children; provides efficient O(log k) update with guaranteed single comparison per level

## Important Formulas

- **Tree Height**: h = ⌈log₂k⌉ for k sorted sequences
- **Construction Time**: Θ(k) comparisons for k leaves
- **Update Time**: O(log k) comparisons per element extraction
- **Space Complexity**: 2k - 1 = Θ(k) nodes
- **Internal Nodes**: k - 1 for k leaves

## Key Points

1. Selection trees solve the k-way merge problem efficiently for external sorting
2. Winner trees store minimum at internal nodes; loser trees store maximum
3. Loser trees guarantee exactly one comparison per tree level during updates
4. For non-power-of-two k, add dummy leaves with +∞ (min trees) or -∞ (max trees)
5. Height of tree is ⌈log₂k⌉, determining the update complexity bound
6. Construction requires exactly k-1 comparisons (one per internal node)
7. Selection trees outperform naive linear merging (O(k) per element) significantly for large k

## Common Mistakes

1. Confusing winner and loser tree update mechanisms—one compares with sibling winner, the other with stored loser
2. Forgetting to handle non-power-of-two leaf counts with dummy values
3. Incorrectly calculating tree height as log₂k instead of ⌈log₂k⌉
4. Believing update is O(1) when it is actually O(log k)
5. Using selection trees for general priority queue operations where heaps are more appropriate
   ===SUMMARY_MD===
