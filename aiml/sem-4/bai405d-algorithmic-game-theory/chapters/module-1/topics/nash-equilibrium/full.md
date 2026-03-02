# Nash Equilibrium

A fundamental concept in game theory, the Nash equilibrium is a stable state in a game where no player can improve their payoff (reward or penalty) by unilaterally changing their strategy, assuming all other players keep their strategies unchanged.

### Historical Context

The Nash equilibrium was first proposed by John Nash, an American mathematician and economist, in his 1950 paper "The Bargaining Problem." However, it was not until the 1960s that Nash's work gained widespread recognition, and the equilibrium became a cornerstone of modern game theory.

### Definition

A Nash equilibrium is a state in a game where no player can improve their payoff by changing their strategy, assuming all other players keep their strategies unchanged. In other words, a Nash equilibrium is a stable state where no player has an incentive to deviate from their chosen strategy.

Formally, a Nash equilibrium can be defined as follows:

Let G = (N, A, u) be a game, where:

- N is the set of players
- A is the set of strategies for each player
- u is the payoff function, which assigns a payoff to each player for each possible strategy combination

A Nash equilibrium is a strategy profile (s, s^(-1)) where:

- s is the strategy chosen by player i
- s^(-1) is the strategy chosen by all other players

For the strategy profile (s, s^(-1)) to be a Nash equilibrium, the following conditions must be satisfied:

- For each player i, u_i(s_i, s^(-1)) ≥ u_i(s_i', s^(-1)) for all s_i' in A_i (the set of possible strategies for player i)
- For each player i, u_i(s_i, s^(-1)) ≥ u_i(s_i, s^(-1)\_i') for all s^(-1)\_i' in S^(-1) (the set of possible strategy combinations for all other players)

### Examples

#### Example 1: The Prisoner's Dilemma

The Prisoner's Dilemma is a classic example of a game that illustrates the concept of Nash equilibrium. Two prisoners, A and B, are arrested and interrogated separately. Each prisoner has two possible strategies: to confess or to remain silent. The payoff matrix for this game is as follows:

|                               | Prisoner B remains silent | Prisoner B confesses |
| ----------------------------- | ------------------------- | -------------------- |
| **Prisoner A confesses**      | A: 0, B: 0                | A: 1, B: 1           |
| **Prisoner A remains silent** | A: 1, B: 0                | A: 0, B: 1           |

The Nash equilibrium for this game is (confess, confess), where both prisoners confess, resulting in a payoff of 1 for each prisoner.

#### Example 2: The Battle of the Sexes

The Battle of the Sexes is a game that models the behavior of two people with different preferences for attending a tennis match or a concert. The payoff matrix for this game is as follows:

|                                   | Attend tennis match | Attend concert |
| --------------------------------- | ------------------- | -------------- |
| **Person 1 attends tennis match** | P1: 2, P2: 2        | P1: 0, P2: 0   |
| **Person 1 attends concert**      | P1: 0, P2: 0        | P1: 1, P2: 1   |

The Nash equilibrium for this game is (attend tennis match, attend concert), where both people attend the event they prefer, resulting in a payoff of 2 for each person.

### Case Studies

#### Case Study 1: Oligopoly

An oligopoly is a market structure in which a small number of firms compete with each other. The Nash equilibrium in an oligopoly arises when each firm chooses a price that maximizes its profit, assuming the other firms keep their prices unchanged.

For example, suppose two firms, X and Y, compete in a market with demand P(q) = 100 - 0.5q, where q is the total quantity supplied. The production costs for each firm are constant at $100 per unit. The profit function for each firm is π(X) = P(q)q - 100q and π(Y) = P(q)q - 100q.

The Nash equilibrium for this game is when both firms produce at a quantity of 50 units, resulting in a price of $50 per unit.

#### Case Study 2: Auctions

Auctions are a classic example of a game where the Nash equilibrium arises in a single-round auction. In a single-round auction, each bidder has two possible strategies: to bid or not to bid.

The payoff matrix for a single-round auction is as follows:

|                           | Bid                      | Do not bid               |
| ------------------------- | ------------------------ | ------------------------ |
| **Bidder 1 bids**         | Bidder 1: 0, Bidder 2: 0 | Bidder 1: 1, Bidder 2: 1 |
| **Bidder 1 does not bid** | Bidder 1: 0, Bidder 2: 0 | Bidder 1: 1, Bidder 2: 1 |

The Nash equilibrium for this game is when both bidders do not bid, resulting in a payoff of 1 for each bidder.

### Applications

#### Application 1: Economics

The Nash equilibrium is a fundamental concept in economics, particularly in the study of oligopolies and auctions. It helps economists understand how firms and bidders make decisions in competitive markets.

#### Application 2: Politics

The Nash equilibrium is also used in politics to study the behavior of politicians and interest groups. It helps analysts understand how politicians make decisions about policy and how interest groups negotiate with policymakers.

#### Application 3: Computer Science

The Nash equilibrium is used in computer science to study the behavior of algorithms and artificial intelligence systems. It helps researchers understand how these systems make decisions and optimize their behavior.

### Modern Developments

In recent years, the Nash equilibrium has been generalized to more complex game situations, such as:

- **Repeated games**: Games where players make decisions multiple times, with the same set of players and strategies.
- **Asymmetric games**: Games where the players have different payoffs and strategies.
- **Evolutionary games**: Games where the players have different strategies and payoffs, and the game evolves over time.

These generalizations have led to the development of new concepts, such as the **fibrational Nash equilibrium**, which extends the Nash equilibrium to asymmetric games.

### Diagrams

#### Diagram 1: Payoff Matrix

A payoff matrix is a table that shows the payoffs for each player in a game. The rows represent the strategies of one player, and the columns represent the strategies of the other player.

|                | Strategy 1 | Strategy 2 |
| -------------- | ---------- | ---------- |
| **Strategy 1** | Payoff 1   | Payoff 2   |
| **Strategy 2** | Payoff 3   | Payoff 4   |

#### Diagram 2: Nash Equilibrium

A Nash equilibrium is a stable state in a game where no player can improve their payoff by changing their strategy, assuming all other players keep their strategies unchanged.

The Nash equilibrium is represented by a pair of strategies, where each strategy is a vector that represents the player's strategy in the game.

#### Diagram 3: Fibrational Nash Equilibrium

A fibrational Nash equilibrium is a generalization of the Nash equilibrium to asymmetric games. It is represented by a pair of strategies, where each strategy is a vector that represents the player's strategy in the game.

### Further Reading

- Nash, J. F. (1950). The Bargaining Problem. Econometrica, 18(2), 155-162.
- Nash, J. F. (1951). Non-Cooperative Games. Annals of Mathematics, 54(2), 286-305.
- Aumann, R. J. (1974). Subjective Probability and Expected Utility. Econometrica, 42(1), 1-33.

This is a basic overview of the Nash equilibrium.
