# Extensive Games with Perfect Information

=====================================================

## Introduction

---

In algorithmic game theory, games with perfect information refer to situations where both players have complete knowledge of the game state, including the actions taken by their opponent. Extensive games are a specific type of game where the game state is divided into stages, and each stage represents a decision node. In this study material, we will focus on extensive games with perfect information.

## Definitions

---

- **Extensive Game**: A game where the game state is divided into stages, and each stage represents a decision node.
- **Perfect Information**: Both players have complete knowledge of the game state, including the actions taken by their opponent.

## Key Concepts

---

- **Game Tree**: A tree-like representation of the game state, where each node represents a decision node and the edges represent possible actions.
- **Path**: A sequence of nodes in the game tree, representing a possible sequence of actions.
- **Player's Value Function**: A function that assigns a value to each node in the game tree, representing the player's expected payoff.

### Subgames

- **Subgame**: A smaller game that is part of the larger game tree.
- **Backward Induction**: A method for solving extensive games by working backwards from the terminal nodes.

## Extensive Games with Perfect Information

---

### Game Tree Representation

In an extensive game with perfect information, the game tree represents the game state at each stage. Each node in the game tree represents a decision node, and the edges represent possible actions.

### Backward Induction

Backward induction is a method for solving extensive games by working backwards from the terminal nodes. The procedure is as follows:

1.  **Assign a value to the terminal nodes**: The terminal nodes represent the final payoffs, and they are assigned a value based on the game's payoff matrix.
2.  **Work backwards**: Starting from the terminal nodes, each node is assigned a value based on the values of its children.
3.  **Solve the subgames**: The subgames are solved recursively until the root node is reached.

### Zero-Sum and Non-Zero-Sum Games

- **Zero-Sum Games**: The sum of the payoffs is zero, and one player's gain is equal to the other player's loss.
- **Non-Zero-Sum Games**: The sum of the payoffs is not zero, and the players' payoffs can be different.

## Examples

---

### Example 1: The Prisoner's Dilemma

The Prisoner's Dilemma is a classic example of a zero-sum game.

|                        | Prisoner A stays | Prisoner A betrays |
| ---------------------- | ---------------- | ------------------ |
| **Prisoner B stays**   | A: 3, B: 3       | A: 0, B: 5         |
| **Prisoner B betrays** | A: 5, B: 0       | A: 1, B: 1         |

In this game, the prisoners' payoffs depend on the actions taken by both prisoners.

### Example 2: The Hawk-Dove Game

The Hawk-Dove Game is an example of a non-zero-sum game.

|          | Hawk (H)   | Dove (D)   |
| -------- | ---------- | ---------- |
| **Hawk** | H: 1, D: 0 | H: 0, D: 0 |
| **Dove** | H: 0, D: 1 | H: 0, D: 1 |

In this game, the payoffs depend on the actions taken by both players, and the sum of the payoffs is not zero.

## Conclusion

---

Extensive games with perfect information are a fundamental concept in algorithmic game theory. By using game trees and backward induction, we can solve these games and determine the optimal strategies for each player. The examples of the Prisoner's Dilemma and the Hawk-Dove Game illustrate the importance of considering the payoffs and the game tree structure when solving extensive games.

### Study Questions

1.  What is the difference between extensive games and extensive games with perfect information?
2.  How does backward induction work in solving extensive games?
3.  What is the difference between zero-sum games and non-zero-sum games?

### References

- Fudenberg, D., & Tirole, J. (1991). Game theory. MIT Press.
- von Neumann, J., & Morgenstern, O. (1944). Theory of games and economic behavior. Princeton University Press.
