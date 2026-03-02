# Regular Stochastic Matrices - Summary

## Key Definitions

- **Stochastic Matrix**: A square matrix where all entries are non-negative and each row sums to 1.
- **Regular Stochastic Matrix**: A stochastic matrix P where P^k has all positive entries for some positive integer k.
- **Stationary Distribution**: A probability vector π satisfying πP = π.
- **Irreducible Chain**: A Markov chain where every state can be reached from every other state.
- **Periodic State**: A state with period > 1, causing cyclical behavior in the chain.

## Important Formulas

- **Stationary Distribution**: πP = π, where Σπᵢ = 1
- **Convergence**: lim(n→∞) P^n = 1̅π, where 1̅ is a column vector of ones
- **Regularity Test**: P is regular if P^k > 0 for some k ∈ ℕ

## Key Points

1. Regular stochastic matrices guarantee a unique stationary distribution that is all-positive.

2. The convergence theorem ensures lim(n→∞) P^n exists and equals a rank-one matrix with all rows equal to π.

3. Every regular matrix is irreducible, but irreducible matrices may be periodic (not regular).

4. Periodicity destroys convergence—periodic chains oscillate rather than settle into a stationary distribution.

5. The Perron-Frobenius theorem guarantees λ=1 is a simple eigenvalue with positive eigenvector for regular matrices.

6. Regularity can be verified by checking if the state transition diagram is strongly connected and aperiodic.

7. In applications like PageRank, the matrix is modified (with teleportation) to ensure regularity.

8. The rate of convergence depends on the magnitude of the second-largest eigenvalue |λ₂|.

## Common Mistakes

1. **Confusing irreducible with regular**: All regular chains are irreducible, but periodic irreducible chains are not regular.

2. **Forgetting the sum-to-one condition**: When finding π, always use π₁ + π₂ + ... + πₙ = 1.

3. **Assuming convergence for all stochastic matrices**: Only regular (primitive) matrices guarantee convergence.

4. **Incorrect matrix multiplication**: When computing P^n, ensure proper matrix multiplication rules are followed.

5. **Ignoring periodicity**: A periodic chain may still have a stationary distribution but won't converge to it.