# **Framework of Reinforcement Learning**

### Overview

- **Definition**: Reinforcement Learning (RL) is a type of machine learning where an agent learns to take actions in an environment to maximize a reward.
- **Key Components**:
  - **Environment**: The external world where the agent interacts.
  - **Agent**: The decision-maker that takes actions.
  - **Actions**: The decisions taken by the agent.
  - **Rewards**: The feedback received by the agent for its actions.
  - **Policy**: The mapping from states to actions.
  - **Value Function**: The expected return for a given state.

### Important Formulas and Definitions

- **Q-Function**: Q(s, a) = E[r + γmax(Q(s', a'))|s=a]
  - Q-function represents the expected return for taking action a in state s.
- **Policy-Value Decomposition**: V(s) = E[r + γπ(a|s)] Q(s, a) = E[r + γmax(Q(s', a'))|s=a]
  - Q-function and policy-value decomposition are fundamental to RL.
- **Bellman Equation**: V(s) = E[r + γV(s')]
  - The Bellman equation is a fundamental equation in RL.

### Theorems

- **Optimality Theorem**: A policy is optimal if and only if it satisfies the Bellman equation.
- **Finite Horizon Problem**: The optimal policy is the one that maximizes the cumulative reward over a finite horizon.

### Key Concepts

- **Exploration-Exploitation Trade-off**: The trade-off between exploring new actions and exploiting known good actions.
- **Off-Policy Learning**: Learning a policy without following the same exploration strategy as the learned policy.
- **On-Policy Learning**: Learning a policy using the same exploration strategy as the learned policy.
