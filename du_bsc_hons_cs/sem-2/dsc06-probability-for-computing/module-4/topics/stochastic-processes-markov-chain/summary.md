# Stochastic Processes and Markov Chains - Summary

## Key Definitions and Concepts

- **Stochastic Process**: A family of random variables {X(t) : t ∈ T} indexed by time, describing the evolution of a system with inherent randomness

- **Markov Chain**: A discrete-time stochastic process satisfying the Markov property: P(Xₙ₊₁ = j | Xₙ = i, Xₙ₋₁, ..., X₀) = P(Xₙ₊₁ = j | Xₙ = i)

- **Transition Probability Matrix**: A stochastic matrix P = [pᵢⱼ] where pᵢⱼ = P(Xₙ₊₁ = j | Xₙ = i), with non-negative entries and each row summing to 1

- **n-step Transition Probability**: pᵢⱼ⁽ⁿ⁾ = P(Xₙ = j | X₀ = i), computed as the (i,j) entry of Pⁿ

- **Stationary Distribution**: A probability vector π satisfying πP = π and Σπᵢ = 1; represents the long-run distribution of the chain

## Important Formulas and Theorems

- **Chapman-Kolmogorov Equation**: pᵢⱼ⁽ᵐ⁺ⁿ⁾ = Σₖ pᵢₖ⁽ᵐ⁾ × pₖⱼ⁽ⁿ⁾ for combining transition probabilities

- **Matrix Power Method**: P⁽ⁿ⁾ = Pⁿ gives all n-step transition probabilities

- **Stationary Distribution Equations**: πⱼ = Σᵢ πᵢpᵢⱼ for all j, or equivalently πP = π

- **Ergodic Theorem**: For an irreducible, aperiodic Markov chain, limₙ→∞ pᵢⱼ⁽ⁿ⁾ = πⱼ exists and is independent of initial state i

## Key Points

- The Markov property (memorylessness) is the defining characteristic of Markov chains—future depends only on present, not history

- Transition probability matrices are stochastic matrices: non-negative entries with each row summing to 1

- States that communicate (mutually accessible) form communication classes; a chain is irreducible if all states communicate

- Recurrent states are visited infinitely often (with probability 1); transient states may be visited only finitely many times

- Aperiodic states have period 1 (gcd of return times = 1); periodicity affects convergence to stationary distribution

- Absorbing states have pᵢᵢ = 1—once entered, never left

- Stationary distribution π represents the long-run proportion of time spent in each state; found by solving πP = π

- For irreducible, aperiodic chains, the limiting distribution equals the unique stationary distribution regardless of initial state

## Common Mistakes to Avoid

- Confusing transition probabilities pᵢⱼ (one-step) with pᵢⱼ⁽ⁿ⁾ (n-step); remember to use matrix powers for n > 1

- Forgetting the constraint Σπᵢ = 1 when solving for stationary distribution—without it, infinitely many solutions exist

- Assuming every Markov chain converges to a stationary distribution; convergence requires irreducibility and aperiodicity

- Mixing up rows and columns when reading the transition matrix—row i represents transitions FROM state i

- Misclassifying periodic states—check the greatest common divisor of all n with positive return probability

## Revision Tips

- Practice setting up transition matrices from word problems—identify states and determine one-step transition probabilities

- For stationary distributions, remember: with m states, you have m equations from πP = π, but one is redundant (replace with Σπᵢ = 1)

- Compute powers of 2×2 and 3×3 matrices by hand to understand the mechanics; verify your answers computationally

- Draw state diagrams to visualize the chain and verify your transition matrix entries

- Memorize key results about long-run behavior: irreducible + aperiodic ⇒ unique stationary distribution and convergence to it