# Equilibrium in a Single Population

=====================================

## Introduction

---

In algorithmic game theory, an equilibrium is a stable state where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. In this section, we will explore the concept of equilibrium in a single population, focusing on mixed strategy Nash equilibrium.

## Definitions

---

- **Mixed Strategy**: A mixed strategy is a probability distribution over a set of pure strategies. It is a way to randomize one's actions to make them unpredictable to others.
- **Nash Equilibrium**: A Nash equilibrium is a concept in game theory that describes a stable state where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged.
- **Single Population Game**: A single population game is a game where there is only one player, and the goal is to maximize their payoff.

## Equilibrium in a Single Population

---

In a single population game, the goal is to maximize the payoff. To achieve this, the player must choose the optimal strategy. The optimal strategy is the strategy that results in the highest payoff.

### Key Concepts

- **Expected Value**: The expected value is the average payoff that a player can expect to receive when using a particular strategy.
- **Payoff Matrix**: A payoff matrix is a table that shows the payoffs for each possible combination of strategies.
- **Dominant Strategy**: A dominant strategy is a strategy that is better than any other strategy, regardless of what the other player chooses.

### Example

Suppose we have a single population game where the player can choose between two strategies: A and B. The payoff matrix is as follows:

|     | A   | B   |
| --- | --- | --- |
| A   | 10  | 5   |
| B   | 5   | 10  |

In this example, the dominant strategy is A, because it results in a higher payoff regardless of what the other player chooses.

### Mixed Strategy Nash Equilibrium

In a single population game, the mixed strategy Nash equilibrium is a stable state where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged.

To find the mixed strategy Nash equilibrium, we need to calculate the expected value of each strategy and compare them.

Let's say the player chooses mixed strategy α = [p, q] = [0.4, 0.6], where p is the probability of choosing strategy A and q is the probability of choosing strategy B.

The expected value of the payoff is given by:

EV(A) = 0.4 \* 10 + 0.6 \* 5 = 6.6

EV(B) = 0.4 \* 5 + 0.6 \* 10 = 8.4

Since EV(B) > EV(A), the player should choose strategy B.

### Example Code (Python)

```python
import numpy as np

# Payoff matrix
payoff_matrix = np.array([[10, 5], [5, 10]])

# Player's mixed strategy
p = 0.4
q = 0.6

# Expected value of the payoff
ev_a = p * payoff_matrix[0, 0] + q * payoff_matrix[0, 1]
ev_b = p * payoff_matrix[1, 0] + q * payoff_matrix[1, 1]

print("Expected value of A:", ev_a)
print("Expected value of B:", ev_b)

if ev_b > ev_a:
    print("Player should choose B")
else:
    print("Player should choose A")
```

This code calculates the expected value of the payoff for each strategy and prints the result.

### Conclusion

In this study material, we explored the concept of equilibrium in a single population, focusing on mixed strategy Nash equilibrium. We defined key concepts such as mixed strategy, Nash equilibrium, and expected value, and provided an example to illustrate the concept. We also provided code to calculate the expected value of the payoff for each strategy.
