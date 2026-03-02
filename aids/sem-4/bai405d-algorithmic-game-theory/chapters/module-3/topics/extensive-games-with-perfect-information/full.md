# **Extensive Games with Perfect Information**

## **Introduction**

In game theory, a game is considered extensive if it has a tree structure, where each player's decision node represents a point in time and has predecessors representing the previous moves made by the other players. In this module, we will delve into the world of extensive games with perfect information, where both players have complete knowledge of the game state and the actions available to them.

## **Definition**

An extensive game with perfect information is a game where both players have complete knowledge of the game state and the actions available to them at each decision node. This means that each player knows the current game state, the available actions, and the rules of the game. The game tree represents the possible sequences of moves that can be made, and each node in the tree corresponds to a decision made by a player.

## **Characteristics**

Extensive games with perfect information have the following characteristics:

- **Complete information**: Both players have complete knowledge of the game state and the actions available to them at each decision node.
- **Tree structure**: The game is represented as a tree, where each decision node represents a point in time and has predecessors representing the previous moves made by the other players.
- **Sequential decision making**: Players make decisions one after another, with each decision node representing a point in time.

## **Examples**

### 1. Chess

Chess is a classic example of an extensive game with perfect information. Both players have complete knowledge of the game state, including the position of all pieces, and the actions available to them at each decision node.

### 2. Tic-Tac-Toe

Tic-Tac-Toe is another example of an extensive game with perfect information. Both players have complete knowledge of the game state, including the position of all X's and O's, and the actions available to them at each decision node.

### 3. Go

Go is an ancient board game of East Asian origin that is also an extensive game with perfect information. Both players have complete knowledge of the game state, including the position of all stones, and the actions available to them at each decision node.

## **The Minimax Algorithm**

The Minimax algorithm is a recursive algorithm used to solve extensive games with perfect information. The algorithm works by recursively exploring the game tree, evaluating the possible outcomes at each decision node, and selecting the move that maximizes the expected outcome.

### Algorithm

1.  Initialize a value for the current node, such as 0 or infinity.
2.  If the current node is a terminal node, evaluate the outcome of the move made at that node and assign a value to it.
3.  If the current node is not a terminal node, recursively explore the child nodes, evaluating the possible outcomes at each decision node.
4.  At each child node, assign a value to it based on the outcome of the move made at that node.
5.  Select the move that maximizes the expected outcome.

### Example

Suppose we want to use the Minimax algorithm to play a game of Tic-Tac-Toe. We start at the root node, which represents the initial game state.

```
  1 | 2 | 3
  ---------
  4 | 5 | 6
  ---------
  7 | 8 | 9
```

We initialize the value of the root node to 0.

```
  1 | 2 | 3
  ---------
  4 | 5 | 6
  ---------
  7 | 8 | 9
  Value: 0
```

We recursively explore the child nodes, evaluating the possible outcomes at each decision node.

```
  Node 1: X (1)
  Node 2: O (2)
  Node 3: X (3)
  Node 4: O (4)
  Node 5: X (5)
  Node 6: O (6)
  Node 7: X (7)
  Node 8: O (8)
  Node 9: X (9)
```

We assign values to each node based on the outcome of the move made at that node.

```
  Node 1: X (1) = -1
  Node 2: O (2) = 1
  Node 3: X (3) = -1
  Node 4: O (4) = 1
  Node 5: X (5) = -1
  Node 6: O (6) = 1
  Node 7: X (7) = -1
  Node 8: O (8) = 1
  Node 9: X (9) = -1
```

We select the move that maximizes the expected outcome.

```
  Move: X (5)
  Value: 1
```

We update the value of the root node to 1.

```
  1 | 2 | 3
  ---------
  4 | X | 6
  ---------
  7 | 8 | 9
  Value: 1
```

We repeat the process until we reach a terminal node.

```
  Move: O (2)
  Value: -1
```

We update the value of the root node to -1.

```
  1 | O | 3
  ---------
  4 | X | 6
  ---------
  7 | 8 | 9
  Value: -1
```

The Minimax algorithm has selected the optimal move for the game of Tic-Tac-Toe.

## **Applications**

Extensive games with perfect information have numerous applications in various fields, including:

- **Artificial Intelligence**: The Minimax algorithm is widely used in AI to solve extensive games with perfect information.
- **Economics**: Extensive games are used to model economic decision-making, such as the allocation of resources.
- **Politics**: Extensive games are used to model political decision-making, such as the negotiation of treaties.
- **Biology**: Extensive games are used to model evolutionary decision-making, such as the evolution of species.

## **Historical Context**

The study of extensive games with perfect information dates back to the early 20th century. The Minimax algorithm was first developed by John Nash in the 1950s as a solution to the game of Tic-Tac-Toe. The algorithm was later generalized to solve extensive games with perfect information.

## **Modern Developments**

In recent years, there has been significant progress in the development of algorithms for solving extensive games with perfect information. Some notable developments include:

- **Monte Carlo Tree Search (MCTS)**: MCTS is a randomized algorithm that uses a tree search to evaluate the possible outcomes of a game.
- **Deep Learning**: Deep learning techniques, such as reinforcement learning and deep decision trees, have been used to solve extensive games with perfect information.
- **Game Theory**: Game theory has continued to evolve, with new models and techniques being developed to solve extensive games with perfect information.

## **Further Reading**

For further reading on extensive games with perfect information, we recommend the following resources:

- **"Game Theory" by Robert Gibbons**: This book provides a comprehensive introduction to game theory, including extensive games with perfect information.
- **"The Minimax Algorithm" by John Nash**: This paper provides a detailed explanation of the Minimax algorithm and its application to solving extensive games with perfect information.
- **"Monte Carlo Tree Search" by Richard Sutton**: This paper provides an introduction to MCTS and its application to solving extensive games with perfect information.
- **"Deep Learning for Game Playing" by DeepMind**: This paper provides an overview of deep learning techniques used to solve extensive games with perfect information.
