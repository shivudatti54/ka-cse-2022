# Stationary Distribution And Absorbing States - Summary

## Key Definitions

- **Stationary Distribution**: A probability vector π satisfying πP = π, where P is the transition matrix of a Markov chain.

- **Regular Markov Chain**: A Markov chain where some power of the transition matrix contains only positive entries.

- **Absorbing State**: A state i where pᵢᵢ = 1, meaning once entered, the chain can never leave.

- **Transient State**: A state that is not absorbing; the chain may leave and potentially never return.

- **Fundamental Matrix**: Q = (I - R)⁻¹, where Q contains probabilities of transitions among transient states in canonical form.

- **Absorption Probability**: The probability that the chain will eventually be absorbed in a particular absorbing state.

## Important Formulas

- Stationary distribution: πP = π, Σπᵢ = 1
- Limit behavior: lim_{n→∞} Pⁿ = 1ᵀπ (for regular chains)
- Fundamental matrix: Q = (I - R)⁻¹
- Absorption probabilities: B = QR

## Key Points

1. A stationary distribution represents the equilibrium state where the probability distribution remains unchanged through transitions.

2. For regular Markov chains, the stationary distribution is unique and the chain converges to it from any initial state.

3. Absorbing states have self-transition probability equal to 1; they form closed communicating classes.

4. In canonical form, the transition matrix partitions into Q (transient-to-transient), R (transient-to-absorbing), zero matrix, and identity block.

5. The fundamental matrix Q gives expected numbers of visits to each transient state before absorption.

6. Every finite irreducible Markov chain has at least one stationary distribution.

7. Aperiodic chains converge to their stationary distribution; periodic chains may oscillate.

## Common Mistakes

1. Forgetting to apply the normalization condition Σπᵢ = 1 when computing stationary distributions.

2. Confusing periodic chains with non-converging chains—periodic chains still have stationary distributions.

3. Incorrectly identifying absorbing states; remember pᵢᵢ must equal 1 exactly.

4. Attempting to invert (I - R) when R contains values making the matrix singular.