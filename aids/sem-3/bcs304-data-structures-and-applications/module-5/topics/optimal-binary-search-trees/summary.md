# Optimal Binary Search Trees - Summary

## Key Definitions

- **Optimal Binary Search Tree (OBST)**: A binary search tree that minimizes the expected search cost given known access probabilities for keys and unsuccessful searches
- **Successful Search Probability (pᵢ)**: The probability that key kᵢ is searched for, representing internal node access
- **Unsuccessful Search Probability (qᵢ)**: The probability of searching for a value between keys, represented by dummy keys at external nodes
- **Weighted External Path Length**: E = Σ pᵢ(depth(kᵢ)+1) + Σ qᵢ(depth(dᵢ)+1), the total expected cost per search
- **Optimal Substructure**: The property that an optimal tree contains optimal subtrees, allowing dynamic programming solutions

## Important Formulas

- **Recurrence Relation**: e[i][j] = w[i][j] + min{e[i][r-1] + e[r+1][j]} for r ∈ [i, j]
- **Weight Sum**: w[i][j] = w[i][j-1] + pⱼ + qⱼ
- **Base Case**: e[i][i-1] = qᵢ₋₁
- **Knuth's Optimization**: root[i][j-1] ≤ root[i][j] ≤ root[i+1][j]

## Key Points

1. OBST minimizes expected search cost rather than worst-case cost, leveraging known access frequency distributions
2. The dynamic programming approach considers all possible root choices for each subtree, making it exhaustive but optimal
3. The tree structure emerges from the root table by recursively selecting roots for left and right subtrees
4. Dummy keys (d₀, d₁, ..., dₙ) represent gaps between keys where unsuccessful searches terminate
5. The sum of all pᵢ and qᵢ probabilities must equal 1 for a valid probability distribution
6. Basic algorithm runs in O(n³) time but Knuth's optimization reduces it to O(n²)
7. Space complexity is O(n²) due to the 2D tables for costs and root indices
8. The optimal tree may not be height-balanced; it prioritizes frequently accessed keys near the root

## Common Mistakes

1. **Confusing indexing**: Many students confuse 0-based vs 1-based indexing when implementing the DP tables, leading to incorrect results
2. **Forgetting base cases**: The e[i][i-1] = qᵢ₋₁ entries are crucial for computing larger subtrees; omitting them breaks the algorithm
3. **Not accumulating weights**: The w[i][j] term must include all probabilities in the subtree, not just the root's probability
4. **Ignoring dummy keys**: Some solutions forget to include qᵢ in calculations, resulting in incomplete cost computation
5. **Incorrect tree construction**: After computing the root table, students often fail to recursively construct the left and right subtrees correctly
