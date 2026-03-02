# Randomized Algorithm Design - Summary

## Key Definitions and Concepts
- **Las Vegas Algorithm**: Always correct, randomized runtime
- **Monte Carlo Algorithm**: Bounded runtime, probabilistic correctness
- **Probabilistic TM**: Computational model allowing random choices
- **FPRAS**: Fully Polynomial Randomized Approximation Scheme

## Important Formulas and Theorems
- **Karger's Success Probability**: Pr[success] ≥ 2/(n(n-1))
- **Chernoff Bound**: Pr[X ≥ (1+δ)μ] ≤ e^(-δ²μ/3) for δ ∈ (0,1)
- **Bloom Filter FP Rate**: (1 - e^(-kn/m))^k ≈ (0.6185)^(m/n)
- **Schöning's Algorithm**: 3-SAT in O((2^(n/3)) poly(n)) time

## Key Points
- Randomization often breaks adversarial input patterns
- Majority voting amplifies Monte Carlo correctness
- Min-Cut via contraction demonstrates power of repeated trials
- Derandomization preserves guarantees but may increase complexity
- Fingerprinting enables O(1) space equality checks
- Randomized rounding bridges continuous-discrete optimization
- Current research extends to differential privacy and sublinear algorithms

## Common Mistakes to Avoid
- Confusing expected runtime with high-probability bounds
- Neglecting to amplify success probability where needed
- Applying Chernoff bounds without independent trials
- Overlooking deterministic alternatives with better worst-case performance

## Revision Tips
1. Practice expectation calculations on dependency chains
2. Memorize proof sketches for Karger's and Bloom Filter analysis
3. Compare randomized vs deterministic approaches for sorting, searching
4. Study recent DU PhD theses on probabilistic data structures