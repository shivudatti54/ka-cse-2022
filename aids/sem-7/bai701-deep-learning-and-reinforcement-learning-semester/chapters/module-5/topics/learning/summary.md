# Learning in Reinforcement Learning - Summary

## Key Definitions and Concepts

- Reinforcement Learning: A learning paradigm where an agent learns optimal decision-making through interaction with an environment, receiving rewards or penalties for actions.

- Policy: A mapping from states to actions that defines the agent's behavior. The goal of learning is to find an optimal policy maximizing cumulative rewards.

- Value Function: An estimate of expected cumulative reward from a given state (state-value V(s)) or state-action pair (action-value Q(s,a)).

- Temporal-Difference Learning: A learning method combining Monte Carlo and dynamic programming ideas, updating value estimates based on differences between consecutive predictions.

- TD Error: The difference between the current value estimate and a bootstrapped estimate incorporating observed reward and next-state value.

- Q-Learning: An off-policy TD control algorithm that learns the optimal action-value function directly.

- SARSA: An on-policy TD control algorithm that learns the value of the policy being followed.

## Important Formulas and Theorems

- TD(0) Update: V(s) ← V(s) + α[R + γV(s') - V(s)]
- Q-Learning Update: Q(s,a) ← Q(s,a) + α[R + γ max Q(s',a') - Q(s,a)]
- SARSA Update: Q(s,a) ← Q(s,a) + α[R + γQ(s',a') - Q(s,a)]
- Bellman Optimality Equation: V*(s) = max [R(s,a) + γ Σ P(s'|s,a)V*(s')]

## Key Points

- Learning in RL differs fundamentally from supervised learning—it requires no labeled data and learns from environmental feedback through actions.

- The exploration-exploitation dilemma is central: agents must balance trying new actions against using known rewarding actions.

- Value functions are learned through iterative updates, bootstrapping from current estimates to improve predictions.

- Q-learning is off-policy—it learns optimal values regardless of the exploration policy being followed.

- SARSA is on-policy—it learns values for the policy actually being executed, including exploration behavior.

- Learning rate (α) controls update magnitude; discount factor (γ) determines the importance of future rewards.

- Convergence requires appropriate exploration and learning rate conditions.

## Common Mistakes to Avoid

- Confusing on-policy and off-policy methods: Remember Q-learning learns optimal values even while exploring randomly, while SARSA learns the exploring policy values.

- Ignoring the discount factor: Without proper discounting, infinite horizon problems yield undefined values.

- Using excessively high learning rates causing instability or failure to converge.

- Forgetting that Q-learning takes the maximum over next-state actions, reflecting optimal future decisions.

## Revision Tips

- Practice tracing Q-learning updates through simple examples until the mechanism is intuitive.

- Create comparison tables distinguishing Q-learning from SARSA, including when each is preferred.

- Memorize the standard update equations and understand each parameter's role conceptually.

- Review the exploration-exploitation trade-off and be ready to explain with examples.

- Solve previous year DU examination questions on RL to understand the exam pattern and important topics.