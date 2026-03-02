# Probability Vectors - Summary

## Key Definitions

- **Probability Vector**: An n-dimensional column vector p = (p₁, p₂, ..., pₙ)ᵀ where pᵢ ≥ 0 for all i and Σᵢ pᵢ = 1

- **Stochastic Vector**: Another term for probability vector, emphasizing its use in stochastic processes

- **State Distribution**: A probability vector representing the probabilities of a system being in each of its possible states

- **Stationary Distribution**: A probability vector p such that p = Pᵀ · p, remaining unchanged under transitions

- **Standard (n-1)-Simplex**: The set of all probability vectors in ℝⁿ, defined by pᵢ ≥ 0 and Σᵢ pᵢ = 1

## Important Formulas

- **Probability Vector Definition**: pᵢ ≥ 0 and Σᵢ pᵢ = 1

- **State Transition**: p⁽ᵏ⁺¹⁾ = Pᵀ · p⁽ᵏ⁾ where P is the stochastic matrix

- **Stationary Distribution**: p = Pᵀ · p or equivalently (Pᵀ - I)p = 0

- **Convex Combination**: αp + (1-α)q is a probability vector for 0 ≤ α ≤ 1

- **L₁ Norm**: ||p||₁ = Σᵢ pᵢ = 1 for any probability vector

## Key Points

1. Probability vectors must satisfy both non-negativity and unity (sum equals 1) conditions

2. The set of probability vectors forms a convex set (the standard simplex)

3. In Markov chains, probability vectors represent complete state distributions, not individual states

4. Matrix multiplication with probability vectors requires using the transpose of the stochastic matrix

5. Stationary distributions are eigenvectors corresponding to eigenvalue λ = 1

6. The sum of components of any probability vector is always 1 (L₁ norm equals 1)

7. Unit vectors e₁, e₂, ..., eₙ are extreme points representing "pure" states

8. Probability vectors provide a compact representation of uncertainty in stochastic systems

## Common Mistakes

1. **Forgetting the transpose**: Using P instead of Pᵀ when multiplying by a probability vector, leading to incorrect results

2. **Ignoring normalization**: After operations, failing to verify or enforce that components sum to 1

3. **Confusing row and column vectors**: Probability vectors are defined as column vectors; row vectors require different matrix operations

4. **Assuming non-uniqueness**: Forgetting that stationary distributions may not be unique for irregular chains

5. **Neglecting non-negativity**: Accepting vectors with negative components as probability vectors