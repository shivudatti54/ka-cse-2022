# Markov Decision Processes and Bellman Equations - Summary

## Key Definitions and Concepts
- **MDP**: Tuple (S, A, P, R, γ) modeling sequential decisions under uncertainty
- **Policy**: Mapping π: S → P(A) specifying action selection rules
- **Value Function**: Expected long-term return from a state or state-action pair
- **Bellman Operator**: Contraction mapping ensuring convergence of DP methods

## Important Formulas and Theorems
- **Bellman Expectation Equation**:  
  V^π(s) = E_π[R_t+1 + γV^π(S_{t+1}) | S_t = s]
- **Bellman Optimality Equation**:  
  V*(s) = max_a E[R_t+1 + γV*(S_{t+1}) | S_t = s, A_t = a]
- **Value Iteration Update**:  
  V_{k+1}(s) ← max_a Σ_{s'} P(s'|s,a)[R(s,a,s') + γV_k(s')]
- **Policy Improvement Theorem**:  
  If Q^π(s,π'(s)) ≥ V^π(s) ∀s, then π' ≥ π

## Key Points
- MDPs require the Markov property: P(s_{t+1}|s_t,a_t) = P(s_{t+1}|h_t)
- Discount factor γ determines planning horizon (γ=0: myopic; γ→1: far-sighted)
- Value iteration converges to ε-optimal policy in O(log(1/ε)) iterations
- Curse of dimensionality makes large MDPs computationally challenging
- Partially Observable MDPs (POMDPs) extend MDPs for imperfect state information
- Robust MDPs (RMDPs) handle transition probability uncertainty
- Deep Reinforcement Learning approximates value functions using neural networks

## Common Mistakes to Avoid
- Confusing model-based (MDP) vs model-free (Q-learning) approaches
- Incorrectly applying max operator in policy evaluation steps
- Neglecting to normalize probabilities in transition matrices
- Assuming deterministic environments when problem specifies stochasticity

## Revision Tips
1. Practice deriving Bellman equations using conditional expectations
2. Implement value iteration for a 4x4 gridworld environment
3. Compare computational complexity: value vs policy iteration
4. Review recent papers on arXiv (search "distributional RL") for modern extensions
5. Use DU's High Performance Computing cluster to test large-scale MDPs

Length: 650 words