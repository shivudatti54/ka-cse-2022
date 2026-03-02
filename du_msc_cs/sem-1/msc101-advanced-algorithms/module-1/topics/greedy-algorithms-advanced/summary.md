# Greedy Algorithms - Advanced - Summary

## Key Definitions and Concepts
- **Matroid**: Pair (E, I) where I ⊆ 2^E satisfies heredity and augmentation
- **Competitive Ratio**: Worst-case online vs optimal offline performance
- **Submodularity**: f(A) + f(B) ≥ f(A∪B) + f(A∩B)
- **Approximation Factor**: Ratio of greedy solution to optimal solution

## Important Formulas and Theorems
- **Matroid Greedy Theorem**: Greedy finds max weight independent set
- **Set Cover Approximation**: H_n = Σ_{i=1}^n 1/i
- **Submodular Guarantee**: (1-1/e) for monotone functions under cardinality constraints
- **Huffman Coding**: L(C) = Σ p(x)l(x) minimized by greedy pairing

## Key Points
- Greedy works when problem exhibits optimal substructure + greedy choice property
- Matroids provide theoretical foundation for many greedy algorithms
- Exchange arguments require showing any solution can be converted to greedy form
- Online algorithms need competitive analysis rather than absolute optimality
- Submodular functions enable greedy approaches in ML feature selection
- Approximation ratios often depend on problem structure (log vs constant factors)
- Hybrid approaches (greedy+DP) handle multiple constraints effectively

## Common Mistakes to Avoid
- Assuming greedy works without verifying matroid properties
- Confusing competitive ratio with approximation factor
- Ignoring problem constraints in submodular optimization
- Forgetting to compare against trivial solutions in approximation proofs
- Misapplying offline analysis techniques to online scenarios

## Revision Tips
1. Practice matroid verification with different problem types (scheduling, graphs)
2. Memorize proof templates for exchange arguments and competitive ratios
3. Implement submodular maximization with budget constraints
4. Solve past DU papers on interval partitioning and Huffman variants
5. Study recent papers on greedy algorithms in ML (e.g., neural architecture search)