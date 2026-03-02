# Q-Learning

## Introduction

Q-learning is a model-free reinforcement learning algorithm used to learn the optimal policy in a Markov Decision Process (MDP). It is an off-policy algorithm, meaning that it can learn from experiences gathered without following the same policy it will use at deployment. Q-learning is one of the most popular reinforcement learning algorithms due to its simplicity and effectiveness.

## Q-Learning Algorithm

The Q-learning algorithm updates the action-value function (Q-function) based on the Temporal Difference (TD) error. The Q-function represents the expected return when taking a particular action in a particular state.

### Q-Learning Update Rule

The Q-learning update rule is as follows:

Q(s, a) ← Q(s, a) + α[r + γmax(Q(s', a')) - Q(s, a)]

where:

- Q(s, a) is the current estimate of the Q-function
- α is the learning rate
- r is the reward received after taking action a in state s
- γ is the discount factor
- max(Q(s', a')) is the maximum Q-value of the next state s'

### How Q-Learning Works

The Q-learning algorithm works as follows:

1. Initialize the Q-function with arbitrary values.
2. Choose an action a in the current state s using an exploration strategy (e.g., ε-greedy).
3. Take action a and observe the next state s' and reward r.
4. Update the Q-function using the Q-learning update rule.
5. Repeat steps 2-4 until convergence.

## Example: Q-Learning in a Grid World

Consider a grid world where an agent can move up, down, left, or right. The goal is to reach the terminal state (T) from the starting state (S). The agent receives a reward of -1 for each step and a reward of 10 for reaching the terminal state.

|     |     |     |
| --- | --- | --- |
| S   |     |     |
|     |     |     |
|     |     | T   |

The Q-learning algorithm can be used to learn the optimal policy in this grid world. The Q-function will represent the expected return when taking a particular action in a particular state.

## Advantages and Disadvantages of Q-Learning

Advantages:

- Q-learning is a model-free algorithm, meaning that it does not require knowledge of the transition model or reward function.
- Q-learning is an off-policy algorithm, meaning that it can learn from experiences gathered without following the same policy it will use at deployment.

Disadvantages:

- Q-learning can suffer from the curse of dimensionality, meaning that the number of states and actions can be very large.
- Q-learning can be slow to converge, especially in complex environments.

## Exam Tips

1. Understand the Q-learning update rule and how it is used to update the Q-function.
2. Know how to choose an action using an exploration strategy (e.g., ε-greedy).
3. Understand the advantages and disadvantages of Q-learning.
4. Be able to apply Q-learning to a simple problem, such as the grid world example.
5. Know how to initialize the Q-function and choose the learning rate and discount factor.
6. Understand the concept of convergence in Q-learning.
