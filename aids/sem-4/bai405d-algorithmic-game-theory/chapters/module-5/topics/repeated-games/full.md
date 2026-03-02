# Repeated Games

## Introduction

Repeated games are a fundamental concept in algorithmic game theory, which studies strategic decision making in situations where the outcome depends on the actions of multiple players. In this topic, we will delve into the world of repeated games, exploring their definition, types, and applications.

### Historical Context

The concept of repeated games dates back to the 1950s, when mathematician John Nash introduced the concept of the "prisoner's dilemma," a classic example of a repeated game. Since then, repeated games have become a cornerstone of game theory, with applications in economics, politics, and computer science.

## Types of Repeated Games

There are several types of repeated games, which can be classified based on the number of periods, the structure of the games, and the reward functions.

### Periodic Games

Periodic games are repeated over a fixed number of periods, with the game resetting at the end of each period. This type of game is also known as a "finite horizon" game.

Example: A company that produces a product with a finite shelf life, where the company must decide whether to produce the product again at the end of the period or not.

### Infinite-Horizon Games

Infinite-horizon games, on the other hand, are repeated over an infinite number of periods, with the game not resetting at all. This type of game is also known as a "discounted infinite-horizon" game.

Example: A politician who must decide whether to support a policy that may have long-term benefits but also has short-term costs.

### Stochastic Games

Stochastic games are repeated games where the outcomes are random. This type of game is also known as a "stochastic process."

Example: A stock market where the prices are random and unpredictable.

## Applications of Repeated Games

Repeated games have numerous applications in various fields, including:

### Economics

Repeated games are used to model strategic decision making in economics, such as:

- **Oligopolies**: Companies compete with each other in a market, and the outcome depends on the actions of each company.
- **Monopolies**: A single company dominates the market, and the outcome depends on the company's actions.

### Politics

Repeated games are used to model strategic decision making in politics, such as:

- **International relations**: Countries interact with each other, and the outcome depends on the actions of each country.
- **Congressional politics**: Politicians interact with each other, and the outcome depends on the actions of each politician.

### Computer Science

Repeated games are used to model strategic decision making in computer science, such as:

- **Artificial intelligence**: AI systems interact with each other, and the outcome depends on the actions of each system.
- **Computer networks**: Devices interact with each other, and the outcome depends on the actions of each device.

## Game Trees and Strategies

In repeated games, players use game trees to represent the possible moves and outcomes. A game tree is a diagram that shows the possible moves and outcomes at each stage of the game.

Example:

Suppose we have a game where two players, Alice and Bob, take turns making moves. The game tree might look like this:

- Node 1: Alice makes a move (A)
  - Child node 1A: Alice makes another move (A), Bob loses
  - Child node 1B: Alice makes another move (B), Alice wins
- Node 2: Bob makes a move (B)
  - Child node 2A: Bob makes another move (A), Bob wins
  - Child node 2B: Bob makes another move (B), Alice wins

Players use strategies to make decisions in repeated games. A strategy is a set of rules that tell a player what to do in each situation.

Example:

Suppose Alice and Bob are playing a game where they take turns making moves. Alice's strategy might be to always make move A, while Bob's strategy might be to always make move B.

## Reputation and Signaling

In repeated games, players can use reputation and signaling to communicate information to each other.

Example:

Suppose Alice and Bob are playing a game where they take turns making moves. Alice can use her reputation to signal to Bob that she is a trustworthy player by always making move A. Bob can then adjust his strategy accordingly.

## Conclusion

Repeated games are a fundamental concept in algorithmic game theory, with numerous applications in economics, politics, and computer science. Understanding repeated games requires knowledge of game trees, strategies, reputation, and signaling. By mastering these concepts, you can develop a deeper understanding of strategic decision making in complex situations.

## Further Reading

- **"Game Theory" by John Nash**: A classic textbook on game theory that covers the basics of repeated games.
- **"Repeated Games" by Robert Aumann and Robert Myerson**: A comprehensive textbook on repeated games that covers the theory and applications.
- **"The Theory of Games and Economic Behavior" by John Nash**: A Nobel Prize-winning book that covers the basics of game theory and repeated games.

## Code Examples

Here are some code examples to illustrate the concepts of repeated games:

### Example 1: Simple Repeated Game

```python
import numpy as np

class Player:
    def __init__(self, name):
        self.name = name
        self.strategy = None

    def make_move(self, opponent_move):
        if self.strategy == 'always_A':
            return 'A'
        elif self.strategy == 'always_B':
            return 'B'
        else:
            raise ValueError('Invalid strategy')

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        player1_move = self.player1.make_move(self.player2.make_move('A'))
        player2_move = self.player2.make_move(self.player1.make_move('B'))
        return player1_move, player2_move

# Create players and game
player1 = Player('Alice')
player2 = Player('Bob')

# Set strategies
player1.strategy = 'always_A'
player2.strategy = 'always_B'

# Play game
game = Game(player1, player2)
player1_move, player2_move = game.play()
print(f'{player1.name} moves: {player1_move}')
print(f'{player2.name} moves: {player2_move}')
```

### Example 2: Stochastic Repeated Game

```python
import numpy as np

class Player:
    def __init__(self, name):
        self.name = name
        self.strategy = None

    def make_move(self, opponent_move):
        if self.strategy == 'always_A':
            return 'A'
        elif self.strategy == 'always_B':
            return 'B'
        else:
            raise ValueError('Invalid strategy')

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        player1_move = self.player1.make_move(np.random.choice(['A', 'B']))
        player2_move = self.player2.make_move(np.random.choice(['A', 'B']))
        return player1_move, player2_move

# Create players and game
player1 = Player('Alice')
player2 = Player('Bob')

# Set strategies
player1.strategy = 'always_A'
player2.strategy = 'always_B'

# Play game
game = Game(player1, player2)
player1_move, player2_move = game.play()
print(f'{player1.name} moves: {player1_move}')
print(f'{player2.name} moves: {player2_move}')
```

Note that these code examples are simplified and do not cover all the complexities of repeated games.
