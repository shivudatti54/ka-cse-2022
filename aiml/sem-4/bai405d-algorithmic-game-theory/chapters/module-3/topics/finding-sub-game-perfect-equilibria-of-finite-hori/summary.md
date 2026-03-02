# Finding Sub-Game Perfect Equilibria of Finite Horizon Games: Backward Induction

=====================================================

### Definition

---

- A sub-game perfect equilibrium in a finite horizon game is a strategy profile that is a Nash equilibrium for each sub-game, and the players make decisions in a backward induction manner.
- A sub-game is a game that is played after a certain date but before a certain future date.

### Key Concepts

---

- **Backward Induction**: A method for finding sub-game perfect equilibria by working backwards from the last stage of the game.
- **Nash Equilibrium**: A strategy profile where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged.
- **Sub-Game Perfect Equilibrium**: A strategy profile that is a Nash equilibrium for each sub-game, and the players make decisions in a backward induction manner.

### Important Formulas and Theorems

---

- **Bellman Equation**: A recursive equation used to find the value function of a game, which represents the best possible payoff for each player at each stage.
- **Backward Induction Formula**: A formula used to find the optimal strategy for each player at each stage, by working backwards from the last stage of the game.
- **Fermat's Duality Principle**: A theorem that states that the optimal solution to a linear programming problem can be found by solving a dual problem.

### Backward Induction Procedure

---

1. **Find the value function**: Use the Bellman equation to find the value function of the game, which represents the best possible payoff for each player at each stage.
2. **Find the optimal strategy for each stage**: Use the backward induction formula to find the optimal strategy for each player at each stage, by working backwards from the last stage of the game.
3. **Verify the sub-game perfect equilibrium**: Verify that the strategy profile obtained is a Nash equilibrium for each sub-game, and that the players make decisions in a backward induction manner.

### Example

---

Suppose we have a finite horizon game with two players, where the game is played over three stages. The payoffs for each player at each stage are given by the following table:

| Stage | Player 1 | Player 2 |
| ----- | -------- | -------- |
| 1     | (1,1)    | (2,2)    |
| 2     | (3,3)    | (4,4)    |
| 3     | (5,5)    | (6,6)    |

Using backward induction, we can find the optimal strategy for each player at each stage. Starting from the last stage, we can find the optimal strategy for each player by working backwards from the last stage of the game.

### Code

---

There is no code required for this topic, as it is a theoretical concept in game theory. However, you can use the following Python code to illustrate the backward induction procedure:

```python
import numpy as np

def backward_induction(payoffs):
    # Initialize the value function
    v = np.zeros((len(payoffs), len(payoffs[0])))

    # Iterate over each stage
    for i in range(len(payoffs)):
        # Find the optimal strategy for each player at this stage
        for j in range(len(payoffs[0])):
            v[i, j] = max([payoffs[i, j][k] + v[i+1, k] for k in range(len(payoffs[0]))])

    return v

# Define the payoffs for the game
payoffs = [
    [[1, 1], [2, 2]],
    [[3, 3], [4, 4]],
    [[5, 5], [6, 6]]
]

# Find the optimal strategy using backward induction
v = backward_induction(payoffs)
print(v)
```

This code illustrates the backward induction procedure by finding the optimal strategy for each player at each stage, using the payoffs given in the table.
