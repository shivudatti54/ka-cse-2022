# Repeated Games

**Introduction**

Repeated games are a fundamental concept in algorithmic game theory, which studies the strategic interactions between players in a series of games. In a repeated game, the same players meet at regular intervals, and each player can choose a strategy for each game. The goal is to design an optimal strategy that maximizes the player's payoff, considering both the current game and future games.

**Historical Context**

The concept of repeated games dates back to the 1940s, when John von Neumann and Oskar Morgenstern introduced the concept of "repeated games" in their book "Theory of Games and Economic Behavior." However, it wasn't until the 1960s that the idea gained significant attention, particularly in the work of John Harsanyi, who introduced the concept of "perfect Bayesian equilibrium" to study repeated games.

**Key Concepts**

Before diving into repeated games, let's define some key concepts:

- **Game**: A pair of players and a set of strategies for each player, where the goal is to maximize the payoff.
- **Game tree**: A diagram that represents the possible strategies and payoffs for each game.
- **Payoff**: The value assigned to each outcome, typically measured in terms of utility or profit.
- **Strategic form**: A mathematical representation of the game, where each player's strategy is represented by a probability distribution.
- **Nash equilibrium**: A stable state where no player can improve their payoff by unilaterally changing their strategy, assuming the other players keep their strategies unchanged.

**Repeated Games**

In a repeated game, players meet at regular intervals, and each player can choose a strategy for each game. The game is divided into a sequence of individual games, and the players' payoffs depend on the strategies chosen in each game.

**Types of Repeated Games**

There are several types of repeated games, including:

- **Zero-sum games**: The sum of the payoffs is constant, and one player's gain is equal to the other player's loss.
- **Non-zero-sum games**: The sum of the payoffs is not constant, and players can gain or lose simultaneously.
- **Dynamic games**: The game is played over an infinite horizon, and players can adjust their strategies based on past experiences.

**Examples**

- **Prisoner's Dilemma**: Two prisoners must decide whether to cooperate or betray each other. In the repeated game version, prisoners can choose to cooperate or defect in each game, and the payoffs depend on the previous game's outcome.
- **War of Attrition**: Two players engage in a repeated game of "tit-for-tat," where each player chooses a strategy based on the previous game's outcome.

**Applications**

Repeated games have numerous applications in various fields, including:

- **Economics**: Repeated games are used to study auctions, bargaining, and negotiations.
- **Politics**: Repeated games are used to model international relations, trade agreements, and elections.
- **Computer Science**: Repeated games are used to design algorithms for robotics, artificial intelligence, and machine learning.

**Diagram Description**

Here is a simple diagram representing a repeated game:

```
  +---------------+
  |  Player 1  |
  |  Strategy A  |
  |  Strategy B  |
  +---------------+
           |
           |
           v
  +---------------+
  |  Game 1  |
  |  Payoff (A, A) = 10  |
  |  Payoff (A, B) = 5  |
  |  Payoff (B, A) = 5  |
  |  Payoff (B, B) = 10  |
  +---------------+
           |
           |
           v
  +---------------+
  |  Player 1  |
  |  Strategy A  |
  |  Strategy B  |
  +---------------+
           |
           |
           v
  ...
```

In this diagram, Player 1 has two strategies, and the payoffs depend on the previous game's outcome. Player 2 chooses a strategy based on the previous game's outcome, and the game is repeated infinitely.

**Nash Equilibrium in Repeated Games**

In a repeated game, the Nash equilibrium is a stable state where no player can improve their payoff by unilaterally changing their strategy, assuming the other players keep their strategies unchanged. The Nash equilibrium can be found using the following conditions:

- **Self-interest**: Each player's strategy maximizes their individual payoff.
- **Cooperation**: Players cooperate in the game, assuming the other players will cooperate.
- **Rationality**: Players choose strategies based on their rational expectations of the other players' actions.

**Further Reading**

- von Neumann, J., & Morgenstern, O. (1944). Theory of games and economic behavior.
- Harsanyi, J. C. (1967). Games of imperfect information.
- Fudenberg, D., & Tirole, J. (1991). Game theory.
- Myerson, R. B. (1978). Perfect Bayesian equilibrium: The theory of games with incomplete information.

In conclusion, repeated games are a fundamental concept in algorithmic game theory, which studies the strategic interactions between players in a series of games. By understanding repeated games, we can design optimal strategies that maximize payoffs, considering both the current game and future games. The applications of repeated games are numerous, and it is an essential concept in various fields, including economics, politics, and computer science.
