# **Environment: Custom Grid (Easily Implemented in Python)**

## **Introduction**

In the context of Deep Reinforcement Learning, an environment is a crucial component that interacts with the agent, providing feedback in the form of rewards or penalties. A custom grid environment is a simple and easily implementable example of an environment that can be used to learn various reinforcement learning algorithms. In this study material, we will explore the concept of custom grid environments, their implementation in Python, and their applications in Deep Reinforcement Learning.

## **What is an Environment?**

An environment is a mathematical representation of a real-world or simulated scenario that an agent interacts with. It provides the agent with a set of possible actions, and for each action, it determines the next state and reward. The environment can be thought of as a black box that the agent does not need to understand in detail.

**Key Concepts:**

- **State:** The current situation or status of the environment, which can be represented as a vector of features.
- **Action:** A possible action that the agent can take in the current state.
- **Transition:** The next state and reward that the environment provides after the agent takes an action.
- **Reward:** A scalar value that the environment provides as feedback for the agent's action.

## **Custom Grid Environment**

A custom grid environment is a simple environment that consists of a grid of cells, each representing a state. The agent can move up, down, left, or right to an adjacent cell. The environment provides a reward for reaching a goal cell or a penalty for hitting a obstacle cell.

## **Implementation in Python**

Here is a simple implementation of a custom grid environment in Python using the Gym library:

```python
import gym
import numpy as np

class CustomGridEnv(gym.Env):
    def __init__(self, size=5, goal=10, obstacle=15):
        self.size = size
        self.goal = goal
        self.obstacle = obstacle
        self.state = np.array([0, 0])  # start at cell (0, 0)
        self.action_space = gym.spaces.Discrete(4)  # up, down, left, right
        self.observation_space = gym.spaces.Box(low=0, high=size*size, shape=(size*size,), dtype=np.uint8)

    def step(self, action):
        x, y = self.state
        if action == 0:  # up
            y = max(0, y-1)
        elif action == 1:  # down
            y = min(self.size-1, y+1)
        elif action == 2:  # left
            x = max(0, x-1)
        elif action == 3:  # right
            x = min(self.size-1, x+1)

        reward = -1
        done = False
        if [x, y] == [self.goal, self.goal]:
            reward = 10
            done = True
        elif [x, y] == [self.obstacle, self.obstacle]:
            reward = -10
            done = True

        self.state = np.array([x, y])
        return {
            'state': self.state.flatten(),
            'reward': reward,
            'done': done,
            'info': {}
        }

    def reset(self):
        self.state = np.array([0, 0])
        return {
            'state': self.state.flatten(),
            'reward': 0,
            'done': False,
            'info': {}
        }
```

## **Applications in Deep Reinforcement Learning**

Custom grid environments are commonly used in Deep Reinforcement Learning to learn various algorithms such as Deep Q-Networks (DQN), Policy Gradient Methods (PGMs), and Actor-Critic Methods (ACMs). The simple structure of the grid environment allows for a large number of trials to be simulated quickly, making it an ideal environment for training agents.

**Key Concepts:**

- **Deep Q-Networks (DQN):** A type of reinforcement learning algorithm that uses a neural network to approximate the Q-function.
- **Policy Gradient Methods (PGMs):** A type of reinforcement learning algorithm that uses a neural network to learn the policy.
- **Actor-Critic Methods (ACMs):** A type of reinforcement learning algorithm that combines the actor and critic components.

By understanding the custom grid environment and its applications in Deep Reinforcement Learning, you can develop a solid foundation in this exciting field.
