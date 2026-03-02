# Finding Sub-Game Perfect Equilibria of Finite Horizon Games: Backward Induction

===========================================================

## Introduction

---

In game theory, a sub-game perfect equilibrium is a strategy profile that is optimal for every sub-game in a game of finite horizon. Backward induction is a method used to find these equilibria by recursively analyzing the sub-games from the last stage to the first.

## Definitions

---

- **Game of finite horizon**: A game with a finite number of stages, where each stage has a set of players and a set of actions for each player.
- **Sub-game**: A game that is a subset of the original game, where the players and actions are the same as the original game, but the stages may be reduced or modified.
- **Perfect equilibrium**: A strategy profile where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged.
- **Backward induction**: A method for finding perfect equilibria by recursively analyzing the sub-games from the last stage to the first.

## How Backward Induction Works

---

The backward induction method works as follows:

1.  **Identify the terminal stages**: Determine the stages in the game that have only one player left.
2.  **Find the optimal strategy for the last player**: Solve the game for the last stage, assuming that all other players have already made their optimal decisions.
3.  **Work backwards**: Analyze each subsequent stage, considering the optimal strategy of the previous player(s).
4.  **Iterate until the first stage**: Continue this process until the first stage is reached.

## Step-by-Step Example

---

Consider the following game:

|     | A     | B     |
| --- | ----- | ----- |
| 1   | (2,2) | (0,4) |
| 2   | (0,4) | (2,2) |

|     | A     | B     |
| --- | ----- | ----- |
| 3   | (3,3) | (1,1) |
| 4   | (1,1) | (3,3) |

|     | A     | B     |
| --- | ----- | ----- |
| 5   | (5,5) | (0,0) |

To find the sub-game perfect equilibrium using backward induction:

1.  **Identify the terminal stages**: The last stage is stage 5, where there is only one player left.
2.  **Find the optimal strategy for the last player**: In stage 5, the optimal strategy is to play (5,5), as it maximizes the payoff.
3.  **Work backwards**: In stage 4, the optimal strategy for player 2 is to play (0,0), as it maximizes the payoff, assuming player 1 plays (5,5).
4.  **Iterate until the first stage**: Continuing this process, we find that the optimal strategy for the first player is to play (2,2), and the optimal strategy for the second player is to play (0,4).

## Key Concepts

---

- **Rationality**: Players make decisions based on their rational self-interest.
- **Perfect equilibrium**: A strategy profile where no player can improve their payoff by unilaterally changing their strategy.
- ** backward induction**: A method for finding perfect equilibria by recursively analyzing the sub-games from the last stage to the first.
- **Strategic complementarity**: Players' strategies are interdependent, and a change in one player's strategy affects the optimal strategy for other players.

## Implementation

---

Backward induction can be implemented using various algorithms, such as:

- **Dynamic programming**: A method for solving optimization problems by breaking them down into smaller sub-problems.
- **Linear programming**: A method for solving optimization problems by finding the optimal solution among a set of linear constraints.
- **Game tree search**: A method for searching the game tree to find the optimal strategy for each player.

Note: This is a simplified example, and in real-world applications, the game tree can be very large, making it difficult to analyze and solve using backward induction.

## Conclusion

---

Backward induction is a powerful method for finding sub-game perfect equilibria of finite horizon games. By recursively analyzing the sub-games from the last stage to the first, we can find the optimal strategy for each player. This method assumes rationality and perfect information, and it can be used to analyze a wide range of games, from simple to complex.
