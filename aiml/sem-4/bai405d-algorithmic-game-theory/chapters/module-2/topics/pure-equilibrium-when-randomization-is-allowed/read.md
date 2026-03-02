# **Pure Equilibrium when Randomization is Allowed**

## **Introduction**

In algorithmic game theory, a pure equilibrium is a strategy profile where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. However, in some strategic games, players may be allowed to randomize their actions. In these cases, the concept of pure equilibrium is extended to include mixed strategies.

## **Mixed Strategies and Randomization**

A mixed strategy is a probability distribution over a set of pure strategies. In other words, a player may choose to play a pure strategy with a certain probability, and a different pure strategy with a different probability.

## **Definition of Pure Equilibrium with Randomization**

A pure equilibrium with randomization is a strategy profile where no player can improve their expected payoff by changing their strategy, assuming all other players keep their strategies unchanged. More formally, a pure equilibrium with randomization is a tuple (σ1, σ2, ..., σn), where:

- σi is a probability distribution over a set of pure strategies for player i
- player i can improve their expected payoff by changing their strategy σi to σi'

**Key Concepts:**

- **Mixed strategy Nash equilibrium**: a pure equilibrium with randomization where no player can improve their expected payoff by changing their strategy.
- **Randomized strategy**: a strategy that involves playing a pure strategy with a certain probability and a different pure strategy with a different probability.
- **Expected payoff**: the average payoff that a player can expect to receive by playing a particular strategy.

**Examples:**

- **Prisoner's Dilemma**: consider two players, A and B, who can either confess or remain silent. Player A can improve their expected payoff by always confessing, regardless of what player B does. However, if both players confess, they both receive a low payoff. A mixed strategy equilibrium can be reached, where player A plays confess with a certain probability and remain silent with a different probability, and similarly for player B.
- **Rock-Paper-Scissors**: consider three players, Alice, Bob, and Charlie, who play Rock-Paper-Scissors. A mixed strategy equilibrium can be reached, where each player plays a particular rock-paper-scissors combination with a certain probability.

## **Algorithms for Computing Pure Equilibria with Randomization**

Several algorithms can be used to compute pure equilibria with randomization. Some of these algorithms include:

- **Bayesian Nash equilibrium**: an algorithm that computes mixed strategy Nash equilibria by assuming a Bayesian model of player behavior.
- **Robust Bayesian Nash equilibrium**: an algorithm that computes mixed strategy Nash equilibria in the presence of uncertainty about player behavior.
- **Newton-Raphson method**: an algorithm that iteratively improves a proposed mixed strategy equilibrium until it converges to a Nash equilibrium.

## **Conclusion**

Pure equilibrium with randomization is an extension of the concept of pure equilibrium to games where players may randomize their actions. Mixed strategies and expected payoffs play a crucial role in computing pure equilibria with randomization. Understanding pure equilibria with randomization is essential in algorithmic game theory, as it enables us to analyze and design strategic games in a more accurate and realistic way.
