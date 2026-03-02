# Higher Transition Probabilities - Summary

## Key Definitions

- **n-step transition probability Pₙ(i,j)**: The probability that the Markov chain moves from state i to state j in exactly n transitions, i.e., Pₙ(i,j) = P(Xₙ = j | X₀ = i)
- **Chapman-Kolmogorov equations**: Fundamental relations Pₘ₊ₙ(i,j) = Σₖ Pₘ(i,k) · Pₙ(k,j) for computing multi-step transitions
- **n-step transition matrix**: The matrix Pⁿ, where entry (i,j) equals Pₙ(i,j)

## Important Formulas

- **Matrix power method**: Pⁿ = P × P × ... × P (n times); entry (i,j) = Pₙ(i,j)
- **State distribution after n steps**: πₙ = π₀ × Pⁿ, where π₀ is the initial distribution
- **Chapman-Kolmogorov**: Pₘ₊ₙ(i,j) = Σₖ Pₘ(i,k) · Pₙ(k,j)
- **Recursive formula**: Pₙ₊₁(i,j) = Σₖ Pₙ(i,k) · P(k,j)
- **Row sum property**: Σⱼ Pₙ(i,j) = 1 for all i and n ≥ 1

## Key Points

1. Higher transition probabilities extend single-step analysis to multiple time steps in a Markov chain
2. The Chapman-Kolmogorov equations provide an intuitive way to break down multi-step transitions through intermediate states
3. Matrix powers Pⁿ offer a computationally efficient method for computing all n-step probabilities simultaneously
4. The entry (i,j) in matrix Pⁿ directly gives Pₙ(i,j), the probability of transitioning from state i to j in n steps
5. For irreducible and aperiodic chains, Pₙ(i,j) converges to a stationary distribution π(j) as n → ∞
6. Higher transition probabilities are essential for analyzing long-term behavior and convergence of Markov chains
7. Initial distribution multiplied by matrix powers yields the state probability distribution at any time n

## Common Mistakes

1. **Incorrect matrix multiplication order**: Using P × π₀ instead of π₀ × P when computing state distributions after n steps
2. **Forgetting to sum over intermediate states**: When using Chapman-Kolmogorov, ensure summation covers all possible intermediate states
3. **Confusing Pⁿ with P × n**: The notation Pⁿ means matrix multiplication, not scalar multiplication
4. **Assuming row sums equal 1 always**: While true for stochastic matrices Pⁿ, errors in computation can violate this property, indicating calculation mistakes