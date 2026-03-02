# Extensive Games with Perfect Information

=====================================

## Introduction

---

Extensive games are a class of games where the outcome of the game is determined by the sequence of moves made by the players. In this chapter, we will focus on extensive games with perfect information. In an extensive game with perfect information, both players have perfect knowledge of the game's state at each point in time, including the moves made by the other player.

## Historical Context

---

The concept of extensive games was first introduced by John von Neumann in the 1920s. However, it was not until the 1950s that the concept of perfect information extensive games was fully developed by John Nash and his colleagues.

## Definition

---

An extensive game with perfect information is a game where both players have complete knowledge of the game's state at each point in time, including the moves made by the other player. This means that both players can look ahead to the entire game tree and make decisions based on that information.

## Types of Extensive Games

---

There are several types of extensive games, including:

- **Zero-sum games**: In a zero-sum game, one player's gain is equal to the other player's loss. Examples include chess and checkers.
- **Non-zero-sum games**: In a non-zero-sum game, the total payoff is not zero. Examples include poker and business.
- **Sequential games**: In a sequential game, players make moves one at a time. Examples include chess and poker.
- **Simultaneous games**: In a simultaneous game, players make moves at the same time. Examples include auctions and bidding.

## Game Trees

---

A game tree is a mathematical representation of the game, where each node represents a state of the game and each edge represents a move. The game tree is used to analyze the game and make decisions.

### Diagrams

Here is a simple example of a game tree for a two-player game:

```
          +---------------+
          |             |
          |  Player 1  |
          |             |
          +---------------+
                  |
                  |
                  v
+-------------------------------+       +-------------------------------+
|                                  |       |                                  |
|  Player 1's Move 1          |       |  Player 2's Move 1          |
|  (A)                     |       |  (B)                     |
+-------------------------------+       +-------------------------------+
|                                  |       |                                  |
|  Player 1's Move 2          |       |  Player 2's Move 2          |
|  (C)                     |       |  (D)                     |
+-------------------------------+       +-------------------------------+
|                                  |       |                                  |
|  Player 1's Move 3          |       |  Player 2's Move 3          |
|  (E)                     |       |  (F)                     |
+-------------------------------+       +-------------------------------+
|                                  |       |                                  |
|  Player 1's Move 4          |       |  Player 2's Move 4          |
|  (G)                     |       |  (H)                     |
+-------------------------------+       +-------------------------------+
```

In this example, the game tree has four levels, representing four moves. Each node represents a state of the game, and each edge represents a move.

## Minimax Algorithm

---

The minimax algorithm is a recursive algorithm used to find the optimal move in an extensive game with perfect information. The algorithm works by minimizing the maximum payoff of the opponent.

### Algorithm

Here is a step-by-step explanation of the minimax algorithm:

1.  **Start at the root node**: Begin at the root node of the game tree.
2.  **Explore the game tree**: Explore the game tree, considering all possible moves.
3.  **Calculate the payoff**: Calculate the payoff for each possible move.
4.  **Recursively apply the algorithm**: Recursively apply the algorithm to each possible move.
5.  **Return the optimal move**: Return the optimal move, which is the move with the maximum payoff.

### Example

Here is an example of how the minimax algorithm would be applied to the game tree above:

```
          +---------------+
          |             |
          |  Player 1  |
          |             |
          +---------------+
                  |
                  |
                  v
+-------------------------------+       +-------------------------------+
|                                  |       |                                  |
|  Player 1's Move 1          |       |  Player 2's Move 1          |
|  (A)                     |       |  (B)                     |
+-------------------------------+       +-------------------------------+
|                                  |       |                                  |
|  Player 1's Move 2          |       |  Player 2's Move 2          |
|  (C)                     |       |  (D)                     |
+-------------------------------+       +-------------------------------+
|                                  |       |                                  |
|  Player 1's Move 3          |       |  Player 2's Move 3          |
|  (E)                     |       |  (F)                     |
+-------------------------------+       +-------------------------------+
|                                  |       |                                  |
|  Player 1's Move 4          |       |  Player 2's Move 4          |
|  (G)                     |       |  (H)                     |
+-------------------------------+       +-------------------------------+
```

In this example, the minimax algorithm would be applied as follows:

1.  **Start at the root node**: Begin at the root node of the game tree.
2.  **Explore the game tree**: Explore the game tree, considering all possible moves.
3.  **Calculate the payoff**: Calculate the payoff for each possible move.
4.  **Recursively apply the algorithm**: Recursively apply the algorithm to each possible move.
5.  **Return the optimal move**: Return the optimal move, which is the move with the maximum payoff.

### Code

Here is an example of how the minimax algorithm could be implemented in Python:

```python
def minimax(node, depth, is_maximizing):
    if depth == 0 or node.children == []:
        return node.payoff

    if is_maximizing:
        payoff = float('-inf')
        for child in node.children:
            payoff = max(payoff, minimax(child, depth-1, False))
        return payoff
    else:
        payoff = float('inf')
        for child in node.children:
            payoff = min(payoff, minimax(child, depth-1, True))
        return payoff
```

## Applications

---

Extensive games with perfect information have numerous applications in various fields, including:

- **Computer Science**: Extensive games are used in computer science to develop algorithms for decision-making, game theory, and artificial intelligence.
- **Economics**: Extensive games are used in economics to model real-world economic phenomena, such as auctions, bidding, and negotiations.
- **Politics**: Extensive games are used in politics to model strategic interactions between nations and political actors.
- **Business**: Extensive games are used in business to model strategic interactions between companies and to develop competitive strategies.

## Case Studies

---

Here are a few case studies that demonstrate the application of extensive games with perfect information:

- **Nash Equilibrium**: The Nash equilibrium is a concept in game theory that describes a stable state where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. The Nash equilibrium is a fundamental concept in extensive games with perfect information.
- **Prisoner's Dilemma**: The prisoner's dilemma is a classic example of an extensive game with perfect information. Two prisoners are given the opportunity to confess or remain silent. The optimal strategy for each prisoner is to confess, but if both prisoners confess, they both receive a lighter sentence. If one prisoner remains silent and the other confesses, the silent prisoner receives a harsher sentence. The Nash equilibrium in this game is (confess, confess).
- **Auction**: An auction is a type of extensive game where bidders make simultaneous bids. The objective is to determine the optimal bid strategy. The Vickrey-Clarke-Groves (VCG) auction is a classic example of an auction that uses the minimax algorithm to determine the optimal bid strategy.

## Further Reading

---

- **Game Theory**: Game theory is a branch of mathematics that studies strategic decision-making in situations where the outcome depends on the actions of multiple individuals or parties. Game theory is used to analyze and optimize strategic interactions in various fields, including economics, politics, and business.
- **Computer Science**: Computer science is a field of study that focuses on the design, development, and testing of computer systems and algorithms. Computer science is used to develop algorithms for decision-making, game theory, and artificial intelligence.
- **Economics**: Economics is a social science that studies the production, distribution, and consumption of goods and services. Economics is used to model real-world economic phenomena, such as auctions, bidding, and negotiations.

Recommended texts:

- **"Game Theory" by Martin Osborne**: This book provides a comprehensive introduction to game theory, covering topics such as strategic decision-making, Nash equilibrium, and auctions.
- **"Algorithms" by Robert Sedgewick and Kevin Wayne**: This book provides a comprehensive introduction to algorithms, covering topics such as sorting, searching, and graph algorithms.
- **"Economics" by Greg Mankiw**: This book provides a comprehensive introduction to economics, covering topics such as microeconomics, macroeconomics, and international trade.

## Conclusion

Extensive games with perfect information are a fundamental concept in game theory and have numerous applications in various fields. The minimax algorithm is a powerful tool for analyzing and optimizing strategic interactions in these games. The Nash equilibrium is a concept in game theory that describes a stable state where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. The prisoner's dilemma is a classic example of an extensive game with perfect information, and the Vickrey-Clarke-Groves (VCG) auction is a classic example of an auction that uses the minimax algorithm to determine the optimal bid strategy.
