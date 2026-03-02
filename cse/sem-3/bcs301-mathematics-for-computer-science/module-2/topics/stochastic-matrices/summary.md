# Stochastic Matrices - Summary

## Key Definitions

- **Stochastic Matrix**: An n×n matrix P = [pᵢⱼ] where pᵢⱼ ≥ 0 and each row sums to 1 (Σⱼ pᵢⱼ = 1)
- **Row-Stochastic Matrix**: Stochastic matrix with row sums equal to 1 (most common in Markov chains)
- **Column-Stochastic Matrix**: Stochastic matrix with column sums equal to 1
- **Regular Stochastic Matrix**: A stochastic matrix P where some power Pᵏ has all positive entries
- **Stationary Distribution**: A probability vector π satisfying πP = π and Σπᵢ = 1
- **Absorbing State**: A state i where pᵢᵢ = 1 and pᵢⱼ = 0 for j ≠ i

## Important Formulas

- **Row sum property**: Σⱼ pᵢⱼ = 1 for all i
- **Eigenvalue property**: P·1 = 1 (where 1 is the all-ones vector)
- **k-step transitions**: Pᵏ gives probability of transitioning in exactly k steps
- **Chapman-Kolmogorov**: P^(m+n) = P^m · P^n
- **Stationary distribution**: πP = π, Σπᵢ = 1
- **Limiting behavior**: For regular P, lim(k→∞) Pᵏ = 1π

## Key Points

1. All entries in a stochastic matrix must be non-negative (between 0 and 1 inclusive)
2. Every stochastic matrix has eigenvalue λ = 1 with corresponding eigenvector (1, 1, ..., 1)ᵀ
3. The entry pᵢⱼ(k) in Pᵏ represents the probability of moving from state i to state j in k steps
4. Regular stochastic matrices guarantee convergence to a unique stationary distribution
5. Absorbing states (row [1, 0, ..., 0]) make a matrix non-regular since they can never transition to other states
6. The stationary distribution π represents the long-run proportion of time spent in each state
7. For regular matrices, all eigenvalues other than 1 have absolute value less than 1 (Perron-Frobenius)
8. The matrix power Pᵏ approaches a constant matrix with identical rows as k → ∞ for regular matrices

## Common Mistakes

1. **Forgetting row sums**: Checking only non-negativity and missing that rows must sum to exactly 1
2. **Confusing left and right eigenvectors**: The stationary distribution is a left eigenvector (row vector), not a right eigenvector
3. **Assuming all stochastic matrices are regular**: Matrices with absorbing states are not regular
4. **Incorrect matrix multiplication**: P² means P × P, not element-wise multiplication—common computation error
5. **Not normalizing the stationary distribution**: The solution to πP = π must be normalized so that Σπᵢ = 1