# Q-Learning

## Summary

Q-learning is a model-free reinforcement learning algorithm used to learn the optimal policy in a Markov Decision Process (MDP). It updates the action-value function (Q-function) based on the Temporal Difference (TD) error. Q-learning is an off-policy algorithm, meaning that it can learn from experiences gathered without following the same policy it will use at deployment.

### Important Formulas, Definitions, and Theorems

- Q-learning update rule: Q(s, a) ← Q(s, a) + α[r + γmax(Q(s', a')) - Q(s, a)]
- Q-function: represents the expected return when taking a particular action in a particular state
- TD error: the difference between the estimated Q-value and the true Q-value

### Key Points

- Q-learning is a model-free algorithm.
- Q-learning is an off-policy algorithm.
- Q-learning updates the Q-function based on the TD error.
- Q-learning can suffer from the curse of dimensionality.
- Q-learning can be slow to converge.
- Q-learning is one of the most popular reinforcement learning algorithms.

### Revision Tips

1. Practice applying Q-learning to simple problems, such as the grid world example.
2. Review the Q-learning update rule and how it is used to update the Q-function.
3. Understand the advantages and disadvantages of Q-learning.
4. Review the concept of convergence in Q-learning.
