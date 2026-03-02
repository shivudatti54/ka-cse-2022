# Skip Lists - Summary

## Key Definitions and Concepts

- **Skip List**: A probabilistic data structure that allows O(log n) average-case search, insertion, and deletion in a sorted sequence.
- **Node**: Contains a key/value and an array of forward pointers to next nodes at each level.
- **Level**: Each tier in the hierarchical linked list structure; higher levels contain subsets of elements from lower levels.
- **Geometric Distribution**: The probabilistic model where each element appears at level i with probability (1/2)^(i+1).
- **Express Lanes**: The metaphor for higher levels that allow skipping over many elements during search.

## Important Formulas and Theorems

- **Random Level Generation**: `P(level = k) = (1/2)^(k+1)` for k ≥ 0
- **Expected Height**: O(log n) for n elements
- **Search Complexity**: O(log n) average, O(n) worst case
- **Insert/Delete Complexity**: O(log n) average, O(n) worst case  
- **Space Complexity**: O(n) average, O(n log n) worst case
- **Expected Pointers per Node**: 1/(1-p) = 2 (for p = 1/2)

## Key Points

- Skip lists use randomization to achieve balanced structure without complex rebalancing algorithms
- The search algorithm moves horizontally at high levels and drops down when overshooting the target
- Insertion generates a random level for each new node using coin flips
- Deletion requires updating pointers at ALL levels where the node exists
- Expected operations are O(log n) due to geometric distribution of levels
- Worst-case O(n) is extremely improbable in practice
- Simpler to implement than balanced BSTs while offering comparable performance
- Memory overhead: approximately 2n pointers on average

## Common Mistakes to Avoid

- Forgetting to update ALL forward pointers during insertion or deletion
- Not checking if a node exists before deletion (can corrupt the list)
- Confusing the random level generation with uniform distribution
- Drawing only one level when diagramming (need to show all levels)
- Assuming worst-case O(n) is the typical behavior (it's not!)

## Revision Tips

1. Practice drawing skip list diagrams with 5-7 elements at all levels
2. Trace search, insert, and delete operations manually on paper
3. Derive the expected height mathematically using geometric series
4. Compare implementation complexity with AVL trees to appreciate skip list simplicity
5. Remember: randomization simplifies design but introduces (very small) probability of poor performance