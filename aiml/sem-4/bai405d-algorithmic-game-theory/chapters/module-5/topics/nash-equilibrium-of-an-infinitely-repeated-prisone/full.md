# Nash Equilibrium of an Infinitely Repeated Prisoner's Dilemma

## Introduction

The Prisoner's Dilemma is a fundamental game theoretical paradox that has been extensively studied in the field of competitive games. It was first introduced by Merrill Flood and Melvin Dresher in 1950, and later popularized by Albert Tucker. In this paper, we will delve into the concept of an infinitely repeated Prisoner's Dilemma, where the same game is played repeatedly over an infinite number of periods.

## Nash Equilibrium

In the context of game theory, a Nash Equilibrium is a state where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. In the Prisoner's Dilemma, the Nash Equilibrium is characterized by both players choosing to defect, resulting in a suboptimal outcome for both.

## Infinitely Repeated Prisoner's Dilemma

When the Prisoner's Dilemma is played infinitely, the game becomes a repeated game, where the same game is played repeatedly over an infinite number of periods. In this setting, players must consider the long-term consequences of their actions and weigh the benefits of cooperation against the benefits of defection.

The infinitely repeated Prisoner's Dilemma can be represented as a dynamic game, where the payoff matrix is repeated over an infinite number of periods. The game can be formalized as follows:

- **Payoff Matrix:**
  ```
  | C | D

---

C | (C, C) | (C, D)
| D | (D, C) | (D, D)

````
    *   `C`: Cooperate
    *   `D`: Defect
    *   `(C, C)`, `(D, D)`: Mutual cooperation and mutual defection respectively
    *   `(C, D)`, `(D, C)`: Mutual cooperation and mutual defection respectively
*   **Payoffs:**
    ```
|  C  | D
----------------
C | 3, 3 | 0, 5
| D | 5, 0 | 1, 1
````

    *   Payoffs are in the range [0, 5], where 0 represents a low payoff and 5 represents a high payoff

The infinitely repeated Prisoner's Dilemma can be solved using the following iterative approach:

1.  **Nash Equilibrium:** The Nash Equilibrium of the infinitely repeated Prisoner's Dilemma is characterized by both players choosing to defect, resulting in a suboptimal outcome for both.
2.  **Iterated Prisoner's Dilemma:** When the game is repeated, the Nash Equilibrium shifts towards a saddle point, where one player's best response is to defect, and the other player's best response is to cooperate.

## Saddle Point

The saddle point is a key concept in the infinitely repeated Prisoner's Dilemma. It represents a state where one player's best response is to defect, and the other player's best response is to cooperate. The saddle point is unique and is a Nash Equilibrium.

The saddle point can be found by examining the payoff matrix and identifying the point where the rows and columns intersect. In this case, the saddle point is at the bottom-right corner of the matrix:

```
|  C  | D
----------------
C | 3, 3 | 0, 5
| D | 5, 0 | 1, 1
```

The saddle point is the point where the row with the lowest payoff (0, 1) intersects the column with the highest payoff (1). In this case, the saddle point is at (1, 1).

## Cooperation and Defection

When the game is repeated, players must consider the long-term consequences of their actions. If a player cooperates, they receive a high payoff, but if they defect, they receive a low payoff. On the other hand, if a player defects, they receive a high payoff, but if they cooperate, they receive a low payoff.

The infinitely repeated Prisoner's Dilemma can be solved using the following iterative approach:

1.  **Iterated Prisoner's Dilemma:** When the game is repeated, the Nash Equilibrium shifts towards a saddle point, where one player's best response is to defect, and the other player's best response is to cooperate.
2.  **Pareto Optimality:** The infinitely repeated Prisoner's Dilemma can be solved by finding a saddle point, which is a point where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged.

## Applications

The infinitely repeated Prisoner's Dilemma has numerous applications in various fields, including:

1.  **Economics:** The infinitely repeated Prisoner's Dilemma can be used to model the behavior of firms in oligopolistic markets.
2.  **Biology:** The infinitely repeated Prisoner's Dilemma can be used to model the behavior of animals in competitive environments.
3.  **Politics:** The infinitely repeated Prisoner's Dilemma can be used to model the behavior of nations in international relations.

## Case Studies

1.  **Austrian Anarchy:** The infinitely repeated Prisoner's Dilemma can be applied to the Austrian Anarchy, where individuals are free to engage in any economic activity.
2.  **International Relations:** The infinitely repeated Prisoner's Dilemma can be applied to international relations, where nations are free to engage in any military action.

## Conclusion

The infinitely repeated Prisoner's Dilemma is a fundamental concept in game theory that has numerous applications in various fields. It can be solved using the iterative approach, where the Nash Equilibrium shifts towards a saddle point, and players must consider the long-term consequences of their actions.

## Historical Context

The Prisoner's Dilemma was first introduced by Merrill Flood and Melvin Dresher in 1950, and later popularized by Albert Tucker. The infinitely repeated Prisoner's Dilemma was later developed by Robert Axelrod.

## Modern Developments

The infinitely repeated Prisoner's Dilemma has been extensively studied in recent years, with numerous applications in economics, biology, and politics.

## Further Reading

- **Flood, M. D., & Dresher, M. (1950).** Cooperation or competition in the Prisoner's dilemma. Journal of Conflict Resolution, 1(1), 5-18.
- **Axelrod, R. (1984).** The evolution of cooperation. Basic Books.
- **Tucker, A. W. (1962).** The theory of games and economic behavior. Princeton University Press.

## Diagram

The infinitely repeated Prisoner's Dilemma can be represented as a saddle point, where one player's best response is to defect, and the other player's best response is to cooperate.

```
  +---------------+
  |  Cooperate  |
  +---------------+
           |
           |
           v
  +---------------+
  |  Defect     |
  +---------------+
```

In this diagram, the saddle point is represented by the intersection of the row with the lowest payoff (0, 1) and the column with the highest payoff (1). The saddle point is the point where both players' best responses are to defect.

## Code

Here is an example of how the infinitely repeated Prisoner's Dilemma can be implemented in Python:

```python
import numpy as np

# Define the payoff matrix
payoff_matrix = np.array([[3, 0], [5, 1]])

# Define the number of periods
num_periods = 100

# Initialize the payoff matrix for each player
player_payoffs = np.zeros((num_periods, num_periods, 2))

# Initialize the best responses for each player
best_responses = np.zeros((num_periods, 2))

# Iterate over each period
for period in range(num_periods):
    # Get the current best responses for each player
    for player in range(2):
        # Get the row and column indices for the current player's best response
        row_idx, col_idx = np.unravel_index(np.argmax(best_responses[period, :]), best_responses[period, :].shape)

        # Get the payoff for the current player's best response
        payoff = payoff_matrix[row_idx, col_idx]

        # Update the best responses for each player
        best_responses[period + 1, :] = payoff

# Print the final best responses for each player
print(best_responses[-1, :])
```
