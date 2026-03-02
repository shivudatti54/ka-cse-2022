# Introduction To Stochastic Process - Summary

## Key Definitions

- **Stochastic Process**: A family of random variables {X(t) : t ∈ T} defined on a probability space, where t represents time. Each X(t) is a random variable, and the set of all possible values is the state space S.

- **Sample Path (Realization)**: The sequence of observed values when fixing a particular outcome ω ∈ Ω. For discrete time, this is a sequence {x₀, x₁, x₂, ...}.

- **State Space (S)**: The set of all possible values that the stochastic process can take at any time point.

- **Index Set (T)**: The time parameter set over which the process is defined; can be discrete or continuous.

## Important Formulas

- **Strict Stationarity**: P(X(t₁) ≤ x₁, ..., X(tₖ) ≤ xₖ) = P(X(t₁+τ) ≤ x₁, ..., X(tₖ+τ) ≤ xₖ) for all t, τ, k

- **Wide-Sense Stationarity**: E[X(t)] = μ (constant) and Cov(X(t), X(s)) = Cov(X(t+τ), X(s+τ)) for all t, s, τ

- **Markov Property**: P(X(t) ∈ A | X(u), 0 ≤ u ≤ s) = P(X(t) ∈ A | X(s)) for s < t

## Key Points

1. A stochastic process extends probability theory by considering how random variables evolve over time, not just their static distribution.

2. Four main classifications exist: discrete time/discrete state, discrete time/continuous state, continuous time/discrete state, and continuous time/continuous state.

3. Sample paths provide a concrete way to visualize stochastic processes by showing one possible realization of the random evolution.

4. Stationarity implies statistical properties remain constant over time, greatly simplifying analysis and prediction.

5. Wide-sense stationarity is weaker than strict stationarity; all strictly stationary processes with finite variance are wide-sense stationary, but not vice versa.

6. The Markov property is crucial because it creates a "memoryless" process where only the current state matters for future predictions.

7. Independent increments mean changes in non-overlapping time intervals are statistically independent—a key property for many stochastic process models.

8. In computer science, stochastic processes model randomized algorithms, network traffic, queuing systems, and form the mathematical foundation of Markov chain-based machine learning.

## Common Mistakes

1. **Confusing time parameter with state**: Students often mix up whether a particular set represents time indices or possible states. Remember T is always time, S is always the set of possible values.

2. **Misunderstanding stationarity**: Assuming a process is stationary just because it looks "similar" over time, without checking the formal mathematical conditions.

3. **Forgetting that X(t) is a random variable**: At any fixed time t, X(t) is a random variable with its own distribution. Only when considering the entire process do we get the stochastic structure.

4. **Applying Markov property incorrectly**: The Markov property requires that the future depends ONLY on the present state. Many processes in nature do NOT have this property.