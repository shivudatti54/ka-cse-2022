# Equilibrium in a Single Population

### Introduction

In Algorithmic Game Theory, equilibrium refers to a stable state where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. In this section, we will focus on equilibrium in a single population, where each player has the same set of strategies and the population is uniform.

### Definition of Equilibrium

Equilibrium in a single population is a state where no player can improve their payoff by changing their strategy, and all players are making the best decision given the strategies of the other players.

### Types of Equilibrium

There are several types of equilibrium, including:

- **Nash Equilibrium**: A Nash equilibrium is a state where no player can improve their payoff by unilaterally changing their strategy, and all players are making the best decision given the strategies of the other players.
- **Pareto Optimality**: A Pareto optimal state is a state where no player can improve their payoff without making another player worse off.

### Key Concepts

- **Strategy**: A strategy is a plan of action that a player can take in a game.
- **Payoff**: A payoff is the reward or penalty that a player receives for taking a particular action.
- **Mixed Strategy**: A mixed strategy is a strategy that involves randomizing between different actions.
- **Uniform Population**: A uniform population is a population where all players have the same set of strategies and the population is uniform.

### Examples

- **Prisoner's Dilemma**: In the prisoner's dilemma, two players have two possible strategies: confess or remain silent. The payoffs are as follows:

  | Strategy 1 (Player 1) | Strategy 2 (Player 1) | Payoff |
  | --------------------- | --------------------- | ------ |
  | Confess               | Confess               | -3, -3 |
  | Confess               | Remain Silent         | -3, 0  |
  | Remain Silent         | Confess               | 0, -3  |
  | Remain Silent         | Remain Silent         | 3, 3   |

  The Nash equilibrium in this game is for both players to confess.

- **Rock-Paper-Scissors**: In rock-paper-scissors, three players have three possible strategies: rock, paper, or scissors. The payoffs are as follows:

  | Strategy 1 (Player 1) | Strategy 2 (Player 1) | Payoff  |
  | --------------------- | --------------------- | ------- |
  | Rock                  | Rock                  | 0, 0, 0 |
  | Rock                  | Paper                 | 0, 0, 1 |
  | Paper                 | Rock                  | 0, 1, 0 |
  | Paper                 | Paper                 | 0, 1, 0 |
  | Scissors              | Rock                  | 1, 0, 0 |
  | Scissors              | Paper                 | 0, 1, 0 |
  | Scissors              | Scissors              | 0, 0, 1 |

  The Nash equilibrium in this game is for each player to choose a random strategy.

### Conclusion

Equilibrium in a single population is an important concept in algorithmic game theory, as it provides a framework for analyzing and designing games. By understanding equilibrium, we can better understand how players make decisions and how to design games that are fair and efficient.
