# **Environment: Custom Grid (Easily Implemented in Python)**

### Key Points

- A custom grid environment is a simple and easily implementable environment for reinforcement learning.
- It consists of a grid of states, where each state is a tuple of coordinates (x, y).
- The environment can be defined using Python.
- The environment has the following properties:
  - **States**: A set of discrete states, represented as tuples of coordinates.
  - **Actions**: A set of discrete actions, typically movement (up, down, left, right).
  - **Transition**: The next state is determined by the current state and action.
  - **Reward**: The reward function assigns a numerical value to each state-action pair.

### Definitions and Theorems

- **State**: A discrete representation of the environment's current situation.
- **Action**: A discrete input that determines the next state.
- **Transition**: The next state is determined by the current state and action.

### Formulas

- **Transition model**: P(s'|s, a) = probability of transitioning from state s to state s' given action a.
- **Reward function**: R(s, a) = reward for taking action a in state s.

### Implementing a Custom Grid Environment in Python

- Import the necessary libraries: `numpy` and `random`.
- Define the grid size and the possible actions (up, down, left, right).
- Implement the transition model and reward function.
- Define the environment class and its methods (step, reset).

### Example Python Code

```python
import numpy as np
import random

class CustomGridEnvironment:
    def __init__(self, grid_size=10, actions=['up', 'down', 'left', 'right']):
        self.grid_size = grid_size
        self.actions = actions
        self.states = [(x, y) for x in range(grid_size) for y in range(grid_size)]
        self.transition_model = {
            (x, y): {a: (x+1, y) if a == 'down' else (x-1, y) if a == 'up' else (x, y+1) if a == 'right' else (x, y-1)} for x in range(grid_size) for y in range(grid_size)
        }
        self.reward_function = {
            (x, y, 'down'): 1, (x, y, 'up'): -1, (x, y, 'right'): 1, (x, y, 'left'): -1
        }

    def step(self, state, action):
        next_state = self.transition_model[state][action]
        reward = self.reward_function[state, action]
        return next_state, reward

    def reset(self):
        return random.choice(self.states)
```

Note: This is a basic implementation and you may need to add more features (e.g., edge cases, obstacles) to your environment.
