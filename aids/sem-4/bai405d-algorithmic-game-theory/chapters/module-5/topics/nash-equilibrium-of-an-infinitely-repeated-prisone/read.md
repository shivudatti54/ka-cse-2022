# Nash Equilibrium of an Infinitely Repeated Prisoner’s Dilemma

### Introduction

The Prisoner's dilemma is a fundamental game theory concept that illustrates the conflict between individual and group rationality. In this study material, we will delve into the Nash equilibrium of an infinitely repeated Prisoner's dilemma, a variant of the classic game.

### Background

The Prisoner's dilemma is a two-player game where two prisoners are given the opportunity to confess or remain silent. The payoffs for each prisoner are as follows:

|                               | Prisoner A confesses | Prisoner A remains silent |
| ----------------------------- | -------------------- | ------------------------- |
| **Prisoner B confesses**      | A: 3, B: 3           | A: 0, B: 5                |
| **Prisoner B remains silent** | A: 5, B: 0           | A: 1, B: 1                |

A Nash equilibrium occurs when no player can improve their payoff by unilaterally changing their strategy, assuming the other player's strategy remains unchanged.

### Infinitely Repeated Prisoner's Dilemma

In an infinitely repeated Prisoner's dilemma, the game is played an infinite number of times. This allows us to analyze the long-term outcomes of different strategies.

### Strategies

There are two main strategies:

- **Confess**: Cooperate and confess
- **Stay Silent**: Cooperate and remain silent

We can represent these strategies as follows:

|                 | Stay Silent | Confess |
| --------------- | ----------- | ------- |
| **Stay Silent** | S, S        | S, C    |
| **Confess**     | C, S        | C, C    |

Here, S represents "Stay Silent" and C represents "Confess".

### Payoffs in an Infinitely Repeated Game

The payoffs for each strategy are as follows:

- **Stay Silent, Stay Silent**: 3 (both prisoners receive 1 point)
- **Stay Silent, Confess**: 4 (prisoner A receives 4 points, prisoner B receives 0 points)
- **Confess, Stay Silent**: 4 (prisoner A receives 0 points, prisoner B receives 4 points)
- **Confess, Confess**: 2 (both prisoners receive 0 points)

### Nash Equilibrium

To find the Nash equilibrium, we need to analyze the payoffs for each strategy.

- **Stay Silent**: Prisoner A's payoff is 3 if both prisoners stay silent, and 4 if prisoner B confesses. Prisoner B's payoff is 3 if both prisoners stay silent, and 0 if prisoner A confesses. Therefore, prisoner A prefers to stay silent if prisoner B stays silent, and prisoner B prefers to confess if prisoner A stays silent.
- **Confess**: Prisoner A's payoff is 4 if both prisoners confess, and 2 if both prisoners stay silent. Prisoner B's payoff is 4 if both prisoners confess, and 3 if both prisoners stay silent. Therefore, prisoner A prefers to confess if prisoner B stays silent, and prisoner B prefers to confess if prisoner A stays silent.

Using the concept of mixed strategies, we can represent the Nash equilibrium as follows:

|                 | Stay Silent | Confess    |
| --------------- | ----------- | ---------- |
| **Stay Silent** | (1/2, 1/2)  | (1/4, 3/4) |
| **Confess**     | (3/4, 1/4)  | (1/2, 1/2) |

In this representation, (p, q) represents the probability of staying silent or confessing. The Nash equilibrium is a mixed-strategy Nash equilibrium, where both players use a mixed strategy.

### Conclusion

In conclusion, the Nash equilibrium of an infinitely repeated Prisoner's dilemma is a mixed-strategy Nash equilibrium, where both prisoners use a mixed strategy. This equilibrium is a stable state where no player can improve their payoff by unilaterally changing their strategy, assuming the other player's strategy remains unchanged.
