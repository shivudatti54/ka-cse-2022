# Monte Carlo vs Las Vegas Algorithms - Summary

## Key Definitions and Concepts
- **Monte Carlo**: Randomized alg. with possible incorrect outputs
- **Las Vegas**: Randomized alg. with random runtime but always correct
- **RP** (Random Polynomial): 1-sided error Monte Carlo
- **ZPP**: Las Vegas algorithms with expected poly-time
- **Amplification**: Error reduction via independent trials

## Important Formulas and Theorems
- Error Probability: Pr[error] ≤ ε → Pr[error after k runs] ≤ ε^k
- Expected Runtime: E[T] = Σ_{t=1}^∞ Pr[T ≥ t]
- Schwartz-Zippel: Pr[f(x)=0] ≤ d/|S| for non-zero poly f
- Yao's Principle: Worst-case expected ≥ average-case for dist.

## Key Points
- Monte Carlo tradeoff: Time vs accuracy
- Las Vegas advantage: Certain correctness
- BPP not known to equal P (major open problem)
- Randomness vs non-determinism in complexity
- Quantum implications: BQP vs BPP relationships
- Practical applications: Cryptography, ML, HPC
- Derandomization via pseudorandom generators

## Common Mistakes to Avoid
- Confusing one-sided vs two-sided error models
- Misapplying expectation formulas for dependent events
- Overlooking certificate requirements in RP/co-RP
- Assuming all Las Vegas algs can be made deterministic
- Ignoring space randomization in streaming algorithms

## Revision Tips
1. Practice error amplification calculations using logarithms
2. Memorize complexity class hierarchy diagram
3. Solve expected value problems using indicator variables
4. Implement Miller-Rabin with different witness counts
5. Study recent papers on derandomization breakthroughs

Length: 650 words