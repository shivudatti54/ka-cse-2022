# Markov Chains - Summary

## Key Definitions

- **Markov Chain**: A stochastic process {X₀, X₁, ...} where the future state depends only on the current state (Markov property): P(Xₙ₊₁=j | Xₙ=i, history) = P(Xₙ₊₁=j | Xₙ=i)

- **State Space (S)**: The finite or countable set of all possible states {s₁, s₂, ..., sₖ}

- **Transition Matrix (P)**: A stochastic matrix where entry pᵢⱼ represents P(Xₙ₊₁=sⱼ | Xₙ=sᵢ), with each row summing to 1

- **Stationary Distribution (π)**: A probability vector satisfying πP = π, representing a distribution that remains unchanged under the transition matrix

- **Absorbing State**: A state sᵢ where pᵢᵢ = 1, from which escape is impossible

## Important Formulas

- **Chapman-Kolmogorov**: pᵢⱼ⁽ⁿ⁾ = ∑ₖ pᵢₖ⁽ᵐ⁾ pₖⱼ⁽ⁿ⁻ᵐ⁾ for 0 < m < n

- **n-step transitions**: P⁽ⁿ⁾ = Pⁿ (matrix exponentiation)

- **Stationary distribution**: Solve πP = π with ∑πᵢ = 1

- **Absorption probability**: From transient state i to absorbing state j, computed using fundamental matrix N = (I - Q)⁻¹

## Key Points

1. The Markov property (memorylessness) is the fundamental assumption enabling mathematical tractability.

2. Every row of a valid transition matrix sums to 1 (∑ⱼ pᵢⱼ = 1 for all i).

3. An irreducible Markov chain has a unique stationary distribution; regular chains converge to it.

4. Transient states are visited only finitely many times; recurrent states are visited infinitely often.

5. The transition matrix Pⁿ provides all n-step transition probabilities through matrix multiplication.

6. Absorbing Markov chains eventually settle into absorbing states; analysis focuses on transient state behavior.

7. PageRank is a famous application of Markov chains to web page ranking.

8. Long-run proportions equal stationary distributions in ergodic chains.

## Common Mistakes

1. **Forgetting row normalization**: Failing to ensure transition matrix rows sum to 1, making the matrix invalid.

2. **Confusing n-step probabilities**: Using P instead of Pⁿ when computing probabilities after n transitions.

3. **Omitting the probability sum constraint**: Solving πP = π without adding ∑πᵢ = 1 leads to infinite solutions.

4. **Ignoring initial conditions**: The stationary distribution is approached in the limit; transient behavior depends on where the chain starts.

5. **Misidentifying absorbing states**: A state is absorbing only if pᵢᵢ = 1, not merely when pᵢᵢ is high.