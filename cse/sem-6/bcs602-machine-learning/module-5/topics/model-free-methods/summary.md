# Model Free Methods

## Summary

Model-free methods are a type of reinforcement learning approach that does not require a predefined model of the environment. Q-learning and SARSA are two popular model-free methods that learn to estimate the expected return or utility of an action in a given state. Model-free methods have advantages such as flexibility, scalability, and robustness, but also disadvantages such as sample inefficiency, exploration-exploitation trade-off, and overfitting.

### Important Formulas, Definitions, and Theorems

- Q-learning update rule: Q(s, a) ← Q(s, a) + α[r + γmax(Q(s', a')) - Q(s, a)]
- SARSA update rule: Q(s, a) ← Q(s, a) + α[r + γQ(s', a') - Q(s, a)]
- Deep Q-Networks (DQN): A type of Q-learning that uses a deep neural network to approximate the Q-function.

### Key Points

- Model-free methods do not require a predefined model of the environment.
- Q-learning and SARSA are two popular model-free methods.
- Model-free methods have advantages such as flexibility, scalability, and robustness.
- Model-free methods have disadvantages such as sample inefficiency, exploration-exploitation trade-off, and overfitting.
- Model-free methods can be applied to a wide range of problems, including robotics, game playing, and recommendation systems.
- The exploration-exploitation trade-off is a key challenge in model-free methods.
- Model-free methods can overfit to the training data, resulting in poor performance in new environments.

### Revision Tips

1.  Review the Q-learning and SARSA update rules.
2.  Understand the advantages and disadvantages of model-free methods.
3.  Practice implementing a simple Q-learning or SARSA algorithm.
4.  Review the applications of model-free methods and think about how they can be applied to real-world problems.
