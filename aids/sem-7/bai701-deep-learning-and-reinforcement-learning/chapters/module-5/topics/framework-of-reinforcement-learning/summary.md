# **Framework of Reinforcement Learning**

### Definitions

- **Reinforcement Learning (RL)**: A type of machine learning where an agent learns to take actions in an environment to maximize a reward.
- **Agent**: The decision-maker that interacts with the environment.
- **Environment**: The external world that the agent interacts with.
- **State**: The current situation or status of the environment.
- **Action**: The decision made by the agent.
- **Reward**: The feedback received by the agent for its action.
- **Policy**: The mapping from states to actions.
- **Value Function**: The expected return for taking an action in a given state.

### Key Concepts

- **Markov Decision Process (MDP)**: A mathematical model used to represent RL problems.
  - States
  - Actions
  - Transition probabilities
  - Rewards
  - Discount factor
- **Q-Function**: The expected return for taking an action in a given state.
- **Action-Value Function**: The expected return for taking a specific action in a given state.
- **Policy-Value Function**: The expected return for following a specific policy in a given state.

### Important Formulas

- **Bellman Equation**: The recursive equation used to compute the Q-function.
  - Q(s, a) = max_a' [R(s, a) + γQ(s', a')]
- **Value Iteration**: The algorithm used to compute the value function.
  - V(s) = max_a Q(s, a)
- **Policy Iteration**: The algorithm used to compute the policy.
  - π(s) = argmax_a [R(s, a) + γV(s)]

### Theorems

- **Optimal Control Problem**: A problem that seeks to find the optimal policy that maximizes the expected return.
- **First-Order Optimal Control Problem**: A problem that seeks to find the optimal policy that maximizes the expected return, subject to a constraint on the action space.

### Important Definitions

- **Stationary Reward**: A reward that does not depend on time.
- **Time-Varying Reward**: A reward that depends on time.
- **Episodic**: A problem that is solved in episodes, where the agent resets to the initial state at the end of each episode.
- **Continuous**: A problem that is solved in continuous time.
