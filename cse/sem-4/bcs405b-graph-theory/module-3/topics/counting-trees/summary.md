# Counting Trees - Summary

## Key Definitions and Concepts

- **Tree:** A connected acyclic graph with n vertices and n-1 edges
- **Labeled Tree:** A tree where each vertex has a unique label from 1 to n
- **Spanning Tree:** A subgraph that is a tree containing all vertices of the original graph
- **Prüfer Sequence:** A unique encoding of length n-2 for a labeled tree with n vertices
- **Laplacian Matrix:** Matrix L where Lᵢᵢ = degree(vᵢ), Lᵢⱼ = -1 if adjacent, 0 otherwise

## Important Formulas and Theorems

- **Cayley's Formula:** Number of labeled trees on n vertices = n^(n-2)
- **Matrix-Tree Theorem:** Number of spanning trees = any cofactor of Laplacian matrix
- **Complete Graph Kₙ:** n^(n-2) spanning trees
- **Complete Bipartite Kₘ,ₙ:** m^(n-1) × n^(m-1) spanning trees
- **Cycle Cₙ:** n spanning trees

## Key Points

1. A tree with n vertices always has exactly n-1 edges
2. Every Prüfer sequence of length n-2 corresponds to exactly one labeled tree
3. In a Prüfer sequence, vertex i appears deg(i) - 1 times
4. Cayley's Formula can be proven using the Prüfer sequence bijection
5. Matrix-Tree Theorem provides an algebraic method for counting spanning trees
6. The Laplacian matrix is always singular with determinant zero
7. Deleting any row and column from Laplacian gives the same cofactor value

## Common Mistakes to Avoid

1. Confusing labeled trees with unlabeled trees—they have different counts
2. Forgetting that Cayley's Formula applies only to labeled trees on n vertices
3. Incorrectly constructing the Laplacian matrix (remember: -1 for edges, 0 otherwise)
4. Using n^(n-2) for unlabeled trees—this is incorrect; unlabeled tree counting is much more complex

## Revision Tips

1. Practice converting between trees and Prüfer sequences—key for exam problems
2. Memorize the special graph formulas for quick problem-solving
3. Understand the degree-counting relationship in Prüfer sequences
4. Practice determinant calculation for 3×3 and 4×4 matrices for Matrix-Tree problems
5. Remember: Prüfer length = n-2, not n-1
