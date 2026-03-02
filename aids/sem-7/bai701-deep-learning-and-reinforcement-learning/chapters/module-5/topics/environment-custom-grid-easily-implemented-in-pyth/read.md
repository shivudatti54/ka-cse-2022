# **Environment: Custom Grid**

### Introduction

In reinforcement learning, an environment is a crucial component that interacts with the agent and provides feedback on its actions. A custom grid environment is a simple, easily implementable environment that can be used to test various reinforcement learning algorithms, such as Q-learning, SARSA, and Deep Q-Networks (DQN). In this section, we will discuss the concept of a custom grid environment, its characteristics, and how to implement it in Python.

### Characteristics of a Custom Grid Environment

A custom grid environment is a discrete environment where the agent navigates through a grid of cells. Each cell may have a reward associated with it, and the agent's goal is to maximize its cumulative reward. The environment has the following characteristics:

- **Discrete Space**: The environment is divided into a finite number of cells (or states).
- **Discrete Actions**: The agent can take a fixed number of discrete actions (e.g., up, down, left, right).
- **Reward Function**: The environment has a reward function that assigns a numerical value to each state-action pair.

### Implementation in Python

We can implement a custom grid environment in Python using a simple grid data structure. Here's an example implementation:

```python
import numpy as np

class GridEnvironment:
    def __init__(self, width=3, height=3, reward_matrix=None):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width))
        self.action_space = ['up', 'down', 'left', 'right']
        self.state_space = [(i, j) for i in range(height) for j in range(width)]
        if reward_matrix is None:
            self.reward_matrix = self.default_reward_matrix()
        else:
            self.reward_matrix = reward_matrix

    def default_reward_matrix(self):
        # Example reward matrix with positive rewards for visiting cells
        reward_matrix = np.zeros((self.height, self.width))
        reward_matrix[0, 0] = 1  # Start cell has a reward
        reward_matrix[self.height - 1, self.width - 1] = 1  # End cell has a reward
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                reward_matrix[i, j] = 0.5  # All other cells have a moderate reward
        return reward_matrix

    def reset(self):
        # Reset the environment to a random initial state
        import random
        state = random.choice(self.state_space)
        self.grid[state[0], state[1]] = 1  # Mark the current state as visited
        return state

    def step(self, action):
        # Take a step in the specified direction
        x, y = self.grid.nonzero()
        state = (x[y == self.grid[x[y == self.grid[x[y == self.grid[x[y == self.grid[x[y == 0]]] == 1]]]]], y[y == self.grid[x[y == self.grid[x[y == self.grid[x[y == self.grid[x[y == 0]]] == 1]]]]])
        if action == 'up' and state[0] > 0:
            state = (state[0] - 1, state[1])
        elif action == 'down' and state[0] < self.height - 1:
            state = (state[0] + 1, state[1])
        elif action == 'left' and state[1] > 0:
            state = (state[0], state[1] - 1)
        elif action == 'right' and state[1] < self.width - 1:
            state = (state[0], state[1] + 1)
        self.grid[state[0], state[1]] = 1  # Mark the new state as visited
        reward = self.reward_matrix[state[0], state[1]]
        done = state == (self.height - 1, self.width - 1)  # Check if the agent reached the end cell
        return state, reward, done

    def render(self):
        # Print the grid environment
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i, j] == 1:
                    print('X', end=' ')
                else:
                    print('.', end=' ')
            print()
```

### Example Usage

```python
env = GridEnvironment()
state = env.reset()
while True:
    action = input("Enter action (up, down, left, right): ")
    state, reward, done = env.step(action)
    print("State:", state)
    print("Reward:", reward)
    print("Done:", done)
    if done:
        break
```

This code creates a 3x3 grid environment with a default reward matrix. The agent starts at a random initial state and navigates through the grid, taking actions based on user input. The environment provides feedback in the form of rewards and terminal states.
