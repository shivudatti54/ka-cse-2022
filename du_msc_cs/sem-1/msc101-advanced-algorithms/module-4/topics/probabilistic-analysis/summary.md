# Probabilistic Analysis - Summary

## Key Definitions and Concepts
- **Probabilistic Analysis**: Study of algorithms using probability distributions over inputs
- **Indicator Variable**: X = 1 if event occurs, 0 otherwise; E[X] = Pr(event)
- **Universal Hashing**: Hash family where Pr(h(k)=h(l)) ≤ 1/m
- **Tail Inequalities**: Bounds for low-probability extreme events

## Important Formulas and Theorems
- Linearity of Expectation: E[ΣX_i] = ΣE[X_i]
- Quicksort Comparisons: E[C(n)] = 2(n+1)H_n - 4n ≈ 1.38n log n
- Markov Inequality: Pr(X ≥ a) ≤ E[X]/a
- Chernoff Bound: Pr(X ≥ (1+δ)μ) ≤ exp(-δ²μ/3) for 0 < δ < 1
- BST Height: E[H(n)] ≤ 3 ln n

## Key Points
- Average-case analysis often more practical than worst-case
- Indicator variables convert complex probabilities to simple expectations
- Universal hashing provides average-case O(1) access time
- Probabilistic recurrences require careful expectation handling
- Chernoff bounds exponentially decrease tail probabilities
- Modern applications include differential privacy and big data systems
- Research trend: Combining PAC learning with probabilistic guarantees

## Common Mistakes to Avoid
- Confusing algorithm randomness with input randomness
- Applying linearity of expectation to dependent variables without justification
- Misusing tail bounds beyond their applicable conditions
- Neglecting to specify probability space in analysis

## Revision Tips
- Practice indicator variable techniques on sorting/hashing problems
- Memorize key inequalities and their application scenarios
- Study classic papers: Knuth's BST analysis, Rabin's hashing
- Implement probabilistic analysis for simple algorithms from scratch
- Relate concepts to recent papers on arXiv (e.g., "probabilistic analysis" in FOCS 2023)

Length: 650 words