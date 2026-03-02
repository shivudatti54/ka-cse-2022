# Markov Decision Process - Summary

## Key Definitions and Concepts

- **Markov Decision Process (MDP)**: A mathematical framework for modeling sequential decision-making where outcomes are partly random and partly controlled by an agent. Formally defined as a tuple (S, A, P, R, γ).

- **Markov Property**: The future state depends only on the current state, not on the history of states. Mathematically: P(Sₜ₊₁|Sₜ) = P(Sₜ₊₁|Sₜ, Sₜ₋₁, ...).

- **Policy (π)**: A mapping from states to actions. Can be deterministic π(s) = a or stochastic π(a|s).

- **State Value Function Vπ(s)**: Expected return when starting from state s and following policy π.

- **Action Value Function Qπ(s,a)**: Expected return when starting from state s, taking action a, and following policy π.

- **Optimal Policy (π\*)**: The policy that maximizes expected cumulative reward.

## Important Formulas and Theorems

- **Bellman Equation for Vπ**: Vπ(s) = Σₐ π(a|s) Σₛ' P(s'|s,a)[R(s,a,s') + γVπ(s')]

- **Bellman Equation for Qπ**: Qπ(s,a) = Σₛ' P(s'|s,a)[R(s,a,s') + γ Σₐ' π(a'|s')Qπ(s',a')]

- **Optimal Value Function**: V*(s) = maxₐ Σₛ' P(s'|s,a)[R(s,a,s') + γV*(s')]

- **Optimal Q-function**: Q*(s,a) = Σₛ' P(s'|s,a)[R(s,a,s') + γ maxₐ' Q*(s',a')]

## Key Points

- MDP provides a formal structure for reinforcement learning problems
- The five components: States (S), Actions (A), Transition Probabilities (P), Rewards (R), Discount Factor (γ)
- Discount factor γ ∈ [0, 1] ensures convergence and models time preference
- Higher γ makes agent consider future rewards more; lower γ prioritizes immediate rewards
- The goal is to find π\* that maximizes expected cumulative discounted reward
- Value functions can be computed recursively using Bellman equations
- Q-function relates to V-function: V*(s) = maxₐ Q*(s, a)

## Common Mistakes to Avoid

1. Confusing state value function V(s) with action value function Q(s, a)
2. Forgetting that transition probabilities sum to 1: Σₛ' P(s'|s,a) = 1
3. Using γ > 1, which causes divergence in value calculations
4. Not understanding that policies can be stochastic; not all policies are deterministic

## Revision Tips

1. Practice writing the Bellman equations from memory
2. Solve at least 2-3 simple MDP problems with 2-3 states
3. Remember the relationship: Q(s,a) = R + γ Σₛ' P(s'|s,a)V(s')
4. Review how Q-learning and other RL algorithms relate to solving MDPs
5. Focus on understanding the discount factor's role in ensuring finite values
