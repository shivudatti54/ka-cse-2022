# Optimal Binary Search Trees - Summary

## Key Definitions

- **Optimal Binary Search Tree (OBST)**: A binary search tree that minimizes the expected search cost given known access probabilities for keys.

- **Search Probability (pᵢ)**: The probability that key Kᵢ is searched for in the tree.

- **Dummy Key (dᵢ)**: Represents unsuccessful searches that fall between keys Kᵢ and Kᵢ₊₁, with probability qᵢ.

- **Expected Search Cost**: The weighted sum of search depths, where weights are the access probabilities of keys and dummy keys.

- **Weight (w[i][j])**: The sum of all probabilities (both key and dummy) in the range i to j.

## Important Formulas

- **Weight calculation**: w[i][j] = w[i][j-1] + pⱼ + qⱼ

- **Cost recurrence**: e[i][j] = e[i][r-1] + e[r+1][j] + w[i][j], where r is the optimal root

- **Optimal root**: r = argmin_{k∈[i,j]} { e[i][k-1] + e[k+1][j] }

- **Base case**: e[i][i-1] = qᵢ₋₁

- **Expected cost**: E[search] = Σᵢ pᵢ(depth(Kᵢ) + 1) + Σᵢ qᵢ(depth(dᵢ) + 1)

## Key Points

1. OBST uses dynamic programming to find the optimal root for each subproblem of keys Kᵢ through Kⱼ.

2. Keys with higher access probabilities should be placed closer to the root to minimize search cost.

3. The algorithm builds solutions bottom-up, starting from single-key trees and building to the full tree.

4. The optimal root for adjacent subproblems tends to be close, enabling O(n²) optimization.

5. Time complexity is O(n³) for basic implementation and O(n²) with optimization.

6. Space complexity is O(n²) for storing the e and root tables.

7. The tree structure itself can be reconstructed from the root table using recursion.

8. If all keys have equal probability, any balanced BST is optimal.

## Common Mistakes

1. **Incorrect weight order**: Using w[i][j] = w[i+1][j] + pᵢ + qᵢ₋₁ instead of the correct w[i][j] = w[i][j-1] + pⱼ + qⱼ.

2. **Forgetting dummy keys**: Many students ignore the dummy key probabilities q₀ through qₙ, which are essential for accurate cost calculation.

3. **Depth counting**: Starting depth from 0 instead of 1 is a common error that gives incorrect final costs.

4. **Base case confusion**: Setting e[i][i] = pᵢ instead of the correct e[i][i-1] = qᵢ₋₁ leads to wrong computations.

5. **Confusion with Huffman**: Attempting to apply Huffman's greedy approach (always combining smallest probabilities) to OBST, which requires dynamic programming.