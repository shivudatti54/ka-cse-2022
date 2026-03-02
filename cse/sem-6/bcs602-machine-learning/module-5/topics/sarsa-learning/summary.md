# SARSA Learning

## Summary

SARSA learning is a type of reinforcement learning algorithm that learns the optimal policy in a Markov Decision Process (MDP). It is an on-policy, temporal-difference (TD) learning algorithm that updates the value function and policy simultaneously.

- The SARSA learning algorithm consists of an agent, environment, actions, states, reward, policy, and value function.
- The algorithm works by initializing the policy and value function, selecting an action, taking the action, getting a reward, observing the next state, updating the value function, and updating the policy.
- The SARSA learning algorithm can be mathematically represented as Q(s, a) ← Q(s, a) + α[r + γQ(s', a') - Q(s, a)] for the value function update and π(s) ← argmax(Q(s, a)) for the policy update.

### Important Formulas, Definitions, and Theorems

- **Value Function Update**: Q(s, a) ← Q(s, a) + α[r + γQ(s', a') - Q(s, a)]
- **Policy Update**: π(s) ← argmax(Q(s, a))
- **Markov Decision Process (MDP)**: A mathematical framework for modeling decision-making problems.
- **Reinforcement Learning**: A type of machine learning that involves learning from interactions with an environment.

### Key Points

- SARSA learning is an on-policy, TD learning algorithm.
- The SARSA learning algorithm updates the value function and policy simultaneously.
- SARSA learning can be used in both episodic and continuous tasks.
- The SARSA learning algorithm can be modified to use eligibility traces for more efficient learning.
- SARSA learning is a type of reinforcement learning algorithm.
- The SARSA learning algorithm is used to learn the optimal policy in a Markov Decision Process (MDP).

### Revision Tips

1.  Practice implementing SARSA learning in a programming language, such as Python.
2.  Review the mathematical representation of the SARSA learning algorithm.
3.  Apply SARSA learning to different problems, such as the grid world example.
4.  Compare SARSA learning with other reinforcement learning algorithms, such as Q-learning.
